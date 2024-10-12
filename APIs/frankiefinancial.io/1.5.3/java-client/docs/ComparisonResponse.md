

# ComparisonResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonDate** | **String** | Timestamp of when the comparison took place |  |
|**correlationId** | **UUID** | The correlationId as passed in the request |  |
|**currentBillData** | [**CurrentBillData**](CurrentBillData.md) |  |  |
|**defaultOffer** | [**DefaultOffer**](DefaultOffer.md) |  |  |
|**marketDisclosure** | [**ComparisonResponseMarketDisclosure**](ComparisonResponseMarketDisclosure.md) |  |  [optional] |
|**maximumSaving** | **BigDecimal** | What is the maximum saving that can be achieved if the user switches to a new plan. This number may be negative if the user is already on the best plan for their usage and no saving can be found. |  |
|**plans** | [**List&lt;Plan&gt;**](Plan.md) | Array of plans, sorted from best to worst saving, for the uploaded bill |  |
|**version** | **String** | Version of the API on which the comparison took place. This value should be reported with any issue raised. |  |



