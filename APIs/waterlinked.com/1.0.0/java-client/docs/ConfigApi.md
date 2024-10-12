# ConfigApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configGet**](ConfigApi.md#configGet) | **GET** /api/v1/config/generic | Get config |
| [**configGetAntennaConfig**](ConfigApi.md#configGetAntennaConfig) | **GET** /api/v1/config/antenna | GetAntennaConfig config |
| [**configGetIP**](ConfigApi.md#configGetIP) | **GET** /api/v1/config/ip | GetIP config |
| [**configGetWIFI**](ConfigApi.md#configGetWIFI) | **GET** /api/v1/config/wifi | GetWIFI config |
| [**configListReceiver**](ConfigApi.md#configListReceiver) | **GET** /api/v1/config/receivers/ | ListReceiver config |
| [**configModify**](ConfigApi.md#configModify) | **PUT** /api/v1/config/generic | Modify config |
| [**configModifyAntennaConfig**](ConfigApi.md#configModifyAntennaConfig) | **PUT** /api/v1/config/antenna | ModifyAntennaConfig config |
| [**configModifyIP**](ConfigApi.md#configModifyIP) | **PUT** /api/v1/config/ip | ModifyIP config |
| [**configModifyReceiver**](ConfigApi.md#configModifyReceiver) | **PUT** /api/v1/config/receivers/{ID} | ModifyReceiver config |
| [**configModifyWIFI**](ConfigApi.md#configModifyWIFI) | **PUT** /api/v1/config/wifi | ModifyWIFI config |
| [**configShowReceiver**](ConfigApi.md#configShowReceiver) | **GET** /api/v1/config/receivers/{ID} | ShowReceiver config |


<a id="configGet"></a>
# **configGet**
> WaterlinkedConfiguration configGet()

Get config

Get generic configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      WaterlinkedConfiguration result = apiInstance.configGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configGet");
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

[**WaterlinkedConfiguration**](WaterlinkedConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.configuration+json, application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="configGetAntennaConfig"></a>
# **configGetAntennaConfig**
> WaterlinkedAntennaConfig configGetAntennaConfig()

GetAntennaConfig config

Get Antenna configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      WaterlinkedAntennaConfig result = apiInstance.configGetAntennaConfig();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configGetAntennaConfig");
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

[**WaterlinkedAntennaConfig**](WaterlinkedAntennaConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.antenna_config+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="configGetIP"></a>
# **configGetIP**
> WaterlinkedIpConfig configGetIP()

GetIP config

Get IP configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      WaterlinkedIpConfig result = apiInstance.configGetIP();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configGetIP");
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

[**WaterlinkedIpConfig**](WaterlinkedIpConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.ip_config+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="configGetWIFI"></a>
# **configGetWIFI**
> WaterlinkedWifiConfig configGetWIFI()

GetWIFI config

Get WIFI configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      WaterlinkedWifiConfig result = apiInstance.configGetWIFI();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configGetWIFI");
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

[**WaterlinkedWifiConfig**](WaterlinkedWifiConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.wifi_config+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="configListReceiver"></a>
# **configListReceiver**
> List&lt;WaterlinkedReceiver&gt; configListReceiver()

ListReceiver config

(Re)Load current receiver settings and return them

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      List<WaterlinkedReceiver> result = apiInstance.configListReceiver();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configListReceiver");
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

[**List&lt;WaterlinkedReceiver&gt;**](WaterlinkedReceiver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.receiver+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned list of receivers |  -  |

<a id="configModify"></a>
# **configModify**
> WaterlinkedOperationResponse configModify(payload)

Modify config

Modify generic configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    ModifyConfigPayload payload = new ModifyConfigPayload(); // ModifyConfigPayload | Configuration parameters
    try {
      WaterlinkedOperationResponse result = apiInstance.configModify(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configModify");
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
| **payload** | [**ModifyConfigPayload**](ModifyConfigPayload.md)| Configuration parameters | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="configModifyAntennaConfig"></a>
# **configModifyAntennaConfig**
> WaterlinkedOperationResponse configModifyAntennaConfig(payload)

ModifyAntennaConfig config

Modify Antenna configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    ModifyAntennaConfigConfigPayload payload = new ModifyAntennaConfigConfigPayload(); // ModifyAntennaConfigConfigPayload | Configuration parameters for antenna set up
    try {
      WaterlinkedOperationResponse result = apiInstance.configModifyAntennaConfig(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configModifyAntennaConfig");
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
| **payload** | [**ModifyAntennaConfigConfigPayload**](ModifyAntennaConfigConfigPayload.md)| Configuration parameters for antenna set up | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="configModifyIP"></a>
# **configModifyIP**
> WaterlinkedOperationResponse configModifyIP(payload)

ModifyIP config

Modify IP configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    ModifyIPConfigPayload payload = new ModifyIPConfigPayload(); // ModifyIPConfigPayload | Configuration parameters
    try {
      WaterlinkedOperationResponse result = apiInstance.configModifyIP(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configModifyIP");
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
| **payload** | [**ModifyIPConfigPayload**](ModifyIPConfigPayload.md)| Configuration parameters | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="configModifyReceiver"></a>
# **configModifyReceiver**
> configModifyReceiver(ID, payload)

ModifyReceiver config

Modify receiver configuration, does not apply the change until generic modify is called. Calling list will discard changes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    Integer ID = 56; // Integer | Identifier
    ModifyReceiverConfigPayload payload = new ModifyReceiverConfigPayload(); // ModifyReceiverConfigPayload | A receiver configuration
    try {
      apiInstance.configModifyReceiver(ID, payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configModifyReceiver");
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
| **ID** | **Integer**| Identifier | |
| **payload** | [**ModifyReceiverConfigPayload**](ModifyReceiverConfigPayload.md)| A receiver configuration | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="configModifyWIFI"></a>
# **configModifyWIFI**
> WaterlinkedOperationResponse configModifyWIFI(payload)

ModifyWIFI config

Modify WIFI configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    ModifyWIFIConfigPayload payload = new ModifyWIFIConfigPayload(); // ModifyWIFIConfigPayload | Configuration parameters
    try {
      WaterlinkedOperationResponse result = apiInstance.configModifyWIFI(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configModifyWIFI");
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
| **payload** | [**ModifyWIFIConfigPayload**](ModifyWIFIConfigPayload.md)| Configuration parameters | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="configShowReceiver"></a>
# **configShowReceiver**
> WaterlinkedReceiver configShowReceiver(ID)

ShowReceiver config

Get receiver configuration by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    Integer ID = 56; // Integer | Identifier
    try {
      WaterlinkedReceiver result = apiInstance.configShowReceiver(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#configShowReceiver");
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
| **ID** | **Integer**| Identifier | |

### Return type

[**WaterlinkedReceiver**](WaterlinkedReceiver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.receiver+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

