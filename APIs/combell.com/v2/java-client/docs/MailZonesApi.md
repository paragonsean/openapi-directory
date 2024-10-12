# MailZonesApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureAlias**](MailZonesApi.md#configureAlias) | **PUT** /mailzones/{domainName}/aliases/{emailAddress} | Configure a alias |
| [**configureAntiSpam**](MailZonesApi.md#configureAntiSpam) | **PUT** /mailzones/{domainName}/antispam | Configure anti-spam for mail zone |
| [**configureSmtpDomain**](MailZonesApi.md#configureSmtpDomain) | **PUT** /mailzones/{domainName}/smtpdomains/{hostname} | Configure an extra smtp domain |
| [**createAlias**](MailZonesApi.md#createAlias) | **POST** /mailzones/{domainName}/aliases | Create a new alias |
| [**createCatchAll**](MailZonesApi.md#createCatchAll) | **POST** /mailzones/{domainName}/catchall | Create a catch-all on the mail zone |
| [**createSmtpDomain**](MailZonesApi.md#createSmtpDomain) | **POST** /mailzones/{domainName}/smtpdomains | Create an extra smtp domain |
| [**deleteAlias**](MailZonesApi.md#deleteAlias) | **DELETE** /mailzones/{domainName}/aliases/{emailAddress} | Delete a alias |
| [**deleteCatchAll**](MailZonesApi.md#deleteCatchAll) | **DELETE** /mailzones/{domainName}/catchall/{emailAddress} | Delete a catch-all on the mail zone |
| [**deleteSmtpDomain**](MailZonesApi.md#deleteSmtpDomain) | **DELETE** /mailzones/{domainName}/smtpdomains/{hostname} | Delete an extra smtp domain |
| [**getMailZone**](MailZonesApi.md#getMailZone) | **GET** /mailzones/{domainName} | Get the mail zone. |


<a id="configureAlias"></a>
# **configureAlias**
> configureAlias(domainName, emailAddress, domainName2, emailAddress2, updateAliasRequest)

Configure a alias

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String emailAddress = "emailAddress_example"; // String | Alias e-mail address.
    String domainName2 = "domainName_example"; // String | Automatically added
    String emailAddress2 = "emailAddress_example"; // String | Automatically added
    UpdateAliasRequest updateAliasRequest = new UpdateAliasRequest(); // UpdateAliasRequest | Contains the alias information.
    try {
      apiInstance.configureAlias(domainName, emailAddress, domainName2, emailAddress2, updateAliasRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#configureAlias");
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
| **domainName** | **String**| Mail zone domain name. | |
| **emailAddress** | **String**| Alias e-mail address. | |
| **domainName2** | **String**| Automatically added | |
| **emailAddress2** | **String**| Automatically added | |
| **updateAliasRequest** | [**UpdateAliasRequest**](UpdateAliasRequest.md)| Contains the alias information. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="configureAntiSpam"></a>
# **configureAntiSpam**
> configureAntiSpam(domainName, domainName2, updateAntiSpamRequest)

Configure anti-spam for mail zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    UpdateAntiSpamRequest updateAntiSpamRequest = new UpdateAntiSpamRequest(); // UpdateAntiSpamRequest | Contains the anti-spam information.
    try {
      apiInstance.configureAntiSpam(domainName, domainName2, updateAntiSpamRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#configureAntiSpam");
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
| **domainName** | **String**| Mail zone domain name. | |
| **domainName2** | **String**| Automatically added | |
| **updateAntiSpamRequest** | [**UpdateAntiSpamRequest**](UpdateAntiSpamRequest.md)| Contains the anti-spam information. | [optional] |

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

<a id="configureSmtpDomain"></a>
# **configureSmtpDomain**
> configureSmtpDomain(domainName, hostname, domainName2, updateSmtpDomainRequest)

Configure an extra smtp domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String hostname = "hostname_example"; // String | Smtp domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    UpdateSmtpDomainRequest updateSmtpDomainRequest = new UpdateSmtpDomainRequest(); // UpdateSmtpDomainRequest | Contains the smtp domain information.
    try {
      apiInstance.configureSmtpDomain(domainName, hostname, domainName2, updateSmtpDomainRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#configureSmtpDomain");
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
| **domainName** | **String**| Mail zone domain name. | |
| **hostname** | **String**| Smtp domain name. | |
| **domainName2** | **String**| Automatically added | |
| **updateSmtpDomainRequest** | [**UpdateSmtpDomainRequest**](UpdateSmtpDomainRequest.md)| Contains the smtp domain information. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="createAlias"></a>
# **createAlias**
> createAlias(domainName, domainName2, createAliasRequest)

Create a new alias

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    CreateAliasRequest createAliasRequest = new CreateAliasRequest(); // CreateAliasRequest | Contains the alias information.
    try {
      apiInstance.createAlias(domainName, domainName2, createAliasRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#createAlias");
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
| **domainName** | **String**| Mail zone domain name. | |
| **domainName2** | **String**| Automatically added | |
| **createAliasRequest** | [**CreateAliasRequest**](CreateAliasRequest.md)| Contains the alias information. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |
| **400** | Bad Request |  -  |

<a id="createCatchAll"></a>
# **createCatchAll**
> createCatchAll(domainName, domainName2, createCatchAllRequest)

Create a catch-all on the mail zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    CreateCatchAllRequest createCatchAllRequest = new CreateCatchAllRequest(); // CreateCatchAllRequest | Contains the catch-all information.
    try {
      apiInstance.createCatchAll(domainName, domainName2, createCatchAllRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#createCatchAll");
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
| **domainName** | **String**| Mail zone domain name. | |
| **domainName2** | **String**| Automatically added | |
| **createCatchAllRequest** | [**CreateCatchAllRequest**](CreateCatchAllRequest.md)| Contains the catch-all information. | [optional] |

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

<a id="createSmtpDomain"></a>
# **createSmtpDomain**
> createSmtpDomain(domainName, domainName2, createSmtpDomainRequest)

Create an extra smtp domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    CreateSmtpDomainRequest createSmtpDomainRequest = new CreateSmtpDomainRequest(); // CreateSmtpDomainRequest | Contains the smtp domain information.
    try {
      apiInstance.createSmtpDomain(domainName, domainName2, createSmtpDomainRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#createSmtpDomain");
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
| **domainName** | **String**| Mail zone domain name. | |
| **domainName2** | **String**| Automatically added | |
| **createSmtpDomainRequest** | [**CreateSmtpDomainRequest**](CreateSmtpDomainRequest.md)| Contains the smtp domain information. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |
| **400** | Bad Request |  -  |

<a id="deleteAlias"></a>
# **deleteAlias**
> deleteAlias(domainName, emailAddress, domainName2, emailAddress2)

Delete a alias

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String emailAddress = "emailAddress_example"; // String | Alias e-mail address.
    String domainName2 = "domainName_example"; // String | Automatically added
    String emailAddress2 = "emailAddress_example"; // String | Automatically added
    try {
      apiInstance.deleteAlias(domainName, emailAddress, domainName2, emailAddress2);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#deleteAlias");
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
| **domainName** | **String**| Mail zone domain name. | |
| **emailAddress** | **String**| Alias e-mail address. | |
| **domainName2** | **String**| Automatically added | |
| **emailAddress2** | **String**| Automatically added | |

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

<a id="deleteCatchAll"></a>
# **deleteCatchAll**
> deleteCatchAll(domainName, emailAddress, domainName2, emailAddress2)

Delete a catch-all on the mail zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String emailAddress = "emailAddress_example"; // String | E-mail address to which all e-mails are sent to inexistent mailboxes or aliases.
    String domainName2 = "domainName_example"; // String | Automatically added
    String emailAddress2 = "emailAddress_example"; // String | Automatically added
    try {
      apiInstance.deleteCatchAll(domainName, emailAddress, domainName2, emailAddress2);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#deleteCatchAll");
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
| **domainName** | **String**| Mail zone domain name. | |
| **emailAddress** | **String**| E-mail address to which all e-mails are sent to inexistent mailboxes or aliases. | |
| **domainName2** | **String**| Automatically added | |
| **emailAddress2** | **String**| Automatically added | |

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

<a id="deleteSmtpDomain"></a>
# **deleteSmtpDomain**
> deleteSmtpDomain(domainName, hostname, domainName2)

Delete an extra smtp domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String hostname = "hostname_example"; // String | Smtp domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      apiInstance.deleteSmtpDomain(domainName, hostname, domainName2);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#deleteSmtpDomain");
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
| **domainName** | **String**| Mail zone domain name. | |
| **hostname** | **String**| Smtp domain name. | |
| **domainName2** | **String**| Automatically added | |

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

<a id="getMailZone"></a>
# **getMailZone**
> MailZone getMailZone(domainName, domainName2)

Get the mail zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MailZonesApi apiInstance = new MailZonesApi(defaultClient);
    String domainName = "domainName_example"; // String | Mail zone domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      MailZone result = apiInstance.getMailZone(domainName, domainName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailZonesApi#getMailZone");
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
| **domainName** | **String**| Mail zone domain name. | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**MailZone**](MailZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

