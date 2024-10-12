

# HpcerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateParameters** | [**HpcerRequestCertificateParameters**](HpcerRequestCertificateParameters.md) |  |  [optional] |
|**consentArtifact** | [**ConsentArtifactSchema**](ConsentArtifactSchema.md) |  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The format of the certificate in response. |  |
|**txnId** | **UUID** | A unique transaction id for this request in UUID format. It is used for tracking the request. |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| XML | &quot;xml&quot; |
| PDF | &quot;pdf&quot; |



