

# PubsubMessage

A message data and its attributes. The message payload must not be empty; it must contain either a non-empty data field, or at least one attribute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | Optional attributes for this message. |  [optional] |
|**data** | **byte[]** | The message payload. For JSON requests, the value of this field must be [base64-encoded](https://tools.ietf.org/html/rfc4648). |  [optional] |
|**messageId** | **String** | ID of this message, assigned by the server when the message is published. Guaranteed to be unique within the topic. This value may be read by a subscriber that receives a &#x60;PubsubMessage&#x60; via a &#x60;Pull&#x60; call or a push delivery. It must not be populated by the publisher in a &#x60;Publish&#x60; call. |  [optional] |
|**publishTime** | **String** | The time at which the message was published, populated by the server when it receives the &#x60;Publish&#x60; call. It must not be populated by the publisher in a &#x60;Publish&#x60; call. |  [optional] |



