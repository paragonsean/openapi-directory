# EventGridManagementClient.DomainUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowTrafficFromAllIPs** | **Boolean** | This determines if IP filtering rules ought to be evaluated or not. By default it will not evaluate and will allow traffic from all IPs. | [optional] 
**inboundIpRules** | [**[InboundIpRule]**](InboundIpRule.md) | This determines the IP filtering rules that ought be applied when events are received on this domain. | [optional] 
**tags** | **{String: String}** | Tags of the domains resource | [optional] 


