

# DataLabel

Settings for one set of data labels. Data labels are annotations that appear next to a set of data, such as the points on a line chart, and provide additional information about what the data represents, such as a text representation of the value behind that point on the graph.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customLabelData** | [**ChartData**](ChartData.md) |  |  [optional] |
|**placement** | [**PlacementEnum**](#PlacementEnum) | The placement of the data label relative to the labeled data. |  [optional] |
|**textFormat** | [**TextFormat**](TextFormat.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the data label. |  [optional] |



## Enum: PlacementEnum

| Name | Value |
|---- | -----|
| DATA_LABEL_PLACEMENT_UNSPECIFIED | &quot;DATA_LABEL_PLACEMENT_UNSPECIFIED&quot; |
| CENTER | &quot;CENTER&quot; |
| LEFT | &quot;LEFT&quot; |
| RIGHT | &quot;RIGHT&quot; |
| ABOVE | &quot;ABOVE&quot; |
| BELOW | &quot;BELOW&quot; |
| INSIDE_END | &quot;INSIDE_END&quot; |
| INSIDE_BASE | &quot;INSIDE_BASE&quot; |
| OUTSIDE_END | &quot;OUTSIDE_END&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATA_LABEL_TYPE_UNSPECIFIED | &quot;DATA_LABEL_TYPE_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| DATA | &quot;DATA&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



