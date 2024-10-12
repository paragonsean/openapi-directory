# CloudTestingApi.ManualSharding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**testTargetsForShard** | [**[TestTargetsForShard]**](TestTargetsForShard.md) | Required. Group of packages, classes, and/or test methods to be run for each manually-created shard. You must specify at least one shard if this field is present. When you select one or more physical devices, the number of repeated test_targets_for_shard must be &lt;&#x3D; 50. When you select one or more ARM virtual devices, it must be &lt;&#x3D; 200. When you select only x86 virtual devices, it must be &lt;&#x3D; 500. | [optional] 


