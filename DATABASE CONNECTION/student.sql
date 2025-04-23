show databases;

create database python1;

use python1;
create table student( 
name varchar(20) , college varchar (20));

insert into student values
('situ','cu'),
('banty','ximb');

select * from student;