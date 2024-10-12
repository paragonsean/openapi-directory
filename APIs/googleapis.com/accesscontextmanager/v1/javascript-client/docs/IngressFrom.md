# AccessContextManagerApi.IngressFrom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | **[String]** | A list of identities that are allowed access through this ingress policy, in the format of &#x60;user:{email_id}&#x60; or &#x60;serviceAccount:{email_id}&#x60;. | [optional] 
**identityType** | **String** | Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of &#x60;identities&#x60; field will be allowed access. | [optional] 
**sources** | [**[IngressSource]**](IngressSource.md) | Sources that this IngressPolicy authorizes access from. | [optional] 



## Enum: IdentityTypeEnum


* `IDENTITY_TYPE_UNSPECIFIED` (value: `"IDENTITY_TYPE_UNSPECIFIED"`)

* `ANY_IDENTITY` (value: `"ANY_IDENTITY"`)

* `ANY_USER_ACCOUNT` (value: `"ANY_USER_ACCOUNT"`)

* `ANY_SERVICE_ACCOUNT` (value: `"ANY_SERVICE_ACCOUNT"`)




