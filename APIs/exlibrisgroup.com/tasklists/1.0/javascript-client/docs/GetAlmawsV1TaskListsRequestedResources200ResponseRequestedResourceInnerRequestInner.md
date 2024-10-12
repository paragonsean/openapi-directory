# ExLibrisApis.GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | The related note of the request. | [optional] 
**destination** | [**GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerDestination**](GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerDestination.md) |  | [optional] 
**id** | **String** | The identifier of the request in Alma. | [optional] 
**link** | **String** |  | [optional] 
**printed** | **Boolean** | Indication whether the request is printed. | [optional] 
**reported** | **Boolean** | Indication whether the request is reported. | [optional] 
**requestDate** | **Date** | Deprecated - use request_time instead. The request date. | [optional] 
**requestSubType** | [**GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequestSubType**](GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequestSubType.md) |  | [optional] 
**requestTime** | **Date** | The creation date and exact time of the request. Output parameter. | [optional] 
**requestType** | **String** |  | 
**requester** | [**GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequester**](GetAlmawsV1TaskListsRequestedResources200ResponseRequestedResourceInnerRequestInnerRequester.md) |  | [optional] 



## Enum: RequestTypeEnum


* `BOOKING` (value: `"BOOKING"`)

* `DIGITIZATION` (value: `"DIGITIZATION"`)

* `HOLD` (value: `"HOLD"`)

* `MOVE` (value: `"MOVE"`)

* `WORK_ORDER` (value: `"WORK_ORDER"`)




