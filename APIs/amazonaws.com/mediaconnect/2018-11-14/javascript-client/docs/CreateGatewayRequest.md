# AwsMediaConnect.CreateGatewayRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egressCidrBlocks** | **[String]** | The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. | 
**name** | **String** | The name of the gateway. This name can not be modified after the gateway is created. | 
**networks** | [**[GatewayNetwork]**](GatewayNetwork.md) | The list of networks that you want to add. | 


