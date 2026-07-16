# (c) 2026 Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_facts
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule


class TestEosFactsModule(TestEosModule):
    module = eos_facts

    def setUp(self):
        super(TestEosFactsModule, self).setUp()
        self.mock_get_facts = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_facts.Facts.get_facts",
        )
        self.get_facts = self.mock_get_facts.start()
        self.get_facts.return_value = ({}, [])

    def tearDown(self):
        super(TestEosFactsModule, self).tearDown()
        self.mock_get_facts.stop()

    def test_eos_facts_exit_emits_warnings(self):
        set_module_args(dict(gather_subset="min"))
        result = self.execute_module(changed=False)
        self.assertIn("ansible_facts", result)
        self.assertNotIn("warnings", result)
