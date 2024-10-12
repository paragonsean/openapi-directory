

# CertificateAddParameter

A certificate that can be installed on compute nodes and can be used to authenticate operations on the machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateFormat** | [**CertificateFormatEnum**](#CertificateFormatEnum) | Gets or sets the format of the certificate data. This must be pfx. |  [optional] |
|**data** | **String** | Gets or sets the base64-encoded contents of the .pfx file containing the certificate. The maximum size is 10KB. This property is not populated by the Get Certificate operation. |  |
|**password** | **String** | Gets or sets the password to access the certificate&#39;s private key. This property is not populated by the Get Certificate operation. |  [optional] |
|**thumbprint** | **String** | Get or sets the X.509 thumbprint of the certificate. This is a sequence of up to 40 hex digits (it may include spaces but these are removed). |  |
|**thumbprintAlgorithm** | **String** | Gets or sets the algorithm used to derive the thumbprint. This must be sha1. |  |



## Enum: CertificateFormatEnum

| Name | Value |
|---- | -----|
| PFX | &quot;pfx&quot; |
| CER | &quot;cer&quot; |
| UNMAPPED | &quot;unmapped&quot; |



