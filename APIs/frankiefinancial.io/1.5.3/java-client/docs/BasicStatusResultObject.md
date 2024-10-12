

# BasicStatusResultObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  |
|**statusMsg** | **String** | Simple message describing the final status of the process. Only to be used in success case responses. Otherwise, use the ErrorObject.  |  |



