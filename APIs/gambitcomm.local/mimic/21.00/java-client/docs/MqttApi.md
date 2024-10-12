# MqttApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolMqttClientGetProtstate**](MqttApi.md#protocolMqttClientGetProtstate) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/get/protstate | Show the agent&#39;s MQTT TCP connection state |
| [**protocolMqttClientGetState**](MqttApi.md#protocolMqttClientGetState) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/get/state | Show the agent&#39;s MQTT state |
| [**protocolMqttClientMessageCard**](MqttApi.md#protocolMqttClientMessageCard) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/message/card | Show the agent&#39;s current messages&#39; cardinality |
| [**protocolMqttClientMessageGet**](MqttApi.md#protocolMqttClientMessageGet) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/message/get/{msgNum}/{attr} | Show the agent&#39;s message attributes |
| [**protocolMqttClientMessageSet**](MqttApi.md#protocolMqttClientMessageSet) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/message/set/{msgNum}/{attr}/{value} | Set the agent&#39;s message attributes |
| [**protocolMqttClientResubscribe**](MqttApi.md#protocolMqttClientResubscribe) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/resubscribe/{subNum} | Restart receiving messages from a subcription of the agent |
| [**protocolMqttClientRuntimeAbort**](MqttApi.md#protocolMqttClientRuntimeAbort) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/runtime/abort | Abort agent&#39;s MQTT TCP session without sending DISCONNECT command |
| [**protocolMqttClientRuntimeConnect**](MqttApi.md#protocolMqttClientRuntimeConnect) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/runtime/connect | Start agent&#39;s MQTT TCP session |
| [**protocolMqttClientRuntimeDisconnect**](MqttApi.md#protocolMqttClientRuntimeDisconnect) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/runtime/disconnect | Disconnect agent&#39;s MQTT TCP session by sending DISCONNECT command |
| [**protocolMqttClientSetBroker**](MqttApi.md#protocolMqttClientSetBroker) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/broker/{brokerAddr} | Set the agent&#39;s MQTT TCP connection target broker |
| [**protocolMqttClientSetCleansession**](MqttApi.md#protocolMqttClientSetCleansession) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/cleansession/{cleanOrNot} | Set the agent&#39;s MQTT session |
| [**protocolMqttClientSetClientid**](MqttApi.md#protocolMqttClientSetClientid) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/clientid/{clientID} | Set the agent&#39;s MQTT client ID |
| [**protocolMqttClientSetKeepalive**](MqttApi.md#protocolMqttClientSetKeepalive) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/keepalive/{aliveTime} | Set the agent&#39;s MQTT TCP keepalive |
| [**protocolMqttClientSetOnDisconnect**](MqttApi.md#protocolMqttClientSetOnDisconnect) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/on_disconnect/{action} | Set the agent&#39;s MQTT disconnection action |
| [**protocolMqttClientSetPassword**](MqttApi.md#protocolMqttClientSetPassword) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/password/{password} | Set the agent&#39;s MQTT client password |
| [**protocolMqttClientSetPort**](MqttApi.md#protocolMqttClientSetPort) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/port/{port} | Set the agent&#39;s MQTT TCP connection target port |
| [**protocolMqttClientSetUsername**](MqttApi.md#protocolMqttClientSetUsername) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/username/{username} | Set the agent&#39;s MQTT client username |
| [**protocolMqttClientSetWillmsg**](MqttApi.md#protocolMqttClientSetWillmsg) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willmsg/{msg} | Set the agent&#39;s MQTT client&#39;s will |
| [**protocolMqttClientSetWillqos**](MqttApi.md#protocolMqttClientSetWillqos) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willqos/{qos} | Set the agent&#39;s MQTT will message&#39;s QOS field |
| [**protocolMqttClientSetWillretain**](MqttApi.md#protocolMqttClientSetWillretain) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willretain/{retain} | Set the agent&#39;s MQTT retained will |
| [**protocolMqttClientSetWilltopic**](MqttApi.md#protocolMqttClientSetWilltopic) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willtopic/{topic} | Set the agent&#39;s MQTT client will&#39;s topic |
| [**protocolMqttClientSubscribeCard**](MqttApi.md#protocolMqttClientSubscribeCard) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/subscribe/card | Show the agent&#39;s current subscriptions&#39; cardinality |
| [**protocolMqttClientSubscribeGet**](MqttApi.md#protocolMqttClientSubscribeGet) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/subscribe/get/{subNum}/{attr} | Show the agent&#39;s subscription attributes |
| [**protocolMqttClientSubscribeSet**](MqttApi.md#protocolMqttClientSubscribeSet) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/subscribe/set/{subNum}/{attr}/{value} | Set the agent&#39;s subscribe attributes |
| [**protocolMqttClientUnsubscribe**](MqttApi.md#protocolMqttClientUnsubscribe) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/unsubscribe/{subNum} | Stops receiving messages from a subcription of the agent |
| [**protocolMqttGetArgs**](MqttApi.md#protocolMqttGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/args | Show the agent&#39;s MQTT argument structure |
| [**protocolMqttGetConfig**](MqttApi.md#protocolMqttGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/config | Show the agent&#39;s MQTT configuration |
| [**protocolMqttGetStatistics**](MqttApi.md#protocolMqttGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/statistics | Show the agent&#39;s MQTT statistics |
| [**protocolMqttGetStatsHdr**](MqttApi.md#protocolMqttGetStatsHdr) | **GET** /mimic/protocol/msg/mqtt/get/stats_hdr | Show the MQTT statistics headers |
| [**protocolMqttGetTrace**](MqttApi.md#protocolMqttGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/trace | Show the agent&#39;s MQTT traffic tracing |
| [**protocolMqttSetConfig**](MqttApi.md#protocolMqttSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/set/config/{argument}/{value} | Set the agent&#39;s MQTT configuration |
| [**protocolMqttSetTrace**](MqttApi.md#protocolMqttSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/set/trace/{enableOrNot} | Set the agent&#39;s MQTT traffic tracing |


<a id="protocolMqttClientGetProtstate"></a>
# **protocolMqttClientGetProtstate**
> List&lt;Integer&gt; protocolMqttClientGetProtstate(agentNum)

Show the agent&#39;s MQTT TCP connection state

0 - stopped, 2 - disconnected, 3 - connecting, 4 - connected, 5 - waiting for CONNACK, 6 - waiting for SUBACK, 7 - CONNACK received, in steady state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT state
    try {
      List<Integer> result = apiInstance.protocolMqttClientGetProtstate(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientGetProtstate");
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
| **agentNum** | **Integer**| Agent to show MQTT state | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientGetState"></a>
# **protocolMqttClientGetState**
> List&lt;Integer&gt; protocolMqttClientGetState(agentNum)

Show the agent&#39;s MQTT state

0 means stopped, 1 means running

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT state
    try {
      List<Integer> result = apiInstance.protocolMqttClientGetState(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientGetState");
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
| **agentNum** | **Integer**| Agent to show MQTT state | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientMessageCard"></a>
# **protocolMqttClientMessageCard**
> List&lt;Integer&gt; protocolMqttClientMessageCard(agentNum)

Show the agent&#39;s current messages&#39; cardinality

0 or more

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT message state
    try {
      List<Integer> result = apiInstance.protocolMqttClientMessageCard(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientMessageCard");
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
| **agentNum** | **Integer**| Agent to show MQTT message state | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientMessageGet"></a>
# **protocolMqttClientMessageGet**
> List&lt;String&gt; protocolMqttClientMessageGet(agentNum, msgNum, attr)

Show the agent&#39;s message attributes

Attribute can be topic, interval, count, sent , pre, post, properties(list of PUBLISH properties), properties.i (i-th PUBLISH property), properties.PROP-NAME (PUBLISH property with name PROP-NAME)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT state
    Integer msgNum = 56; // Integer | Message Number
    String attr = "attr_example"; // String | Attribute
    try {
      List<String> result = apiInstance.protocolMqttClientMessageGet(agentNum, msgNum, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientMessageGet");
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
| **agentNum** | **Integer**| Agent to show MQTT state | |
| **msgNum** | **Integer**| Message Number | |
| **attr** | **String**| Attribute | |

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

<a id="protocolMqttClientMessageSet"></a>
# **protocolMqttClientMessageSet**
> List&lt;String&gt; protocolMqttClientMessageSet(agentNum, msgNum, attr, value)

Set the agent&#39;s message attributes

Attribute can not be sent or properties . Use set/{msgNum}/count/{value} together with get/{msgNum}/count to throttle the outgoing MQTT message to the broker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT state
    Integer msgNum = 56; // Integer | Message Number
    String attr = "attr_example"; // String | Attribute
    String value = "value_example"; // String | Value
    try {
      List<String> result = apiInstance.protocolMqttClientMessageSet(agentNum, msgNum, attr, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientMessageSet");
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
| **agentNum** | **Integer**| Agent to show MQTT state | |
| **msgNum** | **Integer**| Message Number | |
| **attr** | **String**| Attribute | |
| **value** | **String**| Value | |

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

<a id="protocolMqttClientResubscribe"></a>
# **protocolMqttClientResubscribe**
> String protocolMqttClientResubscribe(agentNum, subNum)

Restart receiving messages from a subcription of the agent

Restarts a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to change MQTT state
    Integer subNum = 56; // Integer | Subscription Number
    try {
      String result = apiInstance.protocolMqttClientResubscribe(agentNum, subNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientResubscribe");
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
| **agentNum** | **Integer**| Agent to change MQTT state | |
| **subNum** | **Integer**| Subscription Number | |

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

<a id="protocolMqttClientRuntimeAbort"></a>
# **protocolMqttClientRuntimeAbort**
> List&lt;String&gt; protocolMqttClientRuntimeAbort(agentNum)

Abort agent&#39;s MQTT TCP session without sending DISCONNECT command

Abort a connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT behavior
    try {
      List<String> result = apiInstance.protocolMqttClientRuntimeAbort(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientRuntimeAbort");
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
| **agentNum** | **Integer**| Agent to set MQTT behavior | |

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

<a id="protocolMqttClientRuntimeConnect"></a>
# **protocolMqttClientRuntimeConnect**
> List&lt;String&gt; protocolMqttClientRuntimeConnect(agentNum)

Start agent&#39;s MQTT TCP session

Start a connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT behavior
    try {
      List<String> result = apiInstance.protocolMqttClientRuntimeConnect(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientRuntimeConnect");
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
| **agentNum** | **Integer**| Agent to set MQTT behavior | |

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

<a id="protocolMqttClientRuntimeDisconnect"></a>
# **protocolMqttClientRuntimeDisconnect**
> List&lt;String&gt; protocolMqttClientRuntimeDisconnect(agentNum)

Disconnect agent&#39;s MQTT TCP session by sending DISCONNECT command

Graceful disconnect

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT behavior
    try {
      List<String> result = apiInstance.protocolMqttClientRuntimeDisconnect(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientRuntimeDisconnect");
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
| **agentNum** | **Integer**| Agent to set MQTT behavior | |

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

<a id="protocolMqttClientSetBroker"></a>
# **protocolMqttClientSetBroker**
> List&lt;Integer&gt; protocolMqttClientSetBroker(agentNum, brokerAddr)

Set the agent&#39;s MQTT TCP connection target broker

Broker IP address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String brokerAddr = "brokerAddr_example"; // String | Broker address
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetBroker(agentNum, brokerAddr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetBroker");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **brokerAddr** | **String**| Broker address | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetCleansession"></a>
# **protocolMqttClientSetCleansession**
> List&lt;Integer&gt; protocolMqttClientSetCleansession(agentNum, cleanOrNot)

Set the agent&#39;s MQTT session

1 for clean session , 0 not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    Integer cleanOrNot = 56; // Integer | Clean session
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetCleansession(agentNum, cleanOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetCleansession");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **cleanOrNot** | **Integer**| Clean session | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetClientid"></a>
# **protocolMqttClientSetClientid**
> List&lt;Integer&gt; protocolMqttClientSetClientid(agentNum, clientID)

Set the agent&#39;s MQTT client ID

MQTT client ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String clientID = "clientID_example"; // String | Client ID
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetClientid(agentNum, clientID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetClientid");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **clientID** | **String**| Client ID | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetKeepalive"></a>
# **protocolMqttClientSetKeepalive**
> List&lt;Integer&gt; protocolMqttClientSetKeepalive(agentNum, aliveTime)

Set the agent&#39;s MQTT TCP keepalive

Keep alive the TCP connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    Integer aliveTime = 56; // Integer | period to send keepalive messages
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetKeepalive(agentNum, aliveTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetKeepalive");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **aliveTime** | **Integer**| period to send keepalive messages | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetOnDisconnect"></a>
# **protocolMqttClientSetOnDisconnect**
> List&lt;Integer&gt; protocolMqttClientSetOnDisconnect(agentNum, action)

Set the agent&#39;s MQTT disconnection action

Action to take when MQTT session is disconnected

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String action = "action_example"; // String | Action to take
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetOnDisconnect(agentNum, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetOnDisconnect");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **action** | **String**| Action to take | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetPassword"></a>
# **protocolMqttClientSetPassword**
> List&lt;Integer&gt; protocolMqttClientSetPassword(agentNum, password)

Set the agent&#39;s MQTT client password

Client password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String password = "password_example"; // String | Password
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetPassword(agentNum, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetPassword");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **password** | **String**| Password | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetPort"></a>
# **protocolMqttClientSetPort**
> List&lt;Integer&gt; protocolMqttClientSetPort(agentNum, port)

Set the agent&#39;s MQTT TCP connection target port

target TCP port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String port = "port_example"; // String | TCP port
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetPort(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetPort");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **port** | **String**| TCP port | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetUsername"></a>
# **protocolMqttClientSetUsername**
> List&lt;Integer&gt; protocolMqttClientSetUsername(agentNum, username)

Set the agent&#39;s MQTT client username

Client username

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String username = "username_example"; // String | User name
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetUsername(agentNum, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetUsername");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **username** | **String**| User name | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetWillmsg"></a>
# **protocolMqttClientSetWillmsg**
> List&lt;Integer&gt; protocolMqttClientSetWillmsg(agentNum, msg)

Set the agent&#39;s MQTT client&#39;s will

Will message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String msg = "msg_example"; // String | Will message
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetWillmsg(agentNum, msg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetWillmsg");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **msg** | **String**| Will message | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetWillqos"></a>
# **protocolMqttClientSetWillqos**
> List&lt;Integer&gt; protocolMqttClientSetWillqos(agentNum, qos)

Set the agent&#39;s MQTT will message&#39;s QOS field

QOS field

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String qos = "qos_example"; // String | Quality of service field
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetWillqos(agentNum, qos);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetWillqos");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **qos** | **String**| Quality of service field | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetWillretain"></a>
# **protocolMqttClientSetWillretain**
> List&lt;Integer&gt; protocolMqttClientSetWillretain(agentNum, retain)

Set the agent&#39;s MQTT retained will

Retaining will

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String retain = "retain_example"; // String | Retaining will
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetWillretain(agentNum, retain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetWillretain");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **retain** | **String**| Retaining will | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSetWilltopic"></a>
# **protocolMqttClientSetWilltopic**
> List&lt;Integer&gt; protocolMqttClientSetWilltopic(agentNum, topic)

Set the agent&#39;s MQTT client will&#39;s topic

Will topic for the will message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set MQTT config
    String topic = "topic_example"; // String | topic
    try {
      List<Integer> result = apiInstance.protocolMqttClientSetWilltopic(agentNum, topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSetWilltopic");
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
| **agentNum** | **Integer**| Agent to set MQTT config | |
| **topic** | **String**| topic | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSubscribeCard"></a>
# **protocolMqttClientSubscribeCard**
> List&lt;Integer&gt; protocolMqttClientSubscribeCard(agentNum)

Show the agent&#39;s current subscriptions&#39; cardinality

0 or more

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT subscription state
    try {
      List<Integer> result = apiInstance.protocolMqttClientSubscribeCard(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSubscribeCard");
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
| **agentNum** | **Integer**| Agent to show MQTT subscription state | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttClientSubscribeGet"></a>
# **protocolMqttClientSubscribeGet**
> List&lt;String&gt; protocolMqttClientSubscribeGet(agentNum, subNum, attr)

Show the agent&#39;s subscription attributes

Attribute can be topic, properties(list of SUBSCRIBE properties), properties.i (i-th SUBSCRIBE property), properties.PROP-NAME (SUBSCRIBE property with name PROP-NAME)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT state
    Integer subNum = 56; // Integer | Subscribe Number
    String attr = "attr_example"; // String | Attribute
    try {
      List<String> result = apiInstance.protocolMqttClientSubscribeGet(agentNum, subNum, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSubscribeGet");
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
| **agentNum** | **Integer**| Agent to show MQTT state | |
| **subNum** | **Integer**| Subscribe Number | |
| **attr** | **String**| Attribute | |

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

<a id="protocolMqttClientSubscribeSet"></a>
# **protocolMqttClientSubscribeSet**
> List&lt;String&gt; protocolMqttClientSubscribeSet(agentNum, subNum, attr, value)

Set the agent&#39;s subscribe attributes

Attribute can not be properties .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT state
    Integer subNum = 56; // Integer | Subscribe Number
    String attr = "attr_example"; // String | Attribute
    String value = "value_example"; // String | Value
    try {
      List<String> result = apiInstance.protocolMqttClientSubscribeSet(agentNum, subNum, attr, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientSubscribeSet");
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
| **agentNum** | **Integer**| Agent to show MQTT state | |
| **subNum** | **Integer**| Subscribe Number | |
| **attr** | **String**| Attribute | |
| **value** | **String**| Value | |

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

<a id="protocolMqttClientUnsubscribe"></a>
# **protocolMqttClientUnsubscribe**
> String protocolMqttClientUnsubscribe(agentNum, subNum)

Stops receiving messages from a subcription of the agent

Stops a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to change MQTT state
    Integer subNum = 56; // Integer | Subscription Number
    try {
      String result = apiInstance.protocolMqttClientUnsubscribe(agentNum, subNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttClientUnsubscribe");
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
| **agentNum** | **Integer**| Agent to change MQTT state | |
| **subNum** | **Integer**| Subscription Number | |

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

<a id="protocolMqttGetArgs"></a>
# **protocolMqttGetArgs**
> Object protocolMqttGetArgs(agentNum)

Show the agent&#39;s MQTT argument structure

Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the MQTT argument structure
    try {
      Object result = apiInstance.protocolMqttGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttGetArgs");
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
| **agentNum** | **Integer**| Agent to show the MQTT argument structure | |

### Return type

**Object**

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

<a id="protocolMqttGetConfig"></a>
# **protocolMqttGetConfig**
> ConfigMQTT protocolMqttGetConfig(agentNum)

Show the agent&#39;s MQTT configuration

Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the MQTT configuration
    try {
      ConfigMQTT result = apiInstance.protocolMqttGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttGetConfig");
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
| **agentNum** | **Integer**| Agent to show the MQTT configuration | |

### Return type

[**ConfigMQTT**](ConfigMQTT.md)

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

<a id="protocolMqttGetStatistics"></a>
# **protocolMqttGetStatistics**
> List&lt;Integer&gt; protocolMqttGetStatistics(agentNum)

Show the agent&#39;s MQTT statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show MQTT statistics
    try {
      List<Integer> result = apiInstance.protocolMqttGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttGetStatistics");
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
| **agentNum** | **Integer**| Agent to show MQTT statistics | |

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
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttGetStatsHdr"></a>
# **protocolMqttGetStatsHdr**
> List&lt;String&gt; protocolMqttGetStatsHdr()

Show the MQTT statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolMqttGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttGetStatsHdr");
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolMqttGetTrace"></a>
# **protocolMqttGetTrace**
> ConfigMQTT protocolMqttGetTrace(agentNum)

Show the agent&#39;s MQTT traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether MQTT tracing is enabled
    try {
      ConfigMQTT result = apiInstance.protocolMqttGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether MQTT tracing is enabled | |

### Return type

[**ConfigMQTT**](ConfigMQTT.md)

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

<a id="protocolMqttSetConfig"></a>
# **protocolMqttSetConfig**
> String protocolMqttSetConfig(agentNum, argument, value)

Set the agent&#39;s MQTT configuration

Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the MQTT configuration
    String argument = "argument_example"; // String | Parameter to set the MQTT configuration
    String value = "value_example"; // String | Value to set the MQTT configuration
    try {
      String result = apiInstance.protocolMqttSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttSetConfig");
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
| **agentNum** | **Integer**| Agent to set the MQTT configuration | |
| **argument** | **String**| Parameter to set the MQTT configuration | |
| **value** | **String**| Value to set the MQTT configuration | |

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

<a id="protocolMqttSetTrace"></a>
# **protocolMqttSetTrace**
> String protocolMqttSetTrace(agentNum, enableOrNot)

Set the agent&#39;s MQTT traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MqttApi apiInstance = new MqttApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the MQTT tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the MQTT tracing
    try {
      String result = apiInstance.protocolMqttSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttApi#protocolMqttSetTrace");
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
| **agentNum** | **Integer**| Agent to set the MQTT tracing | |
| **enableOrNot** | **String**| Value to set the MQTT tracing | |

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

