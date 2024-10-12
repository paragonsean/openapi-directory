# AmazonPersonalizeRuntime.DefaultApi

All URIs are relative to *http://personalize-runtime.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPersonalizedRanking**](DefaultApi.md#getPersonalizedRanking) | **POST** /personalize-ranking | 
[**getRecommendations**](DefaultApi.md#getRecommendations) | **POST** /recommendations | 



## getPersonalizedRanking

> GetPersonalizedRankingResponse getPersonalizedRanking(getPersonalizedRankingRequest, opts)



&lt;p&gt;Re-ranks a list of recommended items for the given user. The first item in the list is deemed the most likely item to be of interest to the user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The solution backing the campaign must have been created using a recipe of type PERSONALIZED_RANKING.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonPersonalizeRuntime from 'amazon_personalize_runtime';
let defaultClient = AmazonPersonalizeRuntime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPersonalizeRuntime.DefaultApi();
let getPersonalizedRankingRequest = new AmazonPersonalizeRuntime.GetPersonalizedRankingRequest(); // GetPersonalizedRankingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPersonalizedRanking(getPersonalizedRankingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getPersonalizedRankingRequest** | [**GetPersonalizedRankingRequest**](GetPersonalizedRankingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPersonalizedRankingResponse**](GetPersonalizedRankingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRecommendations

> GetRecommendationsResponse getRecommendations(getRecommendationsRequest, opts)



&lt;p&gt;Returns a list of recommended items. For campaigns, the campaign&#39;s Amazon Resource Name (ARN) is required and the required user and item input depends on the recipe type used to create the solution backing the campaign as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;USER_PERSONALIZATION - &lt;code&gt;userId&lt;/code&gt; required, &lt;code&gt;itemId&lt;/code&gt; not used&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;RELATED_ITEMS - &lt;code&gt;itemId&lt;/code&gt; required, &lt;code&gt;userId&lt;/code&gt; not used&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Campaigns that are backed by a solution created using a recipe of type PERSONALIZED_RANKING use the API.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; For recommenders, the recommender&#39;s ARN is required and the required item and user input depends on the use case (domain-based recipe) backing the recommender. For information on use case requirements see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html\&quot;&gt;Choosing recommender use cases&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonPersonalizeRuntime from 'amazon_personalize_runtime';
let defaultClient = AmazonPersonalizeRuntime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPersonalizeRuntime.DefaultApi();
let getRecommendationsRequest = new AmazonPersonalizeRuntime.GetRecommendationsRequest(); // GetRecommendationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRecommendations(getRecommendationsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getRecommendationsRequest** | [**GetRecommendationsRequest**](GetRecommendationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRecommendationsResponse**](GetRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

