# IncomeTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**incomeTypesGetByCountry**](IncomeTypesApi.md#incomeTypesGetByCountry) | **GET** /api/IncomeTypes |  |
| [**incomeTypesGetById**](IncomeTypesApi.md#incomeTypesGetById) | **GET** /api/IncomeTypes/{id} |  |


<a id="incomeTypesGetByCountry"></a>
# **incomeTypesGetByCountry**
> IncomeTypesModel incomeTypesGetByCountry(country)



Description: This operation retrieves all Income Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Income Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomeTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomeTypesApi apiInstance = new IncomeTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Income Types
    try {
      IncomeTypesModel result = apiInstance.incomeTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomeTypesApi#incomeTypesGetByCountry");
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
| **country** | **String**| The country used to filter Income Types | [enum: UnitedStates, Canada] |

### Return type

[**IncomeTypesModel**](IncomeTypesModel.md)

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
| **404** | Income Type not found. |  -  |

<a id="incomeTypesGetById"></a>
# **incomeTypesGetById**
> IncomeTypeModel incomeTypesGetById(id)



Description: This operation retrieves the Income Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Income Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomeTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomeTypesApi apiInstance = new IncomeTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Income Type used to retreive the Income Type information
    try {
      IncomeTypeModel result = apiInstance.incomeTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomeTypesApi#incomeTypesGetById");
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
| **id** | **Integer**| The ID of Income Type used to retreive the Income Type information | |

### Return type

[**IncomeTypeModel**](IncomeTypeModel.md)

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
| **404** | Income Type not found. |  -  |

