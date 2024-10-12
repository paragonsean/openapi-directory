# SlideRoomApiV2.ApplicantApi

All URIs are relative to *https://api.slideroom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicantDeleteAttributesV2**](ApplicantApi.md#applicantDeleteAttributesV2) | **DELETE** /api/v2/applicant/attributes | Deletes a custom attribute for an applicant.
[**applicantGetAttributeNamesV2**](ApplicantApi.md#applicantGetAttributeNamesV2) | **GET** /api/v2/applicant/attributes/names | Gets the custom applicant attributes used by the organization.
[**applicantGetAttributesV2**](ApplicantApi.md#applicantGetAttributesV2) | **GET** /api/v2/applicant/attributes | Gets the custom attributes for an applicant.
[**applicantPostAttributesV2**](ApplicantApi.md#applicantPostAttributesV2) | **POST** /api/v2/applicant/attributes | Updates the custom attributes for an applicant.



## applicantDeleteAttributesV2

> String applicantDeleteAttributesV2(email, name, opts)

Deletes a custom attribute for an applicant.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicantApi();
let email = "email_example"; // String | The email address of the applicant.
let name = "name_example"; // String | The name of the attribute to be deleted.
let opts = {
  'pool': "pool_example", // String | 
  'commonAppYear': 56 // Number | 
};
apiInstance.applicantDeleteAttributesV2(email, name, opts, (error, data, response) => {
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
 **email** | **String**| The email address of the applicant. | 
 **name** | **String**| The name of the attribute to be deleted. | 
 **pool** | **String**|  | [optional] 
 **commonAppYear** | **Number**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## applicantGetAttributeNamesV2

> [String] applicantGetAttributeNamesV2()

Gets the custom applicant attributes used by the organization.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicantApi();
apiInstance.applicantGetAttributeNamesV2((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## applicantGetAttributesV2

> {String: String} applicantGetAttributesV2(email, opts)

Gets the custom attributes for an applicant.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicantApi();
let email = "email_example"; // String | The email address of the applicant.
let opts = {
  'pool': "pool_example", // String | 
  'commonAppYear': 56 // Number | 
};
apiInstance.applicantGetAttributesV2(email, opts, (error, data, response) => {
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
 **email** | **String**| The email address of the applicant. | 
 **pool** | **String**|  | [optional] 
 **commonAppYear** | **Number**|  | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## applicantPostAttributesV2

> String applicantPostAttributesV2(email, data, opts)

Updates the custom attributes for an applicant.

This method only adds or updates attributes. Null values will be updated as nulls, but not deleted. API Import is available in the Advanced Plan.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicantApi();
let email = "email_example"; // String | The email address of the applicant.
let data = {key: "null"}; // {String: String} | The name/value pairs of the attributes.
let opts = {
  'pool': "pool_example", // String | 
  'commonAppYear': 56 // Number | 
};
apiInstance.applicantPostAttributesV2(email, data, opts, (error, data, response) => {
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
 **email** | **String**| The email address of the applicant. | 
 **data** | [**{String: String}**](String.md)| The name/value pairs of the attributes. | 
 **pool** | **String**|  | [optional] 
 **commonAppYear** | **Number**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

