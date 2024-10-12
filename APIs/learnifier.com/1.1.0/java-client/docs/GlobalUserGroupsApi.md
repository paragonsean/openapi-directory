# GlobalUserGroupsApi

All URIs are relative to *http://learnifier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalusergroupsGet**](GlobalUserGroupsApi.md#globalusergroupsGet) | **GET** /globalusergroups | List Global User Groups. |
| [**globalusergroupsGroupidMembersGet**](GlobalUserGroupsApi.md#globalusergroupsGroupidMembersGet) | **GET** /globalusergroups/{groupid}/members | List of all users in group. |


<a id="globalusergroupsGet"></a>
# **globalusergroupsGet**
> List&lt;GlobalUserGroup&gt; globalusergroupsGet()

List Global User Groups.

Returns a list of Global User Groups. Global User Groups are set up for the realm, and will generate groups that can be used on the client level. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    GlobalUserGroupsApi apiInstance = new GlobalUserGroupsApi(defaultClient);
    try {
      List<GlobalUserGroup> result = apiInstance.globalusergroupsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUserGroupsApi#globalusergroupsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;GlobalUserGroup&gt;**](GlobalUserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Global User Groups. |  -  |
| **0** | Unexpected error |  -  |

<a id="globalusergroupsGroupidMembersGet"></a>
# **globalusergroupsGroupidMembersGet**
> List&lt;User&gt; globalusergroupsGroupidMembersGet(groupid)

List of all users in group.

Returns a list of all members in User Groups that are based on the Global Group with this groupid. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUserGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    GlobalUserGroupsApi apiInstance = new GlobalUserGroupsApi(defaultClient);
    Long groupid = 56L; // Long | ID of group
    try {
      List<User> result = apiInstance.globalusergroupsGroupidMembersGet(groupid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUserGroupsApi#globalusergroupsGroupidMembersGet");
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

