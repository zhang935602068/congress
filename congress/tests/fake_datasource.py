# Copyright (c) 2015 OpenStack Foundation
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
#


from congress.datasources import datasource_driver
from congress.datasources import datasource_utils


def d6service(name, keys, inbox, datapath, args):
    """This method is called by d6cage to create a dataservice instance."""
    return FakeDataSource(name, keys, inbox, datapath, args)


class FakeDataSource(datasource_driver.DataSourceDriver):

    value_trans = {'translation-type': 'VALUE'}
    fake_translator = {
        'translation-type': 'HDICT',
        'table-name': 'fake_table',
        'selector-type': 'DICT_SELECTOR',
        'field-translators':
            ({'fieldname': 'id', 'translator': value_trans},
             {'fieldname': 'name', 'translator': value_trans})}

    TRANSLATORS = [fake_translator]

    def __init__(self, name='', keys='', inbox=None, datapath=None, args=None):
        super(FakeDataSource, self).__init__(name, keys, inbox,
                                             datapath, args)
        self.register_translator(FakeDataSource.fake_translator)
        self.initialized = True

    @staticmethod
    def get_datasource_info():
        result = {}
        result['id'] = 'fake_datasource'
        result['description'] = 'This is a fake driver used for testing'
        result['config'] = datasource_utils.get_openstack_required_config()
        return result
