# MatchReceivedSkusApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**match**](MatchReceivedSkusApi.md#match) | **PUT** /suggestions/{sellerId}/{sellerskuid}/versions/{version}/matches/{matchid} | Match Received SKUs individually |
| [**matchMultiple**](MatchReceivedSkusApi.md#matchMultiple) | **PUT** /suggestions/matches/action/{actionName} | Match Multiple Received SKUs |


<a id="match"></a>
# **match**
> match(accountName, accept, contentType, sellerId, sellerskuid, version, matchid, matchRequest)

Match Received SKUs individually

All SKUs sent from a seller to a marketplace must be reviewed and matched. Actions in the matching process are added in the request body through the [matchType] object. Match type actions include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;itemMatch&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productMatch&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.   5. &#x60;pending&#x60;: the received SKU requires attention.   6. &#x60;incomplete&#x60;: the received SKU is lacking information to be matched.   7. &#x60;insufficientScore&#x60;: the score given by the Matcher to this received SKU doesn&#39;t qualify it to be matched.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchReceivedSkusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MatchReceivedSkusApi apiInstance = new MatchReceivedSkusApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    String sellerskuid = "1234"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    String version = "09072021142808277"; // String | Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the versionId associated to the version you choose to search for. You can get this field's value through the[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the `latestVersionId` field.
    String matchid = "matchid_example"; // String | Whenever an SKU suggestion is matched, it is associated to a unique ID. Fill in this field with the matchId you wish to filter by. The `matchId`'s value can be obtained through the *[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint.
    MatchRequest matchRequest = new MatchRequest(); // MatchRequest | 
    try {
      apiInstance.match(accountName, accept, contentType, sellerId, sellerskuid, version, matchid, matchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchReceivedSkusApi#match");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to seller123] |
| **sellerskuid** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to 1234] |
| **version** | **String**| Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the versionId associated to the version you choose to search for. You can get this field&#39;s value through the[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the &#x60;latestVersionId&#x60; field. | [default to 09072021142808277] |
| **matchid** | **String**| Whenever an SKU suggestion is matched, it is associated to a unique ID. Fill in this field with the matchId you wish to filter by. The &#x60;matchId&#x60;&#39;s value can be obtained through the *[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint. | |
| **matchRequest** | [**MatchRequest**](MatchRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="matchMultiple"></a>
# **matchMultiple**
> matchMultiple(accountName, contentType, accept, actionName, requestBody)

Match Multiple Received SKUs

This endpoint allows the user to bulk approve, deny, or associate received SKUs. In a single request, you can match up to 25 received SKUs from your sellers.  Through the &#x60;actionName&#x60; attribute you can select the operation you want to apply to the received SKU.   Actions include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;skuassociation&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productassociation&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchReceivedSkusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MatchReceivedSkusApi apiInstance = new MatchReceivedSkusApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String actionName = "newprodcut"; // String | This field refers to the operation you choose to apply to received SKUs. Values include: newproduct, skuassociation, productassociation or deny.
    List<List<Object>> requestBody = Arrays.asList(new ArrayList<>()); // List<List<Object>> | 
    try {
      apiInstance.matchMultiple(accountName, contentType, accept, actionName, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchReceivedSkusApi#matchMultiple");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to apiexamples] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **actionName** | **String**| This field refers to the operation you choose to apply to received SKUs. Values include: newproduct, skuassociation, productassociation or deny. | [default to newprodcut] |
| **requestBody** | [**List&lt;List&lt;Object&gt;&gt;**](List.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

