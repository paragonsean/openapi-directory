# ProviderApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**providerGetPublishingUser**](ProviderApi.md#providerGetPublishingUser) | **GET** /providers/Microsoft.Web/publishingUsers/web | Gets publishing user |
| [**providerGetSourceControl**](ProviderApi.md#providerGetSourceControl) | **GET** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Gets source control token |
| [**providerGetSourceControls**](ProviderApi.md#providerGetSourceControls) | **GET** /providers/Microsoft.Web/sourcecontrols | Gets the source controls available for Azure websites |
| [**providerUpdatePublishingUser**](ProviderApi.md#providerUpdatePublishingUser) | **PUT** /providers/Microsoft.Web/publishingUsers/web | Updates publishing user |
| [**providerUpdateSourceControl**](ProviderApi.md#providerUpdateSourceControl) | **PUT** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Updates source control token |


<a id="providerGetPublishingUser"></a>
# **providerGetPublishingUser**
> User providerGetPublishingUser(apiVersion)

Gets publishing user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      User result = apiInstance.providerGetPublishingUser(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerGetPublishingUser");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="providerGetSourceControl"></a>
# **providerGetSourceControl**
> SourceControl providerGetSourceControl(sourceControlType, apiVersion)

Gets source control token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String sourceControlType = "sourceControlType_example"; // String | Type of source control
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SourceControl result = apiInstance.providerGetSourceControl(sourceControlType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerGetSourceControl");
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
| **sourceControlType** | **String**| Type of source control | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="providerGetSourceControls"></a>
# **providerGetSourceControls**
> SourceControlCollection providerGetSourceControls(apiVersion)

Gets the source controls available for Azure websites

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SourceControlCollection result = apiInstance.providerGetSourceControls(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerGetSourceControls");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**SourceControlCollection**](SourceControlCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="providerUpdatePublishingUser"></a>
# **providerUpdatePublishingUser**
> User providerUpdatePublishingUser(apiVersion, requestMessage)

Updates publishing user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    User requestMessage = new User(); // User | Details of publishing user
    try {
      User result = apiInstance.providerUpdatePublishingUser(apiVersion, requestMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerUpdatePublishingUser");
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
| **apiVersion** | **String**| API Version | |
| **requestMessage** | [**User**](User.md)| Details of publishing user | |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="providerUpdateSourceControl"></a>
# **providerUpdateSourceControl**
> SourceControl providerUpdateSourceControl(sourceControlType, apiVersion, requestMessage)

Updates source control token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String sourceControlType = "sourceControlType_example"; // String | Type of source control
    String apiVersion = "apiVersion_example"; // String | API Version
    SourceControl requestMessage = new SourceControl(); // SourceControl | Source control token information
    try {
      SourceControl result = apiInstance.providerUpdateSourceControl(sourceControlType, apiVersion, requestMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerUpdateSourceControl");
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
| **sourceControlType** | **String**| Type of source control | |
| **apiVersion** | **String**| API Version | |
| **requestMessage** | [**SourceControl**](SourceControl.md)| Source control token information | |

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

