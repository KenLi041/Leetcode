# Write your MySQL query statement below

select(select salary from employee 
    group by #must both group and order by salary
        salary
    order by
        salary
    desc 
    limit 1,1) #return n-1 element so second highest is limit 1, 1
as SecondHighestSalary;
