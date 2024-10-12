# DnsZoneApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureDNSForSite**](DnsZoneApi.md#configureDNSForSite) | **PUT** /sites/{site_id}/dns |  |
| [**createDnsRecord**](DnsZoneApi.md#createDnsRecord) | **POST** /dns_zones/{zone_id}/dns_records |  |
| [**createDnsZone**](DnsZoneApi.md#createDnsZone) | **POST** /dns_zones |  |
| [**deleteDnsRecord**](DnsZoneApi.md#deleteDnsRecord) | **DELETE** /dns_zones/{zone_id}/dns_records/{dns_record_id} |  |
| [**deleteDnsZone**](DnsZoneApi.md#deleteDnsZone) | **DELETE** /dns_zones/{zone_id} |  |
| [**getDNSForSite**](DnsZoneApi.md#getDNSForSite) | **GET** /sites/{site_id}/dns |  |
| [**getDnsRecords**](DnsZoneApi.md#getDnsRecords) | **GET** /dns_zones/{zone_id}/dns_records |  |
| [**getDnsZone**](DnsZoneApi.md#getDnsZone) | **GET** /dns_zones/{zone_id} |  |
| [**getDnsZones**](DnsZoneApi.md#getDnsZones) | **GET** /dns_zones |  |
| [**getIndividualDnsRecord**](DnsZoneApi.md#getIndividualDnsRecord) | **GET** /dns_zones/{zone_id}/dns_records/{dns_record_id} |  |
| [**transferDnsZone**](DnsZoneApi.md#transferDnsZone) | **PUT** /dns_zones/{zone_id}/transfer |  |


<a id="configureDNSForSite"></a>
# **configureDNSForSite**
> List&lt;DnsZone&gt; configureDNSForSite(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<DnsZone> result = apiInstance.configureDNSForSite(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#configureDNSForSite");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;DnsZone&gt;**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="createDnsRecord"></a>
# **createDnsRecord**
> DnsRecord createDnsRecord(zoneId, dnsRecord)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    DnsRecordCreate dnsRecord = new DnsRecordCreate(); // DnsRecordCreate | 
    try {
      DnsRecord result = apiInstance.createDnsRecord(zoneId, dnsRecord);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#createDnsRecord");
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
| **zoneId** | **String**|  | |
| **dnsRecord** | [**DnsRecordCreate**](DnsRecordCreate.md)|  | |

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="createDnsZone"></a>
# **createDnsZone**
> DnsZone createDnsZone(dnsZoneParams)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    DnsZoneSetup dnsZoneParams = new DnsZoneSetup(); // DnsZoneSetup | 
    try {
      DnsZone result = apiInstance.createDnsZone(dnsZoneParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#createDnsZone");
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
| **dnsZoneParams** | [**DnsZoneSetup**](DnsZoneSetup.md)|  | |

### Return type

[**DnsZone**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="deleteDnsRecord"></a>
# **deleteDnsRecord**
> deleteDnsRecord(zoneId, dnsRecordId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    String dnsRecordId = "dnsRecordId_example"; // String | 
    try {
      apiInstance.deleteDnsRecord(zoneId, dnsRecordId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#deleteDnsRecord");
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
| **zoneId** | **String**|  | |
| **dnsRecordId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | record deleted |  -  |
| **0** | error |  -  |

<a id="deleteDnsZone"></a>
# **deleteDnsZone**
> deleteDnsZone(zoneId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    try {
      apiInstance.deleteDnsZone(zoneId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#deleteDnsZone");
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
| **zoneId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | delete a single DNS zone |  -  |
| **0** | error |  -  |

<a id="getDNSForSite"></a>
# **getDNSForSite**
> List&lt;DnsZone&gt; getDNSForSite(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<DnsZone> result = apiInstance.getDNSForSite(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#getDNSForSite");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;DnsZone&gt;**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="getDnsRecords"></a>
# **getDnsRecords**
> List&lt;DnsRecord&gt; getDnsRecords(zoneId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    try {
      List<DnsRecord> result = apiInstance.getDnsRecords(zoneId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#getDnsRecords");
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
| **zoneId** | **String**|  | |

### Return type

[**List&lt;DnsRecord&gt;**](DnsRecord.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get all DNS records for a single DNS zone |  -  |
| **0** | error |  -  |

<a id="getDnsZone"></a>
# **getDnsZone**
> DnsZone getDnsZone(zoneId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    try {
      DnsZone result = apiInstance.getDnsZone(zoneId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#getDnsZone");
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
| **zoneId** | **String**|  | |

### Return type

[**DnsZone**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get a single DNS zone |  -  |
| **0** | error |  -  |

<a id="getDnsZones"></a>
# **getDnsZones**
> List&lt;DnsZone&gt; getDnsZones(accountSlug)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    try {
      List<DnsZone> result = apiInstance.getDnsZones(accountSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#getDnsZones");
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
| **accountSlug** | **String**|  | [optional] |

### Return type

[**List&lt;DnsZone&gt;**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get all DNS zones the user has access to |  -  |
| **0** | error |  -  |

<a id="getIndividualDnsRecord"></a>
# **getIndividualDnsRecord**
> DnsRecord getIndividualDnsRecord(zoneId, dnsRecordId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    String dnsRecordId = "dnsRecordId_example"; // String | 
    try {
      DnsRecord result = apiInstance.getIndividualDnsRecord(zoneId, dnsRecordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#getIndividualDnsRecord");
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
| **zoneId** | **String**|  | |
| **dnsRecordId** | **String**|  | |

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get a single DNS record |  -  |
| **0** | error |  -  |

<a id="transferDnsZone"></a>
# **transferDnsZone**
> DnsZone transferDnsZone(zoneId, accountId, transferAccountId, transferUserId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DnsZoneApi apiInstance = new DnsZoneApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    String accountId = "accountId_example"; // String | the account of the dns zone
    String transferAccountId = "transferAccountId_example"; // String | the account you want to transfer the dns zone to
    String transferUserId = "transferUserId_example"; // String | the user you want to transfer the dns zone to
    try {
      DnsZone result = apiInstance.transferDnsZone(zoneId, accountId, transferAccountId, transferUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsZoneApi#transferDnsZone");
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
| **zoneId** | **String**|  | |
| **accountId** | **String**| the account of the dns zone | |
| **transferAccountId** | **String**| the account you want to transfer the dns zone to | |
| **transferUserId** | **String**| the user you want to transfer the dns zone to | |

### Return type

[**DnsZone**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | transfer a DNS zone to another account |  -  |
| **0** | error |  -  |

