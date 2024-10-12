

# CertificateBaseProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx. |  [optional] |
|**thumbprint** | **String** | This must match the thumbprint from the name. |  [optional] |
|**thumbprintAlgorithm** | **String** | This must match the first portion of the certificate name. Currently required to be &#39;SHA1&#39;. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PFX | &quot;Pfx&quot; |
| CER | &quot;Cer&quot; |



