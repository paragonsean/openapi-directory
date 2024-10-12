

# AnalysisServicesServerMutableProperties

An object that represents a set of mutable Analysis Services resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asAdministrators** | [**ServerAdministrators**](ServerAdministrators.md) |  |  [optional] |
|**backupBlobContainerUri** | **String** | The SAS container URI to the backup container. |  [optional] |
|**gatewayDetails** | [**GatewayDetails**](GatewayDetails.md) |  |  [optional] |
|**ipV4FirewallSettings** | [**IPv4FirewallSettings**](IPv4FirewallSettings.md) |  |  [optional] |
|**querypoolConnectionMode** | [**QuerypoolConnectionModeEnum**](#QuerypoolConnectionModeEnum) | How the read-write server&#39;s participation in the query pool is controlled.&lt;br/&gt;It can have the following values: &lt;ul&gt;&lt;li&gt;readOnly - indicates that the read-write server is intended not to participate in query operations&lt;/li&gt;&lt;li&gt;all - indicates that the read-write server can participate in query operations&lt;/li&gt;&lt;/ul&gt;Specifying readOnly when capacity is 1 results in error. |  [optional] |



## Enum: QuerypoolConnectionModeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |



