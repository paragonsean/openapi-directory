# AlerterSystemApi.AlertLogGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertLogErrorMessage** | **String** | The reason why the dispatch of the alert failed. | [optional] 
**alertLogMessageId** | **String** | The id of the successfully dispatched message as received from the transport that was used. | [optional] 
**alertLogStatusCode** | **String** | The status of the alert log. | [optional] 
**alertService** | **String** | The alert service that is related to this resource. | [optional] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] [readonly] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**monitor** | **String** | The monitor that is related to this resource instance. | [optional] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | [optional] 
**ping** | **String** | The ping that triggered this resource instance. | [optional] 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**webhookResponseBody** | **String** | The response body returned by a successful request to a webhook URL. Length limited to 1,000 characters. | [optional] 
**webhookResponseHeaders** | **[String]** | The response headers returned by a successful request to a webhook URL. | [optional] 


