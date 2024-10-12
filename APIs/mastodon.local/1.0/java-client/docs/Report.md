

# Report

Reports filed against users and/or statuses, to be taken action on by moderators.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionTaken** | **Boolean** |  |  [optional] |
|**actionTakenAt** | **OffsetDateTime** |  |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**comment** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**forwarded** | **Boolean** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**ruleIds** | **List&lt;Integer&gt;** |  |  [optional] |
|**statusIds** | **List&lt;Integer&gt;** |  |  [optional] |
|**targetAccount** | [**Account**](Account.md) |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;other&quot; |
| SPAM | &quot;spam&quot; |
| VIOLATION | &quot;violation&quot; |



