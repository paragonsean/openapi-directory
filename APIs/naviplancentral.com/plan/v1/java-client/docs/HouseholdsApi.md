# HouseholdsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**householdsGetByHouseholdid**](HouseholdsApi.md#householdsGetByHouseholdid) | **GET** /api/Households | Retrieve all Households associated with the user |


<a id="householdsGetByHouseholdid"></a>
# **householdsGetByHouseholdid**
> HouseholdsModel householdsGetByHouseholdid(householdId)

Retrieve all Households associated with the user

This operation retrieves a list of households the current user has access to or one household specified by a householdId parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HouseholdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    HouseholdsApi apiInstance = new HouseholdsApi(defaultClient);
    Integer householdId = 56; // Integer | The Id of the specific household to retrieve
    try {
      HouseholdsModel result = apiInstance.householdsGetByHouseholdid(householdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HouseholdsApi#householdsGetByHouseholdid");
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
| **householdId** | **Integer**| The Id of the specific household to retrieve | [optional] |

### Return type

[**HouseholdsModel**](HouseholdsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized for household data access |  -  |
| **403** | Access to household is restricted |  -  |

