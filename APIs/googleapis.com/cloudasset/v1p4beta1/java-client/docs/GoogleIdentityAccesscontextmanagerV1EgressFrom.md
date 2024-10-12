

# GoogleIdentityAccesscontextmanagerV1EgressFrom

Defines the conditions under which an EgressPolicy matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identities** | **List&lt;String&gt;** | A list of identities that are allowed access through this [EgressPolicy]. Should be in the format of email address. The email address should represent individual user or service account only. |  [optional] |
|**identityType** | [**IdentityTypeEnum**](#IdentityTypeEnum) | Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of &#x60;identities&#x60; field will be allowed access. |  [optional] |



## Enum: IdentityTypeEnum

| Name | Value |
|---- | -----|
| IDENTITY_TYPE_UNSPECIFIED | &quot;IDENTITY_TYPE_UNSPECIFIED&quot; |
| ANY_IDENTITY | &quot;ANY_IDENTITY&quot; |
| ANY_USER_ACCOUNT | &quot;ANY_USER_ACCOUNT&quot; |
| ANY_SERVICE_ACCOUNT | &quot;ANY_SERVICE_ACCOUNT&quot; |



