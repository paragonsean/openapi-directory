# RegionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countriesCountryCodeRegionsJsonGet_0**](RegionsApi.md#countriesCountryCodeRegionsJsonGet_0) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country. |
| [**countriesCountryCodeRegionsRegionCodeJsonGet_0**](RegionsApi.md#countriesCountryCodeRegionsRegionCodeJsonGet_0) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object. |


<a id="countriesCountryCodeRegionsJsonGet_0"></a>
# **countriesCountryCodeRegionsJsonGet_0**
> List&lt;Region&gt; countriesCountryCodeRegionsJsonGet_0(login, authtoken, countryCode)

Retrieve all Regions from a single Country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    RegionsApi apiInstance = new RegionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String countryCode = "countryCode_example"; // String | ISO3166 Country Code
    try {
      List<Region> result = apiInstance.countriesCountryCodeRegionsJsonGet_0(login, authtoken, countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionsApi#countriesCountryCodeRegionsJsonGet_0");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **countryCode** | **String**| ISO3166 Country Code | |

### Return type

[**List&lt;Region&gt;**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Regions from a single Country |  -  |
| **404** | Country Not Found. |  -  |

<a id="countriesCountryCodeRegionsRegionCodeJsonGet_0"></a>
# **countriesCountryCodeRegionsRegionCodeJsonGet_0**
> Region countriesCountryCodeRegionsRegionCodeJsonGet_0(login, authtoken, countryCode, regionCode)

Retrieve a single Region information object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    RegionsApi apiInstance = new RegionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String countryCode = "countryCode_example"; // String | ISO3166 Country Code
    String regionCode = "regionCode_example"; // String | Region Code
    try {
      Region result = apiInstance.countriesCountryCodeRegionsRegionCodeJsonGet_0(login, authtoken, countryCode, regionCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionsApi#countriesCountryCodeRegionsRegionCodeJsonGet_0");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **countryCode** | **String**| ISO3166 Country Code | |
| **regionCode** | **String**| Region Code | |

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Region information object |  -  |
| **404** | Country or Region not found. |  -  |

