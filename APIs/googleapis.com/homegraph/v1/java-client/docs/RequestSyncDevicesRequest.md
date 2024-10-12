

# RequestSyncDevicesRequest

Request type for the [`RequestSyncDevices`](#google.home.graph.v1.HomeGraphApiService.RequestSyncDevices) call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentUserId** | **String** | Required. Third-party user ID. |  [optional] |
|**async** | **Boolean** | Optional. If set, the request will be added to a queue and a response will be returned immediately. This enables concurrent requests for the given &#x60;agent_user_id&#x60;, but the caller will not receive any error responses. |  [optional] |



