

# CreateBrokerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationStrategy** | [**AuthenticationStrategyEnum**](#AuthenticationStrategyEnum) | Optional. The authentication strategy used to secure the broker. The default is SIMPLE. |  [optional] |
|**autoMinorVersionUpgrade** | **Boolean** | Enables automatic upgrades to new minor versions for brokers, as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot. Set to true by default, if no value is specified. |  |
|**brokerName** | **String** | &lt;p&gt;Required. The broker&#39;s name. This value must be unique in your Amazon Web Services account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.&lt;/p&gt; &lt;important&gt;&lt;p&gt;Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.&lt;/p&gt;&lt;/important&gt; |  |
|**_configuration** | [**CreateBrokerRequestConfiguration**](CreateBrokerRequestConfiguration.md) |  |  [optional] |
|**creatorRequestId** | **String** | &lt;p&gt;The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action.&lt;/p&gt; &lt;note&gt;&lt;p&gt;We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesn&#39;t require idempotency.&lt;/p&gt;&lt;/note&gt; |  [optional] |
|**deploymentMode** | [**DeploymentModeEnum**](#DeploymentModeEnum) | The broker&#39;s deployment mode. |  |
|**encryptionOptions** | [**CreateBrokerRequestEncryptionOptions**](CreateBrokerRequestEncryptionOptions.md) |  |  [optional] |
|**engineType** | [**EngineTypeEnum**](#EngineTypeEnum) | The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ. |  |
|**engineVersion** | **String** | Required. The broker engine&#39;s version. For a list of supported engine versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker-engine.html\&quot;&gt;Supported engines&lt;/a&gt;. |  |
|**hostInstanceType** | **String** | Required. The broker&#39;s instance type. |  |
|**ldapServerMetadata** | [**CreateBrokerRequestLdapServerMetadata**](CreateBrokerRequestLdapServerMetadata.md) |  |  [optional] |
|**logs** | [**CreateBrokerRequestLogs**](CreateBrokerRequestLogs.md) |  |  [optional] |
|**maintenanceWindowStartTime** | [**CreateBrokerRequestMaintenanceWindowStartTime**](CreateBrokerRequestMaintenanceWindowStartTime.md) |  |  [optional] |
|**publiclyAccessible** | **Boolean** | Enables connections from applications outside of the VPC that hosts the broker&#39;s subnets. Set to false by default, if no value is provided. |  |
|**securityGroups** | **List&lt;String&gt;** | The list of rules (1 minimum, 125 maximum) that authorize connections to brokers. |  [optional] |
|**storageType** | [**StorageTypeEnum**](#StorageTypeEnum) | &lt;p&gt;The broker&#39;s storage type.&lt;/p&gt; &lt;important&gt;&lt;p&gt;EFS is not supported for RabbitMQ engine type.&lt;/p&gt;&lt;/important&gt; |  [optional] |
|**subnetIds** | **List&lt;String&gt;** | &lt;p&gt;The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER_MULTI_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.&lt;/p&gt; &lt;important&gt;&lt;p&gt;If you specify subnets in a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html\&quot;&gt;shared VPC&lt;/a&gt; for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your Amazon Web Services account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your Amazon Web Services account.&lt;/p&gt;&lt;/important&gt; |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Create tags when creating the broker. |  [optional] |
|**users** | [**List&lt;User&gt;**](User.md) | The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console. |  |
|**dataReplicationMode** | [**DataReplicationModeEnum**](#DataReplicationModeEnum) | Specifies whether a broker is a part of a data replication pair. |  [optional] |
|**dataReplicationPrimaryBrokerArn** | **String** | The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR. |  [optional] |



## Enum: AuthenticationStrategyEnum

| Name | Value |
|---- | -----|
| SIMPLE | &quot;SIMPLE&quot; |
| LDAP | &quot;LDAP&quot; |



## Enum: DeploymentModeEnum

| Name | Value |
|---- | -----|
| SINGLE_INSTANCE | &quot;SINGLE_INSTANCE&quot; |
| ACTIVE_STANDBY_MULTI_AZ | &quot;ACTIVE_STANDBY_MULTI_AZ&quot; |
| CLUSTER_MULTI_AZ | &quot;CLUSTER_MULTI_AZ&quot; |



## Enum: EngineTypeEnum

| Name | Value |
|---- | -----|
| ACTIVEMQ | &quot;ACTIVEMQ&quot; |
| RABBITMQ | &quot;RABBITMQ&quot; |



## Enum: StorageTypeEnum

| Name | Value |
|---- | -----|
| EBS | &quot;EBS&quot; |
| EFS | &quot;EFS&quot; |



## Enum: DataReplicationModeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| CRDR | &quot;CRDR&quot; |



