

# AdminReport

Admin-level information about a filed report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**actionTaken** | **String** | The action taken to resolve this report. Enumerable oneOf. |  [optional] |
|**assignedAccount** | [**Account**](Account.md) |  |  [optional] |
|**comment** | **String** | An optional reason for reporting. |  [optional] |
|**createdAt** | **OffsetDateTime** | The time the report was filed. |  [optional] |
|**id** | **String** | The ID of the report in the database. Cast from an integer, but not guaranteed to be a number. |  [optional] |
|**statuses** | [**List&lt;Status&gt;**](Status.md) | Statuses attached to the report, for context. |  [optional] |
|**targetAccount** | [**Account**](Account.md) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The time of last action on this report. |  [optional] |



