# ValuespaceApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**add**](ValuespaceApi.md#add) | **POST** /mimic/agent/{agentNum}/value/add/{object}/{instance} | Add an entry to a table. |
| [**evalValue**](ValuespaceApi.md#evalValue) | **GET** /mimic/agent/{agentNum}/value/eval/{object}/{instance} | Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests. |
| [**getInfo**](ValuespaceApi.md#getInfo) | **GET** /mimic/agent/{agentNum}/value/info/{object} | Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS. |
| [**getInstances**](ValuespaceApi.md#getInstances) | **GET** /mimic/agent/{agentNum}/value/instances/{object} | Display the MIB object instances for the specified object. |
| [**getMib**](ValuespaceApi.md#getMib) | **GET** /mimic/agent/{agentNum}/value/mib/{object} | Return the MIB that defines the specified object. |
| [**getName**](ValuespaceApi.md#getName) | **GET** /mimic/agent/{agentNum}/value/name/{OID} | Return the symbolic name of the specified object identifier. |
| [**getObjects**](ValuespaceApi.md#getObjects) | **GET** /mimic/agent/{agentNum}/value/list/{OID} | Display the MIB objects below the current position |
| [**getOid**](ValuespaceApi.md#getOid) | **GET** /mimic/agent/{agentNum}/value/oid/{object} | Return the numeric OID of the specified object. |
| [**getState**](ValuespaceApi.md#getState) | **GET** /mimic/agent/{agentNum}/value/state/get/{object} | Get the state of a MIB object object. |
| [**getValue**](ValuespaceApi.md#getValue) | **GET** /mimic/agent/{agentNum}/value/get/{object}/{instance}/{variable} | Get a variable in the Value Space. |
| [**getVariables**](ValuespaceApi.md#getVariables) | **GET** /mimic/agent/{agentNum}/value/variables/{object}/{instance} | Display the variables for the specified instance instance for the specified MIB object object |
| [**mevalValue**](ValuespaceApi.md#mevalValue) | **GET** /mimic/agent/{agentNum}/value/meval/{objInsArray} | Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests. |
| [**mgetValue**](ValuespaceApi.md#mgetValue) | **GET** /mimic/agent/{agentNum}/value/mget/{objInsVarArray} | Get multiple variables in the Value Space. |
| [**msetValue**](ValuespaceApi.md#msetValue) | **PUT** /mimic/agent/{agentNum}/value/mset | Set multiple variables in the Value Space. |
| [**munsetValue**](ValuespaceApi.md#munsetValue) | **PUT** /mimic/agent/{agentNum}/value/munset | Unset multiple variables in the Value Space |
| [**remove**](ValuespaceApi.md#remove) | **DELETE** /mimic/agent/{agentNum}/value/remove/{object}/{instance} | Remove an entry from a table. |
| [**setState**](ValuespaceApi.md#setState) | **PUT** /mimic/agent/{agentNum}/value/state/set/{object}/{state} | Set the state of a MIB object object |
| [**setValue**](ValuespaceApi.md#setValue) | **PUT** /mimic/agent/{agentNum}/value/set/{object}/{instance}/{variable} | Set a variable in the Value Space. |
| [**splitOid**](ValuespaceApi.md#splitOid) | **GET** /mimic/agent/{agentNum}/value/split/{OID} | Split the numerical OID into the object OID and instance OID. |
| [**unsetValue**](ValuespaceApi.md#unsetValue) | **PUT** /mimic/agent/{agentNum}/value/unset/{object}/{instance}/{variable} | Unset a variable in the Value Space in order to free its memory. |


<a id="add"></a>
# **add**
> String add(agentNum, _object, instance)

Add an entry to a table.

The object needs to specify the MIB object with the INDEX clause, usually an object whose name ends with Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Object (column) of the table in the agent's value space
    String instance = "instance_example"; // String | Object (column) of the table in the agent's value space
    try {
      String result = apiInstance.add(agentNum, _object, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#add");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Object (column) of the table in the agent&#39;s value space | |
| **instance** | **String**| Object (column) of the table in the agent&#39;s value space | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="evalValue"></a>
# **evalValue**
> String evalValue(agentNum, _object, instance)

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
    String instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
    try {
      String result = apiInstance.evalValue(agentNum, _object, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#evalValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | |
| **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getInfo"></a>
# **getInfo**
> String getInfo(agentNum, _object)

Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.

Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the information of the object
    String _object = "_object_example"; // String | Object
    try {
      String result = apiInstance.getInfo(agentNum, _object);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getInfo");
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
| **agentNum** | **Integer**| Agent to show the information of the object | |
| **_object** | **String**| Object | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getInstances"></a>
# **getInstances**
> List&lt;String&gt; getInstances(agentNum, _object)

Display the MIB object instances for the specified object.

This enables MIB browsing of the MIB on the current agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Object (column) of the table in the agent's value space
    try {
      List<String> result = apiInstance.getInstances(agentNum, _object);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getInstances");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Object (column) of the table in the agent&#39;s value space | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getMib"></a>
# **getMib**
> String getMib(agentNum, _object)

Return the MIB that defines the specified object.

This will only return a MIB name if the object is unmistakeably defined in a MIB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the MIB
    String _object = "_object_example"; // String | Object
    try {
      String result = apiInstance.getMib(agentNum, _object);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getMib");
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
| **agentNum** | **Integer**| Agent to show the MIB | |
| **_object** | **String**| Object | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getName"></a>
# **getName**
> String getName(agentNum, OID)

Return the symbolic name of the specified object identifier.

Return the symbolic name of the specified object identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the object
    String OID = "OID_example"; // String | OID
    try {
      String result = apiInstance.getName(agentNum, OID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getName");
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
| **agentNum** | **Integer**| Agent to show the object | |
| **OID** | **String**| OID | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getObjects"></a>
# **getObjects**
> List&lt;String&gt; getObjects(agentNum, OID)

Display the MIB objects below the current position

This command is similar to the ls or dir operating system commands to list filesystem directories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the OID branches
    String OID = "OID_example"; // String | Current OID
    try {
      List<String> result = apiInstance.getObjects(agentNum, OID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getObjects");
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
| **agentNum** | **Integer**| Agent to show the OID branches | |
| **OID** | **String**| Current OID | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getOid"></a>
# **getOid**
> String getOid(agentNum, _object)

Return the numeric OID of the specified object.

Return the numeric OID of the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the OID
    String _object = "_object_example"; // String | Object
    try {
      String result = apiInstance.getOid(agentNum, _object);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getOid");
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
| **agentNum** | **Integer**| Agent to show the OID | |
| **_object** | **String**| Object | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getState"></a>
# **getState**
> String getState(agentNum, _object)

Get the state of a MIB object object.

To disable traversal into a MIB object and any subtree underneath, set the state to 0, else set the state to 1.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Object
    try {
      String result = apiInstance.getState(agentNum, _object);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getState");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Object | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getValue"></a>
# **getValue**
> String getValue(agentNum, _object, instance, variable)

Get a variable in the Value Space.

Get a variable in the Value Space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Object (column) of the table in the agent's value space
    String instance = "instance_example"; // String | Object (column) of the table in the agent's value space
    String variable = "variable_example"; // String | Object (column) of the table in the agent's value space
    try {
      String result = apiInstance.getValue(agentNum, _object, instance, variable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Object (column) of the table in the agent&#39;s value space | |
| **instance** | **String**| Object (column) of the table in the agent&#39;s value space | |
| **variable** | **String**| Object (column) of the table in the agent&#39;s value space | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getVariables"></a>
# **getVariables**
> List&lt;String&gt; getVariables(agentNum, _object, instance)

Display the variables for the specified instance instance for the specified MIB object object

This enables variable browsing of the MIB on the current agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
    String instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
    try {
      List<String> result = apiInstance.getVariables(agentNum, _object, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#getVariables");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | |
| **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="mevalValue"></a>
# **mevalValue**
> List&lt;String&gt; mevalValue(agentNum, objInsArray)

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    List<List<String>> objInsArray = Arrays.asList(new ArrayList<>()); // List<List<String>> | Multiple objects or object (column) of the table in the agent's value space.
    try {
      List<String> result = apiInstance.mevalValue(agentNum, objInsArray);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#mevalValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **objInsArray** | [**List&lt;List&lt;String&gt;&gt;**](List&lt;String&gt;.md)| Multiple objects or object (column) of the table in the agent&#39;s value space. | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="mgetValue"></a>
# **mgetValue**
> List&lt;String&gt; mgetValue(agentNum, objInsVarArray)

Get multiple variables in the Value Space.

This is a performance optimization of the mimic value get command, to be used when many variables are requested.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    List<List<String>> objInsVarArray = Arrays.asList(new ArrayList<>()); // List<List<String>> | Multiple objects or object (column) of the table in the agent's value space.
    try {
      List<String> result = apiInstance.mgetValue(agentNum, objInsVarArray);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#mgetValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **objInsVarArray** | [**List&lt;List&lt;String&gt;&gt;**](List&lt;String&gt;.md)| Multiple objects or object (column) of the table in the agent&#39;s value space. | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="msetValue"></a>
# **msetValue**
> String msetValue(agentNum, requestBody)

Set multiple variables in the Value Space.

This is a performance optimization of the mimic value set command, to be used when many variables are to be set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    List<List<String>> requestBody = Arrays.asList(new ArrayList<>()); // List<List<String>> | objInsVarValArray
    try {
      String result = apiInstance.msetValue(agentNum, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#msetValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **requestBody** | [**List&lt;List&lt;String&gt;&gt;**](List.md)| objInsVarValArray | [optional] |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="munsetValue"></a>
# **munsetValue**
> String munsetValue(agentNum, requestBody)

Unset multiple variables in the Value Space

This is a performance optimization of the mimic value unset command, to be used when many variables are to be unset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    List<List<String>> requestBody = Arrays.asList(new ArrayList<>()); // List<List<String>> | objInsVarArray
    try {
      String result = apiInstance.munsetValue(agentNum, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#munsetValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **requestBody** | [**List&lt;List&lt;String&gt;&gt;**](List.md)| objInsVarArray | [optional] |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="remove"></a>
# **remove**
> String remove(agentNum, _object, instance)

Remove an entry from a table.

The object needs to specify the MIB object with the INDEX clause, usually an object whose name ends with Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Object (column) of the table in the agent's value space
    String instance = "instance_example"; // String | Object (column) of the table in the agent's value space
    try {
      String result = apiInstance.remove(agentNum, _object, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#remove");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Object (column) of the table in the agent&#39;s value space | |
| **instance** | **String**| Object (column) of the table in the agent&#39;s value space | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setState"></a>
# **setState**
> String setState(agentNum, _object, state)

Set the state of a MIB object object

To disable traversal into a MIB object and any subtree underneath, set the state to 0, else set the state to 1.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Object
    Integer state = 56; // Integer | State
    try {
      String result = apiInstance.setState(agentNum, _object, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#setState");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Object | |
| **state** | **Integer**| State | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setValue"></a>
# **setValue**
> String setValue(agentNum, _object, instance, variable, body)

Set a variable in the Value Space.

NOTE to set a binary string value, specify a string starting with \\\\x followed by pairs of hexadecimal digits, eg. \&quot;\\\\x 01 23 45\&quot;. This command also assigns SNMP PDU action scripts for GET* and SET requests on a MIB object. The instance parameter must be 0. The following variables enable actions, g - The specified TCL script will be run on GET or GETNEXT requests. It has to exist under the simulation directory. s - The specified script will be run on SET requests. It has to exist under the simulation directory. This command also controls advanced trap generation functionality. The following variables control trap generation r, tu, c - These variables together represent the rate settings for the trap. r and tu is the actual per second rate and c represents the total duration in seconds for which the trap is sent. As soon as the c variable is set, the trap generation begins, for this reason it should be the last variable set for a particular trap. The following variables have to be set before setting the c variable to modify the behavior of the generated trap(s). OBJECT - An object name when used as a variable is looked up during the trap send and the value of that variable is included in the PDU. OBJECT.i - This type of variable will be used to assign an optional instance for the specified object in the traps varbind. The value of this variable identifies the index. e.g. The commands below will send ifIndex.2 with a value of 5 in the linkUp trap PDU. i - This variable is used to specify any extra version specific information to the trap generation code. Here is what it can be used to represent for various SNMP versions SNMPv1 - [community_string][,[enterprise][,agent_addr]] SNMPv2c - community_string SNMPv2 - source_party,destination_party,context SNMPv3 - user_name,context v - This variable lets the user override the version of the PDU being generated. The possible values are - \&quot;1\&quot;, \&quot;2c\&quot;, \&quot;2\&quot; and \&quot;3\&quot;. o - This variable is used for traps that need extra variables to be added to the PDU along with the ones defined in the MIB as its variables. This lets the user force extra objects (along with instances if needed). All variables to be sent need to be assigned to the o variable. O - To omit any variables which are defined in the MIB you can use the O (capital o) variable. This needs to be set to the list of OIDs of the variable bindings in the order defined in the MIB. ip - The variable ip is used for generating the trap from the N-th IP alias address. a - This variable associates an action script to the trap or INFORM request. The action script specified in the value of this variable has to exist in the simulation directory. It will be executed before each instance of the trap is sent out. I - This optional variable controls the generation of INFORM PDUs. An INFORM is sent only if the variable is non-zero, else a TRAP is generated. R, T, E - This variable associates an action script to the INFORM request. The action script specified in the value of this variable has to exist in the simulation directory. The action script associated with the R variable will be executed on receiving a INFORM RESPONSE, the one associated with the T variable on a timeout (ie. no response), the one associated with the E variable on a report PDU. eid.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine id for the destination specified by IP-ADDRESS and optionally by PORT. eb.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine boots. et.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
    String instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
    String variable = "variable_example"; // String | Variable
    String body = "body_example"; // String | Value
    try {
      String result = apiInstance.setValue(agentNum, _object, instance, variable, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#setValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | |
| **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | |
| **variable** | **String**| Variable | |
| **body** | **String**| Value | [optional] |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="splitOid"></a>
# **splitOid**
> List&lt;String&gt; splitOid(agentNum, OID)

Split the numerical OID into the object OID and instance OID.

This is useful if you have an OID which is a combination of object and instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String OID = "OID_example"; // String | OID
    try {
      List<String> result = apiInstance.splitOid(agentNum, OID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#splitOid");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **OID** | **String**| OID | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="unsetValue"></a>
# **unsetValue**
> String unsetValue(agentNum, _object, instance, variable)

Unset a variable in the Value Space in order to free its memory.

Only variables that have previously been set can be unset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuespaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ValuespaceApi apiInstance = new ValuespaceApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String _object = "_object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
    String instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
    String variable = "variable_example"; // String | Variable
    try {
      String result = apiInstance.unsetValue(agentNum, _object, instance, variable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuespaceApi#unsetValue");
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
| **agentNum** | **Integer**| Agent of the value space | |
| **_object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | |
| **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | |
| **variable** | **String**| Variable | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

