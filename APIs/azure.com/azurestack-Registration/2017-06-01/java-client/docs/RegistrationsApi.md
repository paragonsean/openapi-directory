# RegistrationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registrationsCreateOrUpdate**](RegistrationsApi.md#registrationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} |  |
| [**registrationsDelete**](RegistrationsApi.md#registrationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} |  |
| [**registrationsGet**](RegistrationsApi.md#registrationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} |  |
| [**registrationsGetActivationKey**](RegistrationsApi.md#registrationsGetActivationKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/getactivationkey |  |
| [**registrationsList**](RegistrationsApi.md#registrationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations |  |
| [**registrationsUpdate**](RegistrationsApi.md#registrationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} |  |


<a id="registrationsCreateOrUpdate"></a>
# **registrationsCreateOrUpdate**
> Registration registrationsCreateOrUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token)



Create or update an Azure Stack registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    RegistrationParameter token = new RegistrationParameter(); // RegistrationParameter | Registration token
    try {
      Registration result = apiInstance.registrationsCreateOrUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registrationsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |
| **token** | [**RegistrationParameter**](RegistrationParameter.md)| Registration token | |

### Return type

[**Registration**](Registration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | CREATED |  -  |

<a id="registrationsDelete"></a>
# **registrationsDelete**
> registrationsDelete(subscriptionId, resourceGroup, registrationName, apiVersion)



Delete the requested Azure Stack registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      apiInstance.registrationsDelete(subscriptionId, resourceGroup, registrationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registrationsDelete");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

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
| **200** | OK |  -  |
| **204** | NO CONTENT |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationsGet"></a>
# **registrationsGet**
> Registration registrationsGet(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns the properties of an Azure Stack registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      Registration result = apiInstance.registrationsGet(subscriptionId, resourceGroup, registrationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registrationsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**Registration**](Registration.md)

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

<a id="registrationsGetActivationKey"></a>
# **registrationsGetActivationKey**
> ActivationKeyResult registrationsGetActivationKey(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns Azure Stack Activation Key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      ActivationKeyResult result = apiInstance.registrationsGetActivationKey(subscriptionId, resourceGroup, registrationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registrationsGetActivationKey");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**ActivationKeyResult**](ActivationKeyResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="registrationsList"></a>
# **registrationsList**
> RegistrationList registrationsList(subscriptionId, resourceGroup, apiVersion)



Returns a list of all registrations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      RegistrationList result = apiInstance.registrationsList(subscriptionId, resourceGroup, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registrationsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**RegistrationList**](RegistrationList.md)

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

<a id="registrationsUpdate"></a>
# **registrationsUpdate**
> Registration registrationsUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token)



Patch an Azure Stack registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    RegistrationParameter token = new RegistrationParameter(); // RegistrationParameter | Registration token
    try {
      Registration result = apiInstance.registrationsUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registrationsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |
| **token** | [**RegistrationParameter**](RegistrationParameter.md)| Registration token | |

### Return type

[**Registration**](Registration.md)

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

