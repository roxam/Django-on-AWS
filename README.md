# code-challenge

#to create db
create database `testapp` character set utf8 collate `utf8_unicode_ci`;# 1 row affected.

create user 'testapp'@'localhost' identified by 'test';# MySQL returned an empty result set (i.e. zero rows).

grant all privileges on testapp.* to 'testapp'@'localhost' 
   with grant option;# MySQL returned an empty result set (i.e. zero rows).

flush privileges;# MySQL returned an empty result set (i.e. zero rows).

