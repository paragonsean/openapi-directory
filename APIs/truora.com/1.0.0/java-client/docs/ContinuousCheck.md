

# ContinuousCheck

Continuous check allows for background checks to be performed on the same people or vehicles periodically and notifies if new information is found. Allowing companies to keep an eye on their workforce or vehicle fleet for any recent wrongdoing they might be involved in.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuousCheckID** | **String** | Continuous check ID [partition key and sort key] |  [optional] |
|**continuousCheckStatus** | [**ContinuousCheckStatusEnum**](#ContinuousCheckStatusEnum) | Shows whether the background check score rose, fell, stood the same or was just created |  |
|**creationDate** | **LocalDate** | Continuous check creation date in RFC3339 format |  [optional] |
|**enabled** | **Boolean** | Indicates whether continuous check is enabled |  [optional] |
|**frequency** | **String** | Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks |  |
|**history** | [**ContinuousCheckEntry**](ContinuousCheckEntry.md) |  |  [optional] |
|**lastCheckID** | **String** | Last check ID |  |
|**nextRunDate** | **LocalDate** | Next background check date, in RFC3339 format (without time) |  [optional] |
|**originalCheck** | [**Check**](Check.md) |  |  [optional] |
|**updateDate** | **LocalDate** | Continuous check update date in RFC3339 format |  [optional] |



## Enum: ContinuousCheckStatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;new&quot; |
| UP | &quot;up&quot; |
| DOWN | &quot;down&quot; |
| SAME | &quot;same&quot; |



