# CriticalIllnessInsurancePolicyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**criticalIllnessInsurancePolicyTypesGetByCountry**](CriticalIllnessInsurancePolicyTypesApi.md#criticalIllnessInsurancePolicyTypesGetByCountry) | **GET** /api/CriticalIllnessInsurancePolicyTypes |  |
| [**criticalIllnessInsurancePolicyTypesGetById**](CriticalIllnessInsurancePolicyTypesApi.md#criticalIllnessInsurancePolicyTypesGetById) | **GET** /api/CriticalIllnessInsurancePolicyTypes/{id} |  |


<a id="criticalIllnessInsurancePolicyTypesGetByCountry"></a>
# **criticalIllnessInsurancePolicyTypesGetByCountry**
> CriticalIllnessInsurancePolicyTypesModel criticalIllnessInsurancePolicyTypesGetByCountry(country)



Description: This operation retrieves all Critical Illness Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePolicyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePolicyTypesApi apiInstance = new CriticalIllnessInsurancePolicyTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Critical Illness Insurance Policy Types
    try {
      CriticalIllnessInsurancePolicyTypesModel result = apiInstance.criticalIllnessInsurancePolicyTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePolicyTypesApi#criticalIllnessInsurancePolicyTypesGetByCountry");
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
| **country** | **String**| The country used to filter Critical Illness Insurance Policy Types | [enum: UnitedStates, Canada] |

### Return type

[**CriticalIllnessInsurancePolicyTypesModel**](CriticalIllnessInsurancePolicyTypesModel.md)

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
| **404** | Critical Illness Insurance Policy Type not found. |  -  |

<a id="criticalIllnessInsurancePolicyTypesGetById"></a>
# **criticalIllnessInsurancePolicyTypesGetById**
> CriticalIllnessInsurancePolicyTypeModel criticalIllnessInsurancePolicyTypesGetById(id)



Description: This operation retrieves the Critical Illness Insurance Policy Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePolicyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePolicyTypesApi apiInstance = new CriticalIllnessInsurancePolicyTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Critical Illness Insurance Policy Type used to retreive the Critical Illness Insurance Policy Type information
    try {
      CriticalIllnessInsurancePolicyTypeModel result = apiInstance.criticalIllnessInsurancePolicyTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePolicyTypesApi#criticalIllnessInsurancePolicyTypesGetById");
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
| **id** | **Integer**| The ID of Critical Illness Insurance Policy Type used to retreive the Critical Illness Insurance Policy Type information | |

### Return type

[**CriticalIllnessInsurancePolicyTypeModel**](CriticalIllnessInsurancePolicyTypeModel.md)

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
| **404** | Critical Illness Insurance Policy Type not found. |  -  |

