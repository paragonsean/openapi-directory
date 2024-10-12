# FigshareApi.InstitutionsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountInstitutionCuration**](InstitutionsApi.md#accountInstitutionCuration) | **GET** /account/institution/review/{curation_id} | Institution Curation Review
[**accountInstitutionCurationComments**](InstitutionsApi.md#accountInstitutionCurationComments) | **GET** /account/institution/review/{curation_id}/comments | Institution Curation Review Comments
[**accountInstitutionCurations**](InstitutionsApi.md#accountInstitutionCurations) | **GET** /account/institution/reviews | Institution Curation Reviews
[**accountInstitutionReviewCurationIdCommentsPost**](InstitutionsApi.md#accountInstitutionReviewCurationIdCommentsPost) | **POST** /account/institution/review/{curation_id}/comments | POST Institution Curation Review Comment
[**customFieldsList**](InstitutionsApi.md#customFieldsList) | **GET** /account/institution/custom_fields | Private account institution group custom fields
[**customFieldsUpload**](InstitutionsApi.md#customFieldsUpload) | **POST** /account/institution/custom_fields/{custom_field_id}/items/upload | Custom fields values files upload
[**institutionArticles**](InstitutionsApi.md#institutionArticles) | **GET** /institutions/{institution_string_id}/articles/filter-by | Public Licenses
[**institutionHrfeedUpload**](InstitutionsApi.md#institutionHrfeedUpload) | **POST** /institution/hrfeed/upload | Private Institution HRfeed Upload
[**privateAccountInstitutionUser**](InstitutionsApi.md#privateAccountInstitutionUser) | **GET** /account/institution/users/{account_id} | Private Account Institution User
[**privateCategoriesList**](InstitutionsApi.md#privateCategoriesList) | **GET** /account/categories | Private Account Categories
[**privateGroupEmbargoOptionsDetails**](InstitutionsApi.md#privateGroupEmbargoOptionsDetails) | **GET** /account/institution/groups/{group_id}/embargo_options | Private Account Institution Group Embargo Options
[**privateInstitutionAccountGroupRoleDelete**](InstitutionsApi.md#privateInstitutionAccountGroupRoleDelete) | **DELETE** /account/institution/roles/{account_id}/{group_id}/{role_id} | Delete Institution Account Group Role
[**privateInstitutionAccountGroupRoles**](InstitutionsApi.md#privateInstitutionAccountGroupRoles) | **GET** /account/institution/roles/{account_id} | List Institution Account Group Roles
[**privateInstitutionAccountGroupRolesCreate**](InstitutionsApi.md#privateInstitutionAccountGroupRolesCreate) | **POST** /account/institution/roles/{account_id} | Add Institution Account Group Roles
[**privateInstitutionAccountsCreate**](InstitutionsApi.md#privateInstitutionAccountsCreate) | **POST** /account/institution/accounts | Create new Institution Account
[**privateInstitutionAccountsList**](InstitutionsApi.md#privateInstitutionAccountsList) | **GET** /account/institution/accounts | Private Account Institution Accounts
[**privateInstitutionAccountsSearch**](InstitutionsApi.md#privateInstitutionAccountsSearch) | **POST** /account/institution/accounts/search | Private Account Institution Accounts Search
[**privateInstitutionAccountsUpdate**](InstitutionsApi.md#privateInstitutionAccountsUpdate) | **PUT** /account/institution/accounts/{account_id} | Update Institution Account
[**privateInstitutionArticles**](InstitutionsApi.md#privateInstitutionArticles) | **GET** /account/institution/articles | Private Institution Articles
[**privateInstitutionDetails**](InstitutionsApi.md#privateInstitutionDetails) | **GET** /account/institution | Private Account Institutions
[**privateInstitutionEmbargoOptionsDetails**](InstitutionsApi.md#privateInstitutionEmbargoOptionsDetails) | **GET** /account/institution/embargo_options | Private Account Institution embargo options
[**privateInstitutionGroupsList**](InstitutionsApi.md#privateInstitutionGroupsList) | **GET** /account/institution/groups | Private Account Institution Groups
[**privateInstitutionRolesList**](InstitutionsApi.md#privateInstitutionRolesList) | **GET** /account/institution/roles | Private Account Institution Roles



## accountInstitutionCuration

> CurationDetail accountInstitutionCuration(curationId)

Institution Curation Review

Retrieve a certain curation review by its ID

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let curationId = 789; // Number | ID of the curation
apiInstance.accountInstitutionCuration(curationId, (error, data, response) => {
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
 **curationId** | **Number**| ID of the curation | 

### Return type

[**CurationDetail**](CurationDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountInstitutionCurationComments

> CurationComment accountInstitutionCurationComments(curationId, opts)

Institution Curation Review Comments

Retrieve a certain curation review&#39;s comments.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let curationId = 789; // Number | ID of the curation
let opts = {
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.accountInstitutionCurationComments(curationId, opts, (error, data, response) => {
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
 **curationId** | **Number**| ID of the curation | 
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**CurationComment**](CurationComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountInstitutionCurations

> Curation accountInstitutionCurations(opts)

Institution Curation Reviews

Retrieve a list of curation reviews for this institution

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let opts = {
  'groupId': 789, // Number | Filter by the group ID
  'articleId': 789, // Number | Retrieve the reviews for this article
  'status': "status_example", // String | Filter by the status of the review
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.accountInstitutionCurations(opts, (error, data, response) => {
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
 **groupId** | **Number**| Filter by the group ID | [optional] 
 **articleId** | **Number**| Retrieve the reviews for this article | [optional] 
 **status** | **String**| Filter by the status of the review | [optional] 
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**Curation**](Curation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountInstitutionReviewCurationIdCommentsPost

> accountInstitutionReviewCurationIdCommentsPost(curationId, curationCommentCreate)

POST Institution Curation Review Comment

Add a new comment to the review.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let curationId = 789; // Number | ID of the curation
let curationCommentCreate = new FigshareApi.CurationCommentCreate(); // CurationCommentCreate | The content/value of the comment.
apiInstance.accountInstitutionReviewCurationIdCommentsPost(curationId, curationCommentCreate, (error, data, response) => {
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
 **curationId** | **Number**| ID of the curation | 
 **curationCommentCreate** | [**CurationCommentCreate**](CurationCommentCreate.md)| The content/value of the comment. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customFieldsList

> [ShortCustomField] customFieldsList(opts)

Private account institution group custom fields

Returns the custom fields in the group the user belongs to, or the ones in the group specified, if the user has access.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let opts = {
  'groupId': 789 // Number | Group_id
};
apiInstance.customFieldsList(opts, (error, data, response) => {
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
 **groupId** | **Number**| Group_id | [optional] 

### Return type

[**[ShortCustomField]**](ShortCustomField.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsUpload

> Object customFieldsUpload(customFieldId, opts)

Custom fields values files upload

Uploads a CSV containing values for a specific custom field of type &lt;b&gt;dropdown_large_list&lt;/b&gt;. More details in the &lt;a href&#x3D;\&quot;#custom_fields\&quot;&gt;Custom Fields section&lt;/a&gt;

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let customFieldId = 789; // Number | Custom field identifier
let opts = {
  'externalFile': "/path/to/file" // File | CSV file to be uploaded
};
apiInstance.customFieldsUpload(customFieldId, opts, (error, data, response) => {
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
 **customFieldId** | **Number**| Custom field identifier | 
 **externalFile** | **File**| CSV file to be uploaded | [optional] 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## institutionArticles

> [Article] institutionArticles(institutionStringId, resourceId, filename)

Public Licenses

Returns a list of articles belonging to the institution

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.InstitutionsApi();
let institutionStringId = "institutionStringId_example"; // String | 
let resourceId = "resourceId_example"; // String | 
let filename = "filename_example"; // String | 
apiInstance.institutionArticles(institutionStringId, resourceId, filename, (error, data, response) => {
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
 **institutionStringId** | **String**|  | 
 **resourceId** | **String**|  | 
 **filename** | **String**|  | 

### Return type

[**[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## institutionHrfeedUpload

> ResponseMessage institutionHrfeedUpload(opts)

Private Institution HRfeed Upload

More info in the &lt;a href&#x3D;\&quot;#hr_feed\&quot;&gt;HR Feed section&lt;/a&gt;

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let opts = {
  'hrfeed': "/path/to/file" // File | You can find an example in the Hr Feed section
};
apiInstance.institutionHrfeedUpload(opts, (error, data, response) => {
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
 **hrfeed** | **File**| You can find an example in the Hr Feed section | [optional] 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## privateAccountInstitutionUser

> User privateAccountInstitutionUser(accountId)

Private Account Institution User

Retrieve institution user information using the account_id

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let accountId = 789; // Number | Account identifier the user is associated to
apiInstance.privateAccountInstitutionUser(accountId, (error, data, response) => {
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
 **accountId** | **Number**| Account identifier the user is associated to | 

### Return type

[**User**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCategoriesList

> [Category] privateCategoriesList()

Private Account Categories

List institution categories (including parent Categories)

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
apiInstance.privateCategoriesList((error, data, response) => {
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

[**[Category]**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateGroupEmbargoOptionsDetails

> [GroupEmbargoOptions] privateGroupEmbargoOptionsDetails(groupId)

Private Account Institution Group Embargo Options

Account institution group embargo options details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let groupId = 789; // Number | Group identifier
apiInstance.privateGroupEmbargoOptionsDetails(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Group identifier | 

### Return type

[**[GroupEmbargoOptions]**](GroupEmbargoOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionAccountGroupRoleDelete

> privateInstitutionAccountGroupRoleDelete(accountId, groupId, roleId)

Delete Institution Account Group Role

Delete Institution Account Group Role

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let accountId = 789; // Number | Account identifier for which to remove the role
let groupId = 789; // Number | Group identifier for which to remove the role
let roleId = 789; // Number | Role identifier
apiInstance.privateInstitutionAccountGroupRoleDelete(accountId, groupId, roleId, (error, data, response) => {
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
 **accountId** | **Number**| Account identifier for which to remove the role | 
 **groupId** | **Number**| Group identifier for which to remove the role | 
 **roleId** | **Number**| Role identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionAccountGroupRoles

> Object privateInstitutionAccountGroupRoles(accountId)

List Institution Account Group Roles

List Institution Account Group Roles

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let accountId = 789; // Number | Account identifier the user is associated to
apiInstance.privateInstitutionAccountGroupRoles(accountId, (error, data, response) => {
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
 **accountId** | **Number**| Account identifier the user is associated to | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionAccountGroupRolesCreate

> privateInstitutionAccountGroupRolesCreate(accountId, body)

Add Institution Account Group Roles

Add Institution Account Group Roles

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let accountId = 789; // Number | Account identifier the user is associated to
let body = {key: null}; // Object | Account description
apiInstance.privateInstitutionAccountGroupRolesCreate(accountId, body, (error, data, response) => {
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
 **accountId** | **Number**| Account identifier the user is associated to | 
 **body** | **Object**| Account description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateInstitutionAccountsCreate

> privateInstitutionAccountsCreate(accountCreate)

Create new Institution Account

Create a new Account by sending account information

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let accountCreate = new FigshareApi.AccountCreate(); // AccountCreate | Account description
apiInstance.privateInstitutionAccountsCreate(accountCreate, (error, data, response) => {
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
 **accountCreate** | [**AccountCreate**](AccountCreate.md)| Account description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateInstitutionAccountsList

> [ShortAccount] privateInstitutionAccountsList(opts)

Private Account Institution Accounts

Returns the accounts for which the account has administrative privileges (assigned and inherited).

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'isActive': 789, // Number | Filter by active status
  'institutionUserId': "institutionUserId_example", // String | Filter by institution_user_id
  'email': "email_example", // String | Filter by email
  'idLte': 789, // Number | Retrieve accounts with an ID lower or equal to the specified value
  'idGte': 789 // Number | Retrieve accounts with an ID greater or equal to the specified value
};
apiInstance.privateInstitutionAccountsList(opts, (error, data, response) => {
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
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **isActive** | **Number**| Filter by active status | [optional] 
 **institutionUserId** | **String**| Filter by institution_user_id | [optional] 
 **email** | **String**| Filter by email | [optional] 
 **idLte** | **Number**| Retrieve accounts with an ID lower or equal to the specified value | [optional] 
 **idGte** | **Number**| Retrieve accounts with an ID greater or equal to the specified value | [optional] 

### Return type

[**[ShortAccount]**](ShortAccount.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionAccountsSearch

> [ShortAccount] privateInstitutionAccountsSearch(institutionAccountsSearch)

Private Account Institution Accounts Search

Returns the accounts for which the account has administrative privileges (assigned and inherited).

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let institutionAccountsSearch = new FigshareApi.InstitutionAccountsSearch(); // InstitutionAccountsSearch | Search Parameters
apiInstance.privateInstitutionAccountsSearch(institutionAccountsSearch, (error, data, response) => {
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
 **institutionAccountsSearch** | [**InstitutionAccountsSearch**](InstitutionAccountsSearch.md)| Search Parameters | 

### Return type

[**[ShortAccount]**](ShortAccount.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateInstitutionAccountsUpdate

> privateInstitutionAccountsUpdate(accountId, accountUpdate)

Update Institution Account

Update Institution Account

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let accountId = 789; // Number | Account identifier the user is associated to
let accountUpdate = new FigshareApi.AccountUpdate(); // AccountUpdate | Account description
apiInstance.privateInstitutionAccountsUpdate(accountId, accountUpdate, (error, data, response) => {
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
 **accountId** | **Number**| Account identifier the user is associated to | 
 **accountUpdate** | [**AccountUpdate**](AccountUpdate.md)| Account description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateInstitutionArticles

> [Article] privateInstitutionArticles(opts)

Private Institution Articles

Get Articles from own institution. User must be administrator of the institution

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'order': "'published_date'", // String | The field by which to order. Default varies by endpoint/resource.
  'orderDirection': "'desc'", // String | 
  'publishedSince': "publishedSince_example", // String | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
  'modifiedSince': "modifiedSince_example", // String | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
  'status': 789, // Number | only return collections with this status
  'resourceDoi': "resourceDoi_example", // String | only return collections with this resource_doi
  'itemType': 789 // Number | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model
};
apiInstance.privateInstitutionArticles(opts, (error, data, response) => {
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
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to &#39;published_date&#39;]
 **orderDirection** | **String**|  | [optional] [default to &#39;desc&#39;]
 **publishedSince** | **String**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **modifiedSince** | **String**| Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **status** | **Number**| only return collections with this status | [optional] 
 **resourceDoi** | **String**| only return collections with this resource_doi | [optional] 
 **itemType** | **Number**| Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] 

### Return type

[**[Article]**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionDetails

> Institution privateInstitutionDetails()

Private Account Institutions

Account institution details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
apiInstance.privateInstitutionDetails((error, data, response) => {
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

[**Institution**](Institution.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionEmbargoOptionsDetails

> [GroupEmbargoOptions] privateInstitutionEmbargoOptionsDetails()

Private Account Institution embargo options

Account institution embargo options details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
apiInstance.privateInstitutionEmbargoOptionsDetails((error, data, response) => {
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

[**[GroupEmbargoOptions]**](GroupEmbargoOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionGroupsList

> [Group] privateInstitutionGroupsList()

Private Account Institution Groups

Returns the groups for which the account has administrative privileges (assigned and inherited).

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
apiInstance.privateInstitutionGroupsList((error, data, response) => {
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

[**[Group]**](Group.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateInstitutionRolesList

> [Role] privateInstitutionRolesList()

Private Account Institution Roles

Returns the roles available for groups and the institution group.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.InstitutionsApi();
apiInstance.privateInstitutionRolesList((error, data, response) => {
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

[**[Role]**](Role.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

