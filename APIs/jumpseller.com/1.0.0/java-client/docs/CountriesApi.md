# CountriesApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countriesCountryCodeJsonGet**](CountriesApi.md#countriesCountryCodeJsonGet) | **GET** /countries/{country_code}.json | Retrieve a single Country information. |
| [**countriesCountryCodeRegionsJsonGet**](CountriesApi.md#countriesCountryCodeRegionsJsonGet) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country. |
| [**countriesCountryCodeRegionsRegionCodeJsonGet**](CountriesApi.md#countriesCountryCodeRegionsRegionCodeJsonGet) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object. |
| [**countriesJsonGet**](CountriesApi.md#countriesJsonGet) | **GET** /countries.json | Retrieve all Countries. |


<a id="countriesCountryCodeJsonGet"></a>
# **countriesCountryCodeJsonGet**
> Country countriesCountryCodeJsonGet(login, authtoken, countryCode)

Retrieve a single Country information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String countryCode = "countryCode_example"; // String | ISO3166 Country Code
    try {
      Country result = apiInstance.countriesCountryCodeJsonGet(login, authtoken, countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesCountryCodeJsonGet");
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

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Country information object |  -  |
| **404** | Country Not Found. |  -  |

<a id="countriesCountryCodeRegionsJsonGet"></a>
# **countriesCountryCodeRegionsJsonGet**
> List&lt;Region&gt; countriesCountryCodeRegionsJsonGet(login, authtoken, countryCode)

Retrieve all Regions from a single Country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String countryCode = "countryCode_example"; // String | ISO3166 Country Code
    try {
      List<Region> result = apiInstance.countriesCountryCodeRegionsJsonGet(login, authtoken, countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesCountryCodeRegionsJsonGet");
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

<a id="countriesCountryCodeRegionsRegionCodeJsonGet"></a>
# **countriesCountryCodeRegionsRegionCodeJsonGet**
> Region countriesCountryCodeRegionsRegionCodeJsonGet(login, authtoken, countryCode, regionCode)

Retrieve a single Region information object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String countryCode = "countryCode_example"; // String | ISO3166 Country Code
    String regionCode = "regionCode_example"; // String | Region Code
    try {
      Region result = apiInstance.countriesCountryCodeRegionsRegionCodeJsonGet(login, authtoken, countryCode, regionCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesCountryCodeRegionsRegionCodeJsonGet");
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

<a id="countriesJsonGet"></a>
# **countriesJsonGet**
> List&lt;Country&gt; countriesJsonGet(login, authtoken)

Retrieve all Countries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      List<Country> result = apiInstance.countriesJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesJsonGet");
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

### Return type

[**List&lt;Country&gt;**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Countries |  -  |

