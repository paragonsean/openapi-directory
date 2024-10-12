# MqttBrokersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkMqttBroker_1**](MqttBrokersApi.md#createNetworkMqttBroker_1) | **POST** /networks/{networkId}/mqttBrokers | Add an MQTT broker |
| [**deleteNetworkMqttBroker_1**](MqttBrokersApi.md#deleteNetworkMqttBroker_1) | **DELETE** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Delete an MQTT broker |
| [**getNetworkMqttBroker_1**](MqttBrokersApi.md#getNetworkMqttBroker_1) | **GET** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Return an MQTT broker |
| [**getNetworkMqttBrokers_1**](MqttBrokersApi.md#getNetworkMqttBrokers_1) | **GET** /networks/{networkId}/mqttBrokers | List the MQTT brokers for this network |
| [**updateNetworkMqttBroker_1**](MqttBrokersApi.md#updateNetworkMqttBroker_1) | **PUT** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Update an MQTT broker |


<a id="createNetworkMqttBroker_1"></a>
# **createNetworkMqttBroker_1**
> Object createNetworkMqttBroker_1(networkId, createNetworkMqttBrokerRequest)

Add an MQTT broker

Add an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttBrokersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MqttBrokersApi apiInstance = new MqttBrokersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkMqttBrokerRequest createNetworkMqttBrokerRequest = new CreateNetworkMqttBrokerRequest(); // CreateNetworkMqttBrokerRequest | 
    try {
      Object result = apiInstance.createNetworkMqttBroker_1(networkId, createNetworkMqttBrokerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttBrokersApi#createNetworkMqttBroker_1");
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
| **networkId** | **String**|  | |
| **createNetworkMqttBrokerRequest** | [**CreateNetworkMqttBrokerRequest**](CreateNetworkMqttBrokerRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkMqttBroker_1"></a>
# **deleteNetworkMqttBroker_1**
> deleteNetworkMqttBroker_1(networkId, mqttBrokerId)

Delete an MQTT broker

Delete an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttBrokersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MqttBrokersApi apiInstance = new MqttBrokersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String mqttBrokerId = "mqttBrokerId_example"; // String | 
    try {
      apiInstance.deleteNetworkMqttBroker_1(networkId, mqttBrokerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttBrokersApi#deleteNetworkMqttBroker_1");
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
| **networkId** | **String**|  | |
| **mqttBrokerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkMqttBroker_1"></a>
# **getNetworkMqttBroker_1**
> Object getNetworkMqttBroker_1(networkId, mqttBrokerId)

Return an MQTT broker

Return an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttBrokersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MqttBrokersApi apiInstance = new MqttBrokersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String mqttBrokerId = "mqttBrokerId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkMqttBroker_1(networkId, mqttBrokerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttBrokersApi#getNetworkMqttBroker_1");
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
| **networkId** | **String**|  | |
| **mqttBrokerId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkMqttBrokers_1"></a>
# **getNetworkMqttBrokers_1**
> List&lt;Object&gt; getNetworkMqttBrokers_1(networkId)

List the MQTT brokers for this network

List the MQTT brokers for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttBrokersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MqttBrokersApi apiInstance = new MqttBrokersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkMqttBrokers_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttBrokersApi#getNetworkMqttBrokers_1");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkMqttBroker_1"></a>
# **updateNetworkMqttBroker_1**
> Object updateNetworkMqttBroker_1(networkId, mqttBrokerId, updateNetworkMqttBrokerRequest)

Update an MQTT broker

Update an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MqttBrokersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MqttBrokersApi apiInstance = new MqttBrokersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String mqttBrokerId = "mqttBrokerId_example"; // String | 
    UpdateNetworkMqttBrokerRequest updateNetworkMqttBrokerRequest = new UpdateNetworkMqttBrokerRequest(); // UpdateNetworkMqttBrokerRequest | 
    try {
      Object result = apiInstance.updateNetworkMqttBroker_1(networkId, mqttBrokerId, updateNetworkMqttBrokerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MqttBrokersApi#updateNetworkMqttBroker_1");
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
| **networkId** | **String**|  | |
| **mqttBrokerId** | **String**|  | |
| **updateNetworkMqttBrokerRequest** | [**UpdateNetworkMqttBrokerRequest**](UpdateNetworkMqttBrokerRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

