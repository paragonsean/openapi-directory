# InstitutionsApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveAllSupportedInstitutionsInAGivenCountry**](InstitutionsApi.md#retrieveAllSupportedInstitutionsInAGivenCountry) | **GET** /api/v2/institutions/ |  |
| [**retrieveInstitution**](InstitutionsApi.md#retrieveInstitution) | **GET** /api/v2/institutions/{id}/ |  |


<a id="retrieveAllSupportedInstitutionsInAGivenCountry"></a>
# **retrieveAllSupportedInstitutionsInAGivenCountry**
> List&lt;Integration&gt; retrieveAllSupportedInstitutionsInAGivenCountry(country, paymentsEnabled)



List all available institutions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String country = "AT"; // String | ISO 3166 two-character country code
    String paymentsEnabled = "false"; // String | Boolean value, indicating if payments are enabled
    try {
      List<Integration> result = apiInstance.retrieveAllSupportedInstitutionsInAGivenCountry(country, paymentsEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#retrieveAllSupportedInstitutionsInAGivenCountry");
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
| **country** | **String**| ISO 3166 two-character country code | [optional] |
| **paymentsEnabled** | **String**| Boolean value, indicating if payments are enabled | [optional] |

### Return type

[**List&lt;Integration&gt;**](Integration.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of supported Institutions in the country |  -  |
| **400** | Unknown Fields |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="retrieveInstitution"></a>
# **retrieveInstitution**
> IntegrationRetrieve retrieveInstitution(id)



Get details about a specific Institution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String id = "N26_NTSBDEB1"; // String | 
    try {
      IntegrationRetrieve result = apiInstance.retrieveInstitution(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#retrieveInstitution");
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
| **id** | **String**|  | |

### Return type

[**IntegrationRetrieve**](IntegrationRetrieve.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve institution by id |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

