# CampaignsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesCampaignsIdJsonGet**](CampaignsApi.md#resourcesCampaignsIdJsonGet) | **GET** /resources/campaigns/{id}.json | Get Campaign by ID |
| [**resourcesCampaignsIdMediaJsonGet**](CampaignsApi.md#resourcesCampaignsIdMediaJsonGet) | **GET** /resources/campaigns/{id}/media.json | Get MediaItems by Campaign ID |
| [**resourcesCampaignsIdSyndicateFormatGet**](CampaignsApi.md#resourcesCampaignsIdSyndicateFormatGet) | **GET** /resources/campaigns/{id}/syndicate.{format} | Get MediaItems for Campaign |
| [**resourcesCampaignsJsonGet**](CampaignsApi.md#resourcesCampaignsJsonGet) | **GET** /resources/campaigns.json | Get Campaigns |


<a id="resourcesCampaignsIdJsonGet"></a>
# **resourcesCampaignsIdJsonGet**
> CampaignWrapped resourcesCampaignsIdJsonGet(id)

Get Campaign by ID

Information about a specific campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    Long id = 56L; // Long | The id of the record to look up
    try {
      CampaignWrapped result = apiInstance.resourcesCampaignsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#resourcesCampaignsIdJsonGet");
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
| **id** | **Long**| The id of the record to look up | |

### Return type

[**CampaignWrapped**](CampaignWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Campaign identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesCampaignsIdMediaJsonGet"></a>
# **resourcesCampaignsIdMediaJsonGet**
> MediaItemWrapped resourcesCampaignsIdMediaJsonGet(id, sort, max, offset)

Get MediaItems by Campaign ID

Campaign Listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    Long id = 56L; // Long | The id of the campaign to find media items for
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | The offset of the records set to return for pagination
    try {
      MediaItemWrapped result = apiInstance.resourcesCampaignsIdMediaJsonGet(id, sort, max, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#resourcesCampaignsIdMediaJsonGet");
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
| **id** | **Long**| The id of the campaign to find media items for | |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| The offset of the records set to return for pagination | [optional] |

### Return type

[**MediaItemWrapped**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of MediaItems for the Campaign identified by the &#39;id&#39;. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesCampaignsIdSyndicateFormatGet"></a>
# **resourcesCampaignsIdSyndicateFormatGet**
> SyndicateMarshallerWrapped resourcesCampaignsIdSyndicateFormatGet(id, format, displayMethod)

Get MediaItems for Campaign

MediaItem

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    Long id = 56L; // Long | The id of the record to look up
    String format = "format_example"; // String | Automatically added
    String displayMethod = "displayMethod_example"; // String | Method used to render an html request. Accepts one: [mv, list, feed]
    try {
      SyndicateMarshallerWrapped result = apiInstance.resourcesCampaignsIdSyndicateFormatGet(id, format, displayMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#resourcesCampaignsIdSyndicateFormatGet");
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
| **id** | **Long**| The id of the record to look up | |
| **format** | **String**| Automatically added | |
| **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] |

### Return type

[**SyndicateMarshallerWrapped**](SyndicateMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Renders the list of MediaItems associated with the Tag identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesCampaignsJsonGet"></a>
# **resourcesCampaignsJsonGet**
> CampaignWrapped resourcesCampaignsJsonGet(max, offset, sort)

Get Campaigns

Media Listings for a specific campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | The offset of the records set to return for pagination
    String sort = "sort_example"; // String | * Set of fields to sort the records by.
    try {
      CampaignWrapped result = apiInstance.resourcesCampaignsJsonGet(max, offset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#resourcesCampaignsJsonGet");
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
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| The offset of the records set to return for pagination | [optional] |
| **sort** | **String**| * Set of fields to sort the records by. | [optional] |

### Return type

[**CampaignWrapped**](CampaignWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of Campaigns. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

