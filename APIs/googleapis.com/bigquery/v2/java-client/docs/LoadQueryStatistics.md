

# LoadQueryStatistics

Statistics for a LOAD query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badRecords** | **String** | Output only. The number of bad records encountered while processing a LOAD query. Note that if the job has failed because of more bad records encountered than the maximum allowed in the load job configuration, then this number can be less than the total number of bad records present in the input data. |  [optional] [readonly] |
|**bytesTransferred** | **String** | Output only. This field is deprecated. The number of bytes of source data copied over the network for a &#x60;LOAD&#x60; query. &#x60;transferred_bytes&#x60; has the canonical value for physical transferred bytes, which is used for BigQuery Omni billing. |  [optional] [readonly] |
|**inputFileBytes** | **String** | Output only. Number of bytes of source data in a LOAD query. |  [optional] [readonly] |
|**inputFiles** | **String** | Output only. Number of source files in a LOAD query. |  [optional] [readonly] |
|**outputBytes** | **String** | Output only. Size of the loaded data in bytes. Note that while a LOAD query is in the running state, this value may change. |  [optional] [readonly] |
|**outputRows** | **String** | Output only. Number of rows imported in a LOAD query. Note that while a LOAD query is in the running state, this value may change. |  [optional] [readonly] |



