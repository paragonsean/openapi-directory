# IndividualsLicensesApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**individualsPartyIdLicensesGet**](IndividualsLicensesApi.md#individualsPartyIdLicensesGet) | **GET** /individuals/{partyId}/licenses | Retrieve a list of licenses |
| [**individualsPartyIdLicensesPost**](IndividualsLicensesApi.md#individualsPartyIdLicensesPost) | **POST** /individuals/{partyId}/licenses | Create a license |
| [**individualsPartyIdLicensesProductIdDelete**](IndividualsLicensesApi.md#individualsPartyIdLicensesProductIdDelete) | **DELETE** /individuals/{partyId}/licenses/{productId} | Delete a license |
| [**individualsPartyIdLicensesProductIdGet**](IndividualsLicensesApi.md#individualsPartyIdLicensesProductIdGet) | **GET** /individuals/{partyId}/licenses/{productId} | Retrieve a license |
| [**individualsPartyIdLicensesProductIdPut**](IndividualsLicensesApi.md#individualsPartyIdLicensesProductIdPut) | **PUT** /individuals/{partyId}/licenses/{productId} | Update a license |


<a id="individualsPartyIdLicensesGet"></a>
# **individualsPartyIdLicensesGet**
> List&lt;License&gt; individualsPartyIdLicensesGet(apiKey, partyId)

Retrieve a list of licenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsLicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsLicensesApi apiInstance = new IndividualsLicensesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      List<License> result = apiInstance.individualsPartyIdLicensesGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsLicensesApi#individualsPartyIdLicensesGet");
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

[**List&lt;License&gt;**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Licenses were retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdLicensesPost"></a>
# **individualsPartyIdLicensesPost**
> License individualsPartyIdLicensesPost(apiKey, partyId, license)

Create a license

Create a license 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsLicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsLicensesApi apiInstance = new IndividualsLicensesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    License license = new License(); // License | License resource
    try {
      License result = apiInstance.individualsPartyIdLicensesPost(apiKey, partyId, license);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsLicensesApi#individualsPartyIdLicensesPost");
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
| **license** | [**License**](License.md)| License resource | |

### Return type

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | License was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

<a id="individualsPartyIdLicensesProductIdDelete"></a>
# **individualsPartyIdLicensesProductIdDelete**
> individualsPartyIdLicensesProductIdDelete(apiKey, partyId, productId)

Delete a license

Delete a license 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsLicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsLicensesApi apiInstance = new IndividualsLicensesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String productId = "productId_example"; // String | The product identifier.
    try {
      apiInstance.individualsPartyIdLicensesProductIdDelete(apiKey, partyId, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsLicensesApi#individualsPartyIdLicensesProductIdDelete");
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
| **204** | License was deleted |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdLicensesProductIdGet"></a>
# **individualsPartyIdLicensesProductIdGet**
> License individualsPartyIdLicensesProductIdGet(apiKey, partyId, productId)

Retrieve a license

Retrieve a license 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsLicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsLicensesApi apiInstance = new IndividualsLicensesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String productId = "productId_example"; // String | The product identifier.
    try {
      License result = apiInstance.individualsPartyIdLicensesProductIdGet(apiKey, partyId, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsLicensesApi#individualsPartyIdLicensesProductIdGet");
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

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | License was retrieved successfully |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdLicensesProductIdPut"></a>
# **individualsPartyIdLicensesProductIdPut**
> License individualsPartyIdLicensesProductIdPut(apiKey, partyId, productId, license)

Update a license

Update a license 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsLicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsLicensesApi apiInstance = new IndividualsLicensesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String productId = "productId_example"; // String | The product identifier.
    License license = new License(); // License | License resource
    try {
      License result = apiInstance.individualsPartyIdLicensesProductIdPut(apiKey, partyId, productId, license);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsLicensesApi#individualsPartyIdLicensesProductIdPut");
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
| **license** | [**License**](License.md)| License resource | |

### Return type

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | License was updated |  -  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

