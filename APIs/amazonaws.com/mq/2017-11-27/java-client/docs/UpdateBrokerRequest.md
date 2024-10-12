

# UpdateBrokerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationStrategy** | [**AuthenticationStrategyEnum**](#AuthenticationStrategyEnum) | Optional. The authentication strategy used to secure the broker. The default is SIMPLE. |  [optional] |
|**autoMinorVersionUpgrade** | **Boolean** | Enables automatic upgrades to new minor versions for brokers, as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot. |  [optional] |
|**_configuration** | [**CreateBrokerRequestConfiguration**](CreateBrokerRequestConfiguration.md) |  |  [optional] |
|**engineVersion** | **String** | The broker engine version. For a list of supported engine versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker-engine.html\&quot;&gt;Supported engines&lt;/a&gt;. |  [optional] |
|**hostInstanceType** | **String** | The broker&#39;s host instance type to upgrade to. For a list of supported instance types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types\&quot;&gt;Broker instance types&lt;/a&gt;. |  [optional] |
|**ldapServerMetadata** | [**CreateBrokerRequestLdapServerMetadata**](CreateBrokerRequestLdapServerMetadata.md) |  |  [optional] |
|**logs** | [**CreateBrokerRequestLogs**](CreateBrokerRequestLogs.md) |  |  [optional] |
|**maintenanceWindowStartTime** | [**CreateBrokerRequestMaintenanceWindowStartTime**](CreateBrokerRequestMaintenanceWindowStartTime.md) |  |  [optional] |
|**securityGroups** | **List&lt;String&gt;** | The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers. |  [optional] |
|**dataReplicationMode** | [**DataReplicationModeEnum**](#DataReplicationModeEnum) | Specifies whether a broker is a part of a data replication pair. |  [optional] |



## Enum: AuthenticationStrategyEnum

| Name | Value |
|---- | -----|
| SIMPLE | &quot;SIMPLE&quot; |
| LDAP | &quot;LDAP&quot; |



## Enum: DataReplicationModeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| CRDR | &quot;CRDR&quot; |



