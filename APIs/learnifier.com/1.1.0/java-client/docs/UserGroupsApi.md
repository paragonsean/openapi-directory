# UserGroupsApi

All URIs are relative to *http://learnifier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orgunitsOrgidUsergroupsGet**](UserGroupsApi.md#orgunitsOrgidUsergroupsGet) | **GET** /orgunits/{orgid}/usergroups | List User Groups. |
| [**orgunitsOrgidUsergroupsGroupidGet**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidGet) | **GET** /orgunits/{orgid}/usergroups/{groupid} | Get user group |
| [**orgunitsOrgidUsergroupsGroupidMembersGet**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidMembersGet) | **GET** /orgunits/{orgid}/usergroups/{groupid}/members | List of all users in group. |
| [**orgunitsOrgidUsergroupsGroupidMembersPost**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidMembersPost) | **POST** /orgunits/{orgid}/usergroups/{groupid}/members | Add user group member. |
| [**orgunitsOrgidUsergroupsGroupidMembersUuidDelete**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidMembersUuidDelete) | **DELETE** /orgunits/{orgid}/usergroups/{groupid}/members/{uuid} | Remove user group member. |
| [**orgunitsOrgidUsergroupsPost**](UserGroupsApi.md#orgunitsOrgidUsergroupsPost) | **POST** /orgunits/{orgid}/usergroups | Create a User Group. |


<a id="orgunitsOrgidUsergroupsGet"></a>
# **orgunitsOrgidUsergroupsGet**
> List&lt;UserGroup&gt; orgunitsOrgidUsergroupsGet(orgid)

List User Groups.

Returns a list of User Groups for the org unit. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UserGroupsApi apiInstance = new UserGroupsApi(defaultClient);
    Long orgid = 56L; // Long | ID of organization
    try {
      List<UserGroup> result = apiInstance.orgunitsOrgidUsergroupsGet(orgid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserGroupsApi#orgunitsOrgidUsergroupsGet");
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
| **orgid** | **Long**| ID of organization | |

### Return type

[**List&lt;UserGroup&gt;**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of User Groups. |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidUsergroupsGroupidGet"></a>
# **orgunitsOrgidUsergroupsGroupidGet**
> UserGroup orgunitsOrgidUsergroupsGroupidGet(orgid, groupid)

Get user group

Returns single User Group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UserGroupsApi apiInstance = new UserGroupsApi(defaultClient);
    Long orgid = 56L; // Long | ID of organization
    Long groupid = 56L; // Long | ID of group
    try {
      UserGroup result = apiInstance.orgunitsOrgidUsergroupsGroupidGet(orgid, groupid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserGroupsApi#orgunitsOrgidUsergroupsGroupidGet");
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
| **orgid** | **Long**| ID of organization | |
| **groupid** | **Long**| ID of group | |

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Group. |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidUsergroupsGroupidMembersGet"></a>
# **orgunitsOrgidUsergroupsGroupidMembersGet**
> List&lt;User&gt; orgunitsOrgidUsergroupsGroupidMembersGet(orgid, groupid)

List of all users in group.

Returns a list of all members in User Groups that are based on the Global Group with this groupid. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UserGroupsApi apiInstance = new UserGroupsApi(defaultClient);
    Long orgid = 56L; // Long | ID of organization
    Long groupid = 56L; // Long | ID of group
    try {
      List<User> result = apiInstance.orgunitsOrgidUsergroupsGroupidMembersGet(orgid, groupid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserGroupsApi#orgunitsOrgidUsergroupsGroupidMembersGet");
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
| **orgid** | **Long**| ID of organization | |
| **groupid** | **Long**| ID of group | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidUsergroupsGroupidMembersPost"></a>
# **orgunitsOrgidUsergroupsGroupidMembersPost**
> UserId orgunitsOrgidUsergroupsGroupidMembersPost(orgid, groupid, body)

Add user group member.

Adds a user to user group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UserGroupsApi apiInstance = new UserGroupsApi(defaultClient);
    Long orgid = 56L; // Long | ID of organization
    Long groupid = 56L; // Long | ID of group
    AddUserGroupMember body = new AddUserGroupMember(); // AddUserGroupMember | 
    try {
      UserId result = apiInstance.orgunitsOrgidUsergroupsGroupidMembersPost(orgid, groupid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserGroupsApi#orgunitsOrgidUsergroupsGroupidMembersPost");
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
| **orgid** | **Long**| ID of organization | |
| **groupid** | **Long**| ID of group | |
| **body** | [**AddUserGroupMember**](AddUserGroupMember.md)|  | |

### Return type

[**UserId**](UserId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User ID of added user |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidUsergroupsGroupidMembersUuidDelete"></a>
# **orgunitsOrgidUsergroupsGroupidMembersUuidDelete**
> orgunitsOrgidUsergroupsGroupidMembersUuidDelete(orgid, groupid, uuid)

Remove user group member.

Removes a user from a user group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UserGroupsApi apiInstance = new UserGroupsApi(defaultClient);
    Long orgid = 56L; // Long | ID of organization
    Long groupid = 56L; // Long | ID of group
    UUID uuid = UUID.randomUUID(); // UUID | UUID of user to remove from group.
    try {
      apiInstance.orgunitsOrgidUsergroupsGroupidMembersUuidDelete(orgid, groupid, uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserGroupsApi#orgunitsOrgidUsergroupsGroupidMembersUuidDelete");
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
| **orgid** | **Long**| ID of organization | |
| **groupid** | **Long**| ID of group | |
| **uuid** | **UUID**| UUID of user to remove from group. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidUsergroupsPost"></a>
# **orgunitsOrgidUsergroupsPost**
> List&lt;GroupId&gt; orgunitsOrgidUsergroupsPost(orgid, body)

Create a User Group.

Create a User Group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UserGroupsApi apiInstance = new UserGroupsApi(defaultClient);
    Long orgid = 56L; // Long | ID of organization
    AddUserGroup body = new AddUserGroup(); // AddUserGroup | 
    try {
      List<GroupId> result = apiInstance.orgunitsOrgidUsergroupsPost(orgid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserGroupsApi#orgunitsOrgidUsergroupsPost");
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
| **orgid** | **Long**| ID of organization | |
| **body** | [**AddUserGroup**](AddUserGroup.md)|  | |

### Return type

[**List&lt;GroupId&gt;**](GroupId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of User Groups. |  -  |
| **0** | Unexpected error |  -  |

