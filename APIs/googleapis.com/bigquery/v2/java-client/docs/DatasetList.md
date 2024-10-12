

# DatasetList

Response format for a page of results when listing datasets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasets** | [**List&lt;DatasetListDatasetsInner&gt;**](DatasetListDatasetsInner.md) | An array of the dataset resources in the project. Each resource contains basic information. For full information about a particular dataset resource, use the Datasets: get method. This property is omitted when there are no datasets in the project. |  [optional] |
|**etag** | **String** | Output only. A hash value of the results page. You can use this property to determine if the page has changed since the last request. |  [optional] [readonly] |
|**kind** | **String** | Output only. The resource type. This property always returns the value \&quot;bigquery#datasetList\&quot; |  [optional] [readonly] |
|**nextPageToken** | **String** | A token that can be used to request the next results page. This property is omitted on the final results page. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of skipped locations that were unreachable. For more information about BigQuery locations, see: https://cloud.google.com/bigquery/docs/locations. Example: \&quot;europe-west5\&quot; |  [optional] |



