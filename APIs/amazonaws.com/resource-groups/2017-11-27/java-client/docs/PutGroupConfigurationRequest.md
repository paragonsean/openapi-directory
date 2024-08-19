

# PutGroupConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**group** | **String** | The name or ARN of the resource group with the configuration that you want to update. |  [optional] |
|**_configuration** | [**List&lt;GroupConfigurationItem&gt;**](GroupConfigurationItem.md) | &lt;p&gt;The new configuration to associate with the specified group. A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of &lt;a&gt;GroupConfigurationItem&lt;/a&gt; elements.&lt;/p&gt; &lt;p&gt;For information about the syntax of a service configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\&quot;&gt;Service configurations for Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A resource group can contain either a &lt;code&gt;Configuration&lt;/code&gt; or a &lt;code&gt;ResourceQuery&lt;/code&gt;, but not both.&lt;/p&gt; &lt;/note&gt; |  [optional] |



