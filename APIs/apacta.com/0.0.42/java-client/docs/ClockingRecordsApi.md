# ClockingRecordsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clockingRecordsCheckoutPost**](ClockingRecordsApi.md#clockingRecordsCheckoutPost) | **POST** /clocking_records/checkout | Checkout active clocking record for authenticated user |
| [**clockingRecordsClockingRecordIdDelete**](ClockingRecordsApi.md#clockingRecordsClockingRecordIdDelete) | **DELETE** /clocking_records/{clocking_record_id} | Delete a clocking record |
| [**clockingRecordsClockingRecordIdGet**](ClockingRecordsApi.md#clockingRecordsClockingRecordIdGet) | **GET** /clocking_records/{clocking_record_id} | Details of 1 clocking_record |
| [**clockingRecordsClockingRecordIdPut**](ClockingRecordsApi.md#clockingRecordsClockingRecordIdPut) | **PUT** /clocking_records/{clocking_record_id} | Edit a clocking record |
| [**clockingRecordsGet**](ClockingRecordsApi.md#clockingRecordsGet) | **GET** /clocking_records | Get a list of clocking records |
| [**clockingRecordsPost**](ClockingRecordsApi.md#clockingRecordsPost) | **POST** /clocking_records | Create clocking record for authenticated user |


<a id="clockingRecordsCheckoutPost"></a>
# **clockingRecordsCheckoutPost**
> ClockingRecordsCheckoutPost201Response clockingRecordsCheckoutPost()

Checkout active clocking record for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClockingRecordsApi;

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

    ClockingRecordsApi apiInstance = new ClockingRecordsApi(defaultClient);
    try {
      ClockingRecordsCheckoutPost201Response result = apiInstance.clockingRecordsCheckoutPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClockingRecordsApi#clockingRecordsCheckoutPost");
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

[**ClockingRecordsCheckoutPost201Response**](ClockingRecordsCheckoutPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully checked out |  -  |
| **422** | Validation error |  -  |

<a id="clockingRecordsClockingRecordIdDelete"></a>
# **clockingRecordsClockingRecordIdDelete**
> ClockingRecordsClockingRecordIdDelete200Response clockingRecordsClockingRecordIdDelete(clockingRecordId)

Delete a clocking record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClockingRecordsApi;

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

    ClockingRecordsApi apiInstance = new ClockingRecordsApi(defaultClient);
    String clockingRecordId = "clockingRecordId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdDelete200Response result = apiInstance.clockingRecordsClockingRecordIdDelete(clockingRecordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClockingRecordsApi#clockingRecordsClockingRecordIdDelete");
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
| **clockingRecordId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="clockingRecordsClockingRecordIdGet"></a>
# **clockingRecordsClockingRecordIdGet**
> ClockingRecordsClockingRecordIdGet200Response clockingRecordsClockingRecordIdGet(clockingRecordId)

Details of 1 clocking_record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClockingRecordsApi;

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

    ClockingRecordsApi apiInstance = new ClockingRecordsApi(defaultClient);
    String clockingRecordId = "clockingRecordId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdGet200Response result = apiInstance.clockingRecordsClockingRecordIdGet(clockingRecordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClockingRecordsApi#clockingRecordsClockingRecordIdGet");
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
| **clockingRecordId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdGet200Response**](ClockingRecordsClockingRecordIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Clocking record not found |  -  |

<a id="clockingRecordsClockingRecordIdPut"></a>
# **clockingRecordsClockingRecordIdPut**
> ClockingRecordsClockingRecordIdPut200Response clockingRecordsClockingRecordIdPut(clockingRecordId)

Edit a clocking record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClockingRecordsApi;

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

    ClockingRecordsApi apiInstance = new ClockingRecordsApi(defaultClient);
    String clockingRecordId = "clockingRecordId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.clockingRecordsClockingRecordIdPut(clockingRecordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClockingRecordsApi#clockingRecordsClockingRecordIdPut");
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
| **clockingRecordId** | **String**|  | |

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

<a id="clockingRecordsGet"></a>
# **clockingRecordsGet**
> ClockingRecordsGet200Response clockingRecordsGet(active)

Get a list of clocking records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClockingRecordsApi;

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

    ClockingRecordsApi apiInstance = new ClockingRecordsApi(defaultClient);
    Boolean active = true; // Boolean | Used to search for active clocking records
    try {
      ClockingRecordsGet200Response result = apiInstance.clockingRecordsGet(active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClockingRecordsApi#clockingRecordsGet");
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
| **active** | **Boolean**| Used to search for active clocking records | [optional] |

### Return type

[**ClockingRecordsGet200Response**](ClockingRecordsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="clockingRecordsPost"></a>
# **clockingRecordsPost**
> ClockingRecordsPost201Response clockingRecordsPost(clockingRecordsPostRequest)

Create clocking record for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClockingRecordsApi;

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

    ClockingRecordsApi apiInstance = new ClockingRecordsApi(defaultClient);
    ClockingRecordsPostRequest clockingRecordsPostRequest = new ClockingRecordsPostRequest(); // ClockingRecordsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.clockingRecordsPost(clockingRecordsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClockingRecordsApi#clockingRecordsPost");
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
| **clockingRecordsPostRequest** | [**ClockingRecordsPostRequest**](ClockingRecordsPostRequest.md)|  | |

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
| **201** | Successfully added clocking record |  -  |
| **422** | Validation error |  -  |

