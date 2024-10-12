# SalesLoftPlatform.PeopleApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2PeopleIdJsonDelete**](PeopleApi.md#v2PeopleIdJsonDelete) | **DELETE** /v2/people/{id}.json | Delete a person
[**v2PeopleIdJsonGet**](PeopleApi.md#v2PeopleIdJsonGet) | **GET** /v2/people/{id}.json | Fetch a person
[**v2PeopleIdJsonPut**](PeopleApi.md#v2PeopleIdJsonPut) | **PUT** /v2/people/{id}.json | Update a person
[**v2PeopleJsonGet**](PeopleApi.md#v2PeopleJsonGet) | **GET** /v2/people.json | List people
[**v2PeopleJsonPost**](PeopleApi.md#v2PeopleJsonPost) | **POST** /v2/people.json | Create a person



## v2PeopleIdJsonDelete

> v2PeopleIdJsonDelete(id)

Delete a person

Deletes a person. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PeopleApi();
let id = "id_example"; // String | Person id
apiInstance.v2PeopleIdJsonDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Person id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2PeopleIdJsonGet

> Person v2PeopleIdJsonGet(id)

Fetch a person

Fetches a person, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PeopleApi();
let id = "id_example"; // String | Person ID
apiInstance.v2PeopleIdJsonGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Person ID | 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2PeopleIdJsonPut

> Person v2PeopleIdJsonPut(id, opts)

Update a person

Updates a person. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PeopleApi();
let id = "id_example"; // String | Person id
let opts = {
  'accountId': 56, // Number | ID of the Account to link this person to
  'city': "city_example", // String | City
  'contactRestrictions': ["null"], // [String] | Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message
  'country': "country_example", // String | Country
  'crmId': "crmId_example", // String | Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\"salesforce\\\" ID must be exactly 18 characters. A \\\"salesforce\\\" ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\"person:set_crm_id\\\" scope.  
  'crmIdType': "crmIdType_example", // String | The CRM that the provided crm_id is for. Must be one of: salesforce
  'customFields': {key: null}, // Object | Custom fields are defined by the user's team. Only fields with values are presented in the API.
  'doNotContact': true, // Boolean | Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed.
  'emailAddress': "emailAddress_example", // String | Email address
  'firstName': "firstName_example", // String | First name
  'homePhone': "homePhone_example", // String | Home phone without formatting
  'importId': 56, // Number | ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import
  'jobSeniority': "jobSeniority_example", // String | The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown
  'lastName': "lastName_example", // String | Last name
  'linkedinUrl': "linkedinUrl_example", // String | Linkedin URL
  'locale': "locale_example", // String | Time locale of the person
  'mobilePhone': "mobilePhone_example", // String | Mobile phone without formatting
  'ownerId': 56, // Number | ID of the User that owns this person
  'personCompanyIndustry': "personCompanyIndustry_example", // String | Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
  'personCompanyName': "personCompanyName_example", // String | Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
  'personCompanyWebsite': "personCompanyWebsite_example", // String | Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
  'personStageId': 56, // Number | ID of the PersonStage of this person
  'personalEmailAddress': "personalEmailAddress_example", // String | Personal email address
  'personalWebsite': "personalWebsite_example", // String | The website of this person
  'phone': "phone_example", // String | Phone without formatting
  'phoneExtension': "phoneExtension_example", // String | Phone extension without formatting
  'secondaryEmailAddress': "secondaryEmailAddress_example", // String | Alternate email address
  'state': "state_example", // String | State
  'tags': ["null"], // [String] | All tags applied to this person
  'title': "title_example", // String | Job title
  'twitterHandle': "twitterHandle_example", // String | The twitter handle of this person
  'workCity': "workCity_example", // String | Work location - city
  'workCountry': "workCountry_example", // String | Work location - country
  'workState': "workState_example" // String | Work location - state
};
apiInstance.v2PeopleIdJsonPut(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Person id | 
 **accountId** | **Number**| ID of the Account to link this person to | [optional] 
 **city** | **String**| City | [optional] 
 **contactRestrictions** | [**[String]**](String.md)| Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message | [optional] 
 **country** | **String**| Country | [optional] 
 **crmId** | **String**| Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;person:set_crm_id\\\&quot; scope.   | [optional] 
 **crmIdType** | **String**| The CRM that the provided crm_id is for. Must be one of: salesforce | [optional] 
 **customFields** | [**Object**](Object.md)| Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. | [optional] 
 **doNotContact** | **Boolean**| Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed. | [optional] 
 **emailAddress** | **String**| Email address | [optional] 
 **firstName** | **String**| First name | [optional] 
 **homePhone** | **String**| Home phone without formatting | [optional] 
 **importId** | **Number**| ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import | [optional] 
 **jobSeniority** | **String**| The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown | [optional] 
 **lastName** | **String**| Last name | [optional] 
 **linkedinUrl** | **String**| Linkedin URL | [optional] 
 **locale** | **String**| Time locale of the person | [optional] 
 **mobilePhone** | **String**| Mobile phone without formatting | [optional] 
 **ownerId** | **Number**| ID of the User that owns this person | [optional] 
 **personCompanyIndustry** | **String**| Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] 
 **personCompanyName** | **String**| Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] 
 **personCompanyWebsite** | **String**| Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] 
 **personStageId** | **Number**| ID of the PersonStage of this person | [optional] 
 **personalEmailAddress** | **String**| Personal email address | [optional] 
 **personalWebsite** | **String**| The website of this person | [optional] 
 **phone** | **String**| Phone without formatting | [optional] 
 **phoneExtension** | **String**| Phone extension without formatting | [optional] 
 **secondaryEmailAddress** | **String**| Alternate email address | [optional] 
 **state** | **String**| State | [optional] 
 **tags** | [**[String]**](String.md)| All tags applied to this person | [optional] 
 **title** | **String**| Job title | [optional] 
 **twitterHandle** | **String**| The twitter handle of this person | [optional] 
 **workCity** | **String**| Work location - city | [optional] 
 **workCountry** | **String**| Work location - country | [optional] 
 **workState** | **String**| Work location - state | [optional] 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2PeopleJsonGet

> [Person] v2PeopleJsonGet(opts)

List people

Fetches multiple person records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PeopleApi();
let opts = {
  'ids': [null], // [Number] | IDs of people to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'updatedAt': ["null"], // [String] | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'emailAddresses': ["null"], // [String] | Filters people by email address. Multiple emails can be applied. An additional value of \"_is_null\" can be passed to filter people that do not have an email address.
  'ownedByGuid': ["null"], // [String] | Filters people by the owner's guid. Multiple owner guids can be applied
  'personStageId': [null], // [Number] | Includes people that have a given person_stage. Multiple person stage ids can be applied. An additional value of \"_is_null\" can be passed to filter people that do not have a stage set.
  'crmId': ["null"], // [String] | Filters people by crm_id. Multiple crm ids can be applied
  'ownerCrmId': ["null"], // [String] | Filters people by owner_crm_id. Multiple owner_crm_ids can be applied. An additional value of \"_is_null\" can be passed to filter people that are unowned. A \"_not_in\" modifier can be used to exclude specific owner_crm_ids. Example: v2/people?owner_crm_id[_not_in]=id
  'doNotContact': true, // Boolean | Includes people that have a given do_not_contact property
  'canEmail': true, // Boolean | Includes people that can be emailed given do_not_contact and contact_restrictions property
  'canCall': true, // Boolean | Includes people that can be called given do_not_contact and contact_restrictions property
  'canText': true, // Boolean | Includes people that can be sent a text message given do_not_contact and contact_restrictions property
  'accountId': [null], // [Number] | Filters people by the account they are linked to. Multiple account ids can be applied
  'customFields': {key: null}, // Object | Filters by people matching all given custom fields. The custom field names are case-sensitive, but the provided values are case-insensitive. Example: v2/people?custom_fields[custom_field_name]=custom_field_value
  'importId': [null], // [Number] | Filters people that were imported by the given import ids. Multiple import ids can be applied. An additional value of \"_is_null\" can be passed to filter people that were not imported.
  'jobSeniority': ["null"], // [String] | Filters people by job seniorty. Multiple job seniorities can be applied. An additional value of \"_is_null\" can be passed to filter people do not have a job_seniority.
  'tagId': [null], // [Number] | Filters people by the tag ids applied to the person. Multiple tag ids can be applied.
  'ownerIsActive': true, // Boolean | Filters people by whether the owner is active or not.
  'cadenceId': [null], // [Number] | Filters people by the cadence that they are currently on. Multiple cadence_ids can be applied. An additional value of \"_is_null\" can be passed to filter people that are not on a cadence.
  'starredByGuid': ["null"], // [String] | Filters people who have been starred by the user guids given.
  'replied': true, // Boolean | Filters people by whether or not they have replied to an email or not.
  'bounced': true, // Boolean | Filters people by whether an email that was sent to them bounced or not.
  'success': true, // Boolean | Filters people by whether or not they have been marked as a success or not.
  'euResident': true, // Boolean | Filters people by whether or not they are marked as an European Union Resident or not.
  'title': ["null"], // [String] | Filters people by their title by exact match. Supports partial matching
  'country': ["null"], // [String] | Filters people by their country by exact match. Supports partial matching
  'state': ["null"], // [String] | Filters people by their state by exact match. Supports partial matching
  'city': ["null"], // [String] | Filters people by their city by exact match. Supports partial matching
  'lastContacted': {key: null}, // Object | Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range. Additional values of \"_is_null\" or \"_is_not_null\" can be passed to filter records that either have no timestamp value or any timestamp value. ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'createdAt': {key: null}, // Object | Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  '_new': true, // Boolean | Filters people by whether or not that person is on a cadence or if they have been contacted in any way.
  'phoneNumber': true, // Boolean | Filter people by whether or not they have a phone number or not
  'locales': ["null"], // [String] | Filters people by locales. Multiple locales can be applied. An additional value of \"Null\" can be passed to filter people that do not have a locale.
  'ownerId': [null], // [Number] | Filters people by owner_id. Multiple owner_ids can be applied.
  'query': "query_example", // String | For internal use only. This field does not comply with our backwards compatibility policies. This filter is for authenticated users of Salesloft only and will not work for OAuth Applications. Filters people by the string provided. Can search and filter by name, title, industry, email_address and linked account name.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at, last_contacted_at, name, title, job_seniority, call_count, sent_emails, clicked_emails, replied_emails, viewed_emails, account, cadence_stage_name. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2PeopleJsonGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[Number]**](Number.md)| IDs of people to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **updatedAt** | [**[String]**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **emailAddresses** | [**[String]**](String.md)| Filters people by email address. Multiple emails can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that do not have an email address. | [optional] 
 **ownedByGuid** | [**[String]**](String.md)| Filters people by the owner&#39;s guid. Multiple owner guids can be applied | [optional] 
 **personStageId** | [**[Number]**](Number.md)| Includes people that have a given person_stage. Multiple person stage ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that do not have a stage set. | [optional] 
 **crmId** | [**[String]**](String.md)| Filters people by crm_id. Multiple crm ids can be applied | [optional] 
 **ownerCrmId** | [**[String]**](String.md)| Filters people by owner_crm_id. Multiple owner_crm_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that are unowned. A \&quot;_not_in\&quot; modifier can be used to exclude specific owner_crm_ids. Example: v2/people?owner_crm_id[_not_in]&#x3D;id | [optional] 
 **doNotContact** | **Boolean**| Includes people that have a given do_not_contact property | [optional] 
 **canEmail** | **Boolean**| Includes people that can be emailed given do_not_contact and contact_restrictions property | [optional] 
 **canCall** | **Boolean**| Includes people that can be called given do_not_contact and contact_restrictions property | [optional] 
 **canText** | **Boolean**| Includes people that can be sent a text message given do_not_contact and contact_restrictions property | [optional] 
 **accountId** | [**[Number]**](Number.md)| Filters people by the account they are linked to. Multiple account ids can be applied | [optional] 
 **customFields** | [**Object**](.md)| Filters by people matching all given custom fields. The custom field names are case-sensitive, but the provided values are case-insensitive. Example: v2/people?custom_fields[custom_field_name]&#x3D;custom_field_value | [optional] 
 **importId** | [**[Number]**](Number.md)| Filters people that were imported by the given import ids. Multiple import ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that were not imported. | [optional] 
 **jobSeniority** | [**[String]**](String.md)| Filters people by job seniorty. Multiple job seniorities can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people do not have a job_seniority. | [optional] 
 **tagId** | [**[Number]**](Number.md)| Filters people by the tag ids applied to the person. Multiple tag ids can be applied. | [optional] 
 **ownerIsActive** | **Boolean**| Filters people by whether the owner is active or not. | [optional] 
 **cadenceId** | [**[Number]**](Number.md)| Filters people by the cadence that they are currently on. Multiple cadence_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that are not on a cadence. | [optional] 
 **starredByGuid** | [**[String]**](String.md)| Filters people who have been starred by the user guids given. | [optional] 
 **replied** | **Boolean**| Filters people by whether or not they have replied to an email or not. | [optional] 
 **bounced** | **Boolean**| Filters people by whether an email that was sent to them bounced or not. | [optional] 
 **success** | **Boolean**| Filters people by whether or not they have been marked as a success or not. | [optional] 
 **euResident** | **Boolean**| Filters people by whether or not they are marked as an European Union Resident or not. | [optional] 
 **title** | [**[String]**](String.md)| Filters people by their title by exact match. Supports partial matching | [optional] 
 **country** | [**[String]**](String.md)| Filters people by their country by exact match. Supports partial matching | [optional] 
 **state** | [**[String]**](String.md)| Filters people by their state by exact match. Supports partial matching | [optional] 
 **city** | [**[String]**](String.md)| Filters people by their city by exact match. Supports partial matching | [optional] 
 **lastContacted** | [**Object**](.md)| Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range. Additional values of \&quot;_is_null\&quot; or \&quot;_is_not_null\&quot; can be passed to filter records that either have no timestamp value or any timestamp value. ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **createdAt** | [**Object**](.md)| Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **_new** | **Boolean**| Filters people by whether or not that person is on a cadence or if they have been contacted in any way. | [optional] 
 **phoneNumber** | **Boolean**| Filter people by whether or not they have a phone number or not | [optional] 
 **locales** | [**[String]**](String.md)| Filters people by locales. Multiple locales can be applied. An additional value of \&quot;Null\&quot; can be passed to filter people that do not have a locale. | [optional] 
 **ownerId** | [**[Number]**](Number.md)| Filters people by owner_id. Multiple owner_ids can be applied. | [optional] 
 **query** | **String**| For internal use only. This field does not comply with our backwards compatibility policies. This filter is for authenticated users of Salesloft only and will not work for OAuth Applications. Filters people by the string provided. Can search and filter by name, title, industry, email_address and linked account name. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, last_contacted_at, name, title, job_seniority, call_count, sent_emails, clicked_emails, replied_emails, viewed_emails, account, cadence_stage_name. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Person]**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2PeopleJsonPost

> Person v2PeopleJsonPost(opts)

Create a person

Creates a person. Either email_address or phone/last_name must be provided as a unique lookup on the team. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PeopleApi();
let opts = {
  'accountId': 56, // Number | ID of the Account to link this person to
  'autotagDate': true, // Boolean | Whether the date should be added to this person as a tag. Default is false. The tag will be Y-m-d format.
  'city': "city_example", // String | City
  'contactRestrictions': ["null"], // [String] | Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message
  'country': "country_example", // String | Country
  'crmId': "crmId_example", // String | Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\"salesforce\\\" ID must be exactly 18 characters. A \\\"salesforce\\\" ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\"person:set_crm_id\\\" scope.  
  'crmIdType': "crmIdType_example", // String | The CRM that the provided crm_id is for. Must be one of: salesforce
  'customFields': {key: null}, // Object | Custom fields are defined by the user's team. Only fields with values are presented in the API.
  'doNotContact': true, // Boolean | Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed.
  'emailAddress': "emailAddress_example", // String | Email address
  'firstName': "firstName_example", // String | First name
  'homePhone': "homePhone_example", // String | Home phone without formatting
  'importId': 56, // Number | ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import
  'jobSeniority': "jobSeniority_example", // String | The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown
  'lastName': "lastName_example", // String | Last name
  'linkedinUrl': "linkedinUrl_example", // String | Linkedin URL
  'locale': "locale_example", // String | Time locale of the person
  'mobilePhone': "mobilePhone_example", // String | Mobile phone without formatting
  'ownerId': 56, // Number | ID of the User that owns this person
  'personCompanyIndustry': "personCompanyIndustry_example", // String | Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
  'personCompanyName': "personCompanyName_example", // String | Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
  'personCompanyWebsite': "personCompanyWebsite_example", // String | Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
  'personStageId': 56, // Number | ID of the PersonStage of this person
  'personalEmailAddress': "personalEmailAddress_example", // String | Personal email address
  'personalWebsite': "personalWebsite_example", // String | The website of this person
  'phone': "phone_example", // String | Phone without formatting
  'phoneExtension': "phoneExtension_example", // String | Phone extension without formatting
  'secondaryEmailAddress': "secondaryEmailAddress_example", // String | Alternate email address
  'state': "state_example", // String | State
  'tags': ["null"], // [String] | All tags applied to this person
  'title': "title_example", // String | Job title
  'twitterHandle': "twitterHandle_example", // String | The twitter handle of this person
  'workCity': "workCity_example", // String | Work location - city
  'workCountry': "workCountry_example", // String | Work location - country
  'workState': "workState_example" // String | Work location - state
};
apiInstance.v2PeopleJsonPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **Number**| ID of the Account to link this person to | [optional] 
 **autotagDate** | **Boolean**| Whether the date should be added to this person as a tag. Default is false. The tag will be Y-m-d format. | [optional] 
 **city** | **String**| City | [optional] 
 **contactRestrictions** | [**[String]**](String.md)| Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message | [optional] 
 **country** | **String**| Country | [optional] 
 **crmId** | **String**| Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;person:set_crm_id\\\&quot; scope.   | [optional] 
 **crmIdType** | **String**| The CRM that the provided crm_id is for. Must be one of: salesforce | [optional] 
 **customFields** | [**Object**](Object.md)| Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. | [optional] 
 **doNotContact** | **Boolean**| Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed. | [optional] 
 **emailAddress** | **String**| Email address | [optional] 
 **firstName** | **String**| First name | [optional] 
 **homePhone** | **String**| Home phone without formatting | [optional] 
 **importId** | **Number**| ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import | [optional] 
 **jobSeniority** | **String**| The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown | [optional] 
 **lastName** | **String**| Last name | [optional] 
 **linkedinUrl** | **String**| Linkedin URL | [optional] 
 **locale** | **String**| Time locale of the person | [optional] 
 **mobilePhone** | **String**| Mobile phone without formatting | [optional] 
 **ownerId** | **Number**| ID of the User that owns this person | [optional] 
 **personCompanyIndustry** | **String**| Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] 
 **personCompanyName** | **String**| Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] 
 **personCompanyWebsite** | **String**| Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] 
 **personStageId** | **Number**| ID of the PersonStage of this person | [optional] 
 **personalEmailAddress** | **String**| Personal email address | [optional] 
 **personalWebsite** | **String**| The website of this person | [optional] 
 **phone** | **String**| Phone without formatting | [optional] 
 **phoneExtension** | **String**| Phone extension without formatting | [optional] 
 **secondaryEmailAddress** | **String**| Alternate email address | [optional] 
 **state** | **String**| State | [optional] 
 **tags** | [**[String]**](String.md)| All tags applied to this person | [optional] 
 **title** | **String**| Job title | [optional] 
 **twitterHandle** | **String**| The twitter handle of this person | [optional] 
 **workCity** | **String**| Work location - city | [optional] 
 **workCountry** | **String**| Work location - country | [optional] 
 **workState** | **String**| Work location - state | [optional] 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

