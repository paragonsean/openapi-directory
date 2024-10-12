

# CrashGroupsList200ResponseCrashGroupsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotation** | **String** |  |  |
|**appVersion** | **String** |  |  |
|**build** | **String** |  |  |
|**count** | **Integer** |  |  |
|**crashGroupId** | **String** |  |  |
|**crashReason** | **String** |  |  |
|**displayId** | **String** |  |  |
|**exception** | **String** |  |  [optional] |
|**fatal** | **Boolean** | Crash or handled exception |  |
|**firstOccurrence** | **OffsetDateTime** |  |  |
|**impactedUsers** | **Integer** |  |  [optional] |
|**lastOccurrence** | **OffsetDateTime** |  |  |
|**newCrashGroupId** | **String** |  |  |
|**reasonFrame** | [**CrashGroupsList200ResponseCrashGroupsInnerReasonFrame**](CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |
| IGNORED | &quot;ignored&quot; |



