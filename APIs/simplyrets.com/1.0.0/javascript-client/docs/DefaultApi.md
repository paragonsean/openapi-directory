# SimplyRets.DefaultApi

All URIs are relative to *https://api.simplyrets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openhousesGet**](DefaultApi.md#openhousesGet) | **GET** /openhouses | The SimplyRETS OpenHouses API
[**openhousesOpenHouseKeyGet**](DefaultApi.md#openhousesOpenHouseKeyGet) | **GET** /openhouses/{openHouseKey} | Single OpenHouse Endpoint
[**propertiesGet**](DefaultApi.md#propertiesGet) | **GET** /properties | The SimplyRETS Listings API
[**propertiesMlsIdGet**](DefaultApi.md#propertiesMlsIdGet) | **GET** /properties/{mlsId} | Single Listing Endpoint



## openhousesGet

> [OpenHouse] openhousesGet(opts)

The SimplyRETS OpenHouses API

This is the main endpoint for accessing openhouses. 

### Example

```javascript
import SimplyRets from 'simply_rets';
let defaultClient = SimplyRets.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new SimplyRets.DefaultApi();
let opts = {
  'type': "type_example", // String | Request listings by a specific property type. This defaults to Residential, and you can only specify one type in a single query. 
  'listingId': "listingId_example", // String | Request openhouses for a specific `listingId`. 
  'cities': ["null"], // [String] | Filter the openhouses returned by a list of valid cities.  The `cities` query parameter is case-insensitive.  The list of `cities` provided by your RETS vendor can be seen by sending an `OPTIONS` request to the `/properties` endpoint:  `curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses` 
  'brokers': ["null"], // [String] | Filter the listings returned by brokerage with a Broker ID. You can specific multiple broker parameters. Note, the Broker ID is provided by your MLS. 
  'agent': "agent_example", // String | Filter the listings returned by an agent ID.  Note, the Agent ID is provided by your MLS. 
  'minprice': 56, // Number | Filter listings by a minimum price. 
  'startdate': new Date("2013-10-20T19:20:30+01:00"), // Date | Scheduled date and time of the open house showing
  'offset': 56, // Number | Increase the offset parameter by the limit to go to the next \"page\" of listings. Also take a look at the Link HTTP Header for pre-built pagination.  *NOTE:* Use the `lastId` parameter for pagination. 
  'lastId': 56, // Number | Used as a cursor for pagination. 
  'limit': 56, // Number | Set the number of listings to return in the response. This defaults to 20 listings, and can be a maximum of 500. To paginate through to the next page of listings, take a look at the `offset` parameter, or the Link in the HTTP Header. 
  'sort': "sort_example", // String | Sort the response by a specific field. Values starting with a minus (-) denote descending order, while the others are ascending. 
  'include': ["null"] // [String] | Include a extra fields which are not in the default response body - 'association' includes additional HOA data - 'agreement' information on the listing agreement - 'garageSpaces' additional garage data - 'maintenanceExpense' data on maintenance expenses - 'parking' additional parking data - 'pool' includes an additional pool description - 'taxAnnualAmount' include the annual tax amount - 'taxYear' include the tax year data - 'rooms' include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an 'include' may become available by default. 
};
apiInstance.openhousesGet(opts, (error, data, response) => {
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
 **type** | **String**| Request listings by a specific property type. This defaults to Residential, and you can only specify one type in a single query.  | [optional] 
 **listingId** | **String**| Request openhouses for a specific &#x60;listingId&#x60;.  | [optional] 
 **cities** | [**[String]**](String.md)| Filter the openhouses returned by a list of valid cities.  The &#x60;cities&#x60; query parameter is case-insensitive.  The list of &#x60;cities&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses&#x60;  | [optional] 
 **brokers** | [**[String]**](String.md)| Filter the listings returned by brokerage with a Broker ID. You can specific multiple broker parameters. Note, the Broker ID is provided by your MLS.  | [optional] 
 **agent** | **String**| Filter the listings returned by an agent ID.  Note, the Agent ID is provided by your MLS.  | [optional] 
 **minprice** | **Number**| Filter listings by a minimum price.  | [optional] 
 **startdate** | **Date**| Scheduled date and time of the open house showing | [optional] 
 **offset** | **Number**| Increase the offset parameter by the limit to go to the next \&quot;page\&quot; of listings. Also take a look at the Link HTTP Header for pre-built pagination.  *NOTE:* Use the &#x60;lastId&#x60; parameter for pagination.  | [optional] 
 **lastId** | **Number**| Used as a cursor for pagination.  | [optional] 
 **limit** | **Number**| Set the number of listings to return in the response. This defaults to 20 listings, and can be a maximum of 500. To paginate through to the next page of listings, take a look at the &#x60;offset&#x60; parameter, or the Link in the HTTP Header.  | [optional] 
 **sort** | **String**| Sort the response by a specific field. Values starting with a minus (-) denote descending order, while the others are ascending.  | [optional] 
 **include** | [**[String]**](String.md)| Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;taxAnnualAmount&#39; include the annual tax amount - &#39;taxYear&#39; include the tax year data - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an &#39;include&#39; may become available by default.  | [optional] 

### Return type

[**[OpenHouse]**](OpenHouse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.simplyrets-v0.1+json


## openhousesOpenHouseKeyGet

> OpenHouse openhousesOpenHouseKeyGet(openHouseKey, opts)

Single OpenHouse Endpoint

Use this endpoint for accessing a single OpenHouse. 

### Example

```javascript
import SimplyRets from 'simply_rets';
let defaultClient = SimplyRets.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new SimplyRets.DefaultApi();
let openHouseKey = 189018; // Number | A unique OpenHouse identification key
let opts = {
  'include': ["null"] // [String] | Include a extra fields which are not in the default response body - 'association' includes additional HOA data - 'agreement' information on the listing agreement - 'garageSpaces' additional garage data - 'maintenanceExpense' data on maintenance expenses - 'parking' additional parking data - 'pool' includes an additional pool description - 'taxAnnualAmount' include the annual tax amount - 'taxYear' include the tax year data - 'rooms' include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an 'include' may become available by default. 
};
apiInstance.openhousesOpenHouseKeyGet(openHouseKey, opts, (error, data, response) => {
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
 **openHouseKey** | **Number**| A unique OpenHouse identification key | [default to 189018]
 **include** | [**[String]**](String.md)| Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;taxAnnualAmount&#39; include the annual tax amount - &#39;taxYear&#39; include the tax year data - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an &#39;include&#39; may become available by default.  | [optional] 

### Return type

[**OpenHouse**](OpenHouse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.simplyrets-v0.1+json


## propertiesGet

> [Listing] propertiesGet(opts)

The SimplyRETS Listings API

This is the main endpoint for accessing your properties. View all of the available query parameters and make requests below! The API uses Basic Authentication, which most HTTP libraries will handle for you. To use the test data (which is what this pages uses), you can use the api key &#x60;simplyrets&#x60; and secret &#x60;simplyrets&#x60;. Note that these test listings are not live MLS listings but the data, query parameters, and response bodies will all work the same. 

### Example

```javascript
import SimplyRets from 'simply_rets';
let defaultClient = SimplyRets.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new SimplyRets.DefaultApi();
let opts = {
  'q': "q_example", // String | A textual keyword search. This parameter will search  the following fields, when available:   - listingId (This does _not_ search the `mlsId` field in the SimplyRETS response body)   - street number   - street name   - mls area (major)   - city   - subdivision name   - postal code 
  'status': ["null"], // [String] | Request listings by a specific status. This parameter defaults to active and you can specify multiple statuses in a single query.  Listing statuses depend on your MLS's availability. Below is a brief description of each status with possible synonyms which may map to your MLS-specific statuses - *Active*: Active Listing which is still on the market - *ActiveUnderContract*: An offer has been accepted but the listing is still on market. Synonyms: Accepting Backup Offers, Backup Offer, Active With Accepted. Synonyms: Offer, Backup, Contingent - *Pending*: An offer has been accepted and the listing is no longer on market. Synonyms: Offer Accepted, Under Contract - *Hold*: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - *Withdrawn*: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - *Closed*: The purchase agreement has been fulfilled or the lease   agreement has been executed. Synonyms: Sold, Leased, Rented, Closed Sale - *Expired*: The listing contract has expired - *Delete*: The listing contract was never valid or other reason for the contract to be nullified. Synonyms: Kill, Zap - *Incomplete*: The listing has not yet be completely entered and is not yet   published in the MLS. Synonyms: Draft, Partially Complted - *ComingSoon* 
  'type': ["null"], // [String] | Request listings by a specific property type. This defaults to Residential and Rental. You can specify multiple property types in a single query. 
  'subtype': ["null"], // [String] | Request listings by a specific property sub type.  *NOTE* not all sub type filters are available for all vendors. 
  'agent': "agent_example", // String | Filter the listings returned by an agent ID.  Note, the Agent ID is provided by your MLS.  The co-listing agent is not included in this query parameter. 
  'brokers': ["null"], // [String] | Filter the listings returned by brokerage with a Broker ID. For some MLS areas, this is the ListOfficeId (Listing Office ID).  You can specific multiple broker parameters. Note, this query parameter is only available if a Broker ID is provided by your MLS. 
  'minprice': 56, // Number | Filter listings by a minimum price. 
  'maxprice': 56, // Number | Filter listings by a maximum price 
  'minarea': 56, // Number | Filter listings by a minimum area size in Sq Ft. 
  'maxarea': 56, // Number | Filter listings by a maximum area size in Sq Ft. 
  'minbaths': 56, // Number | Filter listings by a minimum number of bathrooms. 
  'maxbaths': 56, // Number | Filter listings by a maximum number of bathrooms. 
  'minbeds': 56, // Number | Filter listings by a minimum number of bedrooms. 
  'maxbeds': 56, // Number | Filter listings by a maximum number of bedrooms. 
  'maxdom': 56, // Number | Filter listings by a maximum number of days on market. _Note that your MLS must provide Days on Market data._ 
  'minyear': 56, // Number | Filter listings by a setting a minimum year built. 
  'limit': 56, // Number | Set the number of listings to return in the response. This defaults to 20 listings, and can be a maximum of 500. To paginate through to the next page of listings, take a look at the `offset` parameter, or the Link in the HTTP Header. 
  'offset': 56, // Number | Increase the offset parameter by the limit to go to the next \"page\" of listings. Also take a look at the Link HTTP Header for pre-built pagination.  *NOTE:* Use the `lastId` field to paginate response  *NOTE:* If you're offset is too high, you will receive an `HTTP 400 offset too high` error message. 
  'lastId': 56, // Number | Used as a cursor for pagination. When using `lastId`, the `sort` parameter will not work. 
  'vendor': "vendor_example", // String | Used to specify the vendor (MLS) to search from. This parameter is required on multi-MLS apps, and you can only query one vendor at a time. To get your vendor id's make an OPTIONS request to https://api.simplyrets.com.  `curl -XOPTIONS https://api.simplyrets.com/properties` 
  'postalCodes': ["null"], // [String] | Filter the listings returned by postal codes / zip code. You can specify multiple. 
  'features': ["null"], // [String] | Filter the listings by specific interior features.  You can filter by multiple. For example, to filter trial listings by multiple features you can use, Return listings that are within a set of latitude longitude coordinates. For example,  ``` Wet Bar High Ceiling ```  e.g. `https://simplyrets.com/services?features=Wet%20Bar&features=High%20Ceiling`  The list of `features` provided by your RETS vendor can be seen by sending an `OPTIONS` request to the `/properties` endpoint:  `curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/properties` 
  'water': "water_example", // String | Query water/waterfront listings only. Specify `true` to filter waterfront listings.  If you specify `water=true`, all listings with any `waterfront` value will be queried.  If you specify `water=false`, listings which are **NOT** waterfront listings will be queried.  If you specify `water=LAKE+NAME` or another valid value contained in your feed, that value will be searched 
  'neighborhoods': ["null"], // [String] | Filter the listings returned by specific neighborhoods and subdivisions. You can specify multiple `neighborhoods` by using the query parameter multiple times.  The `neighborhoods` query parameter is case-insensitive.  The list of `neighborhoods` provided by your RETS vendor can be seen by sending an `OPTIONS` request to the `/properties` endpoint:  `curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/properties` 
  'cities': ["null"], // [String] | Filter the listings returned by specific cities. You can specify multiple `cities` query parameters.  The `cities` query parameter is case-insensitive.  The list of `cities` provided by your RETS vendor can be seen by sending an `OPTIONS` request to the `/properties` endpoint:  `curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses` 
  'counties': ["null"], // [String] | Filter the listings returned by specific counties. You can specify multiple `counties` parameters.  The `counties` query parameter is case-insensitive.  The list of `counties` provided by your RETS vendor can be seen by sending an `OPTIONS` request to the `/properties` endpoint:  `curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses` 
  'points': ["null"], // [String] | Return listings that are within a set of latitude longitude coordinates. For example; ``` 29.723837,-95.69778 29.938275,-95.69778 29.938275,-95.32974 29.723837,-95.32974 ``` Note that some MLS's do not provide latitude and longitude for their listings, which is required for this parameter to work. In these cases, SimplyRETS offers a [Geocoding Addon](https://simplyrets.com/services#geocoding).  Check out our [blog post](https://simplyrets.com/blog/interactive-map-search.html) on using the `points` parameter to build a map-based app in javascript. 
  'include': ["null"], // [String] | Include a extra fields which are not in the default response body - 'association' includes additional HOA data - 'agreement' information on the listing agreement - 'garageSpaces' additional garage data - 'maintenanceExpense' data on maintenance expenses - 'parking' additional parking data - 'pool' includes an additional pool description - 'taxAnnualAmount' include the annual tax amount - 'taxYear' include the tax year data - 'rooms' include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an 'include' may become available by default. 
  'sort': "sort_example", // String | Sort the response by a specific field. Values starting with a minus (-) denote descending order, while the others are ascending. 
  'count': 56 // Number | When set to `false`, The `X-Total-Count` header will not be returned  Counting the listings can contribute to slower API calls due to the extra queries that need to be run to get an exact count.  Disabling count can increase query speeds. 
};
apiInstance.propertiesGet(opts, (error, data, response) => {
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
 **q** | **String**| A textual keyword search. This parameter will search  the following fields, when available:   - listingId (This does _not_ search the &#x60;mlsId&#x60; field in the SimplyRETS response body)   - street number   - street name   - mls area (major)   - city   - subdivision name   - postal code  | [optional] 
 **status** | [**[String]**](String.md)| Request listings by a specific status. This parameter defaults to active and you can specify multiple statuses in a single query.  Listing statuses depend on your MLS&#39;s availability. Below is a brief description of each status with possible synonyms which may map to your MLS-specific statuses - *Active*: Active Listing which is still on the market - *ActiveUnderContract*: An offer has been accepted but the listing is still on market. Synonyms: Accepting Backup Offers, Backup Offer, Active With Accepted. Synonyms: Offer, Backup, Contingent - *Pending*: An offer has been accepted and the listing is no longer on market. Synonyms: Offer Accepted, Under Contract - *Hold*: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - *Withdrawn*: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - *Closed*: The purchase agreement has been fulfilled or the lease   agreement has been executed. Synonyms: Sold, Leased, Rented, Closed Sale - *Expired*: The listing contract has expired - *Delete*: The listing contract was never valid or other reason for the contract to be nullified. Synonyms: Kill, Zap - *Incomplete*: The listing has not yet be completely entered and is not yet   published in the MLS. Synonyms: Draft, Partially Complted - *ComingSoon*  | [optional] 
 **type** | [**[String]**](String.md)| Request listings by a specific property type. This defaults to Residential and Rental. You can specify multiple property types in a single query.  | [optional] 
 **subtype** | [**[String]**](String.md)| Request listings by a specific property sub type.  *NOTE* not all sub type filters are available for all vendors.  | [optional] 
 **agent** | **String**| Filter the listings returned by an agent ID.  Note, the Agent ID is provided by your MLS.  The co-listing agent is not included in this query parameter.  | [optional] 
 **brokers** | [**[String]**](String.md)| Filter the listings returned by brokerage with a Broker ID. For some MLS areas, this is the ListOfficeId (Listing Office ID).  You can specific multiple broker parameters. Note, this query parameter is only available if a Broker ID is provided by your MLS.  | [optional] 
 **minprice** | **Number**| Filter listings by a minimum price.  | [optional] 
 **maxprice** | **Number**| Filter listings by a maximum price  | [optional] 
 **minarea** | **Number**| Filter listings by a minimum area size in Sq Ft.  | [optional] 
 **maxarea** | **Number**| Filter listings by a maximum area size in Sq Ft.  | [optional] 
 **minbaths** | **Number**| Filter listings by a minimum number of bathrooms.  | [optional] 
 **maxbaths** | **Number**| Filter listings by a maximum number of bathrooms.  | [optional] 
 **minbeds** | **Number**| Filter listings by a minimum number of bedrooms.  | [optional] 
 **maxbeds** | **Number**| Filter listings by a maximum number of bedrooms.  | [optional] 
 **maxdom** | **Number**| Filter listings by a maximum number of days on market. _Note that your MLS must provide Days on Market data._  | [optional] 
 **minyear** | **Number**| Filter listings by a setting a minimum year built.  | [optional] 
 **limit** | **Number**| Set the number of listings to return in the response. This defaults to 20 listings, and can be a maximum of 500. To paginate through to the next page of listings, take a look at the &#x60;offset&#x60; parameter, or the Link in the HTTP Header.  | [optional] 
 **offset** | **Number**| Increase the offset parameter by the limit to go to the next \&quot;page\&quot; of listings. Also take a look at the Link HTTP Header for pre-built pagination.  *NOTE:* Use the &#x60;lastId&#x60; field to paginate response  *NOTE:* If you&#39;re offset is too high, you will receive an &#x60;HTTP 400 offset too high&#x60; error message.  | [optional] 
 **lastId** | **Number**| Used as a cursor for pagination. When using &#x60;lastId&#x60;, the &#x60;sort&#x60; parameter will not work.  | [optional] 
 **vendor** | **String**| Used to specify the vendor (MLS) to search from. This parameter is required on multi-MLS apps, and you can only query one vendor at a time. To get your vendor id&#39;s make an OPTIONS request to https://api.simplyrets.com.  &#x60;curl -XOPTIONS https://api.simplyrets.com/properties&#x60;  | [optional] 
 **postalCodes** | [**[String]**](String.md)| Filter the listings returned by postal codes / zip code. You can specify multiple.  | [optional] 
 **features** | [**[String]**](String.md)| Filter the listings by specific interior features.  You can filter by multiple. For example, to filter trial listings by multiple features you can use, Return listings that are within a set of latitude longitude coordinates. For example,  &#x60;&#x60;&#x60; Wet Bar High Ceiling &#x60;&#x60;&#x60;  e.g. &#x60;https://simplyrets.com/services?features&#x3D;Wet%20Bar&amp;features&#x3D;High%20Ceiling&#x60;  The list of &#x60;features&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/properties&#x60;  | [optional] 
 **water** | **String**| Query water/waterfront listings only. Specify &#x60;true&#x60; to filter waterfront listings.  If you specify &#x60;water&#x3D;true&#x60;, all listings with any &#x60;waterfront&#x60; value will be queried.  If you specify &#x60;water&#x3D;false&#x60;, listings which are **NOT** waterfront listings will be queried.  If you specify &#x60;water&#x3D;LAKE+NAME&#x60; or another valid value contained in your feed, that value will be searched  | [optional] 
 **neighborhoods** | [**[String]**](String.md)| Filter the listings returned by specific neighborhoods and subdivisions. You can specify multiple &#x60;neighborhoods&#x60; by using the query parameter multiple times.  The &#x60;neighborhoods&#x60; query parameter is case-insensitive.  The list of &#x60;neighborhoods&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/properties&#x60;  | [optional] 
 **cities** | [**[String]**](String.md)| Filter the listings returned by specific cities. You can specify multiple &#x60;cities&#x60; query parameters.  The &#x60;cities&#x60; query parameter is case-insensitive.  The list of &#x60;cities&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses&#x60;  | [optional] 
 **counties** | [**[String]**](String.md)| Filter the listings returned by specific counties. You can specify multiple &#x60;counties&#x60; parameters.  The &#x60;counties&#x60; query parameter is case-insensitive.  The list of &#x60;counties&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses&#x60;  | [optional] 
 **points** | [**[String]**](String.md)| Return listings that are within a set of latitude longitude coordinates. For example; &#x60;&#x60;&#x60; 29.723837,-95.69778 29.938275,-95.69778 29.938275,-95.32974 29.723837,-95.32974 &#x60;&#x60;&#x60; Note that some MLS&#39;s do not provide latitude and longitude for their listings, which is required for this parameter to work. In these cases, SimplyRETS offers a [Geocoding Addon](https://simplyrets.com/services#geocoding).  Check out our [blog post](https://simplyrets.com/blog/interactive-map-search.html) on using the &#x60;points&#x60; parameter to build a map-based app in javascript.  | [optional] 
 **include** | [**[String]**](String.md)| Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;taxAnnualAmount&#39; include the annual tax amount - &#39;taxYear&#39; include the tax year data - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an &#39;include&#39; may become available by default.  | [optional] 
 **sort** | **String**| Sort the response by a specific field. Values starting with a minus (-) denote descending order, while the others are ascending.  | [optional] 
 **count** | **Number**| When set to &#x60;false&#x60;, The &#x60;X-Total-Count&#x60; header will not be returned  Counting the listings can contribute to slower API calls due to the extra queries that need to be run to get an exact count.  Disabling count can increase query speeds.  | [optional] 

### Return type

[**[Listing]**](Listing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.simplyrets-v0.1+json


## propertiesMlsIdGet

> Listing propertiesMlsIdGet(mlsId, opts)

Single Listing Endpoint

Use this endpoint for accessing a single listing. When you make a search to the &#x60;/properties&#x60; endpoint, each listing in the response will contain a unique &#x60;mlsId&#x60; field which should be used to request that listing on this route.  The &#x60;mlsId&#x60; field is a unique identifier for a listing which is specific to the SimplyRETS API only.  It is different from the &#x60;listingId&#x60; field is the public number given to a listing by the MLS and is not used here. 

### Example

```javascript
import SimplyRets from 'simply_rets';
let defaultClient = SimplyRets.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new SimplyRets.DefaultApi();
let mlsId = 1005252; // Number | The `mlsId` field is a unique identifier which is specific to the SimplyRETS API only.  This field is different from the `listingId` field (which is the public number given to a listing by the MLS and is not used here). 
let opts = {
  'include': ["null"] // [String] | Include a extra fields which are not in the default response body - 'association' includes additional HOA data - 'agreement' information on the listing agreement - 'garageSpaces' additional garage data - 'maintenanceExpense' data on maintenance expenses - 'parking' additional parking data - 'pool' includes an additional pool description - 'rooms' include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available with valid data in the API response. If your MLS does not offer these fields, they will contain 'null'.  In the future, fields which require an 'include' may become available by default. 
};
apiInstance.propertiesMlsIdGet(mlsId, opts, (error, data, response) => {
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
 **mlsId** | **Number**| The &#x60;mlsId&#x60; field is a unique identifier which is specific to the SimplyRETS API only.  This field is different from the &#x60;listingId&#x60; field (which is the public number given to a listing by the MLS and is not used here).  | [default to 1005252]
 **include** | [**[String]**](String.md)| Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available with valid data in the API response. If your MLS does not offer these fields, they will contain &#39;null&#39;.  In the future, fields which require an &#39;include&#39; may become available by default.  | [optional] 

### Return type

[**Listing**](Listing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.simplyrets-v0.1+json

