

# ListDataPointChangesResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceId** | **String** | The data stream ID of the data source with data point changes. |  [optional] |
|**deletedDataPoint** | [**List&lt;DataPoint&gt;**](DataPoint.md) | Deleted data points for the user. Note, for modifications this should be parsed before handling insertions. |  [optional] |
|**insertedDataPoint** | [**List&lt;DataPoint&gt;**](DataPoint.md) | Inserted data points for the user. |  [optional] |
|**nextPageToken** | **String** | The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. |  [optional] |



