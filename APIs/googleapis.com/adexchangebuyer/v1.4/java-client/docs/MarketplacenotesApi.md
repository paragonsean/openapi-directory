# MarketplacenotesApi

All URIs are relative to *https://www.googleapis.com/adexchangebuyer/v1.4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adexchangebuyerMarketplacenotesInsert**](MarketplacenotesApi.md#adexchangebuyerMarketplacenotesInsert) | **POST** /proposals/{proposalId}/notes/insert |  |
| [**adexchangebuyerMarketplacenotesList**](MarketplacenotesApi.md#adexchangebuyerMarketplacenotesList) | **GET** /proposals/{proposalId}/notes |  |


<a id="adexchangebuyerMarketplacenotesInsert"></a>
# **adexchangebuyerMarketplacenotesInsert**
> AddOrderNotesResponse adexchangebuyerMarketplacenotesInsert(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, addOrderNotesRequest)



Add notes to the proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacenotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adexchangebuyer/v1.4");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacenotesApi apiInstance = new MarketplacenotesApi(defaultClient);
    String proposalId = "proposalId_example"; // String | The proposalId to add notes for.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AddOrderNotesRequest addOrderNotesRequest = new AddOrderNotesRequest(); // AddOrderNotesRequest | 
    try {
      AddOrderNotesResponse result = apiInstance.adexchangebuyerMarketplacenotesInsert(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, addOrderNotesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacenotesApi#adexchangebuyerMarketplacenotesInsert");
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
| **proposalId** | **String**| The proposalId to add notes for. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **addOrderNotesRequest** | [**AddOrderNotesRequest**](AddOrderNotesRequest.md)|  | [optional] |

### Return type

[**AddOrderNotesResponse**](AddOrderNotesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adexchangebuyerMarketplacenotesList"></a>
# **adexchangebuyerMarketplacenotesList**
> GetOrderNotesResponse adexchangebuyerMarketplacenotesList(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, pqlQuery)



Get all the notes associated with a proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacenotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adexchangebuyer/v1.4");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacenotesApi apiInstance = new MarketplacenotesApi(defaultClient);
    String proposalId = "proposalId_example"; // String | The proposalId to get notes for. To search across all proposals specify order_id = '-' as part of the URL.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String pqlQuery = "pqlQuery_example"; // String | Query string to retrieve specific notes. To search the text contents of notes, please use syntax like \"WHERE note.note = \"foo\" or \"WHERE note.note LIKE \"%bar%\"
    try {
      GetOrderNotesResponse result = apiInstance.adexchangebuyerMarketplacenotesList(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, pqlQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacenotesApi#adexchangebuyerMarketplacenotesList");
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
| **proposalId** | **String**| The proposalId to get notes for. To search across all proposals specify order_id &#x3D; &#39;-&#39; as part of the URL. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **pqlQuery** | **String**| Query string to retrieve specific notes. To search the text contents of notes, please use syntax like \&quot;WHERE note.note &#x3D; \&quot;foo\&quot; or \&quot;WHERE note.note LIKE \&quot;%bar%\&quot; | [optional] |

### Return type

[**GetOrderNotesResponse**](GetOrderNotesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

