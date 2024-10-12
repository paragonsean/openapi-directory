# rudder_api

RudderApi - JavaScript client for rudder_api
Download OpenAPI specification: [openapi.yml](openapi.yml)

# Introduction

Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.

## Versioning

Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you
to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.

You can change the version of the API used by setting it either within the url or in a header:

* the URL: each URL is prefixed by its version id, like `/api/version/function`.

```bash
# Version 10
curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules
# Latest
curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules
# Wrong (not an integer) => 404 not found
curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules
```

* the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.

```bash
# Version 10
curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules
# Wrong => Error response indicating which versions are available
curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules
```

In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe
period of time to allow migration from previous versions.


<h4>Existing versions</h4>
<table>
  <thead>
    <tr>
      <th style=\"width: 20%\">Version</th>
      <th style=\"width: 20%\">Rudder versions it appeared in</th>
      <th style=\"width: 70%\">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class=\"code\">1</td>
      <td class=\"code\">Never released (for internal use only)</td>
      <td>Experimental version</td>
    </tr>
    <tr>
      <td class=\"code\">2 to 10 (deprecated)</td>
      <td class=\"code\">4.3 and before</td>
      <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>
    </tr>
    <tr>
      <td class=\"code\">11</td>
      <td class=\"code\">5.0</td>
      <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>
    </tr>
    <tr>
      <td class=\"code\">12</td>
      <td class=\"code\">6.0 and 6.1</td>
      <td>Node key management</td>
    </tr>
    <tr>
      <td class=\"code\">13</td>
      <td class=\"code\">6.2</td>
      <td><ul>
        <li>Node status endpoint</li>
        <li>System health check</li>
        <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>
      </ul></td>
    </tr>
    <tr>
      <td class=\"code\">14</td>
      <td class=\"code\">7.0</td>
      <td><ul>
        <li>Secret management</li>
        <li>Directive tree</li>
        <li>Improve techniques management</li>
        <li>Demote a relay</li>
      </ul></td>
    </tr>
    <tr>
      <td class=\"code\">15</td>
      <td class=\"code\">7.1</td>
      <td><ul>
        <li>Package updates in nodes</li>
      </ul></td>
    </tr>
    <tr>
      <td class=\"code\">16</td>
      <td class=\"code\">7.2</td>
      <td><ul>
        <li>Create node API included from plugin</li>
        <li>Configuration archive import/export</li>
      </ul></td>
    </tr>
  </tbody>
</table>


## Response format

All responses from the API are in the JSON format.

```json
{
  \"action\": \"The name of the called function\",
  \"id\": \"The ID of the element you want, if relevant\",
  \"result\": \"The result of your action: success or error\",
  \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",
  \"errorDetails\": \"Only present if this is an error, it contains the error message\"
}
```


* __Success__ responses are sent with the 200 HTTP (Success) code

* __Error__ responses are sent with a HTTP error code (mostly 5xx...)


## HTTP method

Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:


* **GET**: search or retrieve information (get rule details, get a group, ...)

* **PUT**: add new objects (create a directive, clone a Rule, ...)

* **DELETE**: remove objects (delete a node, delete a parameter, ...)

* **POST**: update existing objects (update a directive, reload a group, ...)


## Parameters

### General parameters

Some parameters are available for almost all API functions. They will be described in this section.
They must be part of the query and can't be submitted in a JSON form.

#### Available for all requests

<table>
  <thead>
    <tr>
      <th style=\"width: 30%\">Field</th>
      <th style=\"width: 10%\">Type</th>
      <th style=\"width: 70%\">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class=\"code\">prettify</td>
      <td><b>boolean</b><br><i>optional</i></td>
      <td>
        Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.
        <p class=\"default-value\">Default value: <code>false</code></p>
      </td>
    </tr>
  </tbody>
</table>


#### Available for modification requests (PUT/POST/DELETE)

<table>
  <thead>
    <tr>
      <th style=\"width: 25%\">Field</th>
      <th style=\"width: 12%\">Type</th>
      <th style=\"width: 70%\">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class=\"code\">reason</td>
      <td><b>string</b><br><i>optional</i> or <i>required</i></td>
      <td>
        Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.
        <p class=\"default-value\">Default value: <code>\"\"</code></p>
      </td>
    </tr>
    <tr>
      <td class=\"code\">changeRequestName</td>
      <td><b>string</b><br><i>optional</i></td>
      <td>
        Set the change request name, is used only if workflows are enabled. The default value depends on the function called
        <p class=\"default-value\">Default value: <code>A default string for each function</code></p>
      </td>
    </tr>
    <tr>
      <td class=\"code\">changeRequestDescription</td>
      <td><b>string</b><br><i>optional</i></td>
      <td>
        Set the change request description, is used only if workflows are enabled.
        <p class=\"default-value\">Default value: <code>\"\"</code></p>
      </td>
    </tr>
  </tbody>
</table>


### Passing parameters

Parameters to the API can be sent:

* As part of the URL for resource identification

* As data for POST/PUT requests

  * Directly in JSON format

  * As request arguments

#### As part of the URL for resource identification

Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.

```bash
# Get the Rule of ID \"id\"
curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id
```



CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.


#### Sending data for POST/PUT requests

##### Directly in JSON format

JSON format is the preferred way to interact with Rudder API for creating or updating resources.
You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored).
In a `curl` `POST` request, that header can be provided with the `-H` parameter:

```bash
curl -X POST -H \"Content-Type: application/json\" ...
```

The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.

The (human readable) format is:

```json
{
  \"key1\": \"value1\",
  \"key2\": false,
  \"key3\": 42
}
```


Here is an example with inlined data:

```bash
# Update the Rule 'id' with a new name, disabled, and setting it one directive
curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\"
https://rudder.example.com/rudder/api/rules/latest/{id}
  -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}'
```

You can also pass a supply the JSON in a file:

```bash
# Update the Rule 'id' with a new name, disabled, and setting it one directive
curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam
```

Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):

```bash
# Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\"
curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\"
```

##### Request parameters

In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use
request parameters. You will need to pass one parameter for each data you want to change.

Parameters follow the following schema:

```
key=value
```

You can pass parameters by two means:

* As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]

```bash
# Update the Rule 'id' with a new name, disabled, and setting it one directive
curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\"
```

* As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.

```bash
# Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json)
curl -X POST -H \"X-API-Token: yourToken\"
https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json
```

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 17
- Package version: 17
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://www.rudder.io](https://www.rudder.io)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install rudder_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your rudder_api from, and run:

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
var RudderApi = require('rudder_api');

var defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
var API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix['X-API-Token'] = "Token"

