# LetMcApiV2BasicTier2.DiaryAppointmentModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointmentType** | **String** | The diary appointment type. | [optional] 
**cancelled** | **Boolean** | Whether the appointment has been cancelled. | [optional] 
**comment** | **String** | The appointment comments text. | [optional] 
**createdAt** | **Date** | The date/time this appointment was created. | [optional] 
**createdBy** | **String** | The staff member that created this appointment. | [optional] 
**eTag** | **String** | A unique identifier defining the object and change revision. | [optional] 
**end** | **Date** | The end date/time of this appointment. | [optional] 
**OID** | **String** | The unique Object ID (OID). | [optional] 
**remindAt** | **Date** | The date/time to remind the staff member of this appointment. | [optional] 
**remindBefore** | **String** | The number of minutes before the appointment start date/time to remind the staff member. -1 means don&#39;t remind. | [optional] 
**staff** | **String** | The staff member holding this appointment. | [optional] 
**start** | **Date** | The start date/time of this appointment. | [optional] 
**subject** | **String** | The appointment subject text. | [optional] 



## Enum: RemindBeforeEnum


* `Min` (value: `"Min"`)

* `Min2` (value: `"Min2"`)

* `Min5` (value: `"Min5"`)

* `Min10` (value: `"Min10"`)

* `Min15` (value: `"Min15"`)

* `Min30` (value: `"Min30"`)

* `Min45` (value: `"Min45"`)

* `Hour` (value: `"Hour"`)

* `Hour2` (value: `"Hour2"`)

* `Hour3` (value: `"Hour3"`)

* `Hour6` (value: `"Hour6"`)

* `Hour12` (value: `"Hour12"`)

* `Day` (value: `"Day"`)

* `Day2` (value: `"Day2"`)

* `Day3` (value: `"Day3"`)

* `Week` (value: `"Week"`)

* `NoReminder` (value: `"NoReminder"`)




