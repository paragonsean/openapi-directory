# OriginManagementInThisRegionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryAllOriginInformationV1OriginAllGet**](OriginManagementInThisRegionApi.md#queryAllOriginInformationV1OriginAllGet) | **GET** /v1/origin/all | Get the information of the origins of the user in the region. |
| [**queryOriginAddressStatusInformationV1OriginAddressesGet**](OriginManagementInThisRegionApi.md#queryOriginAddressStatusInformationV1OriginAddressesGet) | **GET** /v1/origin/addresses | Get the address status of the origin of the user in the region. |
| [**queryOriginCookieIdStatusInformationV1OriginCookiesGet**](OriginManagementInThisRegionApi.md#queryOriginCookieIdStatusInformationV1OriginCookiesGet) | **GET** /v1/origin/cookies | Get the tracking cookie ID status of the origin of the user in the region. |
| [**queryOriginInformationV1OriginGet**](OriginManagementInThisRegionApi.md#queryOriginInformationV1OriginGet) | **GET** /v1/origin | Get the information of an origin of the user in the region. |
| [**queryOriginScriptsV1OriginScriptsGet**](OriginManagementInThisRegionApi.md#queryOriginScriptsV1OriginScriptsGet) | **GET** /v1/origin/scripts | Get the code snippets of an origin of the user in the region. |
| [**queryOriginStatusDetailV1OriginStatusDetailStatusIdGet**](OriginManagementInThisRegionApi.md#queryOriginStatusDetailV1OriginStatusDetailStatusIdGet) | **GET** /v1/origin/status/detail/{status_id} | Get detail of a status available in the platform. |
| [**queryOriginStatusDetailsV1OriginStatusDetailsGet**](OriginManagementInThisRegionApi.md#queryOriginStatusDetailsV1OriginStatusDetailsGet) | **GET** /v1/origin/status/details | Get the list of different status available in the platform. |
| [**queryOriginStatusV1OriginStatusPost**](OriginManagementInThisRegionApi.md#queryOriginStatusV1OriginStatusPost) | **POST** /v1/origin/status | Get the current cookie ID and IP address status of the origin of user in the region. |
| [**queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet**](OriginManagementInThisRegionApi.md#queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet) | **GET** /v1/origin/traffic/analysis | Get the traffic analysis of the origin. |
| [**queryOriginTrafficClientV1OriginClientAnalysisGet**](OriginManagementInThisRegionApi.md#queryOriginTrafficClientV1OriginClientAnalysisGet) | **GET** /v1/origin/client/analysis | Get the type of clients of the trafffic of the origin. |
| [**updateConfigurationOriginV1OriginPut**](OriginManagementInThisRegionApi.md#updateConfigurationOriginV1OriginPut) | **PUT** /v1/origin | Update the configuration of an origin of the user in the region. |
| [**updateOriginStatusV1OriginStatusPut**](OriginManagementInThisRegionApi.md#updateOriginStatusV1OriginStatusPut) | **PUT** /v1/origin/status | Update the status of a given origin event in the platform. |


<a id="queryAllOriginInformationV1OriginAllGet"></a>
# **queryAllOriginInformationV1OriginAllGet**
> OriginCollectionOutput queryAllOriginInformationV1OriginAllGet()

Get the information of the origins of the user in the region.

### What Obtain the attributes of all the origins of the user in the selected region. The purpose of this function is to display the information of configuration of the origins and also access to the live data of the origins.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters No parameters are required.  ### Result The result is a list of JSON objects with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain all the origins of the user. - &#x60;&#x60;origins&#x60;&#x60;: A list of JSON objects with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of an origin.     - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid.     - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;.     - &#x60;&#x60;token&#x60;&#x60;: the URI to the request to obtain the token of the origin.     - &#x60;&#x60;data&#x60;&#x60;: a JSON object containing all the parameters of the origin as key-value pairs.     - &#x60;&#x60;logs&#x60;&#x60;: the URI to the request to obtain the log activity in the origin.     - &#x60;&#x60;addresses&#x60;&#x60;: the URI to the request to obtain the list of IP addresses active in the origin.     - &#x60;&#x60;cookies&#x60;&#x60;: the URI to the request to obtain the list of cookies active in the origin.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    try {
      OriginCollectionOutput result = apiInstance.queryAllOriginInformationV1OriginAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryAllOriginInformationV1OriginAllGet");
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

[**OriginCollectionOutput**](OriginCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="queryOriginAddressStatusInformationV1OriginAddressesGet"></a>
# **queryOriginAddressStatusInformationV1OriginAddressesGet**
> OriginAddressStatusCollectionOutput queryOriginAddressStatusInformationV1OriginAddressesGet(query, page, pageSize)

Get the address status of the origin of the user in the region.

### What  Obtain the status that trigger the change in the status of the origin of a specific IP address. The status will also describe the current state of the status and the information that triggered the change.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of the status of an origin. - &#x60;&#x60;addresses&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;address&#x60;&#x60;: the IP address of the origin.     - &#x60;&#x60;status&#x60;&#x60;: the status of IP address for the given origin.     - &#x60;&#x60;log_id&#x60;&#x60;: the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin status was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    Integer page = 1; // Integer | The page to be returned
    Integer pageSize = 20; // Integer | The number of items per page
    try {
      OriginAddressStatusCollectionOutput result = apiInstance.queryOriginAddressStatusInformationV1OriginAddressesGet(query, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginAddressStatusInformationV1OriginAddressesGet");
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
| **query** | **String**| The origin site to query | |
| **page** | **Integer**| The page to be returned | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items per page | [optional] [default to 20] |

### Return type

[**OriginAddressStatusCollectionOutput**](OriginAddressStatusCollectionOutput.md)

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

<a id="queryOriginCookieIdStatusInformationV1OriginCookiesGet"></a>
# **queryOriginCookieIdStatusInformationV1OriginCookiesGet**
> OriginCookieIdStatusCollectionOutput queryOriginCookieIdStatusInformationV1OriginCookiesGet(query, page, pageSize)

Get the tracking cookie ID status of the origin of the user in the region.

### What  Obtain the status that trigger the change in the status of the origin of the cookie ID used to track the users. The status will also describe the current state of the status and the information that triggered the change.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of the status of an origin. - &#x60;&#x60;addresses&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;cookie_id&#x60;&#x60;: the ID of the tracking cookie for the origin.     - &#x60;&#x60;status&#x60;&#x60;: the status of tracking cookie ID for the given origin.     - &#x60;&#x60;log_id&#x60;&#x60;: the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin status was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    Integer page = 1; // Integer | The page to be returned
    Integer pageSize = 20; // Integer | The number of items per page
    try {
      OriginCookieIdStatusCollectionOutput result = apiInstance.queryOriginCookieIdStatusInformationV1OriginCookiesGet(query, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginCookieIdStatusInformationV1OriginCookiesGet");
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
| **query** | **String**| The origin site to query | |
| **page** | **Integer**| The page to be returned | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items per page | [optional] [default to 20] |

### Return type

[**OriginCookieIdStatusCollectionOutput**](OriginCookieIdStatusCollectionOutput.md)

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

<a id="queryOriginInformationV1OriginGet"></a>
# **queryOriginInformationV1OriginGet**
> OriginOutput queryOriginInformationV1OriginGet(query)

Get the information of an origin of the user in the region.

### What Obtain the attributes of the origin of the user passed as argument in the selected region. The purpose of this function is to display the information of configuration of the origin and also access to the live data of the origin.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of an origin. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;token&#x60;&#x60;: the URI to the request to obtain the token of the origin. - &#x60;&#x60;data&#x60;&#x60;: a JSON object containing all the parameters of the origin as key-value pairs. - &#x60;&#x60;logs&#x60;&#x60;: the URI to the request to obtain the log activity in the origin. - &#x60;&#x60;addresses&#x60;&#x60;: the URI to the request to obtain the list of IP addresses active in the origin. - &#x60;&#x60;cookies&#x60;&#x60;: the URI to the request to obtain the list of cookies active in the origin. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    try {
      OriginOutput result = apiInstance.queryOriginInformationV1OriginGet(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginInformationV1OriginGet");
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
| **query** | **String**| The origin site to query | |

### Return type

[**OriginOutput**](OriginOutput.md)

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

<a id="queryOriginScriptsV1OriginScriptsGet"></a>
# **queryOriginScriptsV1OriginScriptsGet**
> OriginScriptsOutput queryOriginScriptsV1OriginScriptsGet(query)

Get the code snippets of an origin of the user in the region.

### What Obtain the code snippets of the origin of the user passed as argument in the selected region. The purpose of this function is to help the user to integrate the javascript library in their website with a preconfigured script that contains the origin token.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of an origin. - &#x60;&#x60;detection&#x60;&#x60;: code snippet to integrate into the website described in the origin to detect malicious activity.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    try {
      OriginScriptsOutput result = apiInstance.queryOriginScriptsV1OriginScriptsGet(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginScriptsV1OriginScriptsGet");
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
| **query** | **String**| The origin site to query | |

### Return type

[**OriginScriptsOutput**](OriginScriptsOutput.md)

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

<a id="queryOriginStatusDetailV1OriginStatusDetailStatusIdGet"></a>
# **queryOriginStatusDetailV1OriginStatusDetailStatusIdGet**
> OriginStatusDetailsOutput queryOriginStatusDetailV1OriginStatusDetailStatusIdGet(statusId)

Get detail of a status available in the platform.

### What Obtain the description of a status available in the platform.  ### Parameters A &#x60;status_id&#x60; parameter in the path of the request: - &#x60;PASS&#x60; - &#x60;BLOCK&#x60; - &#x60;CHALLENGE&#x60; - &#x60;BYPASS&#x60; - &#x60;IGNORE&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status detail. - &#x60;&#x60;description&#x60;&#x60;: a human readable description of the status. - &#x60;&#x60;cardinality&#x60;&#x60;: The number describing the cardinality of the status.  ### Errors - a &#x60;400 Bad Request&#x60; error if the origin status is not any of the available ones.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String statusId = "pass"; // String | The status id to query the details
    try {
      OriginStatusDetailsOutput result = apiInstance.queryOriginStatusDetailV1OriginStatusDetailStatusIdGet(statusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginStatusDetailV1OriginStatusDetailStatusIdGet");
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
| **statusId** | **String**| The status id to query the details | [enum: pass, block, challenge, bypass, ignore] |

### Return type

[**OriginStatusDetailsOutput**](OriginStatusDetailsOutput.md)

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

<a id="queryOriginStatusDetailsV1OriginStatusDetailsGet"></a>
# **queryOriginStatusDetailsV1OriginStatusDetailsGet**
> OriginStatusDetailsCollectionOutput queryOriginStatusDetailsV1OriginStatusDetailsGet()

Get the list of different status available in the platform.

### What Obtain the full list and description of the different status available in the platform.  ### Parameters No parameters needed.  ### Result The result is a JSON list with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the list. - &#x60;&#x60;list&#x60;&#x60;: a JSON list with the following elements each one with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to the status detail.     - &#x60;&#x60;description&#x60;&#x60;: a human readable description of the status.     - &#x60;&#x60;cardinality&#x60;&#x60;: The number describing the cardinality of the status.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    try {
      OriginStatusDetailsCollectionOutput result = apiInstance.queryOriginStatusDetailsV1OriginStatusDetailsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginStatusDetailsV1OriginStatusDetailsGet");
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

[**OriginStatusDetailsCollectionOutput**](OriginStatusDetailsCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="queryOriginStatusV1OriginStatusPost"></a>
# **queryOriginStatusV1OriginStatusPost**
> OriginStatusOutput queryOriginStatusV1OriginStatusPost(query, bodyQueryOriginStatusV1OriginStatusPost)

Get the current cookie ID and IP address status of the origin of user in the region.

### What  Obtain the current status of the origin for a given IP address and/or cookie ID. The values can be correlated, but they are not required to be. The status will also describe the following information: - &#x60;PASS&#x60;: The traffic should not be intercepted, but should be analyzed and a positive detection should trigger a change in the status. - &#x60;BLOCK&#x60;: The traffic must be intercepted and redirected to a blocking page. Only a timeout of the IP address or Cookie ID, a solved challenge or a manual status change can change the status. - &#x60;CHALLENGE&#x60;: The traffic must be intercepted and redirected to a page where the user must solve a challenge. If the challenge is succesfully solved the status will change to &#x60;PASS&#x60;. If the user fails to change the challenge a specific amount of times, the status can change to &#x60;BLOCK&#x60;. - &#x60;BYPASS&#x60;: The traffic should not be tapped even if it is suspected to be malicious, as long as the timeout has not expired. When the timeout is reached, it should revert to a previous state instead of going to &#x60;PASS&#x60;. - &#x60;IGNORE&#x60;: Whatever happens to the traffic of the user, it should not be tapped. Once the time expires, it should return to the state PASS.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The body should have at least one of the following fields: - &#x60;address&#x60;: The IP address of the user to query. - &#x60;cookie_id&#x60;: The ID of the tracking cookie of the user to query.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of the &#x60;cookie_id&#x60; and &#x60;address&#x60; status of an origin. - &#x60;&#x60;cookie_id&#x60;&#x60;: a JSON object with the following fields:     - &#x60;&#x60;cookie_id&#x60;&#x60;: the ID of the tracking cookie for the origin.     - &#x60;&#x60;status&#x60;&#x60;: the URI to the status detail of the cookie ID.     - &#x60;&#x60;log_id&#x60;&#x60;: (Optional) the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: (Optional) the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: (Optional) the date and time when the origin status was last updated in UNIX timestamp in milliseconds. - &#x60;&#x60;address&#x60;&#x60;: a JSON object with the following fields:     - &#x60;&#x60;address&#x60;&#x60;: the address for the origin.     - &#x60;&#x60;status&#x60;&#x60;: the URI to the status detail of the cookie ID.     - &#x60;&#x60;log_id&#x60;&#x60;: (Optional) the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: (Optional) the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: (Optional) the date and time when the origin status was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    BodyQueryOriginStatusV1OriginStatusPost bodyQueryOriginStatusV1OriginStatusPost = new BodyQueryOriginStatusV1OriginStatusPost(); // BodyQueryOriginStatusV1OriginStatusPost | 
    try {
      OriginStatusOutput result = apiInstance.queryOriginStatusV1OriginStatusPost(query, bodyQueryOriginStatusV1OriginStatusPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginStatusV1OriginStatusPost");
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
| **query** | **String**| The origin site to query | |
| **bodyQueryOriginStatusV1OriginStatusPost** | [**BodyQueryOriginStatusV1OriginStatusPost**](BodyQueryOriginStatusV1OriginStatusPost.md)|  | [optional] |

### Return type

[**OriginStatusOutput**](OriginStatusOutput.md)

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

<a id="queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet"></a>
# **queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet**
> OriginTrafficAnalysisCollectionOutput queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet(query, interval, fromTimestamp, toTimestamp)

Get the traffic analysis of the origin.

### What Obtain the traffic analysis of the origin in the specified time range and interval. Theanalysis will return the number of requests and the anomalies detected like:  - number of requests - overall score - malicious synthetic traffic (bad bot traffic) - IP in a denylist - IP in a datacenter - user uses a headless webdriver - Autonomous System (ASN) of the IP is risky - The location of the IP address and the ASN is different  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  To restrict the analysis to a specific time range, add the following parameters to the querystring: - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: (Optional) the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: (Optional) the interval of the analysis in minutes. The default value is 60 minutes (HOURLY). Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the traffic analysis for the origin. - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: the interval of the analysis. Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;. - &#x60;&#x60;data&#x60;&#x60;: a JSON list with the following elements each one with the following fields:     - &#x60;&#x60;timestamp&#x60;&#x60;: the date and time of the analysis in UNIX timestamp in milliseconds.     - &#x60;&#x60;total&#x60;&#x60;: the total number of requests.     - &#x60;&#x60;score_high&#x60;&#x60;: the number of requests with a high score (bad traffic).     - &#x60;&#x60;bots&#x60;&#x60;: the number of requests from bad bots.     - &#x60;&#x60;denylists&#x60;&#x60;: the number of requests from IPs in a denylist.     - &#x60;&#x60;datacenters&#x60;&#x60;: the number of requests from IPs in a datacenter.     - &#x60;&#x60;webdrivers&#x60;&#x60;: the number of requests from IPs using a headless webdriver.     - &#x60;&#x60;asn_risky&#x60;&#x60;: the number of requests from IPs with a risky ASN.     - &#x60;&#x60;network_country_mismatches&#x60;&#x60;: the number of requests from IPs with a different location than the ASN.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    String interval = "HOURLY"; // String | The data inteval to aggregate the result dataset
    Integer fromTimestamp = 56; // Integer | A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after or equal to this value.
    Integer toTimestamp = 56; // Integer | A UNIX timestamp in milliseconds to restrict the results of the query to entries logged before this value.
    try {
      OriginTrafficAnalysisCollectionOutput result = apiInstance.queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet(query, interval, fromTimestamp, toTimestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginTrafficAnalysisV1OriginTrafficAnalysisGet");
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
| **query** | **String**| The origin site to query | |
| **interval** | **String**| The data inteval to aggregate the result dataset | [enum: HOURLY] |
| **fromTimestamp** | **Integer**| A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after or equal to this value. | |
| **toTimestamp** | **Integer**| A UNIX timestamp in milliseconds to restrict the results of the query to entries logged before this value. | [optional] |

### Return type

[**OriginTrafficAnalysisCollectionOutput**](OriginTrafficAnalysisCollectionOutput.md)

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

<a id="queryOriginTrafficClientV1OriginClientAnalysisGet"></a>
# **queryOriginTrafficClientV1OriginClientAnalysisGet**
> OriginClientAnalysisCollectionOutput queryOriginTrafficClientV1OriginClientAnalysisGet(query, interval, fromTimestamp, toTimestamp)

Get the type of clients of the trafffic of the origin.

### What Obtain the type of clients of trhe traffic in the specified time range and interval. Thequery will return the number of requests and the different type of CLIENTs and CRAWLERs.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  To restrict the query to a specific time range, add the following parameters to the querystring: - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: (Optional) the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: (Optional) the interval of the analysis in minutes. The default value is 60 minutes (HOURLY). Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the traffic client analysis for the origin. - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: the interval of the analysis. Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;. - &#x60;&#x60;data&#x60;&#x60;: a JSON list with the following elements each one with the following fields:     - &#x60;&#x60;timestamp&#x60;&#x60;: the date and time of the analysis in UNIX timestamp in milliseconds.     - &#x60;&#x60;total&#x60;&#x60;: the total number of requests.     - &#x60;&#x60;client_*&#x60;&#x60;: the number of requests from a specific client. The possible clients are: &#x60;&#x60;browser&#x60;&#x60;, &#x60;&#x60;crawler&#x60;&#x60;, &#x60;&#x60;email&#x60;&#x60;, &#x60;&#x60;library&#x60;&#x60;, &#x60;&#x60;mobile_browser&#x60;&#x60;, &#x60;&#x60;multimedia_player&#x60;&#x60;, &#x60;&#x60;offline_browser&#x60;&#x60;, &#x60;&#x60;unrecognized&#x60;&#x60;, &#x60;&#x60;ua_anonymizer&#x60;&#x60;, &#x60;&#x60;validator&#x60;&#x60;, &#x60;&#x60;wap_browser&#x60;&#x60;.     - &#x60;&#x60;crawler_*&#x60;&#x60;: the number of requests from a specific crawler. The possible crawlers are:&#x60;&#x60;feed_fetcher&#x60;&#x60;, &#x60;&#x60;link_checker&#x60;&#x60;, &#x60;&#x60;marketing&#x60;&#x60;, &#x60;&#x60;screenshot_creator&#x60;&#x60;, &#x60;&#x60;search_engine_bot&#x60;&#x60;,&#x60;&#x60;site_monitor&#x60;&#x60;, &#x60;&#x60;speed_tester&#x60;&#x60;, &#x60;&#x60;tool&#x60;&#x60;, &#x60;&#x60;uncategorized&#x60;&#x60;, &#x60;&#x60;unrecognized&#x60;&#x60;, &#x60;&#x60;virus_scanner&#x60;&#x60;,&#x60;&#x60;vulnerability_scanner&#x60;&#x60;, &#x60;&#x60;web_scraper&#x60;&#x60;.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    String interval = "HOURLY"; // String | The data inteval to aggregate the result dataset
    Integer fromTimestamp = 56; // Integer | A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after or equal to this value.
    Integer toTimestamp = 56; // Integer | A UNIX timestamp in milliseconds to restrict the results of the query to entries logged before this value.
    try {
      OriginClientAnalysisCollectionOutput result = apiInstance.queryOriginTrafficClientV1OriginClientAnalysisGet(query, interval, fromTimestamp, toTimestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#queryOriginTrafficClientV1OriginClientAnalysisGet");
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
| **query** | **String**| The origin site to query | |
| **interval** | **String**| The data inteval to aggregate the result dataset | [enum: HOURLY] |
| **fromTimestamp** | **Integer**| A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after or equal to this value. | |
| **toTimestamp** | **Integer**| A UNIX timestamp in milliseconds to restrict the results of the query to entries logged before this value. | [optional] |

### Return type

[**OriginClientAnalysisCollectionOutput**](OriginClientAnalysisCollectionOutput.md)

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

<a id="updateConfigurationOriginV1OriginPut"></a>
# **updateConfigurationOriginV1OriginPut**
> Object updateConfigurationOriginV1OriginPut(bodyUpdateConfigurationOriginV1OriginPut)

Update the configuration of an origin of the user in the region.

### What Modify the configuration metadata of the origin of the user in the selected region.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the body of the request, add the &#x60;origin&#x60; of the user and the &#x60;config&#x60; parameter with the following format for the &#x60;origin&#x60;:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  The &#x60;config&#x60; parameter is a JSON object containing the configuration of the origin. It only accepts the existing parameters obtained from the &#x60;GET&#x60; request of the origin. If the parameter is not present in the &#x60;config&#x60; object, it will fail to store it. It&#39;s not necessary to send all the parameters, only the ones that need to be updated.  ### Result The result is the JSON object with all the new values of the origin configuration.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format. - a &#x60;400 Bad Request&#x60; error if the &#x60;config&#x60; parameter is not a JSON object or unknown parameters are sent.  It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    BodyUpdateConfigurationOriginV1OriginPut bodyUpdateConfigurationOriginV1OriginPut = new BodyUpdateConfigurationOriginV1OriginPut(); // BodyUpdateConfigurationOriginV1OriginPut | 
    try {
      Object result = apiInstance.updateConfigurationOriginV1OriginPut(bodyUpdateConfigurationOriginV1OriginPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#updateConfigurationOriginV1OriginPut");
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
| **bodyUpdateConfigurationOriginV1OriginPut** | [**BodyUpdateConfigurationOriginV1OriginPut**](BodyUpdateConfigurationOriginV1OriginPut.md)|  | |

### Return type

**Object**

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

<a id="updateOriginStatusV1OriginStatusPut"></a>
# **updateOriginStatusV1OriginStatusPut**
> Object updateOriginStatusV1OriginStatusPut(query, bodyUpdateOriginStatusV1OriginStatusPut)

Update the status of a given origin event in the platform.

### What Update the status of a given origin event in the platform. The status can be one of the    following values: - &#x60;PASS&#x60;: The event is not considered as a threat. - &#x60;BLOCK&#x60;: The event is considered as a threat and the origin must be blocked. - &#x60;CHALLENGE&#x60;: The event is considered as a threat and the origin must be challenged. - &#x60;BYPASS&#x60;: The event is considered as a threat but the origin must be bypassed. - &#x60;IGNORE&#x60;: The event is considered as a threat but the origin must be ignored.  To apply the change, it&#39;s necessary to send a request to the API with the &#x60;log_id&#x60; of the    origin status event and the scope of the change. The scope can be one of the following values: - &#x60;address_and_cookie&#x60;: The change will be applied to the origin IP address and the cookie. - &#x60;address&#x60;: The change will be applied to the origin IP address. - &#x60;cookie&#x60;: The change will be applied to the cookie.  ### Parameters The request must send the following parameters in the body of the request: - &#x60;&#x60;log_id&#x60;&#x60;: the log id of the origin status event. - &#x60;&#x60;scope&#x60;&#x60;: the scope of the change. Possible values are: &#x60;&#x60;address_and_cookie&#x60;&#x60;, &#x60;&#x60;address&#x60;&#x60;, &#x60;&#x60;cookie&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: the new status of the origin. Possible values are: &#x60;&#x60;pass&#x60;&#x60;, &#x60;&#x60;block&#x60;&#x60;, &#x60;&#x60;challenge&#x60;&#x60;, &#x60;&#x60;bypass&#x60;&#x60;, &#x60;&#x60;ignore&#x60;&#x60;.  And in the &#x60;query&#x60; query string parameter, add the origin website in the format &#x60;https://example.com&#x60;.  ### Result A 200 OK response without any content.  ### Errors It will return the API Global errors described in the API description. If the parameters are invalid, it will return a &#x60;400 Bad Request&#x60; error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginManagementInThisRegionApi apiInstance = new OriginManagementInThisRegionApi(defaultClient);
    String query = "query_example"; // String | The origin site to query
    BodyUpdateOriginStatusV1OriginStatusPut bodyUpdateOriginStatusV1OriginStatusPut = new BodyUpdateOriginStatusV1OriginStatusPut(); // BodyUpdateOriginStatusV1OriginStatusPut | 
    try {
      Object result = apiInstance.updateOriginStatusV1OriginStatusPut(query, bodyUpdateOriginStatusV1OriginStatusPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginManagementInThisRegionApi#updateOriginStatusV1OriginStatusPut");
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
| **query** | **String**| The origin site to query | |
| **bodyUpdateOriginStatusV1OriginStatusPut** | [**BodyUpdateOriginStatusV1OriginStatusPut**](BodyUpdateOriginStatusV1OriginStatusPut.md)|  | [optional] |

### Return type

**Object**

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

