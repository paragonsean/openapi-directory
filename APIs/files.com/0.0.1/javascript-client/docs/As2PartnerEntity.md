# FilesComApi.As2PartnerEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as2StationId** | **Number** | Id of the AS2 Station associated with this partner. | [optional] 
**enableDedicatedIps** | **Boolean** | &#x60;true&#x60; if remote server only accepts connections from dedicated IPs | [optional] 
**hexPublicCertificateSerial** | **String** | Serial of public certificate used for message security in hex format. | [optional] 
**id** | **Number** | Id of the AS2 Partner. | [optional] 
**name** | **String** | The partner&#39;s formal AS2 name. | [optional] 
**publicCertificateIssuer** | **String** | Issuer of public certificate used for message security. | [optional] 
**publicCertificateMd5** | **String** | MD5 hash of public certificate used for message security. | [optional] 
**publicCertificateNotAfter** | **String** | Not after value of public certificate used for message security. | [optional] 
**publicCertificateNotBefore** | **String** | Not before value of public certificate used for message security. | [optional] 
**publicCertificateSerial** | **String** | Serial of public certificate used for message security. | [optional] 
**publicCertificateSubject** | **String** | Subject of public certificate used for message security. | [optional] 
**serverCertificate** | **String** | Remote server certificate security setting | [optional] 
**uri** | **String** | Public URI for sending AS2 message to. | [optional] 



## Enum: ServerCertificateEnum


* `require_match` (value: `"require_match"`)

* `allow_any` (value: `"allow_any"`)




