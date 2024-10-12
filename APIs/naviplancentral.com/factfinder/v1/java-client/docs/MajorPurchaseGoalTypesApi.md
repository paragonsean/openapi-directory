# MajorPurchaseGoalTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**majorPurchaseGoalTypesGetByCountry**](MajorPurchaseGoalTypesApi.md#majorPurchaseGoalTypesGetByCountry) | **GET** /api/MajorPurchaseGoalTypes |  |
| [**majorPurchaseGoalTypesGetById**](MajorPurchaseGoalTypesApi.md#majorPurchaseGoalTypesGetById) | **GET** /api/MajorPurchaseGoalTypes/{id} |  |


<a id="majorPurchaseGoalTypesGetByCountry"></a>
# **majorPurchaseGoalTypesGetByCountry**
> MajorPurchaseGoalTypesModel majorPurchaseGoalTypesGetByCountry(country)



Description: This operation retrieves all Major Purchase Goal Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Major Purchase Goal Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalTypesApi apiInstance = new MajorPurchaseGoalTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Major Purchase Goal Types
    try {
      MajorPurchaseGoalTypesModel result = apiInstance.majorPurchaseGoalTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalTypesApi#majorPurchaseGoalTypesGetByCountry");
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
| **country** | **String**| The country used to filter Major Purchase Goal Types | [enum: UnitedStates, Canada] |

### Return type

[**MajorPurchaseGoalTypesModel**](MajorPurchaseGoalTypesModel.md)

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
| **404** | Major Purchase Goal Type not found. |  -  |

<a id="majorPurchaseGoalTypesGetById"></a>
# **majorPurchaseGoalTypesGetById**
> MajorPurchaseGoalTypeModel majorPurchaseGoalTypesGetById(id)



Description: This operation retrieves the Major Purchase Goal Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Major Purchase Goal Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalTypesApi apiInstance = new MajorPurchaseGoalTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Major Purchase Goal Type used to retreive the Major Purchase Goal Type information
    try {
      MajorPurchaseGoalTypeModel result = apiInstance.majorPurchaseGoalTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalTypesApi#majorPurchaseGoalTypesGetById");
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
| **id** | **Integer**| The ID of Major Purchase Goal Type used to retreive the Major Purchase Goal Type information | |

### Return type

[**MajorPurchaseGoalTypeModel**](MajorPurchaseGoalTypeModel.md)

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
| **404** | Major Purchase Goal Type not found. |  -  |

