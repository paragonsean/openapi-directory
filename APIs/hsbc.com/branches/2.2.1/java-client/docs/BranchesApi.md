# BranchesApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openBankingV22BranchesGet**](BranchesApi.md#openBankingV22BranchesGet) | **GET** /open-banking/v2.2/branches |  |
| [**xOpenBankingV22BranchesCountryCountryGet**](BranchesApi.md#xOpenBankingV22BranchesCountryCountryGet) | **GET** /x-open-banking/v2.2/branches/country/{country} |  |
| [**xOpenBankingV22BranchesCountryCountryTownTownGet**](BranchesApi.md#xOpenBankingV22BranchesCountryCountryTownTownGet) | **GET** /x-open-banking/v2.2/branches/country/{country}/town/{town} |  |
| [**xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet**](BranchesApi.md#xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet) | **GET** /x-open-banking/v2.2/branches/geo-location/lat/{latitude}/long/{longitude} |  |
| [**xOpenBankingV22BranchesPostcodePostcodeGet**](BranchesApi.md#xOpenBankingV22BranchesPostcodePostcodeGet) | **GET** /x-open-banking/v2.2/branches/postcode/{postcode} |  |
| [**xOpenBankingV22BranchesSortcodeSortcodeGet**](BranchesApi.md#xOpenBankingV22BranchesSortcodeSortcodeGet) | **GET** /x-open-banking/v2.2/branches/sortcode/{sortcode} |  |


<a id="openBankingV22BranchesGet"></a>
# **openBankingV22BranchesGet**
> BranchDefinitionMeta openBankingV22BranchesGet()



This API will return the branch details for all branches and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    BranchesApi apiInstance = new BranchesApi(defaultClient);
    try {
      BranchDefinitionMeta result = apiInstance.openBankingV22BranchesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchesApi#openBankingV22BranchesGet");
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

[**BranchDefinitionMeta**](BranchDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

<a id="xOpenBankingV22BranchesCountryCountryGet"></a>
# **xOpenBankingV22BranchesCountryCountryGet**
> BranchDefinitionMeta xOpenBankingV22BranchesCountryCountryGet(country)



This extended API will return the branch details for all branches in the specified country. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    BranchesApi apiInstance = new BranchesApi(defaultClient);
    String country = "country_example"; // String | The ISO country code e.g. &quot;GB&quot;
    try {
      BranchDefinitionMeta result = apiInstance.xOpenBankingV22BranchesCountryCountryGet(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchesApi#xOpenBankingV22BranchesCountryCountryGet");
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
| **country** | **String**| The ISO country code e.g. &amp;quot;GB&amp;quot; | |

### Return type

[**BranchDefinitionMeta**](BranchDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

<a id="xOpenBankingV22BranchesCountryCountryTownTownGet"></a>
# **xOpenBankingV22BranchesCountryCountryTownTownGet**
> BranchDefinitionMeta xOpenBankingV22BranchesCountryCountryTownTownGet(country, town)



This extended API will return the branch details for all branches in the specified town. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    BranchesApi apiInstance = new BranchesApi(defaultClient);
    String country = "country_example"; // String | The ISO country code e.g. &quot;GB&quot;
    String town = "town_example"; // String | Town name, not case sensitive
    try {
      BranchDefinitionMeta result = apiInstance.xOpenBankingV22BranchesCountryCountryTownTownGet(country, town);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchesApi#xOpenBankingV22BranchesCountryCountryTownTownGet");
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
| **country** | **String**| The ISO country code e.g. &amp;quot;GB&amp;quot; | |
| **town** | **String**| Town name, not case sensitive | |

### Return type

[**BranchDefinitionMeta**](BranchDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

<a id="xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet"></a>
# **xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet**
> BranchDefinitionMeta xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet(latitude, longitude, radius)



This API will return the branch details for all branches within a specified radius (1 to 10 miles) of the specified latitude and longitude. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    BranchesApi apiInstance = new BranchesApi(defaultClient);
    String latitude = "latitude_example"; // String | Positive or negative decimal value in degrees. eg &quot;51.50551621597067&quot;
    String longitude = "longitude_example"; // String | Positive or negative decimal value in degrees. eg &quot;-0.0180120225995&quot;
    BigDecimal radius = new BigDecimal(78); // BigDecimal | Number of miles (1 to 10) as an integer. Default = 1
    try {
      BranchDefinitionMeta result = apiInstance.xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet(latitude, longitude, radius);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchesApi#xOpenBankingV22BranchesGeoLocationLatLatitudeLongLongitudeGet");
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
| **latitude** | **String**| Positive or negative decimal value in degrees. eg &amp;quot;51.50551621597067&amp;quot; | |
| **longitude** | **String**| Positive or negative decimal value in degrees. eg &amp;quot;-0.0180120225995&amp;quot; | |
| **radius** | **BigDecimal**| Number of miles (1 to 10) as an integer. Default &#x3D; 1 | |

### Return type

[**BranchDefinitionMeta**](BranchDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

<a id="xOpenBankingV22BranchesPostcodePostcodeGet"></a>
# **xOpenBankingV22BranchesPostcodePostcodeGet**
> BranchDefinitionMeta xOpenBankingV22BranchesPostcodePostcodeGet(postcode)



This extended API will return the branch details for all branches within a 5 mile radius of the specified postcode. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    BranchesApi apiInstance = new BranchesApi(defaultClient);
    String postcode = "postcode_example"; // String | Letters and numerals only. No spaces or special characters. eg. &quot;SW1A1AA&quot;
    try {
      BranchDefinitionMeta result = apiInstance.xOpenBankingV22BranchesPostcodePostcodeGet(postcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchesApi#xOpenBankingV22BranchesPostcodePostcodeGet");
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
| **postcode** | **String**| Letters and numerals only. No spaces or special characters. eg. &amp;quot;SW1A1AA&amp;quot; | |

### Return type

[**BranchDefinitionMeta**](BranchDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

<a id="xOpenBankingV22BranchesSortcodeSortcodeGet"></a>
# **xOpenBankingV22BranchesSortcodeSortcodeGet**
> BranchDefinitionMeta xOpenBankingV22BranchesSortcodeSortcodeGet(sortcode)



This extended API will return the branch details for a branch specified by its sort code. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    BranchesApi apiInstance = new BranchesApi(defaultClient);
    String sortcode = "sortcode_example"; // String | 6 digit number with no spaces or special characters. eg. &quot;400003&quot;
    try {
      BranchDefinitionMeta result = apiInstance.xOpenBankingV22BranchesSortcodeSortcodeGet(sortcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchesApi#xOpenBankingV22BranchesSortcodeSortcodeGet");
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
| **sortcode** | **String**| 6 digit number with no spaces or special characters. eg. &amp;quot;400003&amp;quot; | |

### Return type

[**BranchDefinitionMeta**](BranchDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

