

# SoftwareUpdateConfigurationRunProperties

Software update configuration properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computerCount** | **Integer** | Number of computers in the software update configuration run. |  [optional] [readonly] |
|**configuredDuration** | **String** | Configured duration for the software update configuration run. |  [optional] [readonly] |
|**createdBy** | **String** | CreatedBy property, which only appears in the response. |  [optional] [readonly] |
|**creationTime** | **OffsetDateTime** | Creation time of the resource, which only appears in the response. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | End time of the software update configuration run. |  [optional] [readonly] |
|**failedCount** | **Integer** | Number of computers with failed status. |  [optional] [readonly] |
|**lastModifiedBy** | **String** | LastModifiedBy property, which only appears in the response. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | Last time resource was modified, which only appears in the response. |  [optional] [readonly] |
|**osType** | **String** | Operating system target of the software update configuration triggered this run |  [optional] [readonly] |
|**softwareUpdateConfiguration** | [**UpdateConfigurationNavigation**](UpdateConfigurationNavigation.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of the software update configuration run. |  [optional] [readonly] |
|**status** | **String** | Status of the software update configuration run. |  [optional] [readonly] |
|**tasks** | [**SoftareUpdateConfigurationRunTasks**](SoftareUpdateConfigurationRunTasks.md) |  |  [optional] |



