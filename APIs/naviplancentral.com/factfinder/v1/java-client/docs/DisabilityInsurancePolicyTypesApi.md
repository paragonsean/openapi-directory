# DisabilityInsurancePolicyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disabilityInsurancePolicyTypesGetByCountry**](DisabilityInsurancePolicyTypesApi.md#disabilityInsurancePolicyTypesGetByCountry) | **GET** /api/DisabilityInsurancePolicyTypes |  |
| [**disabilityInsurancePolicyTypesGetById**](DisabilityInsurancePolicyTypesApi.md#disabilityInsurancePolicyTypesGetById) | **GET** /api/DisabilityInsurancePolicyTypes/{id} |  |


<a id="disabilityInsurancePolicyTypesGetByCountry"></a>
# **disabilityInsurancePolicyTypesGetByCountry**
> DisabilityInsurancePolicyTypesModel disabilityInsurancePolicyTypesGetByCountry(country)



Description: This operation retrieves all Disability Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePolicyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePolicyTypesApi apiInstance = new DisabilityInsurancePolicyTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Disability Insurance Policy Types
    try {
      DisabilityInsurancePolicyTypesModel result = apiInstance.disabilityInsurancePolicyTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePolicyTypesApi#disabilityInsurancePolicyTypesGetByCountry");
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
| **country** | **String**| The country used to filter Disability Insurance Policy Types | [enum: UnitedStates, Canada] |

### Return type

[**DisabilityInsurancePolicyTypesModel**](DisabilityInsurancePolicyTypesModel.md)

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
| **404** | Disability Insurance Policy Type not found. |  -  |

<a id="disabilityInsurancePolicyTypesGetById"></a>
# **disabilityInsurancePolicyTypesGetById**
> DisabilityInsurancePolicyTypeModel disabilityInsurancePolicyTypesGetById(id)



Description: This operation retrieves all Disability Insurance Policy Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePolicyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePolicyTypesApi apiInstance = new DisabilityInsurancePolicyTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Disability Insurance Policy Type used to retreive the Disability Insurance Policy Type information
    try {
      DisabilityInsurancePolicyTypeModel result = apiInstance.disabilityInsurancePolicyTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePolicyTypesApi#disabilityInsurancePolicyTypesGetById");
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
| **id** | **Integer**| The ID of Disability Insurance Policy Type used to retreive the Disability Insurance Policy Type information | |

### Return type

[**DisabilityInsurancePolicyTypeModel**](DisabilityInsurancePolicyTypeModel.md)

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
| **404** | Disability Insurance Policy Type not found. |  -  |

