# TaggunReceiptOcrScanningApi.Class4CampaignValidationApi

All URIs are relative to *https://api.taggun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteApiValidationV1CampaignSettingsDeleteCampaignid**](Class4CampaignValidationApi.md#deleteApiValidationV1CampaignSettingsDeleteCampaignid) | **DELETE** /api/validation/v1/campaign/settings/delete/{campaignId} | delete campaign settings for a client
[**getApiValidationV1CampaignSettingsCampaignid**](Class4CampaignValidationApi.md#getApiValidationV1CampaignSettingsCampaignid) | **GET** /api/validation/v1/campaign/settings/{campaignId} | get campaign settings for a client
[**getApiValidationV1CampaignSettingsList**](Class4CampaignValidationApi.md#getApiValidationV1CampaignSettingsList) | **GET** /api/validation/v1/campaign/settings/list | list all campaign setting IDs for a client
[**postApiValidationV1CampaignFile**](Class4CampaignValidationApi.md#postApiValidationV1CampaignFile) | **POST** /api/validation/v1/campaign/file | validate and match a receipt against a campaign validation settings by uploading an image file
[**postApiValidationV1CampaignProductvalidationFile**](Class4CampaignValidationApi.md#postApiValidationV1CampaignProductvalidationFile) | **POST** /api/validation/v1/campaign/product-validation/file | validate if user-submitted info like serial number are detected an image file
[**postApiValidationV1CampaignSettingsCreateCampaignid**](Class4CampaignValidationApi.md#postApiValidationV1CampaignSettingsCreateCampaignid) | **POST** /api/validation/v1/campaign/settings/create/{campaignId} | create campaign settings for a client
[**putApiValidationV1CampaignSettingsUpdateCampaignid**](Class4CampaignValidationApi.md#putApiValidationV1CampaignSettingsUpdateCampaignid) | **PUT** /api/validation/v1/campaign/settings/update/{campaignId} | update campaign settings for a client



## deleteApiValidationV1CampaignSettingsDeleteCampaignid

> deleteApiValidationV1CampaignSettingsDeleteCampaignid(apikey, campaignId)

delete campaign settings for a client

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
let campaignId = "campaignId_example"; // String | Remove campaign settings with a campaign ID
apiInstance.deleteApiValidationV1CampaignSettingsDeleteCampaignid(apikey, campaignId, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **campaignId** | **String**| Remove campaign settings with a campaign ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getApiValidationV1CampaignSettingsCampaignid

> getApiValidationV1CampaignSettingsCampaignid(apikey, campaignId)

get campaign settings for a client

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
let campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
apiInstance.getApiValidationV1CampaignSettingsCampaignid(apikey, campaignId, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **campaignId** | **String**| The ID of the campaign to validate the receipt | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getApiValidationV1CampaignSettingsList

> getApiValidationV1CampaignSettingsList(apikey)

list all campaign setting IDs for a client

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
apiInstance.getApiValidationV1CampaignSettingsList(apikey, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postApiValidationV1CampaignFile

> String postApiValidationV1CampaignFile(apikey, campaignId, opts)

validate and match a receipt against a campaign validation settings by uploading an image file

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
let campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
let opts = {
  'file': "/path/to/file", // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
  'incognito': false, // Boolean | Set true to avoid saving the receipt in storage
  'ipAddress': "ipAddress_example", // String | IP Address of the end user
  'near': "near_example", // String | A geo location to search for merchant. Typically in the format of city, state, country.
  'referenceId': "referenceId_example" // String | Tag a request with a unique reference ID for feedback and training purposes
};
apiInstance.postApiValidationV1CampaignFile(apikey, campaignId, opts, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **campaignId** | **String**| The ID of the campaign to validate the receipt | 
 **file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] 
 **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false]
 **ipAddress** | **String**| IP Address of the end user | [optional] 
 **near** | **String**| A geo location to search for merchant. Typically in the format of city, state, country. | [optional] 
 **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postApiValidationV1CampaignProductvalidationFile

> String postApiValidationV1CampaignProductvalidationFile(apikey, productVerificationNumber, opts)

validate if user-submitted info like serial number are detected an image file

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
let productVerificationNumber = "productVerificationNumber_example"; // String | The number of the product to validate the receipt
let opts = {
  'file': "/path/to/file", // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
  'incognito': false, // Boolean | Set true to avoid saving the receipt in storage
  'subAccountId': "subAccountId_example", // String | Tag a request with sub-account ID for billing purposes
  'referenceId': "referenceId_example" // String | Tag a request with a unique reference ID for feedback and training purposes
};
apiInstance.postApiValidationV1CampaignProductvalidationFile(apikey, productVerificationNumber, opts, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **productVerificationNumber** | **String**| The number of the product to validate the receipt | 
 **file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] 
 **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false]
 **subAccountId** | **String**| Tag a request with sub-account ID for billing purposes | [optional] 
 **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postApiValidationV1CampaignSettingsCreateCampaignid

> postApiValidationV1CampaignSettingsCreateCampaignid(apikey, campaignId, opts)

create campaign settings for a client

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
let campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
let opts = {
  'body': new TaggunReceiptOcrScanningApi.Model9() // Model9 | 
};
apiInstance.postApiValidationV1CampaignSettingsCreateCampaignid(apikey, campaignId, opts, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **campaignId** | **String**| The ID of the campaign to validate the receipt | 
 **body** | [**Model9**](Model9.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## putApiValidationV1CampaignSettingsUpdateCampaignid

> putApiValidationV1CampaignSettingsUpdateCampaignid(apikey, campaignId, opts)

update campaign settings for a client

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4CampaignValidationApi();
let apikey = "apikey_example"; // String | API authentication key.
let campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
let opts = {
  'body': new TaggunReceiptOcrScanningApi.Model9() // Model9 | 
};
apiInstance.putApiValidationV1CampaignSettingsUpdateCampaignid(apikey, campaignId, opts, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **campaignId** | **String**| The ID of the campaign to validate the receipt | 
 **body** | [**Model9**](Model9.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

