

# CertificateAddParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateFormat** | [**CertificateFormatEnum**](#CertificateFormatEnum) |  |  [optional] |
|**data** | **String** |  |  |
|**password** | **String** | This is required if the Certificate format is pfx. It should be omitted if the Certificate format is cer. |  [optional] |
|**thumbprint** | **String** |  |  |
|**thumbprintAlgorithm** | **String** |  |  |



## Enum: CertificateFormatEnum

| Name | Value |
|---- | -----|
| PFX | &quot;pfx&quot; |
| CER | &quot;cer&quot; |



