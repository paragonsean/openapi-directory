# AkeneoPimRestApi.SystemApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSystemInformation**](SystemApi.md#getSystemInformation) | **GET** /api/rest/v1/system-information | Get system information



## getSystemInformation

> GetSystemInformation200Response getSystemInformation()

Get system information

This endpoint allows you to get the version and the edition of the PIM. Example of what you can get &lt;table class&#x3D;\&quot;description-table\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Environment&lt;/th&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Edition&lt;/th&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Version&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt; &lt;tbody&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;SaaS EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;Serenity&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;v20230112013744&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;SaaS CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;GE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;v20210526040645&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;PaaS or onPrem EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;5.0.28&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;PaaS or onPrem CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;5.0.28&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.SystemApi();
apiInstance.getSystemInformation((error, data, response) => {
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

[**GetSystemInformation200Response**](GetSystemInformation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, edition, version, code, message

