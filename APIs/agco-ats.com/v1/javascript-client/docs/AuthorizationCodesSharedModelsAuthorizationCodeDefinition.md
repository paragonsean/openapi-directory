# AgcoApi.AuthorizationCodesSharedModelsAuthorizationCodeDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationID** | **String** | The value used for securing codes generated. | [optional] 
**createdByUserID** | **Number** | The ID of the user that created this definition. Read only. | [optional] 
**createdDate** | **Date** | A timestamp of when this definition was created. Read only. | [optional] 
**dataFields** | [**[AuthorizationCodesSharedModelsDataField]**](AuthorizationCodesSharedModelsDataField.md) | The defined fields to include in authorization codes generated from this definition. May not be updated. | [optional] 
**deletedByUserID** | **Number** | The ID of the user that deleted this definition. Read only. | [optional] 
**deletedDate** | **Date** | A timestamp of when this definition was deleted. Read only. | [optional] 
**description** | **String** | A description of this definition. May not be updated. | [optional] 
**durationAccuracy** | **Number** | The number of bits used for timestamp verification. Defaults to 5. May not be updated. | [optional] 
**durationAmount** | **Number** | The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated. | [optional] 
**durationUnits** | **String** | The units of duration used to calculate the Authorization Code. Defaults to &#39;Days&#39;. May not be updated. | [optional] 
**hashLength** | **Number** | The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated. | [optional] 
**ID** | **String** | The ID of the authorization code definition. Read only. | [optional] 
**isDeleted** | **Boolean** | Indicates whether this definition is enabled. True if generating codes is disabled. | [optional] 
**name** | **String** | The name of the authorization code definition. May not be updated. | 
**randomLength** | **Number** | The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of \&quot;identical\&quot; authorization codes containing the same timestamp. Defaults to 5. May not be updated. | [optional] 
**validationFields** | [**[AuthorizationCodesSharedModelsValidationField]**](AuthorizationCodesSharedModelsValidationField.md) | The defined fields to verify when reading authorization codes generated from this definition. May not be updated. | [optional] 



## Enum: DurationUnitsEnum


* `Weeks` (value: `"Weeks"`)

* `Days` (value: `"Days"`)

* `Hours` (value: `"Hours"`)

* `Minutes` (value: `"Minutes"`)




