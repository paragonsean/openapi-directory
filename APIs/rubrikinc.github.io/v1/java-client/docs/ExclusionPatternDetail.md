

# ExclusionPatternDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the exclusion pattern. |  |
|**isActive** | **Boolean** | Indicates if the exclusion pattern applies. |  |
|**isMutable** | **Boolean** | Specifies whether the pattern is mutable. When this value is false, the pattern can not be altered. |  |
|**pattern** | **String** | The pattern is used for existing and future snapshots. The pattern can be a regular expression or filename. Files or directories that match the pattern are not shown in the results of searches and are excluded from restore and download operations. |  |
|**patternStatus** | **PatternStatus** |  |  |
|**primaryClusterId** | **String** |  |  |
|**sourceId** | **String** | ID of the protectable object to which the pattern applies. |  |



