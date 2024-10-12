# DomainsApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloneDomain**](DomainsApi.md#cloneDomain) | **POST** /domains/{domainId}/clone | Domain Clone |
| [**createDomain**](DomainsApi.md#createDomain) | **POST** /domains | Domain Create |
| [**createDomainRecord**](DomainsApi.md#createDomainRecord) | **POST** /domains/{domainId}/records | Domain Record Create |
| [**deleteDomain**](DomainsApi.md#deleteDomain) | **DELETE** /domains/{domainId} | Domain Delete |
| [**deleteDomainRecord**](DomainsApi.md#deleteDomainRecord) | **DELETE** /domains/{domainId}/records/{recordId} | Domain Record Delete |
| [**getDomain**](DomainsApi.md#getDomain) | **GET** /domains/{domainId} | Domain View |
| [**getDomainRecord**](DomainsApi.md#getDomainRecord) | **GET** /domains/{domainId}/records/{recordId} | Domain Record View |
| [**getDomainRecords**](DomainsApi.md#getDomainRecords) | **GET** /domains/{domainId}/records | Domain Records List |
| [**getDomainZone**](DomainsApi.md#getDomainZone) | **GET** /domains/{domainId}/zone-file | Domain Zone File View |
| [**getDomains**](DomainsApi.md#getDomains) | **GET** /domains | Domains List |
| [**importDomain**](DomainsApi.md#importDomain) | **POST** /domains/import | Domain Import |
| [**updateDomain**](DomainsApi.md#updateDomain) | **PUT** /domains/{domainId} | Domain Update |
| [**updateDomainRecord**](DomainsApi.md#updateDomainRecord) | **PUT** /domains/{domainId}/records/{recordId} | Domain Record Update |


<a id="cloneDomain"></a>
# **cloneDomain**
> Domain cloneDomain(domainId, cloneDomainRequest)

Domain Clone

Clones a Domain and all associated DNS records from a Domain that is registered in Linode&#39;s DNS manager. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domainId = "domainId_example"; // String | ID of the Domain to clone.
    CloneDomainRequest cloneDomainRequest = new CloneDomainRequest(); // CloneDomainRequest | Information about the Domain to clone.
    try {
      Domain result = apiInstance.cloneDomain(domainId, cloneDomainRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#cloneDomain");
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
| **domainId** | **String**| ID of the Domain to clone. | |
| **cloneDomainRequest** | [**CloneDomainRequest**](CloneDomainRequest.md)| Information about the Domain to clone. | |

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new Domain in Linode&#39;s DNS Manager, based on a cloned Domain.  |  -  |
| **0** | Error |  -  |

<a id="createDomain"></a>
# **createDomain**
> Domain createDomain(domain)

Domain Create

Adds a new Domain to Linode&#39;s DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode&#39;s nameservers so that the records hosted here are used. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Domain domain = new Domain(); // Domain | Information about the domain you are registering.
    try {
      Domain result = apiInstance.createDomain(domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#createDomain");
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
| **domain** | [**Domain**](Domain.md)| Information about the domain you are registering. | |

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain added successfully.  |  -  |
| **0** | Error |  -  |

<a id="createDomainRecord"></a>
# **createDomainRecord**
> DomainRecord createDomainRecord(domainId, domainRecord)

Domain Record Create

Adds a new Domain Record to the zonefile this Domain represents.  Each domain can have up to 12,000 active records. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain we are accessing Records for.
    DomainRecord domainRecord = new DomainRecord(); // DomainRecord | Information about the new Record to add. 
    try {
      DomainRecord result = apiInstance.createDomainRecord(domainId, domainRecord);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#createDomainRecord");
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
| **domainId** | **Integer**| The ID of the Domain we are accessing Records for. | |
| **domainRecord** | [**DomainRecord**](DomainRecord.md)| Information about the new Record to add.  | |

### Return type

[**DomainRecord**](DomainRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain Record created successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteDomain"></a>
# **deleteDomain**
> Object deleteDomain(domainId)

Domain Delete

Deletes a Domain from Linode&#39;s DNS Manager. The Domain will be removed from Linode&#39;s nameservers shortly after this operation completes. This also deletes all associated Domain Records. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain to access.
    try {
      Object result = apiInstance.deleteDomain(domainId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#deleteDomain");
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
| **domainId** | **Integer**| The ID of the Domain to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteDomainRecord"></a>
# **deleteDomainRecord**
> Object deleteDomainRecord(domainId, recordId)

Domain Record Delete

Deletes a Record on this Domain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain whose Record you are accessing.
    Integer recordId = 56; // Integer | The ID of the Record you are accessing.
    try {
      Object result = apiInstance.deleteDomainRecord(domainId, recordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#deleteDomainRecord");
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
| **domainId** | **Integer**| The ID of the Domain whose Record you are accessing. | |
| **recordId** | **Integer**| The ID of the Record you are accessing. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Record deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="getDomain"></a>
# **getDomain**
> Domain getDomain(domainId)

Domain View

This is a single Domain that you have registered in Linode&#39;s DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode&#39;s nameservers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain to access.
    try {
      Domain result = apiInstance.getDomain(domainId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomain");
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
| **domainId** | **Integer**| The ID of the Domain to access. | |

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Domain in Linode&#39;s DNS Manager.  |  -  |
| **0** | Error |  -  |

<a id="getDomainRecord"></a>
# **getDomainRecord**
> DomainRecord getDomainRecord(domainId, recordId)

Domain Record View

View a single Record on this Domain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain whose Record you are accessing.
    Integer recordId = 56; // Integer | The ID of the Record you are accessing.
    try {
      DomainRecord result = apiInstance.getDomainRecord(domainId, recordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainRecord");
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
| **domainId** | **Integer**| The ID of the Domain whose Record you are accessing. | |
| **recordId** | **Integer**| The ID of the Record you are accessing. | |

### Return type

[**DomainRecord**](DomainRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Domain Record object. |  -  |
| **0** | Error |  -  |

<a id="getDomainRecords"></a>
# **getDomainRecords**
> GetDomainRecords200Response getDomainRecords(domainId, page, pageSize)

Domain Records List

Returns a paginated list of Records configured on a Domain in Linode&#39;s DNS Manager. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain we are accessing Records for.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDomainRecords200Response result = apiInstance.getDomainRecords(domainId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainRecords");
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
| **domainId** | **Integer**| The ID of the Domain we are accessing Records for. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDomainRecords200Response**](GetDomainRecords200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Domain Records. |  -  |

<a id="getDomainZone"></a>
# **getDomainZone**
> GetDomainZone200Response getDomainZone(domainId)

Domain Zone File View

Returns the zone file for the last rendered zone for the specified domain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domainId = "domainId_example"; // String | ID of the Domain.
    try {
      GetDomainZone200Response result = apiInstance.getDomainZone(domainId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainZone");
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
| **domainId** | **String**| ID of the Domain. | |

### Return type

[**GetDomainZone200Response**](GetDomainZone200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array containing the lines of the domain zone file.  |  -  |
| **0** | Error |  -  |

<a id="getDomains"></a>
# **getDomains**
> GetDomains200Response getDomains(page, pageSize)

Domains List

This is a collection of Domains that you have registered in Linode&#39;s DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode&#39;s nameservers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDomains200Response result = apiInstance.getDomains(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomains");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDomains200Response**](GetDomains200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Domains you have registered. |  -  |
| **0** | Error |  -  |

<a id="importDomain"></a>
# **importDomain**
> Domain importDomain(importDomainRequest)

Domain Import

Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:    - 96.126.114.97   - 96.126.114.98   - 2600:3c00::5e   - 2600:3c00::5f 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    ImportDomainRequest importDomainRequest = new ImportDomainRequest(); // ImportDomainRequest | Information about the Domain to import.
    try {
      Domain result = apiInstance.importDomain(importDomainRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#importDomain");
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
| **importDomainRequest** | [**ImportDomainRequest**](ImportDomainRequest.md)| Information about the Domain to import. | [optional] |

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Domain in Linode&#39;s DNS Manager.  |  -  |
| **0** | Error |  -  |

<a id="updateDomain"></a>
# **updateDomain**
> Domain updateDomain(domainId, domain)

Domain Update

Update information about a Domain in Linode&#39;s DNS Manager. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain to access.
    Domain domain = new Domain(); // Domain | The Domain information to update.
    try {
      Domain result = apiInstance.updateDomain(domainId, domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#updateDomain");
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
| **domainId** | **Integer**| The ID of the Domain to access. | |
| **domain** | [**Domain**](Domain.md)| The Domain information to update. | |

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain update successful. |  -  |
| **0** | Error |  -  |

<a id="updateDomainRecord"></a>
# **updateDomainRecord**
> DomainRecord updateDomainRecord(domainId, recordId, updateDomainRecordRequest)

Domain Record Update

Updates a single Record on this Domain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer domainId = 56; // Integer | The ID of the Domain whose Record you are accessing.
    Integer recordId = 56; // Integer | The ID of the Record you are accessing.
    UpdateDomainRecordRequest updateDomainRecordRequest = new UpdateDomainRecordRequest(); // UpdateDomainRecordRequest | The values to change.
    try {
      DomainRecord result = apiInstance.updateDomainRecord(domainId, recordId, updateDomainRecordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#updateDomainRecord");
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
| **domainId** | **Integer**| The ID of the Domain whose Record you are accessing. | |
| **recordId** | **Integer**| The ID of the Record you are accessing. | |
| **updateDomainRecordRequest** | [**UpdateDomainRecordRequest**](UpdateDomainRecordRequest.md)| The values to change. | |

### Return type

[**DomainRecord**](DomainRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain Record updated. |  -  |
| **0** | Error |  -  |

