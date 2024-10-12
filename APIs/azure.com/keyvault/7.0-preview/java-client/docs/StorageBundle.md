

# StorageBundle

A Storage account bundle consists of key vault storage account details plus its attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeKeyName** | **String** | The current active storage account key name. |  [optional] [readonly] |
|**attributes** | [**StorageAccountAttributes**](StorageAccountAttributes.md) |  |  [optional] |
|**autoRegenerateKey** | **Boolean** | whether keyvault should manage the storage account for the user. |  [optional] [readonly] |
|**id** | **String** | The storage account id. |  [optional] [readonly] |
|**regenerationPeriod** | **String** | The key regeneration time duration specified in ISO-8601 format. |  [optional] [readonly] |
|**resourceId** | **String** | The storage account resource id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs |  [optional] [readonly] |



