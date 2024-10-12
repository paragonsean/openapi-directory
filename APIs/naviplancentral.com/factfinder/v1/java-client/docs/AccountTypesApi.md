# AccountTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountTypesGetByCountry**](AccountTypesApi.md#accountTypesGetByCountry) | **GET** /api/AccountTypes |  |
| [**accountTypesGetById**](AccountTypesApi.md#accountTypesGetById) | **GET** /api/AccountTypes/{id} |  |


<a id="accountTypesGetByCountry"></a>
# **accountTypesGetByCountry**
> AccountTypesModel accountTypesGetByCountry(country)



Description: This operation retrieves all Account Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountTypesApi apiInstance = new AccountTypesApi(defaultClient);
    String country = "UnitedStates"; // String | The country used to filter Account Types
    try {
      AccountTypesModel result = apiInstance.accountTypesGetByCountry(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountTypesApi#accountTypesGetByCountry");
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
| **country** | **String**| The country used to filter Account Types | [enum: UnitedStates, Canada] |

### Return type

[**AccountTypesModel**](AccountTypesModel.md)

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
| **404** | Account Type not found |  -  |

<a id="accountTypesGetById"></a>
# **accountTypesGetById**
> AccountTypeModel accountTypesGetById(id)



Description: This operation retrieves all Account Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountTypesApi apiInstance = new AccountTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of Account Type used to retreive the Account Type information
    try {
      AccountTypeModel result = apiInstance.accountTypesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountTypesApi#accountTypesGetById");
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
| **id** | **Integer**| The ID of Account Type used to retreive the Account Type information | |

### Return type

[**AccountTypeModel**](AccountTypeModel.md)

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
| **404** | Account Type not found |  -  |

