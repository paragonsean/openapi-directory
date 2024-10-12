# GooglePlayAndroidDeveloperApi.ModuleMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveryType** | **String** | Indicates the delivery type (e.g. on-demand) of the module. | [optional] 
**dependencies** | **[String]** | Names of the modules that this module directly depends on. Each module implicitly depends on the base module. | [optional] 
**moduleType** | **String** | Indicates the type of this feature module. | [optional] 
**name** | **String** | Module name. | [optional] 
**targeting** | [**ModuleTargeting**](ModuleTargeting.md) |  | [optional] 



## Enum: DeliveryTypeEnum


* `UNKNOWN_DELIVERY_TYPE` (value: `"UNKNOWN_DELIVERY_TYPE"`)

* `INSTALL_TIME` (value: `"INSTALL_TIME"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)

* `FAST_FOLLOW` (value: `"FAST_FOLLOW"`)





## Enum: ModuleTypeEnum


* `UNKNOWN_MODULE_TYPE` (value: `"UNKNOWN_MODULE_TYPE"`)

* `FEATURE_MODULE` (value: `"FEATURE_MODULE"`)




