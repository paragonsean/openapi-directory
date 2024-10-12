

# GoogleCloudDialogflowV2beta1AutomatedAgentConfig

Defines the Automated Agent to connect to a conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agent** | **String** | Required. ID of the Dialogflow agent environment to use. This project needs to either be the same project as the conversation or you need to grant &#x60;service-@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60; the &#x60;Dialogflow API Service Agent&#x60; role in this project. - For ES agents, use format: &#x60;projects//locations//agent/environments/&#x60;. If environment is not specified, the default &#x60;draft&#x60; environment is used. Refer to [DetectIntentRequest](/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.DetectIntentRequest) for more details. - For CX agents, use format &#x60;projects//locations//agents//environments/&#x60;. If environment is not specified, the default &#x60;draft&#x60; environment is used. |  [optional] |
|**sessionTtl** | **String** | Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow CX session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day. |  [optional] |



