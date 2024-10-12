# AmazonChime.CreateSipRuleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the SIP rule. | 
**triggerType** | **String** | The type of trigger assigned to the SIP rule in &lt;code&gt;TriggerValue&lt;/code&gt;, currently &lt;code&gt;RequestUriHostname&lt;/code&gt; or &lt;code&gt;ToPhoneNumber&lt;/code&gt;. | 
**triggerValue** | **String** | If &lt;code&gt;TriggerType&lt;/code&gt; is &lt;code&gt;RequestUriHostname&lt;/code&gt;, the value can be the outbound host name of an Amazon Chime Voice Connector. If &lt;code&gt;TriggerType&lt;/code&gt; is &lt;code&gt;ToPhoneNumber&lt;/code&gt;, the value can be a customer-owned phone number in the E164 format. The &lt;code&gt;SipMediaApplication&lt;/code&gt; specified in the &lt;code&gt;SipRule&lt;/code&gt; is triggered if the request URI in an incoming SIP request matches the &lt;code&gt;RequestUriHostname&lt;/code&gt;, or if the &lt;code&gt;To&lt;/code&gt; header in the incoming SIP request matches the &lt;code&gt;ToPhoneNumber&lt;/code&gt; value. | 
**disabled** | **Boolean** | Enables or disables a rule. You must disable rules before you can delete them. | [optional] 
**targetApplications** | [**[SipRuleTargetApplication]**](SipRuleTargetApplication.md) | List of SIP media applications with priority and AWS Region. Only one SIP application per AWS Region can be used. | 



## Enum: TriggerTypeEnum


* `ToPhoneNumber` (value: `"ToPhoneNumber"`)

* `RequestUriHostname` (value: `"RequestUriHostname"`)




