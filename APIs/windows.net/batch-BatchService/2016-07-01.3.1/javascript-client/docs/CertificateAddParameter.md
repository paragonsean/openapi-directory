# BatchService.CertificateAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateFormat** | **String** |  | [optional] 
**data** | **String** |  | 
**password** | **String** | This is required if the certificate format is pfx. It should be omitted if the certificate format is cer. | [optional] 
**thumbprint** | **String** |  | 
**thumbprintAlgorithm** | **String** |  | 



## Enum: CertificateFormatEnum


* `pfx` (value: `"pfx"`)

* `cer` (value: `"cer"`)

* `unmapped` (value: `"unmapped"`)




