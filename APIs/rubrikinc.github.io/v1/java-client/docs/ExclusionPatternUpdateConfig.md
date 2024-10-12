

# ExclusionPatternUpdateConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isActive** | **Boolean** | Specifies whether or not the exclusion pattern applies. Only applicable to mutable patterns. |  [optional] |
|**isMutable** | **Boolean** | Specifies whether the pattern is mutable. When this value is false, the pattern can not be altered. |  [optional] |
|**pattern** | **String** | The pattern is used for existing and future snapshots. The pattern can be a regular expression or filename. Files or directories that match the pattern are not shown in the results of searches and are excluded from restore and download operations. |  [optional] |



