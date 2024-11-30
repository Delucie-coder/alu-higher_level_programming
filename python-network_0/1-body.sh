#!/bin/bash
# Script to send a GET request and display the body of the r
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
