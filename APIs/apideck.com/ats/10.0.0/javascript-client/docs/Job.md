# AtsApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**availableToEmployees** | **Boolean** | Specifies whether an employee of the organization can apply for the job. | [optional] 
**blocks** | [**[JobBlocksInner]**](JobBlocksInner.md) |  | [optional] 
**branch** | [**Branch**](Branch.md) |  | [optional] 
**closing** | **String** |  | [optional] 
**closingDate** | **Date** |  | [optional] 
**closingHtml** | **String** | The closing section of the job description in HTML format | [optional] 
**code** | **String** | The code of the job. | [optional] 
**confidential** | **Boolean** |  | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customFields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**deleted** | **Boolean** | Flag to indicate if the object is deleted. | [optional] 
**department** | [**Department**](Department.md) |  | [optional] 
**description** | **String** | A description of the object. | [optional] 
**descriptionHtml** | **String** | The job description in HTML format | [optional] 
**employmentTerms** | **String** |  | [optional] 
**experience** | **String** | Level of experience required for the job role. | [optional] 
**followers** | **[String]** |  | [optional] 
**hiringManagers** | **[String]** |  | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**jobPortalUrl** | **String** | URL of the job portal | [optional] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**links** | [**[JobLinksInner]**](JobLinksInner.md) |  | [optional] 
**location** | **String** | Specifies the location for the job posting. | [optional] 
**ownerId** | **String** |  | [optional] 
**publishedAt** | **Date** |  | [optional] [readonly] 
**recordUrl** | **String** |  | [optional] 
**recruiters** | **[String]** | The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant | [optional] 
**remote** | **Boolean** | Specifies whether the posting is for a remote job. | [optional] 
**requisitionId** | **String** | A job&#39;s Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company&#39;s internal processes. | [optional] 
**salary** | [**JobSalary**](JobSalary.md) |  | [optional] 
**sequence** | **Number** | Sequence in relation to other jobs. | [optional] 
**slug** | **String** |  | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**tags** | **[String]** |  | [optional] 
**title** | **String** | The job title of the person. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 
**url** | **String** | URL of the job description | [optional] 
**visibility** | **String** | The visibility of the job | [optional] 



## Enum: EmploymentTermsEnum


* `full-time` (value: `"full-time"`)

* `part-time` (value: `"part-time"`)

* `internship` (value: `"internship"`)

* `contractor` (value: `"contractor"`)

* `employee` (value: `"employee"`)

* `freelance` (value: `"freelance"`)

* `temp` (value: `"temp"`)

* `seasonal` (value: `"seasonal"`)

* `volunteer` (value: `"volunteer"`)

* `other` (value: `"other"`)





## Enum: VisibilityEnum


* `draft` (value: `"draft"`)

* `public` (value: `"public"`)

* `internal` (value: `"internal"`)




