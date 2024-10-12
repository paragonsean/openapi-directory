# FrankieFinancialApi.DOBObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | ISO-3166-1 code for the country of birth. You must use the alpha3 country code (e.g. AUS, USA, IDR, KOR, etc) We&#39;ll convert as needed.  See https://en.wikipedia.org/wiki/ISO_3166-1  | [optional] 
**dateOfBirth** | **Date** | Date of Birth in YYYY-MM-DD format | [optional] 
**locality** | **String** | Place of birth other than country If locality is given, then country must also be provided.  | [optional] 
**yearOfBirth** | **String** | Year of birth or \&quot;unknown\&quot;. This will be autoextracted if dateOfBirth is supplied. | [optional] 


