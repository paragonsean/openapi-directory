

# LongTermEnvironmentResourceProperties

Properties of the long-term environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storageConfiguration** | [**LongTermStorageConfigurationOutput**](LongTermStorageConfigurationOutput.md) |  |  |
|**timeSeriesIdProperties** | [**List&lt;TimeSeriesIdProperty&gt;**](TimeSeriesIdProperty.md) | The list of event properties which will be used to define the environment&#39;s time series id. |  |
|**warmStoreConfiguration** | [**WarmStoreConfigurationProperties**](WarmStoreConfigurationProperties.md) |  |  [optional] |
|**dataAccessFqdn** | **String** | The fully qualified domain name used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**dataAccessId** | **UUID** | An id used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**status** | [**EnvironmentStatus**](EnvironmentStatus.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | The time the resource was created. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |



