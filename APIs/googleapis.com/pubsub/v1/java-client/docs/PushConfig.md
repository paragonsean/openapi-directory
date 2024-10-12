

# PushConfig

Configuration for a push delivery endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | Optional. Endpoint configuration attributes that can be used to control different aspects of the message delivery. The only currently supported attribute is &#x60;x-goog-version&#x60;, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata). If not present during the &#x60;CreateSubscription&#x60; call, it will default to the version of the Pub/Sub API used to make such call. If not present in a &#x60;ModifyPushConfig&#x60; call, its value will not be changed. &#x60;GetSubscription&#x60; calls will always return a valid version, even if the subscription was created without this attribute. The only supported values for the &#x60;x-goog-version&#x60; attribute are: * &#x60;v1beta1&#x60;: uses the push format defined in the v1beta1 Pub/Sub API. * &#x60;v1&#x60; or &#x60;v1beta2&#x60;: uses the push format defined in the v1 Pub/Sub API. For example: &#x60;attributes { \&quot;x-goog-version\&quot;: \&quot;v1\&quot; }&#x60; |  [optional] |
|**noWrapper** | [**NoWrapper**](NoWrapper.md) |  |  [optional] |
|**oidcToken** | [**OidcToken**](OidcToken.md) |  |  [optional] |
|**pubsubWrapper** | **Object** | The payload to the push endpoint is in the form of the JSON representation of a PubsubMessage (https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage). |  [optional] |
|**pushEndpoint** | **String** | Optional. A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use &#x60;https://example.com/push&#x60;. |  [optional] |



