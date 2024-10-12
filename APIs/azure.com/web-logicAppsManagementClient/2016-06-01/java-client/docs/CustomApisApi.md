# CustomApisApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customApisCreateOrUpdate**](CustomApisApi.md#customApisCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Replaces an existing custom API |
| [**customApisDelete**](CustomApisApi.md#customApisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Delete a custom API |
| [**customApisExtractApiDefinitionFromWsdl**](CustomApisApi.md#customApisExtractApiDefinitionFromWsdl) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/extractApiDefinitionFromWsdl | Returns API definition from WSDL |
| [**customApisGet**](CustomApisApi.md#customApisGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Get a custom API |
| [**customApisList**](CustomApisApi.md#customApisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/customApis | List of custom APIs |
| [**customApisListByResourceGroup**](CustomApisApi.md#customApisListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis | List of custom APIs |
| [**customApisListWsdlInterfaces**](CustomApisApi.md#customApisListWsdlInterfaces) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/listWsdlInterfaces | Lists WSDL interfaces |
| [**customApisMove**](CustomApisApi.md#customApisMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName}/move | Moves the custom API |
| [**customApisUpdate**](CustomApisApi.md#customApisUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Update an existing custom API |


<a id="customApisCreateOrUpdate"></a>
# **customApisCreateOrUpdate**
> CustomApiDefinition customApisCreateOrUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi)

Replaces an existing custom API

Creates or updates an existing custom API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiName = "apiName_example"; // String | API name
    String apiVersion = "apiVersion_example"; // String | API Version
    CustomApiDefinition customApi = new CustomApiDefinition(); // CustomApiDefinition | The custom API
    try {
      CustomApiDefinition result = apiInstance.customApisCreateOrUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiName** | **String**| API name | |
| **apiVersion** | **String**| API Version | |
| **customApi** | [**CustomApiDefinition**](CustomApiDefinition.md)| The custom API | |

### Return type

[**CustomApiDefinition**](CustomApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replacing custom API |  -  |

<a id="customApisDelete"></a>
# **customApisDelete**
> customApisDelete(subscriptionId, resourceGroupName, apiName, apiVersion)

Delete a custom API

Deletes a custom API from the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiName = "apiName_example"; // String | API name
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.customApisDelete(subscriptionId, resourceGroupName, apiName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisDelete");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiName** | **String**| API name | |
| **apiVersion** | **String**| API Version | |

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
| **200** | Successfully deleted the custom API |  -  |
| **204** | No custom API to delete |  -  |

<a id="customApisExtractApiDefinitionFromWsdl"></a>
# **customApisExtractApiDefinitionFromWsdl**
> Object customApisExtractApiDefinitionFromWsdl(subscriptionId, location, apiVersion, wsdlDefinition)

Returns API definition from WSDL

Parses the specified WSDL and extracts the API definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String location = "location_example"; // String | The location
    String apiVersion = "apiVersion_example"; // String | API Version
    WsdlDefinition wsdlDefinition = new WsdlDefinition(); // WsdlDefinition | WSDL definition
    try {
      Object result = apiInstance.customApisExtractApiDefinitionFromWsdl(subscriptionId, location, apiVersion, wsdlDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisExtractApiDefinitionFromWsdl");
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
| **subscriptionId** | **String**| Subscription Id | |
| **location** | **String**| The location | |
| **apiVersion** | **String**| API Version | |
| **wsdlDefinition** | [**WsdlDefinition**](WsdlDefinition.md)| WSDL definition | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Swagger of the API extracted from the WSDL |  -  |

<a id="customApisGet"></a>
# **customApisGet**
> CustomApiDefinition customApisGet(subscriptionId, resourceGroupName, apiName, apiVersion)

Get a custom API

Gets a custom API by name for a specific subscription and resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiName = "apiName_example"; // String | API name
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CustomApiDefinition result = apiInstance.customApisGet(subscriptionId, resourceGroupName, apiName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisGet");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiName** | **String**| API name | |
| **apiVersion** | **String**| API Version | |

### Return type

[**CustomApiDefinition**](CustomApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A custom API |  -  |

<a id="customApisList"></a>
# **customApisList**
> CustomApiDefinitionCollection customApisList(subscriptionId, apiVersion, $top, skiptoken)

List of custom APIs

Gets a list of all custom APIs for a subscription id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Integer $top = 56; // Integer | The number of items to be included in the result
    String skiptoken = "skiptoken_example"; // String | Skip Token
    try {
      CustomApiDefinitionCollection result = apiInstance.customApisList(subscriptionId, apiVersion, $top, skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisList");
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
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **$top** | **Integer**| The number of items to be included in the result | [optional] |
| **skiptoken** | **String**| Skip Token | [optional] |

### Return type

[**CustomApiDefinitionCollection**](CustomApiDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of custom APIs |  -  |

<a id="customApisListByResourceGroup"></a>
# **customApisListByResourceGroup**
> CustomApiDefinitionCollection customApisListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top, skiptoken)

List of custom APIs

Gets a list of all custom APIs in a subscription for a specific resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiVersion = "apiVersion_example"; // String | API Version
    Integer $top = 56; // Integer | The number of items to be included in the result
    String skiptoken = "skiptoken_example"; // String | Skip Token
    try {
      CustomApiDefinitionCollection result = apiInstance.customApisListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top, skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiVersion** | **String**| API Version | |
| **$top** | **Integer**| The number of items to be included in the result | [optional] |
| **skiptoken** | **String**| Skip Token | [optional] |

### Return type

[**CustomApiDefinitionCollection**](CustomApiDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of custom APIs |  -  |

<a id="customApisListWsdlInterfaces"></a>
# **customApisListWsdlInterfaces**
> WsdlServiceCollection customApisListWsdlInterfaces(subscriptionId, location, apiVersion, wsdlDefinition)

Lists WSDL interfaces

This returns the list of interfaces in the WSDL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String location = "location_example"; // String | The location
    String apiVersion = "apiVersion_example"; // String | API Version
    WsdlDefinition wsdlDefinition = new WsdlDefinition(); // WsdlDefinition | WSDL definition
    try {
      WsdlServiceCollection result = apiInstance.customApisListWsdlInterfaces(subscriptionId, location, apiVersion, wsdlDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisListWsdlInterfaces");
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
| **subscriptionId** | **String**| Subscription Id | |
| **location** | **String**| The location | |
| **apiVersion** | **String**| API Version | |
| **wsdlDefinition** | [**WsdlDefinition**](WsdlDefinition.md)| WSDL definition | |

### Return type

[**WsdlServiceCollection**](WsdlServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of interfaces |  -  |

<a id="customApisMove"></a>
# **customApisMove**
> customApisMove(subscriptionId, resourceGroupName, apiName, apiVersion, customApiReference)

Moves the custom API

Moves a specific custom API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiName = "apiName_example"; // String | API name
    String apiVersion = "apiVersion_example"; // String | API Version
    CustomApiReference customApiReference = new CustomApiReference(); // CustomApiReference | The custom API reference
    try {
      apiInstance.customApisMove(subscriptionId, resourceGroupName, apiName, apiVersion, customApiReference);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisMove");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiName** | **String**| API name | |
| **apiVersion** | **String**| API Version | |
| **customApiReference** | [**CustomApiReference**](CustomApiReference.md)| The custom API reference | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | custom API successfully moved |  -  |

<a id="customApisUpdate"></a>
# **customApisUpdate**
> CustomApiDefinition customApisUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi)

Update an existing custom API

Updates an existing custom API&#39;s tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomApisApi apiInstance = new CustomApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiName = "apiName_example"; // String | API name
    String apiVersion = "apiVersion_example"; // String | API Version
    CustomApiDefinition customApi = new CustomApiDefinition(); // CustomApiDefinition | The custom API
    try {
      CustomApiDefinition result = apiInstance.customApisUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApisApi#customApisUpdate");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiName** | **String**| API name | |
| **apiVersion** | **String**| API Version | |
| **customApi** | [**CustomApiDefinition**](CustomApiDefinition.md)| The custom API | |

### Return type

[**CustomApiDefinition**](CustomApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated custom API |  -  |

