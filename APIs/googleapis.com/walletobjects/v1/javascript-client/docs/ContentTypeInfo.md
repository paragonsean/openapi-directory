# GoogleWalletApi.ContentTypeInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bestGuess** | **String** | Scotty&#39;s best guess of what the content type of the file is. | [optional] 
**fromBytes** | **String** | The content type of the file derived by looking at specific bytes (i.e. \&quot;magic bytes\&quot;) of the actual file. | [optional] 
**fromFileName** | **String** | The content type of the file derived from the file extension of the original file name used by the client. | [optional] 
**fromHeader** | **String** | The content type of the file as specified in the request headers, multipart headers, or RUPIO start request. | [optional] 
**fromUrlPath** | **String** | The content type of the file derived from the file extension of the URL path. The URL path is assumed to represent a file name (which is typically only true for agents that are providing a REST API). | [optional] 


