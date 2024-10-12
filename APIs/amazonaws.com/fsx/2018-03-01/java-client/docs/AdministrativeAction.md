

# AdministrativeAction

Describes a specific Amazon FSx administrative action for the current Windows, Lustre, or OpenZFS file system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administrativeActionType** | **AdministrativeActionType** |  |  [optional] |
|**progressPercent** | [**Integer**](Integer.md) |  |  [optional] |
|**requestTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**targetFileSystemValues** | [**AdministrativeActionTargetFileSystemValues**](AdministrativeActionTargetFileSystemValues.md) |  |  [optional] |
|**failureDetails** | [**AdministrativeActionFailureDetails**](AdministrativeActionFailureDetails.md) |  |  [optional] |
|**targetVolumeValues** | [**Volume**](Volume.md) |  |  [optional] |
|**targetSnapshotValues** | [**Snapshot**](Snapshot.md) |  |  [optional] |



