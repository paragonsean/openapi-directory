

# PutEmailIdentityFeedbackAttributesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailForwardingEnabled** | **Boolean** | &lt;p&gt;Sets the feedback forwarding configuration for the identity.&lt;/p&gt; &lt;p&gt;If the value is &lt;code&gt;true&lt;/code&gt;, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.&lt;/p&gt; &lt;p&gt;When you set this value to &lt;code&gt;false&lt;/code&gt;, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You&#39;re required to have a method of tracking bounces and complaints. If you haven&#39;t set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).&lt;/p&gt; |  [optional] |



