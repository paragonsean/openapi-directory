# BackupAndDrServiceApi.ManagementServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the instance was created. | [optional] [readonly] 
**description** | **String** | Optional. The description of the ManagementServer instance (2048 characters or less). | [optional] 
**etag** | **String** | Optional. Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. | [optional] 
**labels** | **{String: String}** | Optional. Resource labels to represent user provided metadata. Labels currently defined: 1. migrate_from_go&#x3D; If set to true, the MS is created in migration ready mode. | [optional] 
**managementUri** | [**ManagementURI**](ManagementURI.md) |  | [optional] 
**name** | **String** | Output only. Identifier. The resource name. | [optional] [readonly] 
**networks** | [**[NetworkConfig]**](NetworkConfig.md) | Required. VPC networks to which the ManagementServer instance is connected. For this version, only a single network is supported. | [optional] 
**oauth2ClientId** | **String** | Output only. The OAuth 2.0 client id is required to make API calls to the BackupDR instance API of this ManagementServer. This is the value that should be provided in the ‘aud’ field of the OIDC ID Token (see openid specification https://openid.net/specs/openid-connect-core-1_0.html#IDToken). | [optional] [readonly] 
**state** | **String** | Output only. The ManagementServer state. | [optional] [readonly] 
**type** | **String** | Optional. The type of the ManagementServer resource. | [optional] 
**updateTime** | **String** | Output only. The time when the instance was updated. | [optional] [readonly] 
**workforceIdentityBasedManagementUri** | [**WorkforceIdentityBasedManagementURI**](WorkforceIdentityBasedManagementURI.md) |  | [optional] 
**workforceIdentityBasedOauth2ClientId** | [**WorkforceIdentityBasedOAuth2ClientID**](WorkforceIdentityBasedOAuth2ClientID.md) |  | [optional] 



## Enum: StateEnum


* `INSTANCE_STATE_UNSPECIFIED` (value: `"INSTANCE_STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `REPAIRING` (value: `"REPAIRING"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)

* `ERROR` (value: `"ERROR"`)





## Enum: TypeEnum


* `INSTANCE_TYPE_UNSPECIFIED` (value: `"INSTANCE_TYPE_UNSPECIFIED"`)

* `BACKUP_RESTORE` (value: `"BACKUP_RESTORE"`)




