

# BuildSystemSharedInterfacesIParameterValue

Declares members that must be implemented by parameter value objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direction** | [**DirectionEnum**](#DirectionEnum) | Gets or sets a value indicating whether the parameter value is an               input to the build part or an output from the build part. |  [optional] |
|**name** | **String** | Gets or sets the name of the parameter. |  [optional] |
|**value** | **String** | Gets or sets the value of the parameter. |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INPUT | &quot;Input&quot; |
| OUTPUT | &quot;Output&quot; |



