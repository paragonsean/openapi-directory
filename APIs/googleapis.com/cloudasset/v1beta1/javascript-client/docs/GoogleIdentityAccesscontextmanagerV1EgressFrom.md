# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1EgressFrom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | **[String]** | A list of identities that are allowed access through this [EgressPolicy], in the format of &#x60;user:{email_id}&#x60; or &#x60;serviceAccount:{email_id}&#x60;. | [optional] 
**identityType** | **String** | Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of &#x60;identities&#x60; field will be allowed access. | [optional] 
**sourceRestriction** | **String** | Whether to enforce traffic restrictions based on &#x60;sources&#x60; field. If the &#x60;sources&#x60; fields is non-empty, then this field must be set to &#x60;SOURCE_RESTRICTION_ENABLED&#x60;. | [optional] 
**sources** | [**[GoogleIdentityAccesscontextmanagerV1EgressSource]**](GoogleIdentityAccesscontextmanagerV1EgressSource.md) | Sources that this EgressPolicy authorizes access from. If this field is not empty, then &#x60;source_restriction&#x60; must be set to &#x60;SOURCE_RESTRICTION_ENABLED&#x60;. | [optional] 



## Enum: IdentityTypeEnum


* `IDENTITY_TYPE_UNSPECIFIED` (value: `"IDENTITY_TYPE_UNSPECIFIED"`)

* `ANY_IDENTITY` (value: `"ANY_IDENTITY"`)

* `ANY_USER_ACCOUNT` (value: `"ANY_USER_ACCOUNT"`)

* `ANY_SERVICE_ACCOUNT` (value: `"ANY_SERVICE_ACCOUNT"`)





## Enum: SourceRestrictionEnum


* `UNSPECIFIED` (value: `"SOURCE_RESTRICTION_UNSPECIFIED"`)

* `ENABLED` (value: `"SOURCE_RESTRICTION_ENABLED"`)

* `DISABLED` (value: `"SOURCE_RESTRICTION_DISABLED"`)




