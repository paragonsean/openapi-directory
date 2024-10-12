# CloudSpannerApi.BatchCreateSessionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessionCount** | **Number** | Required. The number of sessions to be created in this batch call. The API may return fewer than the requested number of sessions. If a specific number of sessions are desired, the client can make additional calls to BatchCreateSessions (adjusting session_count as necessary). | [optional] 
**sessionTemplate** | [**Session**](Session.md) |  | [optional] 


