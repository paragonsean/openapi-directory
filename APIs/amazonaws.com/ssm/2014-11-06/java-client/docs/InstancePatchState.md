

# InstancePatchState

Defines the high-level patch compliance state for a managed node, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the managed node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | [**String**](String.md) |  |  |
|**patchGroup** | [**String**](String.md) |  |  |
|**baselineId** | [**String**](String.md) |  |  |
|**snapshotId** | [**String**](String.md) |  |  [optional] |
|**installOverrideList** | [**String**](String.md) |  |  [optional] |
|**ownerInformation** | [**String**](String.md) |  |  [optional] |
|**installedCount** | [**Integer**](Integer.md) |  |  [optional] |
|**installedOtherCount** | [**Integer**](Integer.md) |  |  [optional] |
|**installedPendingRebootCount** | [**Integer**](Integer.md) |  |  [optional] |
|**installedRejectedCount** | [**Integer**](Integer.md) |  |  [optional] |
|**missingCount** | [**Integer**](Integer.md) |  |  [optional] |
|**failedCount** | [**Integer**](Integer.md) |  |  [optional] |
|**unreportedNotApplicableCount** | [**Integer**](Integer.md) |  |  [optional] |
|**notApplicableCount** | [**Integer**](Integer.md) |  |  [optional] |
|**operationStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**operationEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**operation** | [**PatchOperationType**](PatchOperationType.md) |  |  |
|**lastNoRebootInstallOperationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**rebootOption** | [**RebootOption**](RebootOption.md) |  |  [optional] |
|**criticalNonCompliantCount** | [**Integer**](Integer.md) |  |  [optional] |
|**securityNonCompliantCount** | [**Integer**](Integer.md) |  |  [optional] |
|**otherNonCompliantCount** | [**Integer**](Integer.md) |  |  [optional] |



