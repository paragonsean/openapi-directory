

# Job


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**availableToEmployees** | **Boolean** | Specifies whether an employee of the organization can apply for the job. |  [optional] |
|**blocks** | [**List&lt;JobBlocksInner&gt;**](JobBlocksInner.md) |  |  [optional] |
|**branch** | [**Branch**](Branch.md) |  |  [optional] |
|**closing** | **String** |  |  [optional] |
|**closingDate** | **LocalDate** |  |  [optional] |
|**closingHtml** | **String** | The closing section of the job description in HTML format |  [optional] |
|**code** | **String** | The code of the job. |  [optional] |
|**confidential** | **Boolean** |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customFields** | [**List&lt;CustomField&gt;**](CustomField.md) |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**deleted** | **Boolean** | Flag to indicate if the object is deleted. |  [optional] |
|**department** | [**Department**](Department.md) |  |  [optional] |
|**description** | **String** | A description of the object. |  [optional] |
|**descriptionHtml** | **String** | The job description in HTML format |  [optional] |
|**employmentTerms** | [**EmploymentTermsEnum**](#EmploymentTermsEnum) |  |  [optional] |
|**experience** | **String** | Level of experience required for the job role. |  [optional] |
|**followers** | **List&lt;String&gt;** |  |  [optional] |
|**hiringManagers** | **List&lt;String&gt;** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**jobPortalUrl** | **String** | URL of the job portal |  [optional] |
|**language** | **String** | language code according to ISO 639-1. For the United States - EN |  [optional] |
|**links** | [**List&lt;JobLinksInner&gt;**](JobLinksInner.md) |  |  [optional] |
|**location** | **String** | Specifies the location for the job posting. |  [optional] |
|**ownerId** | **String** |  |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**recordUrl** | **String** |  |  [optional] |
|**recruiters** | **List&lt;String&gt;** | The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant |  [optional] |
|**remote** | **Boolean** | Specifies whether the posting is for a remote job. |  [optional] |
|**requisitionId** | **String** | A job&#39;s Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company&#39;s internal processes. |  [optional] |
|**salary** | [**JobSalary**](JobSalary.md) |  |  [optional] |
|**sequence** | **Integer** | Sequence in relation to other jobs. |  [optional] |
|**slug** | **String** |  |  [optional] |
|**status** | **JobStatus** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**title** | **String** | The job title of the person. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**url** | **String** | URL of the job description |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | The visibility of the job |  [optional] |



## Enum: EmploymentTermsEnum

| Name | Value |
|---- | -----|
| FULL_TIME | &quot;full-time&quot; |
| PART_TIME | &quot;part-time&quot; |
| INTERNSHIP | &quot;internship&quot; |
| CONTRACTOR | &quot;contractor&quot; |
| EMPLOYEE | &quot;employee&quot; |
| FREELANCE | &quot;freelance&quot; |
| TEMP | &quot;temp&quot; |
| SEASONAL | &quot;seasonal&quot; |
| VOLUNTEER | &quot;volunteer&quot; |
| OTHER | &quot;other&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| PUBLIC | &quot;public&quot; |
| INTERNAL | &quot;internal&quot; |



