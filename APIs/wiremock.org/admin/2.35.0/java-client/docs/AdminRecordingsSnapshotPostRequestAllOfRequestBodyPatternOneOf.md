

# AdminRecordingsSnapshotPostRequestAllOfRequestBodyPatternOneOf

Automatically determine matcher based on content type (the default)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseInsensitive** | **Boolean** | If equalTo is used, match body use case-insensitive string comparison |  [optional] |
|**ignoreArrayOrder** | **Boolean** | If equalToJson is used, ignore order of array elements |  [optional] |
|**ignoreExtraElements** | **Boolean** | If equalToJson is used, matcher ignores extra elements in objects |  [optional] |
|**matcher** | [**MatcherEnum**](#MatcherEnum) |  |  [optional] |



## Enum: MatcherEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |



