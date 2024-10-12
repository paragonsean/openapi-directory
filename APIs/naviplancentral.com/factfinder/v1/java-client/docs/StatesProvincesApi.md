# StatesProvincesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statesProvincesGetByCountry**](StatesProvincesApi.md#statesProvincesGetByCountry) | **GET** /api/StatesProvinces |  |
| [**statesProvincesGetById**](StatesProvincesApi.md#statesProvincesGetById) | **GET** /api/StatesProvinces/{id} |  |


<a id="statesProvincesGetByCountry"></a>
# **statesProvincesGetByCountry**
> StatesProvincesModel statesProvincesGetByCountry(country)



Description: This operation retrieves all States and Provinces for the specified country.&lt;br /&gt;                Purpose: Provides access to the States and Provinces.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatesProvincesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    StatesProvincesApi apiInstance = new StatesProvincesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter States and Provinces
    try {
      StatesProvincesModel result = apiInstance.statesProvincesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatesProvincesApi#statesProvincesGetByCountry");
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
| **country** | **String**| The country used to filter States and Provinces | [enum: UnitedStates, Canada] |

### Return type

[**StatesProvincesModel**](StatesProvincesModel.md)

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
| **404** | State or Province not found. |  -  |

<a id="statesProvincesGetById"></a>
# **statesProvincesGetById**
> StateProvinceModel statesProvincesGetById(id)



Description: This operation retrieves the States and Provinces for the specified id.&lt;br /&gt;                Purpose: Provides access to the States and Provinces.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatesProvincesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    StatesProvincesApi apiInstance = new StatesProvincesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the State or Province used to retreive the State or Province information
    try {
      StateProvinceModel result = apiInstance.statesProvincesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatesProvincesApi#statesProvincesGetById");
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
| **id** | **Integer**| The ID of the State or Province used to retreive the State or Province information | |

### Return type

[**StateProvinceModel**](StateProvinceModel.md)

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
| **404** | State or Province not found. |  -  |

