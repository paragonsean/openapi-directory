# GeolocationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assessIpSetCsvV1GeoCsvPost**](GeolocationApi.md#assessIpSetCsvV1GeoCsvPost) | **POST** /v1/geo/csv | Get the geolocation data of all the IP addresses uploaded. |
| [**geolocateIpSetV1GeoPost**](GeolocationApi.md#geolocateIpSetV1GeoPost) | **POST** /v1/geo | Get the geolocation data of the IP addresses set. |
| [**geolocateIpV1GeoIpAddressGet**](GeolocationApi.md#geolocateIpV1GeoIpAddressGet) | **GET** /v1/geo/{ip_address} | Get the geo location data of the IP address. |


<a id="assessIpSetCsvV1GeoCsvPost"></a>
# **assessIpSetCsvV1GeoCsvPost**
> GeoIPCollectionOutput assessIpSetCsvV1GeoCsvPost(csvFile, strictParse)

Get the geolocation data of all the IP addresses uploaded.

### What Get the geo location data of all the IP addresses uploaded in a text file. This information includes: - Latitude and longitude - Time zone - Accuracy radius - Postal code - City name - Region - Country - Country of the service provider - Continent - Reverse PTR hostnames  ### Parameters - A text file with a list of public IPv4 or IPv6 addresses. - A header &#x60;Content-Type: multipart/form-data&#x60; is required. - (optional) in the query string the parameeter &#x60;strict_parse&#x60;: If set to &#x60;true&#x60;, no malformed IP addresses allowed, returning an error. If set to &#x60;false&#x60;, malformed IP addresses will be ignored.  Example: &#x60;&#x60;&#x60; curl -X &#39;POST&#39; \\   &#39;https://dublin.api.threatjammer.com/v1/geo/csv[?strict_parse&#x3D;true|false]&#39; \\   -H &#39;accept: application/json&#39; \\   -H &#39;Authorization: Bearer YOUR_API_KEY&#39; \\   -H &#39;Content-Type: multipart/form-data&#39; \\   -F &#39;csv_file&#x3D;@YOUR_TEXT_FILE;type&#x3D;text/csv&#39; &#x60;&#x60;&#x60;  ### Result The result contains a list of the result for each IP address, with the following data set:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;accuracy_radius&#x60;&#x60;:  The radius in kilometers around the specified location where the IP address is likely to be. - &#x60;&#x60;asn_country_iso_code&#x60;&#x60;: The ISO code of the country of the Autonomous System (AS) owner of the IP address. - &#x60;&#x60;city_geoname_code&#x60;&#x60;:&#x60;&#x60;: City geoname code. The geoname code by [GeoNames](https://en.wikipedia.org/wiki/GeoNames) is a unique identifier assigned to each geographical point on the globe. - &#x60;&#x60;city_name&#x60;&#x60;:&#x60;&#x60;: City name, in english. The developer can use the geoname code to localize the name of the city. - &#x60;&#x60;continent_code&#x60;&#x60;: The continent code. It can be any of the following: AF, AN, AS, EU, NA, OC, SA. - &#x60;&#x60;country_iso_code&#x60;&#x60;: The country ISO 3166-1 alpha-2 code. - &#x60;&#x60;hostnames&#x60;&#x60;: The list of hostnames associated with the IP address obtained from the reverse DNS lookup. - &#x60;&#x60;latitude&#x60;&#x60;: The latitude of the geolocation. - &#x60;&#x60;longitude&#x60;&#x60;: The longitude of the geolocation. - &#x60;&#x60;postal_code&#x60;&#x60;:&#x60;&#x60;: The postal code of the city. - &#x60;&#x60;region_geoname_code&#x60;&#x60;:&#x60;&#x60;: The geoname code of the region. - &#x60;&#x60;region_name&#x60;&#x60;:&#x60;&#x60;: The region name, in english. The developer can use the geoname code to localize the name of the region. - &#x60;&#x60;time_zone&#x60;&#x60;: The name of the time zone.   ### Errors The endpoint will return the following errors: - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  The private IP addresses will be ignored, if any.  When the &#x60;strict_parse&#x60; parameter is set to &#x60;true&#x60;, the endpoint will return the following errors: - a &#x60;400 Bad Request&#x60;.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeolocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    GeolocationApi apiInstance = new GeolocationApi(defaultClient);
    File csvFile = new File("/path/to/file"); // File | The CSV file with the IP addresses
    Boolean strictParse = false; // Boolean | When `true`, if any IP address entry in the file is malformed, the assessment is canceled. If `false`, the malformed IP addresses are ignored. Default is `false`.
    try {
      GeoIPCollectionOutput result = apiInstance.assessIpSetCsvV1GeoCsvPost(csvFile, strictParse);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeolocationApi#assessIpSetCsvV1GeoCsvPost");
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
| **csvFile** | **File**| The CSV file with the IP addresses | |
| **strictParse** | **Boolean**| When &#x60;true&#x60;, if any IP address entry in the file is malformed, the assessment is canceled. If &#x60;false&#x60;, the malformed IP addresses are ignored. Default is &#x60;false&#x60;. | [optional] [default to false] |

### Return type

[**GeoIPCollectionOutput**](GeoIPCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The server will return a valid answer in the following cases: |  -  |
| **422** | Validation Error |  -  |

<a id="geolocateIpSetV1GeoPost"></a>
# **geolocateIpSetV1GeoPost**
> GeoIPCollectionOutput geolocateIpSetV1GeoPost(requestBody)

Get the geolocation data of the IP addresses set.

### What Get the geo location data of all the IP addresses passed as argument. This information includes: - Latitude and longitude - Time zone - Accuracy radius - Postal code - City name - Region - Country - Country of the service provider - Continent - Reverse PTR hostnames  ### Parameters A list of public IPv4 or IPv6 addresses is required in the body of the request.  ### Result The result contains a list of the result for each IP address, with the following data set:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;accuracy_radius&#x60;&#x60;:  The radius in kilometers around the specified location where the IP address is likely to be. - &#x60;&#x60;asn_country_iso_code&#x60;&#x60;: The ISO code of the country of the Autonomous System (AS) owner of the IP address. - &#x60;&#x60;city_geoname_code&#x60;&#x60;:&#x60;&#x60;: City geoname code. The geoname code by [GeoNames](https://en.wikipedia.org/wiki/GeoNames) is a unique identifier assigned to each geographical point on the globe. - &#x60;&#x60;city_name&#x60;&#x60;:&#x60;&#x60;: City name, in english. The developer can use the geoname code to localize the name of the city. - &#x60;&#x60;continent_code&#x60;&#x60;: The continent code. It can be any of the following: AF, AN, AS, EU, NA, OC, SA. - &#x60;&#x60;country_iso_code&#x60;&#x60;: The country ISO 3166-1 alpha-2 code. - &#x60;&#x60;hostnames&#x60;&#x60;: The list of hostnames associated with the IP address obtained from the reverse DNS lookup. - &#x60;&#x60;latitude&#x60;&#x60;: The latitude of the geolocation. - &#x60;&#x60;longitude&#x60;&#x60;: The longitude of the geolocation. - &#x60;&#x60;postal_code&#x60;&#x60;:&#x60;&#x60;: The postal code of the city. - &#x60;&#x60;region_geoname_code&#x60;&#x60;:&#x60;&#x60;: The geoname code of the region. - &#x60;&#x60;region_name&#x60;&#x60;:&#x60;&#x60;: The region name, in english. The developer can use the geoname code to localize the name of the region. - &#x60;&#x60;time_zone&#x60;&#x60;: The name of the time zone.   ### Errors The endpoint will return the following errors: - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  The private IP addresses will be ignored, if any.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeolocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    GeolocationApi apiInstance = new GeolocationApi(defaultClient);
    Set<String> requestBody = Arrays.asList(); // Set<String> | 
    try {
      GeoIPCollectionOutput result = apiInstance.geolocateIpSetV1GeoPost(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeolocationApi#geolocateIpSetV1GeoPost");
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
| **requestBody** | [**Set&lt;String&gt;**](String.md)|  | |

### Return type

[**GeoIPCollectionOutput**](GeoIPCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The server will return a valid answer in the following cases: |  -  |
| **422** | Validation Error |  -  |

<a id="geolocateIpV1GeoIpAddressGet"></a>
# **geolocateIpV1GeoIpAddressGet**
> GeoIPOutput geolocateIpV1GeoIpAddressGet(ipAddress)

Get the geo location data of the IP address.

### What Get the geo location data of the IP address passed as argument. This information includes: - Latitude and longitude - Time zone - Accuracy radius - Postal code - City name - Region - Country - Country of the service provider - Continent - Reverse PTR hostnames   ### Parameters The only argument accepted in the query string is a public IPv4 or IPv6 addresses.  ### Result The result contains the following set of data:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;accuracy_radius&#x60;&#x60;:  The radius in kilometers around the specified location where the IP address is likely to be. - &#x60;&#x60;asn_country_iso_code&#x60;&#x60;: The ISO code of the country of the Autonomous System (AS) owner of the IP address. - &#x60;&#x60;city_geoname_code&#x60;&#x60;:&#x60;&#x60;: City geoname code. The geoname code by [GeoNames](https://en.wikipedia.org/wiki/GeoNames) is a unique identifier assigned to each geographical point on the globe. - &#x60;&#x60;city_name&#x60;&#x60;:&#x60;&#x60;: City name, in english. The developer can use the geoname code to localize the name of the city. - &#x60;&#x60;continent_code&#x60;&#x60;: The continent code. It can be any of the following: AF, AN, AS, EU, NA, OC, SA. - &#x60;&#x60;country_iso_code&#x60;&#x60;: The country ISO 3166-1 alpha-2 code. - &#x60;&#x60;hostnames&#x60;&#x60;: The list of hostnames associated with the IP address obtained from the reverse DNS lookup. - &#x60;&#x60;latitude&#x60;&#x60;: The latitude of the geolocation. - &#x60;&#x60;longitude&#x60;&#x60;: The longitude of the geolocation. - &#x60;&#x60;postal_code&#x60;&#x60;:&#x60;&#x60;: The postal code of the city. - &#x60;&#x60;region_geoname_code&#x60;&#x60;:&#x60;&#x60;: The geoname code of the region. - &#x60;&#x60;region_name&#x60;&#x60;:&#x60;&#x60;: The region name, in english. The developer can use the geoname code to localize the name of the region. - &#x60;&#x60;time_zone&#x60;&#x60;: The name of the time zone.   ### Errors The endpoint will return the following errors: - a &#x60;400 Bad Request&#x60; error if the IP address is not public. - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeolocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    GeolocationApi apiInstance = new GeolocationApi(defaultClient);
    String ipAddress = "ipAddress_example"; // String | 
    try {
      GeoIPOutput result = apiInstance.geolocateIpV1GeoIpAddressGet(ipAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeolocationApi#geolocateIpV1GeoIpAddressGet");
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
| **ipAddress** | **String**|  | |

### Return type

[**GeoIPOutput**](GeoIPOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The server will return a valid answer in the following cases: |  -  |
| **422** | Validation Error |  -  |

