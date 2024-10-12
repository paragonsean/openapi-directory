

# UpdateTimesheetModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customMetadata** | **String** | Optional. free nvarchar field available via Api to store any additional metadata against a timesheet. We suggest you use Json or your preferred serialisation format. 1000 characters max. |  [optional] |
|**duration** | **Double** |  |  [optional] |
|**entryDate** | **OffsetDateTime** |  |  [optional] |
|**fieldsToUpdate** | **List&lt;String&gt;** |  |  |
|**notes** | **String** |  |  [optional] |
|**projectIDFK** | **Integer** |  |  |
|**taskIDFK** | **Integer** |  |  [optional] |
|**timeSheetEntryID** | **Long** |  |  |
|**timesheetCategoryIDFK** | **Integer** |  |  [optional] |
|**hasStartEndTime** | **Boolean** |  |  [optional] |



