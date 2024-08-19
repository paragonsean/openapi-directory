# AutonomousSystemsInformationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryAsnPrefixInformationV1AsnPrefixPost**](AutonomousSystemsInformationApi.md#queryAsnPrefixInformationV1AsnPrefixPost) | **POST** /v1/asn/prefix | Get the IPv4 or IPv6 prefix of the CIDR given. |
| [**queryAsnPrefixesListV1AsnNumberPrefixesGet**](AutonomousSystemsInformationApi.md#queryAsnPrefixesListV1AsnNumberPrefixesGet) | **GET** /v1/asn/{number}/prefixes | Get the list of IPv4 and IPv6 prefixes of the AS number given. |
| [**queryAsnV1AsnNumberGet**](AutonomousSystemsInformationApi.md#queryAsnV1AsnNumberGet) | **GET** /v1/asn/{number} | Get the Autonomous System details of the AS number given. |
| [**queryIPAddressNetworkInformationV1AsnIpIpAddressGet**](AutonomousSystemsInformationApi.md#queryIPAddressNetworkInformationV1AsnIpIpAddressGet) | **GET** /v1/asn/ip/{ip_address} | Get the IPv4 or IPv6 prefix of the IP address given. |
| [**queryRegistryByTheNameV1AsnRegistryCodeGet**](AutonomousSystemsInformationApi.md#queryRegistryByTheNameV1AsnRegistryCodeGet) | **GET** /v1/asn/registry/{code} | Get the information of a Regional Internet Registries (RIRs) given. |
| [**queryRegistryNamesV1AsnRegistryAllGet**](AutonomousSystemsInformationApi.md#queryRegistryNamesV1AsnRegistryAllGet) | **GET** /v1/asn/registry/all | Get the list of the Regional Internet Registries (RIRs) entities worldwide. |
| [**queryStatusByTheNameV1AsnStatusCodeGet**](AutonomousSystemsInformationApi.md#queryStatusByTheNameV1AsnStatusCodeGet) | **GET** /v1/asn/status/{code} | Get the information of a status given. |
| [**queryStatusNamesV1AsnStatusAllGet**](AutonomousSystemsInformationApi.md#queryStatusNamesV1AsnStatusAllGet) | **GET** /v1/asn/status/all | Get the list of status of an object in a registry. |


<a id="queryAsnPrefixInformationV1AsnPrefixPost"></a>
# **queryAsnPrefixInformationV1AsnPrefixPost**
> AutonomousSystemPrefixOutput queryAsnPrefixInformationV1AsnPrefixPost(bodyQueryAsnPrefixInformationV1AsnPrefixPost)

Get the IPv4 or IPv6 prefix of the CIDR given.

### What Obtain the IPv4 or IPv6 prefix and the Autonomous System information of the CIDR passed in the body as a POST method. This endpoint works around the problem of passing &#39;/&#39; addresses in the URI.  ### Parameters The endpoint accepts only the following parameter in the body as a JSON object: - &#x60;&#x60;prefix&#x60;&#x60;: (Mandatory) The CIDR v4 or v6 to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix. - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN. - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv4 or IPv6. - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry. - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry. - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD. - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.  ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the prefix information was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the CIDR is malformed.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    BodyQueryAsnPrefixInformationV1AsnPrefixPost bodyQueryAsnPrefixInformationV1AsnPrefixPost = new BodyQueryAsnPrefixInformationV1AsnPrefixPost(); // BodyQueryAsnPrefixInformationV1AsnPrefixPost | 
    try {
      AutonomousSystemPrefixOutput result = apiInstance.queryAsnPrefixInformationV1AsnPrefixPost(bodyQueryAsnPrefixInformationV1AsnPrefixPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryAsnPrefixInformationV1AsnPrefixPost");
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
| **bodyQueryAsnPrefixInformationV1AsnPrefixPost** | [**BodyQueryAsnPrefixInformationV1AsnPrefixPost**](BodyQueryAsnPrefixInformationV1AsnPrefixPost.md)|  | |

### Return type

[**AutonomousSystemPrefixOutput**](AutonomousSystemPrefixOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryAsnPrefixesListV1AsnNumberPrefixesGet"></a>
# **queryAsnPrefixesListV1AsnNumberPrefixesGet**
> AutonomousSystemPrefixesOutput queryAsnPrefixesListV1AsnNumberPrefixesGet(number)

Get the list of IPv4 and IPv6 prefixes of the AS number given.

### What Obtain the full list of IPv4 and IPv6 prefixes of the Autonomous System Number (ASN) passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;number&#x60;&#x60;: (Mandatory) The ASN number to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN. - &#x60;&#x60;prefixes_v4&#x60;&#x60;: the list of IPv4 prefixes that belong to the ASN. Each element of the list is a JSON object with the following structure:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix.     - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN.     - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv4.     - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry.     - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry.     - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD.     - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score. - &#x60;&#x60;prefixes_v6&#x60;&#x60;: the list of IPv6 prefixes that belong to the ASN. Each element of the list is a JSON object with the following structure:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv6 prefix.     - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN.     - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv6.     - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry.     - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry.     - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD.     - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.  ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the AS was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the AS number is malformed.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      AutonomousSystemPrefixesOutput result = apiInstance.queryAsnPrefixesListV1AsnNumberPrefixesGet(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryAsnPrefixesListV1AsnNumberPrefixesGet");
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
| **number** | **Integer**|  | |

### Return type

[**AutonomousSystemPrefixesOutput**](AutonomousSystemPrefixesOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryAsnV1AsnNumberGet"></a>
# **queryAsnV1AsnNumberGet**
> AutonomousSystemOutput queryAsnV1AsnNumberGet(number)

Get the Autonomous System details of the AS number given.

### What Obtain the full details of the Autonomous System Number (ASN) passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;number&#x60;&#x60;: (Mandatory) The ASN number to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;name&#x60;&#x60;: the name of the Autonomous System as registered in the registries databases. - &#x60;&#x60;description&#x60;&#x60;: the description of the Autonomous System as registered in the registries databases. - &#x60;&#x60;country_code&#x60;&#x60;: the ISO 3166-1 alpha-2 country code of the Autonomous System. - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the Autonomous System in the registry. The format is YYYY-MM-DD. - &#x60;&#x60;registry&#x60;&#x60;: the URI of the registry where the Autonomous System is registered. - &#x60;&#x60;status&#x60;&#x60;: the status of the Autonomous System as stored in the registry. - &#x60;&#x60;prefixes&#x60;&#x60;: the URI to the list of prefixes that belong to the Autonomous System. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the Autonomous System. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the Autonomous System. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the AS was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the AS number is malformed.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      AutonomousSystemOutput result = apiInstance.queryAsnV1AsnNumberGet(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryAsnV1AsnNumberGet");
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
| **number** | **Integer**|  | |

### Return type

[**AutonomousSystemOutput**](AutonomousSystemOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryIPAddressNetworkInformationV1AsnIpIpAddressGet"></a>
# **queryIPAddressNetworkInformationV1AsnIpIpAddressGet**
> AutonomousSystemPrefixOutput queryIPAddressNetworkInformationV1AsnIpIpAddressGet(ipAddress)

Get the IPv4 or IPv6 prefix of the IP address given.

### What Obtain the IPv4 or IPv6 prefix and the Autonomous System information of the IP address passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;ip_address&#x60;&#x60;: (Mandatory) The IPv4 or IPv6 address to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix. - &#x60;&#x60;asn&#x60;&#x60;: the URI to query the full details of the ASN. - &#x60;&#x60;object_type&#x60;&#x60;: the type of the prefix. The allowed values are: IPv4 or IPv6. - &#x60;&#x60;maintainer&#x60;&#x60;: the information about the maintainer of this prefix in the registry. - &#x60;&#x60;description&#x60;&#x60;: the description of the prefix as registered in the registry. - &#x60;&#x60;registry_date&#x60;&#x60;: the date of registration of the prefix in the registry. The format is YYYY-MM-DD. - &#x60;&#x60;registry_status&#x60;&#x60;: the URI of the status of the prefix as stored in the registry. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.  ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the prefix information was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    String ipAddress = "ipAddress_example"; // String | 
    try {
      AutonomousSystemPrefixOutput result = apiInstance.queryIPAddressNetworkInformationV1AsnIpIpAddressGet(ipAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryIPAddressNetworkInformationV1AsnIpIpAddressGet");
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

[**AutonomousSystemPrefixOutput**](AutonomousSystemPrefixOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryRegistryByTheNameV1AsnRegistryCodeGet"></a>
# **queryRegistryByTheNameV1AsnRegistryCodeGet**
> AutonomousSystemRegistryOutput queryRegistryByTheNameV1AsnRegistryCodeGet(code)

Get the information of a Regional Internet Registries (RIRs) given.

### What Obtain the information about the Regional Internet Registries (RIRs) given as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the RIR. Possible values are: iana, arin, ripencc, afrinic, apnic, lacnic.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual RIR. - &#x60;&#x60;name&#x60;&#x60;: the RIR name. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the RIR in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    String code = "iana"; // String | 
    try {
      AutonomousSystemRegistryOutput result = apiInstance.queryRegistryByTheNameV1AsnRegistryCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryRegistryByTheNameV1AsnRegistryCodeGet");
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
| **code** | **String**|  | [enum: iana, arin, ripencc, afrinic, apnic, lacnic] |

### Return type

[**AutonomousSystemRegistryOutput**](AutonomousSystemRegistryOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryRegistryNamesV1AsnRegistryAllGet"></a>
# **queryRegistryNamesV1AsnRegistryAllGet**
> List&lt;AutonomousSystemRegistryOutput&gt; queryRegistryNamesV1AsnRegistryAllGet()

Get the list of the Regional Internet Registries (RIRs) entities worldwide.

### What Obtain the list of Regional Internet Registries (RIRs) entities worldwide.  ### Parameters No parameters are required.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual RIR. - &#x60;&#x60;name&#x60;&#x60;: the RIR name. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the RIR in the system. Possible values are: iana, arin, ripencc, afrinic, apnic, lacnic.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    try {
      List<AutonomousSystemRegistryOutput> result = apiInstance.queryRegistryNamesV1AsnRegistryAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryRegistryNamesV1AsnRegistryAllGet");
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

[**List&lt;AutonomousSystemRegistryOutput&gt;**](AutonomousSystemRegistryOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="queryStatusByTheNameV1AsnStatusCodeGet"></a>
# **queryStatusByTheNameV1AsnStatusCodeGet**
> AutonomousSystemStatusOutput queryStatusByTheNameV1AsnStatusCodeGet(code)

Get the information of a status given.

### What Obtain the information about the status of an object in the registry as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the status in the registry. Possible values are: assigned, reserved, allocated, available.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;name&#x60;&#x60;: the human readable name of the status. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the status in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    String code = "assigned"; // String | 
    try {
      AutonomousSystemStatusOutput result = apiInstance.queryStatusByTheNameV1AsnStatusCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryStatusByTheNameV1AsnStatusCodeGet");
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
| **code** | **String**|  | [enum: assigned, reserved, available, allocated] |

### Return type

[**AutonomousSystemStatusOutput**](AutonomousSystemStatusOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryStatusNamesV1AsnStatusAllGet"></a>
# **queryStatusNamesV1AsnStatusAllGet**
> List&lt;AutonomousSystemStatusOutput&gt; queryStatusNamesV1AsnStatusAllGet()

Get the list of status of an object in a registry.

### What Obtain the list of status of an object can be in a registry.  ### Parameters No parameters are required.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;name&#x60;&#x60;: the code name. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the status in the system. Possible values are: assigned, reserved, allocated, available.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutonomousSystemsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AutonomousSystemsInformationApi apiInstance = new AutonomousSystemsInformationApi(defaultClient);
    try {
      List<AutonomousSystemStatusOutput> result = apiInstance.queryStatusNamesV1AsnStatusAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutonomousSystemsInformationApi#queryStatusNamesV1AsnStatusAllGet");
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

[**List&lt;AutonomousSystemStatusOutput&gt;**](AutonomousSystemStatusOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

