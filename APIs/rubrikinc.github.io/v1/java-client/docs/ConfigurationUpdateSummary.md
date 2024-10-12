

# ConfigurationUpdateSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiUser** | **String** | The username of the account that changed the value. |  [optional] |
|**configChangeMetadata** | **String** | JSON-serialized blob of metadata used to fetch information about the configuration update. For example, the upgrade version, previous state, etc.  |  [optional] |
|**modifiedDateTime** | **OffsetDateTime** | The timestamp of the change. |  [optional] |
|**name** | **String** | The name of the updated configuration option. |  [optional] |
|**namespace** | **String** | The namespace of the updated configuration. Changes that do not begin with the string &#x60;local_&#x60; are cluster-wide changes. |  [optional] |
|**newValue** | **String** | The value of the configuration option after the update. |  [optional] |
|**nodeId** | **String** | The updated node. For cluster-wide configuration changes, this value is &#x60;all&#x60;. |  [optional] |
|**oldValue** | **String** | The original value of the configuration option. |  [optional] |
|**source** | **String** | The source of the change. |  [optional] |



