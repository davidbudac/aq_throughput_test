-- populate the queue
declare
  l_enqueue_options     dbms_aq.enqueue_options_t;
  l_message_properties  dbms_aq.message_properties_t;
  l_message_handle      raw(16);
  payload_l             aq_throughput_test_type := aq_throughput_test_type('');
begin
    
    -- 1kB ascii string
    select rpad('*',1024,'*') into payload_l.payload
    from dual
    ;

    for i in 1..140000
    loop
        DBMS_AQ.enqueue(queue_name          => 'aq_throughput_test_queue',        
                        enqueue_options     => l_enqueue_options,     
                        message_properties  => l_message_properties,   
                        payload             => payload_l,             
                        msgid               => l_message_handle);
    end loop;

    commit;

exception when others then
    rollback;
    raise;
end;
/
