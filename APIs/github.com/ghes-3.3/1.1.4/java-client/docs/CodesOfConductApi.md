# CodesOfConductApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**codesOfConductGetAllCodesOfConduct**](CodesOfConductApi.md#codesOfConductGetAllCodesOfConduct) | **GET** /codes_of_conduct | Get all codes of conduct |
| [**codesOfConductGetConductCode**](CodesOfConductApi.md#codesOfConductGetConductCode) | **GET** /codes_of_conduct/{key} | Get a code of conduct |


<a id="codesOfConductGetAllCodesOfConduct"></a>
# **codesOfConductGetAllCodesOfConduct**
> List&lt;CodeOfConduct&gt; codesOfConductGetAllCodesOfConduct()

Get all codes of conduct



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodesOfConductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    CodesOfConductApi apiInstance = new CodesOfConductApi(defaultClient);
    try {
      List<CodeOfConduct> result = apiInstance.codesOfConductGetAllCodesOfConduct();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodesOfConductApi#codesOfConductGetAllCodesOfConduct");
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

[**List&lt;CodeOfConduct&gt;**](CodeOfConduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |

<a id="codesOfConductGetConductCode"></a>
# **codesOfConductGetConductCode**
> CodeOfConduct codesOfConductGetConductCode(key)

Get a code of conduct



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodesOfConductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    CodesOfConductApi apiInstance = new CodesOfConductApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      CodeOfConduct result = apiInstance.codesOfConductGetConductCode(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodesOfConductApi#codesOfConductGetConductCode");
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
| **key** | **String**|  | |

### Return type

[**CodeOfConduct**](CodeOfConduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **404** | Resource not found |  -  |

