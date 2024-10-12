# DefaultApi

All URIs are relative to *http://worldtimeapi.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ipGet**](DefaultApi.md#ipGet) | **GET** /ip | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data. |
| [**ipIpv4Get**](DefaultApi.md#ipIpv4Get) | **GET** /ip/{ipv4} | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data. |
| [**ipIpv4TxtGet**](DefaultApi.md#ipIpv4TxtGet) | **GET** /ip/{ipv4}.txt | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data. |
| [**ipTxtGet**](DefaultApi.md#ipTxtGet) | **GET** /ip.txt | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data. |
| [**timezoneAreaGet**](DefaultApi.md#timezoneAreaGet) | **GET** /timezone/{area} | a listing of all timezones available for that area. |
| [**timezoneAreaLocationGet**](DefaultApi.md#timezoneAreaLocationGet) | **GET** /timezone/{area}/{location} | request the current time for a timezone. |
| [**timezoneAreaLocationRegionGet**](DefaultApi.md#timezoneAreaLocationRegionGet) | **GET** /timezone/{area}/{location}/{region} | request the current time for a timezone. |
| [**timezoneAreaLocationRegionTxtGet**](DefaultApi.md#timezoneAreaLocationRegionTxtGet) | **GET** /timezone/{area}/{location}/{region}.txt | request the current time for a timezone. |
| [**timezoneAreaLocationTxtGet**](DefaultApi.md#timezoneAreaLocationTxtGet) | **GET** /timezone/{area}/{location}.txt | request the current time for a timezone. |
| [**timezoneAreaTxtGet**](DefaultApi.md#timezoneAreaTxtGet) | **GET** /timezone/{area}.txt | a listing of all timezones available for that area. |
| [**timezoneGet**](DefaultApi.md#timezoneGet) | **GET** /timezone | a listing of all timezones. |
| [**timezoneTxtGet**](DefaultApi.md#timezoneTxtGet) | **GET** /timezone.txt | a listing of all timezones. |


<a id="ipGet"></a>
# **ipGet**
> DateTimeJsonResponse ipGet()

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      DateTimeJsonResponse result = apiInstance.ipGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipGet");
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

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in JSON format |  -  |
| **0** | an error response in JSON format |  -  |

<a id="ipIpv4Get"></a>
# **ipIpv4Get**
> DateTimeJsonResponse ipIpv4Get(ipv4)

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ipv4 = "ipv4_example"; // String | 
    try {
      DateTimeJsonResponse result = apiInstance.ipIpv4Get(ipv4);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipIpv4Get");
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
| **ipv4** | **String**|  | |

### Return type

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in JSON format |  -  |
| **0** | an error response in JSON format |  -  |

<a id="ipIpv4TxtGet"></a>
# **ipIpv4TxtGet**
> String ipIpv4TxtGet(ipv4)

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ipv4 = "ipv4_example"; // String | 
    try {
      String result = apiInstance.ipIpv4TxtGet(ipv4);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipIpv4TxtGet");
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
| **ipv4** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in plain text |  -  |
| **0** | an error response in plain text |  -  |

<a id="ipTxtGet"></a>
# **ipTxtGet**
> String ipTxtGet()

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      String result = apiInstance.ipTxtGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipTxtGet");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in plain text |  -  |
| **0** | an error response in plain text |  -  |

<a id="timezoneAreaGet"></a>
# **timezoneAreaGet**
> List&lt;String&gt; timezoneAreaGet(area)

a listing of all timezones available for that area.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String area = "area_example"; // String | 
    try {
      List<String> result = apiInstance.timezoneAreaGet(area);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneAreaGet");
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
| **area** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of available timezones in JSON format |  -  |
| **0** | an error response in JSON format |  -  |

<a id="timezoneAreaLocationGet"></a>
# **timezoneAreaLocationGet**
> DateTimeJsonResponse timezoneAreaLocationGet(area, location)

request the current time for a timezone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String area = "area_example"; // String | 
    String location = "location_example"; // String | 
    try {
      DateTimeJsonResponse result = apiInstance.timezoneAreaLocationGet(area, location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneAreaLocationGet");
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
| **area** | **String**|  | |
| **location** | **String**|  | |

### Return type

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in JSON format |  -  |
| **0** | an error response in JSON format |  -  |

<a id="timezoneAreaLocationRegionGet"></a>
# **timezoneAreaLocationRegionGet**
> DateTimeJsonResponse timezoneAreaLocationRegionGet(area, location, region)

request the current time for a timezone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String area = "area_example"; // String | 
    String location = "location_example"; // String | 
    String region = "region_example"; // String | 
    try {
      DateTimeJsonResponse result = apiInstance.timezoneAreaLocationRegionGet(area, location, region);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneAreaLocationRegionGet");
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
| **area** | **String**|  | |
| **location** | **String**|  | |
| **region** | **String**|  | |

### Return type

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in JSON format |  -  |
| **0** | an error response in JSON format |  -  |

<a id="timezoneAreaLocationRegionTxtGet"></a>
# **timezoneAreaLocationRegionTxtGet**
> String timezoneAreaLocationRegionTxtGet(area, location, region)

request the current time for a timezone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String area = "area_example"; // String | 
    String location = "location_example"; // String | 
    String region = "region_example"; // String | 
    try {
      String result = apiInstance.timezoneAreaLocationRegionTxtGet(area, location, region);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneAreaLocationRegionTxtGet");
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
| **area** | **String**|  | |
| **location** | **String**|  | |
| **region** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in plain text |  -  |
| **0** | an error response in plain text |  -  |

<a id="timezoneAreaLocationTxtGet"></a>
# **timezoneAreaLocationTxtGet**
> String timezoneAreaLocationTxtGet(area, location)

request the current time for a timezone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String area = "area_example"; // String | 
    String location = "location_example"; // String | 
    try {
      String result = apiInstance.timezoneAreaLocationTxtGet(area, location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneAreaLocationTxtGet");
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
| **area** | **String**|  | |
| **location** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the current time for the timezone requested in plain text |  -  |
| **0** | an error response in plain text |  -  |

<a id="timezoneAreaTxtGet"></a>
# **timezoneAreaTxtGet**
> String timezoneAreaTxtGet(area)

a listing of all timezones available for that area.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String area = "area_example"; // String | 
    try {
      String result = apiInstance.timezoneAreaTxtGet(area);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneAreaTxtGet");
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
| **area** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of available timezones in plain text |  -  |
| **0** | an error response in plain text |  -  |

<a id="timezoneGet"></a>
# **timezoneGet**
> List&lt;String&gt; timezoneGet()

a listing of all timezones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<String> result = apiInstance.timezoneGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | the list of available timezones in JSON format |  -  |

<a id="timezoneTxtGet"></a>
# **timezoneTxtGet**
> String timezoneTxtGet()

a listing of all timezones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://worldtimeapi.org/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      String result = apiInstance.timezoneTxtGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timezoneTxtGet");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | the list of available timezones in plain text |  -  |

