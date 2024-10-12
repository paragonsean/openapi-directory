# DefaultApi

All URIs are relative to *http://mbus.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**get**](DefaultApi.md#get) | **POST** /mbus/get/{device}/{baudrate}/{address} |  |
| [**getMulti**](DefaultApi.md#getMulti) | **POST** /mbus/getMulti/{device}/{baudrate}/{address}/{maxframes} |  |
| [**hat**](DefaultApi.md#hat) | **GET** /mbus/hat |  |
| [**hatOff**](DefaultApi.md#hatOff) | **POST** /mbus/hat/off |  |
| [**hatOn**](DefaultApi.md#hatOn) | **POST** /mbus/hat/on |  |
| [**mbusApi**](DefaultApi.md#mbusApi) | **GET** /mbus/api |  |
| [**scan**](DefaultApi.md#scan) | **POST** /mbus/scan/{device}/{baudrate} |  |


<a id="get"></a>
# **get**
> String get(device, baudrate, address)



Gets data from the slave identified by {address}

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String device = "ttyAMA0"; // String | The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
    Baudrate baudrate = Baudrate.fromValue("300"); // Baudrate | Baudrate to communicate with M-Bus devices
    String address = "48"; // String | The slave device to get data from
    try {
      String result = apiInstance.get(device, baudrate, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#get");
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
| **device** | **String**| The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning | |
| **baudrate** | [**Baudrate**](.md)| Baudrate to communicate with M-Bus devices | [enum: 300, 600, 1200, 2400, 4800, 9600] |
| **address** | **String**| The slave device to get data from | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (or M-Bus HTTPD is unauthorized to access it, or to change baud rate to that specified, etc) |  -  |

<a id="getMulti"></a>
# **getMulti**
> String getMulti(device, baudrate, address, maxframes)



Gets data from the slave identified by {address}, and supports multiple responses from the slave

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String device = "ttyAMA0"; // String | The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
    Baudrate baudrate = Baudrate.fromValue("300"); // Baudrate | Baudrate to communicate with M-Bus devices
    String address = "48"; // String | The slave device to get data from
    Integer maxframes = 16; // Integer | The slave device to get data from
    try {
      String result = apiInstance.getMulti(device, baudrate, address, maxframes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMulti");
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
| **device** | **String**| The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning | |
| **baudrate** | [**Baudrate**](.md)| Baudrate to communicate with M-Bus devices | [enum: 300, 600, 1200, 2400, 4800, 9600] |
| **address** | **String**| The slave device to get data from | |
| **maxframes** | **Integer**| The slave device to get data from | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (or M-Bus HTTPD is unauthorized to access it, or to change baud rate to that specified, etc) |  -  |

<a id="hat"></a>
# **hat**
> Hat hat()



Gets Raspberry Pi Hat information

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Hat result = apiInstance.hat();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hat");
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

[**Hat**](Hat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="hatOff"></a>
# **hatOff**
> hatOff()



Turns off power to the M-Bus

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.hatOff();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hatOff");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="hatOn"></a>
# **hatOn**
> hatOn()



Turns on power to the M-Bus

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.hatOn();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hatOn");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="mbusApi"></a>
# **mbusApi**
> String mbusApi()



Returns this API specification

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      String result = apiInstance.mbusApi();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mbusApi");
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
 - **Accept**: text/x-yaml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="scan"></a>
# **scan**
> String scan(device, baudrate)



Scan the specified device for slaves

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
    defaultClient.setBasePath("http://mbus.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String device = "ttyAMA0"; // String | The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
    Baudrate baudrate = Baudrate.fromValue("300"); // Baudrate | Baudrate to communicate with M-Bus devices
    try {
      String result = apiInstance.scan(device, baudrate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#scan");
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
| **device** | **String**| The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning | |
| **baudrate** | [**Baudrate**](.md)| Baudrate to communicate with M-Bus devices | [enum: 300, 600, 1200, 2400, 4800, 9600] |

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
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (e.g. device not found, or M-Bus HTTPD is unauthorized to access it, or to change baud rate to that specified, device not responding etc) |  -  |

