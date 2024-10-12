# OrbitApi.ActivitiesApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugActivitiesGet**](ActivitiesApi.md#workspaceSlugActivitiesGet) | **GET** /{workspace_slug}/activities | List activities for a workspace
[**workspaceSlugActivitiesIdGet**](ActivitiesApi.md#workspaceSlugActivitiesIdGet) | **GET** /{workspace_slug}/activities/{id} | Get an activity in the workspace
[**workspaceSlugActivitiesPost**](ActivitiesApi.md#workspaceSlugActivitiesPost) | **POST** /{workspace_slug}/activities | Create a Custom or a Content activity for a new or existing member
[**workspaceSlugMembersMemberSlugActivitiesGet**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesGet) | **GET** /{workspace_slug}/members/{member_slug}/activities | List activities for a member
[**workspaceSlugMembersMemberSlugActivitiesIdDelete**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesIdDelete) | **DELETE** /{workspace_slug}/members/{member_slug}/activities/{id} | Delete a post activity
[**workspaceSlugMembersMemberSlugActivitiesIdPut**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesIdPut) | **PUT** /{workspace_slug}/members/{member_slug}/activities/{id} | Update a custom activity for a member
[**workspaceSlugMembersMemberSlugActivitiesPost**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesPost) | **POST** /{workspace_slug}/members/{member_slug}/activities | Create a Custom or a Content activity for a member
[**workspaceSlugOrganizationsOrganizationIdActivitiesGet**](ActivitiesApi.md#workspaceSlugOrganizationsOrganizationIdActivitiesGet) | **GET** /{workspace_slug}/organizations/{organization_id}/activities | List member activities in an organization



## workspaceSlugActivitiesGet

> workspaceSlugActivitiesGet(workspaceSlug, opts)

List activities for a workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'affiliation': "affiliation_example", // String | 
  'memberTags': "memberTags_example", // String | The list of tags to filter against. Separate tags with `,` to do an intersection (AND), or with `|` to do a union (OR)
  'orbit': "orbit_example", // String | The list of orbit levels to filter against. Accepted values are 1, 2, 3, 4, n. In the request, a format like `23` would include levels 2 and 3. `n` is for members with no orbit level.
  'activityType': "activityType_example", // String | Comma separated list of activity types
  'identity': "identity_example", // String | 
  'company': "company_example", // String | Comma separated list of companies. The union (OR) of companies is applied.
  'title': "title_example", // String | Comma separated list of job titles. The union (OR) of job titles is applied.
  'regions': "regions_example", // String | Comma separated list of regions. The union (OR) of regions is applied.
  'countries': "countries_example", // String | Comma separated list of countries. The union (OR) of countries is applied.
  'cities': "cities_example", // String | Comma separated list of cities. The union (OR) of cities is applied.
  'startDate': "startDate_example", // String | Filter activities after this date. Format: YYYY-MM-DD.
  'endDate': "endDate_example", // String | Filter activities before this date. Format: YYYY-MM-DD.
  'relative': "relative_example", // String | Relative timeframes. Format: this_<integer>_<period>, with period in [days, weeks, months, years]. For example, this_30_days.
  'page': "page_example", // String | 
  'direction': "direction_example", // String | 
  'items': "items_example", // String | 
  'sort': "sort_example", // String | 
  'type': "type_example" // String | Deprecated in favor of the activity_type parameter.
};
apiInstance.workspaceSlugActivitiesGet(workspaceSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **affiliation** | **String**|  | [optional] 
 **memberTags** | **String**| The list of tags to filter against. Separate tags with &#x60;,&#x60; to do an intersection (AND), or with &#x60;|&#x60; to do a union (OR) | [optional] 
 **orbit** | **String**| The list of orbit levels to filter against. Accepted values are 1, 2, 3, 4, n. In the request, a format like &#x60;23&#x60; would include levels 2 and 3. &#x60;n&#x60; is for members with no orbit level. | [optional] 
 **activityType** | **String**| Comma separated list of activity types | [optional] 
 **identity** | **String**|  | [optional] 
 **company** | **String**| Comma separated list of companies. The union (OR) of companies is applied. | [optional] 
 **title** | **String**| Comma separated list of job titles. The union (OR) of job titles is applied. | [optional] 
 **regions** | **String**| Comma separated list of regions. The union (OR) of regions is applied. | [optional] 
 **countries** | **String**| Comma separated list of countries. The union (OR) of countries is applied. | [optional] 
 **cities** | **String**| Comma separated list of cities. The union (OR) of cities is applied. | [optional] 
 **startDate** | **String**| Filter activities after this date. Format: YYYY-MM-DD. | [optional] 
 **endDate** | **String**| Filter activities before this date. Format: YYYY-MM-DD. | [optional] 
 **relative** | **String**| Relative timeframes. Format: this_&lt;integer&gt;_&lt;period&gt;, with period in [days, weeks, months, years]. For example, this_30_days. | [optional] 
 **page** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 
 **items** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugActivitiesIdGet

> workspaceSlugActivitiesIdGet(workspaceSlug, id)

Get an activity in the workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let id = "id_example"; // String | 
apiInstance.workspaceSlugActivitiesIdGet(workspaceSlug, id, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugActivitiesPost

> workspaceSlugActivitiesPost(workspaceSlug, opts)

Create a Custom or a Content activity for a new or existing member

Use this method when you know an identity of the member (github, email, twitter, etc.) but not their Orbit ID. Pass fields in the member object to update the member in addition to creating the activity.

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'activityAndIdentity': new OrbitApi.ActivityAndIdentity() // ActivityAndIdentity | 
};
apiInstance.workspaceSlugActivitiesPost(workspaceSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **activityAndIdentity** | [**ActivityAndIdentity**](ActivityAndIdentity.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSlugMembersMemberSlugActivitiesGet

> workspaceSlugMembersMemberSlugActivitiesGet(workspaceSlug, memberSlug, opts)

List activities for a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'page': "page_example", // String | 
  'direction': "direction_example", // String | 
  'items': "items_example", // String | 
  'sort': "sort_example", // String | 
  'activityType': "activityType_example", // String | 
  'type': "type_example" // String | Deprecated in favor of the activity_type parameter.
};
apiInstance.workspaceSlugMembersMemberSlugActivitiesGet(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **page** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 
 **items** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **activityType** | **String**|  | [optional] 
 **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugMembersMemberSlugActivitiesIdDelete

> workspaceSlugMembersMemberSlugActivitiesIdDelete(workspaceSlug, memberSlug, id)

Delete a post activity

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let id = "id_example"; // String | 
apiInstance.workspaceSlugMembersMemberSlugActivitiesIdDelete(workspaceSlug, memberSlug, id, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspaceSlugMembersMemberSlugActivitiesIdPut

> workspaceSlugMembersMemberSlugActivitiesIdPut(workspaceSlug, memberSlug, id, opts)

Update a custom activity for a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'activity': new OrbitApi.Activity() // Activity | 
};
apiInstance.workspaceSlugMembersMemberSlugActivitiesIdPut(workspaceSlug, memberSlug, id, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **id** | **String**|  | 
 **activity** | [**Activity**](Activity.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSlugMembersMemberSlugActivitiesPost

> workspaceSlugMembersMemberSlugActivitiesPost(workspaceSlug, memberSlug, opts)

Create a Custom or a Content activity for a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'customOrPostActivity': new OrbitApi.CustomOrPostActivity() // CustomOrPostActivity | 
};
apiInstance.workspaceSlugMembersMemberSlugActivitiesPost(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **customOrPostActivity** | [**CustomOrPostActivity**](CustomOrPostActivity.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSlugOrganizationsOrganizationIdActivitiesGet

> workspaceSlugOrganizationsOrganizationIdActivitiesGet(workspaceSlug, organizationId, opts)

List member activities in an organization

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivitiesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let organizationId = "organizationId_example"; // String | 
let opts = {
  'page': "page_example", // String | 
  'direction': "direction_example", // String | 
  'items': "items_example", // String | 
  'sort': "sort_example", // String | 
  'activityType': "activityType_example" // String | 
};
apiInstance.workspaceSlugOrganizationsOrganizationIdActivitiesGet(workspaceSlug, organizationId, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **organizationId** | **String**|  | 
 **page** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 
 **items** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **activityType** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

