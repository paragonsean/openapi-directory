

# AggregationHistogram

Histogram of bucketed assets counts by field value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lowerBounds** | **List&lt;Double&gt;** | Lower bounds of buckets. The response will contain &#x60;n+1&#x60; buckets for &#x60;n&#x60; bounds. The first bucket will count all assets for which the field value is smaller than the first bound. Subsequent buckets will count assets for which the field value is greater or equal to a lower bound and smaller than the next one. The last bucket will count assets for which the field value is greater or equal to the final lower bound. You can define up to 20 lower bounds. |  [optional] |



