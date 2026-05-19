#!/bin/bash
docker build --tag=web_why_lambda .
docker run -it -p 1337:1337 --rm --name=web_why_lambda web_why_lambda
