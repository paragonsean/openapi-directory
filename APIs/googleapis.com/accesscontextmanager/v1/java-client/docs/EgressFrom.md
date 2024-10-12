

# EgressFrom

Defines the conditions under which an EgressPolicy matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identities** | **List&lt;String&gt;** | A list of identities that are allowed access through this [EgressPolicy], in the format of &#x60;user:{email_id}&#x60; or &#x60;serviceAccount:{email_id}&#x60;. |  [optional] |
|**identityType** | [**IdentityTypeEnum**](#IdentityTypeEnum) | Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of &#x60;identities&#x60; field will be allowed access. |  [optional] |
|**sourceRestriction** | [**SourceRestrictionEnum**](#SourceRestrictionEnum) | Whether to enforce traffic restrictions based on &#x60;sources&#x60; field. If the &#x60;sources&#x60; fields is non-empty, then this field must be set to &#x60;SOURCE_RESTRICTION_ENABLED&#x60;. |  [optional] |
|**sources** | [**List&lt;EgressSource&gt;**](EgressSource.md) | Sources that this EgressPolicy authorizes access from. If this field is not empty, then &#x60;source_restriction&#x60; must be set to &#x60;SOURCE_RESTRICTION_ENABLED&#x60;. |  [optional] |



## Enum: IdentityTypeEnum

| Name | Value |
|---- | -----|
| IDENTITY_TYPE_UNSPECIFIED | &quot;IDENTITY_TYPE_UNSPECIFIED&quot; |
| ANY_IDENTITY | &quot;ANY_IDENTITY&quot; |
| ANY_USER_ACCOUNT | &quot;ANY_USER_ACCOUNT&quot; |
| ANY_SERVICE_ACCOUNT | &quot;ANY_SERVICE_ACCOUNT&quot; |



## Enum: SourceRestrictionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SOURCE_RESTRICTION_UNSPECIFIED&quot; |
| ENABLED | &quot;SOURCE_RESTRICTION_ENABLED&quot; |
| DISABLED | &quot;SOURCE_RESTRICTION_DISABLED&quot; |



