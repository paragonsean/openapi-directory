# SlideRoomApiV2.ApplicationApi

All URIs are relative to *https://api.slideroom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationDeleteAttributesV2**](ApplicationApi.md#applicationDeleteAttributesV2) | **DELETE** /api/v2/application/{applicationId}/attributes | Deletes a custom attribute for an application.
[**applicationGetAttributeNamesV2**](ApplicationApi.md#applicationGetAttributeNamesV2) | **GET** /api/v2/application/attributes/names | Gets the custom application attributes used by the organization.
[**applicationGetAttributesV2**](ApplicationApi.md#applicationGetAttributesV2) | **GET** /api/v2/application/{applicationId}/attributes | Gets the custom attributes for an application.
[**applicationPostAttributesV2**](ApplicationApi.md#applicationPostAttributesV2) | **POST** /api/v2/application/{applicationId}/attributes | Updates the custom attributes for an application. API Import is available in the Advanced Plan.
[**applicationRequestExportByApplicationIdV2**](ApplicationApi.md#applicationRequestExportByApplicationIdV2) | **POST** /api/v2/application/{applicationId}/request-export | Requests the generation of a single application export file (tabular, pdf, zip).
[**applicationRequestExportV2**](ApplicationApi.md#applicationRequestExportV2) | **POST** /api/v2/application/request-export | Requests the generation of application export files (tabular, pdf, zip).



## applicationDeleteAttributesV2

> String applicationDeleteAttributesV2(applicationId, name)

Deletes a custom attribute for an application.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicationApi();
let applicationId = "applicationId_example"; // String | The ID of the application.
let name = "name_example"; // String | The name of the attribute to be deleted.
apiInstance.applicationDeleteAttributesV2(applicationId, name, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application. | 
 **name** | **String**| The name of the attribute to be deleted. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## applicationGetAttributeNamesV2

> [String] applicationGetAttributeNamesV2()

Gets the custom application attributes used by the organization.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicationApi();
apiInstance.applicationGetAttributeNamesV2((error, data, response) => {
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


## applicationGetAttributesV2

> {String: String} applicationGetAttributesV2(applicationId)

Gets the custom attributes for an application.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicationApi();
let applicationId = "applicationId_example"; // String | The ID of the application.
apiInstance.applicationGetAttributesV2(applicationId, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application. | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## applicationPostAttributesV2

> String applicationPostAttributesV2(applicationId, data)

Updates the custom attributes for an application. API Import is available in the Advanced Plan.

This method only adds or updates attributes. Null values will be updated as nulls, but not deleted.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicationApi();
let applicationId = "applicationId_example"; // String | The ID of the application.
let data = {key: "null"}; // {String: String} | The name/value pairs of the attributes.
apiInstance.applicationPostAttributesV2(applicationId, data, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application. | 
 **data** | [**{String: String}**](String.md)| The name/value pairs of the attributes. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## applicationRequestExportByApplicationIdV2

> RequestApplicationExportResultV2 applicationRequestExportByApplicationIdV2(applicationId, opts)

Requests the generation of a single application export file (tabular, pdf, zip).

Exports are generated asynchronously within SlideRoom.  To retrieve the export file generated by this request, use the api/v#/export/{token} endpoint to check the progress/result of the generation process.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicationApi();
let applicationId = "applicationId_example"; // String | The id of the application to export
let opts = {
  'format': "format_example", // String | 
  'roundType': "roundType_example", // String | 
  'roundName': "roundName_example", // String | 
  'tabExport': "tabExport_example", // String | 
  'pdfIncludeForms': true, // Boolean | 
  'pdfIncludeReferences': true, // Boolean | 
  'pdfIncludeMedia': true, // Boolean | 
  'pdfIncludeApplicantAttachments': true, // Boolean | 
  'pdfIncludeOrganizationAttachments': true, // Boolean | 
  'pdfIncludeRatings': true, // Boolean | 
  'pdfIncludeFullPageMedia': true, // Boolean | 
  'pdfIncludeHighlights': true, // Boolean | 
  'pdfIncludeComments': true, // Boolean | 
  'pdfIncludeCommonApp': true, // Boolean | 
  'zipOriginalMedia': true, // Boolean | 
  'zipIncludeForms': true, // Boolean | 
  'zipIncludeReferences': true, // Boolean | 
  'zipIncludeMedia': true, // Boolean | 
  'zipIncludeApplicantAttachments': true, // Boolean | 
  'zipIncludeOrganizationAttachments': true, // Boolean | 
  'zipIncludeRatings': true, // Boolean | 
  'zipIncludeComments': true, // Boolean | 
  'zipIncludeCommonApp': true, // Boolean | 
  'deliveryAccount': "deliveryAccount_example", // String | 
  'deliveryFolder': "deliveryFolder_example" // String | 
};
apiInstance.applicationRequestExportByApplicationIdV2(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The id of the application to export | 
 **format** | **String**|  | [optional] 
 **roundType** | **String**|  | [optional] 
 **roundName** | **String**|  | [optional] 
 **tabExport** | **String**|  | [optional] 
 **pdfIncludeForms** | **Boolean**|  | [optional] 
 **pdfIncludeReferences** | **Boolean**|  | [optional] 
 **pdfIncludeMedia** | **Boolean**|  | [optional] 
 **pdfIncludeApplicantAttachments** | **Boolean**|  | [optional] 
 **pdfIncludeOrganizationAttachments** | **Boolean**|  | [optional] 
 **pdfIncludeRatings** | **Boolean**|  | [optional] 
 **pdfIncludeFullPageMedia** | **Boolean**|  | [optional] 
 **pdfIncludeHighlights** | **Boolean**|  | [optional] 
 **pdfIncludeComments** | **Boolean**|  | [optional] 
 **pdfIncludeCommonApp** | **Boolean**|  | [optional] 
 **zipOriginalMedia** | **Boolean**|  | [optional] 
 **zipIncludeForms** | **Boolean**|  | [optional] 
 **zipIncludeReferences** | **Boolean**|  | [optional] 
 **zipIncludeMedia** | **Boolean**|  | [optional] 
 **zipIncludeApplicantAttachments** | **Boolean**|  | [optional] 
 **zipIncludeOrganizationAttachments** | **Boolean**|  | [optional] 
 **zipIncludeRatings** | **Boolean**|  | [optional] 
 **zipIncludeComments** | **Boolean**|  | [optional] 
 **zipIncludeCommonApp** | **Boolean**|  | [optional] 
 **deliveryAccount** | **String**|  | [optional] 
 **deliveryFolder** | **String**|  | [optional] 

### Return type

[**RequestApplicationExportResultV2**](RequestApplicationExportResultV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## applicationRequestExportV2

> RequestApplicationExportResultV2 applicationRequestExportV2(opts)

Requests the generation of application export files (tabular, pdf, zip).

Exports are generated asynchronously within SlideRoom.  To retrieve the export file generated by this request, use the api/v#/export/{token} endpoint to check the progress/result of the generation process.  PDF and ZIP exports are available in the Advanced Plan.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ApplicationApi();
let opts = {
  'format': "format_example", // String | 
  'roundType': "roundType_example", // String | 
  'roundName': "roundName_example", // String | 
  'tabExport': "tabExport_example", // String | 
  'pdfIncludeForms': true, // Boolean | 
  'pdfIncludeReferences': true, // Boolean | 
  'pdfIncludeMedia': true, // Boolean | 
  'pdfIncludeApplicantAttachments': true, // Boolean | 
  'pdfIncludeOrganizationAttachments': true, // Boolean | 
  'pdfIncludeRatings': true, // Boolean | 
  'pdfIncludeFullPageMedia': true, // Boolean | 
  'pdfIncludeHighlights': true, // Boolean | 
  'pdfIncludeComments': true, // Boolean | 
  'pdfIncludeCommonApp': true, // Boolean | 
  'zipOriginalMedia': true, // Boolean | 
  'zipIncludeForms': true, // Boolean | 
  'zipIncludeReferences': true, // Boolean | 
  'zipIncludeMedia': true, // Boolean | 
  'zipIncludeApplicantAttachments': true, // Boolean | 
  'zipIncludeOrganizationAttachments': true, // Boolean | 
  'zipIncludeRatings': true, // Boolean | 
  'zipIncludeComments': true, // Boolean | 
  'zipIncludeCommonApp': true, // Boolean | 
  'deliveryAccount': "deliveryAccount_example", // String | 
  'deliveryFolder': "deliveryFolder_example", // String | 
  'since': 56, // Number | 
  'pool': "pool_example", // String | 
  'status': "status_example", // String | 
  'searchName': "searchName_example", // String | 
  'email': "email_example" // String | 
};
apiInstance.applicationRequestExportV2(opts, (error, data, response) => {
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
 **roundType** | **String**|  | [optional] 
 **roundName** | **String**|  | [optional] 
 **tabExport** | **String**|  | [optional] 
 **pdfIncludeForms** | **Boolean**|  | [optional] 
 **pdfIncludeReferences** | **Boolean**|  | [optional] 
 **pdfIncludeMedia** | **Boolean**|  | [optional] 
 **pdfIncludeApplicantAttachments** | **Boolean**|  | [optional] 
 **pdfIncludeOrganizationAttachments** | **Boolean**|  | [optional] 
 **pdfIncludeRatings** | **Boolean**|  | [optional] 
 **pdfIncludeFullPageMedia** | **Boolean**|  | [optional] 
 **pdfIncludeHighlights** | **Boolean**|  | [optional] 
 **pdfIncludeComments** | **Boolean**|  | [optional] 
 **pdfIncludeCommonApp** | **Boolean**|  | [optional] 
 **zipOriginalMedia** | **Boolean**|  | [optional] 
 **zipIncludeForms** | **Boolean**|  | [optional] 
 **zipIncludeReferences** | **Boolean**|  | [optional] 
 **zipIncludeMedia** | **Boolean**|  | [optional] 
 **zipIncludeApplicantAttachments** | **Boolean**|  | [optional] 
 **zipIncludeOrganizationAttachments** | **Boolean**|  | [optional] 
 **zipIncludeRatings** | **Boolean**|  | [optional] 
 **zipIncludeComments** | **Boolean**|  | [optional] 
 **zipIncludeCommonApp** | **Boolean**|  | [optional] 
 **deliveryAccount** | **String**|  | [optional] 
 **deliveryFolder** | **String**|  | [optional] 
 **since** | **Number**|  | [optional] 
 **pool** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **searchName** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 

### Return type

[**RequestApplicationExportResultV2**](RequestApplicationExportResultV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

