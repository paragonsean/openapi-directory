# RebillyRestApi.CustomerJWT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[CustomerLink]**](CustomerLink.md) | The links related to resource. | [optional] [readonly] 
**acl** | [**[AclInner]**](AclInner.md) |  | [optional] 
**createdTime** | **Date** | Session created time. | [optional] [readonly] 
**customClaims** | **{String: Object}** |  | [optional] 
**customerId** | **String** | The customer&#39;s ID. | [optional] [readonly] 
**expiredTime** | **Date** | Session expired time. Defaults to one hour. | [optional] 
**id** | **String** | The session identifier string. | [optional] [readonly] 
**invalidate** | **Boolean** | Whether to invalidate token after exchange or not. | [optional] [default to true]
**oneTimePassword** | **String** | The one time password sent via an email. Should contain digits only. | [optional] 
**token** | **String** | The session&#39;s token used for authentication. | [optional] [readonly] 
**type** | **String** | Session type. | [optional] [readonly] 
**updatedTime** | **Date** | Session updated time. | [optional] [readonly] 



## Enum: TypeEnum


* `customer` (value: `"customer"`)




