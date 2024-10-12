# ProposedNegativeStatutoryInstrumentApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBusinessItemsByProposedNegativeStatutoryInstrumentId**](ProposedNegativeStatutoryInstrumentApi.md#getBusinessItemsByProposedNegativeStatutoryInstrumentId) | **GET** /api/v1/ProposedNegativeStatutoryInstrument/{id}/BusinessItems | Returns business items belonging to a proposed negative statutory instrument. |
| [**getProposedNegativeStatutoryInstrumentById**](ProposedNegativeStatutoryInstrumentApi.md#getProposedNegativeStatutoryInstrumentById) | **GET** /api/v1/ProposedNegativeStatutoryInstrument/{id} | Returns proposed negative statutory instrument by ID. |
| [**getProposedNegativeStatutoryInstruments**](ProposedNegativeStatutoryInstrumentApi.md#getProposedNegativeStatutoryInstruments) | **GET** /api/v1/ProposedNegativeStatutoryInstrument | Returns a list of proposed negative statutory instruments. |


<a id="getBusinessItemsByProposedNegativeStatutoryInstrumentId"></a>
# **getBusinessItemsByProposedNegativeStatutoryInstrumentId**
> BusinessItemResourceCollection getBusinessItemsByProposedNegativeStatutoryInstrumentId(id)

Returns business items belonging to a proposed negative statutory instrument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProposedNegativeStatutoryInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProposedNegativeStatutoryInstrumentApi apiInstance = new ProposedNegativeStatutoryInstrumentApi(defaultClient);
    String id = "id_example"; // String | Business items belonging to proposed negative statutory instrument with the ID specified
    try {
      BusinessItemResourceCollection result = apiInstance.getBusinessItemsByProposedNegativeStatutoryInstrumentId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProposedNegativeStatutoryInstrumentApi#getBusinessItemsByProposedNegativeStatutoryInstrumentId");
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
| **id** | **String**| Business items belonging to proposed negative statutory instrument with the ID specified | |

### Return type

[**BusinessItemResourceCollection**](BusinessItemResourceCollection.md)

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

<a id="getProposedNegativeStatutoryInstrumentById"></a>
# **getProposedNegativeStatutoryInstrumentById**
> ProposedNegativeStatutoryInstrumentResource getProposedNegativeStatutoryInstrumentById(id)

Returns proposed negative statutory instrument by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProposedNegativeStatutoryInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProposedNegativeStatutoryInstrumentApi apiInstance = new ProposedNegativeStatutoryInstrumentApi(defaultClient);
    String id = "id_example"; // String | Proposed negative statutory instrument with the ID specified
    try {
      ProposedNegativeStatutoryInstrumentResource result = apiInstance.getProposedNegativeStatutoryInstrumentById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProposedNegativeStatutoryInstrumentApi#getProposedNegativeStatutoryInstrumentById");
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
| **id** | **String**| Proposed negative statutory instrument with the ID specified | |

### Return type

[**ProposedNegativeStatutoryInstrumentResource**](ProposedNegativeStatutoryInstrumentResource.md)

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

<a id="getProposedNegativeStatutoryInstruments"></a>
# **getProposedNegativeStatutoryInstruments**
> ProposedNegativeStatutoryInstrumentResourceCollection getProposedNegativeStatutoryInstruments(name, recommendedForProcedureChange, departmentId, layingBodyId, skip, take)

Returns a list of proposed negative statutory instruments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProposedNegativeStatutoryInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProposedNegativeStatutoryInstrumentApi apiInstance = new ProposedNegativeStatutoryInstrumentApi(defaultClient);
    String name = "name_example"; // String | Proposed negative statutory instruments with the name provided
    Boolean recommendedForProcedureChange = true; // Boolean | Proposed negative statutory instruments recommended for procedure change
    Integer departmentId = 56; // Integer | Proposed negative statutory instruments with the department ID specified
    String layingBodyId = "layingBodyId_example"; // String | Proposed negative statutory instruments with the laying body ID specified
    Integer skip = 56; // Integer | The number of records to skip from the first, default is 0
    Integer take = 56; // Integer | The number of records to return, default is 20
    try {
      ProposedNegativeStatutoryInstrumentResourceCollection result = apiInstance.getProposedNegativeStatutoryInstruments(name, recommendedForProcedureChange, departmentId, layingBodyId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProposedNegativeStatutoryInstrumentApi#getProposedNegativeStatutoryInstruments");
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
| **name** | **String**| Proposed negative statutory instruments with the name provided | [optional] |
| **recommendedForProcedureChange** | **Boolean**| Proposed negative statutory instruments recommended for procedure change | [optional] |
| **departmentId** | **Integer**| Proposed negative statutory instruments with the department ID specified | [optional] |
| **layingBodyId** | **String**| Proposed negative statutory instruments with the laying body ID specified | [optional] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0 | [optional] |
| **take** | **Integer**| The number of records to return, default is 20 | [optional] |

### Return type

[**ProposedNegativeStatutoryInstrumentResourceCollection**](ProposedNegativeStatutoryInstrumentResourceCollection.md)

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

