# ZipCodeDataApi.Zipcode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cityAliases** | [**[ZipcodeCityAliasesInner]**](ZipcodeCityAliasesInner.md) | Array that contains all the city aliases for the given zip code. | 
**countyFipsCode** | **String** | FIPS code assigned to the county of the main city of the zip code. | 
**divisionCode** | **String** | Division Code. Part of the geographical hierarchy of the US provided by the united states census. | 
**divisionName** | **String** | Division Name. Part of the geographical hierarchy of the US provided by the united states census. | 
**landAreaKm2** | **Number** | Zip Code Land Area in square kilometers. | 
**landAreaMi2** | **Number** | Zip Code Land area in Square Miles | 
**latitude** | **Number** | Zip Code Latitude | [optional] 
**longitude** | **Number** | Zip Code Longitude | [optional] 
**msaCode** | **String** | 5 digit MSA (Metropolitan Statistical Area) code. | 
**msaName** | **String** | Name of the defined MSA code. | 
**regionCode** | **String** | Region Code. Part of the geographical hierarchy of the US provided by the united states census. | 
**regionName** | **String** | Region Name. Part of the geographical hierarchy of the US provided by the united states census. | 
**stateAbbr** | **String** | Abbreviation for state name. | 
**stateCode** | **String** | Standard 2 character state code. | 
**stateFipsCode** | **String** | Federal Information Processing Standards 2 digit assigned code. | 
**stateName** | **String** | State Name | 
**titleCaseCityName** | **String** | USPS City / Town Name for the main city of the zip code. Title Case Format. | 
**titleCaseCountyName** | **String** | Main County Name in Title Case | 
**uniqueZipNameInd** | **Boolean** | True &#x3D; Unique Zip Code Name. False the zip code name is not unique. | 
**uspsCarrierRouteRateSortDesc** | **String** | Description for the carrier route code. | 
**uspsCarrierRouteSortCode** | **String** | Code for the available carrier route. | 
**uspsCityMailingInd** | **Boolean** | City names with the City State Mailing Name indicator flag set to True are considered part of a complete and standardized address; city names with the flag set to false  file should not be used in a complete and standardized address. | 
**uspsCountyName** | **String** | Name of the county of the main city for the zip code. | 
**uspsDeliveryCode** | **String** | Determines if the zip code city has Carrier Routes. | 
**uspsDeliveryDesc** | **String** | Determines if the zip code city has Carrier Routes. | 
**uspsFacilityCode** | **String** | Facility code provided by the USPS. B&#x3D;Branch, C&#x3D;Community Post Office, N &#x3D; Non-Postal Community Name, former postal facility or place name, P&#x3D; Post Office, S&#x3D;Station, U &#x3D; Urbanization | 
**uspsFacilityName** | **String** | USPS Facility Name  B&#x3D;Branch, C&#x3D;Community Post Office, N &#x3D; Non-Postal Community Name, former postal facility or place name, P&#x3D; Post Office, S&#x3D;Station, U &#x3D; Urbanization | 
**uspsFinanceNumber** | **String** | USPS Provided Finance Number. This code is assigned to postal service facilities. | 
**uspsMainCityKey** | **String** | USPS City / Town key identifier for the main city of the zip code. | 
**uspsMainCityName** | **String** | USPS City / Town Name for the main city of the zip code. USPS Upper Case Format. | 
**waterAreaKm2** | **Number** | Zip Code water area in Square kilometers. | 
**waterAreaMi2** | **Number** | Zip Code Water Area in Square Miles | 
**zipClassificationCode** | **String** | Code provided by USPS for the type of Zip Code it represents.  P &#x3D; PO Box Zip, U &#x3D; Unique Zip, M &#x3D; APO/FPO Military Zip , null (not provided by USPS),N &#x3D; Non-Unique Zip. | 
**zipClassificationDesc** | **String** | Description of the zip classification code.   P &#x3D; PO Box Zip, U &#x3D; Unique Zip, M &#x3D; APO/FPO Military Zip , null (not provided by USPS), &#x3D; Non-Unique Zip. | 
**zipCode** | **String** | 5 Digit Zip Code. Zone Improvement Plan. | 
**zipCodeStatistics** | [**[ZipcodeZipCodeStatisticsInner]**](ZipcodeZipCodeStatisticsInner.md) | Available statistics by year of the Zip Code. | 


