# OnSchedConsumerApi.LocationsApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1LocationsGet**](LocationsApi.md#consumerV1LocationsGet) | **GET** /consumer/v1/locations | List Locations
[**consumerV1LocationsIdGet**](LocationsApi.md#consumerV1LocationsIdGet) | **GET** /consumer/v1/locations/{id} | Get Location



## consumerV1LocationsGet

> LocationListViewModel consumerV1LocationsGet(opts)

List Locations

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business Locations&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and size. Default offset is 0, and limit is 20 and maximum is 100. Use the other query parameters to filter the results further. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.LocationsApi();
let opts = {
  'name': "name_example", // String | Location name (full or partial)
  'nearestTo': "nearestTo_example", // String | Search by distance nearest Geocoords, City, Postal/Zip Code
  'proximity': 56, // Number | Maximum distance to display
  'units': "units_example", // String | Distance either imperial(miles), metric(kilometers)
  'serviceId': "serviceId_example", // String | Locations that offer this service
  'friendlyId': "friendlyId_example", // String | Frienldy Id of location
  'regionId': "regionId_example", // String | Locations within a specific region
  'ignorePrimary': true, // Boolean | Don't include the Primary Location
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit, default 20, max 100
};
apiInstance.consumerV1LocationsGet(opts, (error, data, response) => {
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
 **name** | **String**| Location name (full or partial) | [optional] 
 **nearestTo** | **String**| Search by distance nearest Geocoords, City, Postal/Zip Code | [optional] 
 **proximity** | **Number**| Maximum distance to display | [optional] 
 **units** | **String**| Distance either imperial(miles), metric(kilometers) | [optional] 
 **serviceId** | **String**| Locations that offer this service | [optional] 
 **friendlyId** | **String**| Frienldy Id of location | [optional] 
 **regionId** | **String**| Locations within a specific region | [optional] 
 **ignorePrimary** | **Boolean**| Don&#39;t include the Primary Location | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit, default 20, max 100 | [optional] 

### Return type

[**LocationListViewModel**](LocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1LocationsIdGet

> LocationViewModel consumerV1LocationsIdGet(id)

Get Location

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Location&lt;/b&gt; object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Find all location id&#39;s by using the &lt;i&gt;GET /consumer/v1/locations&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.LocationsApi();
let id = "id_example"; // String | id of business location
apiInstance.consumerV1LocationsIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of business location | 

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

