

# UpgradeOccurrence

An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distribution** | [**UpgradeDistribution**](UpgradeDistribution.md) |  |  [optional] |
|**_package** | **String** | Required - The package this Upgrade is for. |  [optional] |
|**parsedVersion** | [**Version**](Version.md) |  |  [optional] |



