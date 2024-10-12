

# UpgradeDistribution

The Upgrade Distribution represents metadata about the Upgrade for each operating system (CPE). Some distributions have additional metadata around updates, classifying them into various categories and severities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classification** | **String** | The operating system classification of this Upgrade, as specified by the upstream operating system upgrade feed. |  [optional] |
|**cpeUri** | **String** | Required - The specific operating system this metadata applies to. See https://cpe.mitre.org/specification/. |  [optional] |
|**cve** | **List&lt;String&gt;** | The cve that would be resolved by this upgrade. |  [optional] |
|**severity** | **String** | The severity as specified by the upstream operating system. |  [optional] |



