# MerakiDashboardApi.GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**builtinPerformanceClassName** | **String** | Name of builtin performance class. Must be present when performanceClass type is &#39;builtin&#39; and value must be one of: &#39;VoIP&#39; | [optional] 
**customPerformanceClassId** | **String** | ID of created custom performance class, must be present when performanceClass type is \&quot;custom\&quot; | [optional] 
**type** | **String** | Type of this performance class. Must be one of: &#39;builtin&#39; or &#39;custom&#39; | 



## Enum: BuiltinPerformanceClassNameEnum


* `VoIP` (value: `"VoIP"`)





## Enum: TypeEnum


* `builtin` (value: `"builtin"`)

* `custom` (value: `"custom"`)




