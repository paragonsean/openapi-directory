# redeal_analytics_api

RedealAnalyticsApi - JavaScript client for redeal_analytics_api
Access analytics for Redeal
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
npm install redeal_analytics_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your redeal_analytics_api from, and run:

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
var RedealAnalyticsApi = require('redeal_analytics_api');


var api = new RedealAnalyticsApi.DevelopersApi()
var opts = {
  'company': "company_example", // {String} pass an optional company Id
  'site': "site_example", // {String} pass an optional site Id
  'deal': "deal_example", // {String} pass an optional deal Id
  'type': "type_example", // {String} type of records to return
  'nexttoken': "nexttoken_example", // {String} next token to start returning records from
  'queryexecutionid': "queryexecutionid_example" // {String} id of execution to get more records based on next token
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getEvents(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://analytics.redeal.io/api/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RedealAnalyticsApi.DevelopersApi* | [**getEvents**](docs/DevelopersApi.md#getEvents) | **GET** /events | get events for analytics


## Documentation for Models

 - [RedealAnalyticsApi.EventRecord](docs/EventRecord.md)


## Documentation for Authorization

Endpoints do not require authorization.

