# PackageTypesApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPackageType**](PackageTypesApi.md#createPackageType) | **POST** /v1/packages | Create Custom Package Type |
| [**deletePackageType**](PackageTypesApi.md#deletePackageType) | **DELETE** /v1/packages/{package_id} | Delete A Custom Package By ID |
| [**getPackageTypeById**](PackageTypesApi.md#getPackageTypeById) | **GET** /v1/packages/{package_id} | Get Custom Package Type By ID |
| [**listPackageTypes**](PackageTypesApi.md#listPackageTypes) | **GET** /v1/packages | List Custom Package Types |
| [**updatePackageType**](PackageTypesApi.md#updatePackageType) | **PUT** /v1/packages/{package_id} | Update Custom Package Type By ID |


<a id="createPackageType"></a>
# **createPackageType**
> CreatePackageTypeResponseBody createPackageType(createPackageTypeRequestBody)

Create Custom Package Type

Create a custom package type to better assist in getting accurate rate estimates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    CreatePackageTypeRequestBody createPackageTypeRequestBody = new CreatePackageTypeRequestBody(); // CreatePackageTypeRequestBody | 
    try {
      CreatePackageTypeResponseBody result = apiInstance.createPackageType(createPackageTypeRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#createPackageType");
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
| **createPackageTypeRequestBody** | [**CreatePackageTypeRequestBody**](CreatePackageTypeRequestBody.md)|  | |

### Return type

[**CreatePackageTypeResponseBody**](CreatePackageTypeResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="deletePackageType"></a>
# **deletePackageType**
> String deletePackageType(packageId)

Delete A Custom Package By ID

Delete a custom package using the ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String packageId = "packageId_example"; // String | Package ID
    try {
      String result = apiInstance.deletePackageType(packageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#deletePackageType");
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
| **packageId** | **String**| Package ID | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getPackageTypeById"></a>
# **getPackageTypeById**
> GetPackageTypeByIdResponseBody getPackageTypeById(packageId)

Get Custom Package Type By ID

Get Custom Package Type by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String packageId = "packageId_example"; // String | Package ID
    try {
      GetPackageTypeByIdResponseBody result = apiInstance.getPackageTypeById(packageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#getPackageTypeById");
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
| **packageId** | **String**| Package ID | |

### Return type

[**GetPackageTypeByIdResponseBody**](GetPackageTypeByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listPackageTypes"></a>
# **listPackageTypes**
> ListPackageTypesResponseBody listPackageTypes()

List Custom Package Types

List the custom package types associated with the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    try {
      ListPackageTypesResponseBody result = apiInstance.listPackageTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#listPackageTypes");
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

[**ListPackageTypesResponseBody**](ListPackageTypesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="updatePackageType"></a>
# **updatePackageType**
> String updatePackageType(packageId, updatePackageTypeRequestBody)

Update Custom Package Type By ID

Update the custom package type object by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String packageId = "packageId_example"; // String | Package ID
    UpdatePackageTypeRequestBody updatePackageTypeRequestBody = new UpdatePackageTypeRequestBody(); // UpdatePackageTypeRequestBody | 
    try {
      String result = apiInstance.updatePackageType(packageId, updatePackageTypeRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#updatePackageType");
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
| **packageId** | **String**| Package ID | |
| **updatePackageTypeRequestBody** | [**UpdatePackageTypeRequestBody**](UpdatePackageTypeRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

