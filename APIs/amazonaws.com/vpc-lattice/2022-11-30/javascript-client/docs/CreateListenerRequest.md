# AmazonVpcLattice.CreateListenerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. | [optional] 
**defaultAction** | [**CreateRuleRequestAction**](CreateRuleRequestAction.md) |  | 
**name** | **String** | The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can&#39;t use a hyphen as the first or last character, or immediately after another hyphen. | 
**port** | **Number** | The listener port. You can specify a value from &lt;code&gt;1&lt;/code&gt; to &lt;code&gt;65535&lt;/code&gt;. For HTTP, the default is &lt;code&gt;80&lt;/code&gt;. For HTTPS, the default is &lt;code&gt;443&lt;/code&gt;. | [optional] 
**protocol** | **String** | The listener protocol HTTP or HTTPS. | 
**tags** | **{String: String}** | The tags for the listener. | [optional] 



## Enum: ProtocolEnum


* `HTTP` (value: `"HTTP"`)

* `HTTPS` (value: `"HTTPS"`)




