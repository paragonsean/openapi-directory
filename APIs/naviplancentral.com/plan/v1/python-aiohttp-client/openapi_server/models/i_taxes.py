# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.currency import Currency
from openapi_server import util


class ITaxes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, estate: Currency=None, federal_income: Currency=None, gift_and_generation_skipping_transfer: Currency=None, medicare: Currency=None, pension_early_distribution_penalty: Currency=None, pension_penalty_on_excess_distributions: Currency=None, refundable_credits: Currency=None, social_security_employer: Currency=None, social_security_self_employed: Currency=None, state_income: Currency=None, total: Currency=None):
        """ITaxes - a model defined in OpenAPI

        :param estate: The estate of this ITaxes.
        :param federal_income: The federal_income of this ITaxes.
        :param gift_and_generation_skipping_transfer: The gift_and_generation_skipping_transfer of this ITaxes.
        :param medicare: The medicare of this ITaxes.
        :param pension_early_distribution_penalty: The pension_early_distribution_penalty of this ITaxes.
        :param pension_penalty_on_excess_distributions: The pension_penalty_on_excess_distributions of this ITaxes.
        :param refundable_credits: The refundable_credits of this ITaxes.
        :param social_security_employer: The social_security_employer of this ITaxes.
        :param social_security_self_employed: The social_security_self_employed of this ITaxes.
        :param state_income: The state_income of this ITaxes.
        :param total: The total of this ITaxes.
        """
        self.openapi_types = {
            'estate': Currency,
            'federal_income': Currency,
            'gift_and_generation_skipping_transfer': Currency,
            'medicare': Currency,
            'pension_early_distribution_penalty': Currency,
            'pension_penalty_on_excess_distributions': Currency,
            'refundable_credits': Currency,
            'social_security_employer': Currency,
            'social_security_self_employed': Currency,
            'state_income': Currency,
            'total': Currency
        }

        self.attribute_map = {
            'estate': 'estate',
            'federal_income': 'federalIncome',
            'gift_and_generation_skipping_transfer': 'giftAndGenerationSkippingTransfer',
            'medicare': 'medicare',
            'pension_early_distribution_penalty': 'pensionEarlyDistributionPenalty',
            'pension_penalty_on_excess_distributions': 'pensionPenaltyOnExcessDistributions',
            'refundable_credits': 'refundableCredits',
            'social_security_employer': 'socialSecurityEmployer',
            'social_security_self_employed': 'socialSecuritySelfEmployed',
            'state_income': 'stateIncome',
            'total': 'total'
        }

        self._estate = estate
        self._federal_income = federal_income
        self._gift_and_generation_skipping_transfer = gift_and_generation_skipping_transfer
        self._medicare = medicare
        self._pension_early_distribution_penalty = pension_early_distribution_penalty
        self._pension_penalty_on_excess_distributions = pension_penalty_on_excess_distributions
        self._refundable_credits = refundable_credits
        self._social_security_employer = social_security_employer
        self._social_security_self_employed = social_security_self_employed
        self._state_income = state_income
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ITaxes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ITaxes of this ITaxes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def estate(self):
        """Gets the estate of this ITaxes.


        :return: The estate of this ITaxes.
        :rtype: Currency
        """
        return self._estate

    @estate.setter
    def estate(self, estate):
        """Sets the estate of this ITaxes.


        :param estate: The estate of this ITaxes.
        :type estate: Currency
        """

        self._estate = estate

    @property
    def federal_income(self):
        """Gets the federal_income of this ITaxes.


        :return: The federal_income of this ITaxes.
        :rtype: Currency
        """
        return self._federal_income

    @federal_income.setter
    def federal_income(self, federal_income):
        """Sets the federal_income of this ITaxes.


        :param federal_income: The federal_income of this ITaxes.
        :type federal_income: Currency
        """

        self._federal_income = federal_income

    @property
    def gift_and_generation_skipping_transfer(self):
        """Gets the gift_and_generation_skipping_transfer of this ITaxes.


        :return: The gift_and_generation_skipping_transfer of this ITaxes.
        :rtype: Currency
        """
        return self._gift_and_generation_skipping_transfer

    @gift_and_generation_skipping_transfer.setter
    def gift_and_generation_skipping_transfer(self, gift_and_generation_skipping_transfer):
        """Sets the gift_and_generation_skipping_transfer of this ITaxes.


        :param gift_and_generation_skipping_transfer: The gift_and_generation_skipping_transfer of this ITaxes.
        :type gift_and_generation_skipping_transfer: Currency
        """

        self._gift_and_generation_skipping_transfer = gift_and_generation_skipping_transfer

    @property
    def medicare(self):
        """Gets the medicare of this ITaxes.


        :return: The medicare of this ITaxes.
        :rtype: Currency
        """
        return self._medicare

    @medicare.setter
    def medicare(self, medicare):
        """Sets the medicare of this ITaxes.


        :param medicare: The medicare of this ITaxes.
        :type medicare: Currency
        """

        self._medicare = medicare

    @property
    def pension_early_distribution_penalty(self):
        """Gets the pension_early_distribution_penalty of this ITaxes.


        :return: The pension_early_distribution_penalty of this ITaxes.
        :rtype: Currency
        """
        return self._pension_early_distribution_penalty

    @pension_early_distribution_penalty.setter
    def pension_early_distribution_penalty(self, pension_early_distribution_penalty):
        """Sets the pension_early_distribution_penalty of this ITaxes.


        :param pension_early_distribution_penalty: The pension_early_distribution_penalty of this ITaxes.
        :type pension_early_distribution_penalty: Currency
        """

        self._pension_early_distribution_penalty = pension_early_distribution_penalty

    @property
    def pension_penalty_on_excess_distributions(self):
        """Gets the pension_penalty_on_excess_distributions of this ITaxes.


        :return: The pension_penalty_on_excess_distributions of this ITaxes.
        :rtype: Currency
        """
        return self._pension_penalty_on_excess_distributions

    @pension_penalty_on_excess_distributions.setter
    def pension_penalty_on_excess_distributions(self, pension_penalty_on_excess_distributions):
        """Sets the pension_penalty_on_excess_distributions of this ITaxes.


        :param pension_penalty_on_excess_distributions: The pension_penalty_on_excess_distributions of this ITaxes.
        :type pension_penalty_on_excess_distributions: Currency
        """

        self._pension_penalty_on_excess_distributions = pension_penalty_on_excess_distributions

    @property
    def refundable_credits(self):
        """Gets the refundable_credits of this ITaxes.


        :return: The refundable_credits of this ITaxes.
        :rtype: Currency
        """
        return self._refundable_credits

    @refundable_credits.setter
    def refundable_credits(self, refundable_credits):
        """Sets the refundable_credits of this ITaxes.


        :param refundable_credits: The refundable_credits of this ITaxes.
        :type refundable_credits: Currency
        """

        self._refundable_credits = refundable_credits

    @property
    def social_security_employer(self):
        """Gets the social_security_employer of this ITaxes.


        :return: The social_security_employer of this ITaxes.
        :rtype: Currency
        """
        return self._social_security_employer

    @social_security_employer.setter
    def social_security_employer(self, social_security_employer):
        """Sets the social_security_employer of this ITaxes.


        :param social_security_employer: The social_security_employer of this ITaxes.
        :type social_security_employer: Currency
        """

        self._social_security_employer = social_security_employer

    @property
    def social_security_self_employed(self):
        """Gets the social_security_self_employed of this ITaxes.


        :return: The social_security_self_employed of this ITaxes.
        :rtype: Currency
        """
        return self._social_security_self_employed

    @social_security_self_employed.setter
    def social_security_self_employed(self, social_security_self_employed):
        """Sets the social_security_self_employed of this ITaxes.


        :param social_security_self_employed: The social_security_self_employed of this ITaxes.
        :type social_security_self_employed: Currency
        """

        self._social_security_self_employed = social_security_self_employed

    @property
    def state_income(self):
        """Gets the state_income of this ITaxes.


        :return: The state_income of this ITaxes.
        :rtype: Currency
        """
        return self._state_income

    @state_income.setter
    def state_income(self, state_income):
        """Sets the state_income of this ITaxes.


        :param state_income: The state_income of this ITaxes.
        :type state_income: Currency
        """

        self._state_income = state_income

    @property
    def total(self):
        """Gets the total of this ITaxes.


        :return: The total of this ITaxes.
        :rtype: Currency
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ITaxes.


        :param total: The total of this ITaxes.
        :type total: Currency
        """

        self._total = total
