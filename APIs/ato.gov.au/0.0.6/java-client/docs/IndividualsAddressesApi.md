# IndividualsAddressesApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**individualsPartyIdAddressesAddressIdDelete**](IndividualsAddressesApi.md#individualsPartyIdAddressesAddressIdDelete) | **DELETE** /individuals/{partyId}/addresses/{addressId} | Delete an address |
| [**individualsPartyIdAddressesAddressIdGet**](IndividualsAddressesApi.md#individualsPartyIdAddressesAddressIdGet) | **GET** /individuals/{partyId}/addresses/{addressId} | Retrieve an address |
| [**individualsPartyIdAddressesAddressIdPut**](IndividualsAddressesApi.md#individualsPartyIdAddressesAddressIdPut) | **PUT** /individuals/{partyId}/addresses/{addressId} | Update an address |
| [**individualsPartyIdAddressesGet**](IndividualsAddressesApi.md#individualsPartyIdAddressesGet) | **GET** /individuals/{partyId}/addresses | Retrieve a list of addresses |
| [**individualsPartyIdAddressesPost**](IndividualsAddressesApi.md#individualsPartyIdAddressesPost) | **POST** /individuals/{partyId}/addresses | Create an address |


<a id="individualsPartyIdAddressesAddressIdDelete"></a>
# **individualsPartyIdAddressesAddressIdDelete**
> individualsPartyIdAddressesAddressIdDelete(apiKey, partyId, addressId)

Delete an address

Delete an address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsAddressesApi apiInstance = new IndividualsAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String addressId = "addressId_example"; // String | The address identifier.
    try {
      apiInstance.individualsPartyIdAddressesAddressIdDelete(apiKey, partyId, addressId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsAddressesApi#individualsPartyIdAddressesAddressIdDelete");
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
| **addressId** | **String**| The address identifier. | |

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

<a id="individualsPartyIdAddressesAddressIdGet"></a>
# **individualsPartyIdAddressesAddressIdGet**
> Address individualsPartyIdAddressesAddressIdGet(apiKey, partyId, addressId)

Retrieve an address

Retrieve an address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsAddressesApi apiInstance = new IndividualsAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String addressId = "addressId_example"; // String | The address identifier.
    try {
      Address result = apiInstance.individualsPartyIdAddressesAddressIdGet(apiKey, partyId, addressId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsAddressesApi#individualsPartyIdAddressesAddressIdGet");
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
| **addressId** | **String**| The address identifier. | |

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address was retrieved successfully |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdAddressesAddressIdPut"></a>
# **individualsPartyIdAddressesAddressIdPut**
> Address individualsPartyIdAddressesAddressIdPut(apiKey, partyId, addressId, address)

Update an address

Update an address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsAddressesApi apiInstance = new IndividualsAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String addressId = "addressId_example"; // String | The address identifier.
    Address address = new Address(); // Address | Address resource
    try {
      Address result = apiInstance.individualsPartyIdAddressesAddressIdPut(apiKey, partyId, addressId, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsAddressesApi#individualsPartyIdAddressesAddressIdPut");
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
| **addressId** | **String**| The address identifier. | |
| **address** | [**Address**](Address.md)| Address resource | |

### Return type

[**Address**](Address.md)

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

<a id="individualsPartyIdAddressesGet"></a>
# **individualsPartyIdAddressesGet**
> List&lt;Address&gt; individualsPartyIdAddressesGet(apiKey, partyId)

Retrieve a list of addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsAddressesApi apiInstance = new IndividualsAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      List<Address> result = apiInstance.individualsPartyIdAddressesGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsAddressesApi#individualsPartyIdAddressesGet");
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

[**List&lt;Address&gt;**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Addresses were retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdAddressesPost"></a>
# **individualsPartyIdAddressesPost**
> Address individualsPartyIdAddressesPost(apiKey, partyId, address)

Create an address

Create an address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsAddressesApi apiInstance = new IndividualsAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    Address address = new Address(); // Address | Address resource
    try {
      Address result = apiInstance.individualsPartyIdAddressesPost(apiKey, partyId, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsAddressesApi#individualsPartyIdAddressesPost");
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
| **address** | [**Address**](Address.md)| Address resource | |

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Address was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

