keywords-calculator
===================

A python server that, given a text, it calculates the related keywords

# Guide
1. Open a shell, and execute ./server.py 
2. Open an other shell and execute `curl -X POST -H "Content-Type: application/json" -d '{"text":"ola come stay"}' http://localhost:3010/keywords`
