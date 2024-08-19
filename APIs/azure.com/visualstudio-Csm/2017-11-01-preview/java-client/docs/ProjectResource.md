

# ProjectResource

A Visual Studio Team Services project resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Kind of project resource |  [optional] |
|**properties** | [**ProjectResourceProperties**](ProjectResourceProperties.md) |  |  [optional] |
|**id** | **String** | Unique identifier of the resource. |  [optional] [readonly] |
|**location** | **String** | Resource location. |  [optional] |
|**name** | **String** | Resource name. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**type** | **String** | Resource type. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| PROJECT | &quot;project&quot; |
| BOOTSTRAPPED_PROJECT | &quot;bootstrappedProject&quot; |



