# BrazeEndpoints.EmailTemplatesApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAvailableEmailTemplates_0**](EmailTemplatesApi.md#listAvailableEmailTemplates_0) | **GET** /templates/email/list | List Available Email Templates
[**seeEmailTemplateInformation_0**](EmailTemplatesApi.md#seeEmailTemplateInformation_0) | **GET** /templates/email/info | See Email Template Information



## listAvailableEmailTemplates_0

> listAvailableEmailTemplates_0(opts)

List Available Email Templates

Use this endpoint to get a list of available templates in your Braze account.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Successful Response Properties &#x60;&#x60;&#x60;json {   \&quot;count\&quot;: number of templates returned   \&quot;templates\&quot;: [template with the following properties]:     \&quot;email_template_id\&quot;: (string) your email template&#39;s API Identifier,     \&quot;template_name\&quot;: (string) the name of your email template,     \&quot;created_at\&quot;: (string, in ISO 8601),     \&quot;updated_at\&quot;: (string, in ISO 8601),     \&quot;tags\&quot;: (array of strings) tags appended to the template }   &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.EmailTemplatesApi();
let opts = {
  'modifiedAfter': "2020-01-01T01:01:01.000000", // String | (Optional) String in ISO 8601  Retrieve only templates updated at or after the given time.
  'modifiedBefore': "2020-02-01T01:01:01.000000", // String | (Optional) String in ISO 8601  Retrieve only templates updated at or before the given time
  'limit': "1", // String | (Optional) Positive Number  Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000.
  'offset': "0" // String | (Optional) Positive Number  Number of templates to skip before returning rest of the templates that fit the search criteria.
};
apiInstance.listAvailableEmailTemplates_0(opts, (error, data, response) => {
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
 **modifiedAfter** | **String**| (Optional) String in ISO 8601  Retrieve only templates updated at or after the given time. | [optional] 
 **modifiedBefore** | **String**| (Optional) String in ISO 8601  Retrieve only templates updated at or before the given time | [optional] 
 **limit** | **String**| (Optional) Positive Number  Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. | [optional] 
 **offset** | **String**| (Optional) Positive Number  Number of templates to skip before returning rest of the templates that fit the search criteria. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## seeEmailTemplateInformation_0

> seeEmailTemplateInformation_0(opts)

See Email Template Information

Use to get information on your email templates.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Request Components - [Template Identifier](https://www.braze.com/docs/api/identifier_types/)

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.EmailTemplatesApi();
let opts = {
  'emailTemplateId': "{{email_template_id}}" // String | (Required) String  Your email template's API Identifier.
};
apiInstance.seeEmailTemplateInformation_0(opts, (error, data, response) => {
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
 **emailTemplateId** | **String**| (Required) String  Your email template&#39;s API Identifier. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

