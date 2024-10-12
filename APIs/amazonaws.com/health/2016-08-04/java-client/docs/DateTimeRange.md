

# DateTimeRange

A range of dates and times that is used by the <a href=\"https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html\">EventFilter</a> and <a href=\"https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html\">EntityFilter</a> objects. If <code>from</code> is set and <code>to</code> is set: match items where the timestamp (<code>startTime</code>, <code>endTime</code>, or <code>lastUpdatedTime</code>) is between <code>from</code> and <code>to</code> inclusive. If <code>from</code> is set and <code>to</code> is not set: match items where the timestamp value is equal to or after <code>from</code>. If <code>from</code> is not set and <code>to</code> is set: match items where the timestamp value is equal to or before <code>to</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**to** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



