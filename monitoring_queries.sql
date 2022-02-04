select
    s.event,
    s.program,
    count(*) as count
from
    gv$session s
where
    1=1
and wait_class <>'Idle'
group by
    s.event,
    s.program
/


select count(*) FROM aq_throughput_test_queue_tab;