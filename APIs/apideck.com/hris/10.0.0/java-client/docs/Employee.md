

# Employee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**bankAccounts** | [**List&lt;BankAccount&gt;**](BankAccount.md) |  |  [optional] |
|**birthday** | **LocalDate** | The date of birth of the person. |  [optional] |
|**companyId** | **String** | The unique identifier of the company. |  [optional] |
|**companyName** | **String** | The name of the company. |  [optional] |
|**compensations** | [**List&lt;EmployeeCompensation&gt;**](EmployeeCompensation.md) |  |  [optional] |
|**countryOfBirth** | **String** | Country code according to ISO 3166-1 alpha-2. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customFields** | [**List&lt;CustomField&gt;**](CustomField.md) |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**deceasedOn** | **LocalDate** | The date the person deceased. |  [optional] |
|**deleted** | **Boolean** | Flag to indicate if the object is deleted. |  [optional] |
|**department** | **String** | The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field. |  [optional] |
|**departmentId** | **String** | Unique identifier of the department ID this employee belongs to. |  [optional] |
|**departmentName** | **String** | Name of the department this employee belongs to. |  [optional] |
|**description** | **String** | A description of the object. |  [optional] |
|**dietaryPreference** | **String** | Indicate the employee&#39;s dietary preference. |  [optional] |
|**directReports** | **List&lt;String&gt;** | Direct reports is an array of ids that reflect the individuals in an organizational hierarchy who are directly supervised by this specific employee. |  [optional] |
|**displayName** | **String** | The name used to display the employee, often a combination of their first and last names. |  [optional] |
|**division** | **String** | The division the person is currently in. Usually a collection of departments or teams or regions. |  [optional] |
|**divisionId** | **String** | Unique identifier of the division this employee belongs to. |  [optional] |
|**emails** | [**List&lt;Email&gt;**](Email.md) |  |  [optional] |
|**employeeNumber** | **String** | An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company. |  [optional] |
|**employmentEndDate** | **String** | An End Date is the date that the employee ended working at the company |  [optional] |
|**employmentRole** | [**EmployeeEmploymentRole**](EmployeeEmploymentRole.md) |  |  [optional] |
|**employmentStartDate** | **String** | A Start Date is the date that the employee started working at the company |  [optional] |
|**employmentStatus** | **EmploymentStatus** |  |  [optional] |
|**ethnicity** | **String** | The ethnicity of the employee |  [optional] |
|**firstName** | **String** | The first name of the person. |  [optional] |
|**foodAllergies** | **List&lt;String&gt;** | Indicate the employee&#39;s food allergies. |  [optional] |
|**gender** | **Gender** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**initials** | **String** | The initials of the person, usually derived from their first, middle, and last names. |  [optional] |
|**jobs** | [**List&lt;EmployeeJob&gt;**](EmployeeJob.md) |  |  [optional] |
|**languages** | **List&lt;String&gt;** |  |  [optional] |
|**lastName** | **String** | The last name of the person. |  [optional] |
|**leavingReason** | [**LeavingReasonEnum**](#LeavingReasonEnum) | The reason because the employment ended. |  [optional] |
|**manager** | [**EmployeeManager**](EmployeeManager.md) |  |  [optional] |
|**maritalStatus** | **String** | The marital status of the employee. |  [optional] |
|**middleName** | **String** | Middle name of the person. |  [optional] |
|**nationalities** | **List&lt;String&gt;** |  |  [optional] |
|**partner** | [**Person**](Person.md) |  |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**photoUrl** | **String** | The URL of the photo of a person. |  [optional] |
|**preferredLanguage** | **String** | language code according to ISO 639-1. For the United States - EN |  [optional] |
|**preferredName** | **String** | The name the employee prefers to be addressed by, which may be different from their legal name. |  [optional] |
|**probationPeriod** | [**ProbationPeriod**](ProbationPeriod.md) |  |  [optional] |
|**pronouns** | **String** | The preferred pronouns of the person. |  [optional] |
|**recordUrl** | **String** |  |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**salutation** | **String** | A formal salutation for the person. For example, &#39;Mr&#39;, &#39;Mrs&#39; |  [optional] |
|**socialLinks** | [**List&lt;SocialLink&gt;**](SocialLink.md) |  |  [optional] |
|**socialSecurityNumber** | **String** | A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions. |  [optional] |
|**source** | **String** | When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from. |  [optional] |
|**sourceId** | **String** | Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS). |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**taxCode** | **String** |  |  [optional] |
|**taxId** | **String** |  |  [optional] |
|**team** | [**Team**](Team.md) |  |  [optional] |
|**timezone** | **String** | The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London. |  [optional] |
|**title** | **String** | The job title of the person. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**worksRemote** | **Boolean** | Indicates if the employee works from a remote location. |  [optional] |



## Enum: LeavingReasonEnum

| Name | Value |
|---- | -----|
| DISMISSED | &quot;dismissed&quot; |
| RESIGNED | &quot;resigned&quot; |
| REDUNDANCY | &quot;redundancy&quot; |
| OTHER | &quot;other&quot; |



