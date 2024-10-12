

# UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass

Performance class setting for this uplink preference rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**builtinPerformanceClassName** | [**BuiltinPerformanceClassNameEnum**](#BuiltinPerformanceClassNameEnum) | Name of builtin performance class, must be present when performanceClass type is &#39;builtin&#39;, and value must be one of: &#39;VoIP&#39; |  [optional] |
|**customPerformanceClassId** | **String** | ID of created custom performance class, must be present when performanceClass type is &#39;custom&#39; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this performance class. Must be one of: &#39;builtin&#39; or &#39;custom&#39; |  |



## Enum: BuiltinPerformanceClassNameEnum

| Name | Value |
|---- | -----|
| VO_IP | &quot;VoIP&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BUILTIN | &quot;builtin&quot; |
| CUSTOM | &quot;custom&quot; |



