# NetworkManagementClient.ApplicationGatewayProbePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | Host to send probe to  | [optional] 
**interval** | **Number** | Probing interval in seconds  | [optional] 
**path** | **String** | Relative path of probe  | [optional] 
**protocol** | **String** | Protocol | [optional] 
**provisioningState** | **String** | Provisioning state of the backend http settings resource Updating/Deleting/Failed | [optional] 
**timeout** | **Number** | Probing timeout in seconds  | [optional] 
**unhealthyThreshold** | **Number** | Probing unhealthy threshold  | [optional] 



## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




