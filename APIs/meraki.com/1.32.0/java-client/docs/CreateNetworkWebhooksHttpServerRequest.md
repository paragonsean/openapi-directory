

# CreateNetworkWebhooksHttpServerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | A name for easy reference to the HTTP server |  |
|**payloadTemplate** | [**CreateNetworkWebhooksHttpServerRequestPayloadTemplate**](CreateNetworkWebhooksHttpServerRequestPayloadTemplate.md) |  |  [optional] |
|**sharedSecret** | **String** | A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki. |  [optional] |
|**url** | **String** | The URL of the HTTP server. Once set, cannot be updated. |  |



