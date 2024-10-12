# NprSponsorshipService.SponsorshipApi

All URIs are relative to *https://sponsorship.api.npr.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAds**](SponsorshipApi.md#getAds) | **GET** /v2/ads | Request VAST sponsorship units
[**receiveAdTracking**](SponsorshipApi.md#receiveAdTracking) | **POST** /v2/ads | Record tracking data for VAST sponsorship units



## getAds

> VASTXml getAds(authorization, opts)

Request VAST sponsorship units

**Not** for use by NPR One clients (for whom sponsorship is already integrated into the Listening Service), this endpoint is designed to be used by our other client applications to request sponsorship on behalf of a user. Sponsorship units are returned in the form of VAST XML. It is worth noting that this endpoint attempts to always return XML, even in the case of exceptions.  The default behavior of this endpoint is asynchronous; on an initial request, a call to our external sponsorship provider is placed on a queue, which is typically processed within 3 minutes. Once the sponsorship call is received and processed, the returned sponsorship units are placed in a cache on our server for the current user. Subsequent calls to this endpoint will return VAST sponsorship units from this cache until tracking information is submitted, which removes the ad from the cache and will automatically request additional ads asynchronously if there are fewer than a certain number remaining in the cache.  For development purposes, it&#39;s worth noting that there is currently no way to clear a user&#39;s cache without submitting some form of tracking.

### Example

```javascript
import NprSponsorshipService from 'npr_sponsorship_service';

let apiInstance = new NprSponsorshipService.SponsorshipApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let opts = {
  'xAdvertisingID': "xAdvertisingID_example", // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
  'forceResult': true, // Boolean | Whether to force a synchronous call to our external sponsorship provider; the default behavior is asynchronous.
  'adCount': 56 // Number | How many sponsorship units to request in one call; if left unspecified, the default behavior is to return only 1.
};
apiInstance.getAds(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] 
 **forceResult** | **Boolean**| Whether to force a synchronous call to our external sponsorship provider; the default behavior is asynchronous. | [optional] 
 **adCount** | **Number**| How many sponsorship units to request in one call; if left unspecified, the default behavior is to return only 1. | [optional] 

### Return type

[**VASTXml**](VASTXml.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## receiveAdTracking

> receiveAdTracking(authorization, body, opts)

Record tracking data for VAST sponsorship units

**Not** for use by NPR One clients (for whom sponsorship is already integrated into the Listening Service), this endpoint is designed to be used by our other client applications to submit tracking information for sponsorship units obtained from the &#x60;GET /sponsorship/v2/ads&#x60; endpoint.  The tracking information should be submitted in the body of the request in the form of a JSON object following the Collection.Doc+JSON specification.

### Example

```javascript
import NprSponsorshipService from 'npr_sponsorship_service';

let apiInstance = new NprSponsorshipService.SponsorshipApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let body = new NprSponsorshipService.UserAdDocument(); // UserAdDocument | A JSON object representing sponsorship tracking data to submit to our external provider.
let opts = {
  'xAdvertisingID': "xAdvertisingID_example" // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
};
apiInstance.receiveAdTracking(authorization, body, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **body** | [**UserAdDocument**](UserAdDocument.md)| A JSON object representing sponsorship tracking data to submit to our external provider. | 
 **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/xml

