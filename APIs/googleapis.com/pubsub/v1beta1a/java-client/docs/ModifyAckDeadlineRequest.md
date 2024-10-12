

# ModifyAckDeadlineRequest

Request for the ModifyAckDeadline method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ackDeadlineSeconds** | **Integer** | The new ack deadline with respect to the time this request was sent to the Pub/Sub system. Must be &gt;&#x3D; 0. For example, if the value is 10, the new ack deadline will expire 10 seconds after the ModifyAckDeadline call was made. Specifying zero may immediately make the message available for another pull request. |  [optional] |
|**ackId** | **String** | The acknowledgment ID. Either this or ack_ids must be populated, not both. |  [optional] |
|**ackIds** | **List&lt;String&gt;** | List of acknowledgment IDs. Either this field or ack_id should be populated, not both. |  [optional] |
|**subscription** | **String** | Next Index: 5 The name of the subscription from which messages are being pulled. |  [optional] |



