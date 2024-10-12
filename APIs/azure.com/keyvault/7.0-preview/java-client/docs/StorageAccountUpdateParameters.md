

# StorageAccountUpdateParameters

The storage account update parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeKeyName** | **String** | The current active storage account key name. |  [optional] |
|**attributes** | [**StorageAccountAttributes**](StorageAccountAttributes.md) |  |  [optional] |
|**autoRegenerateKey** | **Boolean** | whether keyvault should manage the storage account for the user. |  [optional] |
|**regenerationPeriod** | **String** | The key regeneration time duration specified in ISO-8601 format. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |



