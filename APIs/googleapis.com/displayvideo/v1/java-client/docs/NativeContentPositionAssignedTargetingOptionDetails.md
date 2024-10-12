

# NativeContentPositionAssignedTargetingOptionDetails

Details for native content position assigned targeting option. This will be populated in the native_content_position_details field when targeting_type is `TARGETING_TYPE_NATIVE_CONTENT_POSITION`. Explicitly targeting all options is not supported. Remove all native content position targeting options to achieve this effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentPosition** | [**ContentPositionEnum**](#ContentPositionEnum) | Required. The content position. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60;. |  [optional] |



## Enum: ContentPositionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;NATIVE_CONTENT_POSITION_UNSPECIFIED&quot; |
| UNKNOWN | &quot;NATIVE_CONTENT_POSITION_UNKNOWN&quot; |
| IN_ARTICLE | &quot;NATIVE_CONTENT_POSITION_IN_ARTICLE&quot; |
| IN_FEED | &quot;NATIVE_CONTENT_POSITION_IN_FEED&quot; |
| PERIPHERAL | &quot;NATIVE_CONTENT_POSITION_PERIPHERAL&quot; |
| RECOMMENDATION | &quot;NATIVE_CONTENT_POSITION_RECOMMENDATION&quot; |



