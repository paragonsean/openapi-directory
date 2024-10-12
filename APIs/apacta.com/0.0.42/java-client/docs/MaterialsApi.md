# MaterialsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**materialsGet**](MaterialsApi.md#materialsGet) | **GET** /materials | View list of all materials |
| [**materialsMaterialIdDelete**](MaterialsApi.md#materialsMaterialIdDelete) | **DELETE** /materials/{material_id} | Delete material |
| [**materialsMaterialIdGet**](MaterialsApi.md#materialsMaterialIdGet) | **GET** /materials/{material_id} | View material |
| [**materialsMaterialIdPut**](MaterialsApi.md#materialsMaterialIdPut) | **PUT** /materials/{material_id} | Edit material |
| [**materialsPost**](MaterialsApi.md#materialsPost) | **POST** /materials | Add material |


<a id="materialsGet"></a>
# **materialsGet**
> MaterialsGet200Response materialsGet(barcode, name, projectId, currentlyRented)

View list of all materials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialsApi apiInstance = new MaterialsApi(defaultClient);
    String barcode = "barcode_example"; // String | Used to filter on the `barcode` of the materials
    String name = "name_example"; // String | Used to filter on the `name` of the materials
    UUID projectId = UUID.randomUUID(); // UUID | Used to find materials used in specific project by `project_id`
    Boolean currentlyRented = true; // Boolean | Used to find currently rented materials
    try {
      MaterialsGet200Response result = apiInstance.materialsGet(barcode, name, projectId, currentlyRented);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialsApi#materialsGet");
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
| **barcode** | **String**| Used to filter on the &#x60;barcode&#x60; of the materials | [optional] |
| **name** | **String**| Used to filter on the &#x60;name&#x60; of the materials | [optional] |
| **projectId** | **UUID**| Used to find materials used in specific project by &#x60;project_id&#x60; | [optional] |
| **currentlyRented** | **Boolean**| Used to find currently rented materials | [optional] |

### Return type

[**MaterialsGet200Response**](MaterialsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsMaterialIdDelete"></a>
# **materialsMaterialIdDelete**
> ClockingRecordsClockingRecordIdPut200Response materialsMaterialIdDelete(materialId)

Delete material

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialsApi apiInstance = new MaterialsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.materialsMaterialIdDelete(materialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialsApi#materialsMaterialIdDelete");
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
| **materialId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsMaterialIdGet"></a>
# **materialsMaterialIdGet**
> MaterialsMaterialIdGet200Response materialsMaterialIdGet(materialId)

View material

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialsApi apiInstance = new MaterialsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    try {
      MaterialsMaterialIdGet200Response result = apiInstance.materialsMaterialIdGet(materialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialsApi#materialsMaterialIdGet");
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
| **materialId** | **String**|  | |

### Return type

[**MaterialsMaterialIdGet200Response**](MaterialsMaterialIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsMaterialIdPut"></a>
# **materialsMaterialIdPut**
> ClockingRecordsClockingRecordIdPut200Response materialsMaterialIdPut(materialId)

Edit material

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialsApi apiInstance = new MaterialsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.materialsMaterialIdPut(materialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialsApi#materialsMaterialIdPut");
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
| **materialId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsPost"></a>
# **materialsPost**
> ClockingRecordsPost201Response materialsPost(materialsPostRequest)

Add material

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialsApi apiInstance = new MaterialsApi(defaultClient);
    MaterialsPostRequest materialsPostRequest = new MaterialsPostRequest(); // MaterialsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.materialsPost(materialsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialsApi#materialsPost");
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
| **materialsPostRequest** | [**MaterialsPostRequest**](MaterialsPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

