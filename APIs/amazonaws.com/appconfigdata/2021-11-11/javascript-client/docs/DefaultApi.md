# AwsAppConfigData.DefaultApi

All URIs are relative to *http://appconfigdata.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLatestConfiguration**](DefaultApi.md#getLatestConfiguration) | **GET** /configuration#configuration_token | 
[**startConfigurationSession**](DefaultApi.md#startConfigurationSession) | **POST** /configurationsessions | 



## getLatestConfiguration

> GetLatestConfigurationResponse getLatestConfiguration(configurationToken, opts)



&lt;p&gt;Retrieves the latest deployed configuration. This API may return empty configuration data if the client already has the latest version. For more information about this API action and to view example CLI commands that show how to use it with the &lt;a&gt;StartConfigurationSession&lt;/a&gt; API action, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\&quot;&gt;Retrieving the configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Note the following important information.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Each configuration token is only valid for one call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;. The &lt;code&gt;GetLatestConfiguration&lt;/code&gt; response includes a &lt;code&gt;NextPollConfigurationToken&lt;/code&gt; that should always replace the token used for the just-completed call in preparation for the next one. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetLatestConfiguration&lt;/code&gt; is a priced call. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/systems-manager/pricing/\&quot;&gt;Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt;

### Example

```javascript
import AwsAppConfigData from 'aws_app_config_data';
let defaultClient = AwsAppConfigData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppConfigData.DefaultApi();
let configurationToken = "configurationToken_example"; // String | <p>Token describing the current state of the configuration session. To obtain a token, first call the <a>StartConfigurationSession</a> API. Note that every call to <code>GetLatestConfiguration</code> will return a new <code>ConfigurationToken</code> (<code>NextPollConfigurationToken</code> in the response) and <i>must</i> be provided to subsequent <code>GetLatestConfiguration</code> API calls.</p> <important> <p>This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a <code>GetLatestConfiguration</code> call uses an expired token, the system returns <code>BadRequestException</code>.</p> </important>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLatestConfiguration(configurationToken, opts, (error, data, response) => {
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
 **configurationToken** | **String**| &lt;p&gt;Token describing the current state of the configuration session. To obtain a token, first call the &lt;a&gt;StartConfigurationSession&lt;/a&gt; API. Note that every call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt; will return a new &lt;code&gt;ConfigurationToken&lt;/code&gt; (&lt;code&gt;NextPollConfigurationToken&lt;/code&gt; in the response) and &lt;i&gt;must&lt;/i&gt; be provided to subsequent &lt;code&gt;GetLatestConfiguration&lt;/code&gt; API calls.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a &lt;code&gt;GetLatestConfiguration&lt;/code&gt; call uses an expired token, the system returns &lt;code&gt;BadRequestException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLatestConfigurationResponse**](GetLatestConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startConfigurationSession

> StartConfigurationSessionResponse startConfigurationSession(startConfigurationSessionRequest, opts)



Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the &lt;a&gt;GetLatestConfiguration&lt;/a&gt; API action, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\&quot;&gt;Retrieving the configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;. 

### Example

```javascript
import AwsAppConfigData from 'aws_app_config_data';
let defaultClient = AwsAppConfigData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppConfigData.DefaultApi();
let startConfigurationSessionRequest = new AwsAppConfigData.StartConfigurationSessionRequest(); // StartConfigurationSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startConfigurationSession(startConfigurationSessionRequest, opts, (error, data, response) => {
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
 **startConfigurationSessionRequest** | [**StartConfigurationSessionRequest**](StartConfigurationSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartConfigurationSessionResponse**](StartConfigurationSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

