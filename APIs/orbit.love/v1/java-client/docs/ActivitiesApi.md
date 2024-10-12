# ActivitiesApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugActivitiesGet**](ActivitiesApi.md#workspaceSlugActivitiesGet) | **GET** /{workspace_slug}/activities | List activities for a workspace |
| [**workspaceSlugActivitiesIdGet**](ActivitiesApi.md#workspaceSlugActivitiesIdGet) | **GET** /{workspace_slug}/activities/{id} | Get an activity in the workspace |
| [**workspaceSlugActivitiesPost**](ActivitiesApi.md#workspaceSlugActivitiesPost) | **POST** /{workspace_slug}/activities | Create a Custom or a Content activity for a new or existing member |
| [**workspaceSlugMembersMemberSlugActivitiesGet**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesGet) | **GET** /{workspace_slug}/members/{member_slug}/activities | List activities for a member |
| [**workspaceSlugMembersMemberSlugActivitiesIdDelete**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesIdDelete) | **DELETE** /{workspace_slug}/members/{member_slug}/activities/{id} | Delete a post activity |
| [**workspaceSlugMembersMemberSlugActivitiesIdPut**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesIdPut) | **PUT** /{workspace_slug}/members/{member_slug}/activities/{id} | Update a custom activity for a member |
| [**workspaceSlugMembersMemberSlugActivitiesPost**](ActivitiesApi.md#workspaceSlugMembersMemberSlugActivitiesPost) | **POST** /{workspace_slug}/members/{member_slug}/activities | Create a Custom or a Content activity for a member |
| [**workspaceSlugOrganizationsOrganizationIdActivitiesGet**](ActivitiesApi.md#workspaceSlugOrganizationsOrganizationIdActivitiesGet) | **GET** /{workspace_slug}/organizations/{organization_id}/activities | List member activities in an organization |


<a id="workspaceSlugActivitiesGet"></a>
# **workspaceSlugActivitiesGet**
> workspaceSlugActivitiesGet(workspaceSlug, affiliation, memberTags, orbit, activityType, identity, company, title, regions, countries, cities, startDate, endDate, relative, page, direction, items, sort, type)

List activities for a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String affiliation = "member"; // String | 
    String memberTags = "memberTags_example"; // String | The list of tags to filter against. Separate tags with `,` to do an intersection (AND), or with `|` to do a union (OR)
    String orbit = "orbit_example"; // String | The list of orbit levels to filter against. Accepted values are 1, 2, 3, 4, n. In the request, a format like `23` would include levels 2 and 3. `n` is for members with no orbit level.
    String activityType = "discourse:topic:created"; // String | Comma separated list of activity types
    String identity = "github"; // String | 
    String company = "company_example"; // String | Comma separated list of companies. The union (OR) of companies is applied.
    String title = "title_example"; // String | Comma separated list of job titles. The union (OR) of job titles is applied.
    String regions = "regions_example"; // String | Comma separated list of regions. The union (OR) of regions is applied.
    String countries = "countries_example"; // String | Comma separated list of countries. The union (OR) of countries is applied.
    String cities = "cities_example"; // String | Comma separated list of cities. The union (OR) of cities is applied.
    String startDate = "startDate_example"; // String | Filter activities after this date. Format: YYYY-MM-DD.
    String endDate = "endDate_example"; // String | Filter activities before this date. Format: YYYY-MM-DD.
    String relative = "relative_example"; // String | Relative timeframes. Format: this_<integer>_<period>, with period in [days, weeks, months, years]. For example, this_30_days.
    String page = "page_example"; // String | 
    String direction = "ASC"; // String | 
    String items = "10"; // String | 
    String sort = "occurred_at"; // String | 
    String type = "type_example"; // String | Deprecated in favor of the activity_type parameter.
    try {
      apiInstance.workspaceSlugActivitiesGet(workspaceSlug, affiliation, memberTags, orbit, activityType, identity, company, title, regions, countries, cities, startDate, endDate, relative, page, direction, items, sort, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugActivitiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **affiliation** | **String**|  | [optional] [enum: member, teammate] |
| **memberTags** | **String**| The list of tags to filter against. Separate tags with &#x60;,&#x60; to do an intersection (AND), or with &#x60;|&#x60; to do a union (OR) | [optional] |
| **orbit** | **String**| The list of orbit levels to filter against. Accepted values are 1, 2, 3, 4, n. In the request, a format like &#x60;23&#x60; would include levels 2 and 3. &#x60;n&#x60; is for members with no orbit level. | [optional] |
| **activityType** | **String**| Comma separated list of activity types | [optional] [enum: discourse:topic:created, discourse:post:liked, discourse:user:created, discourse:post:created, slack:message:sent, slack:thread:replied, slack:channel:joined, note:created, post:created, issues:opened, discord:message:sent, issue_comment:created, discord:thread:replied, custom:happened, dev:comment, discord:message:replied, discord:server:joined, insided:conversation:started, fork:created, insided:idea:replied, insided:article:created, discussions:discussion_created, insided:question:replied, discussions:comment, discussions:reply, insided:article:replied, insided:question:asked, insided:conversation:replied, insided:idea:submitted, reddit:comment, reddit:post, stackoverflow:answer, linkedin:comment, pull_requests:opened, pull_requests:merged, star:created, stackoverflow:question, tweet:sent, twitter:followed, youtube:comment] |
| **identity** | **String**|  | [optional] [enum: github, twitter, email, discourse, linkedin, devto, slack, discord] |
| **company** | **String**| Comma separated list of companies. The union (OR) of companies is applied. | [optional] |
| **title** | **String**| Comma separated list of job titles. The union (OR) of job titles is applied. | [optional] |
| **regions** | **String**| Comma separated list of regions. The union (OR) of regions is applied. | [optional] |
| **countries** | **String**| Comma separated list of countries. The union (OR) of countries is applied. | [optional] |
| **cities** | **String**| Comma separated list of cities. The union (OR) of cities is applied. | [optional] |
| **startDate** | **String**| Filter activities after this date. Format: YYYY-MM-DD. | [optional] |
| **endDate** | **String**| Filter activities before this date. Format: YYYY-MM-DD. | [optional] |
| **relative** | **String**| Relative timeframes. Format: this_&lt;integer&gt;_&lt;period&gt;, with period in [days, weeks, months, years]. For example, this_30_days. | [optional] |
| **page** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] [enum: ASC, DESC] |
| **items** | **String**|  | [optional] [enum: 10, 50, 100] |
| **sort** | **String**|  | [optional] [enum: occurred_at, member] |
| **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugActivitiesIdGet"></a>
# **workspaceSlugActivitiesIdGet**
> workspaceSlugActivitiesIdGet(workspaceSlug, id)

Get an activity in the workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.workspaceSlugActivitiesIdGet(workspaceSlug, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugActivitiesIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugActivitiesPost"></a>
# **workspaceSlugActivitiesPost**
> workspaceSlugActivitiesPost(workspaceSlug, activityAndIdentity)

Create a Custom or a Content activity for a new or existing member

Use this method when you know an identity of the member (github, email, twitter, etc.) but not their Orbit ID. Pass fields in the member object to update the member in addition to creating the activity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    ActivityAndIdentity activityAndIdentity = new ActivityAndIdentity(); // ActivityAndIdentity | 
    try {
      apiInstance.workspaceSlugActivitiesPost(workspaceSlug, activityAndIdentity);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugActivitiesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **activityAndIdentity** | [**ActivityAndIdentity**](ActivityAndIdentity.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | success |  -  |
| **403** | forbidden |  -  |
| **422** | unprocessable |  -  |

<a id="workspaceSlugMembersMemberSlugActivitiesGet"></a>
# **workspaceSlugMembersMemberSlugActivitiesGet**
> workspaceSlugMembersMemberSlugActivitiesGet(workspaceSlug, memberSlug, page, direction, items, sort, activityType, type)

List activities for a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    String page = "page_example"; // String | 
    String direction = "ASC"; // String | 
    String items = "10"; // String | 
    String sort = "occurred_at"; // String | 
    String activityType = "activityType_example"; // String | 
    String type = "type_example"; // String | Deprecated in favor of the activity_type parameter.
    try {
      apiInstance.workspaceSlugMembersMemberSlugActivitiesGet(workspaceSlug, memberSlug, page, direction, items, sort, activityType, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugMembersMemberSlugActivitiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **page** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] [enum: ASC, DESC] |
| **items** | **String**|  | [optional] [enum: 10, 50, 100] |
| **sort** | **String**|  | [optional] [enum: occurred_at, member] |
| **activityType** | **String**|  | [optional] |
| **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugMembersMemberSlugActivitiesIdDelete"></a>
# **workspaceSlugMembersMemberSlugActivitiesIdDelete**
> workspaceSlugMembersMemberSlugActivitiesIdDelete(workspaceSlug, memberSlug, id)

Delete a post activity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugActivitiesIdDelete(workspaceSlug, memberSlug, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugMembersMemberSlugActivitiesIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | activity deleted |  -  |
| **403** | forbidden |  -  |

<a id="workspaceSlugMembersMemberSlugActivitiesIdPut"></a>
# **workspaceSlugMembersMemberSlugActivitiesIdPut**
> workspaceSlugMembersMemberSlugActivitiesIdPut(workspaceSlug, memberSlug, id, activity)

Update a custom activity for a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    String id = "id_example"; // String | 
    Activity activity = new Activity(); // Activity | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugActivitiesIdPut(workspaceSlug, memberSlug, id, activity);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugMembersMemberSlugActivitiesIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **id** | **String**|  | |
| **activity** | [**Activity**](Activity.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | activity updated |  -  |
| **403** | forbidden |  -  |
| **422** | unprocessable entity |  -  |

<a id="workspaceSlugMembersMemberSlugActivitiesPost"></a>
# **workspaceSlugMembersMemberSlugActivitiesPost**
> workspaceSlugMembersMemberSlugActivitiesPost(workspaceSlug, memberSlug, customOrPostActivity)

Create a Custom or a Content activity for a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    CustomOrPostActivity customOrPostActivity = new CustomOrPostActivity(); // CustomOrPostActivity | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugActivitiesPost(workspaceSlug, memberSlug, customOrPostActivity);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugMembersMemberSlugActivitiesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **customOrPostActivity** | [**CustomOrPostActivity**](CustomOrPostActivity.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | success |  -  |
| **403** | forbidden |  -  |
| **422** | unprocessable entity |  -  |

<a id="workspaceSlugOrganizationsOrganizationIdActivitiesGet"></a>
# **workspaceSlugOrganizationsOrganizationIdActivitiesGet**
> workspaceSlugOrganizationsOrganizationIdActivitiesGet(workspaceSlug, organizationId, page, direction, items, sort, activityType)

List member activities in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String organizationId = "organizationId_example"; // String | 
    String page = "page_example"; // String | 
    String direction = "ASC"; // String | 
    String items = "10"; // String | 
    String sort = "occurred_at"; // String | 
    String activityType = "content"; // String | 
    try {
      apiInstance.workspaceSlugOrganizationsOrganizationIdActivitiesGet(workspaceSlug, organizationId, page, direction, items, sort, activityType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#workspaceSlugOrganizationsOrganizationIdActivitiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceSlug** | **String**|  | |
| **organizationId** | **String**|  | |
| **page** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] [enum: ASC, DESC] |
| **items** | **String**|  | [optional] [enum: 10, 50, 100] |
| **sort** | **String**|  | [optional] [enum: occurred_at, member] |
| **activityType** | **String**|  | [optional] [enum: content, custom, discord, discourse, github, slack, twitter] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

