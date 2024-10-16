# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Patient1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, email: str=None, fax: str=None, first_name: str=None, last_name: str=None, middle_name: str=None, npi: str=None, phone: str=None, provider_number: str=None, provider_qualifier: str=None, specialty: str=None, suffix: str=None):
        """Patient1 - a model defined in OpenAPI

        :param address: The address of this Patient1.
        :param email: The email of this Patient1.
        :param fax: The fax of this Patient1.
        :param first_name: The first_name of this Patient1.
        :param last_name: The last_name of this Patient1.
        :param middle_name: The middle_name of this Patient1.
        :param npi: The npi of this Patient1.
        :param phone: The phone of this Patient1.
        :param provider_number: The provider_number of this Patient1.
        :param provider_qualifier: The provider_qualifier of this Patient1.
        :param specialty: The specialty of this Patient1.
        :param suffix: The suffix of this Patient1.
        """
        self.openapi_types = {
            'address': str,
            'email': str,
            'fax': str,
            'first_name': str,
            'last_name': str,
            'middle_name': str,
            'npi': str,
            'phone': str,
            'provider_number': str,
            'provider_qualifier': str,
            'specialty': str,
            'suffix': str
        }

        self.attribute_map = {
            'address': 'address',
            'email': 'email',
            'fax': 'fax',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'middle_name': 'middle_name',
            'npi': 'npi',
            'phone': 'phone',
            'provider_number': 'provider_number',
            'provider_qualifier': 'provider_qualifier',
            'specialty': 'specialty',
            'suffix': 'suffix'
        }

        self._address = address
        self._email = email
        self._fax = fax
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._npi = npi
        self._phone = phone
        self._provider_number = provider_number
        self._provider_qualifier = provider_qualifier
        self._specialty = specialty
        self._suffix = suffix

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Patient1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Patient_1 of this Patient1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this Patient1.

        

        :return: The address of this Patient1.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Patient1.

        

        :param address: The address of this Patient1.
        :type address: str
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this Patient1.

        

        :return: The email of this Patient1.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Patient1.

        

        :param email: The email of this Patient1.
        :type email: str
        """

        self._email = email

    @property
    def fax(self):
        """Gets the fax of this Patient1.

        Should follow format \"xxx-xx-xxxx\"

        :return: The fax of this Patient1.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this Patient1.

        Should follow format \"xxx-xx-xxxx\"

        :param fax: The fax of this Patient1.
        :type fax: str
        """

        self._fax = fax

    @property
    def first_name(self):
        """Gets the first_name of this Patient1.

        

        :return: The first_name of this Patient1.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Patient1.

        

        :param first_name: The first_name of this Patient1.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Patient1.

        

        :return: The last_name of this Patient1.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Patient1.

        

        :param last_name: The last_name of this Patient1.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def middle_name(self):
        """Gets the middle_name of this Patient1.

        

        :return: The middle_name of this Patient1.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this Patient1.

        

        :param middle_name: The middle_name of this Patient1.
        :type middle_name: str
        """

        self._middle_name = middle_name

    @property
    def npi(self):
        """Gets the npi of this Patient1.

        

        :return: The npi of this Patient1.
        :rtype: str
        """
        return self._npi

    @npi.setter
    def npi(self, npi):
        """Sets the npi of this Patient1.

        

        :param npi: The npi of this Patient1.
        :type npi: str
        """

        self._npi = npi

    @property
    def phone(self):
        """Gets the phone of this Patient1.

        Should follow format \"xxx-xx-xxxx\"

        :return: The phone of this Patient1.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Patient1.

        Should follow format \"xxx-xx-xxxx\"

        :param phone: The phone of this Patient1.
        :type phone: str
        """

        self._phone = phone

    @property
    def provider_number(self):
        """Gets the provider_number of this Patient1.

        

        :return: The provider_number of this Patient1.
        :rtype: str
        """
        return self._provider_number

    @provider_number.setter
    def provider_number(self, provider_number):
        """Sets the provider_number of this Patient1.

        

        :param provider_number: The provider_number of this Patient1.
        :type provider_number: str
        """

        self._provider_number = provider_number

    @property
    def provider_qualifier(self):
        """Gets the provider_qualifier of this Patient1.

        Can be one of following, `''`, `'0B'`(State License #), `'1G'`(Provider UPIN #), `'G2'`(Provider Commercial #)

        :return: The provider_qualifier of this Patient1.
        :rtype: str
        """
        return self._provider_qualifier

    @provider_qualifier.setter
    def provider_qualifier(self, provider_qualifier):
        """Sets the provider_qualifier of this Patient1.

        Can be one of following, `''`, `'0B'`(State License #), `'1G'`(Provider UPIN #), `'G2'`(Provider Commercial #)

        :param provider_qualifier: The provider_qualifier of this Patient1.
        :type provider_qualifier: str
        """
        allowed_values = ["", "0B", "1G", "G2"]  # noqa: E501
        if provider_qualifier not in allowed_values:
            raise ValueError(
                "Invalid value for `provider_qualifier` ({0}), must be one of {1}"
                .format(provider_qualifier, allowed_values)
            )

        self._provider_qualifier = provider_qualifier

    @property
    def specialty(self):
        """Gets the specialty of this Patient1.

        Can be one of following, `''`, `'Acupuncture'`, `'Advanced Practice Midwife'`, `'Aesthetic Medicine'`, `'Aesthetician'`, `'Allergist/Immunologist'`, `'Anesthesiologist'`, `'Cardiac Electrophysiologist'`, `'Cardiologist'`, `'Cardiothoracic Surgeon'`, `'Child/Adolescent Psychiatry'`, `'Chiropractor'`, `'Clinical Social Worker'`, `'Colorectal Surgeon'`, `'Correactology'`, `'Cosmetic Medicine'`, `'Counselor Mental Health'`, `'Counselor Professional'`, `'Counselor'`, `'Dentist'`, `'Diabetology'`, `'Dermatologist'`, `'Diagnostic Medical Sonographer'`, `'Dietitian, Registered'`, `'Ear-Nose-Throat Specialist (ENT)'`, `'Emergency Medicine Physician'`, `'Endocrinologist'`, `'Endodontist'`, `'Epidemiologist'`, `'Family Practitioner'`, `'Gastroenterologist'`, `'General Practice'`, `'General Surgeon'`, `'Geneticist'`, `'Geriatrician'`, `'Gerontologist'`, `'Gynecologist (no OB)'`, `'Gynegologic Oncologist'`, `'Hand Surgeon'`, `'Hematologist'`, `'Home Care'`, `'Hospice'`, `'Hospitalist'`, `'Infectious Disease Specialist'`, `'Integrative and Functional Medicine'`, `'Integrative Medicine'`, `'Internist'`, `'Interventional Radiology'`, `'Laboratory Medicine Specialist'`, `'Laser Surgery'`, `'Massage Therapist'`, `'Naturopathic Physician'`, `'Neonatologist'`, `'Nephrologist'`, `'Neurologist'`, `'Neuropsychology'`, `'Neurosurgeon'`, `'Not Actively Practicing'`, `'Nuclear Medicine Specialist'`, `'Nurse Practitioner'`, `'Nursing'`, `'Nutritionist'`, `'Obstetrician/Gynecologist'`, `'Occupational Medicine'`, `'Occupational Therapist'`, `'Oncologist'`, `'Ophthalmologist'`, `'Optometrist'`, `'Oral Surgeon'`, `'Orofacial Pain'`, `'Orthodontist'`, `'Orthopedic Surgeon'`, `'Orthotist'`, `'Other'`, `'Pain Management Specialist'`, `'Pathologist'`, `'Pediatric Dentist'`, `'Pediatric Gastroenterology'`, `'Pediatric Surgeon'`, `'Pediatrician'`, `'Perinatologist'`, `'Periodontist'`, `'Physical Medicine and Rehab Specialist'`, `'Physical Therapist'`, `'Physician Assistant'`, `'Plastic Surgeon'`, `'Podiatrist'`, `'Preventive-Aging Medicine'`, `'Preventive Medicine/Occupational-Environmental Medicine'`, `'Primary Care Physician'`, `'Prosthetist'`, `'Prosthodontist'`, `'Psychiatrist'`, `'Psychologist'`, `'Public Health Professional'`, `'Pulmonologist'`, `'Radiation Oncologist'`, `'Radiologist'`, `'Registered Nurse'`, `'Religious Nonmedical Practitioner'`, `'Reproductive Endocrinologist'`, `'Reproductive Medicine'`, `'Rheumatologist'`, `'Sleep Medicine'`, `'Speech-Language Pathologist'`, `'Sports Medicine Specialist'`, `'Urologist'`, `'Urgent Care'`, `'Vascular Surgeon'`

        :return: The specialty of this Patient1.
        :rtype: str
        """
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        """Sets the specialty of this Patient1.

        Can be one of following, `''`, `'Acupuncture'`, `'Advanced Practice Midwife'`, `'Aesthetic Medicine'`, `'Aesthetician'`, `'Allergist/Immunologist'`, `'Anesthesiologist'`, `'Cardiac Electrophysiologist'`, `'Cardiologist'`, `'Cardiothoracic Surgeon'`, `'Child/Adolescent Psychiatry'`, `'Chiropractor'`, `'Clinical Social Worker'`, `'Colorectal Surgeon'`, `'Correactology'`, `'Cosmetic Medicine'`, `'Counselor Mental Health'`, `'Counselor Professional'`, `'Counselor'`, `'Dentist'`, `'Diabetology'`, `'Dermatologist'`, `'Diagnostic Medical Sonographer'`, `'Dietitian, Registered'`, `'Ear-Nose-Throat Specialist (ENT)'`, `'Emergency Medicine Physician'`, `'Endocrinologist'`, `'Endodontist'`, `'Epidemiologist'`, `'Family Practitioner'`, `'Gastroenterologist'`, `'General Practice'`, `'General Surgeon'`, `'Geneticist'`, `'Geriatrician'`, `'Gerontologist'`, `'Gynecologist (no OB)'`, `'Gynegologic Oncologist'`, `'Hand Surgeon'`, `'Hematologist'`, `'Home Care'`, `'Hospice'`, `'Hospitalist'`, `'Infectious Disease Specialist'`, `'Integrative and Functional Medicine'`, `'Integrative Medicine'`, `'Internist'`, `'Interventional Radiology'`, `'Laboratory Medicine Specialist'`, `'Laser Surgery'`, `'Massage Therapist'`, `'Naturopathic Physician'`, `'Neonatologist'`, `'Nephrologist'`, `'Neurologist'`, `'Neuropsychology'`, `'Neurosurgeon'`, `'Not Actively Practicing'`, `'Nuclear Medicine Specialist'`, `'Nurse Practitioner'`, `'Nursing'`, `'Nutritionist'`, `'Obstetrician/Gynecologist'`, `'Occupational Medicine'`, `'Occupational Therapist'`, `'Oncologist'`, `'Ophthalmologist'`, `'Optometrist'`, `'Oral Surgeon'`, `'Orofacial Pain'`, `'Orthodontist'`, `'Orthopedic Surgeon'`, `'Orthotist'`, `'Other'`, `'Pain Management Specialist'`, `'Pathologist'`, `'Pediatric Dentist'`, `'Pediatric Gastroenterology'`, `'Pediatric Surgeon'`, `'Pediatrician'`, `'Perinatologist'`, `'Periodontist'`, `'Physical Medicine and Rehab Specialist'`, `'Physical Therapist'`, `'Physician Assistant'`, `'Plastic Surgeon'`, `'Podiatrist'`, `'Preventive-Aging Medicine'`, `'Preventive Medicine/Occupational-Environmental Medicine'`, `'Primary Care Physician'`, `'Prosthetist'`, `'Prosthodontist'`, `'Psychiatrist'`, `'Psychologist'`, `'Public Health Professional'`, `'Pulmonologist'`, `'Radiation Oncologist'`, `'Radiologist'`, `'Registered Nurse'`, `'Religious Nonmedical Practitioner'`, `'Reproductive Endocrinologist'`, `'Reproductive Medicine'`, `'Rheumatologist'`, `'Sleep Medicine'`, `'Speech-Language Pathologist'`, `'Sports Medicine Specialist'`, `'Urologist'`, `'Urgent Care'`, `'Vascular Surgeon'`

        :param specialty: The specialty of this Patient1.
        :type specialty: str
        """
        allowed_values = ["", "Acupuncture", "Advanced Practice Midwife", "Aesthetic Medicine", "Aesthetician", "Allergist/Immunologist", "Anesthesiologist", "Cardiac Electrophysiologist", "Cardiologist", "Cardiothoracic Surgeon", "Child/Adolescent Psychiatry", "Chiropractor", "Clinical Social Worker", "Colorectal Surgeon", "Correactology", "Cosmetic Medicine", "Counselor Mental Health", "Counselor Professional", "Counselor", "Dentist", "Diabetology", "Dermatologist", "Diagnostic Medical Sonographer", "Dietitian, Registered", "Ear-Nose-Throat Specialist (ENT)", "Emergency Medicine Physician", "Endocrinologist", "Endodontist", "Epidemiologist", "Family Practitioner", "Gastroenterologist", "General Practice", "General Surgeon", "Geneticist", "Geriatrician", "Gerontologist", "Gynecologist (no OB)", "Gynegologic Oncologist", "Hand Surgeon", "Hematologist", "Home Care", "Hospice", "Hospitalist", "Infectious Disease Specialist", "Integrative and Functional Medicine", "Integrative Medicine", "Internist", "Interventional Radiology", "Laboratory Medicine Specialist", "Laser Surgery", "Massage Therapist", "Naturopathic Physician", "Neonatologist", "Nephrologist", "Neurologist", "Neuropsychology", "Neurosurgeon", "Not Actively Practicing", "Nuclear Medicine Specialist", "Nurse Practitioner", "Nursing", "Nutritionist", "Obstetrician/Gynecologist", "Occupational Medicine", "Occupational Therapist", "Oncologist", "Ophthalmologist", "Optometrist", "Oral Surgeon", "Orofacial Pain", "Orthodontist", "Orthopedic Surgeon", "Orthotist", "Other", "Pain Management Specialist", "Pathologist", "Pediatric Dentist", "Pediatric Gastroenterology", "Pediatric Surgeon", "Pediatrician", "Perinatologist", "Periodontist", "Physical Medicine and Rehab Specialist", "Physical Therapist", "Physician Assistant", "Plastic Surgeon", "Podiatrist", "Preventive-Aging Medicine", "Preventive Medicine/Occupational-Environmental Medicine", "Primary Care Physician", "Prosthetist", "Prosthodontist", "Psychiatrist", "Psychologist", "Public Health Professional", "Pulmonologist", "Radiation Oncologist", "Radiologist", "Registered Nurse", "Religious Nonmedical Practitioner", "Reproductive Endocrinologist", "Reproductive Medicine", "Rheumatologist", "Sleep Medicine", "Speech-Language Pathologist", "Sports Medicine Specialist", "Urologist", "Urgent Care", "Vascular Surgeon"]  # noqa: E501
        if specialty not in allowed_values:
            raise ValueError(
                "Invalid value for `specialty` ({0}), must be one of {1}"
                .format(specialty, allowed_values)
            )

        self._specialty = specialty

    @property
    def suffix(self):
        """Gets the suffix of this Patient1.

        

        :return: The suffix of this Patient1.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this Patient1.

        

        :param suffix: The suffix of this Patient1.
        :type suffix: str
        """

        self._suffix = suffix
