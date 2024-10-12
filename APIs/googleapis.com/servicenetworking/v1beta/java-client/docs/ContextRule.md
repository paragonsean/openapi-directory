

# ContextRule

A context rule provides information about the context for an individual API element.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedRequestExtensions** | **List&lt;String&gt;** | A list of full type names or extension IDs of extensions allowed in grpc side channel from client to backend. |  [optional] |
|**allowedResponseExtensions** | **List&lt;String&gt;** | A list of full type names or extension IDs of extensions allowed in grpc side channel from backend to client. |  [optional] |
|**provided** | **List&lt;String&gt;** | A list of full type names of provided contexts. |  [optional] |
|**requested** | **List&lt;String&gt;** | A list of full type names of requested contexts. |  [optional] |
|**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. |  [optional] |



