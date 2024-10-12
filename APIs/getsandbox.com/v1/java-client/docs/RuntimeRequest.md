

# RuntimeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The body of the given request. |  [optional] |
|**contentType** | **String** | The content type of the body, for example &#39;application/json&#39;. |  [optional] |
|**fullSandboxId** | **String** | The parent ID of the Sandbox that received the request. |  [optional] |
|**fullSandboxName** | **String** | The parent name of the Sandbox that received the request. |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Transport headers for the given request. |  [optional] |
|**ip** | **String** | The requestor IP address. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** |  |  [optional] |
|**receivedTimestamp** | **Long** | The epoch time in milliseconds when the request was received. |  [optional] |
|**sandboxId** | **String** | The ID of the Sandbox that received the request. |  [optional] |
|**sandboxName** | **String** | The name of the Sandbox that received the request. |  [optional] |
|**transport** | **String** | Which transport the request was for, &#39;HTTP&#39;. |  [optional] |



