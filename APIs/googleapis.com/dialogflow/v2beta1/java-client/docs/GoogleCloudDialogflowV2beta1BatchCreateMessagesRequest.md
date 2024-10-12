

# GoogleCloudDialogflowV2beta1BatchCreateMessagesRequest

The request message for Conversations.BatchCreateMessagesRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;GoogleCloudDialogflowV2beta1CreateMessageRequest&gt;**](GoogleCloudDialogflowV2beta1CreateMessageRequest.md) | Required. A maximum of 300 messages can be created in a batch. CreateMessageRequest.message.send_time is required. All created messages will have identical Message.create_time. |  [optional] |



