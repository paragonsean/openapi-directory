# ServicePrincipalOwnersApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicePrincipalsAddOwner**](ServicePrincipalOwnersApi.md#servicePrincipalsAddOwner) | **POST** /{tenantID}/servicePrincipals/{objectId}/$links/owners |  |
| [**servicePrincipalsListOwners**](ServicePrincipalOwnersApi.md#servicePrincipalsListOwners) | **GET** /{tenantID}/servicePrincipals/{objectId}/owners | Directory objects that are owners of this service principal. |
| [**servicePrincipalsRemoveOwner**](ServicePrincipalOwnersApi.md#servicePrincipalsRemoveOwner) | **DELETE** /{tenantID}/servicePrincipals/{objectId}/$links/owners/{ownerObjectId} |  |


<a id="servicePrincipalsAddOwner"></a>
# **servicePrincipalsAddOwner**
> servicePrincipalsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters)



Add an owner to a service principal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalOwnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalOwnersApi apiInstance = new ServicePrincipalOwnersApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal to which to add the owner.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    AddOwnerParameters addOwnerParameters = new AddOwnerParameters(); // AddOwnerParameters | The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
    try {
      apiInstance.servicePrincipalsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalOwnersApi#servicePrincipalsAddOwner");
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
| **objectId** | **String**| The object ID of the service principal to which to add the owner. | |
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

<a id="servicePrincipalsListOwners"></a>
# **servicePrincipalsListOwners**
> DirectoryObjectListResult servicePrincipalsListOwners(objectId, apiVersion, tenantID)

Directory objects that are owners of this service principal.

The owners are a set of non-admin users who are allowed to modify this object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalOwnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalOwnersApi apiInstance = new ServicePrincipalOwnersApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal for which to get owners.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      DirectoryObjectListResult result = apiInstance.servicePrincipalsListOwners(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalOwnersApi#servicePrincipalsListOwners");
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
| **objectId** | **String**| The object ID of the service principal for which to get owners. | |
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

<a id="servicePrincipalsRemoveOwner"></a>
# **servicePrincipalsRemoveOwner**
> servicePrincipalsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID)



Remove a member from owners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalOwnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalOwnersApi apiInstance = new ServicePrincipalOwnersApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal from which to remove the owner.
    String ownerObjectId = "ownerObjectId_example"; // String | Owner object id
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.servicePrincipalsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalOwnersApi#servicePrincipalsRemoveOwner");
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
| **objectId** | **String**| The object ID of the service principal from which to remove the owner. | |
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

