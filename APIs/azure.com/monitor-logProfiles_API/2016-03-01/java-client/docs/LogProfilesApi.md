# LogProfilesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logProfilesCreateOrUpdate**](LogProfilesApi.md#logProfilesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} |  |
| [**logProfilesDelete**](LogProfilesApi.md#logProfilesDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} |  |
| [**logProfilesGet**](LogProfilesApi.md#logProfilesGet) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} |  |
| [**logProfilesList**](LogProfilesApi.md#logProfilesList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles |  |


<a id="logProfilesCreateOrUpdate"></a>
# **logProfilesCreateOrUpdate**
> LogProfileResource logProfilesCreateOrUpdate(logProfileName, apiVersion, subscriptionId, parameters)



Create or update a log profile in Azure Monitoring REST API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LogProfilesApi apiInstance = new LogProfilesApi(defaultClient);
    String logProfileName = "logProfileName_example"; // String | The name of the log profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    LogProfileResource parameters = new LogProfileResource(); // LogProfileResource | Parameters supplied to the operation.
    try {
      LogProfileResource result = apiInstance.logProfilesCreateOrUpdate(logProfileName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogProfilesApi#logProfilesCreateOrUpdate");
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
| **logProfileName** | **String**| The name of the log profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **parameters** | [**LogProfileResource**](LogProfileResource.md)| Parameters supplied to the operation. | |

### Return type

[**LogProfileResource**](LogProfileResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to create or update a log profile |  -  |

<a id="logProfilesDelete"></a>
# **logProfilesDelete**
> logProfilesDelete(logProfileName, apiVersion, subscriptionId)



Deletes the log profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LogProfilesApi apiInstance = new LogProfilesApi(defaultClient);
    String logProfileName = "logProfileName_example"; // String | The name of the log profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      apiInstance.logProfilesDelete(logProfileName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogProfilesApi#logProfilesDelete");
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
| **logProfileName** | **String**| The name of the log profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to delete a log profile |  -  |

<a id="logProfilesGet"></a>
# **logProfilesGet**
> LogProfileResource logProfilesGet(logProfileName, apiVersion, subscriptionId)



Gets the log profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LogProfilesApi apiInstance = new LogProfilesApi(defaultClient);
    String logProfileName = "logProfileName_example"; // String | The name of the log profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      LogProfileResource result = apiInstance.logProfilesGet(logProfileName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogProfilesApi#logProfilesGet");
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
| **logProfileName** | **String**| The name of the log profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**LogProfileResource**](LogProfileResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about a log profile. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="logProfilesList"></a>
# **logProfilesList**
> LogProfileCollection logProfilesList(apiVersion, subscriptionId)



List the log profiles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LogProfilesApi apiInstance = new LogProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      LogProfileCollection result = apiInstance.logProfilesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogProfilesApi#logProfilesList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**LogProfileCollection**](LogProfileCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to list log profiles |  -  |

