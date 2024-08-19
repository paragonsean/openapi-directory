# BatchManagement.CertificateCreateOrUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **String** | The maximum size is 10KB. | 
**password** | **String** | This is required if the certificate format is pfx and must be omitted if the certificate format is cer. | [optional] 
**format** | **String** | The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx. | [optional] 
**thumbprint** | **String** | This must match the thumbprint from the name. | [optional] 
**thumbprintAlgorithm** | **String** | This must match the first portion of the certificate name. Currently required to be &#39;SHA1&#39;. | [optional] 



## Enum: FormatEnum


* `Pfx` (value: `"Pfx"`)

* `Cer` (value: `"Cer"`)




