

# ErrorsGroupList200ResponseErrorGroupsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appBuild** | **String** |  |  [optional] |
|**appVersion** | **String** |  |  |
|**codeRaw** | **String** |  |  [optional] |
|**count** | **Long** |  |  |
|**deviceCount** | **Long** |  |  |
|**errorGroupId** | **String** |  |  |
|**exceptionAppCode** | **Boolean** |  |  [optional] |
|**exceptionClassMethod** | **Boolean** |  |  [optional] |
|**exceptionClassName** | **String** |  |  [optional] |
|**exceptionFile** | **String** |  |  [optional] |
|**exceptionLine** | **String** |  |  [optional] |
|**exceptionMessage** | **String** |  |  [optional] |
|**exceptionMethod** | **String** |  |  [optional] |
|**exceptionType** | **String** |  |  [optional] |
|**firstOccurrence** | **OffsetDateTime** |  |  |
|**hidden** | **Boolean** |  |  [optional] |
|**lastOccurrence** | **OffsetDateTime** |  |  |
|**reasonFrames** | [**List&lt;ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner&gt;**](ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner.md) |  |  [optional] |
|**annotation** | **String** |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |
| IGNORED | &quot;ignored&quot; |



