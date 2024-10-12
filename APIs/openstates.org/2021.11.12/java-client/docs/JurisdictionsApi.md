# JurisdictionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jurisdictionDetailJurisdictionsJurisdictionIdGet**](JurisdictionsApi.md#jurisdictionDetailJurisdictionsJurisdictionIdGet) | **GET** /jurisdictions/{jurisdiction_id} | Jurisdiction Detail |
| [**jurisdictionListJurisdictionsGet**](JurisdictionsApi.md#jurisdictionListJurisdictionsGet) | **GET** /jurisdictions | Jurisdiction List |


<a id="jurisdictionDetailJurisdictionsJurisdictionIdGet"></a>
# **jurisdictionDetailJurisdictionsJurisdictionIdGet**
> Jurisdiction jurisdictionDetailJurisdictionsJurisdictionIdGet(jurisdictionId, include, apikey, xApiKey)

Jurisdiction Detail

Get details on a single Jurisdiction (e.g. state or municipality).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JurisdictionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    JurisdictionsApi apiInstance = new JurisdictionsApi(defaultClient);
    String jurisdictionId = "jurisdictionId_example"; // String | 
    List<JurisdictionInclude> include = Arrays.asList(); // List<JurisdictionInclude> | Additional includes for the Jurisdiction response.
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      Jurisdiction result = apiInstance.jurisdictionDetailJurisdictionsJurisdictionIdGet(jurisdictionId, include, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JurisdictionsApi#jurisdictionDetailJurisdictionsJurisdictionIdGet");
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
| **jurisdictionId** | **String**|  | |
| **include** | [**List&lt;JurisdictionInclude&gt;**](JurisdictionInclude.md)| Additional includes for the Jurisdiction response. | [optional] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**Jurisdiction**](Jurisdiction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="jurisdictionListJurisdictionsGet"></a>
# **jurisdictionListJurisdictionsGet**
> JurisdictionList jurisdictionListJurisdictionsGet(classification, include, page, perPage, apikey, xApiKey)

Jurisdiction List

Get list of supported Jurisdictions, a Jurisdiction is a state or municipality.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JurisdictionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    JurisdictionsApi apiInstance = new JurisdictionsApi(defaultClient);
    JurisdictionClassification classification = JurisdictionClassification.fromValue("state"); // JurisdictionClassification | Filter returned jurisdictions by type.
    List<JurisdictionInclude> include = Arrays.asList(); // List<JurisdictionInclude> | Additional information to include in response.
    Integer page = 1; // Integer | 
    Integer perPage = 52; // Integer | 
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      JurisdictionList result = apiInstance.jurisdictionListJurisdictionsGet(classification, include, page, perPage, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JurisdictionsApi#jurisdictionListJurisdictionsGet");
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
| **classification** | [**JurisdictionClassification**](.md)| Filter returned jurisdictions by type. | [optional] [enum: state, municipality, country] |
| **include** | [**List&lt;JurisdictionInclude&gt;**](JurisdictionInclude.md)| Additional information to include in response. | [optional] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 52] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**JurisdictionList**](JurisdictionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

