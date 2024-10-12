# VotesApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**votesGet**](VotesApi.md#votesGet) | **GET** /votes |  |
| [**votesPost**](VotesApi.md#votesPost) | **POST** /votes | update specified votes for a User |


<a id="votesGet"></a>
# **votesGet**
> List&lt;Vote&gt; votesGet(userId, featureId, positive, negative, offset, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    VotesApi apiInstance = new VotesApi(defaultClient);
    Integer userId = 56; // Integer | Include only votes by User that voted on a feature.
    Integer featureId = 56; // Integer | Include only votes for Feature with this Feature ID
    Boolean positive = true; // Boolean | Include only votes that are positive
    Boolean negative = true; // Boolean | Include only votes that are negative
    BigDecimal offset = new BigDecimal(78); // BigDecimal | Offset to start at
    BigDecimal limit = new BigDecimal(78); // BigDecimal | Limit the number of records returned
    try {
      List<Vote> result = apiInstance.votesGet(userId, featureId, positive, negative, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VotesApi#votesGet");
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
| **userId** | **Integer**| Include only votes by User that voted on a feature. | [optional] |
| **featureId** | **Integer**| Include only votes for Feature with this Feature ID | [optional] |
| **positive** | **Boolean**| Include only votes that are positive | [optional] |
| **negative** | **Boolean**| Include only votes that are negative | [optional] |
| **offset** | **BigDecimal**| Offset to start at | [optional] |
| **limit** | **BigDecimal**| Limit the number of records returned | [optional] |

### Return type

[**List&lt;Vote&gt;**](Vote.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vote records |  -  |

<a id="votesPost"></a>
# **votesPost**
> votesPost(data)

update specified votes for a User

Automatically subscribes/unsubscribes the User to the specifed feature depending on the quantity value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    VotesApi apiInstance = new VotesApi(defaultClient);
    VotesPostRequest data = new VotesPostRequest(); // VotesPostRequest | 
    try {
      apiInstance.votesPost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling VotesApi#votesPost");
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
| **data** | [**VotesPostRequest**](VotesPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated votes |  -  |

