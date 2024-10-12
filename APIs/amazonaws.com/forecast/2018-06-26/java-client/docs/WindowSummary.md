

# WindowSummary

<p>The metrics for a time range within the evaluation portion of a dataset. This object is part of the <a>EvaluationResult</a> object.</p> <p>The <code>TestWindowStart</code> and <code>TestWindowEnd</code> parameters are determined by the <code>BackTestWindowOffset</code> parameter of the <a>EvaluationParameters</a> object.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**testWindowStart** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**testWindowEnd** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**itemCount** | [**Integer**](Integer.md) |  |  [optional] |
|**evaluationType** | [**EvaluationType**](EvaluationType.md) |  |  [optional] |
|**metrics** | [**WindowSummaryMetrics**](WindowSummaryMetrics.md) |  |  [optional] |



