

# ProjectDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetAmount** | **Double** |  |  [optional] |
|**budgetHours** | **Double** |  |  [optional] |
|**companyIDFK** | **Integer** |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** |  |  [optional] |
|**dateUpdated** | **OffsetDateTime** |  |  [optional] |
|**defaultAccountTaskTypeIDFK** | **Integer** |  |  [optional] |
|**defaultAccountTaskTypeName** | **String** |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**members** | [**List&lt;ProjectMemberDetails&gt;**](ProjectMemberDetails.md) |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**projectBillableTypeCode** | **String** | Possible values: CategoryHourly, NoRate, NotBillable, PersonHourly, ProjectHourly |  [optional] |
|**projectBudgetTypeCode** | **String** | Possible Values: CategoryHours, NoBudget, PersonHours, ProjectFees, ProjectHours |  [optional] |
|**projectCategoryColor** | **String** | Html Hex Color Code starting with # |  [optional] |
|**projectCategoryIDFK** | **Integer** |  |  [optional] |
|**projectCategoryName** | **String** |  |  [optional] |
|**projectCode** | **String** |  |  [optional] |
|**projectHourlyRate** | **Double** |  |  [optional] |
|**projectID** | **Integer** |  |  [optional] |
|**projectOwnerUserIDFK** | **Integer** |  |  [optional] |
|**projectStatusCode** | **String** | Possible values: NotStarted, InProgress, Complete |  [optional] |
|**projectTags** | [**List&lt;ProjectTagItem&gt;**](ProjectTagItem.md) |  |  [optional] |
|**sections** | [**List&lt;ProjectSectionDetails&gt;**](ProjectSectionDetails.md) |  |  [optional] |
|**startDate** | **OffsetDateTime** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**isArchived** | **Boolean** |  |  [optional] |
|**isTaskRequiredOnTimesheet** | **Boolean** |  |  [optional] |



