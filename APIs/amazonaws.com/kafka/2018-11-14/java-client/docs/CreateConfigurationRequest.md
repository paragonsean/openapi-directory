

# CreateConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |              &lt;p&gt;The description of the configuration.&lt;/p&gt;           |  [optional] |
|**kafkaVersions** | **List&lt;String&gt;** |              &lt;p&gt;The versions of Apache Kafka with which you can use this MSK configuration.&lt;/p&gt;           |  [optional] |
|**name** | **String** |              &lt;p&gt;The name of the configuration.&lt;/p&gt;           |  |
|**serverProperties** | **String** |              &lt;p&gt;Contents of the &lt;filename&gt;server.properties&lt;/filename&gt; file. When using the API, you must ensure that the contents of the file are base64 encoded.                 When using the AWS Management Console, the SDK, or the AWS CLI, the contents of &lt;filename&gt;server.properties&lt;/filename&gt; can be in plaintext.&lt;/p&gt;           |  |



