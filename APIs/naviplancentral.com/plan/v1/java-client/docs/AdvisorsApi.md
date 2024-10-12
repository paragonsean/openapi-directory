# AdvisorsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**advisorsGet**](AdvisorsApi.md#advisorsGet) | **GET** /api/Advisors | Retrieve Advisors |
| [**advisorsGetByHouseholdidClientid**](AdvisorsApi.md#advisorsGetByHouseholdidClientid) | **GET** /api/Advisors/{householdId}/{clientId} | Retrieve Advisors for a Client |
| [**advisorsGetById**](AdvisorsApi.md#advisorsGetById) | **GET** /api/Advisors/{id} | Retrieve an Advisor |


<a id="advisorsGet"></a>
# **advisorsGet**
> AdvisorsModel advisorsGet()

Retrieve Advisors

This operation retrieves a list of all of the Advisors in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AdvisorsApi apiInstance = new AdvisorsApi(defaultClient);
    try {
      AdvisorsModel result = apiInstance.advisorsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdvisorsApi#advisorsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdvisorsModel**](AdvisorsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for advisor details |  -  |
| **404** | Object not found |  -  |

<a id="advisorsGetByHouseholdidClientid"></a>
# **advisorsGetByHouseholdidClientid**
> AdvisorsModel advisorsGetByHouseholdidClientid(householdId, clientId)

Retrieve Advisors for a Client

This operation retrieves a list of all of the Advisors for the client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AdvisorsApi apiInstance = new AdvisorsApi(defaultClient);
    Integer householdId = 56; // Integer | Integer id of the household
    String clientId = "clientId_example"; // String | Guid id of the client.
    try {
      AdvisorsModel result = apiInstance.advisorsGetByHouseholdidClientid(householdId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdvisorsApi#advisorsGetByHouseholdidClientid");
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
| **householdId** | **Integer**| Integer id of the household | |
| **clientId** | **String**| Guid id of the client. | |

### Return type

[**AdvisorsModel**](AdvisorsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for advisor details |  -  |
| **403** | Request is restricted for access to advisor information |  -  |
| **404** | Object not found |  -  |

<a id="advisorsGetById"></a>
# **advisorsGetById**
> AdvisorModel advisorsGetById(id)

Retrieve an Advisor

This operation retrieves an Advisor from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AdvisorsApi apiInstance = new AdvisorsApi(defaultClient);
    String id = "id_example"; // String | Guid id of the advisor
    try {
      AdvisorModel result = apiInstance.advisorsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdvisorsApi#advisorsGetById");
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
| **id** | **String**| Guid id of the advisor | |

### Return type

[**AdvisorModel**](AdvisorModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for advisor details |  -  |
| **404** | Object not found |  -  |

