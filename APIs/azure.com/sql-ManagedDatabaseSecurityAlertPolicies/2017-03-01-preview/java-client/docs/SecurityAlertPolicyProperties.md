

# SecurityAlertPolicyProperties

Properties of a security alert policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Specifies the UTC creation time of the policy. |  [optional] [readonly] |
|**disabledAlerts** | **List&lt;String&gt;** | Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action |  [optional] |
|**emailAccountAdmins** | **Boolean** | Specifies that the alert is sent to the account administrators. |  [optional] |
|**emailAddresses** | **List&lt;String&gt;** | Specifies an array of e-mail addresses to which the alert is sent. |  [optional] |
|**retentionDays** | **Integer** | Specifies the number of days to keep in the Threat Detection audit logs. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database. |  |
|**storageAccountAccessKey** | **String** | Specifies the identifier key of the Threat Detection audit storage account. |  [optional] |
|**storageEndpoint** | **String** | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



