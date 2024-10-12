# DialogflowApi.GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | The confidence of the matched intent. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). | [optional] 
**displayName** | **String** | Always present. The display name of the last matched intent. | [optional] 
**lastMatchedIntent** | **String** | Always present. The unique identifier of the last matched intent. Format: &#x60;projects//locations//agents//intents/&#x60;. | [optional] 
**parameters** | [**{String: GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue}**](GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue.md) | Parameters identified as a result of intent matching. This is a map of the name of the identified parameter to the value of the parameter identified from the user&#39;s utterance. All parameters defined in the matched intent that are identified will be surfaced here. | [optional] 


