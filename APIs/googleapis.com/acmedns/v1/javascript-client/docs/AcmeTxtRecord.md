# AcmeDnsApi.AcmeTxtRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **String** | Holds the ACME challenge data put in the TXT record. This will be checked to be a valid TXT record data entry. | [optional] 
**fqdn** | **String** | The domain/subdomain for the record. In a request, this MAY be Unicode or Punycode. In a response, this will be in Unicode. The fqdn MUST contain the root_domain field on the request. | [optional] 
**updateTime** | **String** | Output only. The time when this record was last updated. This will be in UTC time. | [optional] [readonly] 


