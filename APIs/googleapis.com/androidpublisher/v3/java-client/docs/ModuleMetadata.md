

# ModuleMetadata

Metadata of a module.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryType** | [**DeliveryTypeEnum**](#DeliveryTypeEnum) | Indicates the delivery type (e.g. on-demand) of the module. |  [optional] |
|**dependencies** | **List&lt;String&gt;** | Names of the modules that this module directly depends on. Each module implicitly depends on the base module. |  [optional] |
|**moduleType** | [**ModuleTypeEnum**](#ModuleTypeEnum) | Indicates the type of this feature module. |  [optional] |
|**name** | **String** | Module name. |  [optional] |
|**targeting** | [**ModuleTargeting**](ModuleTargeting.md) |  |  [optional] |



## Enum: DeliveryTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_DELIVERY_TYPE | &quot;UNKNOWN_DELIVERY_TYPE&quot; |
| INSTALL_TIME | &quot;INSTALL_TIME&quot; |
| ON_DEMAND | &quot;ON_DEMAND&quot; |
| FAST_FOLLOW | &quot;FAST_FOLLOW&quot; |



## Enum: ModuleTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_MODULE_TYPE | &quot;UNKNOWN_MODULE_TYPE&quot; |
| FEATURE_MODULE | &quot;FEATURE_MODULE&quot; |



