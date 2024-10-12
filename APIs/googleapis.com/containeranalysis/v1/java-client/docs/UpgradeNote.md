

# UpgradeNote

An Upgrade Note represents a potential upgrade of a package to a given version. For each package version combination (i.e. bash 4.0, bash 4.1, bash 4.1.2), there will be an Upgrade Note. For Windows, windows_update field represents the information related to the update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distributions** | [**List&lt;UpgradeDistribution&gt;**](UpgradeDistribution.md) | Metadata about the upgrade for each specific operating system. |  [optional] |
|**_package** | **String** | Required for non-Windows OS. The package this Upgrade is for. |  [optional] |
|**version** | [**Version**](Version.md) |  |  [optional] |
|**windowsUpdate** | [**WindowsUpdate**](WindowsUpdate.md) |  |  [optional] |



