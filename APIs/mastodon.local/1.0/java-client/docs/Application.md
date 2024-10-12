

# Application

Represents an application that interfaces with the REST API to access accounts or post statuses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Client ID key, to be used for obtaining OAuth tokens |  [optional] |
|**clientSecret** | **String** | Client secret key, to be used for obtaining OAuth tokens |  [optional] |
|**name** | **String** | The name of your application. |  |
|**vapidKey** | **String** | Used for Push Streaming API. Returned with [POST /api/v1/apps](https://docs.joinmastodon.org/methods/apps/#create-an-application). Equivalent to [PushSubscription#server_key](https://docs.joinmastodon.org/entities/pushsubscription/#server_key) |  [optional] |
|**website** | **String** | The website associated with your application. Must be URL. |  [optional] |



