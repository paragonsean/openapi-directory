# LifestyleAssetTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lifestyleAssetTypesGetByCountry**](LifestyleAssetTypesApi.md#lifestyleAssetTypesGetByCountry) | **GET** /api/LifestyleAssetTypes |  |
| [**lifestyleAssetTypesGetById**](LifestyleAssetTypesApi.md#lifestyleAssetTypesGetById) | **GET** /api/LifestyleAssetTypes/{id} |  |


<a id="lifestyleAssetTypesGetByCountry"></a>
# **lifestyleAssetTypesGetByCountry**
> LifestyleAssetTypesModel lifestyleAssetTypesGetByCountry(country)



Description: This operation retrieves all Lifestyle Asset Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetTypesApi apiInstance = new LifestyleAssetTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Lifestyle Asset Types
    try {
      LifestyleAssetTypesModel result = apiInstance.lifestyleAssetTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetTypesApi#lifestyleAssetTypesGetByCountry");
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
| **country** | **String**| The country used to filter Lifestyle Asset Types | [enum: UnitedStates, Canada] |

### Return type

[**LifestyleAssetTypesModel**](LifestyleAssetTypesModel.md)

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
| **404** | Lifestyle Asset Type not found. |  -  |

<a id="lifestyleAssetTypesGetById"></a>
# **lifestyleAssetTypesGetById**
> LifestyleAssetTypeModel lifestyleAssetTypesGetById(id)



Description: This operation retrieves the Lifestyle Asset Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetTypesApi apiInstance = new LifestyleAssetTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Lifestyle Asset Type used to retreive the Lifestyle Asset Type information
    try {
      LifestyleAssetTypeModel result = apiInstance.lifestyleAssetTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetTypesApi#lifestyleAssetTypesGetById");
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
| **id** | **Integer**| The ID of Lifestyle Asset Type used to retreive the Lifestyle Asset Type information | |

### Return type

[**LifestyleAssetTypeModel**](LifestyleAssetTypeModel.md)

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
| **404** | Lifestyle Asset Type not found. |  -  |

