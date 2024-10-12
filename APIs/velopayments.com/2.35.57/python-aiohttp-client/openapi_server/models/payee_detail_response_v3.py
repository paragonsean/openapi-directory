# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.challenge_v3 import ChallengeV3
from openapi_server.models.company_v3 import CompanyV3
from openapi_server.models.individual_v3 import IndividualV3
from openapi_server.models.payee_address_v3 import PayeeAddressV3
from openapi_server.models.payee_payor_ref_v3 import PayeePayorRefV3
import re
from openapi_server import util


class PayeeDetailResponseV3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accept_terms_and_conditions_timestamp: datetime=None, address: PayeeAddressV3=None, cellphone_number: str=None, challenge: ChallengeV3=None, company: CompanyV3=None, country: str=None, created: datetime=None, disabled: bool=None, disabled_comment: str=None, disabled_updated_timestamp: datetime=None, display_name: str=None, email: str=None, enhanced_kyc_completed: bool=None, grace_period_end_date: date=None, individual: IndividualV3=None, kyc_completed_timestamp: str=None, language: str=None, marketing_opt_in_decision: bool=None, marketing_opt_in_timestamp: str=None, onboarded_status: str=None, pause_payment: bool=None, pause_payment_timestamp: str=None, payee_id: str=None, payee_type: str=None, payor_refs: List[PayeePayorRefV3]=None, watchlist_override_comment: str=None, watchlist_override_expires_at_timestamp: datetime=None, watchlist_status: str=None, watchlist_status_updated_timestamp: str=None):
        """PayeeDetailResponseV3 - a model defined in OpenAPI

        :param accept_terms_and_conditions_timestamp: The accept_terms_and_conditions_timestamp of this PayeeDetailResponseV3.
        :param address: The address of this PayeeDetailResponseV3.
        :param cellphone_number: The cellphone_number of this PayeeDetailResponseV3.
        :param challenge: The challenge of this PayeeDetailResponseV3.
        :param company: The company of this PayeeDetailResponseV3.
        :param country: The country of this PayeeDetailResponseV3.
        :param created: The created of this PayeeDetailResponseV3.
        :param disabled: The disabled of this PayeeDetailResponseV3.
        :param disabled_comment: The disabled_comment of this PayeeDetailResponseV3.
        :param disabled_updated_timestamp: The disabled_updated_timestamp of this PayeeDetailResponseV3.
        :param display_name: The display_name of this PayeeDetailResponseV3.
        :param email: The email of this PayeeDetailResponseV3.
        :param enhanced_kyc_completed: The enhanced_kyc_completed of this PayeeDetailResponseV3.
        :param grace_period_end_date: The grace_period_end_date of this PayeeDetailResponseV3.
        :param individual: The individual of this PayeeDetailResponseV3.
        :param kyc_completed_timestamp: The kyc_completed_timestamp of this PayeeDetailResponseV3.
        :param language: The language of this PayeeDetailResponseV3.
        :param marketing_opt_in_decision: The marketing_opt_in_decision of this PayeeDetailResponseV3.
        :param marketing_opt_in_timestamp: The marketing_opt_in_timestamp of this PayeeDetailResponseV3.
        :param onboarded_status: The onboarded_status of this PayeeDetailResponseV3.
        :param pause_payment: The pause_payment of this PayeeDetailResponseV3.
        :param pause_payment_timestamp: The pause_payment_timestamp of this PayeeDetailResponseV3.
        :param payee_id: The payee_id of this PayeeDetailResponseV3.
        :param payee_type: The payee_type of this PayeeDetailResponseV3.
        :param payor_refs: The payor_refs of this PayeeDetailResponseV3.
        :param watchlist_override_comment: The watchlist_override_comment of this PayeeDetailResponseV3.
        :param watchlist_override_expires_at_timestamp: The watchlist_override_expires_at_timestamp of this PayeeDetailResponseV3.
        :param watchlist_status: The watchlist_status of this PayeeDetailResponseV3.
        :param watchlist_status_updated_timestamp: The watchlist_status_updated_timestamp of this PayeeDetailResponseV3.
        """
        self.openapi_types = {
            'accept_terms_and_conditions_timestamp': datetime,
            'address': PayeeAddressV3,
            'cellphone_number': str,
            'challenge': ChallengeV3,
            'company': CompanyV3,
            'country': str,
            'created': datetime,
            'disabled': bool,
            'disabled_comment': str,
            'disabled_updated_timestamp': datetime,
            'display_name': str,
            'email': str,
            'enhanced_kyc_completed': bool,
            'grace_period_end_date': date,
            'individual': IndividualV3,
            'kyc_completed_timestamp': str,
            'language': str,
            'marketing_opt_in_decision': bool,
            'marketing_opt_in_timestamp': str,
            'onboarded_status': str,
            'pause_payment': bool,
            'pause_payment_timestamp': str,
            'payee_id': str,
            'payee_type': str,
            'payor_refs': List[PayeePayorRefV3],
            'watchlist_override_comment': str,
            'watchlist_override_expires_at_timestamp': datetime,
            'watchlist_status': str,
            'watchlist_status_updated_timestamp': str
        }

        self.attribute_map = {
            'accept_terms_and_conditions_timestamp': 'acceptTermsAndConditionsTimestamp',
            'address': 'address',
            'cellphone_number': 'cellphoneNumber',
            'challenge': 'challenge',
            'company': 'company',
            'country': 'country',
            'created': 'created',
            'disabled': 'disabled',
            'disabled_comment': 'disabledComment',
            'disabled_updated_timestamp': 'disabledUpdatedTimestamp',
            'display_name': 'displayName',
            'email': 'email',
            'enhanced_kyc_completed': 'enhancedKycCompleted',
            'grace_period_end_date': 'gracePeriodEndDate',
            'individual': 'individual',
            'kyc_completed_timestamp': 'kycCompletedTimestamp',
            'language': 'language',
            'marketing_opt_in_decision': 'marketingOptInDecision',
            'marketing_opt_in_timestamp': 'marketingOptInTimestamp',
            'onboarded_status': 'onboardedStatus',
            'pause_payment': 'pausePayment',
            'pause_payment_timestamp': 'pausePaymentTimestamp',
            'payee_id': 'payeeId',
            'payee_type': 'payeeType',
            'payor_refs': 'payorRefs',
            'watchlist_override_comment': 'watchlistOverrideComment',
            'watchlist_override_expires_at_timestamp': 'watchlistOverrideExpiresAtTimestamp',
            'watchlist_status': 'watchlistStatus',
            'watchlist_status_updated_timestamp': 'watchlistStatusUpdatedTimestamp'
        }

        self._accept_terms_and_conditions_timestamp = accept_terms_and_conditions_timestamp
        self._address = address
        self._cellphone_number = cellphone_number
        self._challenge = challenge
        self._company = company
        self._country = country
        self._created = created
        self._disabled = disabled
        self._disabled_comment = disabled_comment
        self._disabled_updated_timestamp = disabled_updated_timestamp
        self._display_name = display_name
        self._email = email
        self._enhanced_kyc_completed = enhanced_kyc_completed
        self._grace_period_end_date = grace_period_end_date
        self._individual = individual
        self._kyc_completed_timestamp = kyc_completed_timestamp
        self._language = language
        self._marketing_opt_in_decision = marketing_opt_in_decision
        self._marketing_opt_in_timestamp = marketing_opt_in_timestamp
        self._onboarded_status = onboarded_status
        self._pause_payment = pause_payment
        self._pause_payment_timestamp = pause_payment_timestamp
        self._payee_id = payee_id
        self._payee_type = payee_type
        self._payor_refs = payor_refs
        self._watchlist_override_comment = watchlist_override_comment
        self._watchlist_override_expires_at_timestamp = watchlist_override_expires_at_timestamp
        self._watchlist_status = watchlist_status
        self._watchlist_status_updated_timestamp = watchlist_status_updated_timestamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PayeeDetailResponseV3':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PayeeDetailResponseV3 of this PayeeDetailResponseV3.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accept_terms_and_conditions_timestamp(self):
        """Gets the accept_terms_and_conditions_timestamp of this PayeeDetailResponseV3.

        The timestamp when the payee last accepted T&Cs

        :return: The accept_terms_and_conditions_timestamp of this PayeeDetailResponseV3.
        :rtype: datetime
        """
        return self._accept_terms_and_conditions_timestamp

    @accept_terms_and_conditions_timestamp.setter
    def accept_terms_and_conditions_timestamp(self, accept_terms_and_conditions_timestamp):
        """Sets the accept_terms_and_conditions_timestamp of this PayeeDetailResponseV3.

        The timestamp when the payee last accepted T&Cs

        :param accept_terms_and_conditions_timestamp: The accept_terms_and_conditions_timestamp of this PayeeDetailResponseV3.
        :type accept_terms_and_conditions_timestamp: datetime
        """

        self._accept_terms_and_conditions_timestamp = accept_terms_and_conditions_timestamp

    @property
    def address(self):
        """Gets the address of this PayeeDetailResponseV3.


        :return: The address of this PayeeDetailResponseV3.
        :rtype: PayeeAddressV3
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PayeeDetailResponseV3.


        :param address: The address of this PayeeDetailResponseV3.
        :type address: PayeeAddressV3
        """

        self._address = address

    @property
    def cellphone_number(self):
        """Gets the cellphone_number of this PayeeDetailResponseV3.


        :return: The cellphone_number of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._cellphone_number

    @cellphone_number.setter
    def cellphone_number(self, cellphone_number):
        """Sets the cellphone_number of this PayeeDetailResponseV3.


        :param cellphone_number: The cellphone_number of this PayeeDetailResponseV3.
        :type cellphone_number: str
        """

        self._cellphone_number = cellphone_number

    @property
    def challenge(self):
        """Gets the challenge of this PayeeDetailResponseV3.


        :return: The challenge of this PayeeDetailResponseV3.
        :rtype: ChallengeV3
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this PayeeDetailResponseV3.


        :param challenge: The challenge of this PayeeDetailResponseV3.
        :type challenge: ChallengeV3
        """

        self._challenge = challenge

    @property
    def company(self):
        """Gets the company of this PayeeDetailResponseV3.


        :return: The company of this PayeeDetailResponseV3.
        :rtype: CompanyV3
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this PayeeDetailResponseV3.


        :param company: The company of this PayeeDetailResponseV3.
        :type company: CompanyV3
        """

        self._company = company

    @property
    def country(self):
        """Gets the country of this PayeeDetailResponseV3.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.

        :return: The country of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PayeeDetailResponseV3.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.

        :param country: The country of this PayeeDetailResponseV3.
        :type country: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")
        if country is not None and len(country) < 2:
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")
        if country is not None and not re.search(r'^[A-Z]{2}$', country):
            raise ValueError("Invalid value for `country`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")

        self._country = country

    @property
    def created(self):
        """Gets the created of this PayeeDetailResponseV3.


        :return: The created of this PayeeDetailResponseV3.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PayeeDetailResponseV3.


        :param created: The created of this PayeeDetailResponseV3.
        :type created: datetime
        """

        self._created = created

    @property
    def disabled(self):
        """Gets the disabled of this PayeeDetailResponseV3.


        :return: The disabled of this PayeeDetailResponseV3.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PayeeDetailResponseV3.


        :param disabled: The disabled of this PayeeDetailResponseV3.
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def disabled_comment(self):
        """Gets the disabled_comment of this PayeeDetailResponseV3.


        :return: The disabled_comment of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._disabled_comment

    @disabled_comment.setter
    def disabled_comment(self, disabled_comment):
        """Sets the disabled_comment of this PayeeDetailResponseV3.


        :param disabled_comment: The disabled_comment of this PayeeDetailResponseV3.
        :type disabled_comment: str
        """

        self._disabled_comment = disabled_comment

    @property
    def disabled_updated_timestamp(self):
        """Gets the disabled_updated_timestamp of this PayeeDetailResponseV3.


        :return: The disabled_updated_timestamp of this PayeeDetailResponseV3.
        :rtype: datetime
        """
        return self._disabled_updated_timestamp

    @disabled_updated_timestamp.setter
    def disabled_updated_timestamp(self, disabled_updated_timestamp):
        """Sets the disabled_updated_timestamp of this PayeeDetailResponseV3.


        :param disabled_updated_timestamp: The disabled_updated_timestamp of this PayeeDetailResponseV3.
        :type disabled_updated_timestamp: datetime
        """

        self._disabled_updated_timestamp = disabled_updated_timestamp

    @property
    def display_name(self):
        """Gets the display_name of this PayeeDetailResponseV3.


        :return: The display_name of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PayeeDetailResponseV3.


        :param display_name: The display_name of this PayeeDetailResponseV3.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this PayeeDetailResponseV3.


        :return: The email of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayeeDetailResponseV3.


        :param email: The email of this PayeeDetailResponseV3.
        :type email: str
        """

        self._email = email

    @property
    def enhanced_kyc_completed(self):
        """Gets the enhanced_kyc_completed of this PayeeDetailResponseV3.


        :return: The enhanced_kyc_completed of this PayeeDetailResponseV3.
        :rtype: bool
        """
        return self._enhanced_kyc_completed

    @enhanced_kyc_completed.setter
    def enhanced_kyc_completed(self, enhanced_kyc_completed):
        """Sets the enhanced_kyc_completed of this PayeeDetailResponseV3.


        :param enhanced_kyc_completed: The enhanced_kyc_completed of this PayeeDetailResponseV3.
        :type enhanced_kyc_completed: bool
        """

        self._enhanced_kyc_completed = enhanced_kyc_completed

    @property
    def grace_period_end_date(self):
        """Gets the grace_period_end_date of this PayeeDetailResponseV3.


        :return: The grace_period_end_date of this PayeeDetailResponseV3.
        :rtype: date
        """
        return self._grace_period_end_date

    @grace_period_end_date.setter
    def grace_period_end_date(self, grace_period_end_date):
        """Sets the grace_period_end_date of this PayeeDetailResponseV3.


        :param grace_period_end_date: The grace_period_end_date of this PayeeDetailResponseV3.
        :type grace_period_end_date: date
        """

        self._grace_period_end_date = grace_period_end_date

    @property
    def individual(self):
        """Gets the individual of this PayeeDetailResponseV3.


        :return: The individual of this PayeeDetailResponseV3.
        :rtype: IndividualV3
        """
        return self._individual

    @individual.setter
    def individual(self, individual):
        """Sets the individual of this PayeeDetailResponseV3.


        :param individual: The individual of this PayeeDetailResponseV3.
        :type individual: IndividualV3
        """

        self._individual = individual

    @property
    def kyc_completed_timestamp(self):
        """Gets the kyc_completed_timestamp of this PayeeDetailResponseV3.


        :return: The kyc_completed_timestamp of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._kyc_completed_timestamp

    @kyc_completed_timestamp.setter
    def kyc_completed_timestamp(self, kyc_completed_timestamp):
        """Sets the kyc_completed_timestamp of this PayeeDetailResponseV3.


        :param kyc_completed_timestamp: The kyc_completed_timestamp of this PayeeDetailResponseV3.
        :type kyc_completed_timestamp: str
        """

        self._kyc_completed_timestamp = kyc_completed_timestamp

    @property
    def language(self):
        """Gets the language of this PayeeDetailResponseV3.

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment. 

        :return: The language of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PayeeDetailResponseV3.

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment. 

        :param language: The language of this PayeeDetailResponseV3.
        :type language: str
        """

        self._language = language

    @property
    def marketing_opt_in_decision(self):
        """Gets the marketing_opt_in_decision of this PayeeDetailResponseV3.


        :return: The marketing_opt_in_decision of this PayeeDetailResponseV3.
        :rtype: bool
        """
        return self._marketing_opt_in_decision

    @marketing_opt_in_decision.setter
    def marketing_opt_in_decision(self, marketing_opt_in_decision):
        """Sets the marketing_opt_in_decision of this PayeeDetailResponseV3.


        :param marketing_opt_in_decision: The marketing_opt_in_decision of this PayeeDetailResponseV3.
        :type marketing_opt_in_decision: bool
        """

        self._marketing_opt_in_decision = marketing_opt_in_decision

    @property
    def marketing_opt_in_timestamp(self):
        """Gets the marketing_opt_in_timestamp of this PayeeDetailResponseV3.


        :return: The marketing_opt_in_timestamp of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._marketing_opt_in_timestamp

    @marketing_opt_in_timestamp.setter
    def marketing_opt_in_timestamp(self, marketing_opt_in_timestamp):
        """Sets the marketing_opt_in_timestamp of this PayeeDetailResponseV3.


        :param marketing_opt_in_timestamp: The marketing_opt_in_timestamp of this PayeeDetailResponseV3.
        :type marketing_opt_in_timestamp: str
        """

        self._marketing_opt_in_timestamp = marketing_opt_in_timestamp

    @property
    def onboarded_status(self):
        """Gets the onboarded_status of this PayeeDetailResponseV3.

        Onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED

        :return: The onboarded_status of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._onboarded_status

    @onboarded_status.setter
    def onboarded_status(self, onboarded_status):
        """Sets the onboarded_status of this PayeeDetailResponseV3.

        Onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED

        :param onboarded_status: The onboarded_status of this PayeeDetailResponseV3.
        :type onboarded_status: str
        """

        self._onboarded_status = onboarded_status

    @property
    def pause_payment(self):
        """Gets the pause_payment of this PayeeDetailResponseV3.


        :return: The pause_payment of this PayeeDetailResponseV3.
        :rtype: bool
        """
        return self._pause_payment

    @pause_payment.setter
    def pause_payment(self, pause_payment):
        """Sets the pause_payment of this PayeeDetailResponseV3.


        :param pause_payment: The pause_payment of this PayeeDetailResponseV3.
        :type pause_payment: bool
        """

        self._pause_payment = pause_payment

    @property
    def pause_payment_timestamp(self):
        """Gets the pause_payment_timestamp of this PayeeDetailResponseV3.


        :return: The pause_payment_timestamp of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._pause_payment_timestamp

    @pause_payment_timestamp.setter
    def pause_payment_timestamp(self, pause_payment_timestamp):
        """Sets the pause_payment_timestamp of this PayeeDetailResponseV3.


        :param pause_payment_timestamp: The pause_payment_timestamp of this PayeeDetailResponseV3.
        :type pause_payment_timestamp: str
        """

        self._pause_payment_timestamp = pause_payment_timestamp

    @property
    def payee_id(self):
        """Gets the payee_id of this PayeeDetailResponseV3.


        :return: The payee_id of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PayeeDetailResponseV3.


        :param payee_id: The payee_id of this PayeeDetailResponseV3.
        :type payee_id: str
        """

        self._payee_id = payee_id

    @property
    def payee_type(self):
        """Gets the payee_type of this PayeeDetailResponseV3.

        Type of Payee. One of the following values: Individual, Company

        :return: The payee_type of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._payee_type

    @payee_type.setter
    def payee_type(self, payee_type):
        """Sets the payee_type of this PayeeDetailResponseV3.

        Type of Payee. One of the following values: Individual, Company

        :param payee_type: The payee_type of this PayeeDetailResponseV3.
        :type payee_type: str
        """

        self._payee_type = payee_type

    @property
    def payor_refs(self):
        """Gets the payor_refs of this PayeeDetailResponseV3.


        :return: The payor_refs of this PayeeDetailResponseV3.
        :rtype: List[PayeePayorRefV3]
        """
        return self._payor_refs

    @payor_refs.setter
    def payor_refs(self, payor_refs):
        """Sets the payor_refs of this PayeeDetailResponseV3.


        :param payor_refs: The payor_refs of this PayeeDetailResponseV3.
        :type payor_refs: List[PayeePayorRefV3]
        """

        self._payor_refs = payor_refs

    @property
    def watchlist_override_comment(self):
        """Gets the watchlist_override_comment of this PayeeDetailResponseV3.


        :return: The watchlist_override_comment of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._watchlist_override_comment

    @watchlist_override_comment.setter
    def watchlist_override_comment(self, watchlist_override_comment):
        """Sets the watchlist_override_comment of this PayeeDetailResponseV3.


        :param watchlist_override_comment: The watchlist_override_comment of this PayeeDetailResponseV3.
        :type watchlist_override_comment: str
        """

        self._watchlist_override_comment = watchlist_override_comment

    @property
    def watchlist_override_expires_at_timestamp(self):
        """Gets the watchlist_override_expires_at_timestamp of this PayeeDetailResponseV3.


        :return: The watchlist_override_expires_at_timestamp of this PayeeDetailResponseV3.
        :rtype: datetime
        """
        return self._watchlist_override_expires_at_timestamp

    @watchlist_override_expires_at_timestamp.setter
    def watchlist_override_expires_at_timestamp(self, watchlist_override_expires_at_timestamp):
        """Sets the watchlist_override_expires_at_timestamp of this PayeeDetailResponseV3.


        :param watchlist_override_expires_at_timestamp: The watchlist_override_expires_at_timestamp of this PayeeDetailResponseV3.
        :type watchlist_override_expires_at_timestamp: datetime
        """

        self._watchlist_override_expires_at_timestamp = watchlist_override_expires_at_timestamp

    @property
    def watchlist_status(self):
        """Gets the watchlist_status of this PayeeDetailResponseV3.

        Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED

        :return: The watchlist_status of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._watchlist_status

    @watchlist_status.setter
    def watchlist_status(self, watchlist_status):
        """Sets the watchlist_status of this PayeeDetailResponseV3.

        Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED

        :param watchlist_status: The watchlist_status of this PayeeDetailResponseV3.
        :type watchlist_status: str
        """

        self._watchlist_status = watchlist_status

    @property
    def watchlist_status_updated_timestamp(self):
        """Gets the watchlist_status_updated_timestamp of this PayeeDetailResponseV3.


        :return: The watchlist_status_updated_timestamp of this PayeeDetailResponseV3.
        :rtype: str
        """
        return self._watchlist_status_updated_timestamp

    @watchlist_status_updated_timestamp.setter
    def watchlist_status_updated_timestamp(self, watchlist_status_updated_timestamp):
        """Sets the watchlist_status_updated_timestamp of this PayeeDetailResponseV3.


        :param watchlist_status_updated_timestamp: The watchlist_status_updated_timestamp of this PayeeDetailResponseV3.
        :type watchlist_status_updated_timestamp: str
        """

        self._watchlist_status_updated_timestamp = watchlist_status_updated_timestamp
