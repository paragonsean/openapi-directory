

# EnvironmentResourceProperties

Properties of the environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataAccessFqdn** | **String** | The fully qualified domain name used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**dataAccessId** | **UUID** | An id used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**status** | [**EnvironmentStatus**](EnvironmentStatus.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | The time the resource was created. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |



