

# DatastoreProperties

Displays the properties of the data store, including the ID, ARN, name, and the status of the data store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datastoreId** | [**String**](String.md) |  |  |
|**datastoreArn** | [**String**](String.md) |  |  |
|**datastoreName** | [**String**](String.md) |  |  [optional] |
|**datastoreStatus** | [**DatastoreStatus**](DatastoreStatus.md) |  |  |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**datastoreTypeVersion** | [**FHIRVersion**](FHIRVersion.md) |  |  |
|**datastoreEndpoint** | [**String**](String.md) |  |  |
|**sseConfiguration** | [**DatastorePropertiesSseConfiguration**](DatastorePropertiesSseConfiguration.md) |  |  [optional] |
|**preloadDataConfig** | [**DatastorePropertiesPreloadDataConfig**](DatastorePropertiesPreloadDataConfig.md) |  |  [optional] |
|**identityProviderConfiguration** | [**DatastorePropertiesIdentityProviderConfiguration**](DatastorePropertiesIdentityProviderConfiguration.md) |  |  [optional] |



