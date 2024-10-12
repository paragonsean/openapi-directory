# LetMcApiV2BasicTier2.PropertyControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**propertyControllerGetPropertiesFacilities**](PropertyControllerApi.md#propertyControllerGetPropertiesFacilities) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/facilities | A collection of facilities linked to a block, property or room
[**propertyControllerGetPropertiesPhotos**](PropertyControllerApi.md#propertyControllerGetPropertiesPhotos) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/photos | A collection showing all the photos linked to a specific block, property or room
[**propertyControllerGetPropertiesRooms**](PropertyControllerApi.md#propertyControllerGetPropertiesRooms) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/rooms | A collection of the rooms that belong to this property or block
[**propertyControllerGetPropertiesTenancies**](PropertyControllerApi.md#propertyControllerGetPropertiesTenancies) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/tenancies | A collection of all tenancies associated with this block, property or room
[**propertyControllerGetPropertyEERDownload**](PropertyControllerApi.md#propertyControllerGetPropertyEERDownload) | **GET** /v2/tier2/{shortName}/property/structures/{propertyStructureID}/reports/eer | Downloads the energy efficiency report (EER) graph for a property
[**propertyControllerGetPropertyEIRDownload**](PropertyControllerApi.md#propertyControllerGetPropertyEIRDownload) | **GET** /v2/tier2/{shortName}/property/structures/{propertyStructureID}/reports/eir | Downloads the environmental impact report (EIR) graph for a property
[**v2Tier2ShortNamePropertyPropertiesGet**](PropertyControllerApi.md#v2Tier2ShortNamePropertyPropertiesGet) | **GET** /v2/tier2/{shortName}/property/properties | A collection of all properties within a company
[**v2Tier2ShortNamePropertyPropertiesPropertyIDGet**](PropertyControllerApi.md#v2Tier2ShortNamePropertyPropertiesPropertyIDGet) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID} | Get a specific property given its unique Object ID (OID)



## propertyControllerGetPropertiesFacilities

> PropertyFacilityModelResults propertyControllerGetPropertiesFacilities(shortName, propertyID, offset, count)

A collection of facilities linked to a block, property or room

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyID = "propertyID_example"; // String | The unique ID of the Property
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.propertyControllerGetPropertiesFacilities(shortName, propertyID, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyID** | **String**| The unique ID of the Property | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PropertyFacilityModelResults**](PropertyFacilityModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## propertyControllerGetPropertiesPhotos

> PhotoModelResults propertyControllerGetPropertiesPhotos(shortName, propertyID, offset, count)

A collection showing all the photos linked to a specific block, property or room

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyID = "propertyID_example"; // String | The unique ID of the Property
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.propertyControllerGetPropertiesPhotos(shortName, propertyID, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyID** | **String**| The unique ID of the Property | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## propertyControllerGetPropertiesRooms

> PropertyRoomModelResults propertyControllerGetPropertiesRooms(shortName, propertyID, offset, count)

A collection of the rooms that belong to this property or block

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyID = "propertyID_example"; // String | The unique ID of the Property
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.propertyControllerGetPropertiesRooms(shortName, propertyID, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyID** | **String**| The unique ID of the Property | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PropertyRoomModelResults**](PropertyRoomModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## propertyControllerGetPropertiesTenancies

> TenancyModelResults propertyControllerGetPropertiesTenancies(shortName, propertyID, offset, count)

A collection of all tenancies associated with this block, property or room

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyID = "propertyID_example"; // String | The unique ID of the Property
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.propertyControllerGetPropertiesTenancies(shortName, propertyID, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyID** | **String**| The unique ID of the Property | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## propertyControllerGetPropertyEERDownload

> Object propertyControllerGetPropertyEERDownload(shortName, propertyStructureID)

Downloads the energy efficiency report (EER) graph for a property

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyStructureID = "propertyStructureID_example"; // String | The unique ID of the property structure
apiInstance.propertyControllerGetPropertyEERDownload(shortName, propertyStructureID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyStructureID** | **String**| The unique ID of the property structure | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## propertyControllerGetPropertyEIRDownload

> Object propertyControllerGetPropertyEIRDownload(shortName, propertyStructureID)

Downloads the environmental impact report (EIR) graph for a property

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyStructureID = "propertyStructureID_example"; // String | The unique ID of the property structure
apiInstance.propertyControllerGetPropertyEIRDownload(shortName, propertyStructureID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyStructureID** | **String**| The unique ID of the property structure | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier2ShortNamePropertyPropertiesGet

> PropertyModelResults v2Tier2ShortNamePropertyPropertiesGet(shortName, offset, count)

A collection of all properties within a company

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier2ShortNamePropertyPropertiesGet(shortName, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PropertyModelResults**](PropertyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier2ShortNamePropertyPropertiesPropertyIDGet

> PropertyModel v2Tier2ShortNamePropertyPropertiesPropertyIDGet(shortName, propertyID)

Get a specific property given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyID = "propertyID_example"; // String | The unique ID of the Property
apiInstance.v2Tier2ShortNamePropertyPropertiesPropertyIDGet(shortName, propertyID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **propertyID** | **String**| The unique ID of the Property | 

### Return type

[**PropertyModel**](PropertyModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

