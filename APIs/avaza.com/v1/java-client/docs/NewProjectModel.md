

# NewProjectModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetAmount** | **Double** |  |  [optional] |
|**budgetHours** | **Double** |  |  [optional] |
|**companyIDFK** | **Integer** | An ID of a company in Avaza to create the Project under. You must provide either a CompanyID, or a CompanyName |  [optional] |
|**companyName** | **String** | The name for a Company to create the project under. Will create company unless it matches an existing company name |  [optional] |
|**currencyCode** | **String** | The ISO 3 letter currency code to use when creating a new Company. If not provided, the account&#39;s default currency will be used. |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**populateDefaultProjectMembers** | **Boolean** | Defaults to true. |  [optional] |
|**projectCategoryIDFK** | **Integer** |  |  [optional] |
|**projectCode** | **String** | Used when Manual Project Codes are enabled |  [optional] |
|**projectNotes** | **String** | Any descriptive notes about the project. (2000 characters max) |  [optional] |
|**projectStatusCode** | **String** |  |  [optional] |
|**projectTitle** | **String** | The title of the new project. (255 characters max) |  |
|**startDate** | **OffsetDateTime** |  |  [optional] |
|**timesheetApprovalRequiredbyDefault** | **Boolean** |  |  [optional] |
|**isTaskRequiredOnTimesheet** | **Boolean** |  |  [optional] |



