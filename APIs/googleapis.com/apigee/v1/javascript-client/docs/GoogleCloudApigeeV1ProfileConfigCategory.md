# ApigeeApi.GoogleCloudApigeeV1ProfileConfigCategory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abuse** | **Object** | Checks for abuse, which includes any requests sent to the API for purposes other than what it is intended for, such as high volumes of requests, data scraping, and abuse related to authorization. | [optional] 
**authorization** | **Object** | By default, following policies will be included: - JWS - JWT - OAuth - BasicAuth - APIKey | [optional] 
**cors** | **Object** | Checks to see if you have CORS policy in place. | [optional] 
**mediation** | **Object** | By default, following policies will be included: - OASValidation - SOAPMessageValidation | [optional] 
**mtls** | **Object** | Checks to see if you have configured mTLS for the target server. | [optional] 
**threat** | **Object** | By default, following policies will be included: - XMLThreatProtection - JSONThreatProtection | [optional] 


