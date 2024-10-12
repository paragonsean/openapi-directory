# TicketmasterPublishApi.DefaultApi

All URIs are relative to *http://www.ticketmaster.com/publish/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patchAttraction**](DefaultApi.md#patchAttraction) | **PATCH** /publish/v2/attractions/{id} | Publish a patch on an attraction
[**patchEvent**](DefaultApi.md#patchEvent) | **PATCH** /publish/v2/events/{id} | Publish a patch on an event
[**patchVenue**](DefaultApi.md#patchVenue) | **PATCH** /publish/v2/venues/{id} | Publish a patch on a venue
[**publishAttraction**](DefaultApi.md#publishAttraction) | **POST** /publish/v2/attractions | Publish an attractions
[**publishAttractionVideos**](DefaultApi.md#publishAttractionVideos) | **POST** /publish/v2/attractions/{id}/videos | Publish a video on an attraction
[**publishEntitlements**](DefaultApi.md#publishEntitlements) | **POST** /publish/v2/entitlements | Publish entitlements on an entity
[**publishEvent**](DefaultApi.md#publishEvent) | **POST** /publish/v2/events | Publish an event
[**publishEventVideos**](DefaultApi.md#publishEventVideos) | **POST** /publish/v2/events/{id}/videos | Publish a video on an event
[**publishExtension**](DefaultApi.md#publishExtension) | **POST** /publish/v2/extensions | Publish extension on an entity
[**publishVenue**](DefaultApi.md#publishVenue) | **POST** /publish/v2/venues | Publish a venue



## patchAttraction

> IngestionResult patchAttraction(id, tMPSCorrelationId, augmentationData)

Publish a patch on an attraction

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let id = "id_example"; // String | ID of the attraction the patch will be applied
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let augmentationData = new TicketmasterPublishApi.AugmentationData(); // AugmentationData | Patch to apply
apiInstance.patchAttraction(id, tMPSCorrelationId, augmentationData, (error, data, response) => {
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
 **id** | **String**| ID of the attraction the patch will be applied | 
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **augmentationData** | [**AugmentationData**](AugmentationData.md)| Patch to apply | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## patchEvent

> IngestionResult patchEvent(id, tMPSCorrelationId, augmentationData)

Publish a patch on an event

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let id = "id_example"; // String | ID of the event the patch will be applied
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let augmentationData = new TicketmasterPublishApi.AugmentationData(); // AugmentationData | Patch to apply
apiInstance.patchEvent(id, tMPSCorrelationId, augmentationData, (error, data, response) => {
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
 **id** | **String**| ID of the event the patch will be applied | 
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **augmentationData** | [**AugmentationData**](AugmentationData.md)| Patch to apply | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## patchVenue

> IngestionResult patchVenue(id, tMPSCorrelationId, augmentationData)

Publish a patch on a venue

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let id = "id_example"; // String | ID of the venue the patch will be applied
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let augmentationData = new TicketmasterPublishApi.AugmentationData(); // AugmentationData | Patch to apply
apiInstance.patchVenue(id, tMPSCorrelationId, augmentationData, (error, data, response) => {
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
 **id** | **String**| ID of the venue the patch will be applied | 
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **augmentationData** | [**AugmentationData**](AugmentationData.md)| Patch to apply | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishAttraction

> IngestionResult publishAttraction(tMPSCorrelationId, attraction)

Publish an attractions

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let attraction = new TicketmasterPublishApi.Attraction(); // Attraction | Attraction
apiInstance.publishAttraction(tMPSCorrelationId, attraction, (error, data, response) => {
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
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **attraction** | [**Attraction**](Attraction.md)| Attraction | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishAttractionVideos

> IngestionResult publishAttractionVideos(id, tMPSCorrelationId, video)

Publish a video on an attraction

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let id = "id_example"; // String | ID of the attraction the video is linked to
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let video = new TicketmasterPublishApi.Video(); // Video | Video data
apiInstance.publishAttractionVideos(id, tMPSCorrelationId, video, (error, data, response) => {
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
 **id** | **String**| ID of the attraction the video is linked to | 
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **video** | [**Video**](Video.md)| Video data | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishEntitlements

> IngestionResult publishEntitlements(tMPSCorrelationId, entitlement)

Publish entitlements on an entity

Since 2.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let entitlement = new TicketmasterPublishApi.Entitlement(); // Entitlement | Entitlements information to add to the entity
apiInstance.publishEntitlements(tMPSCorrelationId, entitlement, (error, data, response) => {
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
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **entitlement** | [**Entitlement**](Entitlement.md)| Entitlements information to add to the entity | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishEvent

> IngestionResult publishEvent(tMPSCorrelationId, event)

Publish an event

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let event = new TicketmasterPublishApi.Event(); // Event | Event
apiInstance.publishEvent(tMPSCorrelationId, event, (error, data, response) => {
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
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **event** | [**Event**](Event.md)| Event | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishEventVideos

> IngestionResult publishEventVideos(id, tMPSCorrelationId, video)

Publish a video on an event

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let id = "id_example"; // String | ID of the event the video is linked to
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let video = new TicketmasterPublishApi.Video(); // Video | Video data
apiInstance.publishEventVideos(id, tMPSCorrelationId, video, (error, data, response) => {
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
 **id** | **String**| ID of the event the video is linked to | 
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **video** | [**Video**](Video.md)| Video data | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishExtension

> IngestionResult publishExtension(tMPSCorrelationId, extensionData)

Publish extension on an entity

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let extensionData = new TicketmasterPublishApi.ExtensionData(); // ExtensionData | Extension information to add to the entity
apiInstance.publishExtension(tMPSCorrelationId, extensionData, (error, data, response) => {
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
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **extensionData** | [**ExtensionData**](ExtensionData.md)| Extension information to add to the entity | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## publishVenue

> IngestionResult publishVenue(tMPSCorrelationId, venue)

Publish a venue

Since 1.0.0

### Example

```javascript
import TicketmasterPublishApi from 'ticketmaster_publish_api';

let apiInstance = new TicketmasterPublishApi.DefaultApi();
let tMPSCorrelationId = "''"; // String | Unique correlation id to be able to trace the request in our system
let venue = new TicketmasterPublishApi.Venue(); // Venue | Venue
apiInstance.publishVenue(tMPSCorrelationId, venue, (error, data, response) => {
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
 **tMPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to &#39;&#39;]
 **venue** | [**Venue**](Venue.md)| Venue | 

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

