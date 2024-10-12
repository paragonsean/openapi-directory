

# GoogleCloudDialogflowCxV3beta1CompareVersionsRequest

The request message for Versions.CompareVersions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | The language to compare the flow versions for. If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. |  [optional] |
|**targetVersion** | **String** | Required. Name of the target flow version to compare with the base version. Use version ID &#x60;0&#x60; to indicate the draft version of the specified flow. Format: &#x60;projects//locations//agents//flows//versions/&#x60;. |  [optional] |



