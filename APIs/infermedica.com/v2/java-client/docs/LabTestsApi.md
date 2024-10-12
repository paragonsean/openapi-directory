# LabTestsApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllLabTests**](LabTestsApi.md#getAllLabTests) | **GET** /lab_tests | List all lab tests |
| [**getLabTest**](LabTestsApi.md#getLabTest) | **GET** /lab_tests/{id} | Get lab test by id |


<a id="getAllLabTests"></a>
# **getAllLabTests**
> List&lt;LabTestPublic&gt; getAllLabTests(ageValue, ageUnit)

List all lab tests

Returns a list of all available lab tests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabTestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    LabTestsApi apiInstance = new LabTestsApi(defaultClient);
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    try {
      List<LabTestPublic> result = apiInstance.getAllLabTests(ageValue, ageUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabTestsApi#getAllLabTests");
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
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |

### Return type

[**List&lt;LabTestPublic&gt;**](LabTestPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLabTest"></a>
# **getLabTest**
> LabTestDetails getLabTest(id, ageValue, ageUnit)

Get lab test by id

Returns details of a single lab test specified by id parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabTestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    LabTestsApi apiInstance = new LabTestsApi(defaultClient);
    String id = "id_example"; // String | lab test id
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    try {
      LabTestDetails result = apiInstance.getLabTest(id, ageValue, ageUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabTestsApi#getLabTest");
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
| **id** | **String**| lab test id | |
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |

### Return type

[**LabTestDetails**](LabTestDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid id specified |  -  |
| **404** | Lab test not found |  -  |

