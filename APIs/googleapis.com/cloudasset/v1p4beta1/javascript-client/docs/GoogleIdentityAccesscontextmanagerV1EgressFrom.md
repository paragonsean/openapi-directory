# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1EgressFrom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | **[String]** | A list of identities that are allowed access through this [EgressPolicy]. Should be in the format of email address. The email address should represent individual user or service account only. | [optional] 
**identityType** | **String** | Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of &#x60;identities&#x60; field will be allowed access. | [optional] 



## Enum: IdentityTypeEnum


* `IDENTITY_TYPE_UNSPECIFIED` (value: `"IDENTITY_TYPE_UNSPECIFIED"`)

* `ANY_IDENTITY` (value: `"ANY_IDENTITY"`)

* `ANY_USER_ACCOUNT` (value: `"ANY_USER_ACCOUNT"`)

* `ANY_SERVICE_ACCOUNT` (value: `"ANY_SERVICE_ACCOUNT"`)




