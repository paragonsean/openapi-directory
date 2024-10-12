# OpenAq.V1Api

All URIs are relative to *http://openaq.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**citiesGetv1V1CitiesGet**](V1Api.md#citiesGetv1V1CitiesGet) | **GET** /v1/cities | Provides a simple listing of cities within the platform
[**countriesGetV1CountriesCountryIdGet**](V1Api.md#countriesGetV1CountriesCountryIdGet) | **GET** /v1/countries/{country_id} | Countries Get
[**countriesGetv1V1CountriesGet**](V1Api.md#countriesGetv1V1CountriesGet) | **GET** /v1/countries | Countries Getv1
[**latestV1GetV1LatestGet**](V1Api.md#latestV1GetV1LatestGet) | **GET** /v1/latest | Latest V1 Get
[**latestV1GetV1LatestLocationIdGet**](V1Api.md#latestV1GetV1LatestLocationIdGet) | **GET** /v1/latest/{location_id} | Latest V1 Get
[**locationsv1GetV1LocationsGet**](V1Api.md#locationsv1GetV1LocationsGet) | **GET** /v1/locations | Locationsv1 Get
[**locationsv1GetV1LocationsLocationIdGet**](V1Api.md#locationsv1GetV1LocationsLocationIdGet) | **GET** /v1/locations/{location_id} | Locationsv1 Get
[**measurementsGetV1V1MeasurementsGet**](V1Api.md#measurementsGetV1V1MeasurementsGet) | **GET** /v1/measurements | Measurements Get V1
[**parametersGetv1V1ParametersGet**](V1Api.md#parametersGetv1V1ParametersGet) | **GET** /v1/parameters | Parameters Getv1
[**sourcesV1GetV1SourcesGet**](V1Api.md#sourcesV1GetV1SourcesGet) | **GET** /v1/sources | Sources V1 Get



## citiesGetv1V1CitiesGet

> OpenAQCitiesResult citiesGetv1V1CitiesGet(opts)

Provides a simple listing of cities within the platform

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.citiesGetv1V1CitiesGet(opts, (error, data, response) => {
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


## countriesGetV1CountriesCountryIdGet

> OpenAQCountriesResult countriesGetV1CountriesCountryIdGet(countryId, opts)

Countries Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
let countryId = "countryId_example"; // String | 
let opts = {
  'limit': 200, // Number | 
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'orderBy': new OpenAq.CountriesOrder() // CountriesOrder | 
};
apiInstance.countriesGetV1CountriesCountryIdGet(countryId, opts, (error, data, response) => {
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


## countriesGetv1V1CountriesGet

> OpenAQCountriesResult countriesGetv1V1CountriesGet(opts)

Countries Getv1

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
let opts = {
  'limit': 200, // Number | 
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'countryId': "countryId_example", // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
  'country': ["null"], // [String] |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
  'orderBy': new OpenAq.CountriesOrder() // CountriesOrder | 
};
apiInstance.countriesGetv1V1CountriesGet(opts, (error, data, response) => {
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


## latestV1GetV1LatestGet

> OpenAQResult latestV1GetV1LatestGet(opts)

Latest V1 Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.latestV1GetV1LatestGet(opts, (error, data, response) => {
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


## latestV1GetV1LatestLocationIdGet

> OpenAQResult latestV1GetV1LatestLocationIdGet(locationId, opts)

Latest V1 Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.latestV1GetV1LatestLocationIdGet(locationId, opts, (error, data, response) => {
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


## locationsv1GetV1LocationsGet

> OpenAQResult locationsv1GetV1LocationsGet(opts)

Locationsv1 Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.locationsv1GetV1LocationsGet(opts, (error, data, response) => {
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


## locationsv1GetV1LocationsLocationIdGet

> OpenAQResult locationsv1GetV1LocationsLocationIdGet(locationId, opts)

Locationsv1 Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.locationsv1GetV1LocationsLocationIdGet(locationId, opts, (error, data, response) => {
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


## measurementsGetV1V1MeasurementsGet

> Object measurementsGetV1V1MeasurementsGet(opts)

Measurements Get V1

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.measurementsGetV1V1MeasurementsGet(opts, (error, data, response) => {
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


## parametersGetv1V1ParametersGet

> OpenAQParametersResult parametersGetv1V1ParametersGet(opts)

Parameters Getv1

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
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
apiInstance.parametersGetv1V1ParametersGet(opts, (error, data, response) => {
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


## sourcesV1GetV1SourcesGet

> OpenAQResult sourcesV1GetV1SourcesGet(opts)

Sources V1 Get

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.V1Api();
let opts = {
  'limit': 100, // Number | Change the number of results returned.
  'page': 1, // Number | Paginate through results.
  'offset': 0, // Number | 
  'sort': new OpenAq.Sort(), // Sort | Define sort order.
  'name': "name_example", // String | 
  'orderBy': new OpenAq.SourcesV1Order() // SourcesV1Order | 
};
apiInstance.sourcesV1GetV1SourcesGet(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **orderBy** | [**SourcesV1Order**](.md)|  | [optional] 

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

