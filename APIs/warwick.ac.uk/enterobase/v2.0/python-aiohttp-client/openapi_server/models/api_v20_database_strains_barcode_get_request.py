# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiV20DatabaseStrainsBarcodeGetRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, antigenic_formulas: str=None, assembly_barcode: str=None, barcode: List[str]=None, city: str=None, collection_date: int=None, collection_month: int=None, collection_time: str=None, collection_year: int=None, comment: str=None, continent: str=None, country: str=None, county: str=None, lab_contact: str=None, latitude: float=None, limit: int=50, longitude: float=None, my_strains: bool=None, offset: int=0, only_fields: List[str]=None, orderby: str='barcode', postcode: str=None, region: str=None, reldate: int=None, return_all: bool=None, sample_accession: str=None, secondary_sample_accession: str=None, serotype: str=None, sortorder: str='asc', source_details: str=None, source_niche: str=None, source_type: str=None, strain_name: str=None, substrains: bool=None, uberstrain: str=None, version: int=None):
        """ApiV20DatabaseStrainsBarcodeGetRequest - a model defined in OpenAPI

        :param antigenic_formulas: The antigenic_formulas of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param assembly_barcode: The assembly_barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param barcode: The barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param city: The city of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param collection_date: The collection_date of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param collection_month: The collection_month of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param collection_time: The collection_time of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param collection_year: The collection_year of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param comment: The comment of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param continent: The continent of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param country: The country of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param county: The county of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param lab_contact: The lab_contact of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param latitude: The latitude of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param limit: The limit of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param longitude: The longitude of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param my_strains: The my_strains of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param offset: The offset of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param only_fields: The only_fields of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param orderby: The orderby of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param postcode: The postcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param region: The region of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param reldate: The reldate of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param return_all: The return_all of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param sample_accession: The sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param secondary_sample_accession: The secondary_sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param serotype: The serotype of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param sortorder: The sortorder of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param source_details: The source_details of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param source_niche: The source_niche of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param source_type: The source_type of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param strain_name: The strain_name of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param substrains: The substrains of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param uberstrain: The uberstrain of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :param version: The version of this ApiV20DatabaseStrainsBarcodeGetRequest.
        """
        self.openapi_types = {
            'antigenic_formulas': str,
            'assembly_barcode': str,
            'barcode': List[str],
            'city': str,
            'collection_date': int,
            'collection_month': int,
            'collection_time': str,
            'collection_year': int,
            'comment': str,
            'continent': str,
            'country': str,
            'county': str,
            'lab_contact': str,
            'latitude': float,
            'limit': int,
            'longitude': float,
            'my_strains': bool,
            'offset': int,
            'only_fields': List[str],
            'orderby': str,
            'postcode': str,
            'region': str,
            'reldate': int,
            'return_all': bool,
            'sample_accession': str,
            'secondary_sample_accession': str,
            'serotype': str,
            'sortorder': str,
            'source_details': str,
            'source_niche': str,
            'source_type': str,
            'strain_name': str,
            'substrains': bool,
            'uberstrain': str,
            'version': int
        }

        self.attribute_map = {
            'antigenic_formulas': 'antigenic_formulas',
            'assembly_barcode': 'assembly_barcode',
            'barcode': 'barcode',
            'city': 'city',
            'collection_date': 'collection_date',
            'collection_month': 'collection_month',
            'collection_time': 'collection_time',
            'collection_year': 'collection_year',
            'comment': 'comment',
            'continent': 'continent',
            'country': 'country',
            'county': 'county',
            'lab_contact': 'lab_contact',
            'latitude': 'latitude',
            'limit': 'limit',
            'longitude': 'longitude',
            'my_strains': 'my_strains',
            'offset': 'offset',
            'only_fields': 'only_fields',
            'orderby': 'orderby',
            'postcode': 'postcode',
            'region': 'region',
            'reldate': 'reldate',
            'return_all': 'return_all',
            'sample_accession': 'sample_accession',
            'secondary_sample_accession': 'secondary_sample_accession',
            'serotype': 'serotype',
            'sortorder': 'sortorder',
            'source_details': 'source_details',
            'source_niche': 'source_niche',
            'source_type': 'source_type',
            'strain_name': 'strain_name',
            'substrains': 'substrains',
            'uberstrain': 'uberstrain',
            'version': 'version'
        }

        self._antigenic_formulas = antigenic_formulas
        self._assembly_barcode = assembly_barcode
        self._barcode = barcode
        self._city = city
        self._collection_date = collection_date
        self._collection_month = collection_month
        self._collection_time = collection_time
        self._collection_year = collection_year
        self._comment = comment
        self._continent = continent
        self._country = country
        self._county = county
        self._lab_contact = lab_contact
        self._latitude = latitude
        self._limit = limit
        self._longitude = longitude
        self._my_strains = my_strains
        self._offset = offset
        self._only_fields = only_fields
        self._orderby = orderby
        self._postcode = postcode
        self._region = region
        self._reldate = reldate
        self._return_all = return_all
        self._sample_accession = sample_accession
        self._secondary_sample_accession = secondary_sample_accession
        self._serotype = serotype
        self._sortorder = sortorder
        self._source_details = source_details
        self._source_niche = source_niche
        self._source_type = source_type
        self._strain_name = strain_name
        self._substrains = substrains
        self._uberstrain = uberstrain
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiV20DatabaseStrainsBarcodeGetRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _api_v2_0__database__strains__barcode__get_request of this ApiV20DatabaseStrainsBarcodeGetRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def antigenic_formulas(self):
        """Gets the antigenic_formulas of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The antigenic_formulas of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._antigenic_formulas

    @antigenic_formulas.setter
    def antigenic_formulas(self, antigenic_formulas):
        """Sets the antigenic_formulas of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param antigenic_formulas: The antigenic_formulas of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type antigenic_formulas: str
        """

        self._antigenic_formulas = antigenic_formulas

    @property
    def assembly_barcode(self):
        """Gets the assembly_barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The assembly_barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._assembly_barcode

    @assembly_barcode.setter
    def assembly_barcode(self, assembly_barcode):
        """Sets the assembly_barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param assembly_barcode: The assembly_barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type assembly_barcode: str
        """

        self._assembly_barcode = assembly_barcode

    @property
    def barcode(self):
        """Gets the barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: List[str]
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param barcode: The barcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type barcode: List[str]
        """

        self._barcode = barcode

    @property
    def city(self):
        """Gets the city of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The city of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param city: The city of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type city: str
        """

        self._city = city

    @property
    def collection_date(self):
        """Gets the collection_date of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The collection_date of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._collection_date

    @collection_date.setter
    def collection_date(self, collection_date):
        """Sets the collection_date of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param collection_date: The collection_date of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type collection_date: int
        """

        self._collection_date = collection_date

    @property
    def collection_month(self):
        """Gets the collection_month of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The collection_month of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._collection_month

    @collection_month.setter
    def collection_month(self, collection_month):
        """Sets the collection_month of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param collection_month: The collection_month of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type collection_month: int
        """

        self._collection_month = collection_month

    @property
    def collection_time(self):
        """Gets the collection_time of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The collection_time of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param collection_time: The collection_time of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type collection_time: str
        """

        self._collection_time = collection_time

    @property
    def collection_year(self):
        """Gets the collection_year of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The collection_year of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._collection_year

    @collection_year.setter
    def collection_year(self, collection_year):
        """Sets the collection_year of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param collection_year: The collection_year of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type collection_year: int
        """

        self._collection_year = collection_year

    @property
    def comment(self):
        """Gets the comment of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The comment of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param comment: The comment of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type comment: str
        """

        self._comment = comment

    @property
    def continent(self):
        """Gets the continent of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The continent of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._continent

    @continent.setter
    def continent(self, continent):
        """Sets the continent of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param continent: The continent of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type continent: str
        """

        self._continent = continent

    @property
    def country(self):
        """Gets the country of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The country of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param country: The country of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type country: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The county of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param county: The county of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type county: str
        """

        self._county = county

    @property
    def lab_contact(self):
        """Gets the lab_contact of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The lab_contact of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._lab_contact

    @lab_contact.setter
    def lab_contact(self, lab_contact):
        """Sets the lab_contact of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param lab_contact: The lab_contact of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type lab_contact: str
        """

        self._lab_contact = lab_contact

    @property
    def latitude(self):
        """Gets the latitude of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The latitude of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param latitude: The latitude of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def limit(self):
        """Gets the limit of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The limit of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param limit: The limit of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type limit: int
        """

        self._limit = limit

    @property
    def longitude(self):
        """Gets the longitude of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The longitude of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param longitude: The longitude of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type longitude: float
        """

        self._longitude = longitude

    @property
    def my_strains(self):
        """Gets the my_strains of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The my_strains of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: bool
        """
        return self._my_strains

    @my_strains.setter
    def my_strains(self, my_strains):
        """Sets the my_strains of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param my_strains: The my_strains of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type my_strains: bool
        """

        self._my_strains = my_strains

    @property
    def offset(self):
        """Gets the offset of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The offset of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param offset: The offset of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type offset: int
        """

        self._offset = offset

    @property
    def only_fields(self):
        """Gets the only_fields of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The only_fields of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: List[str]
        """
        return self._only_fields

    @only_fields.setter
    def only_fields(self, only_fields):
        """Sets the only_fields of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param only_fields: The only_fields of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type only_fields: List[str]
        """

        self._only_fields = only_fields

    @property
    def orderby(self):
        """Gets the orderby of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The orderby of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._orderby

    @orderby.setter
    def orderby(self, orderby):
        """Sets the orderby of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param orderby: The orderby of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type orderby: str
        """

        self._orderby = orderby

    @property
    def postcode(self):
        """Gets the postcode of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The postcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param postcode: The postcode of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type postcode: str
        """

        self._postcode = postcode

    @property
    def region(self):
        """Gets the region of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The region of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param region: The region of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type region: str
        """

        self._region = region

    @property
    def reldate(self):
        """Gets the reldate of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The reldate of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._reldate

    @reldate.setter
    def reldate(self, reldate):
        """Sets the reldate of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param reldate: The reldate of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type reldate: int
        """

        self._reldate = reldate

    @property
    def return_all(self):
        """Gets the return_all of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The return_all of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: bool
        """
        return self._return_all

    @return_all.setter
    def return_all(self, return_all):
        """Sets the return_all of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param return_all: The return_all of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type return_all: bool
        """

        self._return_all = return_all

    @property
    def sample_accession(self):
        """Gets the sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._sample_accession

    @sample_accession.setter
    def sample_accession(self, sample_accession):
        """Sets the sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param sample_accession: The sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type sample_accession: str
        """

        self._sample_accession = sample_accession

    @property
    def secondary_sample_accession(self):
        """Gets the secondary_sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The secondary_sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._secondary_sample_accession

    @secondary_sample_accession.setter
    def secondary_sample_accession(self, secondary_sample_accession):
        """Sets the secondary_sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param secondary_sample_accession: The secondary_sample_accession of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type secondary_sample_accession: str
        """

        self._secondary_sample_accession = secondary_sample_accession

    @property
    def serotype(self):
        """Gets the serotype of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The serotype of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._serotype

    @serotype.setter
    def serotype(self, serotype):
        """Sets the serotype of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param serotype: The serotype of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type serotype: str
        """

        self._serotype = serotype

    @property
    def sortorder(self):
        """Gets the sortorder of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The sortorder of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._sortorder

    @sortorder.setter
    def sortorder(self, sortorder):
        """Sets the sortorder of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param sortorder: The sortorder of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type sortorder: str
        """

        self._sortorder = sortorder

    @property
    def source_details(self):
        """Gets the source_details of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The source_details of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """Sets the source_details of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param source_details: The source_details of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type source_details: str
        """

        self._source_details = source_details

    @property
    def source_niche(self):
        """Gets the source_niche of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The source_niche of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._source_niche

    @source_niche.setter
    def source_niche(self, source_niche):
        """Sets the source_niche of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param source_niche: The source_niche of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type source_niche: str
        """

        self._source_niche = source_niche

    @property
    def source_type(self):
        """Gets the source_type of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The source_type of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param source_type: The source_type of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type source_type: str
        """

        self._source_type = source_type

    @property
    def strain_name(self):
        """Gets the strain_name of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The strain_name of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._strain_name

    @strain_name.setter
    def strain_name(self, strain_name):
        """Sets the strain_name of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param strain_name: The strain_name of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type strain_name: str
        """

        self._strain_name = strain_name

    @property
    def substrains(self):
        """Gets the substrains of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The substrains of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: bool
        """
        return self._substrains

    @substrains.setter
    def substrains(self, substrains):
        """Sets the substrains of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param substrains: The substrains of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type substrains: bool
        """

        self._substrains = substrains

    @property
    def uberstrain(self):
        """Gets the uberstrain of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The uberstrain of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: str
        """
        return self._uberstrain

    @uberstrain.setter
    def uberstrain(self, uberstrain):
        """Sets the uberstrain of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param uberstrain: The uberstrain of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type uberstrain: str
        """

        self._uberstrain = uberstrain

    @property
    def version(self):
        """Gets the version of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :return: The version of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiV20DatabaseStrainsBarcodeGetRequest.


        :param version: The version of this ApiV20DatabaseStrainsBarcodeGetRequest.
        :type version: int
        """

        self._version = version
