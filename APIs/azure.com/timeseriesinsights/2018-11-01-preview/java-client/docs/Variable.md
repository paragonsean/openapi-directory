

# Variable

Variables are named calculations over values from the events. Time Series Insights variable definitions contain formula and computation rules. Variables are stored in the type definition in Time Series Model and can be provided inline via Query APIs to override the stored definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | [**Tsx**](Tsx.md) |  |  [optional] |
|**kind** | **String** | Allowed \&quot;kind\&quot; values are - \&quot;numeric\&quot; or \&quot;aggregate\&quot;. While \&quot;numeric\&quot; allows you to specify value of the reconstructed signal and the expression to aggregate them, the \&quot;aggregate\&quot; kind lets you directly aggregate on the event properties without specifying value. |  |



