# ExchangersApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exchangersGet**](ExchangersApi.md#exchangersGet) | **GET** /exchangers | List of exchangers |
| [**exchangersIdGet**](ExchangersApi.md#exchangersIdGet) | **GET** /exchangers/{id} | Exchanger by ID |


<a id="exchangersGet"></a>
# **exchangersGet**
> ExchangersResponse exchangersGet(pageNumber, pageSize, filterName, filterStatus, sort)

List of exchangers

Returns list of exchange markets. Each object contains general information about exchanger such as name and status, also information about rates export and related link to main organization.&lt;br&gt; Rates export standards is represented by: * [estandards](http://estandards.info) * [jsons](http://jsons.info) * ratex - our internal standard 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExchangersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    ExchangersApi apiInstance = new ExchangersApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterName = "filterName_example"; // String | Filtering by name.
    Set<String> filterStatus = Arrays.asList(); // Set<String> | Filtration by status.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | <nobr>-rates_export_standard</nobr> | 
    try {
      ExchangersResponse result = apiInstance.exchangersGet(pageNumber, pageSize, filterName, filterStatus, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExchangersApi#exchangersGet");
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
| **pageNumber** | **Integer**| Current page number. | [optional] |
| **pageSize** | **Integer**| Page size.&lt;br&gt;*Default value: 100*  | [optional] |
| **filterName** | **String**| Filtering by name. | [optional] |
| **filterStatus** | [**Set&lt;String&gt;**](String.md)| Filtration by status. | [optional] [enum: active, blocked, deleted] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | &lt;nobr&gt;-rates_export_standard&lt;/nobr&gt; |  | [optional] [enum: name, -name, status, -status, wmid, -wmid, rate_type, -rate_type, rates_export_standard, -rates_export_standard] |

### Return type

[**ExchangersResponse**](ExchangersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of exchangers. |  -  |

<a id="exchangersIdGet"></a>
# **exchangersIdGet**
> ExchangerResponse exchangersIdGet(id)

Exchanger by ID

Returns exchanger with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExchangersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    ExchangersApi apiInstance = new ExchangersApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      ExchangerResponse result = apiInstance.exchangersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExchangersApi#exchangersIdGet");
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
| **id** | **String**| Unique ID. | |

### Return type

[**ExchangerResponse**](ExchangerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exchanger information. |  -  |
| **404** | Exchanger ID is not valid. |  -  |

