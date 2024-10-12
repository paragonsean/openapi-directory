# ApplicationInsightsManagementClient.WorkbookProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Workbook category, as defined by the user at creation time. | 
**kind** | **String** | Enum indicating if this workbook definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [default to &#39;shared&#39;]
**name** | **String** | The user-defined name of the workbook. | 
**serializedData** | **String** | Configuration of this particular workbook. Configuration data is a string containing valid JSON | 
**sourceResourceId** | **String** | Optional resourceId for a source resource. | [optional] 
**tags** | **[String]** | A list of 0 or more tags that are associated with this workbook definition | [optional] 
**timeModified** | **String** | Date and time in UTC of the last modification that was made to this workbook definition. | [optional] [readonly] 
**userId** | **String** | Unique user id of the specific user that owns this workbook. | 
**version** | **String** | This instance&#39;s version of the data model. This can change as new features are added that can be marked workbook. | [optional] 
**workbookId** | **String** | Internally assigned unique id of the workbook definition. | 



## Enum: KindEnum


* `shared` (value: `"shared"`)

* `user` (value: `"user"`)




