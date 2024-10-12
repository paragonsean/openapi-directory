# LetMcApiV2BasicTier2.ViewingControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viewingControllerGetBookings**](ViewingControllerApi.md#viewingControllerGetBookings) | **GET** /v2/tier2/{shortName}/viewing/bookings | Gets a list of available viewing slots for one or more properties
[**viewingControllerMakeBooking**](ViewingControllerApi.md#viewingControllerMakeBooking) | **POST** /v2/tier2/{shortName}/viewing/bookings | Book an appointment for a viewing slot returned from the GET verb



## viewingControllerGetBookings

> [ViewingBookingModel] viewingControllerGetBookings(shortName, preferredDate, propertyIDsToView)

Gets a list of available viewing slots for one or more properties

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.ViewingControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let preferredDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The preferred date for a viewing
let propertyIDsToView = ["null"]; // [String] | An array of unique IDs of properties to view
apiInstance.viewingControllerGetBookings(shortName, preferredDate, propertyIDsToView, (error, data, response) => {
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
 **preferredDate** | **Date**| The preferred date for a viewing | 
 **propertyIDsToView** | [**[String]**](String.md)| An array of unique IDs of properties to view | 

### Return type

[**[ViewingBookingModel]**](ViewingBookingModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## viewingControllerMakeBooking

> Boolean viewingControllerMakeBooking(shortName, forename, surname, mobilePhone, emailAddress, propertyIDsToView, selectedViewingSlot, opts)

Book an appointment for a viewing slot returned from the GET verb

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.ViewingControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let forename = "forename_example"; // String | The forename of the prospect
let surname = "surname_example"; // String | The surname of the prospect
let mobilePhone = "mobilePhone_example"; // String | The mobile phone number of the prospect
let emailAddress = "emailAddress_example"; // String | The email address of the prospect
let propertyIDsToView = ["null"]; // [String] | An array of unique IDs of properties to view
let selectedViewingSlot = new LetMcApiV2BasicTier2.ViewingBookingModel(); // ViewingBookingModel | The prospect's selected viewing slot
let opts = {
  'wantRoomInSharedProperty': true, // Boolean | Whether the prospect wants a shared property
  'alertMinRent': 3.4, // Number | The minimum rent amount the prospect is looking for
  'alertMaxRent': 3.4, // Number | The maximum rent amount the prospect is looking for
  'alertNumberOfBeds': 56, // Number | The minimum number of beds the prospect is looking for
  'alertAreaID': "alertAreaID_example", // String | The unique ID of the area the prospect is looking for
  'alertTenantType': "alertTenantType_example", // String | The tenanct type the prospect is looking for
  'subscribeToEmailAlerts': true, // Boolean | Whether to subscribe the prospect to email alerts
  'subscribeToSMSAlerts': true // Boolean | Whether to subscribe the prospect to SMS alerts
};
apiInstance.viewingControllerMakeBooking(shortName, forename, surname, mobilePhone, emailAddress, propertyIDsToView, selectedViewingSlot, opts, (error, data, response) => {
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
 **forename** | **String**| The forename of the prospect | 
 **surname** | **String**| The surname of the prospect | 
 **mobilePhone** | **String**| The mobile phone number of the prospect | 
 **emailAddress** | **String**| The email address of the prospect | 
 **propertyIDsToView** | [**[String]**](String.md)| An array of unique IDs of properties to view | 
 **selectedViewingSlot** | [**ViewingBookingModel**](ViewingBookingModel.md)| The prospect&#39;s selected viewing slot | 
 **wantRoomInSharedProperty** | **Boolean**| Whether the prospect wants a shared property | [optional] 
 **alertMinRent** | **Number**| The minimum rent amount the prospect is looking for | [optional] 
 **alertMaxRent** | **Number**| The maximum rent amount the prospect is looking for | [optional] 
 **alertNumberOfBeds** | **Number**| The minimum number of beds the prospect is looking for | [optional] 
 **alertAreaID** | **String**| The unique ID of the area the prospect is looking for | [optional] 
 **alertTenantType** | **String**| The tenanct type the prospect is looking for | [optional] 
 **subscribeToEmailAlerts** | **Boolean**| Whether to subscribe the prospect to email alerts | [optional] 
 **subscribeToSMSAlerts** | **Boolean**| Whether to subscribe the prospect to SMS alerts | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

