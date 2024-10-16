# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DoctorFeeSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allowed_amount: float=None, base_price: float=None, billing_description: str=None, cash_price: float=None, code: str=None, code_type: str=None, cpt_hcpcs_modifier1: str=None, cpt_hcpcs_modifier2: str=None, cpt_hcpcs_modifier3: str=None, cpt_hcpcs_modifier4: str=None, created_at: str=None, description: str=None, doctor: int=None, id: int=None, insured_out_of_network_price: float=None, insured_price: float=None, ndc_code: str=None, ndc_quantity: float=None, ndc_units: str=None, office: int=None, payer_id: str=None, picklist_category: str=None, plan_name: str=None, updated_at: str=None):
        """DoctorFeeSchedule - a model defined in OpenAPI

        :param allowed_amount: The allowed_amount of this DoctorFeeSchedule.
        :param base_price: The base_price of this DoctorFeeSchedule.
        :param billing_description: The billing_description of this DoctorFeeSchedule.
        :param cash_price: The cash_price of this DoctorFeeSchedule.
        :param code: The code of this DoctorFeeSchedule.
        :param code_type: The code_type of this DoctorFeeSchedule.
        :param cpt_hcpcs_modifier1: The cpt_hcpcs_modifier1 of this DoctorFeeSchedule.
        :param cpt_hcpcs_modifier2: The cpt_hcpcs_modifier2 of this DoctorFeeSchedule.
        :param cpt_hcpcs_modifier3: The cpt_hcpcs_modifier3 of this DoctorFeeSchedule.
        :param cpt_hcpcs_modifier4: The cpt_hcpcs_modifier4 of this DoctorFeeSchedule.
        :param created_at: The created_at of this DoctorFeeSchedule.
        :param description: The description of this DoctorFeeSchedule.
        :param doctor: The doctor of this DoctorFeeSchedule.
        :param id: The id of this DoctorFeeSchedule.
        :param insured_out_of_network_price: The insured_out_of_network_price of this DoctorFeeSchedule.
        :param insured_price: The insured_price of this DoctorFeeSchedule.
        :param ndc_code: The ndc_code of this DoctorFeeSchedule.
        :param ndc_quantity: The ndc_quantity of this DoctorFeeSchedule.
        :param ndc_units: The ndc_units of this DoctorFeeSchedule.
        :param office: The office of this DoctorFeeSchedule.
        :param payer_id: The payer_id of this DoctorFeeSchedule.
        :param picklist_category: The picklist_category of this DoctorFeeSchedule.
        :param plan_name: The plan_name of this DoctorFeeSchedule.
        :param updated_at: The updated_at of this DoctorFeeSchedule.
        """
        self.openapi_types = {
            'allowed_amount': float,
            'base_price': float,
            'billing_description': str,
            'cash_price': float,
            'code': str,
            'code_type': str,
            'cpt_hcpcs_modifier1': str,
            'cpt_hcpcs_modifier2': str,
            'cpt_hcpcs_modifier3': str,
            'cpt_hcpcs_modifier4': str,
            'created_at': str,
            'description': str,
            'doctor': int,
            'id': int,
            'insured_out_of_network_price': float,
            'insured_price': float,
            'ndc_code': str,
            'ndc_quantity': float,
            'ndc_units': str,
            'office': int,
            'payer_id': str,
            'picklist_category': str,
            'plan_name': str,
            'updated_at': str
        }

        self.attribute_map = {
            'allowed_amount': 'allowed_amount',
            'base_price': 'base_price',
            'billing_description': 'billing_description',
            'cash_price': 'cash_price',
            'code': 'code',
            'code_type': 'code_type',
            'cpt_hcpcs_modifier1': 'cpt_hcpcs_modifier1',
            'cpt_hcpcs_modifier2': 'cpt_hcpcs_modifier2',
            'cpt_hcpcs_modifier3': 'cpt_hcpcs_modifier3',
            'cpt_hcpcs_modifier4': 'cpt_hcpcs_modifier4',
            'created_at': 'created_at',
            'description': 'description',
            'doctor': 'doctor',
            'id': 'id',
            'insured_out_of_network_price': 'insured_out_of_network_price',
            'insured_price': 'insured_price',
            'ndc_code': 'ndc_code',
            'ndc_quantity': 'ndc_quantity',
            'ndc_units': 'ndc_units',
            'office': 'office',
            'payer_id': 'payer_id',
            'picklist_category': 'picklist_category',
            'plan_name': 'plan_name',
            'updated_at': 'updated_at'
        }

        self._allowed_amount = allowed_amount
        self._base_price = base_price
        self._billing_description = billing_description
        self._cash_price = cash_price
        self._code = code
        self._code_type = code_type
        self._cpt_hcpcs_modifier1 = cpt_hcpcs_modifier1
        self._cpt_hcpcs_modifier2 = cpt_hcpcs_modifier2
        self._cpt_hcpcs_modifier3 = cpt_hcpcs_modifier3
        self._cpt_hcpcs_modifier4 = cpt_hcpcs_modifier4
        self._created_at = created_at
        self._description = description
        self._doctor = doctor
        self._id = id
        self._insured_out_of_network_price = insured_out_of_network_price
        self._insured_price = insured_price
        self._ndc_code = ndc_code
        self._ndc_quantity = ndc_quantity
        self._ndc_units = ndc_units
        self._office = office
        self._payer_id = payer_id
        self._picklist_category = picklist_category
        self._plan_name = plan_name
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DoctorFeeSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DoctorFeeSchedule of this DoctorFeeSchedule.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allowed_amount(self):
        """Gets the allowed_amount of this DoctorFeeSchedule.

        Typical allowed amount for payer. Not used if blank.

        :return: The allowed_amount of this DoctorFeeSchedule.
        :rtype: float
        """
        return self._allowed_amount

    @allowed_amount.setter
    def allowed_amount(self, allowed_amount):
        """Sets the allowed_amount of this DoctorFeeSchedule.

        Typical allowed amount for payer. Not used if blank.

        :param allowed_amount: The allowed_amount of this DoctorFeeSchedule.
        :type allowed_amount: float
        """

        self._allowed_amount = allowed_amount

    @property
    def base_price(self):
        """Gets the base_price of this DoctorFeeSchedule.

        

        :return: The base_price of this DoctorFeeSchedule.
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this DoctorFeeSchedule.

        

        :param base_price: The base_price of this DoctorFeeSchedule.
        :type base_price: float
        """

        self._base_price = base_price

    @property
    def billing_description(self):
        """Gets the billing_description of this DoctorFeeSchedule.

        

        :return: The billing_description of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._billing_description

    @billing_description.setter
    def billing_description(self, billing_description):
        """Sets the billing_description of this DoctorFeeSchedule.

        

        :param billing_description: The billing_description of this DoctorFeeSchedule.
        :type billing_description: str
        """

        self._billing_description = billing_description

    @property
    def cash_price(self):
        """Gets the cash_price of this DoctorFeeSchedule.

        

        :return: The cash_price of this DoctorFeeSchedule.
        :rtype: float
        """
        return self._cash_price

    @cash_price.setter
    def cash_price(self, cash_price):
        """Sets the cash_price of this DoctorFeeSchedule.

        

        :param cash_price: The cash_price of this DoctorFeeSchedule.
        :type cash_price: float
        """

        self._cash_price = cash_price

    @property
    def code(self):
        """Gets the code of this DoctorFeeSchedule.

        

        :return: The code of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DoctorFeeSchedule.

        

        :param code: The code of this DoctorFeeSchedule.
        :type code: str
        """

        self._code = code

    @property
    def code_type(self):
        """Gets the code_type of this DoctorFeeSchedule.

        

        :return: The code_type of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this DoctorFeeSchedule.

        

        :param code_type: The code_type of this DoctorFeeSchedule.
        :type code_type: str
        """
        allowed_values = ["CPT", "HCPCS", "Custom", "ICD9", "ICD10", "Revenue"]  # noqa: E501
        if code_type not in allowed_values:
            raise ValueError(
                "Invalid value for `code_type` ({0}), must be one of {1}"
                .format(code_type, allowed_values)
            )

        self._code_type = code_type

    @property
    def cpt_hcpcs_modifier1(self):
        """Gets the cpt_hcpcs_modifier1 of this DoctorFeeSchedule.

        

        :return: The cpt_hcpcs_modifier1 of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._cpt_hcpcs_modifier1

    @cpt_hcpcs_modifier1.setter
    def cpt_hcpcs_modifier1(self, cpt_hcpcs_modifier1):
        """Sets the cpt_hcpcs_modifier1 of this DoctorFeeSchedule.

        

        :param cpt_hcpcs_modifier1: The cpt_hcpcs_modifier1 of this DoctorFeeSchedule.
        :type cpt_hcpcs_modifier1: str
        """

        self._cpt_hcpcs_modifier1 = cpt_hcpcs_modifier1

    @property
    def cpt_hcpcs_modifier2(self):
        """Gets the cpt_hcpcs_modifier2 of this DoctorFeeSchedule.

        

        :return: The cpt_hcpcs_modifier2 of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._cpt_hcpcs_modifier2

    @cpt_hcpcs_modifier2.setter
    def cpt_hcpcs_modifier2(self, cpt_hcpcs_modifier2):
        """Sets the cpt_hcpcs_modifier2 of this DoctorFeeSchedule.

        

        :param cpt_hcpcs_modifier2: The cpt_hcpcs_modifier2 of this DoctorFeeSchedule.
        :type cpt_hcpcs_modifier2: str
        """
        allowed_values = ["", "17", "1D", "22", "23", "24", "25", "26", "29", "32", "33", "47", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "62", "63", "66", "73", "74", "76", "77", "78", "79", "80", "81", "82", "83", "90", "91", "92", "93", "95", "96", "97", "99", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AA", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AM", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BL", "BO", "BP", "BR", "BU", "CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CQ", "CR", "CS", "CT", "DA", "E1", "E2", "E3", "E4", "EA", "EB", "EC", "ED", "EE", "EJ", "EM", "EP", "ER", "ET", "EX", "EY", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "FA", "FB", "FC", "FP", "FX", "FY", "G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GQ", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY", "GZ", "H9", "HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ", "HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY", "HZ", "J1", "J2", "J3", "J4", "JA", "JB", "JC", "JD", "JE", "JF", "JG", "JW", "K0", "K1", "K2", "K3", "K4", "KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KI", "KJ", "KK", "KL", "KM", "KN", "KO", "KP", "KQ", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY", "KZ", "L1", "LC", "LD", "LL", "LM", "LR", "LS", "LT", "M2", "ME", "MI", "MR", "MS", "NB", "NH", "NM", "NR", "NU", "P1", "P2", "P3", "P4", "P5", "P6", "PA", "PB", "PC", "PD", "PE", "PI", "PL", "PM", "PN", "PO", "PS", "PT", "Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "QA", "QB", "QC", "QD", "QE", "QF", "QG", "QH", "QJ", "QK", "QL", "QM", "QN", "QP", "QQ", "QR", "QS", "QT", "QU", "QV", "QW", "QX", "QY", "QZ", "RA", "RB", "RC", "RD", "RE", "RI", "RP", "RR", "RT", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ", "SK", "SL", "SM", "SN", "SP", "SQ", "SS", "ST", "SU", "SV", "SW", "SY", "SZ", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "TA", "TB", "TC", "TD", "TE", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TP", "TQ", "TR", "TS", "TT", "TU", "TV", "TW", "TX", "U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "UA", "UB", "UC", "UD", "UE", "UF", "UG", "UH", "UJ", "UK", "UN", "UP", "UQ", "UR", "US", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VP", "VR", "W1", "W5", "W6", "W7", "W8", "W9", "WC", "WH", "WP", "X1", "X2", "X3", "X4", "X5", "XE", "XP", "XS", "XU", "VM", "ZA", "ZB", "ZL", "ZS", "1P", "2P", "3P", "8P"]  # noqa: E501
        if cpt_hcpcs_modifier2 not in allowed_values:
            raise ValueError(
                "Invalid value for `cpt_hcpcs_modifier2` ({0}), must be one of {1}"
                .format(cpt_hcpcs_modifier2, allowed_values)
            )

        self._cpt_hcpcs_modifier2 = cpt_hcpcs_modifier2

    @property
    def cpt_hcpcs_modifier3(self):
        """Gets the cpt_hcpcs_modifier3 of this DoctorFeeSchedule.

        

        :return: The cpt_hcpcs_modifier3 of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._cpt_hcpcs_modifier3

    @cpt_hcpcs_modifier3.setter
    def cpt_hcpcs_modifier3(self, cpt_hcpcs_modifier3):
        """Sets the cpt_hcpcs_modifier3 of this DoctorFeeSchedule.

        

        :param cpt_hcpcs_modifier3: The cpt_hcpcs_modifier3 of this DoctorFeeSchedule.
        :type cpt_hcpcs_modifier3: str
        """
        allowed_values = ["", "17", "1D", "22", "23", "24", "25", "26", "29", "32", "33", "47", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "62", "63", "66", "73", "74", "76", "77", "78", "79", "80", "81", "82", "83", "90", "91", "92", "93", "95", "96", "97", "99", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AA", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AM", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BL", "BO", "BP", "BR", "BU", "CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CQ", "CR", "CS", "CT", "DA", "E1", "E2", "E3", "E4", "EA", "EB", "EC", "ED", "EE", "EJ", "EM", "EP", "ER", "ET", "EX", "EY", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "FA", "FB", "FC", "FP", "FX", "FY", "G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GQ", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY", "GZ", "H9", "HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ", "HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY", "HZ", "J1", "J2", "J3", "J4", "JA", "JB", "JC", "JD", "JE", "JF", "JG", "JW", "K0", "K1", "K2", "K3", "K4", "KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KI", "KJ", "KK", "KL", "KM", "KN", "KO", "KP", "KQ", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY", "KZ", "L1", "LC", "LD", "LL", "LM", "LR", "LS", "LT", "M2", "ME", "MI", "MR", "MS", "NB", "NH", "NM", "NR", "NU", "P1", "P2", "P3", "P4", "P5", "P6", "PA", "PB", "PC", "PD", "PE", "PI", "PL", "PM", "PN", "PO", "PS", "PT", "Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "QA", "QB", "QC", "QD", "QE", "QF", "QG", "QH", "QJ", "QK", "QL", "QM", "QN", "QP", "QQ", "QR", "QS", "QT", "QU", "QV", "QW", "QX", "QY", "QZ", "RA", "RB", "RC", "RD", "RE", "RI", "RP", "RR", "RT", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ", "SK", "SL", "SM", "SN", "SP", "SQ", "SS", "ST", "SU", "SV", "SW", "SY", "SZ", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "TA", "TB", "TC", "TD", "TE", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TP", "TQ", "TR", "TS", "TT", "TU", "TV", "TW", "TX", "U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "UA", "UB", "UC", "UD", "UE", "UF", "UG", "UH", "UJ", "UK", "UN", "UP", "UQ", "UR", "US", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VP", "VR", "W1", "W5", "W6", "W7", "W8", "W9", "WC", "WH", "WP", "X1", "X2", "X3", "X4", "X5", "XE", "XP", "XS", "XU", "VM", "ZA", "ZB", "ZL", "ZS", "1P", "2P", "3P", "8P"]  # noqa: E501
        if cpt_hcpcs_modifier3 not in allowed_values:
            raise ValueError(
                "Invalid value for `cpt_hcpcs_modifier3` ({0}), must be one of {1}"
                .format(cpt_hcpcs_modifier3, allowed_values)
            )

        self._cpt_hcpcs_modifier3 = cpt_hcpcs_modifier3

    @property
    def cpt_hcpcs_modifier4(self):
        """Gets the cpt_hcpcs_modifier4 of this DoctorFeeSchedule.

        

        :return: The cpt_hcpcs_modifier4 of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._cpt_hcpcs_modifier4

    @cpt_hcpcs_modifier4.setter
    def cpt_hcpcs_modifier4(self, cpt_hcpcs_modifier4):
        """Sets the cpt_hcpcs_modifier4 of this DoctorFeeSchedule.

        

        :param cpt_hcpcs_modifier4: The cpt_hcpcs_modifier4 of this DoctorFeeSchedule.
        :type cpt_hcpcs_modifier4: str
        """
        allowed_values = ["", "17", "1D", "22", "23", "24", "25", "26", "29", "32", "33", "47", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "62", "63", "66", "73", "74", "76", "77", "78", "79", "80", "81", "82", "83", "90", "91", "92", "93", "95", "96", "97", "99", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AA", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AM", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BL", "BO", "BP", "BR", "BU", "CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CQ", "CR", "CS", "CT", "DA", "E1", "E2", "E3", "E4", "EA", "EB", "EC", "ED", "EE", "EJ", "EM", "EP", "ER", "ET", "EX", "EY", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "FA", "FB", "FC", "FP", "FX", "FY", "G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GQ", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY", "GZ", "H9", "HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ", "HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY", "HZ", "J1", "J2", "J3", "J4", "JA", "JB", "JC", "JD", "JE", "JF", "JG", "JW", "K0", "K1", "K2", "K3", "K4", "KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KI", "KJ", "KK", "KL", "KM", "KN", "KO", "KP", "KQ", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY", "KZ", "L1", "LC", "LD", "LL", "LM", "LR", "LS", "LT", "M2", "ME", "MI", "MR", "MS", "NB", "NH", "NM", "NR", "NU", "P1", "P2", "P3", "P4", "P5", "P6", "PA", "PB", "PC", "PD", "PE", "PI", "PL", "PM", "PN", "PO", "PS", "PT", "Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "QA", "QB", "QC", "QD", "QE", "QF", "QG", "QH", "QJ", "QK", "QL", "QM", "QN", "QP", "QQ", "QR", "QS", "QT", "QU", "QV", "QW", "QX", "QY", "QZ", "RA", "RB", "RC", "RD", "RE", "RI", "RP", "RR", "RT", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ", "SK", "SL", "SM", "SN", "SP", "SQ", "SS", "ST", "SU", "SV", "SW", "SY", "SZ", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "TA", "TB", "TC", "TD", "TE", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TP", "TQ", "TR", "TS", "TT", "TU", "TV", "TW", "TX", "U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "UA", "UB", "UC", "UD", "UE", "UF", "UG", "UH", "UJ", "UK", "UN", "UP", "UQ", "UR", "US", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VP", "VR", "W1", "W5", "W6", "W7", "W8", "W9", "WC", "WH", "WP", "X1", "X2", "X3", "X4", "X5", "XE", "XP", "XS", "XU", "VM", "ZA", "ZB", "ZL", "ZS", "1P", "2P", "3P", "8P"]  # noqa: E501
        if cpt_hcpcs_modifier4 not in allowed_values:
            raise ValueError(
                "Invalid value for `cpt_hcpcs_modifier4` ({0}), must be one of {1}"
                .format(cpt_hcpcs_modifier4, allowed_values)
            )

        self._cpt_hcpcs_modifier4 = cpt_hcpcs_modifier4

    @property
    def created_at(self):
        """Gets the created_at of this DoctorFeeSchedule.

        

        :return: The created_at of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DoctorFeeSchedule.

        

        :param created_at: The created_at of this DoctorFeeSchedule.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this DoctorFeeSchedule.

        

        :return: The description of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DoctorFeeSchedule.

        

        :param description: The description of this DoctorFeeSchedule.
        :type description: str
        """

        self._description = description

    @property
    def doctor(self):
        """Gets the doctor of this DoctorFeeSchedule.

        

        :return: The doctor of this DoctorFeeSchedule.
        :rtype: int
        """
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        """Sets the doctor of this DoctorFeeSchedule.

        

        :param doctor: The doctor of this DoctorFeeSchedule.
        :type doctor: int
        """

        self._doctor = doctor

    @property
    def id(self):
        """Gets the id of this DoctorFeeSchedule.

        

        :return: The id of this DoctorFeeSchedule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DoctorFeeSchedule.

        

        :param id: The id of this DoctorFeeSchedule.
        :type id: int
        """

        self._id = id

    @property
    def insured_out_of_network_price(self):
        """Gets the insured_out_of_network_price of this DoctorFeeSchedule.

        

        :return: The insured_out_of_network_price of this DoctorFeeSchedule.
        :rtype: float
        """
        return self._insured_out_of_network_price

    @insured_out_of_network_price.setter
    def insured_out_of_network_price(self, insured_out_of_network_price):
        """Sets the insured_out_of_network_price of this DoctorFeeSchedule.

        

        :param insured_out_of_network_price: The insured_out_of_network_price of this DoctorFeeSchedule.
        :type insured_out_of_network_price: float
        """

        self._insured_out_of_network_price = insured_out_of_network_price

    @property
    def insured_price(self):
        """Gets the insured_price of this DoctorFeeSchedule.

        

        :return: The insured_price of this DoctorFeeSchedule.
        :rtype: float
        """
        return self._insured_price

    @insured_price.setter
    def insured_price(self, insured_price):
        """Sets the insured_price of this DoctorFeeSchedule.

        

        :param insured_price: The insured_price of this DoctorFeeSchedule.
        :type insured_price: float
        """

        self._insured_price = insured_price

    @property
    def ndc_code(self):
        """Gets the ndc_code of this DoctorFeeSchedule.

        

        :return: The ndc_code of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._ndc_code

    @ndc_code.setter
    def ndc_code(self, ndc_code):
        """Sets the ndc_code of this DoctorFeeSchedule.

        

        :param ndc_code: The ndc_code of this DoctorFeeSchedule.
        :type ndc_code: str
        """

        self._ndc_code = ndc_code

    @property
    def ndc_quantity(self):
        """Gets the ndc_quantity of this DoctorFeeSchedule.

        

        :return: The ndc_quantity of this DoctorFeeSchedule.
        :rtype: float
        """
        return self._ndc_quantity

    @ndc_quantity.setter
    def ndc_quantity(self, ndc_quantity):
        """Sets the ndc_quantity of this DoctorFeeSchedule.

        

        :param ndc_quantity: The ndc_quantity of this DoctorFeeSchedule.
        :type ndc_quantity: float
        """

        self._ndc_quantity = ndc_quantity

    @property
    def ndc_units(self):
        """Gets the ndc_units of this DoctorFeeSchedule.

        

        :return: The ndc_units of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._ndc_units

    @ndc_units.setter
    def ndc_units(self, ndc_units):
        """Sets the ndc_units of this DoctorFeeSchedule.

        

        :param ndc_units: The ndc_units of this DoctorFeeSchedule.
        :type ndc_units: str
        """
        allowed_values = ["F2", "GR", "ME", "ML", "UN"]  # noqa: E501
        if ndc_units not in allowed_values:
            raise ValueError(
                "Invalid value for `ndc_units` ({0}), must be one of {1}"
                .format(ndc_units, allowed_values)
            )

        self._ndc_units = ndc_units

    @property
    def office(self):
        """Gets the office of this DoctorFeeSchedule.

        

        :return: The office of this DoctorFeeSchedule.
        :rtype: int
        """
        return self._office

    @office.setter
    def office(self, office):
        """Sets the office of this DoctorFeeSchedule.

        

        :param office: The office of this DoctorFeeSchedule.
        :type office: int
        """

        self._office = office

    @property
    def payer_id(self):
        """Gets the payer_id of this DoctorFeeSchedule.

        Fee Schedule pricing specific to this payer, if null, then applies as default to all payers without a more specific fee schedule.

        :return: The payer_id of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """Sets the payer_id of this DoctorFeeSchedule.

        Fee Schedule pricing specific to this payer, if null, then applies as default to all payers without a more specific fee schedule.

        :param payer_id: The payer_id of this DoctorFeeSchedule.
        :type payer_id: str
        """

        self._payer_id = payer_id

    @property
    def picklist_category(self):
        """Gets the picklist_category of this DoctorFeeSchedule.

        Optional: Category to organize the code into.

        :return: The picklist_category of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._picklist_category

    @picklist_category.setter
    def picklist_category(self, picklist_category):
        """Sets the picklist_category of this DoctorFeeSchedule.

        Optional: Category to organize the code into.

        :param picklist_category: The picklist_category of this DoctorFeeSchedule.
        :type picklist_category: str
        """

        self._picklist_category = picklist_category

    @property
    def plan_name(self):
        """Gets the plan_name of this DoctorFeeSchedule.

        Name of insurance plan.

        :return: The plan_name of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this DoctorFeeSchedule.

        Name of insurance plan.

        :param plan_name: The plan_name of this DoctorFeeSchedule.
        :type plan_name: str
        """

        self._plan_name = plan_name

    @property
    def updated_at(self):
        """Gets the updated_at of this DoctorFeeSchedule.

        

        :return: The updated_at of this DoctorFeeSchedule.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DoctorFeeSchedule.

        

        :param updated_at: The updated_at of this DoctorFeeSchedule.
        :type updated_at: str
        """

        self._updated_at = updated_at
