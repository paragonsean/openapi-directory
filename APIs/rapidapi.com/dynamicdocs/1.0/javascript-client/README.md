# dynamic_docs

DynamicDocs - JavaScript client for dynamic_docs
ADVICEment's [DynamicDocs API automates your document generation](https://advicement.io/dynamic-documents-api) and creates dynamic, optimized, interactive PDFs. Write your templates in LaTeX and call the API with JSON data to get your PDFs in seconds.

The template files are stored in your dashboard and can be edited, tested and published online. Document templates can contain dynamic text using logic statements, include tables stretching multiple pages and show great-looking charts based on the underlying data. LaTeX creates crisp, high-quality documents where every detail is well-positioned and styled.

Integrate with ADVICEment DynamicDocs API in minutes and start creating beautiful [dynamic PDF documents](https://advicement.io/dynamic-documents-api) for your needs.

For more information, visit [DynamicDocs API Home page](https://advicement.io/dynamic-documents-api).
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://advicement.io/dynamic-documents-api](https://advicement.io/dynamic-documents-api)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install dynamic_docs --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your dynamic_docs from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var DynamicDocs = require('dynamic_docs');

var defaultClient = DynamicDocs.ApiClient.instance;
// Configure API key authorization: Adv-Security-Token
var Adv-Security-Token = defaultClient.authentications['Adv-Security-Token'];
Adv-Security-Token.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Adv-Security-Token.apiKeyPrefix['ADVICEment API Key'] = "Token"
// Configure API key authorization: X-RapidAPI-Key
var X-RapidAPI-Key = defaultClient.authentications['X-RapidAPI-Key'];
X-RapidAPI-Key.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Key.apiKeyPrefix['RapidAPI.com API Key'] = "Token"

var api = new DynamicDocs.PDFGenerationApi()
var templateToken = "7a582350acb835ed"; // {String} The template-token is available in your template settings after publishing your template.
var contentType = "application/json"; // {String} Should be set to \"application/json\"
var opts = {
  'docUrlExpiresIn': 3600, // {Number} The doc-url-expires-in is a numerical parameter which takes integers and describes after how many seconds the provided URL is available to download the document.
  'latexCompiler': "latexCompiler_example", // {String} The latex-compiler parameter can take the following values:  pdflatex lualatex
  'latexRuns': 56, // {Number} The latex-runs is a numerical parameter and can take values of 1, 2 and 3. 
  'mainFileName': "inputFile.tex", // {String} The main-file-name is a string parameter which identifies the main file to compile.
  'docFileName': "brilliantDocument", // {String} The doc-file-name is a string parameter which determines the name of the file. Note that the extension of the file is not required.
  'body': {"amount":"ZAR 100 000","client":{"address":"xx Long Street","company":"ABC Company Pty Ltd","firstName":"John","lastName":"Smith","location":"Cape Town, South Africa"},"consultant":{"address":"xx Rivonia Road","company":"XYZ Company Pty Ltd","firstName":"Kobus","lastName":"van der Merwe","location":"Sandton, South Africa"},"effectiveDate":"1 February 2021","servicesDescription":"perform analysis on the company's clients and identify existing market segments"} // {Object} Post the dynamic data for the template to compile the document PDF.
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.compile(templateToken, contentType, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://dynamicdocs.p.rapidapi.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DynamicDocs.PDFGenerationApi* | [**compile**](docs/PDFGenerationApi.md#compile) | **POST** /templates/{template-token}/compile | Compile New Document PDF


## Documentation for Models



## Documentation for Authorization


Authentication schemes defined for the API:
### Adv-Security-Token


- **Type**: API key
- **API key parameter name**: ADVICEment API Key
- **Location**: HTTP header

### X-RapidAPI-Key


- **Type**: API key
- **API key parameter name**: RapidAPI.com API Key
- **Location**: HTTP header

