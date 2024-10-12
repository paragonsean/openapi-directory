

# EventRankingRankingsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dq** | **Integer** | Number of times disqualified. |  |
|**extraStats** | **List&lt;BigDecimal&gt;** | Additional special data on the team&#39;s performance calculated by TBA. |  [optional] |
|**matchesPlayed** | **Integer** | Number of matches played by this team. |  |
|**qualAverage** | **Integer** | The average match score during qualifications. Year specific. May be null if not relevant for a given year. |  [optional] |
|**rank** | **Integer** | The team&#39;s rank at the event as provided by FIRST. |  |
|**record** | [**WLTRecord**](WLTRecord.md) |  |  |
|**sortOrders** | **List&lt;BigDecimal&gt;** | Additional year-specific information, may be null. See parent &#x60;sort_order_info&#x60; for details. |  [optional] |
|**teamKey** | **String** | The team with this rank. |  |



