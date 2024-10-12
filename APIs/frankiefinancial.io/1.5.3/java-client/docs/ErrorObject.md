

# ErrorObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commit** | **String** | Server version indication |  [optional] |
|**errorCode** | **String** | Frankie error code |  |
|**errorMsg** | **String** | Will describe the error |  |
|**httpStatusCode** | **Integer** | Deprecated: HTTP status code. Same as that which is passed back in the header.  |  [optional] |
|**issues** | [**List&lt;ErrorObjectIssuesInner&gt;**](ErrorObjectIssuesInner.md) |  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  |



