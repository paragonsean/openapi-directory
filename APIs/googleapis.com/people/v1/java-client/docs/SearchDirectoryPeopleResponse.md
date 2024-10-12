

# SearchDirectoryPeopleResponse

The response to a request for people in the authenticated user's domain directory that match the specified query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**people** | [**List&lt;Person&gt;**](Person.md) | The list of people in the domain directory that match the query. |  [optional] |
|**totalSize** | **Integer** | The total number of items in the list without pagination. |  [optional] |



