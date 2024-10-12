

# TopicUpdateParameters

Properties of the Topic update

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTrafficFromAllIPs** | **Boolean** | This determines if IP filtering rules ought to be evaluated or not. By default it will not evaluate and will allow traffic from all IPs. |  [optional] |
|**inboundIpRules** | [**List&lt;InboundIpRule&gt;**](InboundIpRule.md) | This determines the IP filtering rules that ought be applied when events are received on this domain. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags of the resource. |  [optional] |



