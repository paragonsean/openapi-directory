# GroupsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAMemberToAnOrganizationWithinAGroup**](GroupsApi.md#addAMemberToAnOrganizationWithinAGroup) | **POST** /group/{groupId}/org/{orgId}/members | Add a member to an organization within a group |
| [**deleteTagFromGroup**](GroupsApi.md#deleteTagFromGroup) | **POST** /group/{groupId}/tags/delete | Delete tag from group |
| [**listAllMembersInAGroup**](GroupsApi.md#listAllMembersInAGroup) | **GET** /group/{groupId}/members | List all members in a group |
| [**listAllOrganizationsInAGroup**](GroupsApi.md#listAllOrganizationsInAGroup) | **GET** /group/{groupId}/orgs | List all organizations in a group |
| [**listAllRolesInAGroup**](GroupsApi.md#listAllRolesInAGroup) | **GET** /group/{groupId}/roles | List all roles in a group |
| [**listAllTagsInAGroup**](GroupsApi.md#listAllTagsInAGroup) | **GET** /group/{groupId}/tags | List all tags in a group |
| [**updateGroupSettings**](GroupsApi.md#updateGroupSettings) | **PUT** /group/{groupId}/settings | Update group settings |
| [**viewGroupSettings**](GroupsApi.md#viewGroupSettings) | **GET** /group/{groupId}/settings | View group settings |


<a id="addAMemberToAnOrganizationWithinAGroup"></a>
# **addAMemberToAnOrganizationWithinAGroup**
> addAMemberToAnOrganizationWithinAGroup(groupId, orgId, addAMemberToAnOrganizationWithinAGroupRequest)

Add a member to an organization within a group



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID we want to add the member to. The `API_KEY` must have access to this organization.
    AddAMemberToAnOrganizationWithinAGroupRequest addAMemberToAnOrganizationWithinAGroupRequest = new AddAMemberToAnOrganizationWithinAGroupRequest(); // AddAMemberToAnOrganizationWithinAGroupRequest | 
    try {
      apiInstance.addAMemberToAnOrganizationWithinAGroup(groupId, orgId, addAMemberToAnOrganizationWithinAGroupRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#addAMemberToAnOrganizationWithinAGroup");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | |
| **orgId** | **String**| The organization ID we want to add the member to. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **addAMemberToAnOrganizationWithinAGroupRequest** | [**AddAMemberToAnOrganizationWithinAGroupRequest**](AddAMemberToAnOrganizationWithinAGroupRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteTagFromGroup"></a>
# **deleteTagFromGroup**
> DeleteTagFromGroup200Response deleteTagFromGroup(groupId, deleteTagFromGroupRequest)

Delete tag from group



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
    DeleteTagFromGroupRequest deleteTagFromGroupRequest = new DeleteTagFromGroupRequest(); // DeleteTagFromGroupRequest | 
    try {
      DeleteTagFromGroup200Response result = apiInstance.deleteTagFromGroup(groupId, deleteTagFromGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteTagFromGroup");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | |
| **deleteTagFromGroupRequest** | [**DeleteTagFromGroupRequest**](DeleteTagFromGroupRequest.md)|  | [optional] |

### Return type

[**DeleteTagFromGroup200Response**](DeleteTagFromGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllMembersInAGroup"></a>
# **listAllMembersInAGroup**
> List&lt;Object&gt; listAllMembersInAGroup(groupId)

List all members in a group



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
    try {
      List<Object> result = apiInstance.listAllMembersInAGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listAllMembersInAGroup");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllOrganizationsInAGroup"></a>
# **listAllOrganizationsInAGroup**
> listAllOrganizationsInAGroup(groupId, perPage, page, name)

List all organizations in a group



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "a060a49f-636e-480f-9e14-38e773b2a97f"; // String | The group ID. The `API_KEY` must have READ access to this group and LIST organizations access in this group.
    BigDecimal perPage = new BigDecimal("100"); // BigDecimal | The number of results to return (maximum is 100).
    BigDecimal page = new BigDecimal("1"); // BigDecimal | For pagination - offset (from which to start returning results).
    String name = "my"; // String | Only organizations that have a name that **starts with** this value (case insensitive) will be returned.
    try {
      apiInstance.listAllOrganizationsInAGroup(groupId, perPage, page, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listAllOrganizationsInAGroup");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have READ access to this group and LIST organizations access in this group. | |
| **perPage** | **BigDecimal**| The number of results to return (maximum is 100). | [optional] [default to 100] |
| **page** | **BigDecimal**| For pagination - offset (from which to start returning results). | [optional] |
| **name** | **String**| Only organizations that have a name that **starts with** this value (case insensitive) will be returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllRolesInAGroup"></a>
# **listAllRolesInAGroup**
> listAllRolesInAGroup(groupId)

List all roles in a group



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "a060a49f-636e-480f-9e14-38e773b2a97f"; // String | The group ID. The `API_KEY` must have READ access to this group.
    try {
      apiInstance.listAllRolesInAGroup(groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listAllRolesInAGroup");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have READ access to this group. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllTagsInAGroup"></a>
# **listAllTagsInAGroup**
> ListAllTagsInAGroup200Response listAllTagsInAGroup(groupId, perPage, page)

List all tags in a group



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of results to return (the default is 1000).
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The offset from which to start returning results from.
    try {
      ListAllTagsInAGroup200Response result = apiInstance.listAllTagsInAGroup(groupId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listAllTagsInAGroup");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | |
| **perPage** | **BigDecimal**| The number of results to return (the default is 1000). | [optional] |
| **page** | **BigDecimal**| The offset from which to start returning results from. | [optional] |

### Return type

[**ListAllTagsInAGroup200Response**](ListAllTagsInAGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

<a id="updateGroupSettings"></a>
# **updateGroupSettings**
> ViewGroupSettings200Response updateGroupSettings(groupId)

Update group settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Automatically added
    try {
      ViewGroupSettings200Response result = apiInstance.updateGroupSettings(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#updateGroupSettings");
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
| **groupId** | **String**| Automatically added | |

### Return type

[**ViewGroupSettings200Response**](ViewGroupSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="viewGroupSettings"></a>
# **viewGroupSettings**
> ViewGroupSettings200Response viewGroupSettings(groupId)

View group settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "b61bc07c-27c6-42b3-8b04-0f228ed31a67"; // String | The group ID. The `API_KEY` must have admin access to this group.
    try {
      ViewGroupSettings200Response result = apiInstance.viewGroupSettings(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#viewGroupSettings");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have admin access to this group. | |

### Return type

[**ViewGroupSettings200Response**](ViewGroupSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

