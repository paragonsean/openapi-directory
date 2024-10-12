# OpenAq.V2Api

All URIs are relative to *http://openaq.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**averagesV2GetV2AveragesGet**](V2Api.md#averagesV2GetV2AveragesGet) | **GET** /v2/averages | Averages V2 Get
[**citiesGetV2CitiesGet**](V2Api.md#citiesGetV2CitiesGet) | **GET** /v2/cities | Provides a simple listing of cities within the platform
[**countriesGetV2CountriesCountryIdGet**](V2Api.md#countriesGetV2CountriesCountryIdGet) | **GET** /v2/countries/{country_id} | Countries Get
[**countriesGetV2CountriesGet**](V2Api.md#countriesGetV2CountriesGet) | **GET** /v2/countries | Countries Get
[**demoV2LocationsTilesViewerGet**](V2Api.md#demoV2LocationsTilesViewerGet) | **GET** /v2/locations/tiles/viewer | Demo
[**getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet**](V2Api.md#getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet) | **GET** /v2/locations/tiles/mobile-generalized/{z}/{x}/{y}.pbf | Get Mobilegentile
[**getMobiletileV2LocationsTilesMobileZXYPbfGet**](V2Api.md#getMobiletileV2LocationsTilesMobileZXYPbfGet) | **GET** /v2/locations/tiles/mobile/{z}/{x}/{y}.pbf | Get Mobiletile
[**getTileV2LocationsTilesZXYPbfGet**](V2Api.md#getTileV2LocationsTilesZXYPbfGet) | **GET** /v2/locations/tiles/{z}/{x}/{y}.pbf | Get Tile
[**latestGetV2LatestGet**](V2Api.md#latestGetV2LatestGet) | **GET** /v2/latest | Latest Get
[**latestGetV2LatestLocationIdGet**](V2Api.md#latestGetV2LatestLocationIdGet) | **GET** /v2/latest/{location_id} | Latest Get
[**locationsGetV2LocationsGet**](V2Api.md#locationsGetV2LocationsGet) | **GET** /v2/locations | Locations Get
[**locationsGetV2LocationsLocationIdGet**](V2Api.md#locationsGetV2LocationsLocationIdGet) | **GET** /v2/locations/{location_id} | Locations Get
[**measurementsGetV2MeasurementsGet**](V2Api.md#measurementsGetV2MeasurementsGet) | **GET** /v2/measurements | Measurements Get
[**mfrGetV2ManufacturersGet**](V2Api.md#mfrGetV2ManufacturersGet) | **GET** /v2/manufacturers | Mfr Get
[**mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet**](V2Api.md#mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet) | **GET** /v2/locations/tiles/mobile-generalized/tiles.json | Mobilegentilejson
[**mobiletilejsonV2LocationsTilesMobileTilesJsonGet**](V2Api.md#mobiletilejsonV2LocationsTilesMobileTilesJsonGet) | **GET** /v2/locations/tiles/mobile/tiles.json | Mobiletilejson
[**modelGetV2ModelsGet**](V2Api.md#modelGetV2ModelsGet) | **GET** /v2/models | Model Get
[**parametersGetV2ParametersGet**](V2Api.md#parametersGetV2ParametersGet) | **GET** /v2/parameters | Parameters Get
[**projectsGetV2ProjectsGet**](V2Api.md#projectsGetV2ProjectsGet) | **GET** /v2/projects | Projects Get
[**projectsGetV2ProjectsProjectIdGet**](V2Api.md#projectsGetV2ProjectsProjectIdGet) | **GET** /v2/projects/{project_id} | Projects Get
[**readmeGetV2SourcesReadmeSlugGet**](V2Api.md#readmeGetV2SourcesReadmeSlugGet) | **GET** /v2/sources/readme/{slug} | Readme Get
[**sourcesGetV2SourcesGet**](V2Api.md#sourcesGetV2SourcesGet) | **GET** /v2/sources | Sources Get
[**summaryGetV2SummaryGet**](V2Api.md#summaryGetV2SummaryGet) | **GET** /v2/summary | Summary Get
[**tilejsonV2LocationsTilesTilesJsonGet**](V2Api.md#tilejsonV2LocationsTilesTilesJsonGet) | **GET** /v2/locations/tiles/tiles.json | Tilejson



## averagesV2GetV2AveragesGet

> OpenAQResult averagesV2GetV2AveragesGet(spatial, temporal, opts)

Averages V2 Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let spatial = new OpenAq.Spatial(); // Spatial | 
let temporal = new OpenAq.Temporal(); // Temporal | 
let opts = {
  'dateFrom': new OpenAq.DateFrom(), // DateFrom | 
  'dateTo': new OpenAq.DateTo(), // DateTo | 
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'projectId': 56, // Number | 
  'project': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'location': ["null"], // [String] | 
  'group': false // Boolean | 
};
apiInstance.averagesV2GetV2AveragesGet(spatial, temporal, opts, (error, data, response) => {
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
 **spatial** | [**Spatial**](.md)|  | 
 **temporal** | [**Temporal**](.md)|  | 
 **dateFrom** | [**DateFrom**](.md)|  | [optional] 
 **dateTo** | [**DateTo**](.md)|  | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **projectId** | **Number**|  | [optional] 
 **project** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **location** | [**[String]**](String.md)|  | [optional] 
 **group** | **Boolean**|  | [optional] [default to false]

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## citiesGetV2CitiesGet

> OpenAQCitiesResult citiesGetV2CitiesGet(opts)

Provides a simple listing of cities within the platform

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'city': ["null"], // [String] |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
  'orderBy': new OpenAq.CitiesOrder(), // CitiesOrder | Order by a field
  'entity': "entity_example" // String | 
};
apiInstance.citiesGetV2CitiesGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **city** | [**[String]**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] 
 **orderBy** | [**CitiesOrder**](.md)| Order by a field | [optional] 
 **entity** | **String**|  | [optional] 

### Return type

[**OpenAQCitiesResult**](OpenAQCitiesResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetV2CountriesCountryIdGet

> OpenAQCountriesResult countriesGetV2CountriesCountryIdGet(countryId, opts)

Countries Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let countryId = "countryId_example"; // String | 
let opts = {
  'limit': 200, // Number | 
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'orderBy': new OpenAq.CountriesOrder() // CountriesOrder | 
};
apiInstance.countriesGetV2CountriesCountryIdGet(countryId, opts, (error, data, response) => {
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
 **countryId** | **String**|  | 
 **limit** | **Number**|  | [optional] [default to 200]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **orderBy** | [**CountriesOrder**](.md)|  | [optional] 

### Return type

[**OpenAQCountriesResult**](OpenAQCountriesResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetV2CountriesGet

> OpenAQCountriesResult countriesGetV2CountriesGet(opts)

Countries Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'limit': 200, // Number | 
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'orderBy': new OpenAq.CountriesOrder() // CountriesOrder | 
};
apiInstance.countriesGetV2CountriesGet(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 200]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **orderBy** | [**CountriesOrder**](.md)|  | [optional] 

### Return type

[**OpenAQCountriesResult**](OpenAQCountriesResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## demoV2LocationsTilesViewerGet

> String demoV2LocationsTilesViewerGet()

Demo

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.demoV2LocationsTilesViewerGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html


## getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet

> getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet(z, x, y, opts)

Get Mobilegentile

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let z = 56; // Number | 
let x = 56; // Number | 
let y = 56; // Number | 
let opts = {
  'parameter': new OpenAq.Parameter(), // Parameter | 
  'location': [null], // [Number] | limit data to location id
  'lastUpdatedFrom': new OpenAq.Lastupdatedfrom(), // Lastupdatedfrom | 
  'lastUpdatedTo': new OpenAq.Lastupdatedto(), // Lastupdatedto | 
  'isMobile': true, // Boolean | 
  'project': 56, // Number | 
  'isAnalysis': true // Boolean | 
};
apiInstance.getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet(z, x, y, opts, (error, data, response) => {
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
 **z** | **Number**|  | 
 **x** | **Number**|  | 
 **y** | **Number**|  | 
 **parameter** | [**Parameter**](.md)|  | [optional] 
 **location** | [**[Number]**](Number.md)| limit data to location id | [optional] 
 **lastUpdatedFrom** | [**Lastupdatedfrom**](.md)|  | [optional] 
 **lastUpdatedTo** | [**Lastupdatedto**](.md)|  | [optional] 
 **isMobile** | **Boolean**|  | [optional] 
 **project** | **Number**|  | [optional] 
 **isAnalysis** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-protobuf, application/json


## getMobiletileV2LocationsTilesMobileZXYPbfGet

> getMobiletileV2LocationsTilesMobileZXYPbfGet(z, x, y, dateFrom, dateTo, opts)

Get Mobiletile

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let z = 56; // Number | 
let x = 56; // Number | 
let y = 56; // Number | 
let dateFrom = new OpenAq.Datefrom(); // Datefrom | 
let dateTo = new OpenAq.Dateto(); // Dateto | 
let opts = {
  'parameter': new OpenAq.Parameter(), // Parameter | 
  'location': [null], // [Number] | limit data to location id
  'lastUpdatedFrom': new OpenAq.Lastupdatedfrom(), // Lastupdatedfrom | 
  'lastUpdatedTo': new OpenAq.Lastupdatedto(), // Lastupdatedto | 
  'isMobile': true, // Boolean | 
  'project': 56, // Number | 
  'isAnalysis': true // Boolean | 
};
apiInstance.getMobiletileV2LocationsTilesMobileZXYPbfGet(z, x, y, dateFrom, dateTo, opts, (error, data, response) => {
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
 **z** | **Number**|  | 
 **x** | **Number**|  | 
 **y** | **Number**|  | 
 **dateFrom** | [**Datefrom**](.md)|  | 
 **dateTo** | [**Dateto**](.md)|  | 
 **parameter** | [**Parameter**](.md)|  | [optional] 
 **location** | [**[Number]**](Number.md)| limit data to location id | [optional] 
 **lastUpdatedFrom** | [**Lastupdatedfrom**](.md)|  | [optional] 
 **lastUpdatedTo** | [**Lastupdatedto**](.md)|  | [optional] 
 **isMobile** | **Boolean**|  | [optional] 
 **project** | **Number**|  | [optional] 
 **isAnalysis** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-protobuf, application/json


## getTileV2LocationsTilesZXYPbfGet

> getTileV2LocationsTilesZXYPbfGet(z, x, y, opts)

Get Tile

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let z = 56; // Number | 
let x = 56; // Number | 
let y = 56; // Number | 
let opts = {
  'parameter': new OpenAq.Parameter(), // Parameter | 
  'location': [null], // [Number] | limit data to location id
  'lastUpdatedFrom': new OpenAq.Lastupdatedfrom(), // Lastupdatedfrom | 
  'lastUpdatedTo': new OpenAq.Lastupdatedto(), // Lastupdatedto | 
  'isMobile': true, // Boolean | 
  'project': 56, // Number | 
  'isAnalysis': true // Boolean | 
};
apiInstance.getTileV2LocationsTilesZXYPbfGet(z, x, y, opts, (error, data, response) => {
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
 **z** | **Number**|  | 
 **x** | **Number**|  | 
 **y** | **Number**|  | 
 **parameter** | [**Parameter**](.md)|  | [optional] 
 **location** | [**[Number]**](Number.md)| limit data to location id | [optional] 
 **lastUpdatedFrom** | [**Lastupdatedfrom**](.md)|  | [optional] 
 **lastUpdatedTo** | [**Lastupdatedto**](.md)|  | [optional] 
 **isMobile** | **Boolean**|  | [optional] 
 **project** | **Number**|  | [optional] 
 **isAnalysis** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-protobuf, application/json


## latestGetV2LatestGet

> OpenAQResult latestGetV2LatestGet(opts)

Latest Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Sort Direction
  'hasGeo': true, // Boolean | 
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'coordinates': "coordinates_example", // String | 
  'radius': 1000, // Number | 
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'city': ["null"], // [String] |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
  'locationId': 56, // Number | 
  'location': [new OpenAq.LocationInner()], // [LocationInner] | 
  'orderBy': new OpenAq.LocationsOrder(), // LocationsOrder | Order by a field
  'isMobile': true, // Boolean | Location is mobile
  'isAnalysis': true, // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
  'sourceName': ["null"], // [String] | Name of the data source
  'entity': new OpenAq.EntityTypes(), // EntityTypes | Source entity type.
  'sensorType': new OpenAq.SensorTypes(), // SensorTypes | Type of Sensor
  'modelName': ["null"], // [String] | Model Name of Sensor
  'manufacturerName': ["null"], // [String] | Manufacturer of Sensor
  'dumpRaw': false // Boolean | 
};
apiInstance.latestGetV2LatestGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Sort Direction | [optional] 
 **hasGeo** | **Boolean**|  | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **coordinates** | **String**|  | [optional] 
 **radius** | **Number**|  | [optional] [default to 1000]
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **city** | [**[String]**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] 
 **locationId** | **Number**|  | [optional] 
 **location** | [**[LocationInner]**](LocationInner.md)|  | [optional] 
 **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] 
 **isMobile** | **Boolean**| Location is mobile | [optional] 
 **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] 
 **sourceName** | [**[String]**](String.md)| Name of the data source | [optional] 
 **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] 
 **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] 
 **modelName** | [**[String]**](String.md)| Model Name of Sensor | [optional] 
 **manufacturerName** | [**[String]**](String.md)| Manufacturer of Sensor | [optional] 
 **dumpRaw** | **Boolean**|  | [optional] [default to false]

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## latestGetV2LatestLocationIdGet

> OpenAQResult latestGetV2LatestLocationIdGet(locationId, opts)

Latest Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let locationId = 56; // Number | 
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Sort Direction
  'hasGeo': true, // Boolean | 
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'coordinates': "coordinates_example", // String | 
  'radius': 1000, // Number | 
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'city': ["null"], // [String] |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
  'location': [new OpenAq.LocationInner()], // [LocationInner] | 
  'orderBy': new OpenAq.LocationsOrder(), // LocationsOrder | Order by a field
  'isMobile': true, // Boolean | Location is mobile
  'isAnalysis': true, // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
  'sourceName': ["null"], // [String] | Name of the data source
  'entity': new OpenAq.EntityTypes(), // EntityTypes | Source entity type.
  'sensorType': new OpenAq.SensorTypes(), // SensorTypes | Type of Sensor
  'modelName': ["null"], // [String] | Model Name of Sensor
  'manufacturerName': ["null"], // [String] | Manufacturer of Sensor
  'dumpRaw': false // Boolean | 
};
apiInstance.latestGetV2LatestLocationIdGet(locationId, opts, (error, data, response) => {
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
 **locationId** | **Number**|  | 
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Sort Direction | [optional] 
 **hasGeo** | **Boolean**|  | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **coordinates** | **String**|  | [optional] 
 **radius** | **Number**|  | [optional] [default to 1000]
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **city** | [**[String]**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] 
 **location** | [**[LocationInner]**](LocationInner.md)|  | [optional] 
 **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] 
 **isMobile** | **Boolean**| Location is mobile | [optional] 
 **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] 
 **sourceName** | [**[String]**](String.md)| Name of the data source | [optional] 
 **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] 
 **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] 
 **modelName** | [**[String]**](String.md)| Model Name of Sensor | [optional] 
 **manufacturerName** | [**[String]**](String.md)| Manufacturer of Sensor | [optional] 
 **dumpRaw** | **Boolean**|  | [optional] [default to false]

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsGetV2LocationsGet

> OpenAQResult locationsGetV2LocationsGet(opts)

Locations Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Sort Direction
  'hasGeo': true, // Boolean | 
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'coordinates': "coordinates_example", // String | 
  'radius': 1000, // Number | 
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'city': ["null"], // [String] |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
  'locationId': 56, // Number | 
  'location': [new OpenAq.LocationInner()], // [LocationInner] | 
  'orderBy': new OpenAq.LocationsOrder(), // LocationsOrder | Order by a field
  'isMobile': true, // Boolean | Location is mobile
  'isAnalysis': true, // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
  'sourceName': ["null"], // [String] | Name of the data source
  'entity': new OpenAq.EntityTypes(), // EntityTypes | Source entity type.
  'sensorType': new OpenAq.SensorTypes(), // SensorTypes | Type of Sensor
  'modelName': ["null"], // [String] | Model Name of Sensor
  'manufacturerName': ["null"], // [String] | Manufacturer of Sensor
  'dumpRaw': false // Boolean | 
};
apiInstance.locationsGetV2LocationsGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Sort Direction | [optional] 
 **hasGeo** | **Boolean**|  | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **coordinates** | **String**|  | [optional] 
 **radius** | **Number**|  | [optional] [default to 1000]
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **city** | [**[String]**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] 
 **locationId** | **Number**|  | [optional] 
 **location** | [**[LocationInner]**](LocationInner.md)|  | [optional] 
 **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] 
 **isMobile** | **Boolean**| Location is mobile | [optional] 
 **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] 
 **sourceName** | [**[String]**](String.md)| Name of the data source | [optional] 
 **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] 
 **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] 
 **modelName** | [**[String]**](String.md)| Model Name of Sensor | [optional] 
 **manufacturerName** | [**[String]**](String.md)| Manufacturer of Sensor | [optional] 
 **dumpRaw** | **Boolean**|  | [optional] [default to false]

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsGetV2LocationsLocationIdGet

> OpenAQResult locationsGetV2LocationsLocationIdGet(locationId, opts)

Locations Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let locationId = 56; // Number | 
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Sort Direction
  'hasGeo': true, // Boolean | 
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'coordinates': "coordinates_example", // String | 
  'radius': 1000, // Number | 
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'city': ["null"], // [String] |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
  'location': [new OpenAq.LocationInner()], // [LocationInner] | 
  'orderBy': new OpenAq.LocationsOrder(), // LocationsOrder | Order by a field
  'isMobile': true, // Boolean | Location is mobile
  'isAnalysis': true, // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
  'sourceName': ["null"], // [String] | Name of the data source
  'entity': new OpenAq.EntityTypes(), // EntityTypes | Source entity type.
  'sensorType': new OpenAq.SensorTypes(), // SensorTypes | Type of Sensor
  'modelName': ["null"], // [String] | Model Name of Sensor
  'manufacturerName': ["null"], // [String] | Manufacturer of Sensor
  'dumpRaw': false // Boolean | 
};
apiInstance.locationsGetV2LocationsLocationIdGet(locationId, opts, (error, data, response) => {
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
 **locationId** | **Number**|  | 
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Sort Direction | [optional] 
 **hasGeo** | **Boolean**|  | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **coordinates** | **String**|  | [optional] 
 **radius** | **Number**|  | [optional] [default to 1000]
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **city** | [**[String]**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] 
 **location** | [**[LocationInner]**](LocationInner.md)|  | [optional] 
 **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] 
 **isMobile** | **Boolean**| Location is mobile | [optional] 
 **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] 
 **sourceName** | [**[String]**](String.md)| Name of the data source | [optional] 
 **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] 
 **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] 
 **modelName** | [**[String]**](String.md)| Model Name of Sensor | [optional] 
 **manufacturerName** | [**[String]**](String.md)| Manufacturer of Sensor | [optional] 
 **dumpRaw** | **Boolean**|  | [optional] [default to false]

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## measurementsGetV2MeasurementsGet

> Object measurementsGetV2MeasurementsGet(opts)

Measurements Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'format': "format_example", // String | 
  'dateFrom': new OpenAq.DateFrom(), // DateFrom | 
  'dateTo': new OpenAq.DateTo(), // DateTo | 
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | 
  'hasGeo': true, // Boolean | 
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'coordinates': "coordinates_example", // String | 
  'radius': 1000, // Number | 
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'city': ["null"], // [String] |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
  'locationId': 56, // Number | 
  'location': [new OpenAq.LocationInner()], // [LocationInner] | 
  'orderBy': new OpenAq.MeasOrder(), // MeasOrder | 
  'isMobile': true, // Boolean | 
  'isAnalysis': true, // Boolean | 
  'project': 56, // Number | 
  'entity': new OpenAq.EntityTypes(), // EntityTypes | 
  'sensorType': new OpenAq.SensorTypes(), // SensorTypes | 
  'valueFrom': 3.4, // Number | 
  'valueTo': 3.4, // Number | 
  'includeFields': "includeFields_example" // String | 
};
apiInstance.measurementsGetV2MeasurementsGet(opts, (error, data, response) => {
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
 **format** | **String**|  | [optional] 
 **dateFrom** | [**DateFrom**](.md)|  | [optional] 
 **dateTo** | [**DateTo**](.md)|  | [optional] 
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)|  | [optional] 
 **hasGeo** | **Boolean**|  | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **coordinates** | **String**|  | [optional] 
 **radius** | **Number**|  | [optional] [default to 1000]
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **city** | [**[String]**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] 
 **locationId** | **Number**|  | [optional] 
 **location** | [**[LocationInner]**](LocationInner.md)|  | [optional] 
 **orderBy** | [**MeasOrder**](.md)|  | [optional] 
 **isMobile** | **Boolean**|  | [optional] 
 **isAnalysis** | **Boolean**|  | [optional] 
 **project** | **Number**|  | [optional] 
 **entity** | [**EntityTypes**](.md)|  | [optional] 
 **sensorType** | [**SensorTypes**](.md)|  | [optional] 
 **valueFrom** | **Number**|  | [optional] 
 **valueTo** | **Number**|  | [optional] 
 **includeFields** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mfrGetV2ManufacturersGet

> OpenAQResult mfrGetV2ManufacturersGet()

Mfr Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.mfrGetV2ManufacturersGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet

> TileJSON mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet()

Mobilegentilejson

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TileJSON**](TileJSON.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mobiletilejsonV2LocationsTilesMobileTilesJsonGet

> TileJSON mobiletilejsonV2LocationsTilesMobileTilesJsonGet()

Mobiletilejson

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.mobiletilejsonV2LocationsTilesMobileTilesJsonGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TileJSON**](TileJSON.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetV2ModelsGet

> OpenAQResult modelGetV2ModelsGet()

Model Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.modelGetV2ModelsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## parametersGetV2ParametersGet

> OpenAQParametersResult parametersGetV2ParametersGet(opts)

Parameters Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'sourceName': ["null"], // [String] | 
  'sourceId': [null], // [Number] | 
  'sourceSlug': ["null"], // [String] | 
  'orderBy': new OpenAq.OrderBy() // OrderBy | 
};
apiInstance.parametersGetV2ParametersGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **sourceName** | [**[String]**](String.md)|  | [optional] 
 **sourceId** | [**[Number]**](Number.md)|  | [optional] 
 **sourceSlug** | [**[String]**](String.md)|  | [optional] 
 **orderBy** | [**OrderBy**](.md)|  | [optional] 

### Return type

[**OpenAQParametersResult**](OpenAQParametersResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetV2ProjectsGet

> OpenAQProjectsResult projectsGetV2ProjectsGet(opts)

Projects Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'projectId': 56, // Number | 
  'project': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'orderBy': new OpenAq.ProjectsOrder(), // ProjectsOrder | 
  'isMobile': true, // Boolean | 
  'isAnalysis': true, // Boolean | 
  'entity': "entity_example", // String | 
  'sensorType': "sensorType_example", // String | 
  'sourceName': ["null"] // [String] | 
};
apiInstance.projectsGetV2ProjectsGet(opts, (error, data, response) => {
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
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **projectId** | **Number**|  | [optional] 
 **project** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **orderBy** | [**ProjectsOrder**](.md)|  | [optional] 
 **isMobile** | **Boolean**|  | [optional] 
 **isAnalysis** | **Boolean**|  | [optional] 
 **entity** | **String**|  | [optional] 
 **sensorType** | **String**|  | [optional] 
 **sourceName** | [**[String]**](String.md)|  | [optional] 

### Return type

[**OpenAQProjectsResult**](OpenAQProjectsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetV2ProjectsProjectIdGet

> OpenAQProjectsResult projectsGetV2ProjectsProjectIdGet(projectId, opts)

Projects Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let projectId = 56; // Number | 
let opts = {
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'parameterId': 56, // Number | 
  'parameter': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'unit': ["null"], // [String] | 
  'project': [new OpenAq.ParameterInner()], // [ParameterInner] | 
  'orderBy': new OpenAq.ProjectsOrder(), // ProjectsOrder | 
  'isMobile': true, // Boolean | 
  'isAnalysis': true, // Boolean | 
  'entity': "entity_example", // String | 
  'sensorType': "sensorType_example", // String | 
  'sourceName': ["null"] // [String] | 
};
apiInstance.projectsGetV2ProjectsProjectIdGet(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**|  | 
 **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] 
 **country** | [**[String]**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] 
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **parameterId** | **Number**|  | [optional] 
 **parameter** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **unit** | [**[String]**](String.md)|  | [optional] 
 **project** | [**[ParameterInner]**](ParameterInner.md)|  | [optional] 
 **orderBy** | [**ProjectsOrder**](.md)|  | [optional] 
 **isMobile** | **Boolean**|  | [optional] 
 **isAnalysis** | **Boolean**|  | [optional] 
 **entity** | **String**|  | [optional] 
 **sensorType** | **String**|  | [optional] 
 **sourceName** | [**[String]**](String.md)|  | [optional] 

### Return type

[**OpenAQProjectsResult**](OpenAQProjectsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readmeGetV2SourcesReadmeSlugGet

> Object readmeGetV2SourcesReadmeSlugGet(slug)

Readme Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let slug = "slug_example"; // String | 
apiInstance.readmeGetV2SourcesReadmeSlugGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sourcesGetV2SourcesGet

> OpenAQResult sourcesGetV2SourcesGet(opts)

Sources Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'sourceName': ["null"], // [String] | 
  'sourceId': [null], // [Number] | 
  'sourceSlug': ["null"], // [String] | 
  'orderBy': new OpenAq.SourcesOrder() // SourcesOrder | 
};
apiInstance.sourcesGetV2SourcesGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Change the number of results returned. | [optional] [default to 100]
 **page** | **Number**| Paginate through results. | [optional] [default to 1]
 **offset** | **Number**|  | [optional] [default to 0]
 **sort** | [**Sort**](.md)| Define sort order. | [optional] 
 **sourceName** | [**[String]**](String.md)|  | [optional] 
 **sourceId** | [**[Number]**](Number.md)|  | [optional] 
 **sourceSlug** | [**[String]**](String.md)|  | [optional] 
 **orderBy** | [**SourcesOrder**](.md)|  | [optional] 

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## summaryGetV2SummaryGet

> OpenAQResult summaryGetV2SummaryGet()

Summary Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.summaryGetV2SummaryGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tilejsonV2LocationsTilesTilesJsonGet

> TileJSON tilejsonV2LocationsTilesTilesJsonGet()

Tilejson

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V2Api();
apiInstance.tilejsonV2LocationsTilesTilesJsonGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TileJSON**](TileJSON.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

