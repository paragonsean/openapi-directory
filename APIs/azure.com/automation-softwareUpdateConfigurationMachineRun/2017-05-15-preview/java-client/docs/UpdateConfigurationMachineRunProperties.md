

# UpdateConfigurationMachineRunProperties

Software update configuration machine run properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredDuration** | **String** | configured duration for the software update configuration run. |  [optional] [readonly] |
|**correlationId** | **UUID** | correlation id of the software update configuration machine run |  [optional] [readonly] |
|**createdBy** | **String** | createdBy property, which only appears in the response. |  [optional] [readonly] |
|**creationTime** | **OffsetDateTime** | Creation time of the resource, which only appears in the response. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | End time of the software update configuration machine run. |  [optional] [readonly] |
|**error** | [**SoftwareUpdateConfigurationMachineRunsListDefaultResponse**](SoftwareUpdateConfigurationMachineRunsListDefaultResponse.md) |  |  [optional] |
|**job** | [**JobNavigation**](JobNavigation.md) |  |  [optional] |
|**lastModifiedBy** | **String** | lastModifiedBy property, which only appears in the response. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | Last time resource was modified, which only appears in the response. |  [optional] [readonly] |
|**osType** | **String** | Operating system target of the software update configuration triggered this run |  [optional] [readonly] |
|**softwareUpdateConfiguration** | [**UpdateConfigurationNavigation**](UpdateConfigurationNavigation.md) |  |  [optional] |
|**sourceComputerId** | **UUID** | source computer id of the software update configuration machine run |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Start time of the software update configuration machine run. |  [optional] [readonly] |
|**status** | **String** | Status of the software update configuration machine run. |  [optional] [readonly] |
|**targetComputer** | **String** | name of the updated computer |  [optional] [readonly] |
|**targetComputerType** | **String** | type of the updated computer. |  [optional] [readonly] |



