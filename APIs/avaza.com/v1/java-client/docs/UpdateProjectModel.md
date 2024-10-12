

# UpdateProjectModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetAmount** | **Double** |  |  [optional] |
|**budgetHours** | **Double** |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**fieldsToUpdate** | **List&lt;String&gt;** |  |  [optional] |
|**projectBillableTypeCode** | **String** | The billing method of the project. (string, optional) Possible values: CategoryHourly, NoRate, NotBillable, PersonHourly, ProjectHourly |  [optional] |
|**projectBudgetTypeCode** | **String** | The project budgeting type. (string, optional) Possible values: NoBudget, PersonHours, ProjectFees, ProjectHours, CategoryHours |  [optional] |
|**projectCategoryIDFK** | **Integer** |  |  [optional] |
|**projectID** | **Integer** | The ID of the Project to update |  [optional] |
|**projectNotes** | **String** | (optional) Any descriptive notes about the project. (2000 characters max) |  [optional] |
|**projectStatusCode** | **String** | Update the project status (string, optional): (Possible values: NotStarted, InProgress, Complete, OnHold) |  [optional] |
|**projectTitle** | **String** | (optional) An updated project title. (255 characters max) |  [optional] |
|**startDate** | **OffsetDateTime** |  |  [optional] |
|**timesheetApprovalRequiredbyDefault** | **Boolean** | Whether timesheet approval should be required by default for newly added project members. |  [optional] |
|**isTaskRequiredOnTimesheet** | **Boolean** | Whether timesheets entered against this project require a task to be selected. |  [optional] |



