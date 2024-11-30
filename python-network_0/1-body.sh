#!/bin/bash
# Script to send a GET request and display the body of the r
curl -sL -w "%{http_code}" "$1" -o response.txt | grep -q "200" && cat response.txt
