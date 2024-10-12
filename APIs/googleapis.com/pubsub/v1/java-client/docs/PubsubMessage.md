

# PubsubMessage

A message that is published by publishers and consumed by subscribers. The message must contain either a non-empty data field or at least one attribute. Note that client libraries represent this object differently depending on the language. See the corresponding [client library documentation](https://cloud.google.com/pubsub/docs/reference/libraries) for more information. See [quotas and limits] (https://cloud.google.com/pubsub/quotas) for more information about message limits.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | Optional. Attributes for this message. If this field is empty, the message must contain non-empty data. This can be used to filter messages on the subscription. |  [optional] |
|**data** | **byte[]** | Optional. The message data field. If this field is empty, the message must contain at least one attribute. |  [optional] |
|**messageId** | **String** | ID of this message, assigned by the server when the message is published. Guaranteed to be unique within the topic. This value may be read by a subscriber that receives a &#x60;PubsubMessage&#x60; via a &#x60;Pull&#x60; call or a push delivery. It must not be populated by the publisher in a &#x60;Publish&#x60; call. |  [optional] |
|**orderingKey** | **String** | Optional. If non-empty, identifies related messages for which publish order should be respected. If a &#x60;Subscription&#x60; has &#x60;enable_message_ordering&#x60; set to &#x60;true&#x60;, messages published with the same non-empty &#x60;ordering_key&#x60; value will be delivered to subscribers in the order in which they are received by the Pub/Sub system. All &#x60;PubsubMessage&#x60;s published in a given &#x60;PublishRequest&#x60; must specify the same &#x60;ordering_key&#x60; value. For more information, see [ordering messages](https://cloud.google.com/pubsub/docs/ordering). |  [optional] |
|**publishTime** | **String** | The time at which the message was published, populated by the server when it receives the &#x60;Publish&#x60; call. It must not be populated by the publisher in a &#x60;Publish&#x60; call. |  [optional] |



