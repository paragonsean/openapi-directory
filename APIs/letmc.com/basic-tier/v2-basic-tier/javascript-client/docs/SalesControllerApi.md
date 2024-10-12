# LetMcApiV2BasicTier2.SalesControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesControllerGetAdvertisedSales**](SalesControllerApi.md#salesControllerGetAdvertisedSales) | **GET** /v2/tier2/{shortName}/sales/advertisedsales | Search all sales properties available given a range of search criteria
[**salesControllerGetEER**](SalesControllerApi.md#salesControllerGetEER) | **GET** /v2/tier2/{shortName}/sales/reports/eer/{salesInstructionID} | Downloads the energy efficiency report (EER) graph for a sales instruction
[**salesControllerGetEIR**](SalesControllerApi.md#salesControllerGetEIR) | **GET** /v2/tier2/{shortName}/sales/reports/eir/{salesInstructionID} | Downloads the energy efficiency report (EIR) graph for a sales instruction
[**salesControllerGetSalesInstructionsFeatures**](SalesControllerApi.md#salesControllerGetSalesInstructionsFeatures) | **GET** /v2/tier2/{shortName}/sales/salesinstructions/{salesInstructionID}/features | A collection of all features linked to a sales instruction
[**salesControllerGetSalesInstructionsFloorPlans**](SalesControllerApi.md#salesControllerGetSalesInstructionsFloorPlans) | **GET** /v2/tier2/{shortName}/sales/salesinstructions/{salesInstructionID}/floorplans | A collection of floor plans linked to an instruction
[**salesControllerGetSalesInstructionsPhotos**](SalesControllerApi.md#salesControllerGetSalesInstructionsPhotos) | **GET** /v2/tier2/{shortName}/sales/salesinstructions/{salesInstructionID}/photos | A collection of photos linked to an instruction
[**salesControllerGetSalesInstructionsRooms**](SalesControllerApi.md#salesControllerGetSalesInstructionsRooms) | **GET** /v2/tier2/{shortName}/sales/salesinstructions/{salesInstructionID}/rooms | A collection of rooms linked to an instruction
[**v2Tier2ShortNameSalesSalesfeaturetypesGet**](SalesControllerApi.md#v2Tier2ShortNameSalesSalesfeaturetypesGet) | **GET** /v2/tier2/{shortName}/sales/salesfeaturetypes | A collection of all sales feature types linked to a company
[**v2Tier2ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet**](SalesControllerApi.md#v2Tier2ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet) | **GET** /v2/tier2/{shortName}/sales/salesfeaturetypes/{salesFeatureTypeID} | Get a specific sales feature type given its unique Object ID (OID)
[**v2Tier2ShortNameSalesSalesinstructionsGet**](SalesControllerApi.md#v2Tier2ShortNameSalesSalesinstructionsGet) | **GET** /v2/tier2/{shortName}/sales/salesinstructions | A collection of all sales instructions linked to a company
[**v2Tier2ShortNameSalesSalesinstructionsSalesInstructionIDGet**](SalesControllerApi.md#v2Tier2ShortNameSalesSalesinstructionsSalesInstructionIDGet) | **GET** /v2/tier2/{shortName}/sales/salesinstructions/{salesInstructionID} | Get a specific sales instruction given its unique Object ID (OID)



## salesControllerGetAdvertisedSales

> SalesInstructionModelResults salesControllerGetAdvertisedSales(shortName, branchID, offset, count, onlyDevelopement, onlyInvestements, opts)

Search all sales properties available given a range of search criteria

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
let onlyDevelopement = true; // Boolean | Show only development properties?
let onlyInvestements = true; // Boolean | Show only investment properties?
let opts = {
  'minimumPrice': 3.4, // Number | The minimum price to search for
  'maximumPrice': 3.4, // Number | The maximum price to search for
  'minimumBeds': 56, // Number | The minimum beds to search for
  'minimumBathrooms': 56, // Number | The minimum bathrooms to search for
  'minimumEnsuites': 56, // Number | The minimum ensuite bathrooms to search for
  'minimumToilets': 56, // Number | The minimum toilets to search for
  'minimumReception': 56 // Number | The minimum reception rooms to search for
};
apiInstance.salesControllerGetAdvertisedSales(shortName, branchID, offset, count, onlyDevelopement, onlyInvestements, opts, (error, data, response) => {
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
 **branchID** | **String**| The unique ID of the Branch | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 
 **onlyDevelopement** | **Boolean**| Show only development properties? | 
 **onlyInvestements** | **Boolean**| Show only investment properties? | 
 **minimumPrice** | **Number**| The minimum price to search for | [optional] 
 **maximumPrice** | **Number**| The maximum price to search for | [optional] 
 **minimumBeds** | **Number**| The minimum beds to search for | [optional] 
 **minimumBathrooms** | **Number**| The minimum bathrooms to search for | [optional] 
 **minimumEnsuites** | **Number**| The minimum ensuite bathrooms to search for | [optional] 
 **minimumToilets** | **Number**| The minimum toilets to search for | [optional] 
 **minimumReception** | **Number**| The minimum reception rooms to search for | [optional] 

### Return type

[**SalesInstructionModelResults**](SalesInstructionModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## salesControllerGetEER

> Object salesControllerGetEER(shortName, salesInstructionID)

Downloads the energy efficiency report (EER) graph for a sales instruction

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
apiInstance.salesControllerGetEER(shortName, salesInstructionID, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## salesControllerGetEIR

> Object salesControllerGetEIR(shortName, salesInstructionID)

Downloads the energy efficiency report (EIR) graph for a sales instruction

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
apiInstance.salesControllerGetEIR(shortName, salesInstructionID, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## salesControllerGetSalesInstructionsFeatures

> SalesFeatureModelResults salesControllerGetSalesInstructionsFeatures(shortName, salesInstructionID, offset, count)

A collection of all features linked to a sales instruction

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.salesControllerGetSalesInstructionsFeatures(shortName, salesInstructionID, offset, count, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**SalesFeatureModelResults**](SalesFeatureModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## salesControllerGetSalesInstructionsFloorPlans

> PhotoModelResults salesControllerGetSalesInstructionsFloorPlans(shortName, salesInstructionID, offset, count)

A collection of floor plans linked to an instruction

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.salesControllerGetSalesInstructionsFloorPlans(shortName, salesInstructionID, offset, count, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## salesControllerGetSalesInstructionsPhotos

> PhotoModelResults salesControllerGetSalesInstructionsPhotos(shortName, salesInstructionID, offset, count)

A collection of photos linked to an instruction

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.salesControllerGetSalesInstructionsPhotos(shortName, salesInstructionID, offset, count, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## salesControllerGetSalesInstructionsRooms

> PropertyRoomModelResults salesControllerGetSalesInstructionsRooms(shortName, salesInstructionID, offset, count)

A collection of rooms linked to an instruction

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.salesControllerGetSalesInstructionsRooms(shortName, salesInstructionID, offset, count, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PropertyRoomModelResults**](PropertyRoomModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier2ShortNameSalesSalesfeaturetypesGet

> SalesFeatureTypeModelResults v2Tier2ShortNameSalesSalesfeaturetypesGet(shortName, offset, count)

A collection of all sales feature types linked to a company

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier2ShortNameSalesSalesfeaturetypesGet(shortName, offset, count, (error, data, response) => {
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

[**SalesFeatureTypeModelResults**](SalesFeatureTypeModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier2ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet

> SalesFeatureTypeModel v2Tier2ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet(shortName, salesFeatureTypeID)

Get a specific sales feature type given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesFeatureTypeID = "salesFeatureTypeID_example"; // String | The unique ID of the SalesFeatureType
apiInstance.v2Tier2ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet(shortName, salesFeatureTypeID, (error, data, response) => {
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
 **salesFeatureTypeID** | **String**| The unique ID of the SalesFeatureType | 

### Return type

[**SalesFeatureTypeModel**](SalesFeatureTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier2ShortNameSalesSalesinstructionsGet

> SalesInstructionModelResults v2Tier2ShortNameSalesSalesinstructionsGet(shortName, offset, count)

A collection of all sales instructions linked to a company

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier2ShortNameSalesSalesinstructionsGet(shortName, offset, count, (error, data, response) => {
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

[**SalesInstructionModelResults**](SalesInstructionModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier2ShortNameSalesSalesinstructionsSalesInstructionIDGet

> SalesInstructionModel v2Tier2ShortNameSalesSalesinstructionsSalesInstructionIDGet(shortName, salesInstructionID)

Get a specific sales instruction given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.SalesControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
apiInstance.v2Tier2ShortNameSalesSalesinstructionsSalesInstructionIDGet(shortName, salesInstructionID, (error, data, response) => {
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
 **salesInstructionID** | **String**| The unique ID of the SalesInstruction | 

### Return type

[**SalesInstructionModel**](SalesInstructionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

