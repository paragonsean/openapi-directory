# MailboxesApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeMailboxPassword**](MailboxesApi.md#changeMailboxPassword) | **PUT** /mailboxes/{mailboxName}/password | Change password for mailbox |
| [**configureMailboxAutoForward**](MailboxesApi.md#configureMailboxAutoForward) | **PUT** /mailboxes/{mailboxName}/autoforward | Configure auto-forward for mailbox |
| [**configureMailboxAutoReply**](MailboxesApi.md#configureMailboxAutoReply) | **PUT** /mailboxes/{mailboxName}/autoreply | Configure auto-reply for mailbox |
| [**createMailbox**](MailboxesApi.md#createMailbox) | **POST** /mailboxes | Create a new mailbox. |
| [**deleteMailbox**](MailboxesApi.md#deleteMailbox) | **DELETE** /mailboxes/{mailboxName} | Delete a mailbox |
| [**getMailbox**](MailboxesApi.md#getMailbox) | **GET** /mailboxes/{mailboxName} | Get a specific mailbox |
| [**getMailboxes**](MailboxesApi.md#getMailboxes) | **GET** /mailboxes | Gets your mailboxes. |


<a id="changeMailboxPassword"></a>
# **changeMailboxPassword**
> changeMailboxPassword(mailboxName, mailboxName2, updateMailboxPasswordRequest)

Change password for mailbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    String mailboxName = "mailboxName_example"; // String | Mailbox name.
    String mailboxName2 = "mailboxName_example"; // String | Automatically added
    UpdateMailboxPasswordRequest updateMailboxPasswordRequest = new UpdateMailboxPasswordRequest(); // UpdateMailboxPasswordRequest | Contains the new password.
    try {
      apiInstance.changeMailboxPassword(mailboxName, mailboxName2, updateMailboxPasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#changeMailboxPassword");
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
| **mailboxName** | **String**| Mailbox name. | |
| **mailboxName2** | **String**| Automatically added | |
| **updateMailboxPasswordRequest** | [**UpdateMailboxPasswordRequest**](UpdateMailboxPasswordRequest.md)| Contains the new password. | [optional] |

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
| **204** | Success |  -  |

<a id="configureMailboxAutoForward"></a>
# **configureMailboxAutoForward**
> configureMailboxAutoForward(mailboxName, mailboxName2, autoForward)

Configure auto-forward for mailbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    String mailboxName = "mailboxName_example"; // String | Mailbox name.
    String mailboxName2 = "mailboxName_example"; // String | Automatically added
    AutoForward autoForward = new AutoForward(); // AutoForward | Contains the auto-forward information.
    try {
      apiInstance.configureMailboxAutoForward(mailboxName, mailboxName2, autoForward);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#configureMailboxAutoForward");
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
| **mailboxName** | **String**| Mailbox name. | |
| **mailboxName2** | **String**| Automatically added | |
| **autoForward** | [**AutoForward**](AutoForward.md)| Contains the auto-forward information. | [optional] |

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
| **204** | Success |  -  |

<a id="configureMailboxAutoReply"></a>
# **configureMailboxAutoReply**
> configureMailboxAutoReply(mailboxName, mailboxName2, autoReply)

Configure auto-reply for mailbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    String mailboxName = "mailboxName_example"; // String | Mailbox name.
    String mailboxName2 = "mailboxName_example"; // String | Automatically added
    AutoReply autoReply = new AutoReply(); // AutoReply | Contains the auto-reply information.
    try {
      apiInstance.configureMailboxAutoReply(mailboxName, mailboxName2, autoReply);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#configureMailboxAutoReply");
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
| **mailboxName** | **String**| Mailbox name. | |
| **mailboxName2** | **String**| Automatically added | |
| **autoReply** | [**AutoReply**](AutoReply.md)| Contains the auto-reply information. | [optional] |

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
| **204** | Success |  -  |

<a id="createMailbox"></a>
# **createMailbox**
> createMailbox(createMailboxRequest)

Create a new mailbox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    CreateMailboxRequest createMailboxRequest = new CreateMailboxRequest(); // CreateMailboxRequest | The add mailbox request.
    try {
      apiInstance.createMailbox(createMailboxRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#createMailbox");
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
| **createMailboxRequest** | [**CreateMailboxRequest**](CreateMailboxRequest.md)| The add mailbox request. | [optional] |

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
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="deleteMailbox"></a>
# **deleteMailbox**
> deleteMailbox(mailboxName, mailboxName2)

Delete a mailbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    String mailboxName = "mailboxName_example"; // String | Mailbox name.
    String mailboxName2 = "mailboxName_example"; // String | Automatically added
    try {
      apiInstance.deleteMailbox(mailboxName, mailboxName2);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#deleteMailbox");
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
| **mailboxName** | **String**| Mailbox name. | |
| **mailboxName2** | **String**| Automatically added | |

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
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="getMailbox"></a>
# **getMailbox**
> MailboxDetail getMailbox(mailboxName, mailboxName2)

Get a specific mailbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    String mailboxName = "mailboxName_example"; // String | Mailbox name.
    String mailboxName2 = "mailboxName_example"; // String | Automatically added
    try {
      MailboxDetail result = apiInstance.getMailbox(mailboxName, mailboxName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#getMailbox");
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
| **mailboxName** | **String**| Mailbox name. | |
| **mailboxName2** | **String**| Automatically added | |

### Return type

[**MailboxDetail**](MailboxDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getMailboxes"></a>
# **getMailboxes**
> List&lt;Mailbox&gt; getMailboxes(domainName)

Gets your mailboxes.

Currently only supports getting the mailboxes filtered by domain name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailboxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailboxesApi apiInstance = new MailboxesApi(defaultClient);
    String domainName = "domainName_example"; // String | Obligated domain name for getting mailboxes.
    try {
      List<Mailbox> result = apiInstance.getMailboxes(domainName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailboxesApi#getMailboxes");
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
| **domainName** | **String**| Obligated domain name for getting mailboxes. | [optional] |

### Return type

[**List&lt;Mailbox&gt;**](Mailbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

