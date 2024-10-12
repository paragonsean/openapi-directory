# SalesLoftPlatform.AccountsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2AccountsIdJsonDelete**](AccountsApi.md#v2AccountsIdJsonDelete) | **DELETE** /v2/accounts/{id}.json | Delete an account
[**v2AccountsIdJsonGet**](AccountsApi.md#v2AccountsIdJsonGet) | **GET** /v2/accounts/{id}.json | Fetch an account
[**v2AccountsIdJsonPut**](AccountsApi.md#v2AccountsIdJsonPut) | **PUT** /v2/accounts/{id}.json | Update an existing Account
[**v2AccountsJsonGet**](AccountsApi.md#v2AccountsJsonGet) | **GET** /v2/accounts.json | List accounts
[**v2AccountsJsonPost**](AccountsApi.md#v2AccountsJsonPost) | **POST** /v2/accounts.json | Create an account



## v2AccountsIdJsonDelete

> v2AccountsIdJsonDelete(id)

Delete an account

Deletes an account. This operation is not reversible without contacting support. This operation can be called multiple times successfully.  Deleting an account will remove all connected people from that account. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountsApi();
let id = "id_example"; // String | Account ID
apiInstance.v2AccountsIdJsonDelete(id, (error, data, response) => {
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
 **id** | **String**| Account ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2AccountsIdJsonGet

> Account v2AccountsIdJsonGet(id)

Fetch an account

Fetches an account, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountsApi();
let id = "id_example"; // String | Account ID
apiInstance.v2AccountsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Account ID | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2AccountsIdJsonPut

> Account v2AccountsIdJsonPut(id, domain, name, opts)

Update an existing Account

Updates an account.  \&quot;domain\&quot; must be unique on the current team. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountsApi();
let id = "id_example"; // String | Account ID
let domain = "domain_example"; // String | Website domain, not a fully qualified URI
let name = "name_example"; // String | Account Full Name
let opts = {
  'accountTierId': 56, // Number | ID of the Account Tier for this Account
  'archived': true, // Boolean | Whether this Account should be archived or not. Setting this to true sets archived_at to the current time if it's not already set. Setting this to false will set archived_at to null
  'city': "city_example", // String | City
  'companyStageId': 56, // Number | ID of the CompanyStage assigned to this Account
  'companyType': "companyType_example", // String | Type of the Account's company
  'conversationalName': "conversationalName_example", // String | Conversational name of the Account
  'country': "country_example", // String | Country
  'crmId': "crmId_example", // String | Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\"salesforce\\\" ID must be exactly 18 characters. A \\\"salesforce\\\" ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\"account:set_crm_id\\\" scope.  
  'crmIdType': "crmIdType_example", // String | The CRM that the provided crm_id is for. Must be one of: salesforce
  'customFields': [null], // [Object] | Custom fields are defined by the user's team. Only fields with values are presented in the API.
  'description': "description_example", // String | Description
  'doNotContact': true, // Boolean | Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications
  'founded': "founded_example", // String | Date or year of founding
  'industry': "industry_example", // String | Industry
  'linkedinUrl': "linkedinUrl_example", // String | Full LinkedIn url
  'locale': "locale_example", // String | Time locale
  'ownerId': 56, // Number | ID of the User that owns this Account
  'phone': "phone_example", // String | Phone number without formatting
  'postalCode': "postalCode_example", // String | Postal code
  'revenueRange': "revenueRange_example", // String | Estimated revenue range
  'size': "size_example", // String | Estimated number of people in employment
  'state': "state_example", // String | State
  'street': "street_example", // String | Street name and number
  'tags': ["null"], // [String] | All tags applied to this Account
  'twitterHandle': "twitterHandle_example", // String | Twitter handle, with @
  'website': "website_example" // String | Website
};
apiInstance.v2AccountsIdJsonPut(id, domain, name, opts, (error, data, response) => {
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
 **id** | **String**| Account ID | 
 **domain** | **String**| Website domain, not a fully qualified URI | 
 **name** | **String**| Account Full Name | 
 **accountTierId** | **Number**| ID of the Account Tier for this Account | [optional] 
 **archived** | **Boolean**| Whether this Account should be archived or not. Setting this to true sets archived_at to the current time if it&#39;s not already set. Setting this to false will set archived_at to null | [optional] 
 **city** | **String**| City | [optional] 
 **companyStageId** | **Number**| ID of the CompanyStage assigned to this Account | [optional] 
 **companyType** | **String**| Type of the Account&#39;s company | [optional] 
 **conversationalName** | **String**| Conversational name of the Account | [optional] 
 **country** | **String**| Country | [optional] 
 **crmId** | **String**| Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;account:set_crm_id\\\&quot; scope.   | [optional] 
 **crmIdType** | **String**| The CRM that the provided crm_id is for. Must be one of: salesforce | [optional] 
 **customFields** | [**[Object]**](Object.md)| Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. | [optional] 
 **description** | **String**| Description | [optional] 
 **doNotContact** | **Boolean**| Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications | [optional] 
 **founded** | **String**| Date or year of founding | [optional] 
 **industry** | **String**| Industry | [optional] 
 **linkedinUrl** | **String**| Full LinkedIn url | [optional] 
 **locale** | **String**| Time locale | [optional] 
 **ownerId** | **Number**| ID of the User that owns this Account | [optional] 
 **phone** | **String**| Phone number without formatting | [optional] 
 **postalCode** | **String**| Postal code | [optional] 
 **revenueRange** | **String**| Estimated revenue range | [optional] 
 **size** | **String**| Estimated number of people in employment | [optional] 
 **state** | **String**| State | [optional] 
 **street** | **String**| Street name and number | [optional] 
 **tags** | [**[String]**](String.md)| All tags applied to this Account | [optional] 
 **twitterHandle** | **String**| Twitter handle, with @ | [optional] 
 **website** | **String**| Website | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2AccountsJsonGet

> [Account] v2AccountsJsonGet(opts)

List accounts

Fetches multiple account records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountsApi();
let opts = {
  'ids': [null], // [Number] | IDs of accounts to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'crmId': ["null"], // [String] | Filters accounts by crm_id. Multiple crm ids can be applied
  'tag': ["null"], // [String] | Filters accounts by the tags applied to the account. Multiple tags can be applied
  'tagId': [null], // [Number] | Filters accounts by the tag id's applied to the account. Multiple tag id's can be applied
  'createdAt': ["null"], // [String] | Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'updatedAt': ["null"], // [String] | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'domain': "domain_example", // String | Domain of the accounts to fetch. Domains are unique and lowercase
  'website': ["null"], // [String] | Filters accounts by website. Multiple websites can be applied. An additional value of \"_is_null\" can be passed to filter accounts that do not have a website.
  'archived': true, // Boolean | Filters accounts by archived_at status. Returns only accounts where archived_at is not null if this field is true. Returns only accounts where archived_at is null if this field is false. Do not pass this parameter to return both archived and unarchived accounts. This filter is not applied if any value other than \"true\" or \"false\" is passed.
  'name': ["null"], // [String] | Names of accounts to fetch. Name matches are exact and case sensitive. Multiple names can be fetched.
  'accountStageId': [null], // [Number] | Filters accounts by account_stage_id. Multiple account_stage_ids can be applied. An additional value of \"_is_null\" can be passed to filter accounts that do not have account_stage_id
  'accountTierId': [null], // [Number] | Filters accounts by account_tier_id. Multiple account tier ids can be applied
  'ownerId': ["null"], // [String] | Filters accounts by owner_id. Multiple owner_ids can be applied. An additional value of \"_is_null\" can be passed to filter accounts that are unowned
  'ownerIsActive': true, // Boolean | Filters accounts by whether the owner is active or not.
  'lastContacted': {key: null}, // Object | Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range. Additional values of \"_is_null\" or \"_is_not_null\" can be passed to filter records that either have no timestamp value or any timestamp value. ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'customFields': {key: null}, // Object | Filters by accounts matching all given custom fields. The custom field names are case-sensitive, but the provided values are case-insensitive. Example: v2/accounts?custom_fields[custom_field_name]=custom_field_value
  'industry': ["null"], // [String] | Filters accounts by industry by exact match. Supports partial matching
  'country': ["null"], // [String] | Filters accounts by country by exact match. Supports partial matching
  'state': ["null"], // [String] | Filters accounts by state by exact match. Supports partial matching
  'city': ["null"], // [String] | Filters accounts by city by exact match. Supports partial matching
  'ownerCrmId': ["null"], // [String] | Filters accounts by owner_crm_id. Multiple owner_crm_ids can be applied. An additional value of \"_is_null\" can be passed to filter accounts that are unowned. A \"_not_in\" modifier can be used to exclude specific owner_crm_ids. Example: v2/accounts?owner_crm_id[_not_in]=id
  'locales': ["null"], // [String] | Filters accounts by locale. Multiple locales are allowed
  'userRelationships': {key: null}, // Object | Filters by accounts matching all given user relationship fields, _is_null or _unmapped can be passed to filter accounts with null or unmapped user relationship values. Example: v2/accounts?user_relationships[name]=value
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at, last_contacted_at, account_stage, account_stage_name, account_tier, account_tier_name, name, counts_people. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2AccountsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of accounts to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **crmId** | [**[String]**](String.md)| Filters accounts by crm_id. Multiple crm ids can be applied | [optional] 
 **tag** | [**[String]**](String.md)| Filters accounts by the tags applied to the account. Multiple tags can be applied | [optional] 
 **tagId** | [**[Number]**](Number.md)| Filters accounts by the tag id&#39;s applied to the account. Multiple tag id&#39;s can be applied | [optional] 
 **createdAt** | [**[String]**](String.md)| Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **updatedAt** | [**[String]**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **domain** | **String**| Domain of the accounts to fetch. Domains are unique and lowercase | [optional] 
 **website** | [**[String]**](String.md)| Filters accounts by website. Multiple websites can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that do not have a website. | [optional] 
 **archived** | **Boolean**| Filters accounts by archived_at status. Returns only accounts where archived_at is not null if this field is true. Returns only accounts where archived_at is null if this field is false. Do not pass this parameter to return both archived and unarchived accounts. This filter is not applied if any value other than \&quot;true\&quot; or \&quot;false\&quot; is passed. | [optional] 
 **name** | [**[String]**](String.md)| Names of accounts to fetch. Name matches are exact and case sensitive. Multiple names can be fetched. | [optional] 
 **accountStageId** | [**[Number]**](Number.md)| Filters accounts by account_stage_id. Multiple account_stage_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that do not have account_stage_id | [optional] 
 **accountTierId** | [**[Number]**](Number.md)| Filters accounts by account_tier_id. Multiple account tier ids can be applied | [optional] 
 **ownerId** | [**[String]**](String.md)| Filters accounts by owner_id. Multiple owner_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that are unowned | [optional] 
 **ownerIsActive** | **Boolean**| Filters accounts by whether the owner is active or not. | [optional] 
 **lastContacted** | [**Object**](.md)| Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range. Additional values of \&quot;_is_null\&quot; or \&quot;_is_not_null\&quot; can be passed to filter records that either have no timestamp value or any timestamp value. ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **customFields** | [**Object**](.md)| Filters by accounts matching all given custom fields. The custom field names are case-sensitive, but the provided values are case-insensitive. Example: v2/accounts?custom_fields[custom_field_name]&#x3D;custom_field_value | [optional] 
 **industry** | [**[String]**](String.md)| Filters accounts by industry by exact match. Supports partial matching | [optional] 
 **country** | [**[String]**](String.md)| Filters accounts by country by exact match. Supports partial matching | [optional] 
 **state** | [**[String]**](String.md)| Filters accounts by state by exact match. Supports partial matching | [optional] 
 **city** | [**[String]**](String.md)| Filters accounts by city by exact match. Supports partial matching | [optional] 
 **ownerCrmId** | [**[String]**](String.md)| Filters accounts by owner_crm_id. Multiple owner_crm_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that are unowned. A \&quot;_not_in\&quot; modifier can be used to exclude specific owner_crm_ids. Example: v2/accounts?owner_crm_id[_not_in]&#x3D;id | [optional] 
 **locales** | [**[String]**](String.md)| Filters accounts by locale. Multiple locales are allowed | [optional] 
 **userRelationships** | [**Object**](.md)| Filters by accounts matching all given user relationship fields, _is_null or _unmapped can be passed to filter accounts with null or unmapped user relationship values. Example: v2/accounts?user_relationships[name]&#x3D;value | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, last_contacted_at, account_stage, account_stage_name, account_tier, account_tier_name, name, counts_people. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2AccountsJsonPost

> Account v2AccountsJsonPost(domain, name, opts)

Create an account

Creates an account.  \&quot;domain\&quot; must be unique on the current team. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountsApi();
let domain = "domain_example"; // String | Website domain, not a fully qualified URI
let name = "name_example"; // String | Account Full Name
let opts = {
  'accountTierId': 56, // Number | ID of the Account Tier for this Account
  'city': "city_example", // String | City
  'companyStageId': 56, // Number | ID of the CompanyStage assigned to this Account
  'companyType': "companyType_example", // String | Type of the Account's company
  'conversationalName': "conversationalName_example", // String | Conversational name of the Account
  'country': "country_example", // String | Country
  'crmId': "crmId_example", // String | Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\"salesforce\\\" ID must be exactly 18 characters. A \\\"salesforce\\\" ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\"account:set_crm_id\\\" scope.  
  'crmIdType': "crmIdType_example", // String | The CRM that the provided crm_id is for. Must be one of: salesforce
  'customFields': [null], // [Object] | Custom fields are defined by the user's team. Only fields with values are presented in the API.
  'description': "description_example", // String | Description
  'doNotContact': true, // Boolean | Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications
  'founded': "founded_example", // String | Date or year of founding
  'industry': "industry_example", // String | Industry
  'linkedinUrl': "linkedinUrl_example", // String | Full LinkedIn url
  'locale': "locale_example", // String | Time locale
  'ownerId': 56, // Number | ID of the User that owns this Account
  'phone': "phone_example", // String | Phone number without formatting
  'postalCode': "postalCode_example", // String | Postal code
  'revenueRange': "revenueRange_example", // String | Estimated revenue range
  'size': "size_example", // String | Estimated number of people in employment
  'state': "state_example", // String | State
  'street': "street_example", // String | Street name and number
  'tags': ["null"], // [String] | All tags applied to this Account
  'twitterHandle': "twitterHandle_example", // String | Twitter handle, with @
  'website': "website_example" // String | Website
};
apiInstance.v2AccountsJsonPost(domain, name, opts, (error, data, response) => {
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
 **domain** | **String**| Website domain, not a fully qualified URI | 
 **name** | **String**| Account Full Name | 
 **accountTierId** | **Number**| ID of the Account Tier for this Account | [optional] 
 **city** | **String**| City | [optional] 
 **companyStageId** | **Number**| ID of the CompanyStage assigned to this Account | [optional] 
 **companyType** | **String**| Type of the Account&#39;s company | [optional] 
 **conversationalName** | **String**| Conversational name of the Account | [optional] 
 **country** | **String**| Country | [optional] 
 **crmId** | **String**| Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;account:set_crm_id\\\&quot; scope.   | [optional] 
 **crmIdType** | **String**| The CRM that the provided crm_id is for. Must be one of: salesforce | [optional] 
 **customFields** | [**[Object]**](Object.md)| Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. | [optional] 
 **description** | **String**| Description | [optional] 
 **doNotContact** | **Boolean**| Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications | [optional] 
 **founded** | **String**| Date or year of founding | [optional] 
 **industry** | **String**| Industry | [optional] 
 **linkedinUrl** | **String**| Full LinkedIn url | [optional] 
 **locale** | **String**| Time locale | [optional] 
 **ownerId** | **Number**| ID of the User that owns this Account | [optional] 
 **phone** | **String**| Phone number without formatting | [optional] 
 **postalCode** | **String**| Postal code | [optional] 
 **revenueRange** | **String**| Estimated revenue range | [optional] 
 **size** | **String**| Estimated number of people in employment | [optional] 
 **state** | **String**| State | [optional] 
 **street** | **String**| Street name and number | [optional] 
 **tags** | [**[String]**](String.md)| All tags applied to this Account | [optional] 
 **twitterHandle** | **String**| Twitter handle, with @ | [optional] 
 **website** | **String**| Website | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

