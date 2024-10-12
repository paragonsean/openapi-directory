

# GoogleCloudDiscoveryengineV1alphaWidgetConfigUIComponentField

Facet field that maps to a UI Component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceVisibility** | [**List&lt;DeviceVisibilityEnum&gt;**](#List&lt;DeviceVisibilityEnum&gt;) | The field visibility on different types of devices. |  [optional] |
|**displayTemplate** | **String** | The template to customize how the field is displayed. An example value would be a string that looks like: \&quot;Price: {value}\&quot;. |  [optional] |
|**field** | **String** | Required. Registered field name. The format is &#x60;field.abc&#x60;. |  [optional] |



## Enum: List&lt;DeviceVisibilityEnum&gt;

| Name | Value |
|---- | -----|
| DEVICE_VISIBILITY_UNSPECIFIED | &quot;DEVICE_VISIBILITY_UNSPECIFIED&quot; |
| MOBILE | &quot;MOBILE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |



