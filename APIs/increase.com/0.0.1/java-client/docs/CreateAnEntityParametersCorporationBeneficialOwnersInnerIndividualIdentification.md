

# CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentification

A means of verifying the person's identity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**driversLicense** | [**CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentificationDriversLicense**](CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentificationDriversLicense.md) |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | A method that can be used to verify the individual&#39;s identity. |  |
|**number** | **String** | An identification number that can be used to verify the individual&#39;s identity, such as a social security number. |  |
|**other** | [**CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentificationOther**](CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentificationOther.md) |  |  [optional] |
|**passport** | [**CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentificationPassport**](CreateAnEntityParametersCorporationBeneficialOwnersInnerIndividualIdentificationPassport.md) |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| SOCIAL_SECURITY_NUMBER | &quot;social_security_number&quot; |
| INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER | &quot;individual_taxpayer_identification_number&quot; |
| PASSPORT | &quot;passport&quot; |
| DRIVERS_LICENSE | &quot;drivers_license&quot; |
| OTHER | &quot;other&quot; |



