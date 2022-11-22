import os
import pathlib

# os.mkdir('/Users/ziweishi/Documents/coding/try1')

from pathlib import Path

Path('/Users/ziweishi/Documents/coding/').mkdir( parents=True, exist_ok=True )

os.rmdir('/Users/ziweishi/Documents/coding/')