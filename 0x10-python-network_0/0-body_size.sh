#!/bin/bash
# sends a request an URL, and displays the size of the body of the response
curl -s "$1" | wc -c
