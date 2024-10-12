# TheJiraCloudPlatformRestApi.JQLApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAutoComplete**](JQLApi.md#getAutoComplete) | **GET** /rest/api/3/jql/autocompletedata | Get field reference data (GET)
[**getAutoCompletePost**](JQLApi.md#getAutoCompletePost) | **POST** /rest/api/3/jql/autocompletedata | Get field reference data (POST)
[**getFieldAutoCompleteForQueryString**](JQLApi.md#getFieldAutoCompleteForQueryString) | **GET** /rest/api/3/jql/autocompletedata/suggestions | Get field auto complete suggestions
[**migrateQueries**](JQLApi.md#migrateQueries) | **POST** /rest/api/3/jql/pdcleaner | Convert user identifiers to account IDs in JQL queries
[**parseJqlQueries**](JQLApi.md#parseJqlQueries) | **POST** /rest/api/3/jql/parse | Parse JQL query
[**sanitiseJqlQueries**](JQLApi.md#sanitiseJqlQueries) | **POST** /rest/api/3/jql/sanitize | Sanitize JQL queries



## getAutoComplete

> JQLReferenceData getAutoComplete()

Get field reference data (GET)

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.  To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.JQLApi();
apiInstance.getAutoComplete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**JQLReferenceData**](JQLReferenceData.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAutoCompletePost

> JQLReferenceData getAutoCompletePost(searchAutoCompleteFilter)

Get field reference data (POST)

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.  This operation can filter the custom fields returned by project. Invalid project IDs in &#x60;projectIds&#x60; are ignored. System fields are always returned.  It can also return the collapsed field for custom fields. Collapsed fields enable searches to be performed across all fields with the same name and of the same field type. For example, the collapsed field &#x60;Component - Component[Dropdown]&#x60; enables dropdown fields &#x60;Component - cf[10061]&#x60; and &#x60;Component - cf[10062]&#x60; to be searched simultaneously.  **[Permissions](#permissions) required:** None.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.JQLApi();
let searchAutoCompleteFilter = {"includeCollapsedFields":true,"projectIds":[10000,10001,10002]}; // SearchAutoCompleteFilter | 
apiInstance.getAutoCompletePost(searchAutoCompleteFilter, (error, data, response) => {
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
 **searchAutoCompleteFilter** | [**SearchAutoCompleteFilter**](SearchAutoCompleteFilter.md)|  | 

### Return type

[**JQLReferenceData**](JQLReferenceData.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFieldAutoCompleteForQueryString

> AutoCompleteSuggestions getFieldAutoCompleteForQueryString(opts)

Get field auto complete suggestions

Returns the JQL search auto complete suggestions for a field.  Suggestions can be obtained by providing:   *  &#x60;fieldName&#x60; to get a list of all values for the field.  *  &#x60;fieldName&#x60; and &#x60;fieldValue&#x60; to get a list of values containing the text in &#x60;fieldValue&#x60;.  *  &#x60;fieldName&#x60; and &#x60;predicateName&#x60; to get a list of all predicate values for the field.  *  &#x60;fieldName&#x60;, &#x60;predicateName&#x60;, and &#x60;predicateValue&#x60; to get a list of predicate values containing the text in &#x60;predicateValue&#x60;.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.JQLApi();
let opts = {
  'fieldName': "reporter", // String | The name of the field.
  'fieldValue': "fieldValue_example", // String | The partial field item name entered by the user.
  'predicateName': "predicateName_example", // String | The name of the [ CHANGED operator predicate](https://confluence.atlassian.com/x/hQORLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for which the suggestions are generated. The valid predicate operators are *by*, *from*, and *to*.
  'predicateValue': "predicateValue_example" // String | The partial predicate item name entered by the user.
};
apiInstance.getFieldAutoCompleteForQueryString(opts, (error, data, response) => {
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
 **fieldName** | **String**| The name of the field. | [optional] 
 **fieldValue** | **String**| The partial field item name entered by the user. | [optional] 
 **predicateName** | **String**| The name of the [ CHANGED operator predicate](https://confluence.atlassian.com/x/hQORLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for which the suggestions are generated. The valid predicate operators are *by*, *from*, and *to*. | [optional] 
 **predicateValue** | **String**| The partial predicate item name entered by the user. | [optional] 

### Return type

[**AutoCompleteSuggestions**](AutoCompleteSuggestions.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrateQueries

> ConvertedJQLQueries migrateQueries(jQLPersonalDataMigrationRequest)

Convert user identifiers to account IDs in JQL queries

Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.  You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/).  **[Permissions](#permissions) required:** Permission to access Jira.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.JQLApi();
let jQLPersonalDataMigrationRequest = {"queryStrings":["assignee = mia","issuetype = Bug AND assignee in (mia) AND reporter in (alana) order by lastViewed DESC"]}; // JQLPersonalDataMigrationRequest | 
apiInstance.migrateQueries(jQLPersonalDataMigrationRequest, (error, data, response) => {
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
 **jQLPersonalDataMigrationRequest** | [**JQLPersonalDataMigrationRequest**](JQLPersonalDataMigrationRequest.md)|  | 

### Return type

[**ConvertedJQLQueries**](ConvertedJQLQueries.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## parseJqlQueries

> ParsedJqlQueries parseJqlQueries(jqlQueriesToParse, opts)

Parse JQL query

Parses and validates JQL queries.  Validation is performed in context of the current user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.JQLApi();
let jqlQueriesToParse = {"queries":["summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER startOfMonth(-1M) ORDER BY updated DESC","issue.property[\"spaces here\"].value in (\"Service requests\", Incidents)","invalid query","summary = test","summary in test","project = INVALID","universe = 42"]}; // JqlQueriesToParse | 
let opts = {
  'validation': "'strict'" // String | How to validate the JQL query and treat the validation results. Validation options include:   *  `strict` Returns all errors. If validation fails, the query structure is not returned.  *  `warn` Returns all errors. If validation fails but the JQL query is correctly formed, the query structure is returned.  *  `none` No validation is performed. If JQL query is correctly formed, the query structure is returned.
};
apiInstance.parseJqlQueries(jqlQueriesToParse, opts, (error, data, response) => {
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
 **jqlQueriesToParse** | [**JqlQueriesToParse**](JqlQueriesToParse.md)|  | 
 **validation** | **String**| How to validate the JQL query and treat the validation results. Validation options include:   *  &#x60;strict&#x60; Returns all errors. If validation fails, the query structure is not returned.  *  &#x60;warn&#x60; Returns all errors. If validation fails but the JQL query is correctly formed, the query structure is returned.  *  &#x60;none&#x60; No validation is performed. If JQL query is correctly formed, the query structure is returned. | [optional] [default to &#39;strict&#39;]

### Return type

[**ParsedJqlQueries**](ParsedJqlQueries.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sanitiseJqlQueries

> SanitizedJqlQueries sanitiseJqlQueries(jqlQueriesToSanitize)

Sanitize JQL queries

Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn&#39;t have permission to view the entity.  For example, if the query contains the clause *project &#x3D; &#39;Secret project&#39;*, and a user does not have browse permission for the project \&quot;Secret project\&quot;, the sanitized query replaces the clause with *project &#x3D; 12345\&quot;* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user.  Note that sanitization doesn&#39;t make the queries GDPR-compliant, because it doesn&#39;t remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-api-3-jql-sanitize-post).  Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.JQLApi();
let jqlQueriesToSanitize = {"queries":[{"query":"project = 'Sample project'"},{"accountId":"5b10ac8d82e05b22cc7d4ef5","query":"project = 'Sample project'"},{"accountId":"cda2aa1395ac195d951b3387","query":"project = 'Sample project'"},{"accountId":"5b10ac8d82e05b22cc7d4ef5","query":"invalid query"}]}; // JqlQueriesToSanitize | 
apiInstance.sanitiseJqlQueries(jqlQueriesToSanitize, (error, data, response) => {
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
 **jqlQueriesToSanitize** | [**JqlQueriesToSanitize**](JqlQueriesToSanitize.md)|  | 

### Return type

[**SanitizedJqlQueries**](SanitizedJqlQueries.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

