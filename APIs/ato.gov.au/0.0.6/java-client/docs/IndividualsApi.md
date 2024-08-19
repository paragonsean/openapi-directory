# IndividualsApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**individualsGet**](IndividualsApi.md#individualsGet) | **GET** /individuals | Retrieve a list of individuals |
| [**individualsPartyIdDelete**](IndividualsApi.md#individualsPartyIdDelete) | **DELETE** /individuals/{partyId} | Delete an individual |
| [**individualsPartyIdGet**](IndividualsApi.md#individualsPartyIdGet) | **GET** /individuals/{partyId} | Retrieve an individual |
| [**individualsPartyIdPut**](IndividualsApi.md#individualsPartyIdPut) | **PUT** /individuals/{partyId} | Update an individual |
| [**individualsPost**](IndividualsApi.md#individualsPost) | **POST** /individuals | Create an individual |


<a id="individualsGet"></a>
# **individualsGet**
> List&lt;Individual&gt; individualsGet(apiKey, dateOfBirth, placeOfBirth)

Retrieve a list of individuals

Retrieve a list of individuals 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsApi apiInstance = new IndividualsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String dateOfBirth = "dateOfBirth_example"; // String | The individual's date of birth, for example, `1979-01-13` (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format).
    String placeOfBirth = "placeOfBirth_example"; // String | The individual's place of birth, for example, `Tamworth`.
    try {
      List<Individual> result = apiInstance.individualsGet(apiKey, dateOfBirth, placeOfBirth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsApi#individualsGet");
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
| **dateOfBirth** | **String**| The individual&#39;s date of birth, for example, &#x60;1979-01-13&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format). | [optional] |
| **placeOfBirth** | **String**| The individual&#39;s place of birth, for example, &#x60;Tamworth&#x60;. | [optional] |

### Return type

[**List&lt;Individual&gt;**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of individuals was retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdDelete"></a>
# **individualsPartyIdDelete**
> individualsPartyIdDelete(apiKey, partyId)

Delete an individual

Delete an individual with the specified identifier 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsApi apiInstance = new IndividualsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      apiInstance.individualsPartyIdDelete(apiKey, partyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsApi#individualsPartyIdDelete");
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
| **204** | Individual was deleted |  -  |
| **400** | Request can not be executed in the current system state |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPartyIdGet"></a>
# **individualsPartyIdGet**
> Individual individualsPartyIdGet(apiKey, partyId)

Retrieve an individual

Retrieve an individual with the specified identifier 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsApi apiInstance = new IndividualsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      Individual result = apiInstance.individualsPartyIdGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsApi#individualsPartyIdGet");
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

[**Individual**](Individual.md)

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

<a id="individualsPartyIdPut"></a>
# **individualsPartyIdPut**
> Individual individualsPartyIdPut(apiKey, partyId, individual)

Update an individual

Update an individual 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsApi apiInstance = new IndividualsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    Individual individual = new Individual(); // Individual | Individual resource
    try {
      Individual result = apiInstance.individualsPartyIdPut(apiKey, partyId, individual);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsApi#individualsPartyIdPut");
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
| **individual** | [**Individual**](Individual.md)| Individual resource | |

### Return type

[**Individual**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Individual was updated |  -  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="individualsPost"></a>
# **individualsPost**
> Individual individualsPost(apiKey, individual)

Create an individual

Create an individual 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    IndividualsApi apiInstance = new IndividualsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    Individual individual = new Individual(); // Individual | Individual resource
    try {
      Individual result = apiInstance.individualsPost(apiKey, individual);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualsApi#individualsPost");
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
| **individual** | [**Individual**](Individual.md)| Individual resource | |

### Return type

[**Individual**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Individual was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

