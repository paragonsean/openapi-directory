# CloudPubSubApi.ModifyAckDeadlineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ackDeadlineSeconds** | **Number** | The new ack deadline with respect to the time this request was sent to the Pub/Sub system. Must be &gt;&#x3D; 0. For example, if the value is 10, the new ack deadline will expire 10 seconds after the &#x60;ModifyAckDeadline&#x60; call was made. Specifying zero may immediately make the message available for another pull request. | [optional] 
**ackId** | **String** | The acknowledgment ID. Either this or ack_ids must be populated, but not both. | [optional] 
**ackIds** | **[String]** | List of acknowledgment IDs. | [optional] 


