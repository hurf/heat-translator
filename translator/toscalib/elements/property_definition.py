# vim: tabstop=4 shiftwidth=4 softtabstop=4

#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class PropertyDef(object):
    '''TOSCA built-in Property type.'''

    def __init__(self, name, value=None, schema=None):
        self.name = name
        self.value = value
        self.schema = schema

    @property
    def required(self):
        if self.schema:
            for prop_key, prop_vale in self.schema.items():
                if prop_key == 'required' and prop_vale:
                    return True
        return False
