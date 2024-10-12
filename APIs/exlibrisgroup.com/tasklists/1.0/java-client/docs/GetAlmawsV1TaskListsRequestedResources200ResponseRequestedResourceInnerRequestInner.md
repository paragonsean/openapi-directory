

# GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInner

Request object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | The related note of the request. |  [optional] |
|**destination** | [**GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerDestination**](GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerDestination.md) |  |  [optional] |
|**id** | **String** | The identifier of the request in Alma. |  [optional] |
|**link** | **String** |  |  [optional] |
|**printed** | **Boolean** | Indication whether the request is printed. |  [optional] |
|**reported** | **Boolean** | Indication whether the request is reported. |  [optional] |
|**requestDate** | **LocalDate** | Deprecated - use request_time instead. The request date. |  [optional] |
|**requestSubType** | [**GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequestSubType**](GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequestSubType.md) |  |  [optional] |
|**requestTime** | **OffsetDateTime** | The creation date and exact time of the request. Output parameter. |  [optional] |
|**requestType** | [**RequestTypeEnum**](#RequestTypeEnum) |  |  |
|**requester** | [**GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequester**](GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequester.md) |  |  [optional] |



## Enum: RequestTypeEnum

| Name | Value |
|---- | -----|
| BOOKING | &quot;BOOKING&quot; |
| DIGITIZATION | &quot;DIGITIZATION&quot; |
| HOLD | &quot;HOLD&quot; |
| MOVE | &quot;MOVE&quot; |
| WORK_ORDER | &quot;WORK_ORDER&quot; |



