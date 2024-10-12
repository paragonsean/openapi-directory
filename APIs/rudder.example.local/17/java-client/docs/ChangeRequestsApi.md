# ChangeRequestsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptChangeRequest**](ChangeRequestsApi.md#acceptChangeRequest) | **POST** /changeRequests/{changeRequestId}/accept | Accept a request details |
| [**changeRequestDetails**](ChangeRequestsApi.md#changeRequestDetails) | **GET** /changeRequests/{changeRequestId} | Get a change request details |
| [**declineChangeRequest**](ChangeRequestsApi.md#declineChangeRequest) | **DELETE** /changeRequests/{changeRequestId} | Decline a request details |
| [**listChangeRequests**](ChangeRequestsApi.md#listChangeRequests) | **GET** /api/changeRequests | List all change requests |
| [**listUsers**](ChangeRequestsApi.md#listUsers) | **GET** /users | List user |
| [**removeValidatedUser**](ChangeRequestsApi.md#removeValidatedUser) | **DELETE** /validatedUsers/{username} | Remove an user from validated user list |
| [**saveWorkflowUser**](ChangeRequestsApi.md#saveWorkflowUser) | **POST** /validatedUsers | Update validated user list |
| [**updateChangeRequest**](ChangeRequestsApi.md#updateChangeRequest) | **POST** /changeRequests/{changeRequestId} | Update a request details |


<a id="acceptChangeRequest"></a>
# **acceptChangeRequest**
> AcceptChangeRequest200Response acceptChangeRequest(changeRequestId, acceptChangeRequestRequest)

Accept a request details

Accept a change request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    Integer changeRequestId = 37; // Integer | 
    AcceptChangeRequestRequest acceptChangeRequestRequest = new AcceptChangeRequestRequest(); // AcceptChangeRequestRequest | 
    try {
      AcceptChangeRequest200Response result = apiInstance.acceptChangeRequest(changeRequestId, acceptChangeRequestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#acceptChangeRequest");
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
| **changeRequestId** | **Integer**|  | |
| **acceptChangeRequestRequest** | [**AcceptChangeRequestRequest**](AcceptChangeRequestRequest.md)|  | |

### Return type

[**AcceptChangeRequest200Response**](AcceptChangeRequest200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change requests information |  -  |

<a id="changeRequestDetails"></a>
# **changeRequestDetails**
> ChangeRequestDetails200Response changeRequestDetails(changeRequestId)

Get a change request details

Get a change request details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    Integer changeRequestId = 37; // Integer | 
    try {
      ChangeRequestDetails200Response result = apiInstance.changeRequestDetails(changeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#changeRequestDetails");
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
| **changeRequestId** | **Integer**|  | |

### Return type

[**ChangeRequestDetails200Response**](ChangeRequestDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change requests information |  -  |

<a id="declineChangeRequest"></a>
# **declineChangeRequest**
> DeclineChangeRequest200Response declineChangeRequest(changeRequestId)

Decline a request details

Refuse a change request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    Integer changeRequestId = 37; // Integer | 
    try {
      DeclineChangeRequest200Response result = apiInstance.declineChangeRequest(changeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#declineChangeRequest");
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
| **changeRequestId** | **Integer**|  | |

### Return type

[**DeclineChangeRequest200Response**](DeclineChangeRequest200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change requests information |  -  |

<a id="listChangeRequests"></a>
# **listChangeRequests**
> ListChangeRequests200Response listChangeRequests()

List all change requests

List all change requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    try {
      ListChangeRequests200Response result = apiInstance.listChangeRequests();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#listChangeRequests");
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

[**ListChangeRequests200Response**](ListChangeRequests200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change requests information |  -  |

<a id="listUsers"></a>
# **listUsers**
> ListUsers200Response listUsers()

List user

List all validated and unvalidated users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    try {
      ListUsers200Response result = apiInstance.listUsers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#listUsers");
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

[**ListUsers200Response**](ListUsers200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List users |  -  |

<a id="removeValidatedUser"></a>
# **removeValidatedUser**
> RemoveValidatedUser200Response removeValidatedUser(username)

Remove an user from validated user list

The user is again subject to workflow validation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    String username = "JaneDoe"; // String | Username of an user (unique)
    try {
      RemoveValidatedUser200Response result = apiInstance.removeValidatedUser(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#removeValidatedUser");
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
| **username** | **String**| Username of an user (unique) | |

### Return type

[**RemoveValidatedUser200Response**](RemoveValidatedUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed user |  -  |

<a id="saveWorkflowUser"></a>
# **saveWorkflowUser**
> SaveWorkflowUser200Response saveWorkflowUser(saveWorkflowUserRequest)

Update validated user list

Add and remove user from validated users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    SaveWorkflowUserRequest saveWorkflowUserRequest = new SaveWorkflowUserRequest(); // SaveWorkflowUserRequest | 
    try {
      SaveWorkflowUser200Response result = apiInstance.saveWorkflowUser(saveWorkflowUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#saveWorkflowUser");
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
| **saveWorkflowUserRequest** | [**SaveWorkflowUserRequest**](SaveWorkflowUserRequest.md)|  | |

### Return type

[**SaveWorkflowUser200Response**](SaveWorkflowUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |

<a id="updateChangeRequest"></a>
# **updateChangeRequest**
> UpdateChangeRequest200Response updateChangeRequest(changeRequestId, updateChangeRequestRequest)

Update a request details

Update a change request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ChangeRequestsApi apiInstance = new ChangeRequestsApi(defaultClient);
    Integer changeRequestId = 37; // Integer | 
    UpdateChangeRequestRequest updateChangeRequestRequest = new UpdateChangeRequestRequest(); // UpdateChangeRequestRequest | 
    try {
      UpdateChangeRequest200Response result = apiInstance.updateChangeRequest(changeRequestId, updateChangeRequestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeRequestsApi#updateChangeRequest");
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
| **changeRequestId** | **Integer**|  | |
| **updateChangeRequestRequest** | [**UpdateChangeRequestRequest**](UpdateChangeRequestRequest.md)|  | |

### Return type

[**UpdateChangeRequest200Response**](UpdateChangeRequest200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change requests information |  -  |

