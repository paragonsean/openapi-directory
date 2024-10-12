# NetworkManagementClient.ApplicationGatewaySslPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipherSuites** | [**[CipherSuitesEnum]**](CipherSuitesEnum.md) | Ssl cipher suites to be enabled in the specified order to application gateway. | [optional] 
**disabledSslProtocols** | [**[ProtocolsEnum]**](ProtocolsEnum.md) | Ssl protocols to be disabled on application gateway. | [optional] 
**minProtocolVersion** | [**ProtocolsEnum**](ProtocolsEnum.md) |  | [optional] 
**policyName** | [**PolicyNameEnum**](PolicyNameEnum.md) |  | [optional] 
**policyType** | **String** | Type of Ssl Policy. | [optional] 



## Enum: PolicyTypeEnum


* `Predefined` (value: `"Predefined"`)

* `Custom` (value: `"Custom"`)




