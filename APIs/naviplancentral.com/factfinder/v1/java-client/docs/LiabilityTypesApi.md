# LiabilityTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liabilityTypesGetByCountry**](LiabilityTypesApi.md#liabilityTypesGetByCountry) | **GET** /api/LiabilityTypes |  |
| [**liabilityTypesGetById**](LiabilityTypesApi.md#liabilityTypesGetById) | **GET** /api/LiabilityTypes/{id} |  |


<a id="liabilityTypesGetByCountry"></a>
# **liabilityTypesGetByCountry**
> LiabilityTypesModel liabilityTypesGetByCountry(country)



Description: This operation retrieves all Liability Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Liability Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilityTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilityTypesApi apiInstance = new LiabilityTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Liability Types
    try {
      LiabilityTypesModel result = apiInstance.liabilityTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilityTypesApi#liabilityTypesGetByCountry");
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
| **country** | **String**| The country used to filter Liability Types | [enum: UnitedStates, Canada] |

### Return type

[**LiabilityTypesModel**](LiabilityTypesModel.md)

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
| **404** | Liability Type not found. |  -  |

<a id="liabilityTypesGetById"></a>
# **liabilityTypesGetById**
> LiabilityTypeModel liabilityTypesGetById(id)



Description: This operation retrieves the Liability Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Liability Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilityTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilityTypesApi apiInstance = new LiabilityTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Liability Type used to retreive the Liability Type information
    try {
      LiabilityTypeModel result = apiInstance.liabilityTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilityTypesApi#liabilityTypesGetById");
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
| **id** | **Integer**| The ID of Liability Type used to retreive the Liability Type information | |

### Return type

[**LiabilityTypeModel**](LiabilityTypeModel.md)

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
| **404** | Liability Type not found. |  -  |

