import cx_Oracle
import threading
from datetime import datetime
import time 
import logging

def dequeue_thread(id : int, conn : cx_Oracle.Connection):
    
    payload_type = conn.gettype("AQ_THROUGHPUT_TEST_TYPE")
    queue = conn.queue("AQ_THROUGHPUT_TEST_QUEUE", payload_type)
    queue.deqoptions.wait = cx_Oracle.DEQ_NO_WAIT # don't wait for messages if the queue is empty

    # dequeue messages and print the timestamps into CSVs for each thread
    with open(f'dequeue_thread_{id}.csv','w') as f:

        while True:
            startTime = time.perf_counter()            
            
            msg = queue.deqOne()
            conn.commit()
            
            endTime = time.perf_counter()
            
            f.write(f'"{datetime.now()}","{id}","{endTime - startTime:0.4f}"\n')

            if msg is None:
                logging.info(f"Thread {id} - queue empty, EXITING THREAD")
                break

def main():
    # configuration
    CONNECTIONSTRING = 'user/password@hostname:1521/service'
    THREADS = 21

    # logging formats
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")    

    # open connections (lazy man's connection pool)    
    logging.info("Opening connections..")
    connections = []
    for i in range(THREADS):
        conn = cx_Oracle.connect(CONNECTIONSTRING, encoding='UTF-8', nencoding='UTF-8')
        conn.module='DEQUEUE_TEST'
        connections.append(conn)

        logging.info ("Connection %d opened" % i)
    
    logging.info("..done")
    
    # start the treads
    logging.info("Starting threads..")
    threads = []
    for i in range(THREADS):
        threads.append( threading.Thread(target=dequeue_thread, args=(i,connections[i]), daemon=False))
        threads[i].start()
        logging.info("Thread %d started" % i)
    logging.info("..done")
    logging.info("All threads started - press CTRL-C to stop the program") 
    logging.info("All threads are now running until the queue is empty...")
    

if __name__ == '__main__':
    main()