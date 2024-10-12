

# DatabaseBlobAuditingPolicyProperties

Properties of a database blob auditing policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditActionsAndGroups** | **List&lt;String&gt;** | Specifies the Actions and Actions-Groups to audit. |  [optional] |
|**isStorageSecondaryKeyInUse** | **Boolean** | Specifies whether storageAccountAccessKey value is the storage’s secondary key. |  [optional] |
|**retentionDays** | **Integer** | Specifies the number of days to keep in the audit logs. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Specifies the state of the policy. If state is Enabled, storageEndpoint and storageAccountAccessKey are required. |  |
|**storageAccountAccessKey** | **String** | Specifies the identifier key of the auditing storage account. If state is Enabled, storageAccountAccessKey is required. |  [optional] |
|**storageAccountSubscriptionId** | **UUID** | Specifies the blob storage subscription Id. |  [optional] |
|**storageEndpoint** | **String** | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint is required. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



