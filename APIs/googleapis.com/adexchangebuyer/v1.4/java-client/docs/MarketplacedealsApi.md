# MarketplacedealsApi

All URIs are relative to *https://www.googleapis.com/adexchangebuyer/v1.4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adexchangebuyerMarketplacedealsDelete**](MarketplacedealsApi.md#adexchangebuyerMarketplacedealsDelete) | **POST** /proposals/{proposalId}/deals/delete |  |
| [**adexchangebuyerMarketplacedealsInsert**](MarketplacedealsApi.md#adexchangebuyerMarketplacedealsInsert) | **POST** /proposals/{proposalId}/deals/insert |  |
| [**adexchangebuyerMarketplacedealsList**](MarketplacedealsApi.md#adexchangebuyerMarketplacedealsList) | **GET** /proposals/{proposalId}/deals |  |
| [**adexchangebuyerMarketplacedealsUpdate**](MarketplacedealsApi.md#adexchangebuyerMarketplacedealsUpdate) | **POST** /proposals/{proposalId}/deals/update |  |


<a id="adexchangebuyerMarketplacedealsDelete"></a>
# **adexchangebuyerMarketplacedealsDelete**
> DeleteOrderDealsResponse adexchangebuyerMarketplacedealsDelete(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, deleteOrderDealsRequest)



Delete the specified deals from the proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacedealsApi;

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

    MarketplacedealsApi apiInstance = new MarketplacedealsApi(defaultClient);
    String proposalId = "proposalId_example"; // String | The proposalId to delete deals from.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    DeleteOrderDealsRequest deleteOrderDealsRequest = new DeleteOrderDealsRequest(); // DeleteOrderDealsRequest | 
    try {
      DeleteOrderDealsResponse result = apiInstance.adexchangebuyerMarketplacedealsDelete(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, deleteOrderDealsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacedealsApi#adexchangebuyerMarketplacedealsDelete");
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
| **proposalId** | **String**| The proposalId to delete deals from. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **deleteOrderDealsRequest** | [**DeleteOrderDealsRequest**](DeleteOrderDealsRequest.md)|  | [optional] |

### Return type

[**DeleteOrderDealsResponse**](DeleteOrderDealsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adexchangebuyerMarketplacedealsInsert"></a>
# **adexchangebuyerMarketplacedealsInsert**
> AddOrderDealsResponse adexchangebuyerMarketplacedealsInsert(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, addOrderDealsRequest)



Add new deals for the specified proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacedealsApi;

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

    MarketplacedealsApi apiInstance = new MarketplacedealsApi(defaultClient);
    String proposalId = "proposalId_example"; // String | proposalId for which deals need to be added.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AddOrderDealsRequest addOrderDealsRequest = new AddOrderDealsRequest(); // AddOrderDealsRequest | 
    try {
      AddOrderDealsResponse result = apiInstance.adexchangebuyerMarketplacedealsInsert(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, addOrderDealsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacedealsApi#adexchangebuyerMarketplacedealsInsert");
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
| **proposalId** | **String**| proposalId for which deals need to be added. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **addOrderDealsRequest** | [**AddOrderDealsRequest**](AddOrderDealsRequest.md)|  | [optional] |

### Return type

[**AddOrderDealsResponse**](AddOrderDealsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adexchangebuyerMarketplacedealsList"></a>
# **adexchangebuyerMarketplacedealsList**
> GetOrderDealsResponse adexchangebuyerMarketplacedealsList(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, pqlQuery)



List all the deals for a given proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacedealsApi;

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

    MarketplacedealsApi apiInstance = new MarketplacedealsApi(defaultClient);
    String proposalId = "proposalId_example"; // String | The proposalId to get deals for. To search across all proposals specify order_id = '-' as part of the URL.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String pqlQuery = "pqlQuery_example"; // String | Query string to retrieve specific deals.
    try {
      GetOrderDealsResponse result = apiInstance.adexchangebuyerMarketplacedealsList(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, pqlQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacedealsApi#adexchangebuyerMarketplacedealsList");
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
| **proposalId** | **String**| The proposalId to get deals for. To search across all proposals specify order_id &#x3D; &#39;-&#39; as part of the URL. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **pqlQuery** | **String**| Query string to retrieve specific deals. | [optional] |

### Return type

[**GetOrderDealsResponse**](GetOrderDealsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adexchangebuyerMarketplacedealsUpdate"></a>
# **adexchangebuyerMarketplacedealsUpdate**
> EditAllOrderDealsResponse adexchangebuyerMarketplacedealsUpdate(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, editAllOrderDealsRequest)



Replaces all the deals in the proposal with the passed in deals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacedealsApi;

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

    MarketplacedealsApi apiInstance = new MarketplacedealsApi(defaultClient);
    String proposalId = "proposalId_example"; // String | The proposalId to edit deals on.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    EditAllOrderDealsRequest editAllOrderDealsRequest = new EditAllOrderDealsRequest(); // EditAllOrderDealsRequest | 
    try {
      EditAllOrderDealsResponse result = apiInstance.adexchangebuyerMarketplacedealsUpdate(proposalId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, editAllOrderDealsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacedealsApi#adexchangebuyerMarketplacedealsUpdate");
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
| **proposalId** | **String**| The proposalId to edit deals on. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **editAllOrderDealsRequest** | [**EditAllOrderDealsRequest**](EditAllOrderDealsRequest.md)|  | [optional] |

### Return type

[**EditAllOrderDealsResponse**](EditAllOrderDealsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

