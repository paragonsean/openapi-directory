# AmazonMq.CreateConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationStrategy** | **String** | Optional. The authentication strategy used to secure the broker. The default is SIMPLE. | [optional] 
**engineType** | **String** | The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ. | 
**engineVersion** | **String** | Required. The broker engine&#39;s version. For a list of supported engine versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker-engine.html\&quot;&gt;Supported engines&lt;/a&gt;. | 
**name** | **String** | Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long. | 
**tags** | **{String: String}** | Create tags when creating the configuration. | [optional] 



## Enum: AuthenticationStrategyEnum


* `SIMPLE` (value: `"SIMPLE"`)

* `LDAP` (value: `"LDAP"`)





## Enum: EngineTypeEnum


* `ACTIVEMQ` (value: `"ACTIVEMQ"`)

* `RABBITMQ` (value: `"RABBITMQ"`)




