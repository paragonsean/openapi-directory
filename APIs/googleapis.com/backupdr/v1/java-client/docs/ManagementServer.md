

# ManagementServer

ManagementServer describes a single BackupDR ManagementServer instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the instance was created. |  [optional] [readonly] |
|**description** | **String** | Optional. The description of the ManagementServer instance (2048 characters or less). |  [optional] |
|**etag** | **String** | Optional. Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user provided metadata. Labels currently defined: 1. migrate_from_go&#x3D; If set to true, the MS is created in migration ready mode. |  [optional] |
|**managementUri** | [**ManagementURI**](ManagementURI.md) |  |  [optional] |
|**name** | **String** | Output only. Identifier. The resource name. |  [optional] [readonly] |
|**networks** | [**List&lt;NetworkConfig&gt;**](NetworkConfig.md) | Required. VPC networks to which the ManagementServer instance is connected. For this version, only a single network is supported. |  [optional] |
|**oauth2ClientId** | **String** | Output only. The OAuth 2.0 client id is required to make API calls to the BackupDR instance API of this ManagementServer. This is the value that should be provided in the ‘aud’ field of the OIDC ID Token (see openid specification https://openid.net/specs/openid-connect-core-1_0.html#IDToken). |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The ManagementServer state. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. The type of the ManagementServer resource. |  [optional] |
|**updateTime** | **String** | Output only. The time when the instance was updated. |  [optional] [readonly] |
|**workforceIdentityBasedManagementUri** | [**WorkforceIdentityBasedManagementURI**](WorkforceIdentityBasedManagementURI.md) |  |  [optional] |
|**workforceIdentityBasedOauth2ClientId** | [**WorkforceIdentityBasedOAuth2ClientID**](WorkforceIdentityBasedOAuth2ClientID.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| INSTANCE_STATE_UNSPECIFIED | &quot;INSTANCE_STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| REPAIRING | &quot;REPAIRING&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| ERROR | &quot;ERROR&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INSTANCE_TYPE_UNSPECIFIED | &quot;INSTANCE_TYPE_UNSPECIFIED&quot; |
| BACKUP_RESTORE | &quot;BACKUP_RESTORE&quot; |



