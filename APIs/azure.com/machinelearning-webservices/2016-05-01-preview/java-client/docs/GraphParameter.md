

# GraphParameter

Defines a global parameter in the graph.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of this graph parameter. |  [optional] |
|**links** | [**List&lt;GraphParameterLink&gt;**](GraphParameterLink.md) | Association links for this parameter to nodes in the graph. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Graph parameter&#39;s type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| INT | &quot;Int&quot; |
| FLOAT | &quot;Float&quot; |
| ENUMERATED | &quot;Enumerated&quot; |
| SCRIPT | &quot;Script&quot; |
| MODE | &quot;Mode&quot; |
| CREDENTIAL | &quot;Credential&quot; |
| BOOLEAN | &quot;Boolean&quot; |
| DOUBLE | &quot;Double&quot; |
| COLUMN_PICKER | &quot;ColumnPicker&quot; |
| PARAMETER_RANGE | &quot;ParameterRange&quot; |
| DATA_GATEWAY_NAME | &quot;DataGatewayName&quot; |



