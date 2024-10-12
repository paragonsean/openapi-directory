

# Line

A PageElement kind representing a non-connector line, straight connector, curved connector, or bent connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lineCategory** | [**LineCategoryEnum**](#LineCategoryEnum) | The category of the line. It matches the &#x60;category&#x60; specified in CreateLineRequest, and can be updated with UpdateLineCategoryRequest. |  [optional] |
|**lineProperties** | [**LineProperties**](LineProperties.md) |  |  [optional] |
|**lineType** | [**LineTypeEnum**](#LineTypeEnum) | The type of the line. |  [optional] |



## Enum: LineCategoryEnum

| Name | Value |
|---- | -----|
| LINE_CATEGORY_UNSPECIFIED | &quot;LINE_CATEGORY_UNSPECIFIED&quot; |
| STRAIGHT | &quot;STRAIGHT&quot; |
| BENT | &quot;BENT&quot; |
| CURVED | &quot;CURVED&quot; |



## Enum: LineTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| STRAIGHT_CONNECTOR_1 | &quot;STRAIGHT_CONNECTOR_1&quot; |
| BENT_CONNECTOR_2 | &quot;BENT_CONNECTOR_2&quot; |
| BENT_CONNECTOR_3 | &quot;BENT_CONNECTOR_3&quot; |
| BENT_CONNECTOR_4 | &quot;BENT_CONNECTOR_4&quot; |
| BENT_CONNECTOR_5 | &quot;BENT_CONNECTOR_5&quot; |
| CURVED_CONNECTOR_2 | &quot;CURVED_CONNECTOR_2&quot; |
| CURVED_CONNECTOR_3 | &quot;CURVED_CONNECTOR_3&quot; |
| CURVED_CONNECTOR_4 | &quot;CURVED_CONNECTOR_4&quot; |
| CURVED_CONNECTOR_5 | &quot;CURVED_CONNECTOR_5&quot; |
| STRAIGHT_LINE | &quot;STRAIGHT_LINE&quot; |



