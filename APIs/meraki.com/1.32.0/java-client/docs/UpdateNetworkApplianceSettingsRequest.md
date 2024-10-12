

# UpdateNetworkApplianceSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientTrackingMethod** | [**ClientTrackingMethodEnum**](#ClientTrackingMethodEnum) | Client tracking method of a network |  [optional] |
|**deploymentMode** | [**DeploymentModeEnum**](#DeploymentModeEnum) | Deployment mode of a network |  [optional] |
|**dynamicDns** | [**UpdateNetworkApplianceSettingsRequestDynamicDns**](UpdateNetworkApplianceSettingsRequestDynamicDns.md) |  |  [optional] |



## Enum: ClientTrackingMethodEnum

| Name | Value |
|---- | -----|
| IP_ADDRESS | &quot;IP address&quot; |
| MAC_ADDRESS | &quot;MAC address&quot; |
| UNIQUE_CLIENT_IDENTIFIER | &quot;Unique client identifier&quot; |



## Enum: DeploymentModeEnum

| Name | Value |
|---- | -----|
| PASSTHROUGH | &quot;passthrough&quot; |
| ROUTED | &quot;routed&quot; |



