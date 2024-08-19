

# SuppressionContract

The details of the snoozed or dismissed rule; for example, the duration, name, and GUID associated with the rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suppressionId** | **String** | The GUID of the suppression. |  [optional] |
|**ttl** | **String** | The duration for which the suppression is valid. |  [optional] |
|**id** | **String** | The resource ID. |  [optional] [readonly] |
|**location** | **String** | The location of the resource. This cannot be changed after the resource is created. |  [optional] |
|**name** | **String** | The name of the resource. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | The tags of the resource. |  [optional] |
|**type** | **String** | The type of the resource. |  [optional] [readonly] |



