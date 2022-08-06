# Copyright (C) 2021-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class UnsafeClass:
    """
    Example of unsafe class design practices in Python.

    Specific issues are illustrated by the attributes
    and methods of this class.
    """

    def __init__(self):
        """Manually created __init__."""

        # Assigning value to self creates an instance attribute
        self.instance_attribute = 1

        # Assigning list attribute using []
        self.list_attribute = None