# UserAgentApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**parseUserAgentV1UaUserAgentUrlencodedGet**](UserAgentApi.md#parseUserAgentV1UaUserAgentUrlencodedGet) | **GET** /v1/ua/{user_agent_urlencoded} | Get the information found in an User Agent. |
| [**parseUserAgentsCsvV1UaCsvPost**](UserAgentApi.md#parseUserAgentsCsvV1UaCsvPost) | **POST** /v1/ua/csv | Get the information found in the set of User Agents uploaded. |
| [**parseUserAgentsV1UaPost**](UserAgentApi.md#parseUserAgentsV1UaPost) | **POST** /v1/ua | Get the information found in a set of User Agents. |
| [**queryDeviceByCodeV1UaDeviceCodeGet**](UserAgentApi.md#queryDeviceByCodeV1UaDeviceCodeGet) | **GET** /v1/ua/device/{code} | Get the information of the device of a user agent. |
| [**queryFamilyByCodeV1UaFamilyCodeGet**](UserAgentApi.md#queryFamilyByCodeV1UaFamilyCodeGet) | **GET** /v1/ua/family/{code} | Get the information of the family of a user agent. |
| [**queryOsByCodeV1UaOsCodeGet**](UserAgentApi.md#queryOsByCodeV1UaOsCodeGet) | **GET** /v1/ua/os/{code} | Get the information of the Operating System of a user agent. |
| [**queryTypeByCodeV1UaTypeCodeGet**](UserAgentApi.md#queryTypeByCodeV1UaTypeCodeGet) | **GET** /v1/ua/type/{code} | Get the information of the type of a user agent. |
| [**queryVendorByCodeV1UaVendorCodeGet**](UserAgentApi.md#queryVendorByCodeV1UaVendorCodeGet) | **GET** /v1/ua/vendor/{code} | Get the information of the vendor of a user agent. |


<a id="parseUserAgentV1UaUserAgentUrlencodedGet"></a>
# **parseUserAgentV1UaUserAgentUrlencodedGet**
> UAOutput parseUserAgentV1UaUserAgentUrlencodedGet(userAgentUrlencoded)

Get the information found in an User Agent.

### What Get the information found in the User Agent passed as argument. This information includes: - Type - Render Engine - Version - Vendor - Operating System - Device - How common is the agent worldwide   ### Parameters The only argument accepted in the query string is an URL encoded User Agent string.  ### Result The result contains the following set of data:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;string&#x60;&#x60;:  The full user agent string passed as argument. - &#x60;&#x60;classification&#x60;&#x60;: The classification of the user agent. It can be one of the following: &#x60;&#x60;CRAWLER&#x60;&#x60;, &#x60;&#x60;CLIENT&#x60;&#x60;, &#x60;&#x60;UNKNOWN&#x60;&#x60;. - &#x60;&#x60;type&#x60;&#x60;: An URI to the type of user agent used to identify the client (browser, bot, crawler, etc.). - &#x60;&#x60;agent&#x60;&#x60;: Name of the agent and the version, if any. - &#x60;&#x60;engine&#x60;&#x60;: Agent render engine. - &#x60;&#x60;version&#x60;&#x60;: Version of the agent. - &#x60;&#x60;latest&#x60;&#x60;: Latests known version of the agent. - &#x60;&#x60;family&#x60;&#x60;: URI to the family of the agent. - &#x60;&#x60;vendor&#x60;&#x60;: URI to the vendor or company that produces the agent. - &#x60;&#x60;os&#x60;&#x60;: URI to the operating system used by the agent. - &#x60;&#x60;device&#x60;&#x60;: URI to the device used by the agent. - &#x60;&#x60;frequent&#x60;&#x60;: If the agent is frequently used worlwide or not. The values are &#x60;&#x60;COMMON&#x60;&#x60;, &#x60;&#x60;RARE&#x60;&#x60;, and &#x60;&#x60;UNKNOWN&#x60;&#x60;.   ### Errors The endpoint will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    String userAgentUrlencoded = "userAgentUrlencoded_example"; // String | 
    try {
      UAOutput result = apiInstance.parseUserAgentV1UaUserAgentUrlencodedGet(userAgentUrlencoded);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#parseUserAgentV1UaUserAgentUrlencodedGet");
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
| **userAgentUrlencoded** | **String**|  | |

### Return type

[**UAOutput**](UAOutput.md)

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

<a id="parseUserAgentsCsvV1UaCsvPost"></a>
# **parseUserAgentsCsvV1UaCsvPost**
> UACollectionOutput parseUserAgentsCsvV1UaCsvPost(csvFile)

Get the information found in the set of User Agents uploaded.

### What Get the information found in the list of User Agents uploaded as a CSV file. This information includes: - Type - Render Engine - Version - Vendor - Operating System - Device - How common is the agent worldwide  ### Parameters - A text file with a list of User Agents. - A header &#x60;Content-Type: multipart/form-data&#x60; is required.  Example: &#x60;&#x60;&#x60; curl -X &#39;POST&#39; \\   &#39;https://dublin.api.threatjammer.com/v1/ua/csv&#39; \\   -H &#39;accept: application/json&#39; \\   -H &#39;Authorization: Bearer YOUR_API_KEY&#39; \\   -H &#39;Content-Type: multipart/form-data&#39; \\   -F &#39;csv_file&#x3D;@YOUR_TEXT_FILE;type&#x3D;text/csv&#39; &#x60;&#x60;&#x60;  ### Result The result contains a list of the result for each User Agent, with the following data set:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;string&#x60;&#x60;:  The full user agent string passed as argument. - &#x60;&#x60;classification&#x60;&#x60;: The classification of the user agent. It can be one of the following: &#x60;&#x60;CRAWLER&#x60;&#x60;, &#x60;&#x60;CLIENT&#x60;&#x60;, &#x60;&#x60;UNKNOWN&#x60;&#x60;. - &#x60;&#x60;type&#x60;&#x60;: An URI to the type of user agent used to identify the client (browser, bot, crawler, etc.). - &#x60;&#x60;agent&#x60;&#x60;: Name of the agent and the version, if any. - &#x60;&#x60;engine&#x60;&#x60;: Agent render engine. - &#x60;&#x60;version&#x60;&#x60;: Version of the agent. - &#x60;&#x60;latest&#x60;&#x60;: Latests known version of the agent. - &#x60;&#x60;family&#x60;&#x60;: URI to the family of the agent. - &#x60;&#x60;vendor&#x60;&#x60;: URI to the vendor or company that produces the agent. - &#x60;&#x60;os&#x60;&#x60;: URI to the operating system used by the agent. - &#x60;&#x60;device&#x60;&#x60;: URI to the device used by the agent. - &#x60;&#x60;frequent&#x60;&#x60;: If the agent is frequently used worlwide or not. The values are &#x60;&#x60;COMMON&#x60;&#x60;, &#x60;&#x60;RARE&#x60;&#x60;, and &#x60;&#x60;UNKNOWN&#x60;&#x60;.   ### Errors The endpoint will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    File csvFile = new File("/path/to/file"); // File | The CSV file with the User Agents to parse
    try {
      UACollectionOutput result = apiInstance.parseUserAgentsCsvV1UaCsvPost(csvFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#parseUserAgentsCsvV1UaCsvPost");
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
| **csvFile** | **File**| The CSV file with the User Agents to parse | |

### Return type

[**UACollectionOutput**](UACollectionOutput.md)

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

<a id="parseUserAgentsV1UaPost"></a>
# **parseUserAgentsV1UaPost**
> UACollectionOutput parseUserAgentsV1UaPost(requestBody)

Get the information found in a set of User Agents.

### What Get the information found in the list of User Agents passed as argument. This information includes: - Type - Render Engine - Version - Vendor - Operating System - Device - How common is the agent worldwide  ### Parameters A list of User Agents are required in the body of the request.  ### Result The result contains a list of the result for each User Agent, with the following data set:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;string&#x60;&#x60;:  The full user agent string passed as argument. - &#x60;&#x60;classification&#x60;&#x60;: The classification of the user agent. It can be one of the following: &#x60;&#x60;CRAWLER&#x60;&#x60;, &#x60;&#x60;CLIENT&#x60;&#x60;, &#x60;&#x60;UNKNOWN&#x60;&#x60;. - &#x60;&#x60;type&#x60;&#x60;: An URI to the type of user agent used to identify the client (browser, bot, crawler, etc.). - &#x60;&#x60;agent&#x60;&#x60;: Name of the agent and the version, if any. - &#x60;&#x60;engine&#x60;&#x60;: Agent render engine. - &#x60;&#x60;version&#x60;&#x60;: Version of the agent. - &#x60;&#x60;latest&#x60;&#x60;: Latests known version of the agent. - &#x60;&#x60;family&#x60;&#x60;: URI to the family of the agent. - &#x60;&#x60;vendor&#x60;&#x60;: URI to the vendor or company that produces the agent. - &#x60;&#x60;os&#x60;&#x60;: URI to the operating system used by the agent. - &#x60;&#x60;device&#x60;&#x60;: URI to the device used by the agent. - &#x60;&#x60;frequent&#x60;&#x60;: If the agent is frequently used worlwide or not. The values are &#x60;&#x60;COMMON&#x60;&#x60;, &#x60;&#x60;RARE&#x60;&#x60;, and &#x60;&#x60;UNKNOWN&#x60;&#x60;.   ### Errors The endpoint will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    Set<String> requestBody = Arrays.asList(); // Set<String> | 
    try {
      UACollectionOutput result = apiInstance.parseUserAgentsV1UaPost(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#parseUserAgentsV1UaPost");
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

[**UACollectionOutput**](UACollectionOutput.md)

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

<a id="queryDeviceByCodeV1UaDeviceCodeGet"></a>
# **queryDeviceByCodeV1UaDeviceCodeGet**
> DeviceOutput queryDeviceByCodeV1UaDeviceCodeGet(code)

Get the information of the device of a user agent.

### What Obtain the details of a device of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the device origin of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the device. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the device. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the device in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    String code = "code_example"; // String | 
    try {
      DeviceOutput result = apiInstance.queryDeviceByCodeV1UaDeviceCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#queryDeviceByCodeV1UaDeviceCodeGet");
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
| **code** | **String**|  | |

### Return type

[**DeviceOutput**](DeviceOutput.md)

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

<a id="queryFamilyByCodeV1UaFamilyCodeGet"></a>
# **queryFamilyByCodeV1UaFamilyCodeGet**
> FamilyOutput queryFamilyByCodeV1UaFamilyCodeGet(code)

Get the information of the family of a user agent.

### What Obtain the details of a family of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the family of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the family. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the famly. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the family in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    String code = "code_example"; // String | 
    try {
      FamilyOutput result = apiInstance.queryFamilyByCodeV1UaFamilyCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#queryFamilyByCodeV1UaFamilyCodeGet");
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
| **code** | **String**|  | |

### Return type

[**FamilyOutput**](FamilyOutput.md)

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

<a id="queryOsByCodeV1UaOsCodeGet"></a>
# **queryOsByCodeV1UaOsCodeGet**
> OSOutput queryOsByCodeV1UaOsCodeGet(code)

Get the information of the Operating System of a user agent.

### What Obtain the details of the Operating System of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the Operating System at the origin of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the OS. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the OS. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the OS in the system. - &#x60;&#x60;family&#x60;&#x60;: the family of the OS. - &#x60;&#x60;vendor&#x60;&#x60;: the vendor or manufacturer of the OS.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    String code = "code_example"; // String | 
    try {
      OSOutput result = apiInstance.queryOsByCodeV1UaOsCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#queryOsByCodeV1UaOsCodeGet");
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
| **code** | **String**|  | |

### Return type

[**OSOutput**](OSOutput.md)

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

<a id="queryTypeByCodeV1UaTypeCodeGet"></a>
# **queryTypeByCodeV1UaTypeCodeGet**
> TypeOutput queryTypeByCodeV1UaTypeCodeGet(code)

Get the information of the type of a user agent.

### What Obtain the details of a type of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the type of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the type. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the type. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the type in the system. - &#x60;&#x60;type&#x60;&#x60;: the type of the User Agent. Can be &#x60;&#x60;INTERACTIVE&#x60;&#x60;, &#x60;&#x60;CRAWLER&#x60;&#x60; or &#x60;&#x60;UNKNOWN&#x60;&#x60; if the type is not known.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    String code = "code_example"; // String | 
    try {
      TypeOutput result = apiInstance.queryTypeByCodeV1UaTypeCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#queryTypeByCodeV1UaTypeCodeGet");
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
| **code** | **String**|  | |

### Return type

[**TypeOutput**](TypeOutput.md)

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

<a id="queryVendorByCodeV1UaVendorCodeGet"></a>
# **queryVendorByCodeV1UaVendorCodeGet**
> VendorOutput queryVendorByCodeV1UaVendorCodeGet(code)

Get the information of the vendor of a user agent.

### What Obtain the details of a vendor of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the vendor or manufacurer of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the vendor. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the vendor. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the vendor in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    UserAgentApi apiInstance = new UserAgentApi(defaultClient);
    String code = "code_example"; // String | 
    try {
      VendorOutput result = apiInstance.queryVendorByCodeV1UaVendorCodeGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAgentApi#queryVendorByCodeV1UaVendorCodeGet");
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
| **code** | **String**|  | |

### Return type

[**VendorOutput**](VendorOutput.md)

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

