# MarketcheckApis.CarsMarketAPIApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fareValue**](CarsMarketAPIApi.md#fareValue) | **GET** /predict/car/uk/fmv | Predict fare value of car for UK based on YMMT &amp; miles
[**getDailyStats**](CarsMarketAPIApi.md#getDailyStats) | **GET** /stats/car | Price, Miles and Days on Market stats
[**getMDS**](CarsMarketAPIApi.md#getMDS) | **GET** /mds/car | Market Days Supply
[**getPopularCars**](CarsMarketAPIApi.md#getPopularCars) | **GET** /popular/cars | Get make model wise top 50 popular cars on national, state, city level
[**getSalesCount**](CarsMarketAPIApi.md#getSalesCount) | **GET** /sales/car | Get sales count by make, model, year, trim or taxonomy vin
[**predictCarPrice**](CarsMarketAPIApi.md#predictCarPrice) | **GET** /predict/car/price | Predict car price based on it&#39;s specifications
[**predictUkCarPrice**](CarsMarketAPIApi.md#predictUkCarPrice) | **GET** /predict/car/uk/price | Predict car price for UK based on it&#39;s specifications



## fareValue

> FareValue fareValue(opts)

Predict fare value of car for UK based on YMMT &amp; miles

Predict fare value of car for UK based on YMMT &amp; miles

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'vrm': "vrm_example", // String | Predict price for a VRM
  'year': 56, // Number | Car manufacturing year
  'make': "make_example", // String | Car's make
  'model': "model_example", // String | Car's model
  'variant': "variant_example", // String | Car's variant
  'miles': 56, // Number | miles vehicle has driven in total
  'postalCode': "postalCode_example", // String | Postal code of the car
  'radius': 56 // Number | Radius around the search location (Unit - Miles)
};
apiInstance.fareValue(opts, (error, data, response) => {
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
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **vrm** | **String**| Predict price for a VRM | [optional] 
 **year** | **Number**| Car manufacturing year | [optional] 
 **make** | **String**| Car&#39;s make | [optional] 
 **model** | **String**| Car&#39;s model | [optional] 
 **variant** | **String**| Car&#39;s variant | [optional] 
 **miles** | **Number**| miles vehicle has driven in total | [optional] 
 **postalCode** | **String**| Postal code of the car | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 

### Return type

[**FareValue**](FareValue.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDailyStats

> DailyStats getDailyStats(opts)

Price, Miles and Days on Market stats

National, state and city level stats for price, miles and dom

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'country': "'us'", // String | Country for which the stats are to be searched
  'carType': "'used'", // String | Inventory type for which stats are to be searched, default is used
  'ymm': "ymm_example", // String | Year, Make, Model of the car, Separated by pipe e.g. ymm=2015|ford|f-150
  'ymmt': "ymmt_example", // String | Year, Make, Model, Trim of the car, Separated by pipe e.g. ymmt=2015|ford|f-150|platinum
  'taxonomyVin': "taxonomyVin_example", // String | Taxonomy vin for referance to find stats of similar cars
  'vin': "vin_example", // String | VIN that will be transformed to taxonomy_vin
  'state': "state_example", // String | State level stats
  'cityState': "cityState_example" // String | City level stats, pipe seperated like city_state=jacksonville|FL
};
apiInstance.getDailyStats(opts, (error, data, response) => {
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
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **country** | **String**| Country for which the stats are to be searched | [optional] [default to &#39;us&#39;]
 **carType** | **String**| Inventory type for which stats are to be searched, default is used | [optional] [default to &#39;used&#39;]
 **ymm** | **String**| Year, Make, Model of the car, Separated by pipe e.g. ymm&#x3D;2015|ford|f-150 | [optional] 
 **ymmt** | **String**| Year, Make, Model, Trim of the car, Separated by pipe e.g. ymmt&#x3D;2015|ford|f-150|platinum | [optional] 
 **taxonomyVin** | **String**| Taxonomy vin for referance to find stats of similar cars | [optional] 
 **vin** | **String**| VIN that will be transformed to taxonomy_vin | [optional] 
 **state** | **String**| State level stats | [optional] 
 **cityState** | **String**| City level stats, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] 

### Return type

[**DailyStats**](DailyStats.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMDS

> Mds getMDS(opts)

Market Days Supply

Get the basic information on specifications for a car identified by a valid VIN

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'vin': "vin_example", // String | VIN to decode
  'exact': false, // Boolean | Exact parameter
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'debug': false, // Boolean | Debug parameter
  'includeSold': false, // Boolean | To fetch sold vins
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'source': "source_example", // String | To filter listing on their source
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dealershipGroupName': "dealershipGroupName_example", // String | Name of the dealership group to search for
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'engineSizeRange': "engineSizeRange_example" // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
};
apiInstance.getMDS(opts, (error, data, response) => {
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
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **vin** | **String**| VIN to decode | [optional] 
 **exact** | **Boolean**| Exact parameter | [optional] [default to false]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **debug** | **Boolean**| Debug parameter | [optional] [default to false]
 **includeSold** | **Boolean**| To fetch sold vins | [optional] [default to false]
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **source** | **String**| To filter listing on their source | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 

### Return type

[**Mds**](Mds.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPopularCars

> PopularCars getPopularCars(carType, opts)

Get make model wise top 50 popular cars on national, state, city level

Get make model wise top 50 popular cars on national, state, city level

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let carType = "carType_example"; // String | Inventory type for which popular count is to be searched
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'state': "state_example", // String | State level sales count
  'cityState': "cityState_example", // String | City level sales count, pipe seperated like city_state=jacksonville|FL
  'country': "'us'" // String | Country for which the popular cars are to be searched
};
apiInstance.getPopularCars(carType, opts, (error, data, response) => {
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
 **carType** | **String**| Inventory type for which popular count is to be searched | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **state** | **String**| State level sales count | [optional] 
 **cityState** | **String**| City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] 
 **country** | **String**| Country for which the popular cars are to be searched | [optional] [default to &#39;us&#39;]

### Return type

[**PopularCars**](PopularCars.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSalesCount

> Sales getSalesCount(opts)

Get sales count by make, model, year, trim or taxonomy vin

Get a sales count for city, state or national level by make, model, year, trim or taxonomy vin

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'carType': "'used'", // String | Inventory type for which sales count is to be searched, default is used
  'make': "make_example", // String | Make for which sales count is to be searched
  'mm': "mm_example", // String | Make-Model for which sales count is to be searched, pipe seperated like mm=ford|f-150
  'ymm': "ymm_example", // String | Year-Make-Model for which sales count is to be searched, pipe seperated like ymm=2015|ford|f-150
  'ymmt': "ymmt_example", // String | Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt=2015|ford|f-150|platinum
  'taxonomyVin': "taxonomyVin_example", // String | taxonomy_vin for which sales count is to be searched
  'state': "state_example", // String | State level sales count
  'cityState': "cityState_example", // String | City level sales count, pipe seperated like city_state=jacksonville|FL
  'vin': "vin_example", // String | VIN that will be transformed to taxonomy_vin
  'country': "'us'" // String | Country for which the sales records are to be searched
};
apiInstance.getSalesCount(opts, (error, data, response) => {
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
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **carType** | **String**| Inventory type for which sales count is to be searched, default is used | [optional] [default to &#39;used&#39;]
 **make** | **String**| Make for which sales count is to be searched | [optional] 
 **mm** | **String**| Make-Model for which sales count is to be searched, pipe seperated like mm&#x3D;ford|f-150 | [optional] 
 **ymm** | **String**| Year-Make-Model for which sales count is to be searched, pipe seperated like ymm&#x3D;2015|ford|f-150 | [optional] 
 **ymmt** | **String**| Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt&#x3D;2015|ford|f-150|platinum | [optional] 
 **taxonomyVin** | **String**| taxonomy_vin for which sales count is to be searched | [optional] 
 **state** | **String**| State level sales count | [optional] 
 **cityState** | **String**| City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] 
 **vin** | **String**| VIN that will be transformed to taxonomy_vin | [optional] 
 **country** | **String**| Country for which the sales records are to be searched | [optional] [default to &#39;us&#39;]

### Return type

[**Sales**](Sales.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## predictCarPrice

> PricePrediction predictCarPrice(carType, opts)

Predict car price based on it&#39;s specifications

Predict car price based on it&#39;s specifications

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let carType = "carType_example"; // String | Car condition
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'vin': "vin_example", // String | Predict price for a VIN
  'year': 56, // Number | Car manufacturing year
  'make': "make_example", // String | Car's make
  'model': "model_example", // String | Car's model
  'trim': "trim_example", // String | Car's trim
  'isCertified': true, // Boolean | Boolean to indicate car is certified or not
  'carfax1Owner': true, // Boolean | Boolean to indicate car is carfax one owner or not
  'carfaxCleanTitle': true, // Boolean | Boolean to indicate car has clean title or not
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color of the car
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color of the car
  'transmission': "transmission_example", // String | Transmission on the car
  'drivetrain': "drivetrain_example", // String | Drivetrain on the car
  'engineSize': 3.4, // Number | Engine Size of the car
  'engineBlock': "engineBlock_example", // String | Engine Block of the car
  'cylinders': 56, // Number | Number of cylinders in the vehicle
  'doors': 56, // Number | Number of doors in the vehicle
  'highwayMpg': 56, // Number | Highway mileage
  'cityMpg': 56, // Number | City mileage of the car
  'latitude': 3.4, // Number | Latitude component of the location
  'longitude': 3.4, // Number | Longitude component of the location
  'miles': 56, // Number | miles vehicle has driven in total
  'zip': "zip_example", // String | Location zip
  'country': "'us'" // String | Country for which car price will be predicted
};
apiInstance.predictCarPrice(carType, opts, (error, data, response) => {
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
 **carType** | **String**| Car condition | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **vin** | **String**| Predict price for a VIN | [optional] 
 **year** | **Number**| Car manufacturing year | [optional] 
 **make** | **String**| Car&#39;s make | [optional] 
 **model** | **String**| Car&#39;s model | [optional] 
 **trim** | **String**| Car&#39;s trim | [optional] 
 **isCertified** | **Boolean**| Boolean to indicate car is certified or not | [optional] 
 **carfax1Owner** | **Boolean**| Boolean to indicate car is carfax one owner or not | [optional] 
 **carfaxCleanTitle** | **Boolean**| Boolean to indicate car has clean title or not | [optional] 
 **baseExteriorColor** | **String**| Base exterior color of the car | [optional] 
 **baseInteriorColor** | **String**| Base interior color of the car | [optional] 
 **transmission** | **String**| Transmission on the car | [optional] 
 **drivetrain** | **String**| Drivetrain on the car | [optional] 
 **engineSize** | **Number**| Engine Size of the car | [optional] 
 **engineBlock** | **String**| Engine Block of the car | [optional] 
 **cylinders** | **Number**| Number of cylinders in the vehicle | [optional] 
 **doors** | **Number**| Number of doors in the vehicle | [optional] 
 **highwayMpg** | **Number**| Highway mileage | [optional] 
 **cityMpg** | **Number**| City mileage of the car | [optional] 
 **latitude** | **Number**| Latitude component of the location | [optional] 
 **longitude** | **Number**| Longitude component of the location | [optional] 
 **miles** | **Number**| miles vehicle has driven in total | [optional] 
 **zip** | **String**| Location zip | [optional] 
 **country** | **String**| Country for which car price will be predicted | [optional] [default to &#39;us&#39;]

### Return type

[**PricePrediction**](PricePrediction.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## predictUkCarPrice

> PricePrediction predictUkCarPrice(opts)

Predict car price for UK based on it&#39;s specifications

Predict car price for UK based on it&#39;s specifications

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsMarketAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'vrm': "vrm_example", // String | Predict price for a VRM
  'year': 56, // Number | Car manufacturing year
  'make': "make_example", // String | Car's make
  'model': "model_example", // String | Car's model
  'trim': "trim_example", // String | Car's trim
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color of the car
  'transmission': "transmission_example", // String | Transmission on the car
  'drivetrain': "drivetrain_example", // String | Drivetrain on the car
  'engineSize': 3.4, // Number | Engine Size of the car
  'cylinders': 56, // Number | Number of cylinders in the vehicle
  'doors': 56, // Number | Number of doors in the vehicle
  'fuelType': "fuelType_example", // String | Fuel type of the car
  'highwayMpg': 3.4, // Number | Highway mileage
  'cityMpg': 3.4, // Number | City mileage of the car
  'combinedMpg': 3.4, // Number | Combiined mileage of the car
  'latitude': 3.4, // Number | Latitude component of the location
  'longitude': 3.4, // Number | Longitude component of the location
  'miles': 56, // Number | miles vehicle has driven in total
  'zip': "zip_example" // String | Location zip
};
apiInstance.predictUkCarPrice(opts, (error, data, response) => {
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
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **vrm** | **String**| Predict price for a VRM | [optional] 
 **year** | **Number**| Car manufacturing year | [optional] 
 **make** | **String**| Car&#39;s make | [optional] 
 **model** | **String**| Car&#39;s model | [optional] 
 **trim** | **String**| Car&#39;s trim | [optional] 
 **baseExteriorColor** | **String**| Base exterior color of the car | [optional] 
 **transmission** | **String**| Transmission on the car | [optional] 
 **drivetrain** | **String**| Drivetrain on the car | [optional] 
 **engineSize** | **Number**| Engine Size of the car | [optional] 
 **cylinders** | **Number**| Number of cylinders in the vehicle | [optional] 
 **doors** | **Number**| Number of doors in the vehicle | [optional] 
 **fuelType** | **String**| Fuel type of the car | [optional] 
 **highwayMpg** | **Number**| Highway mileage | [optional] 
 **cityMpg** | **Number**| City mileage of the car | [optional] 
 **combinedMpg** | **Number**| Combiined mileage of the car | [optional] 
 **latitude** | **Number**| Latitude component of the location | [optional] 
 **longitude** | **Number**| Longitude component of the location | [optional] 
 **miles** | **Number**| miles vehicle has driven in total | [optional] 
 **zip** | **String**| Location zip | [optional] 

### Return type

[**PricePrediction**](PricePrediction.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

