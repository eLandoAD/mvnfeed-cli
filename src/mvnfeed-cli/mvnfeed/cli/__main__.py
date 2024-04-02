# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from .mvnfeed_cli import MvnFeedCLI

# https://stackoverflow.com/a/77834685
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

def main():
    try:
        mvnfeed_cli = MvnFeedCLI()
        exit_code = mvnfeed_cli.invoke(sys.argv[1:])
        sys.exit(exit_code)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
