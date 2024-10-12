

# ChartAxisViewWindowOptions

The options that define a \"view window\" for a chart (such as the visible values in an axis).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**viewWindowMax** | **Double** | The maximum numeric value to be shown in this view window. If unset, will automatically determine a maximum value that looks good for the data. |  [optional] |
|**viewWindowMin** | **Double** | The minimum numeric value to be shown in this view window. If unset, will automatically determine a minimum value that looks good for the data. |  [optional] |
|**viewWindowMode** | [**ViewWindowModeEnum**](#ViewWindowModeEnum) | The view window&#39;s mode. |  [optional] |



## Enum: ViewWindowModeEnum

| Name | Value |
|---- | -----|
| DEFAULT_VIEW_WINDOW_MODE | &quot;DEFAULT_VIEW_WINDOW_MODE&quot; |
| VIEW_WINDOW_MODE_UNSUPPORTED | &quot;VIEW_WINDOW_MODE_UNSUPPORTED&quot; |
| EXPLICIT | &quot;EXPLICIT&quot; |
| PRETTY | &quot;PRETTY&quot; |



