# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CompanyOptionDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allow_entry_of_gross_price_in_invoicing: bool=None, credit_input_for_reverse_charge_vat: bool=None, credit_note_journal_ageing_name: str=None, credit_note_journal_ageing_value: int=None, discrepancy_allowed: float=None, enable_vocr_reporting: bool=None, margin_vat_scheme: bool=None, print_os_items_only: bool=None, purchases_vat_analysis_type: int=None, sales_vat_analysis_type: int=None, use_allocations: bool=None, use_nominal: bool=None, use_nominal_code: bool=None, vocr_setting_value: bool=None):
        """CompanyOptionDto - a model defined in OpenAPI

        :param allow_entry_of_gross_price_in_invoicing: The allow_entry_of_gross_price_in_invoicing of this CompanyOptionDto.
        :param credit_input_for_reverse_charge_vat: The credit_input_for_reverse_charge_vat of this CompanyOptionDto.
        :param credit_note_journal_ageing_name: The credit_note_journal_ageing_name of this CompanyOptionDto.
        :param credit_note_journal_ageing_value: The credit_note_journal_ageing_value of this CompanyOptionDto.
        :param discrepancy_allowed: The discrepancy_allowed of this CompanyOptionDto.
        :param enable_vocr_reporting: The enable_vocr_reporting of this CompanyOptionDto.
        :param margin_vat_scheme: The margin_vat_scheme of this CompanyOptionDto.
        :param print_os_items_only: The print_os_items_only of this CompanyOptionDto.
        :param purchases_vat_analysis_type: The purchases_vat_analysis_type of this CompanyOptionDto.
        :param sales_vat_analysis_type: The sales_vat_analysis_type of this CompanyOptionDto.
        :param use_allocations: The use_allocations of this CompanyOptionDto.
        :param use_nominal: The use_nominal of this CompanyOptionDto.
        :param use_nominal_code: The use_nominal_code of this CompanyOptionDto.
        :param vocr_setting_value: The vocr_setting_value of this CompanyOptionDto.
        """
        self.openapi_types = {
            'allow_entry_of_gross_price_in_invoicing': bool,
            'credit_input_for_reverse_charge_vat': bool,
            'credit_note_journal_ageing_name': str,
            'credit_note_journal_ageing_value': int,
            'discrepancy_allowed': float,
            'enable_vocr_reporting': bool,
            'margin_vat_scheme': bool,
            'print_os_items_only': bool,
            'purchases_vat_analysis_type': int,
            'sales_vat_analysis_type': int,
            'use_allocations': bool,
            'use_nominal': bool,
            'use_nominal_code': bool,
            'vocr_setting_value': bool
        }

        self.attribute_map = {
            'allow_entry_of_gross_price_in_invoicing': 'allowEntryOfGrossPriceInInvoicing',
            'credit_input_for_reverse_charge_vat': 'creditInputForReverseChargeVAT',
            'credit_note_journal_ageing_name': 'creditNoteJournalAgeingName',
            'credit_note_journal_ageing_value': 'creditNoteJournalAgeingValue',
            'discrepancy_allowed': 'discrepancyAllowed',
            'enable_vocr_reporting': 'enableVOCRReporting',
            'margin_vat_scheme': 'marginVatScheme',
            'print_os_items_only': 'printOSItemsOnly',
            'purchases_vat_analysis_type': 'purchasesVatAnalysisType',
            'sales_vat_analysis_type': 'salesVatAnalysisType',
            'use_allocations': 'useAllocations',
            'use_nominal': 'useNominal',
            'use_nominal_code': 'useNominalCode',
            'vocr_setting_value': 'vocrSettingValue'
        }

        self._allow_entry_of_gross_price_in_invoicing = allow_entry_of_gross_price_in_invoicing
        self._credit_input_for_reverse_charge_vat = credit_input_for_reverse_charge_vat
        self._credit_note_journal_ageing_name = credit_note_journal_ageing_name
        self._credit_note_journal_ageing_value = credit_note_journal_ageing_value
        self._discrepancy_allowed = discrepancy_allowed
        self._enable_vocr_reporting = enable_vocr_reporting
        self._margin_vat_scheme = margin_vat_scheme
        self._print_os_items_only = print_os_items_only
        self._purchases_vat_analysis_type = purchases_vat_analysis_type
        self._sales_vat_analysis_type = sales_vat_analysis_type
        self._use_allocations = use_allocations
        self._use_nominal = use_nominal
        self._use_nominal_code = use_nominal_code
        self._vocr_setting_value = vocr_setting_value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CompanyOptionDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CompanyOptionDto of this CompanyOptionDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allow_entry_of_gross_price_in_invoicing(self):
        """Gets the allow_entry_of_gross_price_in_invoicing of this CompanyOptionDto.


        :return: The allow_entry_of_gross_price_in_invoicing of this CompanyOptionDto.
        :rtype: bool
        """
        return self._allow_entry_of_gross_price_in_invoicing

    @allow_entry_of_gross_price_in_invoicing.setter
    def allow_entry_of_gross_price_in_invoicing(self, allow_entry_of_gross_price_in_invoicing):
        """Sets the allow_entry_of_gross_price_in_invoicing of this CompanyOptionDto.


        :param allow_entry_of_gross_price_in_invoicing: The allow_entry_of_gross_price_in_invoicing of this CompanyOptionDto.
        :type allow_entry_of_gross_price_in_invoicing: bool
        """

        self._allow_entry_of_gross_price_in_invoicing = allow_entry_of_gross_price_in_invoicing

    @property
    def credit_input_for_reverse_charge_vat(self):
        """Gets the credit_input_for_reverse_charge_vat of this CompanyOptionDto.


        :return: The credit_input_for_reverse_charge_vat of this CompanyOptionDto.
        :rtype: bool
        """
        return self._credit_input_for_reverse_charge_vat

    @credit_input_for_reverse_charge_vat.setter
    def credit_input_for_reverse_charge_vat(self, credit_input_for_reverse_charge_vat):
        """Sets the credit_input_for_reverse_charge_vat of this CompanyOptionDto.


        :param credit_input_for_reverse_charge_vat: The credit_input_for_reverse_charge_vat of this CompanyOptionDto.
        :type credit_input_for_reverse_charge_vat: bool
        """

        self._credit_input_for_reverse_charge_vat = credit_input_for_reverse_charge_vat

    @property
    def credit_note_journal_ageing_name(self):
        """Gets the credit_note_journal_ageing_name of this CompanyOptionDto.


        :return: The credit_note_journal_ageing_name of this CompanyOptionDto.
        :rtype: str
        """
        return self._credit_note_journal_ageing_name

    @credit_note_journal_ageing_name.setter
    def credit_note_journal_ageing_name(self, credit_note_journal_ageing_name):
        """Sets the credit_note_journal_ageing_name of this CompanyOptionDto.


        :param credit_note_journal_ageing_name: The credit_note_journal_ageing_name of this CompanyOptionDto.
        :type credit_note_journal_ageing_name: str
        """

        self._credit_note_journal_ageing_name = credit_note_journal_ageing_name

    @property
    def credit_note_journal_ageing_value(self):
        """Gets the credit_note_journal_ageing_value of this CompanyOptionDto.


        :return: The credit_note_journal_ageing_value of this CompanyOptionDto.
        :rtype: int
        """
        return self._credit_note_journal_ageing_value

    @credit_note_journal_ageing_value.setter
    def credit_note_journal_ageing_value(self, credit_note_journal_ageing_value):
        """Sets the credit_note_journal_ageing_value of this CompanyOptionDto.


        :param credit_note_journal_ageing_value: The credit_note_journal_ageing_value of this CompanyOptionDto.
        :type credit_note_journal_ageing_value: int
        """

        self._credit_note_journal_ageing_value = credit_note_journal_ageing_value

    @property
    def discrepancy_allowed(self):
        """Gets the discrepancy_allowed of this CompanyOptionDto.


        :return: The discrepancy_allowed of this CompanyOptionDto.
        :rtype: float
        """
        return self._discrepancy_allowed

    @discrepancy_allowed.setter
    def discrepancy_allowed(self, discrepancy_allowed):
        """Sets the discrepancy_allowed of this CompanyOptionDto.


        :param discrepancy_allowed: The discrepancy_allowed of this CompanyOptionDto.
        :type discrepancy_allowed: float
        """

        self._discrepancy_allowed = discrepancy_allowed

    @property
    def enable_vocr_reporting(self):
        """Gets the enable_vocr_reporting of this CompanyOptionDto.


        :return: The enable_vocr_reporting of this CompanyOptionDto.
        :rtype: bool
        """
        return self._enable_vocr_reporting

    @enable_vocr_reporting.setter
    def enable_vocr_reporting(self, enable_vocr_reporting):
        """Sets the enable_vocr_reporting of this CompanyOptionDto.


        :param enable_vocr_reporting: The enable_vocr_reporting of this CompanyOptionDto.
        :type enable_vocr_reporting: bool
        """

        self._enable_vocr_reporting = enable_vocr_reporting

    @property
    def margin_vat_scheme(self):
        """Gets the margin_vat_scheme of this CompanyOptionDto.


        :return: The margin_vat_scheme of this CompanyOptionDto.
        :rtype: bool
        """
        return self._margin_vat_scheme

    @margin_vat_scheme.setter
    def margin_vat_scheme(self, margin_vat_scheme):
        """Sets the margin_vat_scheme of this CompanyOptionDto.


        :param margin_vat_scheme: The margin_vat_scheme of this CompanyOptionDto.
        :type margin_vat_scheme: bool
        """

        self._margin_vat_scheme = margin_vat_scheme

    @property
    def print_os_items_only(self):
        """Gets the print_os_items_only of this CompanyOptionDto.


        :return: The print_os_items_only of this CompanyOptionDto.
        :rtype: bool
        """
        return self._print_os_items_only

    @print_os_items_only.setter
    def print_os_items_only(self, print_os_items_only):
        """Sets the print_os_items_only of this CompanyOptionDto.


        :param print_os_items_only: The print_os_items_only of this CompanyOptionDto.
        :type print_os_items_only: bool
        """

        self._print_os_items_only = print_os_items_only

    @property
    def purchases_vat_analysis_type(self):
        """Gets the purchases_vat_analysis_type of this CompanyOptionDto.


        :return: The purchases_vat_analysis_type of this CompanyOptionDto.
        :rtype: int
        """
        return self._purchases_vat_analysis_type

    @purchases_vat_analysis_type.setter
    def purchases_vat_analysis_type(self, purchases_vat_analysis_type):
        """Sets the purchases_vat_analysis_type of this CompanyOptionDto.


        :param purchases_vat_analysis_type: The purchases_vat_analysis_type of this CompanyOptionDto.
        :type purchases_vat_analysis_type: int
        """

        self._purchases_vat_analysis_type = purchases_vat_analysis_type

    @property
    def sales_vat_analysis_type(self):
        """Gets the sales_vat_analysis_type of this CompanyOptionDto.


        :return: The sales_vat_analysis_type of this CompanyOptionDto.
        :rtype: int
        """
        return self._sales_vat_analysis_type

    @sales_vat_analysis_type.setter
    def sales_vat_analysis_type(self, sales_vat_analysis_type):
        """Sets the sales_vat_analysis_type of this CompanyOptionDto.


        :param sales_vat_analysis_type: The sales_vat_analysis_type of this CompanyOptionDto.
        :type sales_vat_analysis_type: int
        """

        self._sales_vat_analysis_type = sales_vat_analysis_type

    @property
    def use_allocations(self):
        """Gets the use_allocations of this CompanyOptionDto.


        :return: The use_allocations of this CompanyOptionDto.
        :rtype: bool
        """
        return self._use_allocations

    @use_allocations.setter
    def use_allocations(self, use_allocations):
        """Sets the use_allocations of this CompanyOptionDto.


        :param use_allocations: The use_allocations of this CompanyOptionDto.
        :type use_allocations: bool
        """

        self._use_allocations = use_allocations

    @property
    def use_nominal(self):
        """Gets the use_nominal of this CompanyOptionDto.


        :return: The use_nominal of this CompanyOptionDto.
        :rtype: bool
        """
        return self._use_nominal

    @use_nominal.setter
    def use_nominal(self, use_nominal):
        """Sets the use_nominal of this CompanyOptionDto.


        :param use_nominal: The use_nominal of this CompanyOptionDto.
        :type use_nominal: bool
        """

        self._use_nominal = use_nominal

    @property
    def use_nominal_code(self):
        """Gets the use_nominal_code of this CompanyOptionDto.


        :return: The use_nominal_code of this CompanyOptionDto.
        :rtype: bool
        """
        return self._use_nominal_code

    @use_nominal_code.setter
    def use_nominal_code(self, use_nominal_code):
        """Sets the use_nominal_code of this CompanyOptionDto.


        :param use_nominal_code: The use_nominal_code of this CompanyOptionDto.
        :type use_nominal_code: bool
        """

        self._use_nominal_code = use_nominal_code

    @property
    def vocr_setting_value(self):
        """Gets the vocr_setting_value of this CompanyOptionDto.


        :return: The vocr_setting_value of this CompanyOptionDto.
        :rtype: bool
        """
        return self._vocr_setting_value

    @vocr_setting_value.setter
    def vocr_setting_value(self, vocr_setting_value):
        """Sets the vocr_setting_value of this CompanyOptionDto.


        :param vocr_setting_value: The vocr_setting_value of this CompanyOptionDto.
        :type vocr_setting_value: bool
        """

        self._vocr_setting_value = vocr_setting_value
