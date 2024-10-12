# DefaultApi

All URIs are relative to *https://api.deutschebahn.com/betriebsstellen/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betriebsstellenAbbrevGet**](DefaultApi.md#betriebsstellenAbbrevGet) | **GET** /betriebsstellen/{abbrev} | Get information about a specific station or stop by abbrevation |
| [**betriebsstellenGet**](DefaultApi.md#betriebsstellenGet) | **GET** /betriebsstellen | Get information of stations matching a given text |


<a id="betriebsstellenAbbrevGet"></a>
# **betriebsstellenAbbrevGet**
> Station betriebsstellenAbbrevGet(abbrev)

Get information about a specific station or stop by abbrevation

Get information about a specific station or stop by abbrevation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/betriebsstellen/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String abbrev = "abbrev_example"; // String | Station or stop abbrevation
    try {
      Station result = apiInstance.betriebsstellenAbbrevGet(abbrev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#betriebsstellenAbbrevGet");
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
| **abbrev** | **String**| Station or stop abbrevation | |

### Return type

[**Station**](Station.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Entry found |  -  |
| **404** | Entry not found |  -  |

<a id="betriebsstellenGet"></a>
# **betriebsstellenGet**
> List&lt;Station&gt; betriebsstellenGet(name)

Get information of stations matching a given text

Get all station and stop infos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/betriebsstellen/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | A station name or part of it
    try {
      List<Station> result = apiInstance.betriebsstellenGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#betriebsstellenGet");
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
| **name** | **String**| A station name or part of it | [optional] |

### Return type

[**List&lt;Station&gt;**](Station.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List was generated |  -  |
| **404** | No stations or stops could be found matching the given name |  -  |
| **416** | Filtering required - specify a name fragment of at least 3 characters |  -  |

