#!/bin/bash

mysql -u "$MYSQL_USERNAME" -p "$MYSQL_DATABASE"

source schema.sql

echo Hello world!

