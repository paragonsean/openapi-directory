# SecurityContactsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**securityContactsCreate**](SecurityContactsApi.md#securityContactsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} |  |
| [**securityContactsDelete**](SecurityContactsApi.md#securityContactsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} |  |
| [**securityContactsGet**](SecurityContactsApi.md#securityContactsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} |  |
| [**securityContactsList**](SecurityContactsApi.md#securityContactsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts |  |
| [**securityContactsUpdate**](SecurityContactsApi.md#securityContactsUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} |  |


<a id="securityContactsCreate"></a>
# **securityContactsCreate**
> SecurityContact securityContactsCreate(apiVersion, subscriptionId, securityContactName, securityContact)



Security contact configurations for the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecurityContactsApi apiInstance = new SecurityContactsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String securityContactName = "securityContactName_example"; // String | Name of the security contact object
    SecurityContact securityContact = new SecurityContact(); // SecurityContact | Security contact object
    try {
      SecurityContact result = apiInstance.securityContactsCreate(apiVersion, subscriptionId, securityContactName, securityContact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityContactsApi#securityContactsCreate");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **securityContactName** | **String**| Name of the security contact object | |
| **securityContact** | [**SecurityContact**](SecurityContact.md)| Security contact object | |

### Return type

[**SecurityContact**](SecurityContact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="securityContactsDelete"></a>
# **securityContactsDelete**
> securityContactsDelete(apiVersion, subscriptionId, securityContactName)



Security contact configurations for the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecurityContactsApi apiInstance = new SecurityContactsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String securityContactName = "securityContactName_example"; // String | Name of the security contact object
    try {
      apiInstance.securityContactsDelete(apiVersion, subscriptionId, securityContactName);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityContactsApi#securityContactsDelete");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **securityContactName** | **String**| Name of the security contact object | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="securityContactsGet"></a>
# **securityContactsGet**
> SecurityContact securityContactsGet(apiVersion, subscriptionId, securityContactName)



Security contact configurations for the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecurityContactsApi apiInstance = new SecurityContactsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String securityContactName = "securityContactName_example"; // String | Name of the security contact object
    try {
      SecurityContact result = apiInstance.securityContactsGet(apiVersion, subscriptionId, securityContactName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityContactsApi#securityContactsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **securityContactName** | **String**| Name of the security contact object | |

### Return type

[**SecurityContact**](SecurityContact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="securityContactsList"></a>
# **securityContactsList**
> SecurityContactList securityContactsList(apiVersion, subscriptionId)



Security contact configurations for the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecurityContactsApi apiInstance = new SecurityContactsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      SecurityContactList result = apiInstance.securityContactsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityContactsApi#securityContactsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**SecurityContactList**](SecurityContactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="securityContactsUpdate"></a>
# **securityContactsUpdate**
> SecurityContact securityContactsUpdate(apiVersion, subscriptionId, securityContactName, securityContact)



Security contact configurations for the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecurityContactsApi apiInstance = new SecurityContactsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String securityContactName = "securityContactName_example"; // String | Name of the security contact object
    SecurityContact securityContact = new SecurityContact(); // SecurityContact | Security contact object
    try {
      SecurityContact result = apiInstance.securityContactsUpdate(apiVersion, subscriptionId, securityContactName, securityContact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityContactsApi#securityContactsUpdate");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **securityContactName** | **String**| Name of the security contact object | |
| **securityContact** | [**SecurityContact**](SecurityContact.md)| Security contact object | |

### Return type

[**SecurityContact**](SecurityContact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

