# OrganisationsApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organisationsGet**](OrganisationsApi.md#organisationsGet) | **GET** /organisations | Retrieve a list of organisations |
| [**organisationsPartyIdDelete**](OrganisationsApi.md#organisationsPartyIdDelete) | **DELETE** /organisations/{partyId} | Delete an organisation |
| [**organisationsPartyIdGet**](OrganisationsApi.md#organisationsPartyIdGet) | **GET** /organisations/{partyId} | Retrieve an organisation |
| [**organisationsPartyIdPut**](OrganisationsApi.md#organisationsPartyIdPut) | **PUT** /organisations/{partyId} | Update an organisation |
| [**organisationsPost**](OrganisationsApi.md#organisationsPost) | **POST** /organisations | Create an organisation |


<a id="organisationsGet"></a>
# **organisationsGet**
> List&lt;Organisation&gt; organisationsGet(apiKey, registeredIdentifier, identifier)

Retrieve a list of organisations

Retrieve a list of organisations 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String registeredIdentifier = "registeredIdentifier_example"; // String | The registered identifier, for example, `ACN` or `ABN`.
    String identifier = "identifier_example"; // String | The identifier, for example, `123456789`.
    try {
      List<Organisation> result = apiInstance.organisationsGet(apiKey, registeredIdentifier, identifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsGet");
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
| **registeredIdentifier** | **String**| The registered identifier, for example, &#x60;ACN&#x60; or &#x60;ABN&#x60;. | [optional] |
| **identifier** | **String**| The identifier, for example, &#x60;123456789&#x60;. | [optional] |

### Return type

[**List&lt;Organisation&gt;**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of organisations was retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdDelete"></a>
# **organisationsPartyIdDelete**
> organisationsPartyIdDelete(apiKey, partyId)

Delete an organisation

Delete an organisation with the specified identifier 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      apiInstance.organisationsPartyIdDelete(apiKey, partyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsPartyIdDelete");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Organisation was deleted |  -  |
| **400** | Request can not be executed in the current system state |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdGet"></a>
# **organisationsPartyIdGet**
> Organisation organisationsPartyIdGet(apiKey, partyId)

Retrieve an organisation

Retrieve an organisation with the specified identifier 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      Organisation result = apiInstance.organisationsPartyIdGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsPartyIdGet");
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

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Individual was retrieved successfully |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdPut"></a>
# **organisationsPartyIdPut**
> Organisation organisationsPartyIdPut(apiKey, partyId, organisation)

Update an organisation

Update an organisation 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    Organisation organisation = new Organisation(); // Organisation | Organisation resource
    try {
      Organisation result = apiInstance.organisationsPartyIdPut(apiKey, partyId, organisation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsPartyIdPut");
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
| **organisation** | [**Organisation**](Organisation.md)| Organisation resource | |

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organisation was updated |  -  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPost"></a>
# **organisationsPost**
> Organisation organisationsPost(apiKey, organisation)

Create an organisation

Create an organisation 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    Organisation organisation = new Organisation(); // Organisation | Organisation resource
    try {
      Organisation result = apiInstance.organisationsPost(apiKey, organisation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsPost");
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
| **organisation** | [**Organisation**](Organisation.md)| Organisation resource | |

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Organisation was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

