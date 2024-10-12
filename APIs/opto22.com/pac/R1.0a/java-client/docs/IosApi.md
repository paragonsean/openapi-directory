# IosApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**readAnalogInputEu_0**](IosApi.md#readAnalogInputEu_0) | **GET** /device/strategy/ios/analogInputs/{ioName}/eu |  |
| [**readAnalogInputs_0**](IosApi.md#readAnalogInputs_0) | **GET** /device/strategy/ios/analogInputs |  |
| [**readAnalogOutputEu_0**](IosApi.md#readAnalogOutputEu_0) | **GET** /device/strategy/ios/analogOutputs/{ioName}/eu |  |
| [**readAnalogOutputs_0**](IosApi.md#readAnalogOutputs_0) | **GET** /device/strategy/ios/analogOutputs |  |
| [**readDigitalInputState_0**](IosApi.md#readDigitalInputState_0) | **GET** /device/strategy/ios/digitalInputs/{ioName}/state |  |
| [**readDigitalInputs_0**](IosApi.md#readDigitalInputs_0) | **GET** /device/strategy/ios/digitalInputs |  |
| [**readDigitalOutputState_0**](IosApi.md#readDigitalOutputState_0) | **GET** /device/strategy/ios/digitalOutputs/{ioName}/state |  |
| [**readDigitalOutputs_0**](IosApi.md#readDigitalOutputs_0) | **GET** /device/strategy/ios/digitalOutputs |  |
| [**writeAnalogOutputEu_0**](IosApi.md#writeAnalogOutputEu_0) | **POST** /device/strategy/ios/analogOutputs/{ioName}/eu |  |
| [**writeDigitalOutputState_0**](IosApi.md#writeDigitalOutputState_0) | **POST** /device/strategy/ios/digitalOutputs/{ioName}/state |  |


<a id="readAnalogInputEu_0"></a>
# **readAnalogInputEu_0**
> FloatValueObject readAnalogInputEu_0(ioName)



Reads the value in engineering units (EU) of the specified analog input

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the analog input point to read
    try {
      FloatValueObject result = apiInstance.readAnalogInputEu_0(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readAnalogInputEu_0");
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
| **ioName** | **String**| Name of the analog input point to read | |

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readAnalogInputs_0"></a>
# **readAnalogInputs_0**
> List&lt;FloatVar&gt; readAnalogInputs_0()



Returns the name and engineering units (EU) for all analog input points in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readAnalogInputs_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readAnalogInputs_0");
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

[**List&lt;FloatVar&gt;**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="readAnalogOutputEu_0"></a>
# **readAnalogOutputEu_0**
> FloatValueObject readAnalogOutputEu_0(ioName)



Reads the value in engineering units (EU) of the specified analog output

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of analog output point to read
    try {
      FloatValueObject result = apiInstance.readAnalogOutputEu_0(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readAnalogOutputEu_0");
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
| **ioName** | **String**| Name of analog output point to read | |

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readAnalogOutputs_0"></a>
# **readAnalogOutputs_0**
> List&lt;FloatVar&gt; readAnalogOutputs_0()



Returns the name and engineering units (EU) for all analog output points in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readAnalogOutputs_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readAnalogOutputs_0");
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

[**List&lt;FloatVar&gt;**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="readDigitalInputState_0"></a>
# **readDigitalInputState_0**
> DigitalPointStateObject readDigitalInputState_0(ioName)



Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the digital input point to read
    try {
      DigitalPointStateObject result = apiInstance.readDigitalInputState_0(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readDigitalInputState_0");
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
| **ioName** | **String**| Name of the digital input point to read | |

### Return type

[**DigitalPointStateObject**](DigitalPointStateObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readDigitalInputs_0"></a>
# **readDigitalInputs_0**
> List&lt;DigitalPointStateVar&gt; readDigitalInputs_0()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    try {
      List<DigitalPointStateVar> result = apiInstance.readDigitalInputs_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readDigitalInputs_0");
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

[**List&lt;DigitalPointStateVar&gt;**](DigitalPointStateVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="readDigitalOutputState_0"></a>
# **readDigitalOutputState_0**
> DigitalPointStateObject readDigitalOutputState_0(ioName)



Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the digit output point to read
    try {
      DigitalPointStateObject result = apiInstance.readDigitalOutputState_0(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readDigitalOutputState_0");
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
| **ioName** | **String**| Name of the digit output point to read | |

### Return type

[**DigitalPointStateObject**](DigitalPointStateObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readDigitalOutputs_0"></a>
# **readDigitalOutputs_0**
> List&lt;DigitalPointStateVar&gt; readDigitalOutputs_0()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    try {
      List<DigitalPointStateVar> result = apiInstance.readDigitalOutputs_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#readDigitalOutputs_0");
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

[**List&lt;DigitalPointStateVar&gt;**](DigitalPointStateVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="writeAnalogOutputEu_0"></a>
# **writeAnalogOutputEu_0**
> writeAnalogOutputEu_0(ioName, body)



Sets the value of the specified analog output point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the analog output point to write
    FloatValueObject body = new FloatValueObject(); // FloatValueObject | Value to write
    try {
      apiInstance.writeAnalogOutputEu_0(ioName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#writeAnalogOutputEu_0");
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
| **ioName** | **String**| Name of the analog output point to write | |
| **body** | [**FloatValueObject**](FloatValueObject.md)| Value to write | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeDigitalOutputState_0"></a>
# **writeDigitalOutputState_0**
> writeDigitalOutputState_0(ioName, body)



Sets the value of the specified digital output point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IosApi apiInstance = new IosApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the digital output point to write
    DigitalPointStateObject body = new DigitalPointStateObject(); // DigitalPointStateObject | Value to write
    try {
      apiInstance.writeDigitalOutputState_0(ioName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling IosApi#writeDigitalOutputState_0");
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
| **ioName** | **String**| Name of the digital output point to write | |
| **body** | [**DigitalPointStateObject**](DigitalPointStateObject.md)| Value to write | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

