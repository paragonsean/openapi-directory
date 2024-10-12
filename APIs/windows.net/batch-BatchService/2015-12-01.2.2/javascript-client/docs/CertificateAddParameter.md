# BatchService.CertificateAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateFormat** | **String** | Gets or sets the format of the certificate data. This must be pfx. | [optional] 
**data** | **String** | Gets or sets the base64-encoded contents of the .pfx file containing the certificate. The maximum size is 10KB. This property is not populated by the Get Certificate operation. | 
**password** | **String** | Gets or sets the password to access the certificate&#39;s private key. This property is not populated by the Get Certificate operation. | [optional] 
**thumbprint** | **String** | Get or sets the X.509 thumbprint of the certificate. This is a sequence of up to 40 hex digits (it may include spaces but these are removed). | 
**thumbprintAlgorithm** | **String** | Gets or sets the algorithm used to derive the thumbprint. This must be sha1. | 



## Enum: CertificateFormatEnum


* `pfx` (value: `"pfx"`)

* `cer` (value: `"cer"`)

* `unmapped` (value: `"unmapped"`)




