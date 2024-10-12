# FrequencyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**frequencyTypesGetByEntityCountry**](FrequencyTypesApi.md#frequencyTypesGetByEntityCountry) | **GET** /api/FrequencyTypes |  |
| [**frequencyTypesGetById**](FrequencyTypesApi.md#frequencyTypesGetById) | **GET** /api/FrequencyTypes/{id} |  |


<a id="frequencyTypesGetByEntityCountry"></a>
# **frequencyTypesGetByEntityCountry**
> FrequencyTypesModel frequencyTypesGetByEntityCountry(entity, country)



Description: This operation retrieves all Frequency Types for the specified country and entity.&lt;br /&gt;                Purpose: Provides access to the Frequency Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrequencyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FrequencyTypesApi apiInstance = new FrequencyTypesApi(defaultClient);
    String entity = "CriticalIllnessInsurancePolicies"; // String | The entity used to filter Frequency Types
    String country = "UnitedStates"; // String | The country used to filter Frequency Types
    try {
      FrequencyTypesModel result = apiInstance.frequencyTypesGetByEntityCountry(entity, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrequencyTypesApi#frequencyTypesGetByEntityCountry");
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
| **entity** | **String**| The entity used to filter Frequency Types | [enum: CriticalIllnessInsurancePolicies, DisabilityInsurancePoliciesPremium, DisabilityInsurancePoliciesBenefit, Expenses, Liabilities, LifeInsurancePolicies, LongTermCareInsurancePoliciesBenefit, LongTermCareInsurancePoliciesPremium, RealEstateAssets, RetirementExpenses, SavingsStrategies] |
| **country** | **String**| The country used to filter Frequency Types | [enum: UnitedStates, Canada] |

### Return type

[**FrequencyTypesModel**](FrequencyTypesModel.md)

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
| **404** | Frequency Type not found. |  -  |

<a id="frequencyTypesGetById"></a>
# **frequencyTypesGetById**
> FrequencyTypeModel frequencyTypesGetById(id)



Description: This operation retrieves the Frequency Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Frequency Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrequencyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FrequencyTypesApi apiInstance = new FrequencyTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Frequency Type used to retreive the Frequency Type information
    try {
      FrequencyTypeModel result = apiInstance.frequencyTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrequencyTypesApi#frequencyTypesGetById");
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
| **id** | **Integer**| The ID of Frequency Type used to retreive the Frequency Type information | |

### Return type

[**FrequencyTypeModel**](FrequencyTypeModel.md)

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
| **404** | Frequency Type not found. |  -  |

