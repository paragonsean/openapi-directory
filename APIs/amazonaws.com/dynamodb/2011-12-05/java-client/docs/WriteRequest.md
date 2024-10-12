

# WriteRequest

This structure is a Union of PutRequest and DeleteRequest. It can contain exactly one of <code>PutRequest</code> or <code>DeleteRequest</code>. Never Both. This is enforced in the code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**putRequest** | [**PutRequest**](PutRequest.md) |  |  [optional] |
|**deleteRequest** | [**DeleteRequest**](DeleteRequest.md) |  |  [optional] |



