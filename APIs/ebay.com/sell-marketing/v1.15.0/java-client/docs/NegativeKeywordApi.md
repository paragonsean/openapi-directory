# NegativeKeywordApi

All URIs are relative to *https://api.ebay.com/sell/marketing/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateNegativeKeyword**](NegativeKeywordApi.md#bulkCreateNegativeKeyword) | **POST** /bulk_create_negative_keyword |  |
| [**bulkUpdateNegativeKeyword**](NegativeKeywordApi.md#bulkUpdateNegativeKeyword) | **POST** /bulk_update_negative_keyword |  |
| [**createNegativeKeyword**](NegativeKeywordApi.md#createNegativeKeyword) | **POST** /negative_keyword |  |
| [**getNegativeKeyword**](NegativeKeywordApi.md#getNegativeKeyword) | **GET** /negative_keyword/{negative_keyword_id} |  |
| [**getNegativeKeywords**](NegativeKeywordApi.md#getNegativeKeywords) | **GET** /negative_keyword |  |
| [**updateNegativeKeyword**](NegativeKeywordApi.md#updateNegativeKeyword) | **PUT** /negative_keyword/{negative_keyword_id} |  |


<a id="bulkCreateNegativeKeyword"></a>
# **bulkCreateNegativeKeyword**
> BulkCreateNegativeKeywordResponse bulkCreateNegativeKeyword(bulkCreateNegativeKeywordRequest)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method adds negative keywords, in bulk, to an existing ad group in a PLA campaign that uses the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;campaignId&lt;/b&gt; and &lt;b&gt;adGroupId&lt;/b&gt; in the request body, along with the &lt;b&gt;negativeKeywordText&lt;/b&gt; and &lt;b&gt;negativeKeywordMatchType&lt;/b&gt;.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a specified seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegativeKeywordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/marketing/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    NegativeKeywordApi apiInstance = new NegativeKeywordApi(defaultClient);
    BulkCreateNegativeKeywordRequest bulkCreateNegativeKeywordRequest = new BulkCreateNegativeKeywordRequest(); // BulkCreateNegativeKeywordRequest | A type that defines the fields for the bulk request to create negative keywords.
    try {
      BulkCreateNegativeKeywordResponse result = apiInstance.bulkCreateNegativeKeyword(bulkCreateNegativeKeywordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegativeKeywordApi#bulkCreateNegativeKeyword");
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
| **bulkCreateNegativeKeywordRequest** | [**BulkCreateNegativeKeywordRequest**](BulkCreateNegativeKeywordRequest.md)| A type that defines the fields for the bulk request to create negative keywords. | |

### Return type

[**BulkCreateNegativeKeywordResponse**](BulkCreateNegativeKeywordResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **207** | Multi Status |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="bulkUpdateNegativeKeyword"></a>
# **bulkUpdateNegativeKeyword**
> BulkUpdateNegativeKeywordResponse bulkUpdateNegativeKeyword(bulkUpdateNegativeKeywordRequest)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method updates the statuses of existing negative keywords, in bulk.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;negativeKeywordId&lt;/b&gt; and &lt;b&gt;negativeKeywordStatus&lt;/b&gt; in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegativeKeywordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/marketing/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    NegativeKeywordApi apiInstance = new NegativeKeywordApi(defaultClient);
    BulkUpdateNegativeKeywordRequest bulkUpdateNegativeKeywordRequest = new BulkUpdateNegativeKeywordRequest(); // BulkUpdateNegativeKeywordRequest | A type that defines the fields for the bulk request to update negative keyword statuses.
    try {
      BulkUpdateNegativeKeywordResponse result = apiInstance.bulkUpdateNegativeKeyword(bulkUpdateNegativeKeywordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegativeKeywordApi#bulkUpdateNegativeKeyword");
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
| **bulkUpdateNegativeKeywordRequest** | [**BulkUpdateNegativeKeywordRequest**](BulkUpdateNegativeKeywordRequest.md)| A type that defines the fields for the bulk request to update negative keyword statuses. | |

### Return type

[**BulkUpdateNegativeKeywordResponse**](BulkUpdateNegativeKeywordResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **207** | Multi Status |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="createNegativeKeyword"></a>
# **createNegativeKeyword**
> Object createNegativeKeyword(createNegativeKeywordRequest)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method adds a negative keyword to an existing ad group in a PLA campaign that uses the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;campaignId&lt;/b&gt; and &lt;b&gt;adGroupId&lt;/b&gt; in the request body, along with the &lt;b&gt;negativeKeywordText&lt;/b&gt; and &lt;b&gt;negativeKeywordMatchType&lt;/b&gt;.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a specified seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegativeKeywordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/marketing/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    NegativeKeywordApi apiInstance = new NegativeKeywordApi(defaultClient);
    CreateNegativeKeywordRequest createNegativeKeywordRequest = new CreateNegativeKeywordRequest(); // CreateNegativeKeywordRequest | A type that defines the fields for the request to create a negative keyword.
    try {
      Object result = apiInstance.createNegativeKeyword(createNegativeKeywordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegativeKeywordApi#createNegativeKeyword");
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
| **createNegativeKeywordRequest** | [**CreateNegativeKeywordRequest**](CreateNegativeKeywordRequest.md)| A type that defines the fields for the request to create a negative keyword. | |

### Return type

**Object**

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location -  <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="getNegativeKeyword"></a>
# **getNegativeKeyword**
> NegativeKeyword getNegativeKeyword(negativeKeywordId)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method retrieves details on a specific negative keyword.&lt;br /&gt;&lt;br /&gt;In the request, specify the &lt;b&gt;negative_keyword_id&lt;/b&gt; as a path parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegativeKeywordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/marketing/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    NegativeKeywordApi apiInstance = new NegativeKeywordApi(defaultClient);
    String negativeKeywordId = "negativeKeywordId_example"; // String | The unique identifier for the negative keyword.<br /><br />This value is returned in the <b>Location</b> response header from the <a href=\"/api-docs/sell/marketing/resources/negative_keyword/methods/createNegativeKeyword\">createNegativeKeyword</a> method.
    try {
      NegativeKeyword result = apiInstance.getNegativeKeyword(negativeKeywordId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegativeKeywordApi#getNegativeKeyword");
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
| **negativeKeywordId** | **String**| The unique identifier for the negative keyword.&lt;br /&gt;&lt;br /&gt;This value is returned in the &lt;b&gt;Location&lt;/b&gt; response header from the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/negative_keyword/methods/createNegativeKeyword\&quot;&gt;createNegativeKeyword&lt;/a&gt; method. | |

### Return type

[**NegativeKeyword**](NegativeKeyword.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="getNegativeKeywords"></a>
# **getNegativeKeywords**
> NegativeKeywordPagedCollectionResponse getNegativeKeywords(adGroupIds, campaignIds, limit, negativeKeywordStatus, offset)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method can be used to retrieve all of the negative keywords for ad groups in PLA campaigns that use the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;The results can be filtered using the &lt;b&gt;campaign_ids&lt;/b&gt;, &lt;b&gt;ad_group_ids&lt;/b&gt;, and &lt;b&gt;negative_keyword_status&lt;/b&gt; query parameters.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegativeKeywordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/marketing/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    NegativeKeywordApi apiInstance = new NegativeKeywordApi(defaultClient);
    String adGroupIds = "adGroupIds_example"; // String | A comma-separated list of ad group IDs.<br /><br />This query parameter is used if the seller wants to retrieve the negative keywords from one or more specific ad groups. The results might not include these ad group IDs if other search conditions exclude them.<br /><br /><span class=\"tablenote\"><b>Note:</b>You can call the <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\">getAdGroups</a> method to retrieve the ad group IDs for a seller.</span><br /><br /><i>Required if</i> the search results must be filtered to include negative keywords created at the ad group level.
    String campaignIds = "campaignIds_example"; // String | A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.<br /><br />This query parameter is used if the seller wants to retrieve the negative keywords from a specific campaign. The results might not include these campaign IDs if other search conditions exclude them.<br /><br /><span class=\"tablenote\"><b>Note:</b> Currently, only one campaign ID value is supported for each request.</span>
    String limit = "limit_example"; // String | The number of results, from the current result set, to be returned in a single page.
    String negativeKeywordStatus = "negativeKeywordStatus_example"; // String | A comma-separated list of negative keyword statuses.<br /><br />This query parameter is used if the seller wants to filter the search results based on one or more negative keyword statuses.
    String offset = "offset_example"; // String | The number of results that will be skipped in the result set. This is used with the <b>limit</b> field to control the pagination of the output.<br /><br />For example, if the <b>offset</b> is set to <code>0</code> and the <b>limit</b> is set to <code>10</code>, the method will retrieve items 1 through 10 from the list of items returned. If the <b>offset</b> is set to <code>10</code> and the <b>limit</b> is set to <code>10</code>, the method will retrieve items 11 through 20 from the list of items returned.
    try {
      NegativeKeywordPagedCollectionResponse result = apiInstance.getNegativeKeywords(adGroupIds, campaignIds, limit, negativeKeywordStatus, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegativeKeywordApi#getNegativeKeywords");
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
| **adGroupIds** | **String**| A comma-separated list of ad group IDs.&lt;br /&gt;&lt;br /&gt;This query parameter is used if the seller wants to retrieve the negative keywords from one or more specific ad groups. The results might not include these ad group IDs if other search conditions exclude them.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;You can call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\&quot;&gt;getAdGroups&lt;/a&gt; method to retrieve the ad group IDs for a seller.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;i&gt;Required if&lt;/i&gt; the search results must be filtered to include negative keywords created at the ad group level. | [optional] |
| **campaignIds** | **String**| A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;This query parameter is used if the seller wants to retrieve the negative keywords from a specific campaign. The results might not include these campaign IDs if other search conditions exclude them.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Currently, only one campaign ID value is supported for each request.&lt;/span&gt; | [optional] |
| **limit** | **String**| The number of results, from the current result set, to be returned in a single page. | [optional] |
| **negativeKeywordStatus** | **String**| A comma-separated list of negative keyword statuses.&lt;br /&gt;&lt;br /&gt;This query parameter is used if the seller wants to filter the search results based on one or more negative keyword statuses. | [optional] |
| **offset** | **String**| The number of results that will be skipped in the result set. This is used with the &lt;b&gt;limit&lt;/b&gt; field to control the pagination of the output.&lt;br /&gt;&lt;br /&gt;For example, if the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;0&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 1 through 10 from the list of items returned. If the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 11 through 20 from the list of items returned. | [optional] |

### Return type

[**NegativeKeywordPagedCollectionResponse**](NegativeKeywordPagedCollectionResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateNegativeKeyword"></a>
# **updateNegativeKeyword**
> updateNegativeKeyword(negativeKeywordId, updateNegativeKeywordRequest)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method updates the status of an existing negative keyword.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;negative_keyword_id&lt;/b&gt; as a path parameter, and specify the &lt;b&gt;negativeKeywordStatus&lt;/b&gt; in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegativeKeywordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/marketing/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    NegativeKeywordApi apiInstance = new NegativeKeywordApi(defaultClient);
    String negativeKeywordId = "negativeKeywordId_example"; // String | The unique identifier for the negative keyword.<br /><br />This value is returned in the <b>Location</b> response header from the <a href=\"/api-docs/sell/marketing/resources/negative_keyword/methods/createNegativeKeyword\">createNegativeKeyword</a> method.
    UpdateNegativeKeywordRequest updateNegativeKeywordRequest = new UpdateNegativeKeywordRequest(); // UpdateNegativeKeywordRequest | A type that defines the fields for the request to update a negative keyword.
    try {
      apiInstance.updateNegativeKeyword(negativeKeywordId, updateNegativeKeywordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegativeKeywordApi#updateNegativeKeyword");
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
| **negativeKeywordId** | **String**| The unique identifier for the negative keyword.&lt;br /&gt;&lt;br /&gt;This value is returned in the &lt;b&gt;Location&lt;/b&gt; response header from the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/negative_keyword/methods/createNegativeKeyword\&quot;&gt;createNegativeKeyword&lt;/a&gt; method. | |
| **updateNegativeKeywordRequest** | [**UpdateNegativeKeywordRequest**](UpdateNegativeKeywordRequest.md)| A type that defines the fields for the request to update a negative keyword. | |

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Business error |  -  |
| **500** | Internal Server Error |  -  |

