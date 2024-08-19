# GettyImages.AssetLicensingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3AssetLicensingAssetIdPost**](AssetLicensingApi.md#v3AssetLicensingAssetIdPost) | **POST** /v3/asset-licensing/{assetId} | Endpoint for acquiring extended licenses with iStock credits for an asset.



## v3AssetLicensingAssetIdPost

> AssetLicensingResponse v3AssetLicensingAssetIdPost(assetId, opts)

Endpoint for acquiring extended licenses with iStock credits for an asset.

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.AssetLicensingApi();
let assetId = "assetId_example"; // String | Getty Images assetId - examples 520621493, 112301284
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'acquireAssetLicensesRequest': new GettyImages.AcquireAssetLicensesRequest() // AcquireAssetLicensesRequest | Structure that specifies an array of LicenseTypes (multiseat, unlimited, resale, indemnification) to acquire,              and whether or not to use Team Credits. Authenticated User must have access to Team Credits if UseTeamCredits is set to \"true\".
};
apiInstance.v3AssetLicensingAssetIdPost(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| Getty Images assetId - examples 520621493, 112301284 | 
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **acquireAssetLicensesRequest** | [**AcquireAssetLicensesRequest**](AcquireAssetLicensesRequest.md)| Structure that specifies an array of LicenseTypes (multiseat, unlimited, resale, indemnification) to acquire,              and whether or not to use Team Credits. Authenticated User must have access to Team Credits if UseTeamCredits is set to \&quot;true\&quot;. | [optional] 

### Return type

[**AssetLicensingResponse**](AssetLicensingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

