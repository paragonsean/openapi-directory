# ExpenseTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseTypesGetByCountry**](ExpenseTypesApi.md#expenseTypesGetByCountry) | **GET** /api/ExpenseTypes |  |
| [**expenseTypesGetById**](ExpenseTypesApi.md#expenseTypesGetById) | **GET** /api/ExpenseTypes/{id} |  |


<a id="expenseTypesGetByCountry"></a>
# **expenseTypesGetByCountry**
> ExpenseTypesModel expenseTypesGetByCountry(country)



Description: This operation retrieves all Expense Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Expense Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpenseTypesApi apiInstance = new ExpenseTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Expense Types
    try {
      ExpenseTypesModel result = apiInstance.expenseTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseTypesApi#expenseTypesGetByCountry");
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
| **country** | **String**| The country used to filter Expense Types | [enum: UnitedStates, Canada] |

### Return type

[**ExpenseTypesModel**](ExpenseTypesModel.md)

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
| **404** | Expense Type not found. |  -  |

<a id="expenseTypesGetById"></a>
# **expenseTypesGetById**
> ExpenseTypeModel expenseTypesGetById(id)



Description: This operation retrieves all Expense Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Expense Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpenseTypesApi apiInstance = new ExpenseTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Expense Type used to retreive the Expense Type information
    try {
      ExpenseTypeModel result = apiInstance.expenseTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseTypesApi#expenseTypesGetById");
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
| **id** | **Integer**| The ID of Expense Type used to retreive the Expense Type information | |

### Return type

[**ExpenseTypeModel**](ExpenseTypeModel.md)

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
| **404** | Expense Type not found. |  -  |

