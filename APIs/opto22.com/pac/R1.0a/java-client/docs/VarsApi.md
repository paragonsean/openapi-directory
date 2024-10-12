# VarsApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**readDownTimerValue_0**](VarsApi.md#readDownTimerValue_0) | **GET** /device/strategy/vars/downTimers/{downTimerName}/value |  |
| [**readDownTimerVars_0**](VarsApi.md#readDownTimerVars_0) | **GET** /device/strategy/vars/downTimers |  |
| [**readFloatVar_0**](VarsApi.md#readFloatVar_0) | **GET** /device/strategy/vars/floats/{floatName} |  |
| [**readFloatVars_0**](VarsApi.md#readFloatVars_0) | **GET** /device/strategy/vars/floats |  |
| [**readInt32Var_0**](VarsApi.md#readInt32Var_0) | **GET** /device/strategy/vars/int32s/{int32Name} |  |
| [**readInt32Vars_0**](VarsApi.md#readInt32Vars_0) | **GET** /device/strategy/vars/int32s |  |
| [**readInt64VarAsString_0**](VarsApi.md#readInt64VarAsString_0) | **GET** /device/strategy/vars/int64s/{int64Name}/_string |  |
| [**readInt64Var_0**](VarsApi.md#readInt64Var_0) | **GET** /device/strategy/vars/int64s/{int64Name} |  |
| [**readInt64VarsAsStrings_0**](VarsApi.md#readInt64VarsAsStrings_0) | **GET** /device/strategy/vars/int64s/_string |  |
| [**readInt64Vars_0**](VarsApi.md#readInt64Vars_0) | **GET** /device/strategy/vars/int64s |  |
| [**readStringVar_0**](VarsApi.md#readStringVar_0) | **GET** /device/strategy/vars/strings/{stringName} |  |
| [**readStringVars_0**](VarsApi.md#readStringVars_0) | **GET** /device/strategy/vars/strings |  |
| [**readUpTimerValue_0**](VarsApi.md#readUpTimerValue_0) | **GET** /device/strategy/vars/upTimers/{upTimerName}/value |  |
| [**readUpTimerVars_0**](VarsApi.md#readUpTimerVars_0) | **GET** /device/strategy/vars/upTimers |  |
| [**writeFloatVar_0**](VarsApi.md#writeFloatVar_0) | **POST** /device/strategy/vars/floats/{floatName} |  |
| [**writeInt32Var_0**](VarsApi.md#writeInt32Var_0) | **POST** /device/strategy/vars/int32s/{int32Name} |  |
| [**writeInt64VarAsString_0**](VarsApi.md#writeInt64VarAsString_0) | **POST** /device/strategy/vars/int64s/{int64Name}/_string |  |
| [**writeInt64Var_0**](VarsApi.md#writeInt64Var_0) | **POST** /device/strategy/vars/int64s/{int64Name} |  |
| [**writeStringVar_0**](VarsApi.md#writeStringVar_0) | **POST** /device/strategy/vars/strings/{stringName} |  |


<a id="readDownTimerValue_0"></a>
# **readDownTimerValue_0**
> FloatValueObject readDownTimerValue_0(downTimerName)



Returns current value of the specified down timer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String downTimerName = "downTimerName_example"; // String | Name of the down timer variable to read
    try {
      FloatValueObject result = apiInstance.readDownTimerValue_0(downTimerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readDownTimerValue_0");
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

<a id="readDownTimerVars_0"></a>
# **readDownTimerVars_0**
> List&lt;FloatVar&gt; readDownTimerVars_0()



Returns the name and current value of all down timers in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readDownTimerVars_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readDownTimerVars_0");
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

<a id="readFloatVar_0"></a>
# **readFloatVar_0**
> FloatValueObject readFloatVar_0(floatName)



Returns value of the specified float variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String floatName = "floatName_example"; // String | Name of float variable to read
    try {
      FloatValueObject result = apiInstance.readFloatVar_0(floatName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readFloatVar_0");
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

<a id="readFloatVars_0"></a>
# **readFloatVars_0**
> List&lt;FloatVar&gt; readFloatVars_0()



Returns the name and value of all (single-precision) float variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readFloatVars_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readFloatVars_0");
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

<a id="readInt32Var_0"></a>
# **readInt32Var_0**
> Int32ValueObject readInt32Var_0(int32Name)



Returns value of the specified integer32 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String int32Name = "int32Name_example"; // String | Name of integer32 variable to read
    try {
      Int32ValueObject result = apiInstance.readInt32Var_0(int32Name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readInt32Var_0");
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

<a id="readInt32Vars_0"></a>
# **readInt32Vars_0**
> List&lt;Int32Var&gt; readInt32Vars_0()



Returns the name and value of all integer32 variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<Int32Var> result = apiInstance.readInt32Vars_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readInt32Vars_0");
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

<a id="readInt64VarAsString_0"></a>
# **readInt64VarAsString_0**
> Int64StringValueObject readInt64VarAsString_0(int64Name)



Returns value of the specified integer64 variable as a string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to read
    try {
      Int64StringValueObject result = apiInstance.readInt64VarAsString_0(int64Name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readInt64VarAsString_0");
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

<a id="readInt64Var_0"></a>
# **readInt64Var_0**
> Int64ValueObject readInt64Var_0(int64Name)



Returns value of the specified integer64 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to read
    try {
      Int64ValueObject result = apiInstance.readInt64Var_0(int64Name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readInt64Var_0");
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

<a id="readInt64VarsAsStrings_0"></a>
# **readInt64VarsAsStrings_0**
> List&lt;Int64VarAsString&gt; readInt64VarsAsStrings_0()



Returns the name and value as a string of all integer64 variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<Int64VarAsString> result = apiInstance.readInt64VarsAsStrings_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readInt64VarsAsStrings_0");
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

<a id="readInt64Vars_0"></a>
# **readInt64Vars_0**
> List&lt;Int64Var&gt; readInt64Vars_0()



Returns the name and value of all integer64 variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<Int64Var> result = apiInstance.readInt64Vars_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readInt64Vars_0");
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

<a id="readStringVar_0"></a>
# **readStringVar_0**
> StringValueObject readStringVar_0(stringName)



Returns value of the specified string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String stringName = "stringName_example"; // String | Name of string variable to read
    try {
      StringValueObject result = apiInstance.readStringVar_0(stringName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readStringVar_0");
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

<a id="readStringVars_0"></a>
# **readStringVars_0**
> List&lt;StringVar&gt; readStringVars_0()



Returns the name and value of all string variables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<StringVar> result = apiInstance.readStringVars_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readStringVars_0");
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

<a id="readUpTimerValue_0"></a>
# **readUpTimerValue_0**
> FloatValueObject readUpTimerValue_0(upTimerName)



Returns current value of the specified up timer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String upTimerName = "upTimerName_example"; // String | Name of the up timer variable to read
    try {
      FloatValueObject result = apiInstance.readUpTimerValue_0(upTimerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readUpTimerValue_0");
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

<a id="readUpTimerVars_0"></a>
# **readUpTimerVars_0**
> List&lt;FloatVar&gt; readUpTimerVars_0()



Returns the name and current value of all up timers in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    try {
      List<FloatVar> result = apiInstance.readUpTimerVars_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#readUpTimerVars_0");
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

<a id="writeFloatVar_0"></a>
# **writeFloatVar_0**
> writeFloatVar_0(floatName, body)



Sets the value of a float variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String floatName = "floatName_example"; // String | Name of the float variable to write
    FloatValueObject body = new FloatValueObject(); // FloatValueObject | Value to write to the float variable
    try {
      apiInstance.writeFloatVar_0(floatName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#writeFloatVar_0");
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

<a id="writeInt32Var_0"></a>
# **writeInt32Var_0**
> writeInt32Var_0(int32Name, body)



Sets the value of an integer32 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String int32Name = "int32Name_example"; // String | Name of integer32 variable to write
    Int32ValueObject body = new Int32ValueObject(); // Int32ValueObject | Value to write to the integer32 variable
    try {
      apiInstance.writeInt32Var_0(int32Name, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#writeInt32Var_0");
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

<a id="writeInt64VarAsString_0"></a>
# **writeInt64VarAsString_0**
> writeInt64VarAsString_0(int64Name, body)



Sets the value of an integer64 variable as a string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to write
    Int64StringValueObject body = new Int64StringValueObject(); // Int64StringValueObject | Value to write to the integer64 variable
    try {
      apiInstance.writeInt64VarAsString_0(int64Name, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#writeInt64VarAsString_0");
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

<a id="writeInt64Var_0"></a>
# **writeInt64Var_0**
> writeInt64Var_0(int64Name, body)



Sets the value of an integer64 variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String int64Name = "int64Name_example"; // String | Name of integer64 variable to write
    Int64ValueObject body = new Int64ValueObject(); // Int64ValueObject | Value to write to the integer64 variable
    try {
      apiInstance.writeInt64Var_0(int64Name, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#writeInt64Var_0");
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

<a id="writeStringVar_0"></a>
# **writeStringVar_0**
> ErrorResponse200OKish writeStringVar_0(stringName, body)



Sets the value of a string variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    VarsApi apiInstance = new VarsApi(defaultClient);
    String stringName = "stringName_example"; // String | Name of string variable to write
    StringValueObject body = new StringValueObject(); // StringValueObject | String to write. If the value is longer than the string width, the string will be truncated to fit.
    try {
      ErrorResponse200OKish result = apiInstance.writeStringVar_0(stringName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VarsApi#writeStringVar_0");
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

