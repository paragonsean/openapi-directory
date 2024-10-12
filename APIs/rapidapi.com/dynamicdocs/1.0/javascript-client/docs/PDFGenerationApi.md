# DynamicDocs.PDFGenerationApi

All URIs are relative to *https://dynamicdocs.p.rapidapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile**](PDFGenerationApi.md#compile) | **POST** /templates/{template-token}/compile | Compile New Document PDF



## compile

> Object compile(templateToken, contentType, opts)

Compile New Document PDF

Compile a PDF document from a specific template

### Example

```javascript
import DynamicDocs from 'dynamic_docs';
let defaultClient = DynamicDocs.ApiClient.instance;
// Configure API key authorization: Adv-Security-Token
let Adv-Security-Token = defaultClient.authentications['Adv-Security-Token'];
Adv-Security-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Adv-Security-Token.apiKeyPrefix = 'Token';
// Configure API key authorization: X-RapidAPI-Key
let X-RapidAPI-Key = defaultClient.authentications['X-RapidAPI-Key'];
X-RapidAPI-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Key.apiKeyPrefix = 'Token';

let apiInstance = new DynamicDocs.PDFGenerationApi();
let templateToken = "7a582350acb835ed"; // String | The template-token is available in your template settings after publishing your template.
let contentType = "application/json"; // String | Should be set to \"application/json\"
let opts = {
  'docUrlExpiresIn': 3600, // Number | The doc-url-expires-in is a numerical parameter which takes integers and describes after how many seconds the provided URL is available to download the document.
  'latexCompiler': "latexCompiler_example", // String | The latex-compiler parameter can take the following values:  pdflatex lualatex
  'latexRuns': 56, // Number | The latex-runs is a numerical parameter and can take values of 1, 2 and 3. 
  'mainFileName': "inputFile.tex", // String | The main-file-name is a string parameter which identifies the main file to compile.
  'docFileName': "brilliantDocument", // String | The doc-file-name is a string parameter which determines the name of the file. Note that the extension of the file is not required.
  'body': {"amount":"ZAR 100 000","client":{"address":"xx Long Street","company":"ABC Company Pty Ltd","firstName":"John","lastName":"Smith","location":"Cape Town, South Africa"},"consultant":{"address":"xx Rivonia Road","company":"XYZ Company Pty Ltd","firstName":"Kobus","lastName":"van der Merwe","location":"Sandton, South Africa"},"effectiveDate":"1 February 2021","servicesDescription":"perform analysis on the company's clients and identify existing market segments"} // Object | Post the dynamic data for the template to compile the document PDF.
};
apiInstance.compile(templateToken, contentType, opts, (error, data, response) => {
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
 **templateToken** | **String**| The template-token is available in your template settings after publishing your template. | 
 **contentType** | **String**| Should be set to \&quot;application/json\&quot; | [default to &#39;application/json&#39;]
 **docUrlExpiresIn** | **Number**| The doc-url-expires-in is a numerical parameter which takes integers and describes after how many seconds the provided URL is available to download the document. | [optional] 
 **latexCompiler** | **String**| The latex-compiler parameter can take the following values:  pdflatex lualatex | [optional] 
 **latexRuns** | **Number**| The latex-runs is a numerical parameter and can take values of 1, 2 and 3.  | [optional] 
 **mainFileName** | **String**| The main-file-name is a string parameter which identifies the main file to compile. | [optional] 
 **docFileName** | **String**| The doc-file-name is a string parameter which determines the name of the file. Note that the extension of the file is not required. | [optional] 
 **body** | **Object**| Post the dynamic data for the template to compile the document PDF. | [optional] 

### Return type

**Object**

### Authorization

[Adv-Security-Token](../README.md#Adv-Security-Token), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

