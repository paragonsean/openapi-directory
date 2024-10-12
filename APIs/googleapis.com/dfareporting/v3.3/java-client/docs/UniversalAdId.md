

# UniversalAdId

A Universal Ad ID as per the VAST 4.0 spec. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and VPAID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**registry** | [**RegistryEnum**](#RegistryEnum) | Registry used for the Ad ID value. |  [optional] |
|**value** | **String** | ID value for this creative. Only alphanumeric characters and the following symbols are valid: \&quot;_/\\-\&quot;. Maximum length is 64 characters. Read only when registry is DCM. |  [optional] |



## Enum: RegistryEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;OTHER&quot; |
| AD_ID_ORG | &quot;AD_ID.ORG&quot; |
| CLEARCAST | &quot;CLEARCAST&quot; |
| DCM | &quot;DCM&quot; |



