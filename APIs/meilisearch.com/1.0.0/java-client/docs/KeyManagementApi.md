# KeyManagementApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAKey**](KeyManagementApi.md#createAKey) | **POST** /keys | Create a key |
| [**deleteAKey**](KeyManagementApi.md#deleteAKey) | **DELETE** /keys/kN2aK9EO8a7b627e425717d9196c8081552ca004e513545ed178f8a56981dbd3080d4a5b | Delete a key |
| [**getKeys**](KeyManagementApi.md#getKeys) | **GET** /keys | Get keys |
| [**getOneKey**](KeyManagementApi.md#getOneKey) | **GET** /keys/L8l05tFb188aab693735bbaf1f898b9902fb39f865160d39dddba2b47b940115a0430705 | Get one key |
| [**updateAKey**](KeyManagementApi.md#updateAKey) | **PATCH** /keys/wYZjGJyBcdb0621b97999c233246a8ec0a35d0fcd9a6417ef8ccee0c8978b64b123af2dd | Update a key |


<a id="createAKey"></a>
# **createAKey**
> createAKey(createAKeyRequest)

Create a key

Create a key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);
    CreateAKeyRequest createAKeyRequest = new CreateAKeyRequest(); // CreateAKeyRequest | 
    try {
      apiInstance.createAKey(createAKeyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#createAKey");
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
| **createAKeyRequest** | [**CreateAKeyRequest**](CreateAKeyRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteAKey"></a>
# **deleteAKey**
> deleteAKey()

Delete a key

Delete a key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);
    try {
      apiInstance.deleteAKey();
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#deleteAKey");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getKeys"></a>
# **getKeys**
> getKeys(offset, limit)

Get keys

Get keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);
    String offset = "0"; // String | 
    String limit = "10"; // String | 
    try {
      apiInstance.getKeys(offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getKeys");
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
| **offset** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getOneKey"></a>
# **getOneKey**
> getOneKey()

Get one key

Get one key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);
    try {
      apiInstance.getOneKey();
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#getOneKey");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateAKey"></a>
# **updateAKey**
> updateAKey(updateAKeyRequest)

Update a key

Update a key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    KeyManagementApi apiInstance = new KeyManagementApi(defaultClient);
    UpdateAKeyRequest updateAKeyRequest = new UpdateAKeyRequest(); // UpdateAKeyRequest | 
    try {
      apiInstance.updateAKey(updateAKeyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyManagementApi#updateAKey");
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
| **updateAKeyRequest** | [**UpdateAKeyRequest**](UpdateAKeyRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

