# OrganisationsBusinessNamesApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organisationsPartyIdBusinessNamesGet**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesGet) | **GET** /organisations/{partyId}/business-names | Retrieve a list of business names |
| [**organisationsPartyIdBusinessNamesPost**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesPost) | **POST** /organisations/{partyId}/business-names | Create a business name |
| [**organisationsPartyIdBusinessNamesProductIdDelete**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesProductIdDelete) | **DELETE** /organisations/{partyId}/business-names/{productId} | Delete a business name |
| [**organisationsPartyIdBusinessNamesProductIdGet**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesProductIdGet) | **GET** /organisations/{partyId}/business-names/{productId} | Retrieve a business name |
| [**organisationsPartyIdBusinessNamesProductIdPut**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesProductIdPut) | **PUT** /organisations/{partyId}/business-names/{productId} | Update a business name |


<a id="organisationsPartyIdBusinessNamesGet"></a>
# **organisationsPartyIdBusinessNamesGet**
> List&lt;BusinessName&gt; organisationsPartyIdBusinessNamesGet(apiKey, partyId)

Retrieve a list of business names

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsBusinessNamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsBusinessNamesApi apiInstance = new OrganisationsBusinessNamesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      List<BusinessName> result = apiInstance.organisationsPartyIdBusinessNamesGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsBusinessNamesApi#organisationsPartyIdBusinessNamesGet");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |

### Return type

[**List&lt;BusinessName&gt;**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business Names were retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdBusinessNamesPost"></a>
# **organisationsPartyIdBusinessNamesPost**
> BusinessName organisationsPartyIdBusinessNamesPost(apiKey, partyId, businessName)

Create a business name

Create a business name 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsBusinessNamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsBusinessNamesApi apiInstance = new OrganisationsBusinessNamesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    BusinessName businessName = new BusinessName(); // BusinessName | Business Name resource
    try {
      BusinessName result = apiInstance.organisationsPartyIdBusinessNamesPost(apiKey, partyId, businessName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsBusinessNamesApi#organisationsPartyIdBusinessNamesPost");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **businessName** | [**BusinessName**](BusinessName.md)| Business Name resource | |

### Return type

[**BusinessName**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Business Name was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

<a id="organisationsPartyIdBusinessNamesProductIdDelete"></a>
# **organisationsPartyIdBusinessNamesProductIdDelete**
> organisationsPartyIdBusinessNamesProductIdDelete(apiKey, partyId, productId)

Delete a business name

Delete a business name 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsBusinessNamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsBusinessNamesApi apiInstance = new OrganisationsBusinessNamesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String productId = "productId_example"; // String | The product identifier.
    try {
      apiInstance.organisationsPartyIdBusinessNamesProductIdDelete(apiKey, partyId, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsBusinessNamesApi#organisationsPartyIdBusinessNamesProductIdDelete");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **productId** | **String**| The product identifier. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Address was deleted |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdBusinessNamesProductIdGet"></a>
# **organisationsPartyIdBusinessNamesProductIdGet**
> BusinessName organisationsPartyIdBusinessNamesProductIdGet(apiKey, partyId, productId)

Retrieve a business name

Retrieve a business name 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsBusinessNamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsBusinessNamesApi apiInstance = new OrganisationsBusinessNamesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String productId = "productId_example"; // String | The product identifier.
    try {
      BusinessName result = apiInstance.organisationsPartyIdBusinessNamesProductIdGet(apiKey, partyId, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsBusinessNamesApi#organisationsPartyIdBusinessNamesProductIdGet");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **productId** | **String**| The product identifier. | |

### Return type

[**BusinessName**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business Name was retrieved successfully |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdBusinessNamesProductIdPut"></a>
# **organisationsPartyIdBusinessNamesProductIdPut**
> BusinessName organisationsPartyIdBusinessNamesProductIdPut(apiKey, partyId, productId, businessName)

Update a business name

Update a business name 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsBusinessNamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsBusinessNamesApi apiInstance = new OrganisationsBusinessNamesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String productId = "productId_example"; // String | The product identifier.
    BusinessName businessName = new BusinessName(); // BusinessName | Business Name resource
    try {
      BusinessName result = apiInstance.organisationsPartyIdBusinessNamesProductIdPut(apiKey, partyId, productId, businessName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsBusinessNamesApi#organisationsPartyIdBusinessNamesProductIdPut");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **productId** | **String**| The product identifier. | |
| **businessName** | [**BusinessName**](BusinessName.md)| Business Name resource | |

### Return type

[**BusinessName**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address was updated |  -  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

