

# ListServicesResponse

Response message for `ListServices`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to retrieve the next page of results. To retrieve the next page, call &#x60;ListServices&#x60; again with the &#x60;page_token&#x60; field set to this value. This field is empty if there are no more results to retrieve. |  [optional] |
|**services** | [**List&lt;Service&gt;**](Service.md) | A list of services. |  [optional] |



