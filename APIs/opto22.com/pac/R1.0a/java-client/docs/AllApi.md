# AllApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**readAnalogInputEu**](AllApi.md#readAnalogInputEu) | **GET** /device/strategy/ios/analogInputs/{ioName}/eu |  |
| [**readAnalogInputs**](AllApi.md#readAnalogInputs) | **GET** /device/strategy/ios/analogInputs |  |
| [**readAnalogOutputEu**](AllApi.md#readAnalogOutputEu) | **GET** /device/strategy/ios/analogOutputs/{ioName}/eu |  |
| [**readAnalogOutputs**](AllApi.md#readAnalogOutputs) | **GET** /device/strategy/ios/analogOutputs |  |
| [**readDeviceDetails**](AllApi.md#readDeviceDetails) | **GET** /device |  |
| [**readDigitalInputState**](AllApi.md#readDigitalInputState) | **GET** /device/strategy/ios/digitalInputs/{ioName}/state |  |
| [**readDigitalInputs**](AllApi.md#readDigitalInputs) | **GET** /device/strategy/ios/digitalInputs |  |
| [**readDigitalOutputState**](AllApi.md#readDigitalOutputState) | **GET** /device/strategy/ios/digitalOutputs/{ioName}/state |  |
| [**readDigitalOutputs**](AllApi.md#readDigitalOutputs) | **GET** /device/strategy/ios/digitalOutputs |  |
| [**readDownTimerValue**](AllApi.md#readDownTimerValue) | **GET** /device/strategy/vars/downTimers/{downTimerName}/value |  |
| [**readDownTimerVars**](AllApi.md#readDownTimerVars) | **GET** /device/strategy/vars/downTimers |  |
| [**readFloatTable**](AllApi.md#readFloatTable) | **GET** /device/strategy/tables/floats/{tableName} |  |
| [**readFloatTableElement**](AllApi.md#readFloatTableElement) | **GET** /device/strategy/tables/floats/{tableName}/{index} |  |
| [**readFloatTables**](AllApi.md#readFloatTables) | **GET** /device/strategy/tables/floats |  |
| [**readFloatVar**](AllApi.md#readFloatVar) | **GET** /device/strategy/vars/floats/{floatName} |  |
| [**readFloatVars**](AllApi.md#readFloatVars) | **GET** /device/strategy/vars/floats |  |
| [**readInt32Table**](AllApi.md#readInt32Table) | **GET** /device/strategy/tables/int32s/{tableName} |  |
| [**readInt32TableElement**](AllApi.md#readInt32TableElement) | **GET** /device/strategy/tables/int32s/{tableName}/{index} |  |
| [**readInt32Tables**](AllApi.md#readInt32Tables) | **GET** /device/strategy/tables/int32s |  |
| [**readInt32Var**](AllApi.md#readInt32Var) | **GET** /device/strategy/vars/int32s/{int32Name} |  |
| [**readInt32Vars**](AllApi.md#readInt32Vars) | **GET** /device/strategy/vars/int32s |  |
| [**readInt64Table**](AllApi.md#readInt64Table) | **GET** /device/strategy/tables/int64s/{tableName} |  |
| [**readInt64TableAsString**](AllApi.md#readInt64TableAsString) | **GET** /device/strategy/tables/int64s/{tableName}/_string |  |
| [**readInt64TableElement**](AllApi.md#readInt64TableElement) | **GET** /device/strategy/tables/int64s/{tableName}/{index} |  |
| [**readInt64TableElementAsString**](AllApi.md#readInt64TableElementAsString) | **GET** /device/strategy/tables/int64s/{tableName}/{index}/_string |  |
| [**readInt64Tables**](AllApi.md#readInt64Tables) | **GET** /device/strategy/tables/int64s |  |
| [**readInt64Var**](AllApi.md#readInt64Var) | **GET** /device/strategy/vars/int64s/{int64Name} |  |
| [**readInt64VarAsString**](AllApi.md#readInt64VarAsString) | **GET** /device/strategy/vars/int64s/{int64Name}/_string |  |
| [**readInt64Vars**](AllApi.md#readInt64Vars) | **GET** /device/strategy/vars/int64s |  |
| [**readInt64VarsAsStrings**](AllApi.md#readInt64VarsAsStrings) | **GET** /device/strategy/vars/int64s/_string |  |
| [**readStrategyDetails**](AllApi.md#readStrategyDetails) | **GET** /device/strategy |  |
| [**readStringTable**](AllApi.md#readStringTable) | **GET** /device/strategy/tables/strings/{tableName} |  |
| [**readStringTableElement**](AllApi.md#readStringTableElement) | **GET** /device/strategy/tables/strings/{tableName}/{index} |  |
| [**readStringTables**](AllApi.md#readStringTables) | **GET** /device/strategy/tables/strings |  |
| [**readStringVar**](AllApi.md#readStringVar) | **GET** /device/strategy/vars/strings/{stringName} |  |
| [**readStringVars**](AllApi.md#readStringVars) | **GET** /device/strategy/vars/strings |  |
| [**readUpTimerValue**](AllApi.md#readUpTimerValue) | **GET** /device/strategy/vars/upTimers/{upTimerName}/value |  |
| [**readUpTimerVars**](AllApi.md#readUpTimerVars) | **GET** /device/strategy/vars/upTimers |  |
| [**writeAnalogOutputEu**](AllApi.md#writeAnalogOutputEu) | **POST** /device/strategy/ios/analogOutputs/{ioName}/eu |  |
| [**writeDigitalOutputState**](AllApi.md#writeDigitalOutputState) | **POST** /device/strategy/ios/digitalOutputs/{ioName}/state |  |
| [**writeFloatTable**](AllApi.md#writeFloatTable) | **POST** /device/strategy/tables/floats/{tableName} |  |
| [**writeFloatTableElement**](AllApi.md#writeFloatTableElement) | **POST** /device/strategy/tables/floats/{tableName}/{index} |  |
| [**writeFloatVar**](AllApi.md#writeFloatVar) | **POST** /device/strategy/vars/floats/{floatName} |  |
| [**writeInt32Table**](AllApi.md#writeInt32Table) | **POST** /device/strategy/tables/int32s/{tableName} |  |
| [**writeInt32TableElement**](AllApi.md#writeInt32TableElement) | **POST** /device/strategy/tables/int32s/{tableName}/{index} |  |
| [**writeInt32Var**](AllApi.md#writeInt32Var) | **POST** /device/strategy/vars/int32s/{int32Name} |  |
| [**writeInt64Table**](AllApi.md#writeInt64Table) | **POST** /device/strategy/tables/int64s/{tableName} |  |
| [**writeInt64TableAsString**](AllApi.md#writeInt64TableAsString) | **POST** /device/strategy/tables/int64s/{tableName}/_string |  |
| [**writeInt64TableElement**](AllApi.md#writeInt64TableElement) | **POST** /device/strategy/tables/int64s/{tableName}/{index} |  |
| [**writeInt64TableElementAsString**](AllApi.md#writeInt64TableElementAsString) | **POST** /device/strategy/tables/int64s/{tableName}/{index}/_string |  |
| [**writeInt64Var**](AllApi.md#writeInt64Var) | **POST** /device/strategy/vars/int64s/{int64Name} |  |
| [**writeInt64VarAsString**](AllApi.md#writeInt64VarAsString) | **POST** /device/strategy/vars/int64s/{int64Name}/_string |  |
| [**writeStringTable**](AllApi.md#writeStringTable) | **POST** /device/strategy/tables/strings/{tableName} |  |
| [**writeStringTableElement**](AllApi.md#writeStringTableElement) | **POST** /device/strategy/tables/strings/{tableName}/{index} |  |
| [**writeStringVar**](AllApi.md#writeStringVar) | **POST** /device/strategy/vars/strings/{stringName} |  |


<a id="readAnalogInputEu"></a>
# **readAnalogInputEu**
> FloatValueObject readAnalogInputEu(ioName)



Reads the value in engineering units (EU) of the specified analog input

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the analog input point to read
    try {
      FloatValueObject result = apiInstance.readAnalogInputEu(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readAnalogInputEu");
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

<a id="readAnalogInputs"></a>
# **readAnalogInputs**
> List&lt;FloatVar&gt; readAnalogInputs()



Returns the name and engineering units (EU) for all analog input points in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readAnalogInputs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readAnalogInputs");
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

<a id="readAnalogOutputEu"></a>
# **readAnalogOutputEu**
> FloatValueObject readAnalogOutputEu(ioName)



Reads the value in engineering units (EU) of the specified analog output

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of analog output point to read
    try {
      FloatValueObject result = apiInstance.readAnalogOutputEu(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readAnalogOutputEu");
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

<a id="readAnalogOutputs"></a>
# **readAnalogOutputs**
> List&lt;FloatVar&gt; readAnalogOutputs()



Returns the name and engineering units (EU) for all analog output points in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readAnalogOutputs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readAnalogOutputs");
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

<a id="readDeviceDetails"></a>
# **readDeviceDetails**
> ControllerResponse readDeviceDetails()



Returns controller&#39;s type; firmware version; both mac addresses; and uptime in seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      ControllerResponse result = apiInstance.readDeviceDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDeviceDetails");
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

[**ControllerResponse**](ControllerResponse.md)

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

<a id="readDigitalInputState"></a>
# **readDigitalInputState**
> DigitalPointStateObject readDigitalInputState(ioName)



Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the digital input point to read
    try {
      DigitalPointStateObject result = apiInstance.readDigitalInputState(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDigitalInputState");
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

<a id="readDigitalInputs"></a>
# **readDigitalInputs**
> List&lt;DigitalPointStateVar&gt; readDigitalInputs()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<DigitalPointStateVar> result = apiInstance.readDigitalInputs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDigitalInputs");
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

<a id="readDigitalOutputState"></a>
# **readDigitalOutputState**
> DigitalPointStateObject readDigitalOutputState(ioName)



Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the digit output point to read
    try {
      DigitalPointStateObject result = apiInstance.readDigitalOutputState(ioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDigitalOutputState");
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

<a id="readDigitalOutputs"></a>
# **readDigitalOutputs**
> List&lt;DigitalPointStateVar&gt; readDigitalOutputs()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<DigitalPointStateVar> result = apiInstance.readDigitalOutputs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDigitalOutputs");
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

<a id="readDownTimerValue"></a>
# **readDownTimerValue**
> FloatValueObject readDownTimerValue(downTimerName)



Returns current value of the specified down timer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String downTimerName = "downTimerName_example"; // String | Name of the down timer variable to read
    try {
      FloatValueObject result = apiInstance.readDownTimerValue(downTimerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDownTimerValue");
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
| **downTimerName** | **String**| Name of the down timer variable to read | |

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

<a id="readDownTimerVars"></a>
# **readDownTimerVars**
> List&lt;FloatVar&gt; readDownTimerVars()



Returns the name and current value of all down timers in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readDownTimerVars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readDownTimerVars");
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

<a id="readFloatTable"></a>
# **readFloatTable**
> List&lt;Float&gt; readFloatTable(tableName, startIndex, numElements)



Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<Float> result = apiInstance.readFloatTable(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readFloatTable");
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
| **tableName** | **String**| Name of float table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;Float&gt;**

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

<a id="readFloatTableElement"></a>
# **readFloatTableElement**
> FloatValueObject readFloatTableElement(tableName, index)



Read specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      FloatValueObject result = apiInstance.readFloatTableElement(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readFloatTableElement");
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
| **tableName** | **String**| Name of float table to read | |
| **index** | **Integer**| Index of element to read | |

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

<a id="readFloatTables"></a>
# **readFloatTables**
> List&lt;TableDef&gt; readFloatTables()



Returns an array of the name and length of all the float tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readFloatTables();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readFloatTables");
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

[**List&lt;TableDef&gt;**](TableDef.md)

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

<a id="readFloatVar"></a>
# **readFloatVar**
> FloatValueObject readFloatVar(floatName)



Returns value of the specified float variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String floatName = "floatName_example"; // String | Name of float variable to read
    try {
      FloatValueObject result = apiInstance.readFloatVar(floatName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readFloatVar");
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
| **floatName** | **String**| Name of float variable to read | |

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

<a id="readFloatVars"></a>
# **readFloatVars**
> List&lt;FloatVar&gt; readFloatVars()



Returns the name and value of all (single-precision) float variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readFloatVars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readFloatVars");
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

<a id="readInt32Table"></a>
# **readInt32Table**
> List&lt;Integer&gt; readInt32Table(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<Integer> result = apiInstance.readInt32Table(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt32Table");
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
| **tableName** | **String**| Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;Integer&gt;**

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

<a id="readInt32TableElement"></a>
# **readInt32TableElement**
> Int32ValueObject readInt32TableElement(tableName, index)



Read specified integer32 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer32 table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      Int32ValueObject result = apiInstance.readInt32TableElement(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt32TableElement");
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
| **tableName** | **String**| Name of the integer32 table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**Int32ValueObject**](Int32ValueObject.md)

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

<a id="readInt32Tables"></a>
# **readInt32Tables**
> List&lt;TableDef&gt; readInt32Tables()



Returns an array of the name and length of all the integer32 tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readInt32Tables();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt32Tables");
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

[**List&lt;TableDef&gt;**](TableDef.md)

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

<a id="readInt32Var"></a>
# **readInt32Var**
> Int32ValueObject readInt32Var(int32Name)



Returns value of the specified integer32 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String int32Name = "int32Name_example"; // String | Name of integer32 variable to read
    try {
      Int32ValueObject result = apiInstance.readInt32Var(int32Name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt32Var");
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
| **int32Name** | **String**| Name of integer32 variable to read | |

### Return type

[**Int32ValueObject**](Int32ValueObject.md)

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

<a id="readInt32Vars"></a>
# **readInt32Vars**
> List&lt;Int32Var&gt; readInt32Vars()



Returns the name and value of all integer32 variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Int32Var> result = apiInstance.readInt32Vars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt32Vars");
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

[**List&lt;Int32Var&gt;**](Int32Var.md)

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

<a id="readInt64Table"></a>
# **readInt64Table**
> List&lt;Long&gt; readInt64Table(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<Long> result = apiInstance.readInt64Table(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64Table");
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
| **tableName** | **String**| Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;Long&gt;**

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

<a id="readInt64TableAsString"></a>
# **readInt64TableAsString**
> List&lt;String&gt; readInt64TableAsString(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<String> result = apiInstance.readInt64TableAsString(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64TableAsString");
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
| **tableName** | **String**| Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;String&gt;**

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

<a id="readInt64TableElement"></a>
# **readInt64TableElement**
> Int64ValueObject readInt64TableElement(tableName, index)



Read specified integer64 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      Int64ValueObject result = apiInstance.readInt64TableElement(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64TableElement");
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
| **tableName** | **String**| Name of integer64 table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**Int64ValueObject**](Int64ValueObject.md)

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

<a id="readInt64TableElementAsString"></a>
# **readInt64TableElementAsString**
> Int64StringValueObject readInt64TableElementAsString(tableName, index)



Read specified integer64 table element as string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      Int64StringValueObject result = apiInstance.readInt64TableElementAsString(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64TableElementAsString");
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
| **tableName** | **String**| Name of integer64 table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**Int64StringValueObject**](Int64StringValueObject.md)

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

<a id="readInt64Tables"></a>
# **readInt64Tables**
> List&lt;TableDef&gt; readInt64Tables()



Returns an array of the name and length of all the integer64 tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readInt64Tables();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64Tables");
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

[**List&lt;TableDef&gt;**](TableDef.md)

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

<a id="readInt64Var"></a>
# **readInt64Var**
> Int64ValueObject readInt64Var(int64Name)



Returns value of the specified integer64 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to read
    try {
      Int64ValueObject result = apiInstance.readInt64Var(int64Name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64Var");
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
| **int64Name** | **String**| Name of integer64 variable to read | |

### Return type

[**Int64ValueObject**](Int64ValueObject.md)

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

<a id="readInt64VarAsString"></a>
# **readInt64VarAsString**
> Int64StringValueObject readInt64VarAsString(int64Name)



Returns value of the specified integer64 variable as a string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to read
    try {
      Int64StringValueObject result = apiInstance.readInt64VarAsString(int64Name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64VarAsString");
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
| **int64Name** | **String**| Name of integer64 variable to read | |

### Return type

[**Int64StringValueObject**](Int64StringValueObject.md)

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

<a id="readInt64Vars"></a>
# **readInt64Vars**
> List&lt;Int64Var&gt; readInt64Vars()



Returns the name and value of all integer64 variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Int64Var> result = apiInstance.readInt64Vars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64Vars");
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

[**List&lt;Int64Var&gt;**](Int64Var.md)

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

<a id="readInt64VarsAsStrings"></a>
# **readInt64VarsAsStrings**
> List&lt;Int64VarAsString&gt; readInt64VarsAsStrings()



Returns the name and value as a string of all integer64 variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Int64VarAsString> result = apiInstance.readInt64VarsAsStrings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readInt64VarsAsStrings");
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

[**List&lt;Int64VarAsString&gt;**](Int64VarAsString.md)

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

<a id="readStrategyDetails"></a>
# **readStrategyDetails**
> StrategyResponse readStrategyDetails()



Returns the name, date, time, and CRC of the strategy currently in the controller, and the number of charts currently running. Empty strings and a 0 will be returned when there is no strategy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      StrategyResponse result = apiInstance.readStrategyDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readStrategyDetails");
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

[**StrategyResponse**](StrategyResponse.md)

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

<a id="readStringTable"></a>
# **readStringTable**
> List&lt;String&gt; readStringTable(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<String> result = apiInstance.readStringTable(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readStringTable");
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
| **tableName** | **String**| Name of string table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;String&gt;**

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

<a id="readStringTableElement"></a>
# **readStringTableElement**
> StringValueObject readStringTableElement(tableName, index)



Read specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      StringValueObject result = apiInstance.readStringTableElement(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readStringTableElement");
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
| **tableName** | **String**| Name of string table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**StringValueObject**](StringValueObject.md)

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

<a id="readStringTables"></a>
# **readStringTables**
> List&lt;TableDef&gt; readStringTables()



Returns an array of the name and length of all the string tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readStringTables();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readStringTables");
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

[**List&lt;TableDef&gt;**](TableDef.md)

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

<a id="readStringVar"></a>
# **readStringVar**
> StringValueObject readStringVar(stringName)



Returns value of the specified string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String stringName = "stringName_example"; // String | Name of string variable to read
    try {
      StringValueObject result = apiInstance.readStringVar(stringName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readStringVar");
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
| **stringName** | **String**| Name of string variable to read | |

### Return type

[**StringValueObject**](StringValueObject.md)

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

<a id="readStringVars"></a>
# **readStringVars**
> List&lt;StringVar&gt; readStringVars()



Returns the name and value of all string variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<StringVar> result = apiInstance.readStringVars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readStringVars");
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

[**List&lt;StringVar&gt;**](StringVar.md)

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

<a id="readUpTimerValue"></a>
# **readUpTimerValue**
> FloatValueObject readUpTimerValue(upTimerName)



Returns current value of the specified up timer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String upTimerName = "upTimerName_example"; // String | Name of the up timer variable to read
    try {
      FloatValueObject result = apiInstance.readUpTimerValue(upTimerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readUpTimerValue");
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
| **upTimerName** | **String**| Name of the up timer variable to read | |

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

<a id="readUpTimerVars"></a>
# **readUpTimerVars**
> List&lt;FloatVar&gt; readUpTimerVars()



Returns the name and current value of all up timers in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readUpTimerVars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#readUpTimerVars");
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

<a id="writeAnalogOutputEu"></a>
# **writeAnalogOutputEu**
> writeAnalogOutputEu(ioName, body)



Sets the value of the specified analog output point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the analog output point to write
    FloatValueObject body = new FloatValueObject(); // FloatValueObject | Value to write
    try {
      apiInstance.writeAnalogOutputEu(ioName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeAnalogOutputEu");
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

<a id="writeDigitalOutputState"></a>
# **writeDigitalOutputState**
> writeDigitalOutputState(ioName, body)



Sets the value of the specified digital output point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String ioName = "ioName_example"; // String | Name of the digital output point to write
    DigitalPointStateObject body = new DigitalPointStateObject(); // DigitalPointStateObject | Value to write
    try {
      apiInstance.writeDigitalOutputState(ioName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeDigitalOutputState");
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

<a id="writeFloatTable"></a>
# **writeFloatTable**
> writeFloatTable(tableName, floatArray, startIndex)



Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to write; starting index may be specified
    List<Float> floatArray = Arrays.asList(); // List<Float> | Array of element values to write starting at startIndex
    Integer startIndex = 56; // Integer | Index of first element to write (default is 0)
    try {
      apiInstance.writeFloatTable(tableName, floatArray, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeFloatTable");
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
| **tableName** | **String**| Name of float table to write; starting index may be specified | |
| **floatArray** | [**List&lt;Float&gt;**](Float.md)| Array of element values to write starting at startIndex | |
| **startIndex** | **Integer**| Index of first element to write (default is 0) | [optional] |

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

<a id="writeFloatTableElement"></a>
# **writeFloatTableElement**
> writeFloatTableElement(tableName, index, floatElementObject)



Write specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to write
    Integer index = 56; // Integer | Index of element to write
    FloatValueObject floatElementObject = new FloatValueObject(); // FloatValueObject | Element to write starting at index
    try {
      apiInstance.writeFloatTableElement(tableName, index, floatElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeFloatTableElement");
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
| **tableName** | **String**| Name of float table to write | |
| **index** | **Integer**| Index of element to write | |
| **floatElementObject** | [**FloatValueObject**](FloatValueObject.md)| Element to write starting at index | |

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

<a id="writeFloatVar"></a>
# **writeFloatVar**
> writeFloatVar(floatName, body)



Sets the value of a float variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String floatName = "floatName_example"; // String | Name of the float variable to write
    FloatValueObject body = new FloatValueObject(); // FloatValueObject | Value to write to the float variable
    try {
      apiInstance.writeFloatVar(floatName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeFloatVar");
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
| **floatName** | **String**| Name of the float variable to write | |
| **body** | [**FloatValueObject**](FloatValueObject.md)| Value to write to the float variable | |

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

<a id="writeInt32Table"></a>
# **writeInt32Table**
> writeInt32Table(tableName, int32Array, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer32 table to write; starting index may be specified
    List<Integer> int32Array = Arrays.asList(); // List<Integer> | Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored
    Integer startIndex = 56; // Integer | Index of first element to write (default is 0)
    try {
      apiInstance.writeInt32Table(tableName, int32Array, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt32Table");
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
| **tableName** | **String**| Name of integer32 table to write; starting index may be specified | |
| **int32Array** | [**List&lt;Integer&gt;**](Integer.md)| Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored | |
| **startIndex** | **Integer**| Index of first element to write (default is 0) | [optional] |

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

<a id="writeInt32TableElement"></a>
# **writeInt32TableElement**
> writeInt32TableElement(tableName, index, int32ElementObject)



Write specified integer32 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer32 table to write
    Integer index = 56; // Integer | Index of element to write
    Int32ValueObject int32ElementObject = new Int32ValueObject(); // Int32ValueObject | Element to write at index specified
    try {
      apiInstance.writeInt32TableElement(tableName, index, int32ElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt32TableElement");
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
| **tableName** | **String**| Name of the integer32 table to write | |
| **index** | **Integer**| Index of element to write | |
| **int32ElementObject** | [**Int32ValueObject**](Int32ValueObject.md)| Element to write at index specified | |

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

<a id="writeInt32Var"></a>
# **writeInt32Var**
> writeInt32Var(int32Name, body)



Sets the value of an integer32 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String int32Name = "int32Name_example"; // String | Name of integer32 variable to write
    Int32ValueObject body = new Int32ValueObject(); // Int32ValueObject | Value to write to the integer32 variable
    try {
      apiInstance.writeInt32Var(int32Name, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt32Var");
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
| **int32Name** | **String**| Name of integer32 variable to write | |
| **body** | [**Int32ValueObject**](Int32ValueObject.md)| Value to write to the integer32 variable | |

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

<a id="writeInt64Table"></a>
# **writeInt64Table**
> writeInt64Table(tableName, int64Array, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
    List<Long> int64Array = Arrays.asList(); // List<Long> | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    Integer startIndex = 56; // Integer | Index of first element to write; default is 0
    try {
      apiInstance.writeInt64Table(tableName, int64Array, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt64Table");
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
| **tableName** | **String**| Name of integer64 table to write; starting index may be specified | |
| **int64Array** | [**List&lt;Long&gt;**](Long.md)| Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored | |
| **startIndex** | **Integer**| Index of first element to write; default is 0 | [optional] |

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

<a id="writeInt64TableAsString"></a>
# **writeInt64TableAsString**
> writeInt64TableAsString(tableName, int64AsStringArray, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
    List<String> int64AsStringArray = Arrays.asList(); // List<String> | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    Integer startIndex = 56; // Integer | Index of first element to write; default is 0.
    try {
      apiInstance.writeInt64TableAsString(tableName, int64AsStringArray, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt64TableAsString");
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
| **tableName** | **String**| Name of integer64 table to write; starting index may be specified | |
| **int64AsStringArray** | [**List&lt;String&gt;**](String.md)| Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored | |
| **startIndex** | **Integer**| Index of first element to write; default is 0. | [optional] |

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

<a id="writeInt64TableElement"></a>
# **writeInt64TableElement**
> writeInt64TableElement(tableName, index, int64ElementObject)



Write specified integer64 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to write
    Integer index = 56; // Integer | Index of element to write
    Int64ValueObject int64ElementObject = new Int64ValueObject(); // Int64ValueObject | Element to write starting at index specified
    try {
      apiInstance.writeInt64TableElement(tableName, index, int64ElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt64TableElement");
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
| **tableName** | **String**| Name of the integer64 table to write | |
| **index** | **Integer**| Index of element to write | |
| **int64ElementObject** | [**Int64ValueObject**](Int64ValueObject.md)| Element to write starting at index specified | |

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

<a id="writeInt64TableElementAsString"></a>
# **writeInt64TableElementAsString**
> writeInt64TableElementAsString(tableName, index, int64ElementObject)



Write specified integer64 table element as string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to write
    Integer index = 56; // Integer | Index of element to write
    Int64StringValueObject int64ElementObject = new Int64StringValueObject(); // Int64StringValueObject | Element to write starting at index specified
    try {
      apiInstance.writeInt64TableElementAsString(tableName, index, int64ElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt64TableElementAsString");
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
| **tableName** | **String**| Name of the integer64 table to write | |
| **index** | **Integer**| Index of element to write | |
| **int64ElementObject** | [**Int64StringValueObject**](Int64StringValueObject.md)| Element to write starting at index specified | |

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

<a id="writeInt64Var"></a>
# **writeInt64Var**
> writeInt64Var(int64Name, body)



Sets the value of an integer64 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to write
    Int64ValueObject body = new Int64ValueObject(); // Int64ValueObject | Value to write to the integer64 variable
    try {
      apiInstance.writeInt64Var(int64Name, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt64Var");
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
| **int64Name** | **String**| Name of integer64 variable to write | |
| **body** | [**Int64ValueObject**](Int64ValueObject.md)| Value to write to the integer64 variable | |

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

<a id="writeInt64VarAsString"></a>
# **writeInt64VarAsString**
> writeInt64VarAsString(int64Name, body)



Sets the value of an integer64 variable as a string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to write
    Int64StringValueObject body = new Int64StringValueObject(); // Int64StringValueObject | Value to write to the integer64 variable
    try {
      apiInstance.writeInt64VarAsString(int64Name, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeInt64VarAsString");
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
| **int64Name** | **String**| Name of integer64 variable to write | |
| **body** | [**Int64StringValueObject**](Int64StringValueObject.md)| Value to write to the integer64 variable | |

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

<a id="writeStringTable"></a>
# **writeStringTable**
> ErrorResponse200OKish writeStringTable(tableName, stringArray, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to write; starting index may be specified
    List<String> stringArray = Arrays.asList(); // List<String> | Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit
    Integer startIndex = 56; // Integer | Index of first element to write (default is 0)
    try {
      ErrorResponse200OKish result = apiInstance.writeStringTable(tableName, stringArray, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeStringTable");
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
| **tableName** | **String**| Name of string table to write; starting index may be specified | |
| **stringArray** | [**List&lt;String&gt;**](String.md)| Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit | |
| **startIndex** | **Integer**| Index of first element to write (default is 0) | [optional] |

### Return type

[**ErrorResponse200OKish**](ErrorResponse200OKish.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - but check details for any error messages |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeStringTableElement"></a>
# **writeStringTableElement**
> writeStringTableElement(tableName, index, stringElementObject)



Write specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to write
    Integer index = 56; // Integer | Index of element to write
    StringValueObject stringElementObject = new StringValueObject(); // StringValueObject | Element to write starting at index
    try {
      apiInstance.writeStringTableElement(tableName, index, stringElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeStringTableElement");
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
| **tableName** | **String**| Name of string table to write | |
| **index** | **Integer**| Index of element to write | |
| **stringElementObject** | [**StringValueObject**](StringValueObject.md)| Element to write starting at index | |

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

<a id="writeStringVar"></a>
# **writeStringVar**
> ErrorResponse200OKish writeStringVar(stringName, body)



Sets the value of a string variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AllApi apiInstance = new AllApi(defaultClient);
    String stringName = "stringName_example"; // String | Name of string variable to write
    StringValueObject body = new StringValueObject(); // StringValueObject | String to write. If the value is longer than the string width, the string will be truncated to fit.
    try {
      ErrorResponse200OKish result = apiInstance.writeStringVar(stringName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#writeStringVar");
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
| **stringName** | **String**| Name of string variable to write | |
| **body** | [**StringValueObject**](StringValueObject.md)| String to write. If the value is longer than the string width, the string will be truncated to fit. | |

### Return type

[**ErrorResponse200OKish**](ErrorResponse200OKish.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - but check details for any error messages |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

