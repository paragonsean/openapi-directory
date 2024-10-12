

# V1ListSettlementsRequest



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchToken** | **String** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. |  [optional] |
|**beginTime** | **String** | The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year. |  [optional] |
|**endTime** | **String** | The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time. |  [optional] |
|**limit** | **Integer** | The maximum number of settlements to return in a single response. This value cannot exceed 200. |  [optional] |
|**order** | **String** | The order in which settlements are listed in the response. |  [optional] |
|**status** | **String** | Provide this parameter to retrieve only settlements with a particular status (SENT or FAILED). |  [optional] |



