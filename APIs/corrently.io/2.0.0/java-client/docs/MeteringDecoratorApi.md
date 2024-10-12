# MeteringDecoratorApi

All URIs are relative to *https://api.corrently.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meteringGet**](MeteringDecoratorApi.md#meteringGet) | **GET** /metering/reading | Meter Reading |
| [**meteringPost**](MeteringDecoratorApi.md#meteringPost) | **POST** /metering/reading | Meter Reading |


<a id="meteringGet"></a>
# **meteringGet**
> MeteringGet200Response meteringGet(account)

Meter Reading

Retrieves a metered reading using account (Stromkonto). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeteringDecoratorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    MeteringDecoratorApi apiInstance = new MeteringDecoratorApi(defaultClient);
    String account = "account_example"; // String | Account/Address (Stromkonto) to retrieve reading for.
    try {
      MeteringGet200Response result = apiInstance.meteringGet(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeteringDecoratorApi#meteringGet");
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
| **account** | **String**| Account/Address (Stromkonto) to retrieve reading for. | [optional] |

### Return type

[**MeteringGet200Response**](MeteringGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="meteringPost"></a>
# **meteringPost**
> MeteringPost200Response meteringPost(meteringPostRequest)

Meter Reading

Post meter reading and get it decorated. Best practice is to first create a new Stromkonto with the register method and choose a nice secret to protect updates. Now regularly send updates to get readings (consumption) split into green power (1.8.1) and grey power (1.8.2). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeteringDecoratorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    MeteringDecoratorApi apiInstance = new MeteringDecoratorApi(defaultClient);
    MeteringPostRequest meteringPostRequest = new MeteringPostRequest(); // MeteringPostRequest | 
    try {
      MeteringPost200Response result = apiInstance.meteringPost(meteringPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeteringDecoratorApi#meteringPost");
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
| **meteringPostRequest** | [**MeteringPostRequest**](MeteringPostRequest.md)|  | |

### Return type

[**MeteringPost200Response**](MeteringPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

