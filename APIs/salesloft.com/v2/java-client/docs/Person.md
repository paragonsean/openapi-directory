

# Person


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**bouncing** | **Boolean** | Whether this person&#39;s current email address has bounced |  [optional] |
|**cadences** | [**List&lt;EmbeddedResource&gt;**](EmbeddedResource.md) | The list of active cadences person is added to |  [optional] |
|**city** | **String** | City |  [optional] |
|**contactRestrictions** | **List&lt;String&gt;** | Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message |  [optional] |
|**country** | **String** | Country |  [optional] |
|**counts** | [**PersonCounts**](PersonCounts.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the person was created |  [optional] |
|**crmId** | **String** | CRM ID |  [optional] |
|**crmObjectType** | **String** | CRM object type |  [optional] |
|**crmUrl** | **String** | CRM url |  [optional] |
|**customFields** | **Object** | Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. |  [optional] |
|**displayName** | **String** | Either the full name or the email address. Use this when showing a person&#39;s name |  [optional] |
|**doNotContact** | **Boolean** | Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed. |  [optional] |
|**emailAddress** | **String** | Email address |  [optional] |
|**euResident** | **Boolean** | Whether this person is marked as a European Union Resident or not |  [optional] |
|**firstName** | **String** | First name |  [optional] |
|**fullEmailAddress** | **String** | Full email address with name |  [optional] |
|**homePhone** | **String** | Home phone without formatting |  [optional] |
|**id** | **Integer** | Person ID |  [optional] |
|**_import** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**jobSeniority** | **String** | The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown |  [optional] |
|**lastCompletedStep** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**lastCompletedStepCadence** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**lastContactedAt** | **OffsetDateTime** | Last datetime this person was contacted |  [optional] |
|**lastContactedBy** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**lastContactedType** | **String** | The type of the last touch to this person. Can be call, email, other |  [optional] |
|**lastName** | **String** | Last name |  [optional] |
|**lastRepliedAt** | **OffsetDateTime** | Last datetime this person replied to an email |  [optional] |
|**linkedinUrl** | **String** | Linkedin URL |  [optional] |
|**locale** | **String** | Time locale of the person |  [optional] |
|**localeUtcOffset** | **Integer** | The locale&#39;s timezone offset from UTC in minutes |  [optional] |
|**mobilePhone** | **String** | Mobile phone without formatting |  [optional] |
|**mostRecentCadence** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**owner** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**ownerCrmId** | **String** | Mapped owner field from your CRM |  [optional] |
|**personCompanyIndustry** | **String** | Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended |  [optional] |
|**personCompanyName** | **String** | Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended |  [optional] |
|**personCompanyWebsite** | **String** | Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended |  [optional] |
|**personStage** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**personalEmailAddress** | **String** | Personal email address |  [optional] |
|**personalWebsite** | **String** | The website of this person |  [optional] |
|**phone** | **String** | Phone without formatting |  [optional] |
|**phoneExtension** | **String** | Phone extension without formatting |  [optional] |
|**secondaryEmailAddress** | **String** | Alternate email address |  [optional] |
|**starred** | **Boolean** | Whether this person is starred by the current user |  [optional] |
|**state** | **String** | State |  [optional] |
|**successCount** | **Integer** | The person&#39;s success count. 1 if person has any active successes, 0 otherwise. |  [optional] |
|**tags** | **List&lt;String&gt;** | All tags applied to this person |  [optional] |
|**title** | **String** | Job title |  [optional] |
|**twitterHandle** | **String** | The twitter handle of this person |  [optional] |
|**untouched** | **Boolean** | The person&#39;s untouched status |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the person was last updated |  [optional] |
|**workCity** | **String** | Work location - city |  [optional] |
|**workCountry** | **String** | Work location - country |  [optional] |
|**workState** | **String** | Work location - state |  [optional] |



