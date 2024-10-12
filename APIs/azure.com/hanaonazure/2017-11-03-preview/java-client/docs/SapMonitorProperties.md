

# SapMonitorProperties

Describes the properties of a SAP monitor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableCustomerAnalytics** | **Boolean** | The value indicating whether to send analytics to Microsoft |  [optional] |
|**hanaDbCredentialsMsiId** | **String** | MSI ID passed by customer which has access to customer&#39;s KeyVault and to be assigned to the Collector VM. |  [optional] |
|**hanaDbName** | **String** | Database name of the HANA instance. |  [optional] |
|**hanaDbPassword** | **String** | Database password of the HANA instance. |  [optional] |
|**hanaDbPasswordKeyVaultUrl** | **String** | KeyVault URL link to the password for the HANA database. |  [optional] |
|**hanaDbSqlPort** | **Integer** | Database port of the HANA instance. |  [optional] |
|**hanaDbUsername** | **String** | Database username of the HANA instance. |  [optional] |
|**hanaHostname** | **String** | Hostname of the HANA instance. |  [optional] |
|**hanaSubnet** | **String** | Specifies the SAP monitor unique ID. |  [optional] |
|**keyVaultId** | **String** | Key Vault ID containing customer&#39;s HANA credentials. |  [optional] |
|**logAnalyticsWorkspaceArmId** | **String** | The ARM ID of the Log Analytics Workspace that is used for monitoring |  [optional] |
|**logAnalyticsWorkspaceId** | **String** | The workspace ID of the log analytics workspace to be used for monitoring |  [optional] |
|**logAnalyticsWorkspaceSharedKey** | **String** | The shared key of the log analytics workspace that is used for monitoring |  [optional] |
|**managedResourceGroupName** | **String** | The name of the resource group the SAP Monitor resources get deployed into. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | State of provisioning of the HanaInstance |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DELETING | &quot;Deleting&quot; |
| MIGRATING | &quot;Migrating&quot; |



