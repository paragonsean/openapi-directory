

# ListDatabaseInstancesResponse

The response from the ListDatabaseInstances method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instances** | [**List&lt;DatabaseInstance&gt;**](DatabaseInstance.md) | List of each DatabaseInstance that is in the parent Firebase project. |  [optional] |
|**nextPageToken** | **String** | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent call to &#x60;ListDatabaseInstances&#x60; to find the next group of database instances. Page tokens are short-lived and should not be persisted. |  [optional] |



