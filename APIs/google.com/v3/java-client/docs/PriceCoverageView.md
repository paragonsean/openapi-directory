

# PriceCoverageView

A price coverage view. Covers the `price_coverage_stats` Scorecard functionality in pre-v3.0 API versions. For more information, refer to Price Coverage for Push and Hint partners.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculationDate** | [**Date**](Date.md) |  |  [optional] |
|**matchedPropertyCount** | **Integer** | The total number of properties that have prices for the given itineraries. |  [optional] |
|**priceCoverageBinaryPercent** | **Double** | The ratio between the number of hotels which have at least one price for the calculation period and &#x60;matched_property_count&#x60;. |  [optional] |
|**priceCoverageBuckets** | [**List&lt;PriceCoverageBucket&gt;**](PriceCoverageBucket.md) | Price coverage stats for combinations of advance booking window and length of stay ranges. |  [optional] |
|**priceCoveragePercent** | **Double** | The overall price coverage for an account. This value is the ratio between the number of hotel prices for the calculation booking window and length of stay range divided by the number of all possible prices, which is &#x60;matched_property_count&#x60; times 330 (for advance book window) times 30 (for length of stay). |  [optional] |



