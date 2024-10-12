

# ApplicationGatewaySslPolicy

Application Gateway Ssl policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cipherSuites** | **List&lt;CipherSuitesEnum&gt;** | Ssl cipher suites to be enabled in the specified order to application gateway. |  [optional] |
|**disabledSslProtocols** | **List&lt;ProtocolsEnum&gt;** | Ssl protocols to be disabled on application gateway. |  [optional] |
|**minProtocolVersion** | **ProtocolsEnum** |  |  [optional] |
|**policyName** | **PolicyNameEnum** |  |  [optional] |
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) | Type of Ssl Policy. |  [optional] |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| PREDEFINED | &quot;Predefined&quot; |
| CUSTOM | &quot;Custom&quot; |



