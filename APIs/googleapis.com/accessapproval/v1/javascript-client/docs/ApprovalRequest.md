# AccessApprovalApi.ApprovalRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approve** | [**ApproveDecision**](ApproveDecision.md) |  | [optional] 
**dismiss** | [**DismissDecision**](DismissDecision.md) |  | [optional] 
**name** | **String** | The resource name of the request. Format is \&quot;{projects|folders|organizations}/{id}/approvalRequests/{approval_request}\&quot;. | [optional] 
**requestTime** | **String** | The time at which approval was requested. | [optional] 
**requestedDuration** | **String** | The requested access duration. | [optional] 
**requestedExpiration** | **String** | The original requested expiration for the approval. Calculated by adding the requested_duration to the request_time. | [optional] 
**requestedLocations** | [**AccessLocations**](AccessLocations.md) |  | [optional] 
**requestedReason** | [**AccessReason**](AccessReason.md) |  | [optional] 
**requestedResourceName** | **String** | The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a \&quot;full\&quot; resource name (e.g. \&quot;//library.googleapis.com/shelves/shelf1/books/book2\&quot;) or a \&quot;relative\&quot; resource name (e.g. \&quot;shelves/shelf1/books/book2\&quot;) as described in the resource name specification. | [optional] 
**requestedResourceProperties** | [**ResourceProperties**](ResourceProperties.md) |  | [optional] 


