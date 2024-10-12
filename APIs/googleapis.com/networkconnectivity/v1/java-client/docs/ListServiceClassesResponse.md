

# ListServiceClassesResponse

Response for ListServiceClasses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |  [optional] |
|**serviceClasses** | [**List&lt;ServiceClass&gt;**](ServiceClass.md) | ServiceClasses to be returned. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



