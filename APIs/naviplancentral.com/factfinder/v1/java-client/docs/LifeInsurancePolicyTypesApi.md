# LifeInsurancePolicyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lifeInsurancePolicyTypesGetByCountry**](LifeInsurancePolicyTypesApi.md#lifeInsurancePolicyTypesGetByCountry) | **GET** /api/LifeInsurancePolicyTypes |  |
| [**lifeInsurancePolicyTypesGetById**](LifeInsurancePolicyTypesApi.md#lifeInsurancePolicyTypesGetById) | **GET** /api/LifeInsurancePolicyTypes/{id} |  |


<a id="lifeInsurancePolicyTypesGetByCountry"></a>
# **lifeInsurancePolicyTypesGetByCountry**
> LifeInsurancePolicyTypesModel lifeInsurancePolicyTypesGetByCountry(country)



Description: This operation retrieves all Life Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePolicyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePolicyTypesApi apiInstance = new LifeInsurancePolicyTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Life Insurance Policy Types
    try {
      LifeInsurancePolicyTypesModel result = apiInstance.lifeInsurancePolicyTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePolicyTypesApi#lifeInsurancePolicyTypesGetByCountry");
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
| **country** | **String**| The country used to filter Life Insurance Policy Types | [enum: UnitedStates, Canada] |

### Return type

[**LifeInsurancePolicyTypesModel**](LifeInsurancePolicyTypesModel.md)

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
| **404** | Life Insurance Policy Type not found. |  -  |

<a id="lifeInsurancePolicyTypesGetById"></a>
# **lifeInsurancePolicyTypesGetById**
> LifeInsurancePolicyTypeModel lifeInsurancePolicyTypesGetById(id)



Description: This operation retrieves the Life Insurance Policy Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePolicyTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePolicyTypesApi apiInstance = new LifeInsurancePolicyTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Life Insurance Policy Type used to retreive the Life Insurance Policy Type information
    try {
      LifeInsurancePolicyTypeModel result = apiInstance.lifeInsurancePolicyTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePolicyTypesApi#lifeInsurancePolicyTypesGetById");
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
| **id** | **Integer**| The ID of Life Insurance Policy Type used to retreive the Life Insurance Policy Type information | |

### Return type

[**LifeInsurancePolicyTypeModel**](LifeInsurancePolicyTypeModel.md)

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
| **404** | Life Insurance Policy Type not found. |  -  |