var api = new RudderApi.APIInfoApi()
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.apiGeneralInformations(callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RudderApi.APIInfoApi* | [**apiGeneralInformations**](docs/APIInfoApi.md#apiGeneralInformations) | **GET** /info | List all endoints
*RudderApi.APIInfoApi* | [**apiInformations**](docs/APIInfoApi.md#apiInformations) | **GET** /info/details/{endpointName} | Get information about one API endpoint
*RudderApi.APIInfoApi* | [**apiSubInformations**](docs/APIInfoApi.md#apiSubInformations) | **GET** /info/{sectionId} | Get information on endpoint in a section
*RudderApi.ArchivesApi* | [**callExport**](docs/ArchivesApi.md#callExport) | **GET** /archives/export | Get a ZIP archive of the requested items and their dependencies
*RudderApi.ArchivesApi* | [**callImport**](docs/ArchivesApi.md#callImport) | **POST** /archives/import | Import a ZIP archive of policies into Rudder
*RudderApi.BrandingApi* | [**getBrandingConf**](docs/BrandingApi.md#getBrandingConf) | **GET** /branding | Get branding configuration
*RudderApi.BrandingApi* | [**reloadBrandingConf**](docs/BrandingApi.md#reloadBrandingConf) | **POST** /branding/reload | Reload branding file
*RudderApi.BrandingApi* | [**updateBRandingConf**](docs/BrandingApi.md#updateBRandingConf) | **POST** /branding | Update web interface customization
*RudderApi.CVEApi* | [**checkCVE**](docs/CVEApi.md#checkCVE) | **POST** /cve/check | Trigger a CVE check
*RudderApi.CVEApi* | [**getAllCve**](docs/CVEApi.md#getAllCve) | **GET** /cve | Get all CVE details
*RudderApi.CVEApi* | [**getCVECheckConfiguration**](docs/CVEApi.md#getCVECheckConfiguration) | **GET** /cve/check/config | Get CVE check config
*RudderApi.CVEApi* | [**getCVEList**](docs/CVEApi.md#getCVEList) | **POST** /cve/list | Get a list of CVE details
*RudderApi.CVEApi* | [**getCve**](docs/CVEApi.md#getCve) | **GET** /cve/{cveId} | Get a CVE details
*RudderApi.CVEApi* | [**getLastCVECheck**](docs/CVEApi.md#getLastCVECheck) | **GET** /cve/check/last | Get last CVE check result
*RudderApi.CVEApi* | [**readCVEfromFS**](docs/CVEApi.md#readCVEfromFS) | **POST** /cve/update/fs | Update CVE database from file system
*RudderApi.CVEApi* | [**updateCVE**](docs/CVEApi.md#updateCVE) | **POST** /cve/update | Update CVE database from remote source
*RudderApi.CVEApi* | [**updateCVECheckConfiguration**](docs/CVEApi.md#updateCVECheckConfiguration) | **POST** /cve/check/config | Update cve check config
*RudderApi.CampaignsApi* | [**allCampaigns**](docs/CampaignsApi.md#allCampaigns) | **GET** /campaigns | Get all campaigns details
*RudderApi.CampaignsApi* | [**deleteCampaign**](docs/CampaignsApi.md#deleteCampaign) | **DELETE** /campaigns/{id} | Delete a campaign
*RudderApi.CampaignsApi* | [**deleteCampaignEvent**](docs/CampaignsApi.md#deleteCampaignEvent) | **DELETE** /campaigns/events/{id} | Delete a campaign event details
*RudderApi.CampaignsApi* | [**getAllCampaignEvents**](docs/CampaignsApi.md#getAllCampaignEvents) | **GET** /campaigns/events | Get all campaign events
*RudderApi.CampaignsApi* | [**getCampaign**](docs/CampaignsApi.md#getCampaign) | **GET** /campaigns/{id} | Get a campaign details
*RudderApi.CampaignsApi* | [**getCampaignEvent**](docs/CampaignsApi.md#getCampaignEvent) | **GET** /campaigns/events/{id} | Get a campaign event details
*RudderApi.CampaignsApi* | [**getEventsCampaign**](docs/CampaignsApi.md#getEventsCampaign) | **GET** /campaigns/{id}/events | Get campaign events for a campaign
*RudderApi.CampaignsApi* | [**saveCampaign**](docs/CampaignsApi.md#saveCampaign) | **POST** /campaigns | Save a campaign
*RudderApi.CampaignsApi* | [**saveCampaignEvent**](docs/CampaignsApi.md#saveCampaignEvent) | **POST** /campaigns/events/{id} | Update an existing event
*RudderApi.CampaignsApi* | [**scheduleCampaign**](docs/CampaignsApi.md#scheduleCampaign) | **POST** /campaigns/{id}/schedule | Schedule a campaign event for a campaign
*RudderApi.ChangeRequestsApi* | [**acceptChangeRequest**](docs/ChangeRequestsApi.md#acceptChangeRequest) | **POST** /changeRequests/{changeRequestId}/accept | Accept a request details
*RudderApi.ChangeRequestsApi* | [**changeRequestDetails**](docs/ChangeRequestsApi.md#changeRequestDetails) | **GET** /changeRequests/{changeRequestId} | Get a change request details
*RudderApi.ChangeRequestsApi* | [**declineChangeRequest**](docs/ChangeRequestsApi.md#declineChangeRequest) | **DELETE** /changeRequests/{changeRequestId} | Decline a request details
*RudderApi.ChangeRequestsApi* | [**listChangeRequests**](docs/ChangeRequestsApi.md#listChangeRequests) | **GET** /api/changeRequests | List all change requests
*RudderApi.ChangeRequestsApi* | [**listUsers**](docs/ChangeRequestsApi.md#listUsers) | **GET** /users | List user
*RudderApi.ChangeRequestsApi* | [**removeValidatedUser**](docs/ChangeRequestsApi.md#removeValidatedUser) | **DELETE** /validatedUsers/{username} | Remove an user from validated user list
*RudderApi.ChangeRequestsApi* | [**saveWorkflowUser**](docs/ChangeRequestsApi.md#saveWorkflowUser) | **POST** /validatedUsers | Update validated user list
*RudderApi.ChangeRequestsApi* | [**updateChangeRequest**](docs/ChangeRequestsApi.md#updateChangeRequest) | **POST** /changeRequests/{changeRequestId} | Update a request details
*RudderApi.ComplianceApi* | [**getDirectiveComplianceId**](docs/ComplianceApi.md#getDirectiveComplianceId) | **GET** /compliance/directives/{directiveId} | Compliance details by directive
*RudderApi.ComplianceApi* | [**getDirectivesCompliance**](docs/ComplianceApi.md#getDirectivesCompliance) | **GET** /compliance/directives | Compliance details for all directives
*RudderApi.ComplianceApi* | [**getGlobalCompliance**](docs/ComplianceApi.md#getGlobalCompliance) | **GET** /compliance | Global compliance
*RudderApi.ComplianceApi* | [**getNodeCompliance**](docs/ComplianceApi.md#getNodeCompliance) | **GET** /compliance/nodes/{nodeId} | Compliance details by node
*RudderApi.ComplianceApi* | [**getNodesCompliance**](docs/ComplianceApi.md#getNodesCompliance) | **GET** /compliance/nodes | Compliance details for all nodes
*RudderApi.ComplianceApi* | [**getRuleCompliance**](docs/ComplianceApi.md#getRuleCompliance) | **GET** /compliance/rules/{ruleId} | Compliance details by rule
*RudderApi.ComplianceApi* | [**getRulesCompliance**](docs/ComplianceApi.md#getRulesCompliance) | **GET** /compliance/rules | Compliance details for all rules
*RudderApi.DataSourcesApi* | [**createDataSource**](docs/DataSourcesApi.md#createDataSource) | **PUT** /datasources | Create a data source
*RudderApi.DataSourcesApi* | [**deleteDataSource**](docs/DataSourcesApi.md#deleteDataSource) | **DELETE** /datasources/{datasourceId} | Delete a data source
*RudderApi.DataSourcesApi* | [**getAllDataSources**](docs/DataSourcesApi.md#getAllDataSources) | **GET** /datasources | List all data sources
*RudderApi.DataSourcesApi* | [**getDataSource**](docs/DataSourcesApi.md#getDataSource) | **GET** /datasources/{datasourceId} | Get data source configuration
*RudderApi.DataSourcesApi* | [**reloadAllDatasourcesAllNodes**](docs/DataSourcesApi.md#reloadAllDatasourcesAllNodes) | **POST** /datasources/reload | Update properties from data sources
*RudderApi.DataSourcesApi* | [**reloadAllDatasourcesOneNode**](docs/DataSourcesApi.md#reloadAllDatasourcesOneNode) | **POST** /nodes/{nodeId}/fetchData | Update properties for one node from all data sources
*RudderApi.DataSourcesApi* | [**reloadOneDatasourceAllNodes**](docs/DataSourcesApi.md#reloadOneDatasourceAllNodes) | **POST** /datasources/reload/{datasourceId} | Update properties from data sources
*RudderApi.DataSourcesApi* | [**reloadOneDatasourceOneNode**](docs/DataSourcesApi.md#reloadOneDatasourceOneNode) | **POST** /nodes/{nodeId}/fetchData/{datasourceId} | Update properties for one node from a data source
*RudderApi.DataSourcesApi* | [**updateDataSource**](docs/DataSourcesApi.md#updateDataSource) | **POST** /datasources/{datasourceId} | Update a data source configuration
*RudderApi.DirectivesApi* | [**checkDirective**](docs/DirectivesApi.md#checkDirective) | **POST** /directives/{directiveId}/check | Check that update on a directive is valid
*RudderApi.DirectivesApi* | [**createDirective**](docs/DirectivesApi.md#createDirective) | **PUT** /directives | Create a directive
*RudderApi.DirectivesApi* | [**deleteDirective**](docs/DirectivesApi.md#deleteDirective) | **DELETE** /directives/{directiveId} | Delete a directive
*RudderApi.DirectivesApi* | [**directiveDetails**](docs/DirectivesApi.md#directiveDetails) | **GET** /directives/{directiveId} | Get directive details
*RudderApi.DirectivesApi* | [**listDirectives**](docs/DirectivesApi.md#listDirectives) | **GET** /directives | List all directives
*RudderApi.DirectivesApi* | [**updateDirective**](docs/DirectivesApi.md#updateDirective) | **POST** /directives/{directiveId} | Update a directive details
*RudderApi.GroupsApi* | [**createGroup**](docs/GroupsApi.md#createGroup) | **PUT** /groups | Create a group
*RudderApi.GroupsApi* | [**createGroupCategory**](docs/GroupsApi.md#createGroupCategory) | **PUT** /groups/categories | Create a group category
*RudderApi.GroupsApi* | [**deleteGroup**](docs/GroupsApi.md#deleteGroup) | **DELETE** /groups/{groupId} | Delete a group
*RudderApi.GroupsApi* | [**deleteGroupCategory**](docs/GroupsApi.md#deleteGroupCategory) | **DELETE** /groups/categories/{groupCategoryId} | Delete group category
*RudderApi.GroupsApi* | [**getGroupCategoryDetails**](docs/GroupsApi.md#getGroupCategoryDetails) | **GET** /groups/categories/{groupCategoryId} | Get group category details
*RudderApi.GroupsApi* | [**getGroupTree**](docs/GroupsApi.md#getGroupTree) | **GET** /groups/tree | Get groups tree
*RudderApi.GroupsApi* | [**groupDetails**](docs/GroupsApi.md#groupDetails) | **GET** /groups/{groupId} | Get group details
*RudderApi.GroupsApi* | [**listGroups**](docs/GroupsApi.md#listGroups) | **GET** /groups | List all groups
*RudderApi.GroupsApi* | [**reloadGroup**](docs/GroupsApi.md#reloadGroup) | **POST** /groups/{groupId}/reload | Reload a group
*RudderApi.GroupsApi* | [**updateGroup**](docs/GroupsApi.md#updateGroup) | **POST** /groups/{groupId} | Update group details
*RudderApi.GroupsApi* | [**updateGroupCategory**](docs/GroupsApi.md#updateGroupCategory) | **POST** /groups/categories/{groupCategoryId} | Update group category details
*RudderApi.InventoriesApi* | [**fileWatcherRestart**](docs/InventoriesApi.md#fileWatcherRestart) | **POST** /inventories/watcher/restart | Restart inventory watcher
*RudderApi.InventoriesApi* | [**fileWatcherStart**](docs/InventoriesApi.md#fileWatcherStart) | **POST** /inventories/watcher/start | Start inventory watcher
*RudderApi.InventoriesApi* | [**fileWatcherStop**](docs/InventoriesApi.md#fileWatcherStop) | **POST** /inventories/watcher/stop | Stop inventory watcher
*RudderApi.InventoriesApi* | [**queueInformation**](docs/InventoriesApi.md#queueInformation) | **GET** /inventories/info | Get information about inventory processing queue
*RudderApi.InventoriesApi* | [**uploadInventory**](docs/InventoriesApi.md#uploadInventory) | **POST** /inventories/upload | Upload an inventory for processing
*RudderApi.NodesApi* | [**applyPolicy**](docs/NodesApi.md#applyPolicy) | **POST** /nodes/{nodeId}/applyPolicy | Trigger an agent run
*RudderApi.NodesApi* | [**applyPolicyAllNodes**](docs/NodesApi.md#applyPolicyAllNodes) | **POST** /nodes/applyPolicy | Trigger an agent run on all nodes
*RudderApi.NodesApi* | [**changePendingNodeStatus**](docs/NodesApi.md#changePendingNodeStatus) | **POST** /nodes/pending/{nodeId} | Update pending Node status
*RudderApi.NodesApi* | [**createNodes**](docs/NodesApi.md#createNodes) | **PUT** /nodes | Create one or several new nodes
*RudderApi.NodesApi* | [**deleteNode**](docs/NodesApi.md#deleteNode) | **DELETE** /nodes/{nodeId} | Delete a node
*RudderApi.NodesApi* | [**getNodesStatus**](docs/NodesApi.md#getNodesStatus) | **GET** /nodes/status | Get nodes acceptation status
*RudderApi.NodesApi* | [**listAcceptedNodes**](docs/NodesApi.md#listAcceptedNodes) | **GET** /nodes | List managed nodes
*RudderApi.NodesApi* | [**listPendingNodes**](docs/NodesApi.md#listPendingNodes) | **GET** /nodes/pending | List pending nodes
*RudderApi.NodesApi* | [**nodeDetails**](docs/NodesApi.md#nodeDetails) | **GET** /nodes/{nodeId} | Get information about a node
*RudderApi.NodesApi* | [**nodeInheritedProperties**](docs/NodesApi.md#nodeInheritedProperties) | **GET** /nodes/{nodeId}/inheritedProperties | Get inherited node properties for a node
*RudderApi.NodesApi* | [**updateNode**](docs/NodesApi.md#updateNode) | **POST** /nodes/{nodeId} | Update node settings and properties
*RudderApi.ParametersApi* | [**createParameter**](docs/ParametersApi.md#createParameter) | **PUT** /parameters | Create a new parameter
*RudderApi.ParametersApi* | [**deleteParameter**](docs/ParametersApi.md#deleteParameter) | **DELETE** /parameters/{parameterId} | Delete a parameter
*RudderApi.ParametersApi* | [**listParameters**](docs/ParametersApi.md#listParameters) | **GET** /parameters | List all global parameters
*RudderApi.ParametersApi* | [**parameterDetails**](docs/ParametersApi.md#parameterDetails) | **GET** /parameters/{parameterId} | Get the value of a parameter
*RudderApi.ParametersApi* | [**updateParameter**](docs/ParametersApi.md#updateParameter) | **POST** /parameters/{parameterId} | Update a parameter&#39;s value
*RudderApi.RulesApi* | [**createRule**](docs/RulesApi.md#createRule) | **PUT** /rules | Create a rule
*RudderApi.RulesApi* | [**createRuleCategory**](docs/RulesApi.md#createRuleCategory) | **PUT** /rules/categories | Create a rule category
*RudderApi.RulesApi* | [**deleteRule**](docs/RulesApi.md#deleteRule) | **DELETE** /rules/{ruleId} | Delete a rule
*RudderApi.RulesApi* | [**deleteRuleCategory**](docs/RulesApi.md#deleteRuleCategory) | **DELETE** /rules/categories/{ruleCategoryId} | Delete group category
*RudderApi.RulesApi* | [**getRuleCategoryDetails**](docs/RulesApi.md#getRuleCategoryDetails) | **GET** /rules/categories/{ruleCategoryId} | Get rule category details
*RudderApi.RulesApi* | [**getRuleTree**](docs/RulesApi.md#getRuleTree) | **GET** /rules/tree | Get rules tree
*RudderApi.RulesApi* | [**listRules**](docs/RulesApi.md#listRules) | **GET** /rules | List all rules
*RudderApi.RulesApi* | [**ruleDetails**](docs/RulesApi.md#ruleDetails) | **GET** /rules/{ruleId} | Get a rule details
*RudderApi.RulesApi* | [**updateRule**](docs/RulesApi.md#updateRule) | **POST** /rules/{ruleId} | Update a rule details
*RudderApi.RulesApi* | [**updateRuleCategory**](docs/RulesApi.md#updateRuleCategory) | **POST** /rules/categories/{ruleCategoryId} | Update rule category details
*RudderApi.ScaleOutRelayApi* | [**demoteToNode**](docs/ScaleOutRelayApi.md#demoteToNode) | **POST** /scaleoutrelay/demote/{nodeId} | Demote a relay to simple node
*RudderApi.ScaleOutRelayApi* | [**promoteToRelay**](docs/ScaleOutRelayApi.md#promoteToRelay) | **POST** /scaleoutrelay/promote/{nodeId} | Promote a node to relay
*RudderApi.SecretManagementApi* | [**addSecret**](docs/SecretManagementApi.md#addSecret) | **PUT** /secret | Create a secret
*RudderApi.SecretManagementApi* | [**deleteSecret**](docs/SecretManagementApi.md#deleteSecret) | **DELETE** /secret/{name} | Delete a secret
*RudderApi.SecretManagementApi* | [**getAllSecrets**](docs/SecretManagementApi.md#getAllSecrets) | **GET** /secret | List all secrets
*RudderApi.SecretManagementApi* | [**getSecret**](docs/SecretManagementApi.md#getSecret) | **GET** /secret/{name} | Get one secret
*RudderApi.SecretManagementApi* | [**updateSecret**](docs/SecretManagementApi.md#updateSecret) | **POST** /secret | Update a secret
*RudderApi.SettingsApi* | [**getAllSettings**](docs/SettingsApi.md#getAllSettings) | **GET** /settings | List all settings
*RudderApi.SettingsApi* | [**getAllowedNetworks**](docs/SettingsApi.md#getAllowedNetworks) | **GET** /settings/allowed_networks/{nodeId} | Get allowed networks for a policy server
*RudderApi.SettingsApi* | [**getSetting**](docs/SettingsApi.md#getSetting) | **GET** /settings/{settingId} | Get the value of a setting
*RudderApi.SettingsApi* | [**modifyAllowedNetworks**](docs/SettingsApi.md#modifyAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId}/diff | Modify allowed networks for a policy server
*RudderApi.SettingsApi* | [**modifySetting**](docs/SettingsApi.md#modifySetting) | **POST** /settings/{settingId} | Set the value of a setting
*RudderApi.SettingsApi* | [**setAllowedNetworks**](docs/SettingsApi.md#setAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId} | Set allowed networks for a policy server
*RudderApi.StatusApi* | [**none**](docs/StatusApi.md#none) | **GET** /status | Check if Rudder is alive
*RudderApi.SystemApi* | [**createArchive**](docs/SystemApi.md#createArchive) | **POST** /system/archives/{archiveKind} | Create an archive
*RudderApi.SystemApi* | [**getHealthcheckResult**](docs/SystemApi.md#getHealthcheckResult) | **GET** /system/healthcheck | Get healthcheck
*RudderApi.SystemApi* | [**getStatus**](docs/SystemApi.md#getStatus) | **GET** /system/status | Get server status
*RudderApi.SystemApi* | [**getSystemInfo**](docs/SystemApi.md#getSystemInfo) | **GET** /system/info | Get server information
*RudderApi.SystemApi* | [**getZipArchive**](docs/SystemApi.md#getZipArchive) | **GET** /system/archives/{archiveKind}/zip/{commitId} | Get an archive as a ZIP
*RudderApi.SystemApi* | [**listArchives**](docs/SystemApi.md#listArchives) | **GET** /system/archives/{archiveKind} | List archives
*RudderApi.SystemApi* | [**purgeSoftware**](docs/SystemApi.md#purgeSoftware) | **POST** /system/maintenance/purgeSoftware | Trigger batch for cleaning unreferenced software
*RudderApi.SystemApi* | [**regeneratePolicies**](docs/SystemApi.md#regeneratePolicies) | **POST** /system/regenerate/policies | Trigger a new policy generation
*RudderApi.SystemApi* | [**reloadAll**](docs/SystemApi.md#reloadAll) | **POST** /system/reload | Reload both techniques and dynamic groups
*RudderApi.SystemApi* | [**reloadGroups**](docs/SystemApi.md#reloadGroups) | **POST** /system/reload/groups | Reload dynamic groups
*RudderApi.SystemApi* | [**reloadTechniques**](docs/SystemApi.md#reloadTechniques) | **POST** /system/reload/techniques | Reload techniques
*RudderApi.SystemApi* | [**restoreArchive**](docs/SystemApi.md#restoreArchive) | **POST** /system/archives/{archiveKind}/restore/{archiveRestoreKind} | Restore an archive
*RudderApi.SystemApi* | [**updatePolicies**](docs/SystemApi.md#updatePolicies) | **POST** /system/update/policies | Trigger update of policies
*RudderApi.SystemUpdateCampaignsApi* | [**getCampaignEventResult**](docs/SystemUpdateCampaignsApi.md#getCampaignEventResult) | **GET** /systemUpdate/events/{id}/result | Get a campaign event result
*RudderApi.SystemUpdateCampaignsApi* | [**getCampaignEventResultForNode**](docs/SystemUpdateCampaignsApi.md#getCampaignEventResultForNode) | **GET** /systemUpdate/events/{id}/result/{nodeId} | Get detailed campaign event result for a Node
*RudderApi.SystemUpdateCampaignsApi* | [**getCampaignHistory**](docs/SystemUpdateCampaignsApi.md#getCampaignHistory) | **GET** /systemUpdate/campaigns/{id}/history | Get a campaign result history
*RudderApi.TechniquesApi* | [**createTechnique**](docs/TechniquesApi.md#createTechnique) | **PUT** /techniques | Create technique
*RudderApi.TechniquesApi* | [**deleteTechnique**](docs/TechniquesApi.md#deleteTechnique) | **DELETE** /techniques/{techniqueId}/{techniqueVersion} | Delete technique
*RudderApi.TechniquesApi* | [**getTechniqueAllVersion**](docs/TechniquesApi.md#getTechniqueAllVersion) | **GET** /techniques/{techniqueId} | Technique metadata by ID
*RudderApi.TechniquesApi* | [**getTechniqueAllVersionId**](docs/TechniquesApi.md#getTechniqueAllVersionId) | **GET** /techniques/{techniqueId}/{techniqueVersion} | Technique metadata by version and ID
*RudderApi.TechniquesApi* | [**getTechniquesResources**](docs/TechniquesApi.md#getTechniquesResources) | **GET** /techniques/{techniqueId}/{techniqueVersion}/resources | Technique&#39;s resources
*RudderApi.TechniquesApi* | [**listTechniqueVersionDirectives**](docs/TechniquesApi.md#listTechniqueVersionDirectives) | **GET** /techniques/{techniqueId}/{techniqueVersion}/directives | List all directives based on a version of a technique
*RudderApi.TechniquesApi* | [**listTechniques**](docs/TechniquesApi.md#listTechniques) | **GET** /techniques | List all techniques
*RudderApi.TechniquesApi* | [**listTechniquesDirectives**](docs/TechniquesApi.md#listTechniquesDirectives) | **GET** /techniques/{techniqueId}/directives | List all directives based on a technique
*RudderApi.TechniquesApi* | [**listTechniquesVersions**](docs/TechniquesApi.md#listTechniquesVersions) | **GET** /techniques/versions | List versions
*RudderApi.TechniquesApi* | [**methods**](docs/TechniquesApi.md#methods) | **GET** /methods | List methods
*RudderApi.TechniquesApi* | [**reloadMethods**](docs/TechniquesApi.md#reloadMethods) | **POST** /methods/reload | Reload methods
*RudderApi.TechniquesApi* | [**techniqueCategories**](docs/TechniquesApi.md#techniqueCategories) | **GET** /techniques/categories | List categories
*RudderApi.TechniquesApi* | [**techniqueRevisions**](docs/TechniquesApi.md#techniqueRevisions) | **GET** /techniques/{techniqueId}/{techniqueVersion}/revisions | Technique&#39;s revisions
*RudderApi.TechniquesApi* | [**techniques**](docs/TechniquesApi.md#techniques) | **POST** /techniques/reload | Reload techniques
*RudderApi.TechniquesApi* | [**updateTechnique**](docs/TechniquesApi.md#updateTechnique) | **POST** /techniques/{techniqueId}/{techniqueVersion} | Update technique
*RudderApi.UserManagementApi* | [**addUser**](docs/UserManagementApi.md#addUser) | **POST** /usermanagement | Add user
*RudderApi.UserManagementApi* | [**deleteUser**](docs/UserManagementApi.md#deleteUser) | **DELETE** /usermanagement/{username} | Delete an user
*RudderApi.UserManagementApi* | [**getRole**](docs/UserManagementApi.md#getRole) | **GET** /usermanagement/roles | List all roles
*RudderApi.UserManagementApi* | [**getUserInfo**](docs/UserManagementApi.md#getUserInfo) | **GET** /usermanagement/users | List all users
*RudderApi.UserManagementApi* | [**reloadUserConf**](docs/UserManagementApi.md#reloadUserConf) | **GET** /usermanagement/users/reload | Reload user
*RudderApi.UserManagementApi* | [**updateUser**](docs/UserManagementApi.md#updateUser) | **POST** /usermanagement/update/{username} | Update user&#39;s infos


## Documentation for Models

 - [RudderApi.AcceptChangeRequest200Response](docs/AcceptChangeRequest200Response.md)
 - [RudderApi.AcceptChangeRequestRequest](docs/AcceptChangeRequestRequest.md)
 - [RudderApi.AddSecret200Response](docs/AddSecret200Response.md)
 - [RudderApi.AddUser200Response](docs/AddUser200Response.md)
 - [RudderApi.AddUser200ResponseData](docs/AddUser200ResponseData.md)
 - [RudderApi.AddUser200ResponseDataAddedUser](docs/AddUser200ResponseDataAddedUser.md)
 - [RudderApi.AgentKey](docs/AgentKey.md)
 - [RudderApi.AllCampaigns200Response](docs/AllCampaigns200Response.md)
 - [RudderApi.AllCampaigns200ResponseData](docs/AllCampaigns200ResponseData.md)
 - [RudderApi.ApiEndpointsInner](docs/ApiEndpointsInner.md)
 - [RudderApi.ApiGeneralInformations200Response](docs/ApiGeneralInformations200Response.md)
 - [RudderApi.ApiGeneralInformations200ResponseData](docs/ApiGeneralInformations200ResponseData.md)
 - [RudderApi.ApiInformations200Response](docs/ApiInformations200Response.md)
 - [RudderApi.ApiInformations200ResponseData](docs/ApiInformations200ResponseData.md)
 - [RudderApi.ApiInformations200ResponseDataEndpointsInner](docs/ApiInformations200ResponseDataEndpointsInner.md)
 - [RudderApi.ApiSubInformations200Response](docs/ApiSubInformations200Response.md)
 - [RudderApi.ApiVersion](docs/ApiVersion.md)
 - [RudderApi.ApiVersionAllInner](docs/ApiVersionAllInner.md)
 - [RudderApi.ApiVersions](docs/ApiVersions.md)
 - [RudderApi.ApplyPolicyAllNodes200Response](docs/ApplyPolicyAllNodes200Response.md)
 - [RudderApi.ApplyPolicyAllNodes200ResponseDataInner](docs/ApplyPolicyAllNodes200ResponseDataInner.md)
 - [RudderApi.BrandingConf](docs/BrandingConf.md)
 - [RudderApi.CampaignDetails](docs/CampaignDetails.md)
 - [RudderApi.CampaignDetailsDetails](docs/CampaignDetailsDetails.md)
 - [RudderApi.CampaignDetailsInfo](docs/CampaignDetailsInfo.md)
 - [RudderApi.CampaignDetailsInfoSchedule](docs/CampaignDetailsInfoSchedule.md)
 - [RudderApi.CampaignDetailsInfoStatus](docs/CampaignDetailsInfoStatus.md)
 - [RudderApi.CampaignEventDetails](docs/CampaignEventDetails.md)
 - [RudderApi.CampaignEventDetailsStatus](docs/CampaignEventDetailsStatus.md)
 - [RudderApi.CampaignEventNodeResult](docs/CampaignEventNodeResult.md)
 - [RudderApi.CampaignEventNodeResultNodesInner](docs/CampaignEventNodeResultNodesInner.md)
 - [RudderApi.CampaignEventNodeResultNodesInnerResult](docs/CampaignEventNodeResultNodesInnerResult.md)
 - [RudderApi.CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner](docs/CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner.md)
 - [RudderApi.CampaignEventResult](docs/CampaignEventResult.md)
 - [RudderApi.CampaignEventResultNodesInner](docs/CampaignEventResultNodesInner.md)
 - [RudderApi.CampaignScheduleMonthly](docs/CampaignScheduleMonthly.md)
 - [RudderApi.CampaignScheduleMonthlyEnd](docs/CampaignScheduleMonthlyEnd.md)
 - [RudderApi.CampaignScheduleMonthlyStart](docs/CampaignScheduleMonthlyStart.md)
 - [RudderApi.CampaignScheduleOneshot](docs/CampaignScheduleOneshot.md)
 - [RudderApi.CampaignScheduleWeekly](docs/CampaignScheduleWeekly.md)
 - [RudderApi.CampaignScheduleWeeklyEnd](docs/CampaignScheduleWeeklyEnd.md)
 - [RudderApi.CampaignScheduleWeeklyStart](docs/CampaignScheduleWeeklyStart.md)
 - [RudderApi.CampaignSoftwareUpdate](docs/CampaignSoftwareUpdate.md)
 - [RudderApi.CampaignSoftwareUpdateSoftwareUpdateInner](docs/CampaignSoftwareUpdateSoftwareUpdateInner.md)
 - [RudderApi.CampaignStatusArchived](docs/CampaignStatusArchived.md)
 - [RudderApi.CampaignStatusDisabled](docs/CampaignStatusDisabled.md)
 - [RudderApi.CampaignStatusEnabled](docs/CampaignStatusEnabled.md)
 - [RudderApi.CampaignSystemUpdate](docs/CampaignSystemUpdate.md)
 - [RudderApi.CategoriesTree](docs/CategoriesTree.md)
 - [RudderApi.ChangePendingNodeStatus200Response](docs/ChangePendingNodeStatus200Response.md)
 - [RudderApi.ChangePendingNodeStatus200ResponseData](docs/ChangePendingNodeStatus200ResponseData.md)
 - [RudderApi.ChangePendingNodeStatusRequest](docs/ChangePendingNodeStatusRequest.md)
 - [RudderApi.ChangeRequest](docs/ChangeRequest.md)
 - [RudderApi.ChangeRequestChanges](docs/ChangeRequestChanges.md)
 - [RudderApi.ChangeRequestChangesRulesInner](docs/ChangeRequestChangesRulesInner.md)
 - [RudderApi.ChangeRequestDetails200Response](docs/ChangeRequestDetails200Response.md)
 - [RudderApi.Check](docs/Check.md)
 - [RudderApi.CheckCVE200Response](docs/CheckCVE200Response.md)
 - [RudderApi.CheckCVE200ResponseData](docs/CheckCVE200ResponseData.md)
 - [RudderApi.CheckDirective200Response](docs/CheckDirective200Response.md)
 - [RudderApi.Color](docs/Color.md)
 - [RudderApi.ComplianceDirectiveId](docs/ComplianceDirectiveId.md)
 - [RudderApi.ComplianceDirectiveIdData](docs/ComplianceDirectiveIdData.md)
 - [RudderApi.CreateArchive200Response](docs/CreateArchive200Response.md)
 - [RudderApi.CreateArchive200ResponseData](docs/CreateArchive200ResponseData.md)
 - [RudderApi.CreateDataSource200Response](docs/CreateDataSource200Response.md)
 - [RudderApi.CreateDataSource200ResponseData](docs/CreateDataSource200ResponseData.md)
 - [RudderApi.CreateDirective200Response](docs/CreateDirective200Response.md)
 - [RudderApi.CreateGroup200Response](docs/CreateGroup200Response.md)
 - [RudderApi.CreateGroupCategory200Response](docs/CreateGroupCategory200Response.md)
 - [RudderApi.CreateGroupCategory200ResponseData](docs/CreateGroupCategory200ResponseData.md)
 - [RudderApi.CreateNodes200Response](docs/CreateNodes200Response.md)
 - [RudderApi.CreateNodes200ResponseData](docs/CreateNodes200ResponseData.md)
 - [RudderApi.CreateParameter200Response](docs/CreateParameter200Response.md)
 - [RudderApi.CreateRule200Response](docs/CreateRule200Response.md)
 - [RudderApi.CreateRuleCategory200Response](docs/CreateRuleCategory200Response.md)
 - [RudderApi.CreateRuleCategory200ResponseData](docs/CreateRuleCategory200ResponseData.md)
 - [RudderApi.CreateTechnique200Response](docs/CreateTechnique200Response.md)
 - [RudderApi.CreateTechnique200ResponseData](docs/CreateTechnique200ResponseData.md)
 - [RudderApi.CreateTechnique200ResponseDataTechniques](docs/CreateTechnique200ResponseDataTechniques.md)
 - [RudderApi.CveCheck](docs/CveCheck.md)
 - [RudderApi.CveCheckPackagesInner](docs/CveCheckPackagesInner.md)
 - [RudderApi.CveCheckScore](docs/CveCheckScore.md)
 - [RudderApi.CveDetails](docs/CveDetails.md)
 - [RudderApi.CveDetailsCvssv2](docs/CveDetailsCvssv2.md)
 - [RudderApi.CveDetailsCvssv3](docs/CveDetailsCvssv3.md)
 - [RudderApi.Datasource](docs/Datasource.md)
 - [RudderApi.DatasourceRunParameters](docs/DatasourceRunParameters.md)
 - [RudderApi.DatasourceRunParametersSchedule](docs/DatasourceRunParametersSchedule.md)
 - [RudderApi.DatasourceType](docs/DatasourceType.md)
 - [RudderApi.DatasourceTypeParameters](docs/DatasourceTypeParameters.md)
 - [RudderApi.DatasourceTypeParametersHeadersInner](docs/DatasourceTypeParametersHeadersInner.md)
 - [RudderApi.DatasourceTypeParametersRequestMode](docs/DatasourceTypeParametersRequestMode.md)
 - [RudderApi.DeclineChangeRequest200Response](docs/DeclineChangeRequest200Response.md)
 - [RudderApi.DeleteCampaign200Response](docs/DeleteCampaign200Response.md)
 - [RudderApi.DeleteCampaignEvent200Response](docs/DeleteCampaignEvent200Response.md)
 - [RudderApi.DeleteDataSource200Response](docs/DeleteDataSource200Response.md)
 - [RudderApi.DeleteDirective200Response](docs/DeleteDirective200Response.md)
 - [RudderApi.DeleteGroup200Response](docs/DeleteGroup200Response.md)
 - [RudderApi.DeleteGroupCategory200Response](docs/DeleteGroupCategory200Response.md)
 - [RudderApi.DeleteNode200Response](docs/DeleteNode200Response.md)
 - [RudderApi.DeleteParameter200Response](docs/DeleteParameter200Response.md)
 - [RudderApi.DeleteParameter500Response](docs/DeleteParameter500Response.md)
 - [RudderApi.DeleteRule200Response](docs/DeleteRule200Response.md)
 - [RudderApi.DeleteRuleCategory200Response](docs/DeleteRuleCategory200Response.md)
 - [RudderApi.DeleteRuleCategory200ResponseData](docs/DeleteRuleCategory200ResponseData.md)
 - [RudderApi.DeleteSecret200Response](docs/DeleteSecret200Response.md)
 - [RudderApi.DeleteTechnique200Response](docs/DeleteTechnique200Response.md)
 - [RudderApi.DeleteTechnique200ResponseData](docs/DeleteTechnique200ResponseData.md)
 - [RudderApi.DeleteTechnique200ResponseDataTechniques](docs/DeleteTechnique200ResponseDataTechniques.md)
 - [RudderApi.DeleteUser200Response](docs/DeleteUser200Response.md)
 - [RudderApi.DeleteUser200ResponseData](docs/DeleteUser200ResponseData.md)
 - [RudderApi.DeleteUser200ResponseDataDeletedUser](docs/DeleteUser200ResponseDataDeletedUser.md)
 - [RudderApi.DemoteToNode200Response](docs/DemoteToNode200Response.md)
 - [RudderApi.Directive](docs/Directive.md)
 - [RudderApi.DirectiveDetails200Response](docs/DirectiveDetails200Response.md)
 - [RudderApi.DirectiveNew](docs/DirectiveNew.md)
 - [RudderApi.DirectiveNodeCompliance](docs/DirectiveNodeCompliance.md)
 - [RudderApi.DirectiveNodeComplianceComplianceDetails](docs/DirectiveNodeComplianceComplianceDetails.md)
 - [RudderApi.DirectiveRuleCompliance](docs/DirectiveRuleCompliance.md)
 - [RudderApi.DirectiveRuleComplianceComponentsInner](docs/DirectiveRuleComplianceComponentsInner.md)
 - [RudderApi.DirectiveTagsInner](docs/DirectiveTagsInner.md)
 - [RudderApi.EditorTechnique](docs/EditorTechnique.md)
 - [RudderApi.EditorTechniqueCallsInner](docs/EditorTechniqueCallsInner.md)
 - [RudderApi.FileWatcherRestart200Response](docs/FileWatcherRestart200Response.md)
 - [RudderApi.FileWatcherStart200Response](docs/FileWatcherStart200Response.md)
 - [RudderApi.FileWatcherStop200Response](docs/FileWatcherStop200Response.md)
 - [RudderApi.GetAllCampaignEvents200Response](docs/GetAllCampaignEvents200Response.md)
 - [RudderApi.GetAllCampaignEvents200ResponseData](docs/GetAllCampaignEvents200ResponseData.md)
 - [RudderApi.GetAllCve200Response](docs/GetAllCve200Response.md)
 - [RudderApi.GetAllCve200ResponseData](docs/GetAllCve200ResponseData.md)
 - [RudderApi.GetAllDataSources200Response](docs/GetAllDataSources200Response.md)
 - [RudderApi.GetAllDataSources200ResponseData](docs/GetAllDataSources200ResponseData.md)
 - [RudderApi.GetAllSecrets200Response](docs/GetAllSecrets200Response.md)
 - [RudderApi.GetAllSecrets200ResponseData](docs/GetAllSecrets200ResponseData.md)
 - [RudderApi.GetAllSecrets200ResponseDataSecretsInner](docs/GetAllSecrets200ResponseDataSecretsInner.md)
 - [RudderApi.GetAllSettings200Response](docs/GetAllSettings200Response.md)
 - [RudderApi.GetAllSettings200ResponseData](docs/GetAllSettings200ResponseData.md)
 - [RudderApi.GetAllSettings200ResponseDataSettings](docs/GetAllSettings200ResponseDataSettings.md)
 - [RudderApi.GetAllSettings200ResponseDataSettingsAllowedNetworksInner](docs/GetAllSettings200ResponseDataSettingsAllowedNetworksInner.md)
 - [RudderApi.GetAllowedNetworks200Response](docs/GetAllowedNetworks200Response.md)
 - [RudderApi.GetAllowedNetworks200ResponseData](docs/GetAllowedNetworks200ResponseData.md)
 - [RudderApi.GetAllowedNetworks200ResponseDataSettings](docs/GetAllowedNetworks200ResponseDataSettings.md)
 - [RudderApi.GetBrandingConf200Response](docs/GetBrandingConf200Response.md)
 - [RudderApi.GetBrandingConf200ResponseData](docs/GetBrandingConf200ResponseData.md)
 - [RudderApi.GetCVECheckConfiguration200Response](docs/GetCVECheckConfiguration200Response.md)
 - [RudderApi.GetCVECheckConfiguration200ResponseData](docs/GetCVECheckConfiguration200ResponseData.md)
 - [RudderApi.GetCVEList200Response](docs/GetCVEList200Response.md)
 - [RudderApi.GetCVEListRequest](docs/GetCVEListRequest.md)
 - [RudderApi.GetCampaign200Response](docs/GetCampaign200Response.md)
 - [RudderApi.GetCampaignEventResult200Response](docs/GetCampaignEventResult200Response.md)
 - [RudderApi.GetCampaignEventResult200ResponseData](docs/GetCampaignEventResult200ResponseData.md)
 - [RudderApi.GetCampaignEventResultForNode200Response](docs/GetCampaignEventResultForNode200Response.md)
 - [RudderApi.GetCampaignEventResultForNode200ResponseData](docs/GetCampaignEventResultForNode200ResponseData.md)
 - [RudderApi.GetCampaignHistory200Response](docs/GetCampaignHistory200Response.md)
 - [RudderApi.GetCampaignHistory200ResponseData](docs/GetCampaignHistory200ResponseData.md)
 - [RudderApi.GetCve200Response](docs/GetCve200Response.md)
 - [RudderApi.GetDataSource200Response](docs/GetDataSource200Response.md)
 - [RudderApi.GetDirectiveComplianceId200Response](docs/GetDirectiveComplianceId200Response.md)
 - [RudderApi.GetDirectivesCompliance200Response](docs/GetDirectivesCompliance200Response.md)
 - [RudderApi.GetDirectivesCompliance200ResponseData](docs/GetDirectivesCompliance200ResponseData.md)
 - [RudderApi.GetDirectivesCompliance200ResponseDataDirectivesCompliance](docs/GetDirectivesCompliance200ResponseDataDirectivesCompliance.md)
 - [RudderApi.GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails](docs/GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails.md)
 - [RudderApi.GetEventsCampaign200Response](docs/GetEventsCampaign200Response.md)
 - [RudderApi.GetGlobalCompliance200Response](docs/GetGlobalCompliance200Response.md)
 - [RudderApi.GetGlobalCompliance200ResponseData](docs/GetGlobalCompliance200ResponseData.md)
 - [RudderApi.GetGlobalCompliance200ResponseDataGlobalCompliance](docs/GetGlobalCompliance200ResponseDataGlobalCompliance.md)
 - [RudderApi.GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails](docs/GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails.md)
 - [RudderApi.GetGroupCategoryDetails200Response](docs/GetGroupCategoryDetails200Response.md)
 - [RudderApi.GetGroupTree200Response](docs/GetGroupTree200Response.md)
 - [RudderApi.GetGroupTree200ResponseData](docs/GetGroupTree200ResponseData.md)
 - [RudderApi.GetHealthcheckResult200Response](docs/GetHealthcheckResult200Response.md)
 - [RudderApi.GetLastCVECheck200Response](docs/GetLastCVECheck200Response.md)
 - [RudderApi.GetLastCVECheck200ResponseData](docs/GetLastCVECheck200ResponseData.md)
 - [RudderApi.GetNodeCompliance200Response](docs/GetNodeCompliance200Response.md)
 - [RudderApi.GetNodesCompliance200Response](docs/GetNodesCompliance200Response.md)
 - [RudderApi.GetNodesCompliance200ResponseData](docs/GetNodesCompliance200ResponseData.md)
 - [RudderApi.GetNodesCompliance200ResponseDataNodesInner](docs/GetNodesCompliance200ResponseDataNodesInner.md)
 - [RudderApi.GetNodesStatus200Response](docs/GetNodesStatus200Response.md)
 - [RudderApi.GetNodesStatus200ResponseData](docs/GetNodesStatus200ResponseData.md)
 - [RudderApi.GetNodesStatus200ResponseDataNodesInner](docs/GetNodesStatus200ResponseDataNodesInner.md)
 - [RudderApi.GetRole200Response](docs/GetRole200Response.md)
 - [RudderApi.GetRole200ResponseDataInner](docs/GetRole200ResponseDataInner.md)
 - [RudderApi.GetRuleCategoryDetails200Response](docs/GetRuleCategoryDetails200Response.md)
 - [RudderApi.GetRuleCategoryDetails200ResponseData](docs/GetRuleCategoryDetails200ResponseData.md)
 - [RudderApi.GetRuleCompliance200Response](docs/GetRuleCompliance200Response.md)
 - [RudderApi.GetRuleTree200Response](docs/GetRuleTree200Response.md)
 - [RudderApi.GetRuleTree200ResponseData](docs/GetRuleTree200ResponseData.md)
 - [RudderApi.GetRulesCompliance200Response](docs/GetRulesCompliance200Response.md)
 - [RudderApi.GetRulesCompliance200ResponseData](docs/GetRulesCompliance200ResponseData.md)
 - [RudderApi.GetRulesCompliance200ResponseDataRulesInner](docs/GetRulesCompliance200ResponseDataRulesInner.md)
 - [RudderApi.GetSecret200Response](docs/GetSecret200Response.md)
 - [RudderApi.GetSetting200Response](docs/GetSetting200Response.md)
 - [RudderApi.GetSetting200ResponseData](docs/GetSetting200ResponseData.md)
 - [RudderApi.GetStatus200Response](docs/GetStatus200Response.md)
 - [RudderApi.GetStatus200ResponseData](docs/GetStatus200ResponseData.md)
 - [RudderApi.GetSystemInfo200Response](docs/GetSystemInfo200Response.md)
 - [RudderApi.GetSystemInfo200ResponseData](docs/GetSystemInfo200ResponseData.md)
 - [RudderApi.GetSystemInfo200ResponseDataRudder](docs/GetSystemInfo200ResponseDataRudder.md)
 - [RudderApi.GetTechniqueAllVersion200Response](docs/GetTechniqueAllVersion200Response.md)
 - [RudderApi.GetTechniqueAllVersion200ResponseData](docs/GetTechniqueAllVersion200ResponseData.md)
 - [RudderApi.GetTechniqueAllVersion200ResponseDataTechniquesInner](docs/GetTechniqueAllVersion200ResponseDataTechniquesInner.md)
 - [RudderApi.GetTechniquesResources200Response](docs/GetTechniquesResources200Response.md)
 - [RudderApi.GetTechniquesResources200ResponseData](docs/GetTechniquesResources200ResponseData.md)
 - [RudderApi.GetUserInfo200Response](docs/GetUserInfo200Response.md)
 - [RudderApi.GetUserInfo200ResponseData](docs/GetUserInfo200ResponseData.md)
 - [RudderApi.Group](docs/Group.md)
 - [RudderApi.GroupCategory](docs/GroupCategory.md)
 - [RudderApi.GroupCategoryUpdate](docs/GroupCategoryUpdate.md)
 - [RudderApi.GroupDetails200Response](docs/GroupDetails200Response.md)
 - [RudderApi.GroupNew](docs/GroupNew.md)
 - [RudderApi.GroupNewQuery](docs/GroupNewQuery.md)
 - [RudderApi.GroupPropertiesInner](docs/GroupPropertiesInner.md)
 - [RudderApi.GroupQuery](docs/GroupQuery.md)
 - [RudderApi.GroupQueryWhereInner](docs/GroupQueryWhereInner.md)
 - [RudderApi.GroupUpdate](docs/GroupUpdate.md)
 - [RudderApi.Import200Response](docs/Import200Response.md)
 - [RudderApi.Import200ResponseData](docs/Import200ResponseData.md)
 - [RudderApi.ListAcceptedNodes200Response](docs/ListAcceptedNodes200Response.md)
 - [RudderApi.ListAcceptedNodes200ResponseData](docs/ListAcceptedNodes200ResponseData.md)
 - [RudderApi.ListArchives200Response](docs/ListArchives200Response.md)
 - [RudderApi.ListArchives200ResponseData](docs/ListArchives200ResponseData.md)
 - [RudderApi.ListArchives200ResponseDataFullInner](docs/ListArchives200ResponseDataFullInner.md)
 - [RudderApi.ListChangeRequests200Response](docs/ListChangeRequests200Response.md)
 - [RudderApi.ListChangeRequests200ResponseData](docs/ListChangeRequests200ResponseData.md)
 - [RudderApi.ListDirectives200Response](docs/ListDirectives200Response.md)
 - [RudderApi.ListDirectives200ResponseData](docs/ListDirectives200ResponseData.md)
 - [RudderApi.ListGroups200Response](docs/ListGroups200Response.md)
 - [RudderApi.ListGroups200ResponseData](docs/ListGroups200ResponseData.md)
 - [RudderApi.ListParameters200Response](docs/ListParameters200Response.md)
 - [RudderApi.ListParameters200ResponseData](docs/ListParameters200ResponseData.md)
 - [RudderApi.ListPendingNodes200Response](docs/ListPendingNodes200Response.md)
 - [RudderApi.ListRules200Response](docs/ListRules200Response.md)
 - [RudderApi.ListRules200ResponseData](docs/ListRules200ResponseData.md)
 - [RudderApi.ListTechniqueVersionDirectives200Response](docs/ListTechniqueVersionDirectives200Response.md)
 - [RudderApi.ListTechniques200Response](docs/ListTechniques200Response.md)
 - [RudderApi.ListTechniques200ResponseData](docs/ListTechniques200ResponseData.md)
 - [RudderApi.ListTechniquesDirectives200Response](docs/ListTechniquesDirectives200Response.md)
 - [RudderApi.ListTechniquesVersions200Response](docs/ListTechniquesVersions200Response.md)
 - [RudderApi.ListTechniquesVersions200ResponseData](docs/ListTechniquesVersions200ResponseData.md)
 - [RudderApi.ListUsers200Response](docs/ListUsers200Response.md)
 - [RudderApi.Logo](docs/Logo.md)
 - [RudderApi.MethodParameter](docs/MethodParameter.md)
 - [RudderApi.MethodParameterConstraints](docs/MethodParameterConstraints.md)
 - [RudderApi.Methods](docs/Methods.md)
 - [RudderApi.Methods200Response](docs/Methods200Response.md)
 - [RudderApi.Methods200ResponseData](docs/Methods200ResponseData.md)
 - [RudderApi.MethodsCondition](docs/MethodsCondition.md)
 - [RudderApi.MethodsDeprecated](docs/MethodsDeprecated.md)
 - [RudderApi.ModifyAllowedNetworks200Response](docs/ModifyAllowedNetworks200Response.md)
 - [RudderApi.ModifyAllowedNetworks200ResponseData](docs/ModifyAllowedNetworks200ResponseData.md)
 - [RudderApi.ModifyAllowedNetworksRequest](docs/ModifyAllowedNetworksRequest.md)
 - [RudderApi.ModifyAllowedNetworksRequestAllowedNetworks](docs/ModifyAllowedNetworksRequestAllowedNetworks.md)
 - [RudderApi.ModifySetting200Response](docs/ModifySetting200Response.md)
 - [RudderApi.ModifySettingRequest](docs/ModifySettingRequest.md)
 - [RudderApi.NodeAddInner](docs/NodeAddInner.md)
 - [RudderApi.NodeAddInnerPropertiesInner](docs/NodeAddInnerPropertiesInner.md)
 - [RudderApi.NodeComplianceComponent](docs/NodeComplianceComponent.md)
 - [RudderApi.NodeComplianceComponentValuesInner](docs/NodeComplianceComponentValuesInner.md)
 - [RudderApi.NodeComplianceComponentValuesInnerReportsInner](docs/NodeComplianceComponentValuesInnerReportsInner.md)
 - [RudderApi.NodeDetails200Response](docs/NodeDetails200Response.md)
 - [RudderApi.NodeFull](docs/NodeFull.md)
 - [RudderApi.NodeFullBios](docs/NodeFullBios.md)
 - [RudderApi.NodeFullControllersInner](docs/NodeFullControllersInner.md)
 - [RudderApi.NodeFullEnvironmentVariablesInner](docs/NodeFullEnvironmentVariablesInner.md)
 - [RudderApi.NodeFullFileSystemsInner](docs/NodeFullFileSystemsInner.md)
 - [RudderApi.NodeFullMachine](docs/NodeFullMachine.md)
 - [RudderApi.NodeFullManagementTechnologyDetails](docs/NodeFullManagementTechnologyDetails.md)
 - [RudderApi.NodeFullManagementTechnologyInner](docs/NodeFullManagementTechnologyInner.md)
 - [RudderApi.NodeFullMemoriesInner](docs/NodeFullMemoriesInner.md)
 - [RudderApi.NodeFullNetworkInterfacesInner](docs/NodeFullNetworkInterfacesInner.md)
 - [RudderApi.NodeFullOs](docs/NodeFullOs.md)
 - [RudderApi.NodeFullPortsInner](docs/NodeFullPortsInner.md)
 - [RudderApi.NodeFullProcessesInner](docs/NodeFullProcessesInner.md)
 - [RudderApi.NodeFullProcessorsInner](docs/NodeFullProcessorsInner.md)
 - [RudderApi.NodeFullSlotsInner](docs/NodeFullSlotsInner.md)
 - [RudderApi.NodeFullSoftwareInner](docs/NodeFullSoftwareInner.md)
 - [RudderApi.NodeFullSoftwareInnerLicense](docs/NodeFullSoftwareInnerLicense.md)
 - [RudderApi.NodeFullSoftwareUpdateInner](docs/NodeFullSoftwareUpdateInner.md)
 - [RudderApi.NodeFullSoundInner](docs/NodeFullSoundInner.md)
 - [RudderApi.NodeFullStorageInner](docs/NodeFullStorageInner.md)
 - [RudderApi.NodeFullTimezone](docs/NodeFullTimezone.md)
 - [RudderApi.NodeFullVideosInner](docs/NodeFullVideosInner.md)
 - [RudderApi.NodeFullVirtualMachinesInner](docs/NodeFullVirtualMachinesInner.md)
 - [RudderApi.NodeInheritedProperties](docs/NodeInheritedProperties.md)
 - [RudderApi.NodeInheritedProperties200Response](docs/NodeInheritedProperties200Response.md)
 - [RudderApi.NodeInheritedPropertiesPropertiesInner](docs/NodeInheritedPropertiesPropertiesInner.md)
 - [RudderApi.NodeInheritedPropertiesPropertiesInnerHierarchyInner](docs/NodeInheritedPropertiesPropertiesInnerHierarchyInner.md)
 - [RudderApi.NodeSettings](docs/NodeSettings.md)
 - [RudderApi.Os](docs/Os.md)
 - [RudderApi.Parameter](docs/Parameter.md)
 - [RudderApi.ParameterDetails200Response](docs/ParameterDetails200Response.md)
 - [RudderApi.PromoteToRelay200Response](docs/PromoteToRelay200Response.md)
 - [RudderApi.PurgeSoftware200Response](docs/PurgeSoftware200Response.md)
 - [RudderApi.QueueInformation200Response](docs/QueueInformation200Response.md)
 - [RudderApi.QueueInformation200ResponseData](docs/QueueInformation200ResponseData.md)
 - [RudderApi.ReadCVEfromFS200Response](docs/ReadCVEfromFS200Response.md)
 - [RudderApi.RegeneratePolicies200Response](docs/RegeneratePolicies200Response.md)
 - [RudderApi.RegeneratePolicies200ResponseData](docs/RegeneratePolicies200ResponseData.md)
 - [RudderApi.ReloadAll200Response](docs/ReloadAll200Response.md)
 - [RudderApi.ReloadAll200ResponseData](docs/ReloadAll200ResponseData.md)
 - [RudderApi.ReloadAllDatasourcesAllNodes200Response](docs/ReloadAllDatasourcesAllNodes200Response.md)
 - [RudderApi.ReloadAllDatasourcesOneNode200Response](docs/ReloadAllDatasourcesOneNode200Response.md)
 - [RudderApi.ReloadGroup200Response](docs/ReloadGroup200Response.md)
 - [RudderApi.ReloadGroups200Response](docs/ReloadGroups200Response.md)
 - [RudderApi.ReloadGroups200ResponseData](docs/ReloadGroups200ResponseData.md)
 - [RudderApi.ReloadOneDatasourceAllNodes200Response](docs/ReloadOneDatasourceAllNodes200Response.md)
 - [RudderApi.ReloadOneDatasourceOneNode200Response](docs/ReloadOneDatasourceOneNode200Response.md)
 - [RudderApi.ReloadTechniques200Response](docs/ReloadTechniques200Response.md)
 - [RudderApi.ReloadTechniques200ResponseData](docs/ReloadTechniques200ResponseData.md)
 - [RudderApi.ReloadUserConf200Response](docs/ReloadUserConf200Response.md)
 - [RudderApi.ReloadUserConf200ResponseData](docs/ReloadUserConf200ResponseData.md)
 - [RudderApi.ReloadUserConf200ResponseDataReload](docs/ReloadUserConf200ResponseDataReload.md)
 - [RudderApi.RemoveValidatedUser200Response](docs/RemoveValidatedUser200Response.md)
 - [RudderApi.RestoreArchive200Response](docs/RestoreArchive200Response.md)
 - [RudderApi.RestoreArchive200ResponseData](docs/RestoreArchive200ResponseData.md)
 - [RudderApi.Rule](docs/Rule.md)
 - [RudderApi.RuleCategory](docs/RuleCategory.md)
 - [RudderApi.RuleCategoryUpdate](docs/RuleCategoryUpdate.md)
 - [RudderApi.RuleComplianceComponent](docs/RuleComplianceComponent.md)
 - [RudderApi.RuleComplianceComponentComplianceDetails](docs/RuleComplianceComponentComplianceDetails.md)
 - [RudderApi.RuleComplianceComponentComponentsInner](docs/RuleComplianceComponentComponentsInner.md)
 - [RudderApi.RuleComplianceComponentComponentsInnerValuesInner](docs/RuleComplianceComponentComponentsInnerValuesInner.md)
 - [RudderApi.RuleComplianceComponentComponentsInnerValuesInnerReportsInner](docs/RuleComplianceComponentComponentsInnerValuesInnerReportsInner.md)
 - [RudderApi.RuleDetails200Response](docs/RuleDetails200Response.md)
 - [RudderApi.RuleNew](docs/RuleNew.md)
 - [RudderApi.RuleTarget](docs/RuleTarget.md)
 - [RudderApi.RuleTargetsInner](docs/RuleTargetsInner.md)
 - [RudderApi.RuleTargetsInnerExclude](docs/RuleTargetsInnerExclude.md)
 - [RudderApi.RuleTargetsInnerInclude](docs/RuleTargetsInnerInclude.md)
 - [RudderApi.RuleWithCategory](docs/RuleWithCategory.md)
 - [RudderApi.SaveCampaign200Response](docs/SaveCampaign200Response.md)
 - [RudderApi.SaveCampaignEvent200Response](docs/SaveCampaignEvent200Response.md)
 - [RudderApi.SaveWorkflowUser200Response](docs/SaveWorkflowUser200Response.md)
 - [RudderApi.SaveWorkflowUserRequest](docs/SaveWorkflowUserRequest.md)
 - [RudderApi.ScheduleCampaign200Response](docs/ScheduleCampaign200Response.md)
 - [RudderApi.Secrets](docs/Secrets.md)
 - [RudderApi.SetAllowedNetworks200Response](docs/SetAllowedNetworks200Response.md)
 - [RudderApi.SetAllowedNetworks200ResponseData](docs/SetAllowedNetworks200ResponseData.md)
 - [RudderApi.SetAllowedNetworksRequest](docs/SetAllowedNetworksRequest.md)
 - [RudderApi.TechniqueBlock](docs/TechniqueBlock.md)
 - [RudderApi.TechniqueBlockReportingLogic](docs/TechniqueBlockReportingLogic.md)
 - [RudderApi.TechniqueCategories200Response](docs/TechniqueCategories200Response.md)
 - [RudderApi.TechniqueCategories200ResponseData](docs/TechniqueCategories200ResponseData.md)
 - [RudderApi.TechniqueCategory](docs/TechniqueCategory.md)
 - [RudderApi.TechniqueMethodCall](docs/TechniqueMethodCall.md)
 - [RudderApi.TechniqueMethodCallParametersInner](docs/TechniqueMethodCallParametersInner.md)
 - [RudderApi.TechniqueParameter](docs/TechniqueParameter.md)
 - [RudderApi.TechniqueResource](docs/TechniqueResource.md)
 - [RudderApi.TechniqueRevisions200Response](docs/TechniqueRevisions200Response.md)
 - [RudderApi.TechniqueRevisions200ResponseData](docs/TechniqueRevisions200ResponseData.md)
 - [RudderApi.TechniquesResourcesInner](docs/TechniquesResourcesInner.md)
 - [RudderApi.TechniquesRevisionsInner](docs/TechniquesRevisionsInner.md)
 - [RudderApi.TechniquesVersionsInner](docs/TechniquesVersionsInner.md)
 - [RudderApi.Timezone](docs/Timezone.md)
 - [RudderApi.UpdateBRandingConf200Response](docs/UpdateBRandingConf200Response.md)
 - [RudderApi.UpdateCVE200Response](docs/UpdateCVE200Response.md)
 - [RudderApi.UpdateCVE200ResponseData](docs/UpdateCVE200ResponseData.md)
 - [RudderApi.UpdateCVECheckConfiguration200Response](docs/UpdateCVECheckConfiguration200Response.md)
 - [RudderApi.UpdateCVECheckConfigurationRequest](docs/UpdateCVECheckConfigurationRequest.md)
 - [RudderApi.UpdateCVERequest](docs/UpdateCVERequest.md)
 - [RudderApi.UpdateChangeRequest200Response](docs/UpdateChangeRequest200Response.md)
 - [RudderApi.UpdateChangeRequestRequest](docs/UpdateChangeRequestRequest.md)
 - [RudderApi.UpdateDataSource200Response](docs/UpdateDataSource200Response.md)
 - [RudderApi.UpdateDirective200Response](docs/UpdateDirective200Response.md)
 - [RudderApi.UpdateGroup200Response](docs/UpdateGroup200Response.md)
 - [RudderApi.UpdateGroupCategory200Response](docs/UpdateGroupCategory200Response.md)
 - [RudderApi.UpdateNode200Response](docs/UpdateNode200Response.md)
 - [RudderApi.UpdateParameter200Response](docs/UpdateParameter200Response.md)
 - [RudderApi.UpdatePolicies200Response](docs/UpdatePolicies200Response.md)
 - [RudderApi.UpdateRule200Response](docs/UpdateRule200Response.md)
 - [RudderApi.UpdateRule200ResponseData](docs/UpdateRule200ResponseData.md)
 - [RudderApi.UpdateRuleCategory200Response](docs/UpdateRuleCategory200Response.md)
 - [RudderApi.UpdateSecret200Response](docs/UpdateSecret200Response.md)
 - [RudderApi.UpdateUser200Response](docs/UpdateUser200Response.md)
 - [RudderApi.UpdateUser200ResponseData](docs/UpdateUser200ResponseData.md)
 - [RudderApi.UpdateUser200ResponseDataUpdatedUser](docs/UpdateUser200ResponseDataUpdatedUser.md)
 - [RudderApi.UploadInventory200Response](docs/UploadInventory200Response.md)
 - [RudderApi.Users](docs/Users.md)
 - [RudderApi.ValidatedUser](docs/ValidatedUser.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### API-Tokens


- **Type**: API key
- **API key parameter name**: X-API-Token
- **Location**: HTTP header

