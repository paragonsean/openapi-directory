# CloudPubSubApi.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ackDeadlineSeconds** | **Number** | This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call &#x60;ModifyAckDeadline&#x60; with the corresponding &#x60;ack_id&#x60; if using pull. The maximum custom deadline you can specify is 600 seconds (10 minutes). For push delivery, this value is also used to set the request timeout for the call to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message. If this parameter is 0, a default value of 10 seconds is used. | [optional] 
**name** | **String** | The name of the subscription. It must have the format &#x60;\&quot;projects/{project}/subscriptions/{subscription}\&quot;&#x60;. &#x60;{subscription}&#x60; must start with a letter, and contain only letters (&#x60;[A-Za-z]&#x60;), numbers (&#x60;[0-9]&#x60;), dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), periods (&#x60;.&#x60;), tildes (&#x60;~&#x60;), plus (&#x60;+&#x60;) or percent signs (&#x60;%&#x60;). It must be between 3 and 255 characters in length, and it must not start with &#x60;\&quot;goog\&quot;&#x60;. | [optional] 
**pushConfig** | [**PushConfig**](PushConfig.md) |  | [optional] 
**topic** | **String** | The name of the topic from which this subscription is receiving messages. The value of this field will be &#x60;_deleted-topic_&#x60; if the topic has been deleted. | [optional] 


