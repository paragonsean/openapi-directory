

# SearchQuery


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**criteria** | [**List&lt;Criteria&gt;**](Criteria.md) | Optional search criteria. All criteria are ANDed together. |  [optional] |
|**endDate** | **String** | The end date (inclusive) &#39;2015-04-22T10:03:19&#39; in the timezone of your merchant account. |  |
|**endRow** | **BigDecimal** | Used to page the results. 1-based. This should always be 1 larger than start_row. |  |
|**name** | **String** | Only accepts 2 values. Can be either &#39;Search&#39; for all fields or &#39;TransHistoryMinimal&#39; for a subset of the fields returned in the results. |  |
|**startDate** | **String** | The start date (inclusive) &#39;2015-04-22T10:03:19&#39; in the timezone of your merchant account. |  |
|**startRow** | **BigDecimal** | Used to page the results. 1-based |  |



