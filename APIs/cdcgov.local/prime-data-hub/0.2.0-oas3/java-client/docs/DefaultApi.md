# DefaultApi

All URIs are relative to *http://cdcgov.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsPost**](DefaultApi.md#reportsPost) | **POST** /reports | Post a report to the data hub |
| [**settingsOrganizationsGet**](DefaultApi.md#settingsOrganizationsGet) | **GET** /settings/organizations |  |
| [**settingsOrganizationsHead**](DefaultApi.md#settingsOrganizationsHead) | **HEAD** /settings/organizations |  |
| [**settingsOrganizationsOrganizationNameDelete**](DefaultApi.md#settingsOrganizationsOrganizationNameDelete) | **DELETE** /settings/organizations/{organizationName} |  |
| [**settingsOrganizationsOrganizationNameGet**](DefaultApi.md#settingsOrganizationsOrganizationNameGet) | **GET** /settings/organizations/{organizationName} |  |
| [**settingsOrganizationsOrganizationNamePut**](DefaultApi.md#settingsOrganizationsOrganizationNamePut) | **PUT** /settings/organizations/{organizationName} |  |
| [**settingsOrganizationsOrganizationNameReceiversGet**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversGet) | **GET** /settings/organizations/{organizationName}/receivers |  |
| [**settingsOrganizationsOrganizationNameReceiversReceiverNameDelete**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversReceiverNameDelete) | **DELETE** /settings/organizations/{organizationName}/receivers/{receiverName} |  |
| [**settingsOrganizationsOrganizationNameReceiversReceiverNameGet**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversReceiverNameGet) | **GET** /settings/organizations/{organizationName}/receivers/{receiverName} |  |
| [**settingsOrganizationsOrganizationNameReceiversReceiverNamePut**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversReceiverNamePut) | **PUT** /settings/organizations/{organizationName}/receivers/{receiverName} |  |
| [**settingsOrganizationsOrganizationNameSendersGet**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersGet) | **GET** /settings/organizations/{organizationName}/senders |  |
| [**settingsOrganizationsOrganizationNameSendersSenderNameDelete**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersSenderNameDelete) | **DELETE** /settings/organizations/{organizationName}/senders/{senderName} |  |
| [**settingsOrganizationsOrganizationNameSendersSenderNameGet**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersSenderNameGet) | **GET** /settings/organizations/{organizationName}/senders/{senderName} |  |
| [**settingsOrganizationsOrganizationNameSendersSenderNamePut**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersSenderNamePut) | **PUT** /settings/organizations/{organizationName}/senders/{senderName} |  |


<a id="reportsPost"></a>
# **reportsPost**
> Report reportsPost(client, body, option, _default, routeTo)

Post a report to the data hub

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String client = "simple_report"; // String | The client's name that matches the client name in metadata
    String body = header1, header2
value1, value2; // String | The public health information being routed
    String option = "ValidatePayload"; // String | Optional ways to process the request
    List<String> _default = Arrays.asList(); // List<String> | Dynamic default values for an element. ':' or %3A is used to seperate element name and value
    List<String> routeTo = Arrays.asList(); // List<String> | A comma speparated list of receiver names. Limit the list of possible receivers to these receivers.
    try {
      Report result = apiInstance.reportsPost(client, body, option, _default, routeTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reportsPost");
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
| **client** | **String**| The client&#39;s name that matches the client name in metadata | |
| **body** | **String**| The public health information being routed | |
| **option** | **String**| Optional ways to process the request | [optional] [enum: ValidatePayload, CheckConnections, SendImmediately, SkipSend, SkipInvalidItems] |
| **_default** | [**List&lt;String&gt;**](String.md)| Dynamic default values for an element. &#39;:&#39; or %3A is used to seperate element name and value | [optional] |
| **routeTo** | [**List&lt;String&gt;**](String.md)| A comma speparated list of receiver names. Limit the list of possible receivers to these receivers. | [optional] |

### Return type

[**Report**](Report.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created. A report was created, but items may have been rejected. |  -  |
| **400** | Invalid request. No report created. |  -  |
| **500** | Internal Server Error |  -  |

<a id="settingsOrganizationsGet"></a>
# **settingsOrganizationsGet**
> List&lt;Organization&gt; settingsOrganizationsGet()



The settings for all organizations of the system. Must have admin access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<Organization> result = apiInstance.settingsOrganizationsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsGet");
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

[**List&lt;Organization&gt;**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Last-Modified - The Last-Modified response HTTP header contains the date and time any setting was modified. <br>  |

<a id="settingsOrganizationsHead"></a>
# **settingsOrganizationsHead**
> settingsOrganizationsHead()



Retrived the last modified for all settings of the system. Must have admin access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.settingsOrganizationsHead();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsHead");
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Last-Modified - The Last-Modified response HTTP header contains the date and time any setting was modified. <br>  |

<a id="settingsOrganizationsOrganizationNameDelete"></a>
# **settingsOrganizationsOrganizationNameDelete**
> Organization settingsOrganizationsOrganizationNameDelete(organizationName)



Delete an organization (and the associated receivers and senders)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "organizationName_example"; // String | The name of the organization
    try {
      Organization result = apiInstance.settingsOrganizationsOrganizationNameDelete(organizationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameDelete");
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
| **organizationName** | **String**| The name of the organization | |

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, the organization setting was deleted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameGet"></a>
# **settingsOrganizationsOrganizationNameGet**
> Organization settingsOrganizationsOrganizationNameGet(organizationName)



A single organization settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "organizationName_example"; // String | The name of the organization
    try {
      Organization result = apiInstance.settingsOrganizationsOrganizationNameGet(organizationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameGet");
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
| **organizationName** | **String**| The name of the organization | |

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="settingsOrganizationsOrganizationNamePut"></a>
# **settingsOrganizationsOrganizationNamePut**
> Organization settingsOrganizationsOrganizationNamePut(organizationName, organization)



Create or update the direct settings associated with an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "organizationName_example"; // String | The name of the organization
    Organization organization = new Organization(); // Organization | 
    try {
      Organization result = apiInstance.settingsOrganizationsOrganizationNamePut(organizationName, organization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNamePut");
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
| **organizationName** | **String**| The name of the organization | |
| **organization** | [**Organization**](Organization.md)|  | [optional] |

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, the organization setting was updated |  -  |
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameReceiversGet"></a>
# **settingsOrganizationsOrganizationNameReceiversGet**
> List&lt;Receiver&gt; settingsOrganizationsOrganizationNameReceiversGet(organizationName)



A list of receivers and their current settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | Fetch receivers with this organization name
    try {
      List<Receiver> result = apiInstance.settingsOrganizationsOrganizationNameReceiversGet(organizationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameReceiversGet");
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
| **organizationName** | **String**| Fetch receivers with this organization name | |

### Return type

[**List&lt;Receiver&gt;**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameReceiversReceiverNameDelete"></a>
# **settingsOrganizationsOrganizationNameReceiversReceiverNameDelete**
> Receiver settingsOrganizationsOrganizationNameReceiversReceiverNameDelete(organizationName, receiverName)



Delete a receiver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | the organization name
    String receiverName = "elr"; // String | The name of the receiver
    try {
      Receiver result = apiInstance.settingsOrganizationsOrganizationNameReceiversReceiverNameDelete(organizationName, receiverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameReceiversReceiverNameDelete");
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
| **organizationName** | **String**| the organization name | |
| **receiverName** | **String**| The name of the receiver | |

### Return type

[**Receiver**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, the receiver was deleted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameReceiversReceiverNameGet"></a>
# **settingsOrganizationsOrganizationNameReceiversReceiverNameGet**
> Receiver settingsOrganizationsOrganizationNameReceiversReceiverNameGet(organizationName, receiverName)



The settings of a single of receiver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | Create receivers under this organization name
    String receiverName = "elr"; // String | The name of the receiver
    try {
      Receiver result = apiInstance.settingsOrganizationsOrganizationNameReceiversReceiverNameGet(organizationName, receiverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameReceiversReceiverNameGet");
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
| **organizationName** | **String**| Create receivers under this organization name | |
| **receiverName** | **String**| The name of the receiver | |

### Return type

[**Receiver**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameReceiversReceiverNamePut"></a>
# **settingsOrganizationsOrganizationNameReceiversReceiverNamePut**
> Receiver settingsOrganizationsOrganizationNameReceiversReceiverNamePut(organizationName, receiverName, receiver)



Update a single reciever

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | Create receivers under this organization name
    String receiverName = "elr"; // String | The name of the receiver
    Receiver receiver = new Receiver(); // Receiver | 
    try {
      Receiver result = apiInstance.settingsOrganizationsOrganizationNameReceiversReceiverNamePut(organizationName, receiverName, receiver);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameReceiversReceiverNamePut");
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
| **organizationName** | **String**| Create receivers under this organization name | |
| **receiverName** | **String**| The name of the receiver | |
| **receiver** | [**Receiver**](Receiver.md)|  | [optional] |

### Return type

[**Receiver**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, the receiver setting was updated |  -  |
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameSendersGet"></a>
# **settingsOrganizationsOrganizationNameSendersGet**
> List&lt;Sender&gt; settingsOrganizationsOrganizationNameSendersGet(organizationName)



A list of senders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | Fetch senders with this organization name
    try {
      List<Sender> result = apiInstance.settingsOrganizationsOrganizationNameSendersGet(organizationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameSendersGet");
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
| **organizationName** | **String**| Fetch senders with this organization name | |

### Return type

[**List&lt;Sender&gt;**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameSendersSenderNameDelete"></a>
# **settingsOrganizationsOrganizationNameSendersSenderNameDelete**
> Sender settingsOrganizationsOrganizationNameSendersSenderNameDelete(organizationName, senderName)



Delete a sender

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | the organization name
    String senderName = "default"; // String | The name of a sender to the data hub
    try {
      Sender result = apiInstance.settingsOrganizationsOrganizationNameSendersSenderNameDelete(organizationName, senderName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameSendersSenderNameDelete");
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
| **organizationName** | **String**| the organization name | |
| **senderName** | **String**| The name of a sender to the data hub | |

### Return type

[**Sender**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, the sender was deleted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameSendersSenderNameGet"></a>
# **settingsOrganizationsOrganizationNameSendersSenderNameGet**
> Sender settingsOrganizationsOrganizationNameSendersSenderNameGet(organizationName, senderName)



The settings of a single of sender

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | Fetch senders with this organization name
    String senderName = "default"; // String | The name of a sender to the data hub
    try {
      Sender result = apiInstance.settingsOrganizationsOrganizationNameSendersSenderNameGet(organizationName, senderName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameSendersSenderNameGet");
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
| **organizationName** | **String**| Fetch senders with this organization name | |
| **senderName** | **String**| The name of a sender to the data hub | |

### Return type

[**Sender**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="settingsOrganizationsOrganizationNameSendersSenderNamePut"></a>
# **settingsOrganizationsOrganizationNameSendersSenderNamePut**
> List&lt;Sender&gt; settingsOrganizationsOrganizationNameSendersSenderNamePut(organizationName, senderName, sender)



Update a single sender

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cdcgov.local");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String organizationName = "az-phd"; // String | Fetch senders with this organization name
    String senderName = "default"; // String | The name of a sender to the data hub
    Sender sender = new Sender(); // Sender | 
    try {
      List<Sender> result = apiInstance.settingsOrganizationsOrganizationNameSendersSenderNamePut(organizationName, senderName, sender);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsOrganizationsOrganizationNameSendersSenderNamePut");
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
| **organizationName** | **String**| Fetch senders with this organization name | |
| **senderName** | **String**| The name of a sender to the data hub | |
| **sender** | [**Sender**](Sender.md)|  | [optional] |

### Return type

[**List&lt;Sender&gt;**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

