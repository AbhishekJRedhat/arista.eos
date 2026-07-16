# (c) 2026 Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_vrf
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule


class TestEosVrfModule(TestEosModule):
    module = eos_vrf

    def setUp(self):
        super(TestEosVrfModule, self).setUp()
        self.mock_map_config = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_vrf.map_config_to_obj",
        )
        self.map_config = self.mock_map_config.start()
        self.map_config.return_value = []

        self.mock_load_config = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_vrf.load_config",
        )
        self.load_config = self.mock_load_config.start()
        self.load_config.return_value = dict(diff=None, session="session")

    def tearDown(self):
        super(TestEosVrfModule, self).tearDown()
        self.mock_map_config.stop()
        self.mock_load_config.stop()

    def test_eos_vrf_present(self):
        set_module_args(dict(name="management", state="present"))
        result = self.execute_module(changed=True)
        self.assertTrue(result["changed"])
        self.assertNotIn("warnings", result)
