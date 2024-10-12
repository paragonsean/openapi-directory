# ProcedureApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProceduresByIdV1**](ProcedureApi.md#getProceduresByIdV1) | **GET** /api/v1/Procedure/{id} | Returns procedure by ID. |
| [**getProceduresV1**](ProcedureApi.md#getProceduresV1) | **GET** /api/v1/Procedure | Returns all procedures. |


<a id="getProceduresByIdV1"></a>
# **getProceduresByIdV1**
> ProcedureDetailsResource getProceduresByIdV1(id)

Returns procedure by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcedureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProcedureApi apiInstance = new ProcedureApi(defaultClient);
    String id = "id_example"; // String | Procedure with the ID specified
    try {
      ProcedureDetailsResource result = apiInstance.getProceduresByIdV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcedureApi#getProceduresByIdV1");
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
| **id** | **String**| Procedure with the ID specified | |

### Return type

[**ProcedureDetailsResource**](ProcedureDetailsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="getProceduresV1"></a>
# **getProceduresV1**
> ProcedureResourceCollection getProceduresV1()

Returns all procedures.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcedureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProcedureApi apiInstance = new ProcedureApi(defaultClient);
    try {
      ProcedureResourceCollection result = apiInstance.getProceduresV1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcedureApi#getProceduresV1");
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

[**ProcedureResourceCollection**](ProcedureResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

