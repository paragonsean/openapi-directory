# BikeWiseApiV2.IncidentsApi

All URIs are relative to *https://bikewise.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETVersionIncidentsFormat**](IncidentsApi.md#gETVersionIncidentsFormat) | **GET** /v2/incidents | Paginated incidents matching parameters
[**gETVersionIncidentsIdFormat**](IncidentsApi.md#gETVersionIncidentsIdFormat) | **GET** /v2/incidents/{id} | 



## gETVersionIncidentsFormat

> gETVersionIncidentsFormat(opts)

Paginated incidents matching parameters

 &lt;p&gt;If you’d like more detailed information about bike incidents, use this endpoint. For mapping, &lt;code&gt;locations&lt;/code&gt; is probably a better bet.&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Notes on location searching&lt;/strong&gt;: &lt;br /&gt; - &lt;code&gt;proximity&lt;/code&gt; accepts an ip address, an address, zipcode, city, or latitude,longitude - i.e. &lt;code&gt;70.210.133.87&lt;/code&gt;, &lt;code&gt;210 NW 11th Ave, Portland, OR&lt;/code&gt;, &lt;code&gt;60647&lt;/code&gt;, &lt;code&gt;Chicago, IL&lt;/code&gt;, and &lt;code&gt;45.521728,-122.67326&lt;/code&gt; are all acceptable&lt;br /&gt; - &lt;code&gt;proximity_square&lt;/code&gt; sets the length of the sides of the square to find matches inside of. The square is centered on the location specified by &lt;code&gt;proximity&lt;/code&gt;. It defaults to 100.&lt;/p&gt; 

### Example

```javascript
import BikeWiseApiV2 from 'bike_wise_api_v2';

let apiInstance = new BikeWiseApiV2.IncidentsApi();
let opts = {
  'page': 1, // Number | <p>Page of results to fetch.</p> 
  'perPage': 56, // Number | <p>Number of results to return per page.</p> 
  'occurredBefore': 56, // Number | <p>End of period</p> 
  'occurredAfter': 56, // Number | <p>Start of period</p> 
  'incidentType': "incidentType_example", // String | <p>Only incidents of specific type</p> 
  'proximity': "proximity_example", // String | <p>Center of location for proximity search</p> 
  'proximitySquare': 100, // Number | <p>Size of the proximity search</p> 
  'query': "query_example" // String | <p>Full text search of incidents</p> 
};
apiInstance.gETVersionIncidentsFormat(opts, (error, data, response) => {
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
 **page** | **Number**| &lt;p&gt;Page of results to fetch.&lt;/p&gt;  | [optional] [default to 1]
 **perPage** | **Number**| &lt;p&gt;Number of results to return per page.&lt;/p&gt;  | [optional] 
 **occurredBefore** | **Number**| &lt;p&gt;End of period&lt;/p&gt;  | [optional] 
 **occurredAfter** | **Number**| &lt;p&gt;Start of period&lt;/p&gt;  | [optional] 
 **incidentType** | **String**| &lt;p&gt;Only incidents of specific type&lt;/p&gt;  | [optional] 
 **proximity** | **String**| &lt;p&gt;Center of location for proximity search&lt;/p&gt;  | [optional] 
 **proximitySquare** | **Number**| &lt;p&gt;Size of the proximity search&lt;/p&gt;  | [optional] [default to 100]
 **query** | **String**| &lt;p&gt;Full text search of incidents&lt;/p&gt;  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETVersionIncidentsIdFormat

> gETVersionIncidentsIdFormat(id)



### Example

```javascript
import BikeWiseApiV2 from 'bike_wise_api_v2';

let apiInstance = new BikeWiseApiV2.IncidentsApi();
let id = 56; // Number | <p>Incident ID</p> 
apiInstance.gETVersionIncidentsIdFormat(id, (error, data, response) => {
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
 **id** | **Number**| &lt;p&gt;Incident ID&lt;/p&gt;  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

