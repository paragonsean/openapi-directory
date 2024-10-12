

# KeyOperationAttestation

Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations] (https://cloud.google.com/kms/docs/attest-key).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certChains** | [**CertificateChains**](CertificateChains.md) |  |  [optional] |
|**content** | **byte[]** | Output only. The attestation data provided by the HSM when the key operation was performed. |  [optional] [readonly] |
|**format** | [**FormatEnum**](#FormatEnum) | Output only. The format of the attestation data. |  [optional] [readonly] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| ATTESTATION_FORMAT_UNSPECIFIED | &quot;ATTESTATION_FORMAT_UNSPECIFIED&quot; |
| CAVIUM_V1_COMPRESSED | &quot;CAVIUM_V1_COMPRESSED&quot; |
| CAVIUM_V2_COMPRESSED | &quot;CAVIUM_V2_COMPRESSED&quot; |



