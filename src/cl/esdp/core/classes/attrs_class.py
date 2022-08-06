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

from attrs import define
from typing import Optional, List


@define
class AttrsClass:
    """
    Sample class for the attrs library.
    """

    instance_attribute: Optional[int] = None
    """Optional integer attribute."""

    list_attribute: List[int] = []
    """List attribute assigned an empty list by default."""

    def multiply_by_two(self) -> int:
        """
        Multiply int_param by 2 and return the result.
        """
        return self.int_param * 2