# NetworkManagementClient.ApplicationGatewayProbePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | Gets or sets the host to send probe to  | [optional] 
**interval** | **Number** | Gets or sets probing interval in seconds  | [optional] 
**path** | **String** | Gets or sets the relative path of probe  | [optional] 
**protocol** | **String** | Gets or sets the protocol | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the backend http settings resource Updating/Deleting/Failed | [optional] 
**timeout** | **Number** | Gets or sets probing timeout in seconds  | [optional] 
**unhealthyThreshold** | **Number** | Gets or sets probing unhealthy threshold  | [optional] 



## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




