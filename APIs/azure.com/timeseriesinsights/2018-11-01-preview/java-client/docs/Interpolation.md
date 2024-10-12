

# Interpolation

The interpolation operation to be performed on the raw data points. Currently, only sampling of interpolated time series is allowed. Allowed aggregate function - eg: left($value). Can be null if no interpolation needs to be applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundary** | [**InterpolationBoundary**](InterpolationBoundary.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | The type of interpolation technique : \&quot;Linear\&quot; or \&quot;Step\&quot;. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| LINEAR | &quot;Linear&quot; |
| STEP | &quot;Step&quot; |



