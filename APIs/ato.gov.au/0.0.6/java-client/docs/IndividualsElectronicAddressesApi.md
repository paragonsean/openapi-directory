# IndividualsElectronicAddressesApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**individualsPartyIdElectronicAddressesAddressIdDelete**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesAddressIdDelete) | **DELETE** /individuals/{partyId}/electronic-addresses/{addressId} | Delete an electronic address |
| [**individualsPartyIdElectronicAddressesAddressIdGet**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesAddressIdGet) | **GET** /individuals/{partyId}/electronic-addresses/{addressId} | Retrieve an electronic address |
| [**individualsPartyIdElectronicAddressesAddressIdPut**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesAddressIdPut) | **PUT** /individuals/{partyId}/electronic-addresses/{addressId} | Update an electronic address |
| [**individualsPartyIdElectronicAddressesGet**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesGet) | **GET** /individuals/{partyId}/electronic-addresses | Retrieve a list of electronic addresses |
| [**individualsPartyIdElectronicAddressesPost**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesPost) | **POST** /individuals/{partyId}/electronic-addresses | Create an electronic address |


<a id="individualsPartyIdElectronicAddressesAddressIdDelete"></a>
# **individualsPartyIdElectronicAddressesAddressIdDelete**
> individualsPartyIdElectronicAddressesAddressIdDelete(apiKey, partyId, addressId)

Delete an electronic address

Delete an electronic address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsElectronicAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsElectronicAddressesApi apiInstance = new IndividualsElectronicAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String addressId = "addressId_example"; // String | The address identifier.
    try {
      apiInstance.individualsPartyIdElectronicAddressesAddressIdDelete(apiKey, partyId, addressId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsElectronicAddressesApi#individualsPartyIdElectronicAddressesAddressIdDelete");
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
| **204** | Electronic Address was deleted |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdElectronicAddressesAddressIdGet"></a>
# **individualsPartyIdElectronicAddressesAddressIdGet**
> ElectronicAddress individualsPartyIdElectronicAddressesAddressIdGet(apiKey, partyId, addressId)

Retrieve an electronic address

Retrieve an electronic address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsElectronicAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsElectronicAddressesApi apiInstance = new IndividualsElectronicAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String addressId = "addressId_example"; // String | The address identifier.
    try {
      ElectronicAddress result = apiInstance.individualsPartyIdElectronicAddressesAddressIdGet(apiKey, partyId, addressId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsElectronicAddressesApi#individualsPartyIdElectronicAddressesAddressIdGet");
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

[**ElectronicAddress**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Electronic Address was retrieved successfully |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdElectronicAddressesAddressIdPut"></a>
# **individualsPartyIdElectronicAddressesAddressIdPut**
> ElectronicAddress individualsPartyIdElectronicAddressesAddressIdPut(apiKey, partyId, addressId, electronicAddress)

Update an electronic address

Update an electronic address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsElectronicAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsElectronicAddressesApi apiInstance = new IndividualsElectronicAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String addressId = "addressId_example"; // String | The address identifier.
    ElectronicAddress electronicAddress = new ElectronicAddress(); // ElectronicAddress | Electronic Address resource
    try {
      ElectronicAddress result = apiInstance.individualsPartyIdElectronicAddressesAddressIdPut(apiKey, partyId, addressId, electronicAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsElectronicAddressesApi#individualsPartyIdElectronicAddressesAddressIdPut");
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
| **electronicAddress** | [**ElectronicAddress**](ElectronicAddress.md)| Electronic Address resource | |

### Return type

[**ElectronicAddress**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Electronic Address was updated |  -  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdElectronicAddressesGet"></a>
# **individualsPartyIdElectronicAddressesGet**
> List&lt;ElectronicAddress&gt; individualsPartyIdElectronicAddressesGet(apiKey, partyId)

Retrieve a list of electronic addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsElectronicAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsElectronicAddressesApi apiInstance = new IndividualsElectronicAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      List<ElectronicAddress> result = apiInstance.individualsPartyIdElectronicAddressesGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsElectronicAddressesApi#individualsPartyIdElectronicAddressesGet");
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

[**List&lt;ElectronicAddress&gt;**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Electronic addresses were retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdElectronicAddressesPost"></a>
# **individualsPartyIdElectronicAddressesPost**
> ElectronicAddress individualsPartyIdElectronicAddressesPost(apiKey, partyId, electronicAddress)

Create an electronic address

Create an electronic address 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsElectronicAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsElectronicAddressesApi apiInstance = new IndividualsElectronicAddressesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    ElectronicAddress electronicAddress = new ElectronicAddress(); // ElectronicAddress | Electronic Address resource
    try {
      ElectronicAddress result = apiInstance.individualsPartyIdElectronicAddressesPost(apiKey, partyId, electronicAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsElectronicAddressesApi#individualsPartyIdElectronicAddressesPost");
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
| **electronicAddress** | [**ElectronicAddress**](ElectronicAddress.md)| Electronic Address resource | |

### Return type

[**ElectronicAddress**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Electronic Address was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

