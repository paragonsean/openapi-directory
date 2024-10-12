# DataTypeApi

All URIs are relative to *https://cenit.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupDataTypeGet**](DataTypeApi.md#setupDataTypeGet) | **GET** /setup/data_type/ | Returns a list of data types |
| [**setupDataTypeIdDelete**](DataTypeApi.md#setupDataTypeIdDelete) | **DELETE** /setup/data_type/{id} | Delete a data type |
| [**setupDataTypeIdGet**](DataTypeApi.md#setupDataTypeIdGet) | **GET** /setup/data_type/{id} | Retrieve a data type |
| [**setupDataTypePost**](DataTypeApi.md#setupDataTypePost) | **POST** /setup/data_type/ | Create or update a data type |


<a id="setupDataTypeGet"></a>
# **setupDataTypeGet**
> List&lt;DataType&gt; setupDataTypeGet()

Returns a list of data types

Returns a list of data types you&#39;ve previously created. The data types are returned in sorted order, with the most recent DataType appearing first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    DataTypeApi apiInstance = new DataTypeApi(defaultClient);
    try {
      List<DataType> result = apiInstance.setupDataTypeGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataTypeApi#setupDataTypeGet");
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

[**List&lt;DataType&gt;**](DataType.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="setupDataTypeIdDelete"></a>
# **setupDataTypeIdDelete**
> setupDataTypeIdDelete(id)

Delete a data type

Deletes the specified data type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    DataTypeApi apiInstance = new DataTypeApi(defaultClient);
    String id = "id_example"; // String | data type ID
    try {
      apiInstance.setupDataTypeIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataTypeApi#setupDataTypeIdDelete");
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
| **id** | **String**| data type ID | |

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Item not found |  -  |

<a id="setupDataTypeIdGet"></a>
# **setupDataTypeIdGet**
> DataType setupDataTypeIdGet(id)

Retrieve a data type

Retrieves the details of an existing data type. You need only supply the unique data  type identifier that was returned upon DataType creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    DataTypeApi apiInstance = new DataTypeApi(defaultClient);
    String id = "id_example"; // String | data type ID
    try {
      DataType result = apiInstance.setupDataTypeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataTypeApi#setupDataTypeIdGet");
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
| **id** | **String**| data type ID | |

### Return type

[**DataType**](DataType.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Item not found. |  -  |

<a id="setupDataTypePost"></a>
# **setupDataTypePost**
> DataType setupDataTypePost()

Create or update a data type

Creates or updates the specified data type by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    DataTypeApi apiInstance = new DataTypeApi(defaultClient);
    try {
      DataType result = apiInstance.setupDataTypePost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataTypeApi#setupDataTypePost");
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

[**DataType**](DataType.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

