"""_Custom script to upload data for the `{{cookiecutter.__project_name}}` pipeline_.

"""

from pathlib import Path, PurePosixPath

import pandas as pd
from djsciops import authentication as djsciops_authentication
from djsciops import settings as djsciops_settings
from djsciops.axon import upload_files
