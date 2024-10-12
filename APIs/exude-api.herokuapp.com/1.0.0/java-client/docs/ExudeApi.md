# ExudeApi

All URIs are relative to *https://exude-api.herokuapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filterFileDataStoppings**](ExudeApi.md#filterFileDataStoppings) | **POST** /exude/{type}/file | Filter the stopping words from the provided input file |
| [**filterStoppings**](ExudeApi.md#filterStoppings) | **POST** /exude/{type}/data | Filter the stopping words from the provided input data or links |


<a id="filterFileDataStoppings"></a>
# **filterFileDataStoppings**
> ExudeResponseBean filterFileDataStoppings(type, _file)

Filter the stopping words from the provided input file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExudeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://exude-api.herokuapp.com");

    ExudeApi apiInstance = new ExudeApi(defaultClient);
    String type = "type_example"; // String | provide the type of filtering required stopping/swear
    File _file = new File("/path/to/file"); // File | 
    try {
      ExudeResponseBean result = apiInstance.filterFileDataStoppings(type, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExudeApi#filterFileDataStoppings");
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
| **type** | **String**| provide the type of filtering required stopping/swear | |
| **_file** | **File**|  | [optional] |

### Return type

[**ExudeResponseBean**](ExudeResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | model response |  -  |

<a id="filterStoppings"></a>
# **filterStoppings**
> ExudeResponseBean filterStoppings(type, data, links)

Filter the stopping words from the provided input data or links

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExudeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://exude-api.herokuapp.com");

    ExudeApi apiInstance = new ExudeApi(defaultClient);
    String type = "stopping"; // String | provide the type of filtering required stopping/swear
    String data = "data_example"; // String | 
    List<String> links = Arrays.asList(); // List<String> | 
    try {
      ExudeResponseBean result = apiInstance.filterStoppings(type, data, links);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExudeApi#filterStoppings");
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
| **type** | **String**| provide the type of filtering required stopping/swear | |
| **data** | **String**|  | [optional] |
| **links** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**ExudeResponseBean**](ExudeResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exude response |  -  |

