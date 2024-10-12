# AtmsApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openBankingV22AtmsGet**](AtmsApi.md#openBankingV22AtmsGet) | **GET** /open-banking/v2.2/atms |  |
| [**xOpenBankingV22AtmsCountryCountryGet**](AtmsApi.md#xOpenBankingV22AtmsCountryCountryGet) | **GET** /x-open-banking/v2.2/atms/country/{country} |  |
| [**xOpenBankingV22AtmsCountryCountryTownTownGet**](AtmsApi.md#xOpenBankingV22AtmsCountryCountryTownTownGet) | **GET** /x-open-banking/v2.2/atms/country/{country}/town/{town} |  |
| [**xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet**](AtmsApi.md#xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet) | **GET** /x-open-banking/v2.2/atms/geo-location/lat/{latitude}/long/{longitude} |  |
| [**xOpenBankingV22AtmsPostcodePostcodeGet**](AtmsApi.md#xOpenBankingV22AtmsPostcodePostcodeGet) | **GET** /x-open-banking/v2.2/atms/postcode/{postcode} |  |


<a id="openBankingV22AtmsGet"></a>
# **openBankingV22AtmsGet**
> ATMDefinitionMeta openBankingV22AtmsGet()



This API will return data about all our ATMs and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    AtmsApi apiInstance = new AtmsApi(defaultClient);
    try {
      ATMDefinitionMeta result = apiInstance.openBankingV22AtmsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmsApi#openBankingV22AtmsGet");
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

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

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

<a id="xOpenBankingV22AtmsCountryCountryGet"></a>
# **xOpenBankingV22AtmsCountryCountryGet**
> ATMDefinitionMeta xOpenBankingV22AtmsCountryCountryGet(country)



This extended API will return data about all ATMs in the specified country. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    AtmsApi apiInstance = new AtmsApi(defaultClient);
    String country = "country_example"; // String | The ISO country code e.g. &quot;GB&quot;
    try {
      ATMDefinitionMeta result = apiInstance.xOpenBankingV22AtmsCountryCountryGet(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmsApi#xOpenBankingV22AtmsCountryCountryGet");
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

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

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

<a id="xOpenBankingV22AtmsCountryCountryTownTownGet"></a>
# **xOpenBankingV22AtmsCountryCountryTownTownGet**
> ATMDefinitionMeta xOpenBankingV22AtmsCountryCountryTownTownGet(country, town)



This extended API will return data about all ATMs in the specified town. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    AtmsApi apiInstance = new AtmsApi(defaultClient);
    String country = "country_example"; // String | The ISO country code e.g. &quot;GB&quot;
    String town = "town_example"; // String | Town name, not case sensitive
    try {
      ATMDefinitionMeta result = apiInstance.xOpenBankingV22AtmsCountryCountryTownTownGet(country, town);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmsApi#xOpenBankingV22AtmsCountryCountryTownTownGet");
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

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

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

<a id="xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet"></a>
# **xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet**
> ATMDefinitionMeta xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet(latitude, longitude, radius)



This extended API will data about all ATMs within a specified radius (1 to 10 miles) of the specified latitude and longitude. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    AtmsApi apiInstance = new AtmsApi(defaultClient);
    String latitude = "latitude_example"; // String | Positive or negative decimal value in degrees. eg &quot;51.50551621597067&quot;
    String longitude = "longitude_example"; // String | Positive or negative decimal value in degrees. eg &quot;-0.0180120225995&quot;
    BigDecimal radius = new BigDecimal(78); // BigDecimal | Number of miles (1 to 10) as an integer. Default = 1
    try {
      ATMDefinitionMeta result = apiInstance.xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet(latitude, longitude, radius);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmsApi#xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet");
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

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

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

<a id="xOpenBankingV22AtmsPostcodePostcodeGet"></a>
# **xOpenBankingV22AtmsPostcodePostcodeGet**
> ATMDefinitionMeta xOpenBankingV22AtmsPostcodePostcodeGet(postcode)



This extended API will return data about all ATMs within a 5 mile radius of the specified postcode. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    AtmsApi apiInstance = new AtmsApi(defaultClient);
    String postcode = "postcode_example"; // String | Letters and numerals only. No spaces or special characters. eg  &quot;SW1A1AA&quot;
    try {
      ATMDefinitionMeta result = apiInstance.xOpenBankingV22AtmsPostcodePostcodeGet(postcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmsApi#xOpenBankingV22AtmsPostcodePostcodeGet");
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
| **postcode** | **String**| Letters and numerals only. No spaces or special characters. eg  &amp;quot;SW1A1AA&amp;quot; | |

### Return type

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

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

