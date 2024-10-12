

# GoogleCloudDialogflowCxV3beta1IntentParameter

Represents an intent parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityType** | **String** | Required. The entity type of the parameter. Format: &#x60;projects/-/locations/-/agents/-/entityTypes/&#x60; for system entity types (for example, &#x60;projects/-/locations/-/agents/-/entityTypes/sys.date&#x60;), or &#x60;projects//locations//agents//entityTypes/&#x60; for developer entity types. |  [optional] |
|**id** | **String** | Required. The unique identifier of the parameter. This field is used by training phrases to annotate their parts. |  [optional] |
|**isList** | **Boolean** | Indicates whether the parameter represents a list of values. |  [optional] |
|**redact** | **Boolean** | Indicates whether the parameter content should be redacted in log. If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or entity type level redaction is enabled. |  [optional] |



