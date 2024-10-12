# PostgreSqlManagementClient.SecurityAlertPolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabledAlerts** | **[String]** | Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly | [optional] 
**emailAccountAdmins** | **Boolean** | Specifies that the alert is sent to the account administrators. | [optional] 
**emailAddresses** | **[String]** | Specifies an array of e-mail addresses to which the alert is sent. | [optional] 
**retentionDays** | **Number** | Specifies the number of days to keep in the Threat Detection audit logs. | [optional] 
**state** | **String** | Specifies the state of the policy, whether it is enabled or disabled. | 
**storageAccountAccessKey** | **String** | Specifies the identifier key of the Threat Detection audit storage account. | [optional] 
**storageEndpoint** | **String** | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. | [optional] 



## Enum: StateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




