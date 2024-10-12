

# ProductAvailabilityChangeEvent

An event generated whenever a product's availability changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityStatus** | [**AvailabilityStatusEnum**](#AvailabilityStatusEnum) | The new state of the product. This field will always be present. |  [optional] |
|**productId** | **String** | The id of the product (e.g. \&quot;app:com.google.android.gm\&quot;) for which the product availability changed. This field will always be present. |  [optional] |



## Enum: AvailabilityStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| AVAILABLE | &quot;available&quot; |
| REMOVED | &quot;removed&quot; |
| UNPUBLISHED | &quot;unpublished&quot; |



