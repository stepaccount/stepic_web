#!/bin/bash

sudo /etc/init.d/mysql start
mysql -uroot -e "create database if not exists qadatabase"
mysql -uroot -e "create user megauser@localhost identified by 'megapass'"
mysql -uroot -e "grant all on qadatabase.* to megauser@localhost"
