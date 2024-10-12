# BanksApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**banksGet**](BanksApi.md#banksGet) | **GET** /banks | List of banks |
| [**banksIdGet**](BanksApi.md#banksIdGet) | **GET** /banks/{id} | Bank by ID |


<a id="banksGet"></a>
# **banksGet**
> BanksResponse banksGet(pageNumber, pageSize, filterSortCode, filterCode, filterStatus, sort)

List of banks

Returns list of banks. Each object contains general information about bank such as name and status, also information about bank details and related link to main organization. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BanksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    BanksApi apiInstance = new BanksApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSortCode = "filterSortCode_example"; // String | Filtering by banks code.
    String filterCode = "filterCode_example"; // String | Filtering by code.
    Set<String> filterStatus = Arrays.asList(); // Set<String> | Filtration by status.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code | 
    try {
      BanksResponse result = apiInstance.banksGet(pageNumber, pageSize, filterSortCode, filterCode, filterStatus, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BanksApi#banksGet");
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
| **filterSortCode** | **String**| Filtering by banks code. | [optional] |
| **filterCode** | **String**| Filtering by code. | [optional] |
| **filterStatus** | [**Set&lt;String&gt;**](String.md)| Filtration by status. | [optional] [enum: active, liquidated, problem, deleted] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code |  | [optional] [enum: name, -name, status, -status, code, -code, sort_code, -sort_code] |

### Return type

[**BanksResponse**](BanksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of banks. |  -  |

<a id="banksIdGet"></a>
# **banksIdGet**
> BankResponse banksIdGet(id)

Bank by ID

Returns bank with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BanksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    BanksApi apiInstance = new BanksApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      BankResponse result = apiInstance.banksIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BanksApi#banksIdGet");
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

[**BankResponse**](BankResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank information. |  -  |
| **404** | Bank ID is not valid. |  -  |

