# PatrowlEngineApi

All URIs are relative to *http://patrowl.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cleanScanPage**](PatrowlEngineApi.md#cleanScanPage) | **GET** /clean/{scanId} | Clean scan |
| [**cleanScansPage**](PatrowlEngineApi.md#cleanScansPage) | **GET** /clean | Clean all scans |
| [**getDefaultPage**](PatrowlEngineApi.md#getDefaultPage) | **GET** / | Index page |
| [**getFindingPage**](PatrowlEngineApi.md#getFindingPage) | **GET** /getfindings/{scanId} | Get findings on finished scans |
| [**getInfoPage**](PatrowlEngineApi.md#getInfoPage) | **GET** /info | Engine info page |
| [**getLivenessPage**](PatrowlEngineApi.md#getLivenessPage) | **GET** /liveness | Liveness page |
| [**getReadinessPage**](PatrowlEngineApi.md#getReadinessPage) | **GET** /readiness | Readiness page |
| [**getTestPage**](PatrowlEngineApi.md#getTestPage) | **GET** /test | Test page |
| [**reloadConfigurationPage**](PatrowlEngineApi.md#reloadConfigurationPage) | **GET** /reloadconfig | Configuration reloading page |
| [**startScanPage**](PatrowlEngineApi.md#startScanPage) | **POST** /startscan | Start a new scan |
| [**statusScanPage**](PatrowlEngineApi.md#statusScanPage) | **GET** /status/{scanId} | Status of a scan |
| [**statusScansPage**](PatrowlEngineApi.md#statusScansPage) | **GET** /status | Status on all scans |
| [**stopScanPage**](PatrowlEngineApi.md#stopScanPage) | **GET** /stop/{scanId} | Stop a scan |
| [**stopScansPage**](PatrowlEngineApi.md#stopScansPage) | **GET** /stopscans | Stop all scans |


<a id="cleanScanPage"></a>
# **cleanScanPage**
> ModelApiResponse cleanScanPage(scanId)

Clean scan

Clean scan identified by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    Integer scanId = 56; // Integer | Numeric ID of the scan to clean
    try {
      ModelApiResponse result = apiInstance.cleanScanPage(scanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#cleanScanPage");
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
| **scanId** | **Integer**| Numeric ID of the scan to clean | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cleanScansPage"></a>
# **cleanScansPage**
> ModelApiResponse cleanScansPage()

Clean all scans

Clean all current scans.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.cleanScansPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#cleanScansPage");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getDefaultPage"></a>
# **getDefaultPage**
> ModelApiResponse getDefaultPage()

Index page

Return index page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.getDefaultPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#getDefaultPage");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getFindingPage"></a>
# **getFindingPage**
> List&lt;FindingsInner&gt; getFindingPage(scanId)

Get findings on finished scans

Get findings on finished scans.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    Integer scanId = 56; // Integer | Numeric ID of the scan to get findings
    try {
      List<FindingsInner> result = apiInstance.getFindingPage(scanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#getFindingPage");
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
| **scanId** | **Integer**| Numeric ID of the scan to get findings | |

### Return type

[**List&lt;FindingsInner&gt;**](FindingsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getInfoPage"></a>
# **getInfoPage**
> ModelApiResponse getInfoPage()

Engine info page

Return information on engine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.getInfoPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#getInfoPage");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLivenessPage"></a>
# **getLivenessPage**
> getLivenessPage()

Liveness page

Return liveness page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      apiInstance.getLivenessPage();
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#getLivenessPage");
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getReadinessPage"></a>
# **getReadinessPage**
> getReadinessPage()

Readiness page

Return liveness page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      apiInstance.getReadinessPage();
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#getReadinessPage");
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getTestPage"></a>
# **getTestPage**
> getTestPage()

Test page

Return test page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      apiInstance.getTestPage();
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#getTestPage");
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="reloadConfigurationPage"></a>
# **reloadConfigurationPage**
> ModelApiResponse reloadConfigurationPage()

Configuration reloading page

Reload the configuration file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.reloadConfigurationPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#reloadConfigurationPage");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="startScanPage"></a>
# **startScanPage**
> ModelApiResponse startScanPage(scanDefinition)

Start a new scan

Start a new scan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    ScanDefinition scanDefinition = new ScanDefinition(); // ScanDefinition | 
    try {
      ModelApiResponse result = apiInstance.startScanPage(scanDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#startScanPage");
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
| **scanDefinition** | [**ScanDefinition**](ScanDefinition.md)|  | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="statusScanPage"></a>
# **statusScanPage**
> ModelApiResponse statusScanPage(scanId)

Status of a scan

Status of a scan identified by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    Integer scanId = 56; // Integer | Numeric ID of the scan to get status
    try {
      ModelApiResponse result = apiInstance.statusScanPage(scanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#statusScanPage");
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
| **scanId** | **Integer**| Numeric ID of the scan to get status | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="statusScansPage"></a>
# **statusScansPage**
> ModelApiResponse statusScansPage()

Status on all scans

Status all current scans.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.statusScansPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#statusScansPage");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="stopScanPage"></a>
# **stopScanPage**
> ModelApiResponse stopScanPage(scanId)

Stop a scan

Stop a scan identified by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    Integer scanId = 56; // Integer | Numeric ID of the scan to stop
    try {
      ModelApiResponse result = apiInstance.stopScanPage(scanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#stopScanPage");
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
| **scanId** | **Integer**| Numeric ID of the scan to stop | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="stopScansPage"></a>
# **stopScansPage**
> ModelApiResponse stopScansPage()

Stop all scans

Stop all current scans.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatrowlEngineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://patrowl.local");

    PatrowlEngineApi apiInstance = new PatrowlEngineApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.stopScansPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatrowlEngineApi#stopScansPage");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

