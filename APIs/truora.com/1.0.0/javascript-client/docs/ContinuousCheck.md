# ChecksApi.ContinuousCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuousCheckID** | **String** | Continuous check ID [partition key and sort key] | [optional] 
**continuousCheckStatus** | **String** | Shows whether the background check score rose, fell, stood the same or was just created | 
**creationDate** | **Date** | Continuous check creation date in RFC3339 format | [optional] 
**enabled** | **Boolean** | Indicates whether continuous check is enabled | [optional] 
**frequency** | **String** | Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks | 
**history** | [**ContinuousCheckEntry**](ContinuousCheckEntry.md) |  | [optional] 
**lastCheckID** | **String** | Last check ID | 
**nextRunDate** | **Date** | Next background check date, in RFC3339 format (without time) | [optional] 
**originalCheck** | [**Check**](Check.md) |  | [optional] 
**updateDate** | **Date** | Continuous check update date in RFC3339 format | [optional] 



## Enum: ContinuousCheckStatusEnum


* `new` (value: `"new"`)

* `up` (value: `"up"`)

* `down` (value: `"down"`)

* `same` (value: `"same"`)




