# DomainsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureDomain**](DomainsApi.md#configureDomain) | **PUT** /domains/{domainName}/renew | Edit domain name renew state |
| [**editNameServers**](DomainsApi.md#editNameServers) | **PUT** /domains/{domainName}/nameservers | Edit domain name servers |
| [**getDomain**](DomainsApi.md#getDomain) | **GET** /domains/{domainName} | Details of a domain |
| [**getDomains**](DomainsApi.md#getDomains) | **GET** /domains | Overviews of domains |
| [**register**](DomainsApi.md#register) | **POST** /domains/registrations | Register a domain |
| [**transfer**](DomainsApi.md#transfer) | **POST** /domains/transfers | Transfer a domain |


<a id="configureDomain"></a>
# **configureDomain**
> configureDomain(domainName, domainName2, editDomainWillRenewRequest)

Edit domain name renew state

Allowed if can_toggle_renew is true on the domain detail:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;If there are no unpaid invoices for the domain name anymore.&lt;/li&gt;&lt;li&gt;If the renewal won&#39;t start within 1 month.&lt;/li&gt;&lt;/ul&gt;  Allowed if the requesting user has the finance role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name
    String domainName2 = "domainName_example"; // String | Automatically added
    EditDomainWillRenewRequest editDomainWillRenewRequest = new EditDomainWillRenewRequest(); // EditDomainWillRenewRequest | Contains the domain renew information
    try {
      apiInstance.configureDomain(domainName, domainName2, editDomainWillRenewRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#configureDomain");
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
| **domainName** | **String**| The domain name | |
| **domainName2** | **String**| Automatically added | |
| **editDomainWillRenewRequest** | [**EditDomainWillRenewRequest**](EditDomainWillRenewRequest.md)| Contains the domain renew information | [optional] |

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

<a id="editNameServers"></a>
# **editNameServers**
> editNameServers(domainName, domainName2, editNameServers)

Edit domain name servers



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name
    String domainName2 = "domainName_example"; // String | Automatically added
    EditNameServers editNameServers = new EditNameServers(); // EditNameServers | 
    try {
      apiInstance.editNameServers(domainName, domainName2, editNameServers);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#editNameServers");
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
| **domainName** | **String**| The domain name | |
| **domainName2** | **String**| Automatically added | |
| **editNameServers** | [**EditNameServers**](EditNameServers.md)|  | [optional] |

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

<a id="getDomain"></a>
# **getDomain**
> DomainDetail getDomain(domainName, domainName2)

Details of a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      DomainDetail result = apiInstance.getDomain(domainName, domainName2);
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
| **domainName** | **String**| The domain name | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**DomainDetail**](DomainDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDomains"></a>
# **getDomains**
> List&lt;Domain&gt; getDomains(skip, take)

Overviews of domains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<Domain> result = apiInstance.getDomains(skip, take);
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;Domain&gt;**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

<a id="register"></a>
# **register**
> register(registerDomain)

Register a domain

Registers an available domain.&lt;br /&gt;Domain names with extension &#39;.ca&#39; are only available for registrants with country code &#39;CA&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    RegisterDomain registerDomain = new RegisterDomain(); // RegisterDomain | 
    try {
      apiInstance.register(registerDomain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#register");
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
| **registerDomain** | [**RegisterDomain**](RegisterDomain.md)|  | [optional] |

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
| **202** | Success |  -  |

<a id="transfer"></a>
# **transfer**
> transfer(transferDomain)

Transfer a domain

Transfers a domain with a transfer authorization code.&lt;br /&gt;Domain names with extension &#39;.ca&#39; are only available for registrants with country code &#39;CA&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    TransferDomain transferDomain = new TransferDomain(); // TransferDomain | 
    try {
      apiInstance.transfer(transferDomain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#transfer");
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
| **transferDomain** | [**TransferDomain**](TransferDomain.md)|  | [optional] |

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
| **202** | Success |  -  |

