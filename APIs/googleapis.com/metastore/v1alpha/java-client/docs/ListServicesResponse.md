

# ListServicesResponse

Response message for DataprocMetastore.ListServices.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token that can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**services** | [**List&lt;Service&gt;**](Service.md) | The services in the specified location. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



