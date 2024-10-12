# AvazaApiDocumentation.NewTimesheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customMetadata** | **String** | Optional. free nvarchar field available via Api to store any additional metadata against a timesheet. We suggest you use Json or your preferred serialisation format. 1000 characters max. | [optional] 
**duration** | **Number** | The duration of the timesheet, in decimal hours. If null or 0, a timer will be started. | [optional] 
**entryDate** | **Date** | The date of the timesheet entry, with an optional start time component. | [optional] 
**notes** | **String** | Timesheet Notes | [optional] 
**projectIDFK** | **Number** | The project to associate the timesheet with. | [optional] 
**taskIDFK** | **Number** | Optional. Link the timesheet to a specific task | [optional] 
**timesheetCategoryIDFK** | **Number** | The Project timesheet category to link the timesheet to | [optional] 
**userIDFK** | **Number** | UserID for a Timesheet user in Avaza | [optional] 
**hasStartEndTime** | **Boolean** | If true, the start time will be take from the time component of the Entry Date field, and the end time will be calculated by adding the Duration to the StartDate | [optional] 
**isInvoiced** | **Boolean** | Optional. False by default. Allows you to mark the timesheet as invoiced in an external system. | [optional] 


