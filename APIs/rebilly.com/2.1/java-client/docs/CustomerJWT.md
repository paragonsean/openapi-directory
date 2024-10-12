

# CustomerJWT


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;CustomerLink&gt;**](CustomerLink.md) | The links related to resource. |  [optional] [readonly] |
|**acl** | [**List&lt;AclInner&gt;**](AclInner.md) |  |  [optional] |
|**createdTime** | **OffsetDateTime** | Session created time. |  [optional] [readonly] |
|**customClaims** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**customerId** | **String** | The customer&#39;s ID. |  [optional] [readonly] |
|**expiredTime** | **OffsetDateTime** | Session expired time. Defaults to one hour. |  [optional] |
|**id** | **String** | The session identifier string. |  [optional] [readonly] |
|**invalidate** | **Boolean** | Whether to invalidate token after exchange or not. |  [optional] |
|**oneTimePassword** | **String** | The one time password sent via an email. Should contain digits only. |  [optional] |
|**token** | **String** | The session&#39;s token used for authentication. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Session type. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Session updated time. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;customer&quot; |



