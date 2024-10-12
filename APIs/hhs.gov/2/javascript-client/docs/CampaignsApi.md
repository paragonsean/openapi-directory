# HhsMediaServicesApi.CampaignsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesCampaignsIdJsonGet**](CampaignsApi.md#resourcesCampaignsIdJsonGet) | **GET** /resources/campaigns/{id}.json | Get Campaign by ID
[**resourcesCampaignsIdMediaJsonGet**](CampaignsApi.md#resourcesCampaignsIdMediaJsonGet) | **GET** /resources/campaigns/{id}/media.json | Get MediaItems by Campaign ID
[**resourcesCampaignsIdSyndicateFormatGet**](CampaignsApi.md#resourcesCampaignsIdSyndicateFormatGet) | **GET** /resources/campaigns/{id}/syndicate.{format} | Get MediaItems for Campaign
[**resourcesCampaignsJsonGet**](CampaignsApi.md#resourcesCampaignsJsonGet) | **GET** /resources/campaigns.json | Get Campaigns



## resourcesCampaignsIdJsonGet

> CampaignWrapped resourcesCampaignsIdJsonGet(id)

Get Campaign by ID

Information about a specific campaign

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.CampaignsApi();
let id = 789; // Number | The id of the record to look up
apiInstance.resourcesCampaignsIdJsonGet(id, (error, data, response) => {
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
 **id** | **Number**| The id of the record to look up | 

### Return type

[**CampaignWrapped**](CampaignWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesCampaignsIdMediaJsonGet

> MediaItemWrapped resourcesCampaignsIdMediaJsonGet(id, opts)

Get MediaItems by Campaign ID

Campaign Listings

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.CampaignsApi();
let id = 789; // Number | The id of the campaign to find media items for
let opts = {
  'sort': "sort_example", // String | The name of the property to which sorting will be applied
  'max': 56, // Number | The maximum number of records to return
  'offset': 56 // Number | The offset of the records set to return for pagination
};
apiInstance.resourcesCampaignsIdMediaJsonGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the campaign to find media items for | 
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| The offset of the records set to return for pagination | [optional] 

### Return type

[**MediaItemWrapped**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesCampaignsIdSyndicateFormatGet

> SyndicateMarshallerWrapped resourcesCampaignsIdSyndicateFormatGet(id, format, opts)

Get MediaItems for Campaign

MediaItem

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.CampaignsApi();
let id = 789; // Number | The id of the record to look up
let format = "format_example"; // String | Automatically added
let opts = {
  'displayMethod': "displayMethod_example" // String | Method used to render an html request. Accepts one: [mv, list, feed]
};
apiInstance.resourcesCampaignsIdSyndicateFormatGet(id, format, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the record to look up | 
 **format** | **String**| Automatically added | 
 **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] 

### Return type

[**SyndicateMarshallerWrapped**](SyndicateMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesCampaignsJsonGet

> CampaignWrapped resourcesCampaignsJsonGet(opts)

Get Campaigns

Media Listings for a specific campaign

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.CampaignsApi();
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56, // Number | The offset of the records set to return for pagination
  'sort': "sort_example" // String | * Set of fields to sort the records by.
};
apiInstance.resourcesCampaignsJsonGet(opts, (error, data, response) => {
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
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| The offset of the records set to return for pagination | [optional] 
 **sort** | **String**| * Set of fields to sort the records by. | [optional] 

### Return type

[**CampaignWrapped**](CampaignWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

