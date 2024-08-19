

# SchemaRestrictionResponse

The schema restrictions actively enforced in creating this report. To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeMetricRestrictions** | [**List&lt;ActiveMetricRestriction&gt;**](ActiveMetricRestriction.md) | All restrictions actively enforced in creating the report. For example, &#x60;purchaseRevenue&#x60; always has the restriction type &#x60;REVENUE_DATA&#x60;. However, this active response restriction is only populated if the user&#39;s custom role disallows access to &#x60;REVENUE_DATA&#x60;. |  [optional] |



