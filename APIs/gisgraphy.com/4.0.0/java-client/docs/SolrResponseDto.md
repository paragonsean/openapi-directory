

# SolrResponseDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adm1Code** | **String** | The internal code for the administrative division of level 1 |  [optional] |
|**adm1Name** | **String** | The name of the administrative division of level 1 |  [optional] |
|**adm1NamesAlternate** | **List&lt;String&gt;** | The alternate names of the administrative division of level 1 without specific language code |  [optional] |
|**adm2Code** | **String** | The internal code for the administrative division of level 2 |  [optional] |
|**adm2Name** | **String** | The name of the administrative division of level 2 |  [optional] |
|**adm2NamesAlternate** | **List&lt;String&gt;** | The alternate names of the administrative division of level 2 without specific language code |  [optional] |
|**adm3Code** | **String** | The internal code for the administrative division of level 3 |  [optional] |
|**adm3Name** | **String** | The name of the administrative division of level 3 |  [optional] |
|**adm4Code** | **String** | The internal code for the administrative division of level 4 |  [optional] |
|**adm4Name** | **String** | The name of the administrative division of level 4 |  [optional] |
|**amenity** | **String** | Informations on category of OpenStreetMap POIs |  [optional] |
|**area** | **Double** | Area of the country in m² (only for country placetype) |  [optional] |
|**capitalName** | **String** | Name of the capital of the country(only for country placetype) |  [optional] |
|**continent** | **String** | The continent the country belongs (only for country placetype) |  [optional] |
|**countryCode** | **String** | The ISO 3166 country code |  [optional] |
|**countryFlagUrl** | **String** | The relative URL to get the country flag image |  [optional] |
|**countryName** | **String** | The name of the country the features belongs to |  [optional] |
|**countryNamesAlternate** | **List&lt;String&gt;** | The alternate names of the country without specific language code |  [optional] |
|**currencyCode** | **String** | The ISO 4217 Currency from the curencycode (only for country placetype) |  [optional] |
|**currencyName** | **String** | The name of the currency of the country (only for country placetype) |  [optional] |
|**elevation** | **Integer** | Elevation in meters |  [optional] |
|**featureClass** | **String** | The feature Class. |  [optional] |
|**featureCode** | **String** | The feature Code. |  [optional] |
|**featureId** | **Long** | A unique id that identify the feature |  [optional] |
|**fipsCode** | **String** | The FIPS Code of the country (only for country placetype) |  [optional] |
|**fullyQualifiedAddress** | **String** | NOT USED YET |  [optional] |
|**fullyQualifiedName** | **String** | A name of the form : (adm1Name et adm2Name are printed) Paris, Département de Ville-De-Paris, Ile-De-France, (FR) |  [optional] |
|**googleMapUrl** | **String** | The URL to get the location on Google Map |  [optional] |
|**gtopo30** | **Integer** | Average elevation of 30&#39;x30&#39; (ca 900mx900m) area in meters |  [optional] |
|**houseNumbers** | [**List&lt;HouseNumberDto&gt;**](HouseNumberDto.md) | a list of all the house numbers sorted and their coordinates (only for placetype street) |  [optional] |
|**isIn** | **String** | Information on the city where the street / POI is (depends on OpenStreetMap &#39;is_in&#39; field), the city in general (only for placetype street) |  [optional] |
|**isInAdm** | **String** | Information of the administration division where the street / POI is. |  [optional] |
|**isInPlace** | **String** | Information on the place where the street / POI is (quater, common place). Generally a place at a lower level than city |  [optional] |
|**isInZip** | **List&lt;String&gt;** | Information of the zipcode where the street / POI is (often fill for placetype street) |  [optional] |
|**isoalpha2CountryCode** | **String** | The ISO 3166 alpha 2 code of the country (only for country placetype) |  [optional] |
|**isoalpha3CountryCode** | **String** | The ISO 3166 alpha 3 code of the country (only for country placetype) |  [optional] |
|**lat** | **Double** | The latitude (north-south) |  [optional] |
|**length** | **Double** | The length of the street (only for placetype street) |  [optional] |
|**level** | **Integer** | Level of the Adm 1 , 2, 3, or 4(only for Adm placetype) |  [optional] |
|**lng** | **Double** | The longitude (east-West) |  [optional] |
|**municipality** | **Boolean** | if the place is a municipality. it is usefull for geonames feature that don&#39;t have concept of &#39;city&#39; but a populated place (that can be a quarter) |  [optional] |
|**name** | **String** | The name of the feature |  [optional] |
|**nameAlternates** | **List&lt;String&gt;** | The alternate names of the feature that without specific language code |  [optional] |
|**nameAscii** | **String** | The ASCII name |  [optional] |
|**oneWay** | **Boolean** | whether the street is one way or not (only for placetype street) |  [optional] |
|**openstreetmapId** | **Long** | The OpenStreetMap unique id of the street (only for placetype street) |  [optional] |
|**openstreetmapMapUrl** | **String** | The URL to get the location on OpenStreetMap.org |  [optional] |
|**phonePrefix** | **String** | The phone prefix of the country. e.g : +33 .(only for country placetype) |  [optional] |
|**placetype** | **String** | The place Type of the Feature |  [optional] |
|**population** | **Integer** | How many people live in this feature |  [optional] |
|**postalCodeMask** | **String** | The mask that postal codes should verify. e.g : ##### (only for country placetype) |  [optional] |
|**postalCodeRegex** | **String** | The regular expression that postal codes should verify (only for country placetype) |  [optional] |
|**score** | **Float** | a number that indicates the relevance of the result |  [optional] |
|**spokenLanguages** | **List&lt;String&gt;** | List of languages spoken in the country (only for country placetype) |  [optional] |
|**streetType** | **String** | The type of the street (only for placetype street) |  [optional] |
|**timezone** | **String** | The timezone (e.g :Europe/Paris). |  [optional] |
|**tld** | **String** | Top level domain of the country (only for country placetype) |  [optional] |
|**yahooMapUrl** | **String** | The URL to get the location on Yahoo Map |  [optional] |
|**zipcodes** | **List&lt;String&gt;** | The zipcodes |  [optional] |



