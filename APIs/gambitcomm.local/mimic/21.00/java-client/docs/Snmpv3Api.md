# Snmpv3Api

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolSnmpv3AccessAdd**](Snmpv3Api.md#protocolSnmpv3AccessAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/add/{groupName}/{prefix}/{securityModel}/{securityLevel}/{contextMatch}/{readView}/{writeView}/{notifyView} | Adds a new access entry with the specified parameters. |
| [**protocolSnmpv3AccessClear**](Snmpv3Api.md#protocolSnmpv3AccessClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/clear | Clears all access entries. |
| [**protocolSnmpv3AccessDel**](Snmpv3Api.md#protocolSnmpv3AccessDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/del/{accessName} | Deletes the specified access entry. |
| [**protocolSnmpv3AccessList**](Snmpv3Api.md#protocolSnmpv3AccessList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/list | Returns the current acccess entries as an array of strings. |
| [**protocolSnmpv3GetConfig**](Snmpv3Api.md#protocolSnmpv3GetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/config | Returns the SNMPv3 configuration. |
| [**protocolSnmpv3GetContextEngineid**](Snmpv3Api.md#protocolSnmpv3GetContextEngineid) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/context_engineid | Retrieves the contextEngineID for the agent instance. |
| [**protocolSnmpv3GetEngineboots**](Snmpv3Api.md#protocolSnmpv3GetEngineboots) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/engineboots | Retrieves the number of times the agent has been restarted. |
| [**protocolSnmpv3GetEngineid**](Snmpv3Api.md#protocolSnmpv3GetEngineid) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/engineid | For started agents, retrieves the current engineID in use by the snmpv3 module. |
| [**protocolSnmpv3GetEnginetime**](Snmpv3Api.md#protocolSnmpv3GetEnginetime) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/enginetime | Retrieves the time in seconds for which the agent has been running. |
| [**protocolSnmpv3GroupAdd**](Snmpv3Api.md#protocolSnmpv3GroupAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/add/{groupName}/{securityModel}/{securityName} | Adds a new group entry with the specified parameters. |
| [**protocolSnmpv3GroupClear**](Snmpv3Api.md#protocolSnmpv3GroupClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/clear | Clears all group entries. |
| [**protocolSnmpv3GroupDel**](Snmpv3Api.md#protocolSnmpv3GroupDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/del/{groupName} | Deletes the specified group entry. |
| [**protocolSnmpv3GroupList**](Snmpv3Api.md#protocolSnmpv3GroupList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/list | Returns the current group entries as an array of strings. |
| [**protocolSnmpv3SetConfig**](Snmpv3Api.md#protocolSnmpv3SetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/set/config/{parameter}/{value} | Changes the SNMPv3 configuration. |
| [**protocolSnmpv3UserAdd**](Snmpv3Api.md#protocolSnmpv3UserAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/add/{userName}/{securityName}/{authProtocol}/{authKey}/{privProtocol}/{privKey} | Adds a new user entry with the specified parameters. |
| [**protocolSnmpv3UserClear**](Snmpv3Api.md#protocolSnmpv3UserClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/clear | Clears all user entries. |
| [**protocolSnmpv3UserDel**](Snmpv3Api.md#protocolSnmpv3UserDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/del/{userName} | Deletes the specified user entry. |
| [**protocolSnmpv3UserList**](Snmpv3Api.md#protocolSnmpv3UserList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/list | Returns the current user entries as a Tcl list. |
| [**protocolSnmpv3UsmSave**](Snmpv3Api.md#protocolSnmpv3UsmSave) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/usm/save | Saves current user settings in the currently loaded USM config file. |
| [**protocolSnmpv3UsmSaveas**](Snmpv3Api.md#protocolSnmpv3UsmSaveas) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/usm/saveas/{filename} | Saves current user settings in the specified USM config file. |
| [**protocolSnmpv3VacmSave**](Snmpv3Api.md#protocolSnmpv3VacmSave) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/vacm/save | Saves current group, access, view settings in the currently loaded VACM config file. |
| [**protocolSnmpv3VacmSaveas**](Snmpv3Api.md#protocolSnmpv3VacmSaveas) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/vacm/saveas/{filename} | Saves current group, access, view settings in the specified VACM config file. |
| [**protocolSnmpv3ViewAdd**](Snmpv3Api.md#protocolSnmpv3ViewAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/add/{viewName}/{viewType}/{subtree}/{mask} | Adds a new view entry with the specified parameters. |
| [**protocolSnmpv3ViewClear**](Snmpv3Api.md#protocolSnmpv3ViewClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/clear | Clears all view entries. |
| [**protocolSnmpv3ViewDel**](Snmpv3Api.md#protocolSnmpv3ViewDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/del/{viewName} | Deletes the specified view entry. |
| [**protocolSnmpv3ViewList**](Snmpv3Api.md#protocolSnmpv3ViewList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/list | Returns the current view entries as an array of strings. |


<a id="protocolSnmpv3AccessAdd"></a>
# **protocolSnmpv3AccessAdd**
> String protocolSnmpv3AccessAdd(agentNum, groupName, prefix, securityModel, securityLevel, contextMatch, readView, writeView, notifyView)

Adds a new access entry with the specified parameters.

Adds a new access entry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 access
    String groupName = "groupName_example"; // String | SNMPv3 access name
    String prefix = "prefix_example"; // String | SNMPv3 prefix
    String securityModel = "securityModel_example"; // String | SNMPv3 access security model
    String securityLevel = "securityLevel_example"; // String | SNMPv3 access security level
    String contextMatch = "contextMatch_example"; // String | SNMPv3 access context match
    String readView = "readView_example"; // String | SNMPv3 access read view
    String writeView = "writeView_example"; // String | SNMPv3 access write view
    String notifyView = "notifyView_example"; // String | SNMPv3 access notify view
    try {
      String result = apiInstance.protocolSnmpv3AccessAdd(agentNum, groupName, prefix, securityModel, securityLevel, contextMatch, readView, writeView, notifyView);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3AccessAdd");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 access | |
| **groupName** | **String**| SNMPv3 access name | |
| **prefix** | **String**| SNMPv3 prefix | |
| **securityModel** | **String**| SNMPv3 access security model | |
| **securityLevel** | **String**| SNMPv3 access security level | |
| **contextMatch** | **String**| SNMPv3 access context match | |
| **readView** | **String**| SNMPv3 access read view | |
| **writeView** | **String**| SNMPv3 access write view | |
| **notifyView** | **String**| SNMPv3 access notify view | |

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

<a id="protocolSnmpv3AccessClear"></a>
# **protocolSnmpv3AccessClear**
> String protocolSnmpv3AccessClear(agentNum)

Clears all access entries.

Clears all access entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 access
    try {
      String result = apiInstance.protocolSnmpv3AccessClear(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3AccessClear");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 access | |

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

<a id="protocolSnmpv3AccessDel"></a>
# **protocolSnmpv3AccessDel**
> String protocolSnmpv3AccessDel(agentNum, accessName)

Deletes the specified access entry.

Deletes the specified access entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 access
    String accessName = "accessName_example"; // String | SNMPv3 access name
    try {
      String result = apiInstance.protocolSnmpv3AccessDel(agentNum, accessName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3AccessDel");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 access | |
| **accessName** | **String**| SNMPv3 access name | |

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

<a id="protocolSnmpv3AccessList"></a>
# **protocolSnmpv3AccessList**
> List&lt;String&gt; protocolSnmpv3AccessList(agentNum)

Returns the current acccess entries as an array of strings.

Returns the current acccess entries as an array of strings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      List<String> result = apiInstance.protocolSnmpv3AccessList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3AccessList");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

<a id="protocolSnmpv3GetConfig"></a>
# **protocolSnmpv3GetConfig**
> ConfigSNMPv3 protocolSnmpv3GetConfig(agentNum)

Returns the SNMPv3 configuration.

Returns the SNMPv3 configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      ConfigSNMPv3 result = apiInstance.protocolSnmpv3GetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GetConfig");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

### Return type

[**ConfigSNMPv3**](ConfigSNMPv3.md)

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

<a id="protocolSnmpv3GetContextEngineid"></a>
# **protocolSnmpv3GetContextEngineid**
> String protocolSnmpv3GetContextEngineid(agentNum)

Retrieves the contextEngineID for the agent instance.

Retrieves the contextEngineID for the agent instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 engine
    try {
      String result = apiInstance.protocolSnmpv3GetContextEngineid(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GetContextEngineid");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 engine | |

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

<a id="protocolSnmpv3GetEngineboots"></a>
# **protocolSnmpv3GetEngineboots**
> Integer protocolSnmpv3GetEngineboots(agentNum)

Retrieves the number of times the agent has been restarted.

Retrieves the number of times the agent has been restarted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 engine
    try {
      Integer result = apiInstance.protocolSnmpv3GetEngineboots(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GetEngineboots");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 engine | |

### Return type

**Integer**

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

<a id="protocolSnmpv3GetEngineid"></a>
# **protocolSnmpv3GetEngineid**
> String protocolSnmpv3GetEngineid(agentNum)

For started agents, retrieves the current engineID in use by the snmpv3 module.

For stopped agents, this operation is meaningless. If not explicitly set by the user then the autogenerated engineID is returned. The format of the engineID is in the familiar hex format, eg. \\x01 23 45 67 89...

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      String result = apiInstance.protocolSnmpv3GetEngineid(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GetEngineid");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

<a id="protocolSnmpv3GetEnginetime"></a>
# **protocolSnmpv3GetEnginetime**
> Integer protocolSnmpv3GetEnginetime(agentNum)

Retrieves the time in seconds for which the agent has been running.

Retrieves the time in seconds for which the agent has been running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 engine
    try {
      Integer result = apiInstance.protocolSnmpv3GetEnginetime(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GetEnginetime");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 engine | |

### Return type

**Integer**

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

<a id="protocolSnmpv3GroupAdd"></a>
# **protocolSnmpv3GroupAdd**
> String protocolSnmpv3GroupAdd(agentNum, groupName, securityModel, securityName)

Adds a new group entry with the specified parameters.

Adds a new group entry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 group
    String groupName = "groupName_example"; // String | SNMPv3 group name
    String securityModel = "securityModel_example"; // String | SNMPv3 group security model
    String securityName = "securityName_example"; // String | SNMPv3 group security name
    try {
      String result = apiInstance.protocolSnmpv3GroupAdd(agentNum, groupName, securityModel, securityName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GroupAdd");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 group | |
| **groupName** | **String**| SNMPv3 group name | |
| **securityModel** | **String**| SNMPv3 group security model | |
| **securityName** | **String**| SNMPv3 group security name | |

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

<a id="protocolSnmpv3GroupClear"></a>
# **protocolSnmpv3GroupClear**
> String protocolSnmpv3GroupClear(agentNum)

Clears all group entries.

Clears all group entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 group
    try {
      String result = apiInstance.protocolSnmpv3GroupClear(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GroupClear");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 group | |

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

<a id="protocolSnmpv3GroupDel"></a>
# **protocolSnmpv3GroupDel**
> String protocolSnmpv3GroupDel(agentNum, groupName)

Deletes the specified group entry.

Deletes the specified group entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 group
    String groupName = "groupName_example"; // String | SNMPv3 group name
    try {
      String result = apiInstance.protocolSnmpv3GroupDel(agentNum, groupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GroupDel");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 group | |
| **groupName** | **String**| SNMPv3 group name | |

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

<a id="protocolSnmpv3GroupList"></a>
# **protocolSnmpv3GroupList**
> List&lt;String&gt; protocolSnmpv3GroupList(agentNum)

Returns the current group entries as an array of strings.

Returns the current group entries as an array of strings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      List<String> result = apiInstance.protocolSnmpv3GroupList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3GroupList");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

<a id="protocolSnmpv3SetConfig"></a>
# **protocolSnmpv3SetConfig**
> String protocolSnmpv3SetConfig(agentNum, parameter, value)

Changes the SNMPv3 configuration.

Changes the SNMPv3 configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    String parameter = "parameter_example"; // String | SNMPv3 configuration parameter
    String value = "value_example"; // String | SNMPv3 parameter value
    try {
      String result = apiInstance.protocolSnmpv3SetConfig(agentNum, parameter, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3SetConfig");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |
| **parameter** | **String**| SNMPv3 configuration parameter | |
| **value** | **String**| SNMPv3 parameter value | |

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

<a id="protocolSnmpv3UserAdd"></a>
# **protocolSnmpv3UserAdd**
> String protocolSnmpv3UserAdd(agentNum, userName, securityName, authProtocol, authKey, privProtocol, privKey)

Adds a new user entry with the specified parameters.

Adds a new user entry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 user
    String userName = "userName_example"; // String | SNMPv3 user name
    String securityName = "securityName_example"; // String | SNMPv3 user security name
    String authProtocol = "authProtocol_example"; // String | SNMPv3 user authentication protocol
    String authKey = "authKey_example"; // String | SNMPv3 user authentication key
    String privProtocol = "privProtocol_example"; // String | SNMPv3 user privacy encryption protocol
    String privKey = "privKey_example"; // String | SNMPv3 user privacy encryption key
    try {
      String result = apiInstance.protocolSnmpv3UserAdd(agentNum, userName, securityName, authProtocol, authKey, privProtocol, privKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3UserAdd");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 user | |
| **userName** | **String**| SNMPv3 user name | |
| **securityName** | **String**| SNMPv3 user security name | |
| **authProtocol** | **String**| SNMPv3 user authentication protocol | |
| **authKey** | **String**| SNMPv3 user authentication key | |
| **privProtocol** | **String**| SNMPv3 user privacy encryption protocol | |
| **privKey** | **String**| SNMPv3 user privacy encryption key | |

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

<a id="protocolSnmpv3UserClear"></a>
# **protocolSnmpv3UserClear**
> String protocolSnmpv3UserClear(agentNum)

Clears all user entries.

Clears all user entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 user
    try {
      String result = apiInstance.protocolSnmpv3UserClear(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3UserClear");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 user | |

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

<a id="protocolSnmpv3UserDel"></a>
# **protocolSnmpv3UserDel**
> String protocolSnmpv3UserDel(agentNum, userName)

Deletes the specified user entry.

Deletes the specified user entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 user
    String userName = "userName_example"; // String | SNMPv3 user name
    try {
      String result = apiInstance.protocolSnmpv3UserDel(agentNum, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3UserDel");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 user | |
| **userName** | **String**| SNMPv3 user name | |

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

<a id="protocolSnmpv3UserList"></a>
# **protocolSnmpv3UserList**
> List&lt;String&gt; protocolSnmpv3UserList(agentNum)

Returns the current user entries as a Tcl list.

Returns the current user entries as a Tcl list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      List<String> result = apiInstance.protocolSnmpv3UserList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3UserList");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

<a id="protocolSnmpv3UsmSave"></a>
# **protocolSnmpv3UsmSave**
> List&lt;String&gt; protocolSnmpv3UsmSave(agentNum)

Saves current user settings in the currently loaded USM config file.

Saves current user settings in the currently loaded USM config file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      List<String> result = apiInstance.protocolSnmpv3UsmSave(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3UsmSave");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

<a id="protocolSnmpv3UsmSaveas"></a>
# **protocolSnmpv3UsmSaveas**
> List&lt;String&gt; protocolSnmpv3UsmSaveas(agentNum, filename)

Saves current user settings in the specified USM config file.

Saves current user settings in the specified USM config file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    String filename = "filename_example"; // String | Filename to save
    try {
      List<String> result = apiInstance.protocolSnmpv3UsmSaveas(agentNum, filename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3UsmSaveas");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |
| **filename** | **String**| Filename to save | |

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

<a id="protocolSnmpv3VacmSave"></a>
# **protocolSnmpv3VacmSave**
> List&lt;String&gt; protocolSnmpv3VacmSave(agentNum)

Saves current group, access, view settings in the currently loaded VACM config file.

Saves current group, access, view settings in the currently loaded VACM config file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      List<String> result = apiInstance.protocolSnmpv3VacmSave(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3VacmSave");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

<a id="protocolSnmpv3VacmSaveas"></a>
# **protocolSnmpv3VacmSaveas**
> List&lt;String&gt; protocolSnmpv3VacmSaveas(agentNum, filename)

Saves current group, access, view settings in the specified VACM config file.

Saves current group, access, view settings in the specified VACM config file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    String filename = "filename_example"; // String | Filename to save
    try {
      List<String> result = apiInstance.protocolSnmpv3VacmSaveas(agentNum, filename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3VacmSaveas");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |
| **filename** | **String**| Filename to save | |

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

<a id="protocolSnmpv3ViewAdd"></a>
# **protocolSnmpv3ViewAdd**
> String protocolSnmpv3ViewAdd(agentNum, viewName, viewType, subtree, mask)

Adds a new view entry with the specified parameters.

Adds a new view entry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 view
    String viewName = "viewName_example"; // String | SNMPv3 view name
    String viewType = "viewType_example"; // String | SNMPv3 view type
    String subtree = "subtree_example"; // String | SNMPv3 view subtree
    String mask = "mask_example"; // String | SNMPv3 view mask
    try {
      String result = apiInstance.protocolSnmpv3ViewAdd(agentNum, viewName, viewType, subtree, mask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3ViewAdd");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 view | |
| **viewName** | **String**| SNMPv3 view name | |
| **viewType** | **String**| SNMPv3 view type | |
| **subtree** | **String**| SNMPv3 view subtree | |
| **mask** | **String**| SNMPv3 view mask | |

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

<a id="protocolSnmpv3ViewClear"></a>
# **protocolSnmpv3ViewClear**
> String protocolSnmpv3ViewClear(agentNum)

Clears all view entries.

Clears all view entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 view
    try {
      String result = apiInstance.protocolSnmpv3ViewClear(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3ViewClear");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 view | |

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

<a id="protocolSnmpv3ViewDel"></a>
# **protocolSnmpv3ViewDel**
> String protocolSnmpv3ViewDel(agentNum, viewName)

Deletes the specified view entry.

Deletes the specified view entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the SNMPv3 view
    String viewName = "viewName_example"; // String | SNMPv3 view name
    try {
      String result = apiInstance.protocolSnmpv3ViewDel(agentNum, viewName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3ViewDel");
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
| **agentNum** | **Integer**| Agent to add the SNMPv3 view | |
| **viewName** | **String**| SNMPv3 view name | |

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

<a id="protocolSnmpv3ViewList"></a>
# **protocolSnmpv3ViewList**
> List&lt;String&gt; protocolSnmpv3ViewList(agentNum)

Returns the current view entries as an array of strings.

Returns the current view entries as an array of strings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Snmpv3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    Snmpv3Api apiInstance = new Snmpv3Api(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPv3 configuration
    try {
      List<String> result = apiInstance.protocolSnmpv3ViewList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Snmpv3Api#protocolSnmpv3ViewList");
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
| **agentNum** | **Integer**| Agent to show the SNMPv3 configuration | |

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

