# FdaApplicationsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFDAApplication**](FdaApplicationsApi.md#getFDAApplication) | **GET** /fda_applications/{id} |  |
| [**listFDAApplications**](FdaApplicationsApi.md#listFDAApplications) | **GET** /fda_applications |  |


<a id="getFDAApplication"></a>
# **getFDAApplication**
> FDAApplication getFDAApplication(id)



Returns an FDA application details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FdaApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    FdaApplicationsApi apiInstance = new FdaApplicationsApi(defaultClient);
    String id = "id_example"; // String | ID of the FDA application
    try {
      FDAApplication result = apiInstance.getFDAApplication(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FdaApplicationsApi#getFDAApplication");
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
| **id** | **String**| ID of the FDA application | |

### Return type

[**FDAApplication**](FDAApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | FDA application not found |  -  |
| **0** | Error |  -  |

<a id="listFDAApplications"></a>
# **listFDAApplications**
> FDAApplicationList listFDAApplications(page, perPage)



Returns FDA applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FdaApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    FdaApplicationsApi apiInstance = new FdaApplicationsApi(defaultClient);
    Integer page = 1; // Integer | The page number
    Integer perPage = 20; // Integer | Number of items per page
    try {
      FDAApplicationList result = apiInstance.listFDAApplications(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FdaApplicationsApi#listFDAApplications");
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
| **page** | **Integer**| The page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of items per page | [optional] [default to 20] |

### Return type

[**FDAApplicationList**](FDAApplicationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

