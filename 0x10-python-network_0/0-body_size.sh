#!/bin/bash
# script that take in url, send a request and display the body
curl -sI $1 | grep -i 'content-length' | cut -d ' ' -f2
