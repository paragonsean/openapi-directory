# BatchService.CertificateAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateFormat** | **String** | The format of the certificate data. | [optional] 
**data** | **String** | The base64-encoded contents of the certificate. The maximum size is 10KB. | 
**password** | **String** | The password to access the certificate&#39;s private key. | [optional] 
**thumbprint** | **String** | The X.509 thumbprint of the certificate. This is a sequence of up to 40 hex digits (it may include spaces but these are removed). | 
**thumbprintAlgorithm** | **String** | The algorithm used to derive the thumbprint. This must be sha1. | 



## Enum: CertificateFormatEnum


* `pfx` (value: `"pfx"`)

* `cer` (value: `"cer"`)

* `unmapped` (value: `"unmapped"`)




