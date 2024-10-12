

# IngressFrom

Defines the conditions under which an IngressPolicy matches a request. Conditions are based on information about the source of the request. The request must satisfy what is defined in `sources` AND identity related fields in order to match.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identities** | **List&lt;String&gt;** | A list of identities that are allowed access through this ingress policy, in the format of &#x60;user:{email_id}&#x60; or &#x60;serviceAccount:{email_id}&#x60;. |  [optional] |
|**identityType** | [**IdentityTypeEnum**](#IdentityTypeEnum) | Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of &#x60;identities&#x60; field will be allowed access. |  [optional] |
|**sources** | [**List&lt;IngressSource&gt;**](IngressSource.md) | Sources that this IngressPolicy authorizes access from. |  [optional] |



## Enum: IdentityTypeEnum

| Name | Value |
|---- | -----|
| IDENTITY_TYPE_UNSPECIFIED | &quot;IDENTITY_TYPE_UNSPECIFIED&quot; |
| ANY_IDENTITY | &quot;ANY_IDENTITY&quot; |
| ANY_USER_ACCOUNT | &quot;ANY_USER_ACCOUNT&quot; |
| ANY_SERVICE_ACCOUNT | &quot;ANY_SERVICE_ACCOUNT&quot; |



