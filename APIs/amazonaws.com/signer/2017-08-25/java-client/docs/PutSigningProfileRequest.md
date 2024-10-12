

# PutSigningProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**signingMaterial** | [**PutSigningProfileRequestSigningMaterial**](PutSigningProfileRequestSigningMaterial.md) |  |  [optional] |
|**signatureValidityPeriod** | [**PutSigningProfileRequestSignatureValidityPeriod**](PutSigningProfileRequestSignatureValidityPeriod.md) |  |  [optional] |
|**platformId** | **String** | The ID of the signing platform to be created. |  |
|**overrides** | [**PutSigningProfileRequestOverrides**](PutSigningProfileRequestOverrides.md) |  |  [optional] |
|**signingParameters** | **Map&lt;String, String&gt;** | Map of key-value pairs for signing. These can include any information that you want to use during signing. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags to be associated with the signing profile that is being created. |  [optional] |



