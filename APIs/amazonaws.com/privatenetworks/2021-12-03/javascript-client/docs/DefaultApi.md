# AwsPrivate5G.DefaultApi

All URIs are relative to *http://private-networks.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledgeOrderReceipt**](DefaultApi.md#acknowledgeOrderReceipt) | **POST** /v1/orders/acknowledge | 
[**activateDeviceIdentifier**](DefaultApi.md#activateDeviceIdentifier) | **POST** /v1/device-identifiers/activate | 
[**activateNetworkSite**](DefaultApi.md#activateNetworkSite) | **POST** /v1/network-sites/activate | 
[**configureAccessPoint**](DefaultApi.md#configureAccessPoint) | **POST** /v1/network-resources/configure | 
[**createNetwork**](DefaultApi.md#createNetwork) | **POST** /v1/networks | 
[**createNetworkSite**](DefaultApi.md#createNetworkSite) | **POST** /v1/network-sites | 
[**deactivateDeviceIdentifier**](DefaultApi.md#deactivateDeviceIdentifier) | **POST** /v1/device-identifiers/deactivate | 
[**deleteNetwork**](DefaultApi.md#deleteNetwork) | **DELETE** /v1/networks/{networkArn} | 
[**deleteNetworkSite**](DefaultApi.md#deleteNetworkSite) | **DELETE** /v1/network-sites/{networkSiteArn} | 
[**getDeviceIdentifier**](DefaultApi.md#getDeviceIdentifier) | **GET** /v1/device-identifiers/{deviceIdentifierArn} | 
[**getNetwork**](DefaultApi.md#getNetwork) | **GET** /v1/networks/{networkArn} | 
[**getNetworkResource**](DefaultApi.md#getNetworkResource) | **GET** /v1/network-resources/{networkResourceArn} | 
[**getNetworkSite**](DefaultApi.md#getNetworkSite) | **GET** /v1/network-sites/{networkSiteArn} | 
[**getOrder**](DefaultApi.md#getOrder) | **GET** /v1/orders/{orderArn} | 
[**listDeviceIdentifiers**](DefaultApi.md#listDeviceIdentifiers) | **POST** /v1/device-identifiers/list | 
[**listNetworkResources**](DefaultApi.md#listNetworkResources) | **POST** /v1/network-resources | 
[**listNetworkSites**](DefaultApi.md#listNetworkSites) | **POST** /v1/network-sites/list | 
[**listNetworks**](DefaultApi.md#listNetworks) | **POST** /v1/networks/list | 
[**listOrders**](DefaultApi.md#listOrders) | **POST** /v1/orders/list | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**ping**](DefaultApi.md#ping) | **GET** /ping | 
[**startNetworkResourceUpdate**](DefaultApi.md#startNetworkResourceUpdate) | **POST** /v1/network-resources/update | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateNetworkSite**](DefaultApi.md#updateNetworkSite) | **PUT** /v1/network-sites/site | 
[**updateNetworkSitePlan**](DefaultApi.md#updateNetworkSitePlan) | **PUT** /v1/network-sites/plan | 



## acknowledgeOrderReceipt

> AcknowledgeOrderReceiptResponse acknowledgeOrderReceipt(acknowledgeOrderReceiptRequest, opts)



Acknowledges that the specified network order was received.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let acknowledgeOrderReceiptRequest = new AwsPrivate5G.AcknowledgeOrderReceiptRequest(); // AcknowledgeOrderReceiptRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acknowledgeOrderReceipt(acknowledgeOrderReceiptRequest, opts, (error, data, response) => {
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
 **acknowledgeOrderReceiptRequest** | [**AcknowledgeOrderReceiptRequest**](AcknowledgeOrderReceiptRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AcknowledgeOrderReceiptResponse**](AcknowledgeOrderReceiptResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activateDeviceIdentifier

> ActivateDeviceIdentifierResponse activateDeviceIdentifier(activateDeviceIdentifierRequest, opts)



Activates the specified device identifier.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let activateDeviceIdentifierRequest = new AwsPrivate5G.ActivateDeviceIdentifierRequest(); // ActivateDeviceIdentifierRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.activateDeviceIdentifier(activateDeviceIdentifierRequest, opts, (error, data, response) => {
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
 **activateDeviceIdentifierRequest** | [**ActivateDeviceIdentifierRequest**](ActivateDeviceIdentifierRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ActivateDeviceIdentifierResponse**](ActivateDeviceIdentifierResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activateNetworkSite

> ActivateNetworkSiteResponse activateNetworkSite(activateNetworkSiteRequest, opts)



Activates the specified network site.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let activateNetworkSiteRequest = new AwsPrivate5G.ActivateNetworkSiteRequest(); // ActivateNetworkSiteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.activateNetworkSite(activateNetworkSiteRequest, opts, (error, data, response) => {
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
 **activateNetworkSiteRequest** | [**ActivateNetworkSiteRequest**](ActivateNetworkSiteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ActivateNetworkSiteResponse**](ActivateNetworkSiteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configureAccessPoint

> ConfigureAccessPointResponse configureAccessPoint(configureAccessPointRequest, opts)



&lt;p&gt;Configures the specified network resource. &lt;/p&gt; &lt;p&gt; Use this action to specify the geographic position of the hardware. You must provide Certified Professional Installer (CPI) credentials in the request so that we can obtain spectrum grants. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/private-networks/latest/userguide/radio-units.html\&quot;&gt;Radio units&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Private 5G User Guide&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let configureAccessPointRequest = new AwsPrivate5G.ConfigureAccessPointRequest(); // ConfigureAccessPointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.configureAccessPoint(configureAccessPointRequest, opts, (error, data, response) => {
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
 **configureAccessPointRequest** | [**ConfigureAccessPointRequest**](ConfigureAccessPointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ConfigureAccessPointResponse**](ConfigureAccessPointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetwork

> CreateNetworkResponse createNetwork(createNetworkRequest, opts)



Creates a network.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let createNetworkRequest = new AwsPrivate5G.CreateNetworkRequest(); // CreateNetworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createNetwork(createNetworkRequest, opts, (error, data, response) => {
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
 **createNetworkRequest** | [**CreateNetworkRequest**](CreateNetworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateNetworkResponse**](CreateNetworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSite

> CreateNetworkSiteResponse createNetworkSite(createNetworkSiteRequest, opts)



Creates a network site.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let createNetworkSiteRequest = new AwsPrivate5G.CreateNetworkSiteRequest(); // CreateNetworkSiteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createNetworkSite(createNetworkSiteRequest, opts, (error, data, response) => {
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
 **createNetworkSiteRequest** | [**CreateNetworkSiteRequest**](CreateNetworkSiteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateNetworkSiteResponse**](CreateNetworkSiteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivateDeviceIdentifier

> DeactivateDeviceIdentifierResponse deactivateDeviceIdentifier(activateDeviceIdentifierRequest, opts)



Deactivates the specified device identifier.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let activateDeviceIdentifierRequest = new AwsPrivate5G.ActivateDeviceIdentifierRequest(); // ActivateDeviceIdentifierRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deactivateDeviceIdentifier(activateDeviceIdentifierRequest, opts, (error, data, response) => {
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
 **activateDeviceIdentifierRequest** | [**ActivateDeviceIdentifierRequest**](ActivateDeviceIdentifierRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeactivateDeviceIdentifierResponse**](DeactivateDeviceIdentifierResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetwork

> DeleteNetworkResponse deleteNetwork(networkArn, opts)



Deletes the specified network. You must delete network sites before you delete the network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/private-networks/latest/APIReference/API_DeleteNetworkSite.html\&quot;&gt;DeleteNetworkSite&lt;/a&gt; in the &lt;i&gt;API Reference for Amazon Web Services Private 5G&lt;/i&gt;.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let networkArn = "networkArn_example"; // String | The Amazon Resource Name (ARN) of the network.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html\">How to ensure idempotency</a>.
};
apiInstance.deleteNetwork(networkArn, opts, (error, data, response) => {
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
 **networkArn** | **String**| The Amazon Resource Name (ARN) of the network. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html\&quot;&gt;How to ensure idempotency&lt;/a&gt;. | [optional] 

### Return type

[**DeleteNetworkResponse**](DeleteNetworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNetworkSite

> DeleteNetworkSiteResponse deleteNetworkSite(networkSiteArn, opts)



Deletes the specified network site. Return the hardware after you delete the network site. You are responsible for minimum charges. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/private-networks/latest/userguide/hardware-maintenance.html\&quot;&gt;Hardware returns&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Private 5G User Guide&lt;/i&gt;. 

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let networkSiteArn = "networkSiteArn_example"; // String | The Amazon Resource Name (ARN) of the network site.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html\">How to ensure idempotency</a>.
};
apiInstance.deleteNetworkSite(networkSiteArn, opts, (error, data, response) => {
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
 **networkSiteArn** | **String**| The Amazon Resource Name (ARN) of the network site. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html\&quot;&gt;How to ensure idempotency&lt;/a&gt;. | [optional] 

### Return type

[**DeleteNetworkSiteResponse**](DeleteNetworkSiteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceIdentifier

> GetDeviceIdentifierResponse getDeviceIdentifier(deviceIdentifierArn, opts)



Gets the specified device identifier.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let deviceIdentifierArn = "deviceIdentifierArn_example"; // String | The Amazon Resource Name (ARN) of the device identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeviceIdentifier(deviceIdentifierArn, opts, (error, data, response) => {
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
 **deviceIdentifierArn** | **String**| The Amazon Resource Name (ARN) of the device identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDeviceIdentifierResponse**](GetDeviceIdentifierResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetwork

> GetNetworkResponse getNetwork(networkArn, opts)



Gets the specified network.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let networkArn = "networkArn_example"; // String | The Amazon Resource Name (ARN) of the network.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getNetwork(networkArn, opts, (error, data, response) => {
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
 **networkArn** | **String**| The Amazon Resource Name (ARN) of the network. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetNetworkResponse**](GetNetworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkResource

> GetNetworkResourceResponse getNetworkResource(networkResourceArn, opts)



Gets the specified network resource.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let networkResourceArn = "networkResourceArn_example"; // String | The Amazon Resource Name (ARN) of the network resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getNetworkResource(networkResourceArn, opts, (error, data, response) => {
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
 **networkResourceArn** | **String**| The Amazon Resource Name (ARN) of the network resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetNetworkResourceResponse**](GetNetworkResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSite

> GetNetworkSiteResponse getNetworkSite(networkSiteArn, opts)



Gets the specified network site.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let networkSiteArn = "networkSiteArn_example"; // String | The Amazon Resource Name (ARN) of the network site.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getNetworkSite(networkSiteArn, opts, (error, data, response) => {
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
 **networkSiteArn** | **String**| The Amazon Resource Name (ARN) of the network site. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetNetworkSiteResponse**](GetNetworkSiteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrder

> GetOrderResponse getOrder(orderArn, opts)



Gets the specified order.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let orderArn = "orderArn_example"; // String | The Amazon Resource Name (ARN) of the order.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOrder(orderArn, opts, (error, data, response) => {
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
 **orderArn** | **String**| The Amazon Resource Name (ARN) of the order. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeviceIdentifiers

> ListDeviceIdentifiersResponse listDeviceIdentifiers(listDeviceIdentifiersRequest, opts)



&lt;p&gt;Lists device identifiers. Add filters to your request to return a more specific list of results. Use filters to match the Amazon Resource Name (ARN) of an order, the status of device identifiers, or the ARN of the traffic group.&lt;/p&gt; &lt;p&gt;If you specify multiple filters, filters are joined with an OR, and the request returns results that match all of the specified filters.&lt;/p&gt;

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let listDeviceIdentifiersRequest = new AwsPrivate5G.ListDeviceIdentifiersRequest(); // ListDeviceIdentifiersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'startToken': "startToken_example" // String | Pagination token
};
apiInstance.listDeviceIdentifiers(listDeviceIdentifiersRequest, opts, (error, data, response) => {
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
 **listDeviceIdentifiersRequest** | [**ListDeviceIdentifiersRequest**](ListDeviceIdentifiersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **startToken** | **String**| Pagination token | [optional] 

### Return type

[**ListDeviceIdentifiersResponse**](ListDeviceIdentifiersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listNetworkResources

> ListNetworkResourcesResponse listNetworkResources(listNetworkResourcesRequest, opts)



&lt;p&gt;Lists network resources. Add filters to your request to return a more specific list of results. Use filters to match the Amazon Resource Name (ARN) of an order or the status of network resources.&lt;/p&gt; &lt;p&gt;If you specify multiple filters, filters are joined with an OR, and the request returns results that match all of the specified filters.&lt;/p&gt;

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let listNetworkResourcesRequest = new AwsPrivate5G.ListNetworkResourcesRequest(); // ListNetworkResourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'startToken': "startToken_example" // String | Pagination token
};
apiInstance.listNetworkResources(listNetworkResourcesRequest, opts, (error, data, response) => {
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
 **listNetworkResourcesRequest** | [**ListNetworkResourcesRequest**](ListNetworkResourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **startToken** | **String**| Pagination token | [optional] 

### Return type

[**ListNetworkResourcesResponse**](ListNetworkResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listNetworkSites

> ListNetworkSitesResponse listNetworkSites(listNetworkSitesRequest, opts)



Lists network sites. Add filters to your request to return a more specific list of results. Use filters to match the status of the network site.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let listNetworkSitesRequest = new AwsPrivate5G.ListNetworkSitesRequest(); // ListNetworkSitesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'startToken': "startToken_example" // String | Pagination token
};
apiInstance.listNetworkSites(listNetworkSitesRequest, opts, (error, data, response) => {
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
 **listNetworkSitesRequest** | [**ListNetworkSitesRequest**](ListNetworkSitesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **startToken** | **String**| Pagination token | [optional] 

### Return type

[**ListNetworkSitesResponse**](ListNetworkSitesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listNetworks

> ListNetworksResponse listNetworks(listNetworksRequest, opts)



Lists networks. Add filters to your request to return a more specific list of results. Use filters to match the status of the network.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let listNetworksRequest = new AwsPrivate5G.ListNetworksRequest(); // ListNetworksRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'startToken': "startToken_example" // String | Pagination token
};
apiInstance.listNetworks(listNetworksRequest, opts, (error, data, response) => {
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
 **listNetworksRequest** | [**ListNetworksRequest**](ListNetworksRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **startToken** | **String**| Pagination token | [optional] 

### Return type

[**ListNetworksResponse**](ListNetworksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOrders

> ListOrdersResponse listOrders(listOrdersRequest, opts)



&lt;p&gt;Lists orders. Add filters to your request to return a more specific list of results. Use filters to match the Amazon Resource Name (ARN) of the network site or the status of the order.&lt;/p&gt; &lt;p&gt;If you specify multiple filters, filters are joined with an OR, and the request returns results that match all of the specified filters.&lt;/p&gt;

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let listOrdersRequest = new AwsPrivate5G.ListOrdersRequest(); // ListOrdersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'startToken': "startToken_example" // String | Pagination token
};
apiInstance.listOrders(listOrdersRequest, opts, (error, data, response) => {
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
 **listOrdersRequest** | [**ListOrdersRequest**](ListOrdersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **startToken** | **String**| Pagination token | [optional] 

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags for the specified resource.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ping

> PingResponse ping(opts)



Checks the health of the service.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.ping(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startNetworkResourceUpdate

> StartNetworkResourceUpdateResponse startNetworkResourceUpdate(startNetworkResourceUpdateRequest, opts)



&lt;p&gt;Use this action to do the following tasks:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update the duration and renewal status of the commitment period for a radio unit. The update goes into effect immediately.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Request a replacement for a network resource.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Request that you return a network resource.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you submit a request to replace or return a network resource, the status of the network resource changes to &lt;code&gt;CREATING_SHIPPING_LABEL&lt;/code&gt;. The shipping label is available when the status of the network resource is &lt;code&gt;PENDING_RETURN&lt;/code&gt;. After the network resource is successfully returned, its status changes to &lt;code&gt;DELETED&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/private-networks/latest/userguide/radio-units.html#return-radio-unit\&quot;&gt;Return a radio unit&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let startNetworkResourceUpdateRequest = new AwsPrivate5G.StartNetworkResourceUpdateRequest(); // StartNetworkResourceUpdateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startNetworkResourceUpdate(startNetworkResourceUpdateRequest, opts, (error, data, response) => {
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
 **startNetworkResourceUpdateRequest** | [**StartNetworkResourceUpdateRequest**](StartNetworkResourceUpdateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartNetworkResourceUpdateResponse**](StartNetworkResourceUpdateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



 Adds tags to the specified resource. 

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the resource. 
let tagResourceRequest = new AwsPrivate5G.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the resource.  | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes tags from the specified resource.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagKeys = ["null"]; // [String] | The tag keys.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSite

> UpdateNetworkSiteResponse updateNetworkSite(updateNetworkSiteRequest, opts)



Updates the specified network site.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let updateNetworkSiteRequest = new AwsPrivate5G.UpdateNetworkSiteRequest(); // UpdateNetworkSiteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateNetworkSite(updateNetworkSiteRequest, opts, (error, data, response) => {
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
 **updateNetworkSiteRequest** | [**UpdateNetworkSiteRequest**](UpdateNetworkSiteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateNetworkSiteResponse**](UpdateNetworkSiteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSitePlan

> UpdateNetworkSiteResponse updateNetworkSitePlan(updateNetworkSitePlanRequest, opts)



Updates the specified network site plan.

### Example

```javascript
import AwsPrivate5G from 'aws_private_5_g';
let defaultClient = AwsPrivate5G.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPrivate5G.DefaultApi();
let updateNetworkSitePlanRequest = new AwsPrivate5G.UpdateNetworkSitePlanRequest(); // UpdateNetworkSitePlanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateNetworkSitePlan(updateNetworkSitePlanRequest, opts, (error, data, response) => {
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
 **updateNetworkSitePlanRequest** | [**UpdateNetworkSitePlanRequest**](UpdateNetworkSitePlanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateNetworkSiteResponse**](UpdateNetworkSiteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

