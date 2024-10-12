# DrivingTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkDeleteDrivingTypes**](DrivingTypesApi.md#bulkDeleteDrivingTypes) | **DELETE** /driving_types/bulkDelete | Bulk delete driving types |
| [**deleteDrivingTypesDrivingTypeId**](DrivingTypesApi.md#deleteDrivingTypesDrivingTypeId) | **DELETE** /driving_types/{driving_type_id} | Delete driving type |
| [**getDrivingTypes**](DrivingTypesApi.md#getDrivingTypes) | **GET** /driving_types | List the driving types of the company |
| [**getDrivingTypesDrivingTypeId**](DrivingTypesApi.md#getDrivingTypesDrivingTypeId) | **GET** /driving_types/{driving_type_id} | View driving type |
| [**postDrivingTypes**](DrivingTypesApi.md#postDrivingTypes) | **POST** /driving_types | Create driving type |
| [**putDrivingTypesDrivingTypeId**](DrivingTypesApi.md#putDrivingTypesDrivingTypeId) | **PUT** /driving_types/{driving_type_id} | Edit driving type |


<a id="bulkDeleteDrivingTypes"></a>
# **bulkDeleteDrivingTypes**
> EmptySuccessResponse bulkDeleteDrivingTypes(bulkActionRequestBody)

Bulk delete driving types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivingTypesApi;

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

    DrivingTypesApi apiInstance = new DrivingTypesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Driving types ids
    try {
      EmptySuccessResponse result = apiInstance.bulkDeleteDrivingTypes(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivingTypesApi#bulkDeleteDrivingTypes");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Driving types ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="deleteDrivingTypesDrivingTypeId"></a>
# **deleteDrivingTypesDrivingTypeId**
> EmptySuccessResponse deleteDrivingTypesDrivingTypeId(drivingTypeId)

Delete driving type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivingTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    DrivingTypesApi apiInstance = new DrivingTypesApi(defaultClient);
    String drivingTypeId = "drivingTypeId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.deleteDrivingTypesDrivingTypeId(drivingTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivingTypesApi#deleteDrivingTypesDrivingTypeId");
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
| **drivingTypeId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="getDrivingTypes"></a>
# **getDrivingTypes**
> GetDrivingTypes200Response getDrivingTypes(q, sort, direction)

List the driving types of the company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivingTypesApi;

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

    DrivingTypesApi apiInstance = new DrivingTypesApi(defaultClient);
    String q = "q_example"; // String | 
    String sort = "sort_example"; // String | 
    String direction = "direction_example"; // String | 
    try {
      GetDrivingTypes200Response result = apiInstance.getDrivingTypes(q, sort, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivingTypesApi#getDrivingTypes");
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
| **q** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] |

### Return type

[**GetDrivingTypes200Response**](GetDrivingTypes200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getDrivingTypesDrivingTypeId"></a>
# **getDrivingTypesDrivingTypeId**
> DrivingType getDrivingTypesDrivingTypeId(drivingTypeId, drivingTypeId2)

View driving type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivingTypesApi;

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

    DrivingTypesApi apiInstance = new DrivingTypesApi(defaultClient);
    String drivingTypeId = "drivingTypeId_example"; // String | 
    String drivingTypeId2 = "drivingTypeId_example"; // String | 
    try {
      DrivingType result = apiInstance.getDrivingTypesDrivingTypeId(drivingTypeId, drivingTypeId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivingTypesApi#getDrivingTypesDrivingTypeId");
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
| **drivingTypeId** | **String**|  | |
| **drivingTypeId2** | **String**|  | |

### Return type

[**DrivingType**](DrivingType.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="postDrivingTypes"></a>
# **postDrivingTypes**
> CreateSuccessResponse postDrivingTypes(postDrivingTypesRequest)

Create driving type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivingTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    DrivingTypesApi apiInstance = new DrivingTypesApi(defaultClient);
    PostDrivingTypesRequest postDrivingTypesRequest = new PostDrivingTypesRequest(); // PostDrivingTypesRequest | 
    try {
      CreateSuccessResponse result = apiInstance.postDrivingTypes(postDrivingTypesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivingTypesApi#postDrivingTypes");
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
| **postDrivingTypesRequest** | [**PostDrivingTypesRequest**](PostDrivingTypesRequest.md)|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | Validation error |  -  |

<a id="putDrivingTypesDrivingTypeId"></a>
# **putDrivingTypesDrivingTypeId**
> DrivingType putDrivingTypesDrivingTypeId(drivingTypeId)

Edit driving type



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivingTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    DrivingTypesApi apiInstance = new DrivingTypesApi(defaultClient);
    String drivingTypeId = "drivingTypeId_example"; // String | 
    try {
      DrivingType result = apiInstance.putDrivingTypesDrivingTypeId(drivingTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivingTypesApi#putDrivingTypesDrivingTypeId");
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
| **drivingTypeId** | **String**|  | |

### Return type

[**DrivingType**](DrivingType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | Validation error |  -  |

