

# CreateBulkMessageResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **URI** | The location of the created message if StatusCode equals Created. |  [optional] |
|**statusCode** | **Integer** | Status code of the individual messages as if it were being created through the non-bulk endpoint.  If a message was succesfully created, the status code will be 201 and location will contain an URL.  If a message was ignored, the status code will be 200 and the location will be empty. |  [optional] |



