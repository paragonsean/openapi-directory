

# PutEmailIdentityFeedbackAttributesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailForwardingEnabled** | **Boolean** | &lt;p&gt;Sets the feedback forwarding configuration for the identity.&lt;/p&gt; &lt;p&gt;If the value is &lt;code&gt;true&lt;/code&gt;, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the &lt;code&gt;Return-Path&lt;/code&gt; header of the original email.&lt;/p&gt; &lt;p&gt;You&#39;re required to have a method of tracking bounces and complaints. If you haven&#39;t set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).&lt;/p&gt; |  [optional] |



