

# BatchDeleteVersionsRequest

The request to delete multiple versions across a repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**names** | **List&lt;String&gt;** | Required. The names of the versions to delete. A maximum of 10000 versions can be deleted in a batch. |  [optional] |
|**validateOnly** | **Boolean** | If true, the request is performed without deleting data, following AIP-163. |  [optional] |



