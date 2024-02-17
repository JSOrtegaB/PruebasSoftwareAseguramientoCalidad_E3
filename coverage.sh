
#!/bin/bash
coverage run -m unittest discover -s test -p "*_test.py"
coverage report
coverage html


