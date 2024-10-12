

# CreateConfigurationSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationSetName** | **String** | &lt;p&gt;The name of a configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt; |  |
|**trackingOptions** | [**CreateConfigurationSetRequestTrackingOptions**](CreateConfigurationSetRequestTrackingOptions.md) |  |  [optional] |
|**deliveryOptions** | [**CreateConfigurationSetRequestDeliveryOptions**](CreateConfigurationSetRequestDeliveryOptions.md) |  |  [optional] |
|**reputationOptions** | [**CreateConfigurationSetRequestReputationOptions**](CreateConfigurationSetRequestReputationOptions.md) |  |  [optional] |
|**sendingOptions** | [**CreateConfigurationSetRequestSendingOptions**](CreateConfigurationSetRequestSendingOptions.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | An array of objects that define the tags (keys and values) that you want to associate with the configuration set. |  [optional] |



