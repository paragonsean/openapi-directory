

# OrgChartSpec

An org chart. Org charts require a unique set of labels in labels and may optionally include parent_labels and tooltips. parent_labels contain, for each node, the label identifying the parent node. tooltips contain, for each node, an optional tooltip. For example, to describe an OrgChart with Alice as the CEO, Bob as the President (reporting to Alice) and Cathy as VP of Sales (also reporting to Alice), have labels contain \"Alice\", \"Bob\", \"Cathy\", parent_labels contain \"\", \"Alice\", \"Alice\" and tooltips contain \"CEO\", \"President\", \"VP Sales\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labels** | [**ChartData**](ChartData.md) |  |  [optional] |
|**nodeColor** | [**Color**](Color.md) |  |  [optional] |
|**nodeColorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**nodeSize** | [**NodeSizeEnum**](#NodeSizeEnum) | The size of the org chart nodes. |  [optional] |
|**parentLabels** | [**ChartData**](ChartData.md) |  |  [optional] |
|**selectedNodeColor** | [**Color**](Color.md) |  |  [optional] |
|**selectedNodeColorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**tooltips** | [**ChartData**](ChartData.md) |  |  [optional] |



## Enum: NodeSizeEnum

| Name | Value |
|---- | -----|
| ORG_CHART_LABEL_SIZE_UNSPECIFIED | &quot;ORG_CHART_LABEL_SIZE_UNSPECIFIED&quot; |
| SMALL | &quot;SMALL&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LARGE | &quot;LARGE&quot; |



