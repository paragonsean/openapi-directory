

# SyncV1Service


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. |  [optional] |
|**aclEnabled** | **Boolean** | Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource. It is disabled (false) by default. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**reachabilityDebouncingEnabled** | **Boolean** | Whether every &#x60;endpoint_disconnected&#x60; event should occur after a configurable delay. The default is &#x60;false&#x60;, where the &#x60;endpoint_disconnected&#x60; event occurs immediately after disconnection. When &#x60;true&#x60;, intervening reconnections can prevent the &#x60;endpoint_disconnected&#x60; event. |  [optional] |
|**reachabilityDebouncingWindow** | **Integer** | The reachability event delay in milliseconds if &#x60;reachability_debouncing_enabled&#x60; &#x3D; &#x60;true&#x60;.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before &#x60;webhook_url&#x60; is called, if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the reachability event from occurring. |  [optional] |
|**reachabilityWebhooksEnabled** | **Boolean** | Whether the service instance calls &#x60;webhook_url&#x60; when client endpoints connect to Sync. The default is &#x60;false&#x60;. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Service resource. |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. It is a read-only property, it cannot be assigned using REST API. |  [optional] |
|**url** | **URI** | The absolute URL of the Service resource. |  [optional] |
|**webhookUrl** | **URI** | The URL we call when Sync objects are manipulated. |  [optional] |
|**webhooksFromRestEnabled** | **Boolean** | Whether the Service instance should call &#x60;webhook_url&#x60; when the REST API is used to update Sync objects. The default is &#x60;false&#x60;. |  [optional] |



