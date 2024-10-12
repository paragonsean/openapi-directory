

# Nsx

Details about a NSX Manager appliance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fqdn** | **String** | Fully qualified domain name of the appliance. |  [optional] |
|**internalIp** | **String** | Internal IP address of the appliance. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the appliance. |  [optional] [readonly] |
|**version** | **String** | Version of the appliance. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |



