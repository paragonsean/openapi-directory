# OrbitApi.MembersApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugMembersFindGet**](MembersApi.md#workspaceSlugMembersFindGet) | **GET** /{workspace_slug}/members/find | Find a member by an identity
[**workspaceSlugMembersGet**](MembersApi.md#workspaceSlugMembersGet) | **GET** /{workspace_slug}/members | List members in a workspace
[**workspaceSlugMembersMemberSlugDelete**](MembersApi.md#workspaceSlugMembersMemberSlugDelete) | **DELETE** /{workspace_slug}/members/{member_slug} | Delete a member
[**workspaceSlugMembersMemberSlugGet**](MembersApi.md#workspaceSlugMembersMemberSlugGet) | **GET** /{workspace_slug}/members/{member_slug} | Get a member
[**workspaceSlugMembersMemberSlugIdentitiesDelete**](MembersApi.md#workspaceSlugMembersMemberSlugIdentitiesDelete) | **DELETE** /{workspace_slug}/members/{member_slug}/identities | Remove identity from a member
[**workspaceSlugMembersMemberSlugIdentitiesPost**](MembersApi.md#workspaceSlugMembersMemberSlugIdentitiesPost) | **POST** /{workspace_slug}/members/{member_slug}/identities | Add identity to a member
[**workspaceSlugMembersMemberSlugPut**](MembersApi.md#workspaceSlugMembersMemberSlugPut) | **PUT** /{workspace_slug}/members/{member_slug} | Update a member
[**workspaceSlugMembersPost**](MembersApi.md#workspaceSlugMembersPost) | **POST** /{workspace_slug}/members | Create or update a member
[**workspaceSlugOrganizationsOrganizationIdMembersGet**](MembersApi.md#workspaceSlugOrganizationsOrganizationIdMembersGet) | **GET** /{workspace_slug}/organizations/{organization_id}/members | List members in an organization



## workspaceSlugMembersFindGet

> workspaceSlugMembersFindGet(workspaceSlug, opts)

Find a member by an identity

Provide a source and one of username/uid/email params to return a member with that identity, if one exists. Common values for source include github, twitter, and email.

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'source': "source_example", // String | 
  'sourceHost': "sourceHost_example", // String | 
  'uid': "uid_example", // String | 
  'username': "username_example", // String | 
  'email': "email_example", // String | 
  'github': "github_example" // String | Deprecated, please use source=github and username=<username> instead
};
apiInstance.workspaceSlugMembersFindGet(workspaceSlug, opts, (error, data, response) => {
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
 **source** | **String**|  | [optional] 
 **sourceHost** | **String**|  | [optional] 
 **uid** | **String**|  | [optional] 
 **username** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **github** | **String**| Deprecated, please use source&#x3D;github and username&#x3D;&lt;username&gt; instead | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugMembersGet

> workspaceSlugMembersGet(workspaceSlug, opts)

List members in a workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
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
  'query': "query_example", // String | 
  'page': "page_example", // String | 
  'direction': "direction_example", // String | 
  'items': "items_example", // String | 
  'activitiesCountMin': "activitiesCountMin_example", // String | 
  'activitiesCountMax': "activitiesCountMax_example", // String | 
  'sort': "sort_example", // String | 
  'type': "type_example" // String | Deprecated in favor of the activity_type parameter.
};
apiInstance.workspaceSlugMembersGet(workspaceSlug, opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 
 **items** | **String**|  | [optional] 
 **activitiesCountMin** | **String**|  | [optional] 
 **activitiesCountMax** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugMembersMemberSlugDelete

> workspaceSlugMembersMemberSlugDelete(workspaceSlug, memberSlug)

Delete a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
apiInstance.workspaceSlugMembersMemberSlugDelete(workspaceSlug, memberSlug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspaceSlugMembersMemberSlugGet

> workspaceSlugMembersMemberSlugGet(workspaceSlug, memberSlug)

Get a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
apiInstance.workspaceSlugMembersMemberSlugGet(workspaceSlug, memberSlug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugMembersMemberSlugIdentitiesDelete

> workspaceSlugMembersMemberSlugIdentitiesDelete(workspaceSlug, memberSlug, opts)

Remove identity from a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'identity': new OrbitApi.Identity() // Identity | 
};
apiInstance.workspaceSlugMembersMemberSlugIdentitiesDelete(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **identity** | [**Identity**](Identity.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSlugMembersMemberSlugIdentitiesPost

> workspaceSlugMembersMemberSlugIdentitiesPost(workspaceSlug, memberSlug, opts)

Add identity to a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'identity': new OrbitApi.Identity() // Identity | 
};
apiInstance.workspaceSlugMembersMemberSlugIdentitiesPost(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **identity** | [**Identity**](Identity.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSlugMembersMemberSlugPut

> workspaceSlugMembersMemberSlugPut(workspaceSlug, memberSlug, opts)

Update a member

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'member': new OrbitApi.Member() // Member | 
};
apiInstance.workspaceSlugMembersMemberSlugPut(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **member** | [**Member**](Member.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## workspaceSlugMembersPost

> workspaceSlugMembersPost(workspaceSlug, opts)

Create or update a member

This method is useful when you know a member&#39;s identity in another system and want to create or update the corresponding Orbit member. Identities can be specified in the identity object or member attributes like member.github. If no member exists, a new member will be created and linked to any provided identities.

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'memberAndIdentity': new OrbitApi.MemberAndIdentity() // MemberAndIdentity | 
};
apiInstance.workspaceSlugMembersPost(workspaceSlug, opts, (error, data, response) => {
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
 **memberAndIdentity** | [**MemberAndIdentity**](MemberAndIdentity.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSlugOrganizationsOrganizationIdMembersGet

> workspaceSlugOrganizationsOrganizationIdMembersGet(workspaceSlug, organizationId, opts)

List members in an organization

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.MembersApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let organizationId = "organizationId_example"; // String | 
let opts = {
  'page': "page_example", // String | 
  'items': "items_example" // String | 
};
apiInstance.workspaceSlugOrganizationsOrganizationIdMembersGet(workspaceSlug, organizationId, opts, (error, data, response) => {
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
 **items** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

