

# GoogleCloudDialogflowCxV3FormParameter

Represents a form parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettings**](GoogleCloudDialogflowCxV3AdvancedSettings.md) |  |  [optional] |
|**defaultValue** | **Object** | The default value of an optional parameter. If the parameter is required, the default value will be ignored. |  [optional] |
|**displayName** | **String** | Required. The human-readable name of the parameter, unique within the form. |  [optional] |
|**entityType** | **String** | Required. The entity type of the parameter. Format: &#x60;projects/-/locations/-/agents/-/entityTypes/&#x60; for system entity types (for example, &#x60;projects/-/locations/-/agents/-/entityTypes/sys.date&#x60;), or &#x60;projects//locations//agents//entityTypes/&#x60; for developer entity types. |  [optional] |
|**fillBehavior** | [**GoogleCloudDialogflowCxV3FormParameterFillBehavior**](GoogleCloudDialogflowCxV3FormParameterFillBehavior.md) |  |  [optional] |
|**isList** | **Boolean** | Indicates whether the parameter represents a list of values. |  [optional] |
|**redact** | **Boolean** | Indicates whether the parameter content should be redacted in log. If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or entity type level redaction is enabled. |  [optional] |
|**required** | **Boolean** | Indicates whether the parameter is required. Optional parameters will not trigger prompts; however, they are filled if the user specifies them. Required parameters must be filled before form filling concludes. |  [optional] |



