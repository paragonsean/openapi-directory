# GooglePlayIntegrityApi.RequestDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **String** | Nonce that was provided in the request (which is base64 web-safe no-wrap). | [optional] 
**requestHash** | **String** | Request hash that was provided in the request. | [optional] 
**requestPackageName** | **String** | Required. Application package name this attestation was requested for. Note: This field makes no guarantees or promises on the caller integrity. For details on application integrity, check application_integrity. | [optional] 
**timestampMillis** | **String** | Required. Timestamp, in milliseconds, of the integrity application request. | [optional] 


