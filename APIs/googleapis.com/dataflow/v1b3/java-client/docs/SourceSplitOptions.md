

# SourceSplitOptions

Hints for splitting a Source into bundles (parts for parallel processing) using SourceSplitRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**desiredBundleSizeBytes** | **String** | The source should be split into a set of bundles where the estimated size of each is approximately this many bytes. |  [optional] |
|**desiredShardSizeBytes** | **String** | DEPRECATED in favor of desired_bundle_size_bytes. |  [optional] |



