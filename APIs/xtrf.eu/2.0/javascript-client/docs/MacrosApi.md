# XtrfHomePortalApi.MacrosApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run**](MacrosApi.md#run) | **POST** /macros/{macroId}/run | Executes a macro.



## run

> ActionStartedDTO run(macroId, macroRequestDTO)

Executes a macro.

Runs a specified macro on a specified list of items (\&quot;list\&quot; variable in the macro code). The list of items can be empty if the macro doesn&#39;t use it. Additional custom parameters can be provided to the macro when necessary (\&quot;params\&quot; variable in the macro code).   &lt;BR&gt;Note: Macros that support parameters can be also run from GUI (Views in Home Portal),so they should also handle the empty parameters map (e.g. by defining default values when parameters are not provided).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.MacrosApi();
let macroId = 789; // Number | macro internal identifier
let macroRequestDTO = /home-api/assets/examples/macros/runMacroAsynchronously.json#requestBody; // MacroRequestDTO | Generated client invoices documents.
apiInstance.run(macroId, macroRequestDTO, (error, data, response) => {
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
 **macroId** | **Number**| macro internal identifier | 
 **macroRequestDTO** | [**MacroRequestDTO**](MacroRequestDTO.md)| Generated client invoices documents. | 

### Return type

[**ActionStartedDTO**](ActionStartedDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

