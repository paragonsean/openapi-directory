

# PostV3ProjectsIdHooksRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **String** | The URL to send the request to |  |
|**pushEvents** | **Boolean** | Trigger hook on push events |  [optional] |
|**issuesEvents** | **Boolean** | Trigger hook on issues events |  [optional] |
|**mergeRequestsEvents** | **Boolean** | Trigger hook on merge request events |  [optional] |
|**tagPushEvents** | **Boolean** | Trigger hook on tag push events |  [optional] |
|**noteEvents** | **Boolean** | Trigger hook on note(comment) events |  [optional] |
|**buildEvents** | **Boolean** | Trigger hook on build events |  [optional] |
|**pipelineEvents** | **Boolean** | Trigger hook on pipeline events |  [optional] |
|**wikiPageEvents** | **Boolean** | Trigger hook on wiki events |  [optional] |
|**enableSslVerification** | **Boolean** | Do SSL verification when triggering the hook |  [optional] |
|**token** | **String** | Secret token to validate received payloads; this will not be returned in the response |  [optional] |



