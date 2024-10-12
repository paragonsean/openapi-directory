# DefaultApi

All URIs are relative to *https://global.metadapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDistance**](DefaultApi.md#getDistance) | **GET** /zipc/v1/distance | Distance Between 2 Zip Codes |
| [**getMsagroups**](DefaultApi.md#getMsagroups) | **GET** /zipc/v1/msagroups | List All MSA Groups |
| [**getMsagroupsMsacode**](DefaultApi.md#getMsagroupsMsacode) | **GET** /zipc/v1/msagroups/{msaCode} | Metro/Micro Statistical Area Details |
| [**getRadius**](DefaultApi.md#getRadius) | **GET** /zipc/v1/radius | Zip Code Radius |
| [**getZipcV1**](DefaultApi.md#getZipcV1) | **GET** /zipc/v1 | Validate License Key |
| [**getZipcode**](DefaultApi.md#getZipcode) | **GET** /zipc/v1/zipcodes/{zipcode} | Zip Code Details |
| [**getZipcodes**](DefaultApi.md#getZipcodes) | **GET** /zipc/v1/zipcodes | List all Zip Codes |


<a id="getDistance"></a>
# **getDistance**
> GetDistance200Response getDistance(zipCode1, zipCode2)

Distance Between 2 Zip Codes

Gets the distance (in miles and kilometers) between 2 zip codes passed as parameters. There are 2 mandatory query parameters (zipCode1 and zipCode2). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String zipCode1 = "90210"; // String | Zip Code 1
    String zipCode2 = "33162"; // String | Zip Code 2
    try {
      GetDistance200Response result = apiInstance.getDistance(zipCode1, zipCode2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDistance");
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
| **zipCode1** | **String**| Zip Code 1 | |
| **zipCode2** | **String**| Zip Code 2 | |

### Return type

[**GetDistance200Response**](GetDistance200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getMsagroups"></a>
# **getMsagroups**
> GetMsagroups200Response getMsagroups(limit, offset, stateCode)

List All MSA Groups

This end point lists all the Metropolitan and Micropolitan Statistical Areas in the United States with the corresponding states and counties that make up the group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | Number of records to return in each page. Max value: 50.
    Integer offset = 56; // Integer | Offset is the position in the dataset to start retrieval of records.
    String stateCode = "CA"; // String | Parameter for state code.
    try {
      GetMsagroups200Response result = apiInstance.getMsagroups(limit, offset, stateCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMsagroups");
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
| **limit** | **Integer**| Number of records to return in each page. Max value: 50. | |
| **offset** | **Integer**| Offset is the position in the dataset to start retrieval of records. | |
| **stateCode** | **String**| Parameter for state code. | [optional] |

### Return type

[**GetMsagroups200Response**](GetMsagroups200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getMsagroupsMsacode"></a>
# **getMsagroupsMsacode**
> GetMsagroupsMsacode200Response getMsagroupsMsacode(msaCode)

Metro/Micro Statistical Area Details

Gets the details of a single Metropolitan Statistical Area code passed as a path parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String msaCode = "11580"; // String | 5 digit MSA (Metropolitan Statistical Area) code.
    try {
      GetMsagroupsMsacode200Response result = apiInstance.getMsagroupsMsacode(msaCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMsagroupsMsacode");
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
| **msaCode** | **String**| 5 digit MSA (Metropolitan Statistical Area) code. | |

### Return type

[**GetMsagroupsMsacode200Response**](GetMsagroupsMsacode200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getRadius"></a>
# **getRadius**
> GetRadius200Response getRadius(zipCode, radius, uom)

Zip Code Radius

Endpoint that returns the zip codes that fall within the specified radius of another zip code. The returned zip codes are sorted by distance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String zipCode = "zipCode_example"; // String | 5 Digit US Zip Code
    Integer radius = 56; // Integer | Radius distance.  Max 322 km or 200 mi
    String uom = "mi"; // String | Unit of Measure
    try {
      GetRadius200Response result = apiInstance.getRadius(zipCode, radius, uom);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRadius");
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
| **zipCode** | **String**| 5 Digit US Zip Code | |
| **radius** | **Integer**| Radius distance.  Max 322 km or 200 mi | |
| **uom** | **String**| Unit of Measure | [enum: mi, km] |

### Return type

[**GetRadius200Response**](GetRadius200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Quota Exceeded. The error message will display how long in dd:hh:mi:ss for the quota to be reset. |  -  |

<a id="getZipcV1"></a>
# **getZipcV1**
> getZipcV1()

Validate License Key

Endpoint used to validate license key only. Returns 204 on Success

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getZipcV1();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getZipcV1");
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

null (empty response body)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |

<a id="getZipcode"></a>
# **getZipcode**
> GetZipcode200Response getZipcode(zipcode)

Zip Code Details

Gets the details of a single Zip code. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String zipcode = "zipcode_example"; // String | 5 Digit US Zip Code
    try {
      GetZipcode200Response result = apiInstance.getZipcode(zipcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getZipcode");
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
| **zipcode** | **String**| 5 Digit US Zip Code | |

### Return type

[**GetZipcode200Response**](GetZipcode200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Access Denied |  -  |
| **403** | Quota Exceeded. The error message will display how long in dd:hh:mi:ss for the quota to be reset. |  -  |

<a id="getZipcodes"></a>
# **getZipcodes**
> ZipCodeResponse getZipcodes(offset, limit, zipcode, uspsMainCityKey, zipClassificationCode, uspsFacilityCode, uspsDeliveryCode, uspsCarrierRouteSortCode, uniqueZipNameInd, uspsFinanceNumber, stateCode, stateFipsCode, countyFipsCode, divisionCode, regionCode, msaCode)

List all Zip Codes

Returns a list of zip codes. Results are always paginated. Visit the [Zip Code Data API](https://www.metadapi.com/API-Products/API-Product-Details/zip-code-api) product page for information on how to get an API key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://global.metadapi.com");
    
    // Configure API key authorization: subscription-key
    ApiKeyAuth subscription-key = (ApiKeyAuth) defaultClient.getAuthentication("subscription-key");
    subscription-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //subscription-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal offset = new BigDecimal("10"); // BigDecimal | Offset is the position in the dataset to start retrieval of records.
    BigDecimal limit = new BigDecimal("10"); // BigDecimal | Number of records to return in each page.
    String zipcode = "90210,33162"; // String | 5 Digit Zip Code query parameter. Can have multiple values (separated by comma).
    String uspsMainCityKey = "Z20259"; // String | Parameter for USPS City / Town key identifier for the main city of the zip code.
    String zipClassificationCode = "P"; // String | Parameter for zipClassificationCode
    String uspsFacilityCode = "B"; // String | Parameter for facility code.
    String uspsDeliveryCode = "uspsDeliveryCode_example"; // String | Parameter for delivery code.
    String uspsCarrierRouteSortCode = "uspsCarrierRouteSortCode_example"; // String | Parameter for carrier route sort code.
    Boolean uniqueZipNameInd = true; // Boolean | Parameter for unique zip name indicator.
    String uspsFinanceNumber = "uspsFinanceNumber_example"; // String | Parameter for finance number.
    String stateCode = "CA"; // String | Parameter for state code.
    String stateFipsCode = "06"; // String | Parameter for State FIPS code.
    String countyFipsCode = "037"; // String | Parameter for county FIPS code.
    String divisionCode = "9"; // String | Parameter for division code. 
    String regionCode = "4"; // String | Parameter for region code. 
    String msaCode = "31080"; // String | Parameter for msaCode.
    try {
      ZipCodeResponse result = apiInstance.getZipcodes(offset, limit, zipcode, uspsMainCityKey, zipClassificationCode, uspsFacilityCode, uspsDeliveryCode, uspsCarrierRouteSortCode, uniqueZipNameInd, uspsFinanceNumber, stateCode, stateFipsCode, countyFipsCode, divisionCode, regionCode, msaCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getZipcodes");
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
| **offset** | **BigDecimal**| Offset is the position in the dataset to start retrieval of records. | [optional] |
| **limit** | **BigDecimal**| Number of records to return in each page. | [optional] |
| **zipcode** | **String**| 5 Digit Zip Code query parameter. Can have multiple values (separated by comma). | [optional] |
| **uspsMainCityKey** | **String**| Parameter for USPS City / Town key identifier for the main city of the zip code. | [optional] |
| **zipClassificationCode** | **String**| Parameter for zipClassificationCode | [optional] |
| **uspsFacilityCode** | **String**| Parameter for facility code. | [optional] |
| **uspsDeliveryCode** | **String**| Parameter for delivery code. | [optional] |
| **uspsCarrierRouteSortCode** | **String**| Parameter for carrier route sort code. | [optional] |
| **uniqueZipNameInd** | **Boolean**| Parameter for unique zip name indicator. | [optional] |
| **uspsFinanceNumber** | **String**| Parameter for finance number. | [optional] |
| **stateCode** | **String**| Parameter for state code. | [optional] |
| **stateFipsCode** | **String**| Parameter for State FIPS code. | [optional] |
| **countyFipsCode** | **String**| Parameter for county FIPS code. | [optional] |
| **divisionCode** | **String**| Parameter for division code.  | [optional] |
| **regionCode** | **String**| Parameter for region code.  | [optional] |
| **msaCode** | **String**| Parameter for msaCode. | [optional] |

### Return type

[**ZipCodeResponse**](ZipCodeResponse.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

