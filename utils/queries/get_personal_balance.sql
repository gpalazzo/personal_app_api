select *
from personal_finances.balance
where
    cast(run_timestamp as date) = '{date}';
