# CitiesApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**citiesDrillersList**](CitiesApi.md#citiesDrillersList) | **GET** /cities/drillers/ |  |
| [**citiesInstallersList**](CitiesApi.md#citiesInstallersList) | **GET** /cities/installers/ |  |


<a id="citiesDrillersList"></a>
# **citiesDrillersList**
> List&lt;CityList&gt; citiesDrillersList()



returns a list of cities with a qualified, registered operator (driller or installer)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CitiesApi apiInstance = new CitiesApi(defaultClient);
    try {
      List<CityList> result = apiInstance.citiesDrillersList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitiesApi#citiesDrillersList");
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

[**List&lt;CityList&gt;**](CityList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="citiesInstallersList"></a>
# **citiesInstallersList**
> List&lt;CityList&gt; citiesInstallersList()



returns a list of cities with a qualified, registered operator (driller or installer)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CitiesApi apiInstance = new CitiesApi(defaultClient);
    try {
      List<CityList> result = apiInstance.citiesInstallersList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitiesApi#citiesInstallersList");
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

[**List&lt;CityList&gt;**](CityList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

