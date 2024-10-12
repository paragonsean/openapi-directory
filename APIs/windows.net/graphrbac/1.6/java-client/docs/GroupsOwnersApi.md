# GroupsOwnersApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groupsAddOwner**](GroupsOwnersApi.md#groupsAddOwner) | **POST** /{tenantID}/groups/{objectId}/$links/owners |  |
| [**groupsRemoveOwner**](GroupsOwnersApi.md#groupsRemoveOwner) | **DELETE** /{tenantID}/groups/{objectId}/$links/owners/{ownerObjectId} |  |


<a id="groupsAddOwner"></a>
# **groupsAddOwner**
> groupsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters)



Add an owner to a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsOwnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupsOwnersApi apiInstance = new GroupsOwnersApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the application to which to add the owner.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    AddOwnerParameters addOwnerParameters = new AddOwnerParameters(); // AddOwnerParameters | The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
    try {
      apiInstance.groupsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsOwnersApi#groupsAddOwner");
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
| **objectId** | **String**| The object ID of the application to which to add the owner. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **addOwnerParameters** | [**AddOwnerParameters**](AddOwnerParameters.md)| The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd. | |

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

<a id="groupsRemoveOwner"></a>
# **groupsRemoveOwner**
> groupsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID)



Remove a member from owners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsOwnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GroupsOwnersApi apiInstance = new GroupsOwnersApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the group from which to remove the owner.
    String ownerObjectId = "ownerObjectId_example"; // String | Owner object id
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.groupsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsOwnersApi#groupsRemoveOwner");
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
| **objectId** | **String**| The object ID of the group from which to remove the owner. | |
| **ownerObjectId** | **String**| Owner object id | |
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

