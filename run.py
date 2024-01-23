import os
import time

import pytest

from common.yaml_util import read_test_yaml

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
