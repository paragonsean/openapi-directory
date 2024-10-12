# CloudKeyManagementServiceKmsApi.KeyOperationAttestation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certChains** | [**CertificateChains**](CertificateChains.md) |  | [optional] 
**content** | **Blob** | Output only. The attestation data provided by the HSM when the key operation was performed. | [optional] [readonly] 
**format** | **String** | Output only. The format of the attestation data. | [optional] [readonly] 



## Enum: FormatEnum


* `ATTESTATION_FORMAT_UNSPECIFIED` (value: `"ATTESTATION_FORMAT_UNSPECIFIED"`)

* `CAVIUM_V1_COMPRESSED` (value: `"CAVIUM_V1_COMPRESSED"`)

* `CAVIUM_V2_COMPRESSED` (value: `"CAVIUM_V2_COMPRESSED"`)




