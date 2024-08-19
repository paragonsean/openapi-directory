# MembersApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugMembersFindGet**](MembersApi.md#workspaceSlugMembersFindGet) | **GET** /{workspace_slug}/members/find | Find a member by an identity |
| [**workspaceSlugMembersGet**](MembersApi.md#workspaceSlugMembersGet) | **GET** /{workspace_slug}/members | List members in a workspace |
| [**workspaceSlugMembersMemberSlugDelete**](MembersApi.md#workspaceSlugMembersMemberSlugDelete) | **DELETE** /{workspace_slug}/members/{member_slug} | Delete a member |
| [**workspaceSlugMembersMemberSlugGet**](MembersApi.md#workspaceSlugMembersMemberSlugGet) | **GET** /{workspace_slug}/members/{member_slug} | Get a member |
| [**workspaceSlugMembersMemberSlugIdentitiesDelete**](MembersApi.md#workspaceSlugMembersMemberSlugIdentitiesDelete) | **DELETE** /{workspace_slug}/members/{member_slug}/identities | Remove identity from a member |
| [**workspaceSlugMembersMemberSlugIdentitiesPost**](MembersApi.md#workspaceSlugMembersMemberSlugIdentitiesPost) | **POST** /{workspace_slug}/members/{member_slug}/identities | Add identity to a member |
| [**workspaceSlugMembersMemberSlugPut**](MembersApi.md#workspaceSlugMembersMemberSlugPut) | **PUT** /{workspace_slug}/members/{member_slug} | Update a member |
| [**workspaceSlugMembersPost**](MembersApi.md#workspaceSlugMembersPost) | **POST** /{workspace_slug}/members | Create or update a member |
| [**workspaceSlugOrganizationsOrganizationIdMembersGet**](MembersApi.md#workspaceSlugOrganizationsOrganizationIdMembersGet) | **GET** /{workspace_slug}/organizations/{organization_id}/members | List members in an organization |


<a id="workspaceSlugMembersFindGet"></a>
# **workspaceSlugMembersFindGet**
> workspaceSlugMembersFindGet(workspaceSlug, source, sourceHost, uid, username, email, github)

Find a member by an identity

Provide a source and one of username/uid/email params to return a member with that identity, if one exists. Common values for source include github, twitter, and email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String source = "source_example"; // String | 
    String sourceHost = "sourceHost_example"; // String | 
    String uid = "uid_example"; // String | 
    String username = "username_example"; // String | 
    String email = "email_example"; // String | 
    String github = "github_example"; // String | Deprecated, please use source=github and username=<username> instead
    try {
      apiInstance.workspaceSlugMembersFindGet(workspaceSlug, source, sourceHost, uid, username, email, github);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersFindGet");
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
| **source** | **String**|  | [optional] |
| **sourceHost** | **String**|  | [optional] |
| **uid** | **String**|  | [optional] |
| **username** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **github** | **String**| Deprecated, please use source&#x3D;github and username&#x3D;&lt;username&gt; instead | [optional] |

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
| **404** | Not found |  -  |

<a id="workspaceSlugMembersGet"></a>
# **workspaceSlugMembersGet**
> workspaceSlugMembersGet(workspaceSlug, affiliation, memberTags, orbit, activityType, identity, company, title, regions, countries, cities, startDate, endDate, relative, query, page, direction, items, activitiesCountMin, activitiesCountMax, sort, type)

List members in a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
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
    String query = "query_example"; // String | 
    String page = "page_example"; // String | 
    String direction = "ASC"; // String | 
    String items = "10"; // String | 
    String activitiesCountMin = "activitiesCountMin_example"; // String | 
    String activitiesCountMax = "activitiesCountMax_example"; // String | 
    String sort = "activities_count"; // String | 
    String type = "type_example"; // String | Deprecated in favor of the activity_type parameter.
    try {
      apiInstance.workspaceSlugMembersGet(workspaceSlug, affiliation, memberTags, orbit, activityType, identity, company, title, regions, countries, cities, startDate, endDate, relative, query, page, direction, items, activitiesCountMin, activitiesCountMax, sort, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersGet");
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
| **query** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] [enum: ASC, DESC] |
| **items** | **String**|  | [optional] [enum: 10, 50, 100] |
| **activitiesCountMin** | **String**|  | [optional] |
| **activitiesCountMax** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] [enum: activities_count, company, created_at, first_activity, github_followers, id, last_activity, location, love, name, orbit, reach, title, twitter_followers, updated_at] |
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

<a id="workspaceSlugMembersMemberSlugDelete"></a>
# **workspaceSlugMembersMemberSlugDelete**
> workspaceSlugMembersMemberSlugDelete(workspaceSlug, memberSlug)

Delete a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugDelete(workspaceSlug, memberSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersMemberSlugDelete");
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
| **204** | member deleted |  -  |
| **403** | forbidden |  -  |

<a id="workspaceSlugMembersMemberSlugGet"></a>
# **workspaceSlugMembersMemberSlugGet**
> workspaceSlugMembersMemberSlugGet(workspaceSlug, memberSlug)

Get a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugGet(workspaceSlug, memberSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersMemberSlugGet");
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

<a id="workspaceSlugMembersMemberSlugIdentitiesDelete"></a>
# **workspaceSlugMembersMemberSlugIdentitiesDelete**
> workspaceSlugMembersMemberSlugIdentitiesDelete(workspaceSlug, memberSlug, identity)

Remove identity from a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    Identity identity = new Identity(); // Identity | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugIdentitiesDelete(workspaceSlug, memberSlug, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersMemberSlugIdentitiesDelete");
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
| **identity** | [**Identity**](Identity.md)|  | [optional] |

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
| **204** | identity deleted |  -  |
| **403** | forbidden |  -  |
| **422** | identity is invalid or not attached to member |  -  |

<a id="workspaceSlugMembersMemberSlugIdentitiesPost"></a>
# **workspaceSlugMembersMemberSlugIdentitiesPost**
> workspaceSlugMembersMemberSlugIdentitiesPost(workspaceSlug, memberSlug, identity)

Add identity to a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    Identity identity = new Identity(); // Identity | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugIdentitiesPost(workspaceSlug, memberSlug, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersMemberSlugIdentitiesPost");
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
| **identity** | [**Identity**](Identity.md)|  | [optional] |

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
| **422** | identity is invalid |  -  |

<a id="workspaceSlugMembersMemberSlugPut"></a>
# **workspaceSlugMembersMemberSlugPut**
> workspaceSlugMembersMemberSlugPut(workspaceSlug, memberSlug, member)

Update a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    Member member = new Member(); // Member | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugPut(workspaceSlug, memberSlug, member);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersMemberSlugPut");
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
| **member** | [**Member**](Member.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | member updated |  -  |
| **403** | forbidden |  -  |

<a id="workspaceSlugMembersPost"></a>
# **workspaceSlugMembersPost**
> workspaceSlugMembersPost(workspaceSlug, memberAndIdentity)

Create or update a member

This method is useful when you know a member&#39;s identity in another system and want to create or update the corresponding Orbit member. Identities can be specified in the identity object or member attributes like member.github. If no member exists, a new member will be created and linked to any provided identities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    MemberAndIdentity memberAndIdentity = new MemberAndIdentity(); // MemberAndIdentity | 
    try {
      apiInstance.workspaceSlugMembersPost(workspaceSlug, memberAndIdentity);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugMembersPost");
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
| **memberAndIdentity** | [**MemberAndIdentity**](MemberAndIdentity.md)|  | [optional] |

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
| **200** | success |  -  |
| **201** | created |  -  |
| **403** | forbidden |  -  |
| **422** | unprocessable |  -  |

<a id="workspaceSlugOrganizationsOrganizationIdMembersGet"></a>
# **workspaceSlugOrganizationsOrganizationIdMembersGet**
> workspaceSlugOrganizationsOrganizationIdMembersGet(workspaceSlug, organizationId, page, items)

List members in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String organizationId = "organizationId_example"; // String | 
    String page = "page_example"; // String | 
    String items = "10"; // String | 
    try {
      apiInstance.workspaceSlugOrganizationsOrganizationIdMembersGet(workspaceSlug, organizationId, page, items);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#workspaceSlugOrganizationsOrganizationIdMembersGet");
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
| **items** | **String**|  | [optional] [enum: 10, 50, 100] |

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

