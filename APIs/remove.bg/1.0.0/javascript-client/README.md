# background_removal_api

BackgroundRemovalApi - JavaScript client for background_removal_api
Remove the background of any image
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install background_removal_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your background_removal_api from, and run:

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
var BackgroundRemovalApi = require('background_removal_api');

var defaultClient = BackgroundRemovalApi.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
var APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix['X-API-Key'] = "Token"

var api = new BackgroundRemovalApi.BackgroundRemovalApi()
var removeBgJson = new BackgroundRemovalApi.RemoveBgJson(); // {RemoveBgJson} 
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.removebgPost(removeBgJson, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.remove.bg/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BackgroundRemovalApi.BackgroundRemovalApi* | [**removebgPost**](docs/BackgroundRemovalApi.md#removebgPost) | **POST** /removebg | Remove the background of an image
*BackgroundRemovalApi.FetchAccountInfoApi* | [**accountGet**](docs/FetchAccountInfoApi.md#accountGet) | **GET** /account | Fetch credit balance and free API calls.
*BackgroundRemovalApi.ImprovementProgramApi* | [**improvePost**](docs/ImprovementProgramApi.md#improvePost) | **POST** /improve | 


## Documentation for Models

 - [BackgroundRemovalApi.AccountGet200Response](docs/AccountGet200Response.md)
 - [BackgroundRemovalApi.AccountGet200ResponseData](docs/AccountGet200ResponseData.md)
 - [BackgroundRemovalApi.AccountGet200ResponseDataAttributes](docs/AccountGet200ResponseDataAttributes.md)
 - [BackgroundRemovalApi.AccountGet200ResponseDataAttributesApi](docs/AccountGet200ResponseDataAttributesApi.md)
 - [BackgroundRemovalApi.AccountGet200ResponseDataAttributesCredits](docs/AccountGet200ResponseDataAttributesCredits.md)
 - [BackgroundRemovalApi.AuthFailed](docs/AuthFailed.md)
 - [BackgroundRemovalApi.AuthFailedErrorsInner](docs/AuthFailedErrorsInner.md)
 - [BackgroundRemovalApi.ImprovePost400Response](docs/ImprovePost400Response.md)
 - [BackgroundRemovalApi.ImprovePost400ResponseErrorsInner](docs/ImprovePost400ResponseErrorsInner.md)
 - [BackgroundRemovalApi.ImprovementProgramJson](docs/ImprovementProgramJson.md)
 - [BackgroundRemovalApi.ImprovementProgramJsonResponse](docs/ImprovementProgramJsonResponse.md)
 - [BackgroundRemovalApi.RateLimit](docs/RateLimit.md)
 - [BackgroundRemovalApi.RateLimitErrorsInner](docs/RateLimitErrorsInner.md)
 - [BackgroundRemovalApi.RemoveBgJson](docs/RemoveBgJson.md)
 - [BackgroundRemovalApi.RemoveBgJsonResponse](docs/RemoveBgJsonResponse.md)
 - [BackgroundRemovalApi.RemoveBgJsonResponseData](docs/RemoveBgJsonResponseData.md)
 - [BackgroundRemovalApi.RemovebgPost400Response](docs/RemovebgPost400Response.md)
 - [BackgroundRemovalApi.RemovebgPost400ResponseErrorsInner](docs/RemovebgPost400ResponseErrorsInner.md)
 - [BackgroundRemovalApi.RemovebgPost402Response](docs/RemovebgPost402Response.md)
 - [BackgroundRemovalApi.RemovebgPost402ResponseErrorsInner](docs/RemovebgPost402ResponseErrorsInner.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### APIKeyHeader


- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header

