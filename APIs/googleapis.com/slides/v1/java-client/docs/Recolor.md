

# Recolor

A recolor effect applied on an image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**NameEnum**](#NameEnum) | The name of the recolor effect. The name is determined from the &#x60;recolor_stops&#x60; by matching the gradient against the colors in the page&#39;s current color scheme. This property is read-only. |  [optional] |
|**recolorStops** | [**List&lt;ColorStop&gt;**](ColorStop.md) | The recolor effect is represented by a gradient, which is a list of color stops. The colors in the gradient will replace the corresponding colors at the same position in the color palette and apply to the image. This property is read-only. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| LIGHT1 | &quot;LIGHT1&quot; |
| LIGHT2 | &quot;LIGHT2&quot; |
| LIGHT3 | &quot;LIGHT3&quot; |
| LIGHT4 | &quot;LIGHT4&quot; |
| LIGHT5 | &quot;LIGHT5&quot; |
| LIGHT6 | &quot;LIGHT6&quot; |
| LIGHT7 | &quot;LIGHT7&quot; |
| LIGHT8 | &quot;LIGHT8&quot; |
| LIGHT9 | &quot;LIGHT9&quot; |
| LIGHT10 | &quot;LIGHT10&quot; |
| DARK1 | &quot;DARK1&quot; |
| DARK2 | &quot;DARK2&quot; |
| DARK3 | &quot;DARK3&quot; |
| DARK4 | &quot;DARK4&quot; |
| DARK5 | &quot;DARK5&quot; |
| DARK6 | &quot;DARK6&quot; |
| DARK7 | &quot;DARK7&quot; |
| DARK8 | &quot;DARK8&quot; |
| DARK9 | &quot;DARK9&quot; |
| DARK10 | &quot;DARK10&quot; |
| GRAYSCALE | &quot;GRAYSCALE&quot; |
| NEGATIVE | &quot;NEGATIVE&quot; |
| SEPIA | &quot;SEPIA&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



