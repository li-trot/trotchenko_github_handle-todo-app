# module required
import sys
import datetime

if __name__ == "__main__":
    TEXT = (
        """Command Line Todo application
=============================
    
Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task""")
    sys.stdout.buffer.write(TEXT.encode('utf8'))
