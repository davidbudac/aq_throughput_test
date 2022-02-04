### Install 
```sql
@install.sql
@populate_queue.sql
```
```bash
pip3 install cx_Oracle

python3 dequeue.py
```

### Results
[Local macbook linux VM database](https://public.tableau.com/views/AQdequeuetest-localVM/Throughputperthreadmessagespersec?:language=en-GB&:display_count=n&:origin=viz_share_link)

[Remote database server with 50ms latency](https://public.tableau.com/app/profile/davidbudac/viz/AQdequeuetest-remote/DequeueTime)

[Local infrastructure - database server](https://public.tableau.com/views/AQdequeuetest-localinfrastructure-databaseserver/Throughputperthreadmessagespersec?:language=en-GB&:display_count=n&:origin=viz_share_link)