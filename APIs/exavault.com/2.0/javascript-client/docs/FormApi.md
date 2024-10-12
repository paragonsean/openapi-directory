# ExaVault.FormApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFormMessageById**](FormApi.md#deleteFormMessageById) | **DELETE** /forms/entries/{id} | Delete a receive form submission
[**getFormById**](FormApi.md#getFormById) | **GET** /forms/{id} | Get receive folder form by Id
[**getFormByShareHash**](FormApi.md#getFormByShareHash) | **GET** /forms | Get receive folder form settings
[**getFormEntries**](FormApi.md#getFormEntries) | **GET** /forms/entries/{id} | Get form data entries for a receive
[**updateFormById**](FormApi.md#updateFormById) | **PATCH** /forms/{id} | Updates a form with given parameters



## deleteFormMessageById

> EmptyResponse deleteFormMessageById(evApiKey, evAccessToken, id)

Delete a receive form submission

Deletes a form submission entry, which represents one time that a visitor filled out the form and uploaded files. This deletes only the record of the submission (the date, the values entered in the form and the names of the files uploaded by the visitor).The share and any associated file resources will not be deleted by this.   **Notes**:  - Use the [GET /form/entries/{formId}](#operation/getFormMessageById) to list the submissions and obtain the ID of the entry you want to delete - You must have the [DeleteFormData permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) in order to use this operation - It is not possible to un-delete data that is removed in this way 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.FormApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let id = 789; // Number | ID of the entry to be deleted data for
apiInstance.deleteFormMessageById(evApiKey, evAccessToken, id, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call.  | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **id** | **Number**| ID of the entry to be deleted data for | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFormById

> FormResponse getFormById(id, evApiKey, evAccessToken, opts)

Get receive folder form by Id

Returns the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders). The form details will return all the input fields and their settings.   Use the &#x60;include&#x60; parameter (with the value **share**) to also retrieve the details of the associated receive folder.   **Note**  If you prefer to find a form by its shareHash, you can use the [GET /forms](#operation/getFormByShareHash) endpoint instead.  

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.FormApi();
let id = 56; // Number | Form unique ID number.
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "evAccessToken_example"; // String | Access Token required to make the API call.
let opts = {
  'include': "share" // String | Enter \"**share**\" to get information about associated receive folder.
};
apiInstance.getFormById(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| Form unique ID number. | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access Token required to make the API call. | 
 **include** | **String**| Enter \&quot;**share**\&quot; to get information about associated receive folder. | [optional] 

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFormByShareHash

> FormResponse getFormByShareHash(evApiKey, evAccessToken, shareHash, opts)

Get receive folder form settings

Get the information for the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders) by its shareHash. The form details will return all the input field settings and the CSS for the form.  Use the &#x60;include&#x60; parameter (with the value **share**) to also get the details of the associated receive folder.  **Note**  - If you prefer to find a form by its ID, you can use the [GET /forms/{id}](#operation/getFormById) endpoint instead.  

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.FormApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "evAccessToken_example"; // String | Access Token required to make the API call.
let shareHash = "shareHash_example"; // String | Share hash to retrieve the form for.
let opts = {
  'include': "include_example" // String | Related record types to include in the response. Valid option is **share**
};
apiInstance.getFormByShareHash(evApiKey, evAccessToken, shareHash, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access Token required to make the API call. | 
 **shareHash** | **String**| Share hash to retrieve the form for. | 
 **include** | **String**| Related record types to include in the response. Valid option is **share** | [optional] 

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFormEntries

> FormEntryResponse getFormEntries(evApiKey, evAccessToken, id, opts)

Get form data entries for a receive

Returns the form data entries for a specific form for a receive. Optional parameters can be included in the call to manage larger data sets. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.FormApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let id = 56; // Number | ID of the form to retrieve entries for.
let opts = {
  'limit': 10, // Number | Limit of records to be returned (for pagination)
  'offset': 100 // Number | Current offset of records (for pagination)
};
apiInstance.getFormEntries(evApiKey, evAccessToken, id, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call.  | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **id** | **Number**| ID of the form to retrieve entries for. | 
 **limit** | **Number**| Limit of records to be returned (for pagination) | [optional] 
 **offset** | **Number**| Current offset of records (for pagination) | [optional] 

### Return type

[**FormEntryResponse**](FormEntryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFormById

> FormResponse updateFormById(id, evApiKey, evAccessToken, opts)

Updates a form with given parameters

Add, update, or delete a form&#39;s parameters. This will alter how your users/customers will see and interact with the form when sending you files.   **Notes**  *This call will **replace** your current form in its entirety.* If you want to keep any existing elements unchanged, be sure to submit the call with an element&#39;s current settings to preserve them.                          

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.FormApi();
let id = 56; // Number | Form unique ID number.
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'updateFormByIdRequestBody': {"elements":[{"name":"Name","order":0,"settings":{"description":"this is a description test","isRequired":true,"senderEmail":false,"useAsFolderName":false,"width":1},"type":"name"},{"id":2331,"name":"Email Address","order":1,"settings":{"description":null,"isRequired":true,"senderEmail":false,"useAsFolderName":false,"width":1},"type":"email"},{"id":2333,"name":"Subject","order":2,"settings":{"description":null,"isRequired":true,"senderEmail":false,"useAsFolderName":false,"width":1},"type":"text"},{"id":2335,"name":"Message","order":3,"settings":{"description":null,"isRequired":false,"senderEmail":false,"useAsFolderName":false,"width":1},"type":"textarea"},{"id":2337,"name":"Upload Area","order":4,"settings":{"description":null,"isRequired":false,"senderEmail":false,"useAsFolderName":false,"width":1},"type":"upload_area"}],"formDescription":"hello world","submitButtonText":"goodbye world","successMessage":"thank you"} // UpdateFormByIdRequestBody | 
};
apiInstance.updateFormById(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| Form unique ID number. | 
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **updateFormByIdRequestBody** | [**UpdateFormByIdRequestBody**](UpdateFormByIdRequestBody.md)|  | [optional] 

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

