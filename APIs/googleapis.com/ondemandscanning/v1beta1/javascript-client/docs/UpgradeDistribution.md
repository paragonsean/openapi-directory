# OnDemandScanningApi.UpgradeDistribution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **String** | The operating system classification of this Upgrade, as specified by the upstream operating system upgrade feed. For Windows the classification is one of the category_ids listed at https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ff357803(v&#x3D;vs.85) | [optional] 
**cpeUri** | **String** | Required - The specific operating system this metadata applies to. See https://cpe.mitre.org/specification/. | [optional] 
**cve** | **[String]** | The cve tied to this Upgrade. | [optional] 
**severity** | **String** | The severity as specified by the upstream operating system. | [optional] 


