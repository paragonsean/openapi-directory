# UtisControllerApi

All URIs are relative to *http://cybertaxonomy.eu/eu-bon/utis/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**capabilities**](UtisControllerApi.md#capabilities) | **GET** /capabilities | capabilities |
| [**search**](UtisControllerApi.md#search) | **GET** /search | search |


<a id="capabilities"></a>
# **capabilities**
> List&lt;ServiceProviderInfo&gt; capabilities()

capabilities

capabilities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtisControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cybertaxonomy.eu/eu-bon/utis/1.0");

    UtisControllerApi apiInstance = new UtisControllerApi(defaultClient);
    try {
      List<ServiceProviderInfo> result = apiInstance.capabilities();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtisControllerApi#capabilities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ServiceProviderInfo&gt;**](ServiceProviderInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="search"></a>
# **search**
> TnrMsg search(query, providers, searchMode, addSynonymy, timeout)

search

search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtisControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://cybertaxonomy.eu/eu-bon/utis/1.0");

    UtisControllerApi apiInstance = new UtisControllerApi(defaultClient);
    String query = "query_example"; // String | The scientific name to search for. For example: \"Bellis perennis\", \"Prionus\" or \"Bolinus brandaris\". This is an exact search so wildcard characters are not supported.
    String providers = "pesi,eunis,bgbm-cdm-server[col]"; // String | A list of provider id strings concatenated by comma characters. The default : \"pesi,bgbm-cdm-server[col]\" will be used if this parameter is not set. A list of all available provider ids can be obtained from the '/capabilities' service end point. Providers can be nested, that is a parent provider can have sub providers. If the id of the parent provider is supplied all subproviders will be queried. The query can also be restriced to one or more subproviders by using the following syntax: parent-id[sub-id-1,sub-id2,...]
    String searchMode = "scientificNameExact"; // String | Specifies the searchMode. Possible search modes are: scientificNameExact, scientificNameLike (begins with), vernacularNameExact, vernacularNameLike (contains), findByIdentifier. If the a provider does not support the chosen searchMode it will be skipped and the status message in the tnrClientStatus will be set to 'unsupported search mode' in this case.
    Boolean addSynonymy = false; // Boolean | Indicates whether the synonymy of the accepted taxon should be included into the response. Turning this option on may cause an increased response time.
    Long timeout = 0L; // Long | The maximum of milliseconds to wait for responses from any of the providers. If the timeout is exceeded the service will jut return the resonses that have been received so far. The default timeout is 0 ms (wait for ever)
    try {
      TnrMsg result = apiInstance.search(query, providers, searchMode, addSynonymy, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtisControllerApi#search");
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
| **query** | **String**| The scientific name to search for. For example: \&quot;Bellis perennis\&quot;, \&quot;Prionus\&quot; or \&quot;Bolinus brandaris\&quot;. This is an exact search so wildcard characters are not supported. | |
| **providers** | **String**| A list of provider id strings concatenated by comma characters. The default : \&quot;pesi,bgbm-cdm-server[col]\&quot; will be used if this parameter is not set. A list of all available provider ids can be obtained from the &#39;/capabilities&#39; service end point. Providers can be nested, that is a parent provider can have sub providers. If the id of the parent provider is supplied all subproviders will be queried. The query can also be restriced to one or more subproviders by using the following syntax: parent-id[sub-id-1,sub-id2,...] | [optional] [default to pesi,eunis,bgbm-cdm-server[col]] |
| **searchMode** | **String**| Specifies the searchMode. Possible search modes are: scientificNameExact, scientificNameLike (begins with), vernacularNameExact, vernacularNameLike (contains), findByIdentifier. If the a provider does not support the chosen searchMode it will be skipped and the status message in the tnrClientStatus will be set to &#39;unsupported search mode&#39; in this case. | [optional] [default to scientificNameExact] [enum: scientificNameExact, scientificNameLike, vernacularNameExact, vernacularNameLike, findByIdentifier] |
| **addSynonymy** | **Boolean**| Indicates whether the synonymy of the accepted taxon should be included into the response. Turning this option on may cause an increased response time. | [optional] [default to false] |
| **timeout** | **Long**| The maximum of milliseconds to wait for responses from any of the providers. If the timeout is exceeded the service will jut return the resonses that have been received so far. The default timeout is 0 ms (wait for ever) | [optional] [default to 0] |

### Return type

[**TnrMsg**](TnrMsg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

