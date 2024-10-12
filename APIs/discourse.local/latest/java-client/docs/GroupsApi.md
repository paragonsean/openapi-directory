# GroupsApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addGroupMembers**](GroupsApi.md#addGroupMembers) | **PUT** /groups/{id}/members.json | Add group members |
| [**createGroup**](GroupsApi.md#createGroup) | **POST** /admin/groups.json | Create a group |
| [**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /admin/groups/{id}.json | Delete a group |
| [**getGroup**](GroupsApi.md#getGroup) | **GET** /groups/{id}.json | Get a group |
| [**listGroupMembers**](GroupsApi.md#listGroupMembers) | **GET** /groups/{id}/members.json | List group members |
| [**listGroups**](GroupsApi.md#listGroups) | **GET** /groups.json | List groups |
| [**removeGroupMembers**](GroupsApi.md#removeGroupMembers) | **DELETE** /groups/{id}/members.json | Remove group members |
| [**updateGroup**](GroupsApi.md#updateGroup) | **PUT** /groups/{id}.json | Update a group |


<a id="addGroupMembers"></a>
# **addGroupMembers**
> AddGroupMembers200Response addGroupMembers(id, addGroupMembersRequest)

Add group members

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | 
    AddGroupMembersRequest addGroupMembersRequest = new AddGroupMembersRequest(); // AddGroupMembersRequest | 
    try {
      AddGroupMembers200Response result = apiInstance.addGroupMembers(id, addGroupMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#addGroupMembers");
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
| **id** | **Integer**|  | |
| **addGroupMembersRequest** | [**AddGroupMembersRequest**](AddGroupMembersRequest.md)|  | [optional] |

### Return type

[**AddGroupMembers200Response**](AddGroupMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="createGroup"></a>
# **createGroup**
> CreateGroup200Response createGroup(createGroupRequest)

Create a group

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    CreateGroupRequest createGroupRequest = new CreateGroupRequest(); // CreateGroupRequest | 
    try {
      CreateGroup200Response result = apiInstance.createGroup(createGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#createGroup");
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
| **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | [optional] |

### Return type

[**CreateGroup200Response**](CreateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | group created |  -  |

<a id="deleteGroup"></a>
# **deleteGroup**
> DeleteGroup200Response deleteGroup(id)

Delete a group

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      DeleteGroup200Response result = apiInstance.deleteGroup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteGroup");
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
| **id** | **Integer**|  | |

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="getGroup"></a>
# **getGroup**
> GetGroup200Response getGroup(id)

Get a group

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "name"; // String | Use group name instead of id
    try {
      GetGroup200Response result = apiInstance.getGroup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroup");
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
| **id** | **String**| Use group name instead of id | |

### Return type

[**GetGroup200Response**](GetGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="listGroupMembers"></a>
# **listGroupMembers**
> ListGroupMembers200Response listGroupMembers(id)

List group members

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "name"; // String | Use group name instead of id
    try {
      ListGroupMembers200Response result = apiInstance.listGroupMembers(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listGroupMembers");
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
| **id** | **String**| Use group name instead of id | |

### Return type

[**ListGroupMembers200Response**](ListGroupMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="listGroups"></a>
# **listGroups**
> ListGroups200Response listGroups()

List groups

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    try {
      ListGroups200Response result = apiInstance.listGroups();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listGroups");
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

[**ListGroups200Response**](ListGroups200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="removeGroupMembers"></a>
# **removeGroupMembers**
> RemoveGroupMembers200Response removeGroupMembers(id, addGroupMembersRequest)

Remove group members

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | 
    AddGroupMembersRequest addGroupMembersRequest = new AddGroupMembersRequest(); // AddGroupMembersRequest | 
    try {
      RemoveGroupMembers200Response result = apiInstance.removeGroupMembers(id, addGroupMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#removeGroupMembers");
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
| **id** | **Integer**|  | |
| **addGroupMembersRequest** | [**AddGroupMembersRequest**](AddGroupMembersRequest.md)|  | [optional] |

### Return type

[**RemoveGroupMembers200Response**](RemoveGroupMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="updateGroup"></a>
# **updateGroup**
> UpdateGroup200Response updateGroup(id, updateGroupRequest)

Update a group

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
    defaultClient.setBasePath("http://discourse.local");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | 
    UpdateGroupRequest updateGroupRequest = new UpdateGroupRequest(); // UpdateGroupRequest | 
    try {
      UpdateGroup200Response result = apiInstance.updateGroup(id, updateGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#updateGroup");
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
| **id** | **Integer**|  | |
| **updateGroupRequest** | [**UpdateGroupRequest**](UpdateGroupRequest.md)|  | [optional] |

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

