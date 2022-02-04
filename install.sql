create or replace type aq_throughput_test_type as object (
  payload varchar2(1024 byte)
);
/

execute dbms_aqadm.create_queue_table ( queue_table => 'aq_throughput_test_queue_tab',queue_payload_type => 'aq_throughput_test_type');
execute dbms_aqadm.create_queue ( queue_name => 'aq_throughput_test_queue', queue_table =>  'aq_throughput_test_queue_tab');
execute dbms_aqadm.start_queue ( queue_name => 'aq_throughput_test_queue', enqueue => true);