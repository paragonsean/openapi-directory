# nba_v3_roto_baller_articles

NbaV3RotoBallerArticles - JavaScript client for nba_v3_roto_baller_articles
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install nba_v3_roto_baller_articles --save
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

To use the link you just defined in your project, switch to the directory you want to use your nba_v3_roto_baller_articles from, and run:

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
var NbaV3RotoBallerArticles = require('nba_v3_roto_baller_articles');

var defaultClient = NbaV3RotoBallerArticles.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
var apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix['key'] = "Token"
// Configure API key authorization: apiKeyHeader
var apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix['Ocp-Apim-Subscription-Key'] = "Token"

var api = new NbaV3RotoBallerArticles.DefaultApi()
var format = "'xml'"; // {String} Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.rotoballerArticles(format, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://azure-api.sportsdata.io/v3/nba/articles-rotoballer*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NbaV3RotoBallerArticles.DefaultApi* | [**rotoballerArticles**](docs/DefaultApi.md#rotoballerArticles) | **GET** /{format}/RotoBallerArticles | RotoBaller Articles
*NbaV3RotoBallerArticles.DefaultApi* | [**rotoballerArticlesByDate**](docs/DefaultApi.md#rotoballerArticlesByDate) | **GET** /{format}/RotoBallerArticlesByDate/{date} | RotoBaller Articles by Date
*NbaV3RotoBallerArticles.DefaultApi* | [**rotoballerArticlesByPlayer**](docs/DefaultApi.md#rotoballerArticlesByPlayer) | **GET** /{format}/RotoBallerArticlesByPlayerID/{playerid} | RotoBaller Articles by Player


## Documentation for Models

 - [NbaV3RotoBallerArticles.Article](docs/Article.md)
 - [NbaV3RotoBallerArticles.PlayerInfo](docs/PlayerInfo.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### apiKeyHeader


- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

### apiKeyQuery


- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string

