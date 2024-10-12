# PromotionsTaxesApi.CampaignAudiencesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcampaignaudiences**](CampaignAudiencesApi.md#getcampaignaudiences) | **GET** /api/rnb/pvt/campaignConfiguration | Get all campaign audiences
[**getcampaignconfiguration**](CampaignAudiencesApi.md#getcampaignconfiguration) | **GET** /api/rnb/pvt/campaignConfiguration/{campaignId} | Get campaign audience configuration
[**setcampaignconfiguration**](CampaignAudiencesApi.md#setcampaignconfiguration) | **POST** /api/rnb/pvt/campaignConfiguration | Create campaign audience



## getcampaignaudiences

> [Getcampaignaudiences200ResponseInner] getcampaignaudiences(contentType, accept)

Get all campaign audiences

Retrieves a list of all campaign audiences and their respective configurations.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.CampaignAudiencesApi();
let contentType = "application/json"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getcampaignaudiences(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**[Getcampaignaudiences200ResponseInner]**](Getcampaignaudiences200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getcampaignconfiguration

> Getcampaignconfiguration200Response getcampaignconfiguration(contentType, accept, campaignId)

Get campaign audience configuration

Retrieves a specific campaign audience configuration by its ID. This API uses the campaign ID, not the campaign name.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.CampaignAudiencesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let campaignId = "dd270d06-1ed1-47fc-b04e-a2431121b5a4"; // String | Campaign audience unique identifier.
apiInstance.getcampaignconfiguration(contentType, accept, campaignId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **campaignId** | **String**| Campaign audience unique identifier. | 

### Return type

[**Getcampaignconfiguration200Response**](Getcampaignconfiguration200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setcampaignconfiguration

> Setcampaignconfiguration200Response setcampaignconfiguration(contentType, accept, setcampaignconfigurationRequest)

Create campaign audience

Creates a new campaign audience.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.CampaignAudiencesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let setcampaignconfigurationRequest = new PromotionsTaxesApi.SetcampaignconfigurationRequest(); // SetcampaignconfigurationRequest | 
apiInstance.setcampaignconfiguration(contentType, accept, setcampaignconfigurationRequest, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **setcampaignconfigurationRequest** | [**SetcampaignconfigurationRequest**](SetcampaignconfigurationRequest.md)|  | 

### Return type

[**Setcampaignconfiguration200Response**](Setcampaignconfiguration200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

