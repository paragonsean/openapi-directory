

# UpgradeOccurrence

An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability). For Windows, both distribution and windows_update contain information for the Windows update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distribution** | [**UpgradeDistribution**](UpgradeDistribution.md) |  |  [optional] |
|**_package** | **String** | Required for non-Windows OS. The package this Upgrade is for. |  [optional] |
|**parsedVersion** | [**Version**](Version.md) |  |  [optional] |
|**windowsUpdate** | [**WindowsUpdate**](WindowsUpdate.md) |  |  [optional] |



