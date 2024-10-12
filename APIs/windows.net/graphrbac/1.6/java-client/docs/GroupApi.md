# GroupApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groupsAddMember**](GroupApi.md#groupsAddMember) | **POST** /{tenantID}/groups/{groupObjectId}/$links/members |  |
| [**groupsCreate**](GroupApi.md#groupsCreate) | **POST** /{tenantID}/groups |  |
| [**groupsDelete**](GroupApi.md#groupsDelete) | **DELETE** /{tenantID}/groups/{objectId} |  |
| [**groupsGet**](GroupApi.md#groupsGet) | **GET** /{tenantID}/groups/{objectId} |  |
| [**groupsGetGroupMembers**](GroupApi.md#groupsGetGroupMembers) | **GET** /{tenantID}/groups/{objectId}/members |  |
| [**groupsGetMemberGroups**](GroupApi.md#groupsGetMemberGroups) | **POST** /{tenantID}/groups/{objectId}/getMemberGroups |  |
| [**groupsIsMemberOf**](GroupApi.md#groupsIsMemberOf) | **POST** /{tenantID}/isMemberOf |  |
| [**groupsList**](GroupApi.md#groupsList) | **GET** /{tenantID}/groups |  |
| [**groupsRemoveMember**](GroupApi.md#groupsRemoveMember) | **DELETE** /{tenantID}/groups/{groupObjectId}/$links/members/{memberObjectId} |  |


<a id="groupsAddMember"></a>
# **groupsAddMember**
> groupsAddMember(groupObjectId, apiVersion, tenantID, groupAddMemberParameters)



Add a member to a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupObjectId = "groupObjectId_example"; // String | The object ID of the group to which to add the member.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    GroupAddMemberParameters groupAddMemberParameters = new GroupAddMemberParameters(); // GroupAddMemberParameters | The URL of the member object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
    try {
      apiInstance.groupsAddMember(groupObjectId, apiVersion, tenantID, groupAddMemberParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsAddMember");
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
| **groupObjectId** | **String**| The object ID of the group to which to add the member. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **groupAddMemberParameters** | [**GroupAddMemberParameters**](GroupAddMemberParameters.md)| The URL of the member object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. Indicates success. No response body is returned. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsCreate"></a>
# **groupsCreate**
> ADGroup groupsCreate(apiVersion, tenantID, groupCreateParameters)



Create a group in the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    GroupCreateParameters groupCreateParameters = new GroupCreateParameters(); // GroupCreateParameters | The parameters for the group to create.
    try {
      ADGroup result = apiInstance.groupsCreate(apiVersion, tenantID, groupCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **groupCreateParameters** | [**GroupCreateParameters**](GroupCreateParameters.md)| The parameters for the group to create. | |

### Return type

[**ADGroup**](ADGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsDelete"></a>
# **groupsDelete**
> groupsDelete(objectId, apiVersion, tenantID)



Delete a group from the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the group to delete.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.groupsDelete(objectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsDelete");
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
| **objectId** | **String**| The object ID of the group to delete. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsGet"></a>
# **groupsGet**
> ADGroup groupsGet(objectId, apiVersion, tenantID)



Gets group information from the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the user for which to get group information.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      ADGroup result = apiInstance.groupsGet(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsGet");
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
| **objectId** | **String**| The object ID of the user for which to get group information. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**ADGroup**](ADGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsGetGroupMembers"></a>
# **groupsGetGroupMembers**
> DirectoryObjectListResult groupsGetGroupMembers(objectId, apiVersion, tenantID)



Gets the members of a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the group whose members should be retrieved.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      DirectoryObjectListResult result = apiInstance.groupsGetGroupMembers(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsGetGroupMembers");
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
| **objectId** | **String**| The object ID of the group whose members should be retrieved. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsGetMemberGroups"></a>
# **groupsGetMemberGroups**
> GroupGetMemberGroupsResult groupsGetMemberGroups(objectId, apiVersion, tenantID, groupGetMemberGroupsParameters)



Gets a collection of object IDs of groups of which the specified group is a member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the group for which to get group membership.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    GroupGetMemberGroupsParameters groupGetMemberGroupsParameters = new GroupGetMemberGroupsParameters(); // GroupGetMemberGroupsParameters | Group filtering parameters.
    try {
      GroupGetMemberGroupsResult result = apiInstance.groupsGetMemberGroups(objectId, apiVersion, tenantID, groupGetMemberGroupsParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsGetMemberGroups");
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
| **objectId** | **String**| The object ID of the group for which to get group membership. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **groupGetMemberGroupsParameters** | [**GroupGetMemberGroupsParameters**](GroupGetMemberGroupsParameters.md)| Group filtering parameters. | |

### Return type

[**GroupGetMemberGroupsResult**](GroupGetMemberGroupsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsIsMemberOf"></a>
# **groupsIsMemberOf**
> CheckGroupMembershipResult groupsIsMemberOf(apiVersion, tenantID, checkGroupMembershipParameters)



Checks whether the specified user, group, contact, or service principal is a direct or transitive member of the specified group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    CheckGroupMembershipParameters checkGroupMembershipParameters = new CheckGroupMembershipParameters(); // CheckGroupMembershipParameters | The check group membership parameters.
    try {
      CheckGroupMembershipResult result = apiInstance.groupsIsMemberOf(apiVersion, tenantID, checkGroupMembershipParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsIsMemberOf");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **checkGroupMembershipParameters** | [**CheckGroupMembershipParameters**](CheckGroupMembershipParameters.md)| The check group membership parameters. | |

### Return type

[**CheckGroupMembershipResult**](CheckGroupMembershipResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Indicates success. Returns true if the user, contact, group, or service principal is a direct or a transitive member of the specified group; otherwise, false. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsList"></a>
# **groupsList**
> GroupListResult groupsList(apiVersion, tenantID, $filter)



Gets list of groups for the current tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    try {
      GroupListResult result = apiInstance.groupsList(apiVersion, tenantID, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsList");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |

### Return type

[**GroupListResult**](GroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsRemoveMember"></a>
# **groupsRemoveMember**
> groupsRemoveMember(groupObjectId, memberObjectId, apiVersion, tenantID)



Remove a member from a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupObjectId = "groupObjectId_example"; // String | The object ID of the group from which to remove the member.
    String memberObjectId = "memberObjectId_example"; // String | Member object id
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.groupsRemoveMember(groupObjectId, memberObjectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#groupsRemoveMember");
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
| **groupObjectId** | **String**| The object ID of the group from which to remove the member. | |
| **memberObjectId** | **String**| Member object id | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. Indicates success. No response body is returned. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

