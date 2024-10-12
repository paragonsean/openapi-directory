# FilingStatusTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filingStatusTypesGetByCountry**](FilingStatusTypesApi.md#filingStatusTypesGetByCountry) | **GET** /api/FilingStatusTypes |  |
| [**filingStatusTypesGetById**](FilingStatusTypesApi.md#filingStatusTypesGetById) | **GET** /api/FilingStatusTypes/{id} |  |


<a id="filingStatusTypesGetByCountry"></a>
# **filingStatusTypesGetByCountry**
> FilingStatusTypesModel filingStatusTypesGetByCountry(country)



Description: This operation retrieves all Filing Status Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Filing Status Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilingStatusTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FilingStatusTypesApi apiInstance = new FilingStatusTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Filing Status Types
    try {
      FilingStatusTypesModel result = apiInstance.filingStatusTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilingStatusTypesApi#filingStatusTypesGetByCountry");
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
| **country** | **String**| The country used to filter Filing Status Types | [enum: UnitedStates, Canada] |

### Return type

[**FilingStatusTypesModel**](FilingStatusTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **404** | Filing Status Type not found. |  -  |

<a id="filingStatusTypesGetById"></a>
# **filingStatusTypesGetById**
> FilingStatusTypeModel filingStatusTypesGetById(id)



Description: This operation retrieves all Filing Status Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Filing Status Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilingStatusTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FilingStatusTypesApi apiInstance = new FilingStatusTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Filing Status Type used to retreive the Filing Status Type information
    try {
      FilingStatusTypeModel result = apiInstance.filingStatusTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilingStatusTypesApi#filingStatusTypesGetById");
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
| **id** | **Integer**| The ID of Filing Status Type used to retreive the Filing Status Type information | |

### Return type

[**FilingStatusTypeModel**](FilingStatusTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **404** | Filing Status Type not found. |  -  |

