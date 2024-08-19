

# NotificationSettings

This type is the union of the settings types for each of the various notification types supported by the API.  The properties correspond to the following notification types:  #### All Types - onBuildSuccess - onBuildFailure - onBuildStatusChanged  #### Campfire - account - authToken - room - template  #### Email - subjectTemplate - bodyTemplate - recipients - recipientsValue  #### GitHubPullRequest - authToken - template  #### HipChat - authToken - from - room - template - serverUrl  #### Slack - incomingWebhookUrl - authToken - channel - template  #### Webhook - method - url - headers - headersValue - addCustomRequestBody - customRequestBodyContentType - customRequestBody  #### VSOTeamRoom - vsoAccount - username - password - room - template 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**$type** | **NotificationSettingsType** |  |  [optional] |
|**account** | **String** |  |  [optional] |
|**addCustomRequestBody** | **Boolean** |  |  [optional] |
|**authToken** | [**StoredValue**](StoredValue.md) |  |  [optional] |
|**bodyTemplate** | **String** |  |  [optional] |
|**channel** | **String** |  |  [optional] |
|**customRequestBody** | **String** |  |  [optional] |
|**customRequestBodyContentType** | **String** |  |  [optional] |
|**from** | **String** |  |  [optional] |
|**headers** | [**List&lt;StoredNameValue&gt;**](StoredNameValue.md) |  |  [optional] |
|**headersValue** | **String** |  |  [optional] |
|**incomingWebhookUrl** | **URI** |  |  [optional] |
|**method** | **HttpMethodRestricted** |  |  [optional] |
|**onBuildFailure** | **Boolean** |  |  [optional] |
|**onBuildStatusChanged** | **Boolean** |  |  [optional] |
|**onBuildSuccess** | **Boolean** |  |  [optional] |
|**password** | [**StoredValue**](StoredValue.md) |  |  [optional] |
|**recipients** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**recipientsValue** | **String** |  |  [optional] |
|**room** | **String** |  |  [optional] |
|**serverUrl** | **URI** |  |  [optional] |
|**subjectTemplate** | **String** |  |  [optional] |
|**template** | **String** |  |  [optional] |
|**url** | **URI** |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**vsoAccount** | **String** |  |  [optional] |



