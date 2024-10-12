

# Outline

The outline of a PageElement. If these fields are unset, they may be inherited from a parent placeholder if it exists. If there is no parent, the fields will default to the value used for new page elements created in the Slides editor, which may depend on the page element kind.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dashStyle** | [**DashStyleEnum**](#DashStyleEnum) | The dash style of the outline. |  [optional] |
|**outlineFill** | [**OutlineFill**](OutlineFill.md) |  |  [optional] |
|**propertyState** | [**PropertyStateEnum**](#PropertyStateEnum) | The outline property state. Updating the outline on a page element will implicitly update this field to &#x60;RENDERED&#x60;, unless another value is specified in the same request. To have no outline on a page element, set this field to &#x60;NOT_RENDERED&#x60;. In this case, any other outline fields set in the same request will be ignored. |  [optional] |
|**weight** | [**Dimension**](Dimension.md) |  |  [optional] |



## Enum: DashStyleEnum

| Name | Value |
|---- | -----|
| DASH_STYLE_UNSPECIFIED | &quot;DASH_STYLE_UNSPECIFIED&quot; |
| SOLID | &quot;SOLID&quot; |
| DOT | &quot;DOT&quot; |
| DASH | &quot;DASH&quot; |
| DASH_DOT | &quot;DASH_DOT&quot; |
| LONG_DASH | &quot;LONG_DASH&quot; |
| LONG_DASH_DOT | &quot;LONG_DASH_DOT&quot; |



## Enum: PropertyStateEnum

| Name | Value |
|---- | -----|
| RENDERED | &quot;RENDERED&quot; |
| NOT_RENDERED | &quot;NOT_RENDERED&quot; |
| INHERIT | &quot;INHERIT&quot; |



