

# AuthorizationCodesSharedModelsAuthorizationCodeDefinition

Represents the model used to define how a type of authorization code is generated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationID** | **String** | The value used for securing codes generated. |  [optional] |
|**createdByUserID** | **Integer** | The ID of the user that created this definition. Read only. |  [optional] |
|**createdDate** | **OffsetDateTime** | A timestamp of when this definition was created. Read only. |  [optional] |
|**dataFields** | [**List&lt;AuthorizationCodesSharedModelsDataField&gt;**](AuthorizationCodesSharedModelsDataField.md) | The defined fields to include in authorization codes generated from this definition. May not be updated. |  [optional] |
|**deletedByUserID** | **Integer** | The ID of the user that deleted this definition. Read only. |  [optional] |
|**deletedDate** | **OffsetDateTime** | A timestamp of when this definition was deleted. Read only. |  [optional] |
|**description** | **String** | A description of this definition. May not be updated. |  [optional] |
|**durationAccuracy** | **Integer** | The number of bits used for timestamp verification. Defaults to 5. May not be updated. |  [optional] |
|**durationAmount** | **Integer** | The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated. |  [optional] |
|**durationUnits** | [**DurationUnitsEnum**](#DurationUnitsEnum) | The units of duration used to calculate the Authorization Code. Defaults to &#39;Days&#39;. May not be updated. |  [optional] |
|**hashLength** | **Integer** | The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated. |  [optional] |
|**ID** | **String** | The ID of the authorization code definition. Read only. |  [optional] |
|**isDeleted** | **Boolean** | Indicates whether this definition is enabled. True if generating codes is disabled. |  [optional] |
|**name** | **String** | The name of the authorization code definition. May not be updated. |  |
|**randomLength** | **Integer** | The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of \&quot;identical\&quot; authorization codes containing the same timestamp. Defaults to 5. May not be updated. |  [optional] |
|**validationFields** | [**List&lt;AuthorizationCodesSharedModelsValidationField&gt;**](AuthorizationCodesSharedModelsValidationField.md) | The defined fields to verify when reading authorization codes generated from this definition. May not be updated. |  [optional] |



## Enum: DurationUnitsEnum

| Name | Value |
|---- | -----|
| WEEKS | &quot;Weeks&quot; |
| DAYS | &quot;Days&quot; |
| HOURS | &quot;Hours&quot; |
| MINUTES | &quot;Minutes&quot; |



