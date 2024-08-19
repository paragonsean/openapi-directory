# openapi-java-client

Rudder API
- API version: 17
  - Build date: 2024-10-12T12:31:58.781092-04:00[America/New_York]
  - Generator version: 7.9.0

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


  For more information, please visit [https://www.rudder.io](https://www.rudder.io)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>17</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:17"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-17.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.ApiInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ApiInfoApi apiInstance = new ApiInfoApi(defaultClient);
    try {
      ApiGeneralInformations200Response result = apiInstance.apiGeneralInformations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiInfoApi#apiGeneralInformations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiInfoApi* | [**apiGeneralInformations**](docs/ApiInfoApi.md#apiGeneralInformations) | **GET** /info | List all endoints
*ApiInfoApi* | [**apiInformations**](docs/ApiInfoApi.md#apiInformations) | **GET** /info/details/{endpointName} | Get information about one API endpoint
*ApiInfoApi* | [**apiSubInformations**](docs/ApiInfoApi.md#apiSubInformations) | **GET** /info/{sectionId} | Get information on endpoint in a section
*ArchivesApi* | [**callImport**](docs/ArchivesApi.md#callImport) | **POST** /archives/import | Import a ZIP archive of policies into Rudder
*ArchivesApi* | [**export**](docs/ArchivesApi.md#export) | **GET** /archives/export | Get a ZIP archive of the requested items and their dependencies
*BrandingApi* | [**getBrandingConf**](docs/BrandingApi.md#getBrandingConf) | **GET** /branding | Get branding configuration
*BrandingApi* | [**reloadBrandingConf**](docs/BrandingApi.md#reloadBrandingConf) | **POST** /branding/reload | Reload branding file
*BrandingApi* | [**updateBRandingConf**](docs/BrandingApi.md#updateBRandingConf) | **POST** /branding | Update web interface customization
*CampaignsApi* | [**allCampaigns**](docs/CampaignsApi.md#allCampaigns) | **GET** /campaigns | Get all campaigns details
*CampaignsApi* | [**deleteCampaign**](docs/CampaignsApi.md#deleteCampaign) | **DELETE** /campaigns/{id} | Delete a campaign
*CampaignsApi* | [**deleteCampaignEvent**](docs/CampaignsApi.md#deleteCampaignEvent) | **DELETE** /campaigns/events/{id} | Delete a campaign event details
*CampaignsApi* | [**getAllCampaignEvents**](docs/CampaignsApi.md#getAllCampaignEvents) | **GET** /campaigns/events | Get all campaign events
*CampaignsApi* | [**getCampaign**](docs/CampaignsApi.md#getCampaign) | **GET** /campaigns/{id} | Get a campaign details
*CampaignsApi* | [**getCampaignEvent**](docs/CampaignsApi.md#getCampaignEvent) | **GET** /campaigns/events/{id} | Get a campaign event details
*CampaignsApi* | [**getEventsCampaign**](docs/CampaignsApi.md#getEventsCampaign) | **GET** /campaigns/{id}/events | Get campaign events for a campaign
*CampaignsApi* | [**saveCampaign**](docs/CampaignsApi.md#saveCampaign) | **POST** /campaigns | Save a campaign
*CampaignsApi* | [**saveCampaignEvent**](docs/CampaignsApi.md#saveCampaignEvent) | **POST** /campaigns/events/{id} | Update an existing event
*CampaignsApi* | [**scheduleCampaign**](docs/CampaignsApi.md#scheduleCampaign) | **POST** /campaigns/{id}/schedule | Schedule a campaign event for a campaign
*ChangeRequestsApi* | [**acceptChangeRequest**](docs/ChangeRequestsApi.md#acceptChangeRequest) | **POST** /changeRequests/{changeRequestId}/accept | Accept a request details
*ChangeRequestsApi* | [**changeRequestDetails**](docs/ChangeRequestsApi.md#changeRequestDetails) | **GET** /changeRequests/{changeRequestId} | Get a change request details
*ChangeRequestsApi* | [**declineChangeRequest**](docs/ChangeRequestsApi.md#declineChangeRequest) | **DELETE** /changeRequests/{changeRequestId} | Decline a request details
*ChangeRequestsApi* | [**listChangeRequests**](docs/ChangeRequestsApi.md#listChangeRequests) | **GET** /api/changeRequests | List all change requests
*ChangeRequestsApi* | [**listUsers**](docs/ChangeRequestsApi.md#listUsers) | **GET** /users | List user
*ChangeRequestsApi* | [**removeValidatedUser**](docs/ChangeRequestsApi.md#removeValidatedUser) | **DELETE** /validatedUsers/{username} | Remove an user from validated user list
*ChangeRequestsApi* | [**saveWorkflowUser**](docs/ChangeRequestsApi.md#saveWorkflowUser) | **POST** /validatedUsers | Update validated user list
*ChangeRequestsApi* | [**updateChangeRequest**](docs/ChangeRequestsApi.md#updateChangeRequest) | **POST** /changeRequests/{changeRequestId} | Update a request details
*ComplianceApi* | [**getDirectiveComplianceId**](docs/ComplianceApi.md#getDirectiveComplianceId) | **GET** /compliance/directives/{directiveId} | Compliance details by directive
*ComplianceApi* | [**getDirectivesCompliance**](docs/ComplianceApi.md#getDirectivesCompliance) | **GET** /compliance/directives | Compliance details for all directives
*ComplianceApi* | [**getGlobalCompliance**](docs/ComplianceApi.md#getGlobalCompliance) | **GET** /compliance | Global compliance
*ComplianceApi* | [**getNodeCompliance**](docs/ComplianceApi.md#getNodeCompliance) | **GET** /compliance/nodes/{nodeId} | Compliance details by node
*ComplianceApi* | [**getNodesCompliance**](docs/ComplianceApi.md#getNodesCompliance) | **GET** /compliance/nodes | Compliance details for all nodes
*ComplianceApi* | [**getRuleCompliance**](docs/ComplianceApi.md#getRuleCompliance) | **GET** /compliance/rules/{ruleId} | Compliance details by rule
*ComplianceApi* | [**getRulesCompliance**](docs/ComplianceApi.md#getRulesCompliance) | **GET** /compliance/rules | Compliance details for all rules
*CveApi* | [**checkCVE**](docs/CveApi.md#checkCVE) | **POST** /cve/check | Trigger a CVE check
*CveApi* | [**getAllCve**](docs/CveApi.md#getAllCve) | **GET** /cve | Get all CVE details
*CveApi* | [**getCVECheckConfiguration**](docs/CveApi.md#getCVECheckConfiguration) | **GET** /cve/check/config | Get CVE check config
*CveApi* | [**getCVEList**](docs/CveApi.md#getCVEList) | **POST** /cve/list | Get a list of CVE details
*CveApi* | [**getCve**](docs/CveApi.md#getCve) | **GET** /cve/{cveId} | Get a CVE details
*CveApi* | [**getLastCVECheck**](docs/CveApi.md#getLastCVECheck) | **GET** /cve/check/last | Get last CVE check result
*CveApi* | [**readCVEfromFS**](docs/CveApi.md#readCVEfromFS) | **POST** /cve/update/fs | Update CVE database from file system
*CveApi* | [**updateCVE**](docs/CveApi.md#updateCVE) | **POST** /cve/update | Update CVE database from remote source
*CveApi* | [**updateCVECheckConfiguration**](docs/CveApi.md#updateCVECheckConfiguration) | **POST** /cve/check/config | Update cve check config
*DataSourcesApi* | [**createDataSource**](docs/DataSourcesApi.md#createDataSource) | **PUT** /datasources | Create a data source
*DataSourcesApi* | [**deleteDataSource**](docs/DataSourcesApi.md#deleteDataSource) | **DELETE** /datasources/{datasourceId} | Delete a data source
*DataSourcesApi* | [**getAllDataSources**](docs/DataSourcesApi.md#getAllDataSources) | **GET** /datasources | List all data sources
*DataSourcesApi* | [**getDataSource**](docs/DataSourcesApi.md#getDataSource) | **GET** /datasources/{datasourceId} | Get data source configuration
*DataSourcesApi* | [**reloadAllDatasourcesAllNodes**](docs/DataSourcesApi.md#reloadAllDatasourcesAllNodes) | **POST** /datasources/reload | Update properties from data sources
*DataSourcesApi* | [**reloadAllDatasourcesOneNode**](docs/DataSourcesApi.md#reloadAllDatasourcesOneNode) | **POST** /nodes/{nodeId}/fetchData | Update properties for one node from all data sources
*DataSourcesApi* | [**reloadOneDatasourceAllNodes**](docs/DataSourcesApi.md#reloadOneDatasourceAllNodes) | **POST** /datasources/reload/{datasourceId} | Update properties from data sources
*DataSourcesApi* | [**reloadOneDatasourceOneNode**](docs/DataSourcesApi.md#reloadOneDatasourceOneNode) | **POST** /nodes/{nodeId}/fetchData/{datasourceId} | Update properties for one node from a data source
*DataSourcesApi* | [**updateDataSource**](docs/DataSourcesApi.md#updateDataSource) | **POST** /datasources/{datasourceId} | Update a data source configuration
*DirectivesApi* | [**checkDirective**](docs/DirectivesApi.md#checkDirective) | **POST** /directives/{directiveId}/check | Check that update on a directive is valid
*DirectivesApi* | [**createDirective**](docs/DirectivesApi.md#createDirective) | **PUT** /directives | Create a directive
*DirectivesApi* | [**deleteDirective**](docs/DirectivesApi.md#deleteDirective) | **DELETE** /directives/{directiveId} | Delete a directive
*DirectivesApi* | [**directiveDetails**](docs/DirectivesApi.md#directiveDetails) | **GET** /directives/{directiveId} | Get directive details
*DirectivesApi* | [**listDirectives**](docs/DirectivesApi.md#listDirectives) | **GET** /directives | List all directives
*DirectivesApi* | [**updateDirective**](docs/DirectivesApi.md#updateDirective) | **POST** /directives/{directiveId} | Update a directive details
*GroupsApi* | [**createGroup**](docs/GroupsApi.md#createGroup) | **PUT** /groups | Create a group
*GroupsApi* | [**createGroupCategory**](docs/GroupsApi.md#createGroupCategory) | **PUT** /groups/categories | Create a group category
*GroupsApi* | [**deleteGroup**](docs/GroupsApi.md#deleteGroup) | **DELETE** /groups/{groupId} | Delete a group
*GroupsApi* | [**deleteGroupCategory**](docs/GroupsApi.md#deleteGroupCategory) | **DELETE** /groups/categories/{groupCategoryId} | Delete group category
*GroupsApi* | [**getGroupCategoryDetails**](docs/GroupsApi.md#getGroupCategoryDetails) | **GET** /groups/categories/{groupCategoryId} | Get group category details
*GroupsApi* | [**getGroupTree**](docs/GroupsApi.md#getGroupTree) | **GET** /groups/tree | Get groups tree
*GroupsApi* | [**groupDetails**](docs/GroupsApi.md#groupDetails) | **GET** /groups/{groupId} | Get group details
*GroupsApi* | [**listGroups**](docs/GroupsApi.md#listGroups) | **GET** /groups | List all groups
*GroupsApi* | [**reloadGroup**](docs/GroupsApi.md#reloadGroup) | **POST** /groups/{groupId}/reload | Reload a group
*GroupsApi* | [**updateGroup**](docs/GroupsApi.md#updateGroup) | **POST** /groups/{groupId} | Update group details
*GroupsApi* | [**updateGroupCategory**](docs/GroupsApi.md#updateGroupCategory) | **POST** /groups/categories/{groupCategoryId} | Update group category details
*InventoriesApi* | [**fileWatcherRestart**](docs/InventoriesApi.md#fileWatcherRestart) | **POST** /inventories/watcher/restart | Restart inventory watcher
*InventoriesApi* | [**fileWatcherStart**](docs/InventoriesApi.md#fileWatcherStart) | **POST** /inventories/watcher/start | Start inventory watcher
*InventoriesApi* | [**fileWatcherStop**](docs/InventoriesApi.md#fileWatcherStop) | **POST** /inventories/watcher/stop | Stop inventory watcher
*InventoriesApi* | [**queueInformation**](docs/InventoriesApi.md#queueInformation) | **GET** /inventories/info | Get information about inventory processing queue
*InventoriesApi* | [**uploadInventory**](docs/InventoriesApi.md#uploadInventory) | **POST** /inventories/upload | Upload an inventory for processing
*NodesApi* | [**applyPolicy**](docs/NodesApi.md#applyPolicy) | **POST** /nodes/{nodeId}/applyPolicy | Trigger an agent run
*NodesApi* | [**applyPolicyAllNodes**](docs/NodesApi.md#applyPolicyAllNodes) | **POST** /nodes/applyPolicy | Trigger an agent run on all nodes
*NodesApi* | [**changePendingNodeStatus**](docs/NodesApi.md#changePendingNodeStatus) | **POST** /nodes/pending/{nodeId} | Update pending Node status
*NodesApi* | [**createNodes**](docs/NodesApi.md#createNodes) | **PUT** /nodes | Create one or several new nodes
*NodesApi* | [**deleteNode**](docs/NodesApi.md#deleteNode) | **DELETE** /nodes/{nodeId} | Delete a node
*NodesApi* | [**getNodesStatus**](docs/NodesApi.md#getNodesStatus) | **GET** /nodes/status | Get nodes acceptation status
*NodesApi* | [**listAcceptedNodes**](docs/NodesApi.md#listAcceptedNodes) | **GET** /nodes | List managed nodes
*NodesApi* | [**listPendingNodes**](docs/NodesApi.md#listPendingNodes) | **GET** /nodes/pending | List pending nodes
*NodesApi* | [**nodeDetails**](docs/NodesApi.md#nodeDetails) | **GET** /nodes/{nodeId} | Get information about a node
*NodesApi* | [**nodeInheritedProperties**](docs/NodesApi.md#nodeInheritedProperties) | **GET** /nodes/{nodeId}/inheritedProperties | Get inherited node properties for a node
*NodesApi* | [**updateNode**](docs/NodesApi.md#updateNode) | **POST** /nodes/{nodeId} | Update node settings and properties
*ParametersApi* | [**createParameter**](docs/ParametersApi.md#createParameter) | **PUT** /parameters | Create a new parameter
*ParametersApi* | [**deleteParameter**](docs/ParametersApi.md#deleteParameter) | **DELETE** /parameters/{parameterId} | Delete a parameter
*ParametersApi* | [**listParameters**](docs/ParametersApi.md#listParameters) | **GET** /parameters | List all global parameters
*ParametersApi* | [**parameterDetails**](docs/ParametersApi.md#parameterDetails) | **GET** /parameters/{parameterId} | Get the value of a parameter
*ParametersApi* | [**updateParameter**](docs/ParametersApi.md#updateParameter) | **POST** /parameters/{parameterId} | Update a parameter&#39;s value
*RulesApi* | [**createRule**](docs/RulesApi.md#createRule) | **PUT** /rules | Create a rule
*RulesApi* | [**createRuleCategory**](docs/RulesApi.md#createRuleCategory) | **PUT** /rules/categories | Create a rule category
*RulesApi* | [**deleteRule**](docs/RulesApi.md#deleteRule) | **DELETE** /rules/{ruleId} | Delete a rule
*RulesApi* | [**deleteRuleCategory**](docs/RulesApi.md#deleteRuleCategory) | **DELETE** /rules/categories/{ruleCategoryId} | Delete group category
*RulesApi* | [**getRuleCategoryDetails**](docs/RulesApi.md#getRuleCategoryDetails) | **GET** /rules/categories/{ruleCategoryId} | Get rule category details
*RulesApi* | [**getRuleTree**](docs/RulesApi.md#getRuleTree) | **GET** /rules/tree | Get rules tree
*RulesApi* | [**listRules**](docs/RulesApi.md#listRules) | **GET** /rules | List all rules
*RulesApi* | [**ruleDetails**](docs/RulesApi.md#ruleDetails) | **GET** /rules/{ruleId} | Get a rule details
*RulesApi* | [**updateRule**](docs/RulesApi.md#updateRule) | **POST** /rules/{ruleId} | Update a rule details
*RulesApi* | [**updateRuleCategory**](docs/RulesApi.md#updateRuleCategory) | **POST** /rules/categories/{ruleCategoryId} | Update rule category details
*ScaleOutRelayApi* | [**demoteToNode**](docs/ScaleOutRelayApi.md#demoteToNode) | **POST** /scaleoutrelay/demote/{nodeId} | Demote a relay to simple node
*ScaleOutRelayApi* | [**promoteToRelay**](docs/ScaleOutRelayApi.md#promoteToRelay) | **POST** /scaleoutrelay/promote/{nodeId} | Promote a node to relay
*SecretManagementApi* | [**addSecret**](docs/SecretManagementApi.md#addSecret) | **PUT** /secret | Create a secret
*SecretManagementApi* | [**deleteSecret**](docs/SecretManagementApi.md#deleteSecret) | **DELETE** /secret/{name} | Delete a secret
*SecretManagementApi* | [**getAllSecrets**](docs/SecretManagementApi.md#getAllSecrets) | **GET** /secret | List all secrets
*SecretManagementApi* | [**getSecret**](docs/SecretManagementApi.md#getSecret) | **GET** /secret/{name} | Get one secret
*SecretManagementApi* | [**updateSecret**](docs/SecretManagementApi.md#updateSecret) | **POST** /secret | Update a secret
*SettingsApi* | [**getAllSettings**](docs/SettingsApi.md#getAllSettings) | **GET** /settings | List all settings
*SettingsApi* | [**getAllowedNetworks**](docs/SettingsApi.md#getAllowedNetworks) | **GET** /settings/allowed_networks/{nodeId} | Get allowed networks for a policy server
*SettingsApi* | [**getSetting**](docs/SettingsApi.md#getSetting) | **GET** /settings/{settingId} | Get the value of a setting
*SettingsApi* | [**modifyAllowedNetworks**](docs/SettingsApi.md#modifyAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId}/diff | Modify allowed networks for a policy server
*SettingsApi* | [**modifySetting**](docs/SettingsApi.md#modifySetting) | **POST** /settings/{settingId} | Set the value of a setting
*SettingsApi* | [**setAllowedNetworks**](docs/SettingsApi.md#setAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId} | Set allowed networks for a policy server
*StatusApi* | [**none**](docs/StatusApi.md#none) | **GET** /status | Check if Rudder is alive
*SystemApi* | [**createArchive**](docs/SystemApi.md#createArchive) | **POST** /system/archives/{archiveKind} | Create an archive
*SystemApi* | [**getHealthcheckResult**](docs/SystemApi.md#getHealthcheckResult) | **GET** /system/healthcheck | Get healthcheck
*SystemApi* | [**getStatus**](docs/SystemApi.md#getStatus) | **GET** /system/status | Get server status
*SystemApi* | [**getSystemInfo**](docs/SystemApi.md#getSystemInfo) | **GET** /system/info | Get server information
*SystemApi* | [**getZipArchive**](docs/SystemApi.md#getZipArchive) | **GET** /system/archives/{archiveKind}/zip/{commitId} | Get an archive as a ZIP
*SystemApi* | [**listArchives**](docs/SystemApi.md#listArchives) | **GET** /system/archives/{archiveKind} | List archives
*SystemApi* | [**purgeSoftware**](docs/SystemApi.md#purgeSoftware) | **POST** /system/maintenance/purgeSoftware | Trigger batch for cleaning unreferenced software
*SystemApi* | [**regeneratePolicies**](docs/SystemApi.md#regeneratePolicies) | **POST** /system/regenerate/policies | Trigger a new policy generation
*SystemApi* | [**reloadAll**](docs/SystemApi.md#reloadAll) | **POST** /system/reload | Reload both techniques and dynamic groups
*SystemApi* | [**reloadGroups**](docs/SystemApi.md#reloadGroups) | **POST** /system/reload/groups | Reload dynamic groups
*SystemApi* | [**reloadTechniques**](docs/SystemApi.md#reloadTechniques) | **POST** /system/reload/techniques | Reload techniques
*SystemApi* | [**restoreArchive**](docs/SystemApi.md#restoreArchive) | **POST** /system/archives/{archiveKind}/restore/{archiveRestoreKind} | Restore an archive
*SystemApi* | [**updatePolicies**](docs/SystemApi.md#updatePolicies) | **POST** /system/update/policies | Trigger update of policies
*SystemUpdateCampaignsApi* | [**getCampaignEventResult**](docs/SystemUpdateCampaignsApi.md#getCampaignEventResult) | **GET** /systemUpdate/events/{id}/result | Get a campaign event result
*SystemUpdateCampaignsApi* | [**getCampaignEventResultForNode**](docs/SystemUpdateCampaignsApi.md#getCampaignEventResultForNode) | **GET** /systemUpdate/events/{id}/result/{nodeId} | Get detailed campaign event result for a Node
*SystemUpdateCampaignsApi* | [**getCampaignHistory**](docs/SystemUpdateCampaignsApi.md#getCampaignHistory) | **GET** /systemUpdate/campaigns/{id}/history | Get a campaign result history
*TechniquesApi* | [**createTechnique**](docs/TechniquesApi.md#createTechnique) | **PUT** /techniques | Create technique
*TechniquesApi* | [**deleteTechnique**](docs/TechniquesApi.md#deleteTechnique) | **DELETE** /techniques/{techniqueId}/{techniqueVersion} | Delete technique
*TechniquesApi* | [**getTechniqueAllVersion**](docs/TechniquesApi.md#getTechniqueAllVersion) | **GET** /techniques/{techniqueId} | Technique metadata by ID
*TechniquesApi* | [**getTechniqueAllVersionId**](docs/TechniquesApi.md#getTechniqueAllVersionId) | **GET** /techniques/{techniqueId}/{techniqueVersion} | Technique metadata by version and ID
*TechniquesApi* | [**getTechniquesResources**](docs/TechniquesApi.md#getTechniquesResources) | **GET** /techniques/{techniqueId}/{techniqueVersion}/resources | Technique&#39;s resources
*TechniquesApi* | [**listTechniqueVersionDirectives**](docs/TechniquesApi.md#listTechniqueVersionDirectives) | **GET** /techniques/{techniqueId}/{techniqueVersion}/directives | List all directives based on a version of a technique
*TechniquesApi* | [**listTechniques**](docs/TechniquesApi.md#listTechniques) | **GET** /techniques | List all techniques
*TechniquesApi* | [**listTechniquesDirectives**](docs/TechniquesApi.md#listTechniquesDirectives) | **GET** /techniques/{techniqueId}/directives | List all directives based on a technique
*TechniquesApi* | [**listTechniquesVersions**](docs/TechniquesApi.md#listTechniquesVersions) | **GET** /techniques/versions | List versions
*TechniquesApi* | [**methods**](docs/TechniquesApi.md#methods) | **GET** /methods | List methods
*TechniquesApi* | [**reloadMethods**](docs/TechniquesApi.md#reloadMethods) | **POST** /methods/reload | Reload methods
*TechniquesApi* | [**techniqueCategories**](docs/TechniquesApi.md#techniqueCategories) | **GET** /techniques/categories | List categories
*TechniquesApi* | [**techniqueRevisions**](docs/TechniquesApi.md#techniqueRevisions) | **GET** /techniques/{techniqueId}/{techniqueVersion}/revisions | Technique&#39;s revisions
*TechniquesApi* | [**techniques**](docs/TechniquesApi.md#techniques) | **POST** /techniques/reload | Reload techniques
*TechniquesApi* | [**updateTechnique**](docs/TechniquesApi.md#updateTechnique) | **POST** /techniques/{techniqueId}/{techniqueVersion} | Update technique
*UserManagementApi* | [**addUser**](docs/UserManagementApi.md#addUser) | **POST** /usermanagement | Add user
*UserManagementApi* | [**deleteUser**](docs/UserManagementApi.md#deleteUser) | **DELETE** /usermanagement/{username} | Delete an user
*UserManagementApi* | [**getRole**](docs/UserManagementApi.md#getRole) | **GET** /usermanagement/roles | List all roles
*UserManagementApi* | [**getUserInfo**](docs/UserManagementApi.md#getUserInfo) | **GET** /usermanagement/users | List all users
*UserManagementApi* | [**reloadUserConf**](docs/UserManagementApi.md#reloadUserConf) | **GET** /usermanagement/users/reload | Reload user
*UserManagementApi* | [**updateUser**](docs/UserManagementApi.md#updateUser) | **POST** /usermanagement/update/{username} | Update user&#39;s infos


## Documentation for Models

 - [AcceptChangeRequest200Response](docs/AcceptChangeRequest200Response.md)
 - [AcceptChangeRequestRequest](docs/AcceptChangeRequestRequest.md)
 - [AddSecret200Response](docs/AddSecret200Response.md)
 - [AddUser200Response](docs/AddUser200Response.md)
 - [AddUser200ResponseData](docs/AddUser200ResponseData.md)
 - [AddUser200ResponseDataAddedUser](docs/AddUser200ResponseDataAddedUser.md)
 - [AgentKey](docs/AgentKey.md)
 - [AllCampaigns200Response](docs/AllCampaigns200Response.md)
 - [AllCampaigns200ResponseData](docs/AllCampaigns200ResponseData.md)
 - [ApiEndpointsInner](docs/ApiEndpointsInner.md)
 - [ApiGeneralInformations200Response](docs/ApiGeneralInformations200Response.md)
 - [ApiGeneralInformations200ResponseData](docs/ApiGeneralInformations200ResponseData.md)
 - [ApiInformations200Response](docs/ApiInformations200Response.md)
 - [ApiInformations200ResponseData](docs/ApiInformations200ResponseData.md)
 - [ApiInformations200ResponseDataEndpointsInner](docs/ApiInformations200ResponseDataEndpointsInner.md)
 - [ApiSubInformations200Response](docs/ApiSubInformations200Response.md)
 - [ApiVersion](docs/ApiVersion.md)
 - [ApiVersionAllInner](docs/ApiVersionAllInner.md)
 - [ApiVersions](docs/ApiVersions.md)
 - [ApplyPolicyAllNodes200Response](docs/ApplyPolicyAllNodes200Response.md)
 - [ApplyPolicyAllNodes200ResponseDataInner](docs/ApplyPolicyAllNodes200ResponseDataInner.md)
 - [BrandingConf](docs/BrandingConf.md)
 - [CampaignDetails](docs/CampaignDetails.md)
 - [CampaignDetailsDetails](docs/CampaignDetailsDetails.md)
 - [CampaignDetailsInfo](docs/CampaignDetailsInfo.md)
 - [CampaignDetailsInfoSchedule](docs/CampaignDetailsInfoSchedule.md)
 - [CampaignDetailsInfoStatus](docs/CampaignDetailsInfoStatus.md)
 - [CampaignEventDetails](docs/CampaignEventDetails.md)
 - [CampaignEventDetailsStatus](docs/CampaignEventDetailsStatus.md)
 - [CampaignEventNodeResult](docs/CampaignEventNodeResult.md)
 - [CampaignEventNodeResultNodesInner](docs/CampaignEventNodeResultNodesInner.md)
 - [CampaignEventNodeResultNodesInnerResult](docs/CampaignEventNodeResultNodesInnerResult.md)
 - [CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner](docs/CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner.md)
 - [CampaignEventResult](docs/CampaignEventResult.md)
 - [CampaignEventResultNodesInner](docs/CampaignEventResultNodesInner.md)
 - [CampaignScheduleMonthly](docs/CampaignScheduleMonthly.md)
 - [CampaignScheduleMonthlyEnd](docs/CampaignScheduleMonthlyEnd.md)
 - [CampaignScheduleMonthlyStart](docs/CampaignScheduleMonthlyStart.md)
 - [CampaignScheduleOneshot](docs/CampaignScheduleOneshot.md)
 - [CampaignScheduleWeekly](docs/CampaignScheduleWeekly.md)
 - [CampaignScheduleWeeklyEnd](docs/CampaignScheduleWeeklyEnd.md)
 - [CampaignScheduleWeeklyStart](docs/CampaignScheduleWeeklyStart.md)
 - [CampaignSoftwareUpdate](docs/CampaignSoftwareUpdate.md)
 - [CampaignSoftwareUpdateSoftwareUpdateInner](docs/CampaignSoftwareUpdateSoftwareUpdateInner.md)
 - [CampaignStatusArchived](docs/CampaignStatusArchived.md)
 - [CampaignStatusDisabled](docs/CampaignStatusDisabled.md)
 - [CampaignStatusEnabled](docs/CampaignStatusEnabled.md)
 - [CampaignSystemUpdate](docs/CampaignSystemUpdate.md)
 - [CategoriesTree](docs/CategoriesTree.md)
 - [ChangePendingNodeStatus200Response](docs/ChangePendingNodeStatus200Response.md)
 - [ChangePendingNodeStatus200ResponseData](docs/ChangePendingNodeStatus200ResponseData.md)
 - [ChangePendingNodeStatusRequest](docs/ChangePendingNodeStatusRequest.md)
 - [ChangeRequest](docs/ChangeRequest.md)
 - [ChangeRequestChanges](docs/ChangeRequestChanges.md)
 - [ChangeRequestChangesRulesInner](docs/ChangeRequestChangesRulesInner.md)
 - [ChangeRequestDetails200Response](docs/ChangeRequestDetails200Response.md)
 - [Check](docs/Check.md)
 - [CheckCVE200Response](docs/CheckCVE200Response.md)
 - [CheckCVE200ResponseData](docs/CheckCVE200ResponseData.md)
 - [CheckDirective200Response](docs/CheckDirective200Response.md)
 - [Color](docs/Color.md)
 - [ComplianceDirectiveId](docs/ComplianceDirectiveId.md)
 - [ComplianceDirectiveIdData](docs/ComplianceDirectiveIdData.md)
 - [CreateArchive200Response](docs/CreateArchive200Response.md)
 - [CreateArchive200ResponseData](docs/CreateArchive200ResponseData.md)
 - [CreateDataSource200Response](docs/CreateDataSource200Response.md)
 - [CreateDataSource200ResponseData](docs/CreateDataSource200ResponseData.md)
 - [CreateDirective200Response](docs/CreateDirective200Response.md)
 - [CreateGroup200Response](docs/CreateGroup200Response.md)
 - [CreateGroupCategory200Response](docs/CreateGroupCategory200Response.md)
 - [CreateGroupCategory200ResponseData](docs/CreateGroupCategory200ResponseData.md)
 - [CreateNodes200Response](docs/CreateNodes200Response.md)
 - [CreateNodes200ResponseData](docs/CreateNodes200ResponseData.md)
 - [CreateParameter200Response](docs/CreateParameter200Response.md)
 - [CreateRule200Response](docs/CreateRule200Response.md)
 - [CreateRuleCategory200Response](docs/CreateRuleCategory200Response.md)
 - [CreateRuleCategory200ResponseData](docs/CreateRuleCategory200ResponseData.md)
 - [CreateTechnique200Response](docs/CreateTechnique200Response.md)
 - [CreateTechnique200ResponseData](docs/CreateTechnique200ResponseData.md)
 - [CreateTechnique200ResponseDataTechniques](docs/CreateTechnique200ResponseDataTechniques.md)
 - [CveCheck](docs/CveCheck.md)
 - [CveCheckPackagesInner](docs/CveCheckPackagesInner.md)
 - [CveCheckScore](docs/CveCheckScore.md)
 - [CveDetails](docs/CveDetails.md)
 - [CveDetailsCvssv2](docs/CveDetailsCvssv2.md)
 - [CveDetailsCvssv3](docs/CveDetailsCvssv3.md)
 - [Datasource](docs/Datasource.md)
 - [DatasourceRunParameters](docs/DatasourceRunParameters.md)
 - [DatasourceRunParametersSchedule](docs/DatasourceRunParametersSchedule.md)
 - [DatasourceType](docs/DatasourceType.md)
 - [DatasourceTypeParameters](docs/DatasourceTypeParameters.md)
 - [DatasourceTypeParametersHeadersInner](docs/DatasourceTypeParametersHeadersInner.md)
 - [DatasourceTypeParametersRequestMode](docs/DatasourceTypeParametersRequestMode.md)
 - [DeclineChangeRequest200Response](docs/DeclineChangeRequest200Response.md)
 - [DeleteCampaign200Response](docs/DeleteCampaign200Response.md)
 - [DeleteCampaignEvent200Response](docs/DeleteCampaignEvent200Response.md)
 - [DeleteDataSource200Response](docs/DeleteDataSource200Response.md)
 - [DeleteDirective200Response](docs/DeleteDirective200Response.md)
 - [DeleteGroup200Response](docs/DeleteGroup200Response.md)
 - [DeleteGroupCategory200Response](docs/DeleteGroupCategory200Response.md)
 - [DeleteNode200Response](docs/DeleteNode200Response.md)
 - [DeleteParameter200Response](docs/DeleteParameter200Response.md)
 - [DeleteParameter500Response](docs/DeleteParameter500Response.md)
 - [DeleteRule200Response](docs/DeleteRule200Response.md)
 - [DeleteRuleCategory200Response](docs/DeleteRuleCategory200Response.md)
 - [DeleteRuleCategory200ResponseData](docs/DeleteRuleCategory200ResponseData.md)
 - [DeleteSecret200Response](docs/DeleteSecret200Response.md)
 - [DeleteTechnique200Response](docs/DeleteTechnique200Response.md)
 - [DeleteTechnique200ResponseData](docs/DeleteTechnique200ResponseData.md)
 - [DeleteTechnique200ResponseDataTechniques](docs/DeleteTechnique200ResponseDataTechniques.md)
 - [DeleteUser200Response](docs/DeleteUser200Response.md)
 - [DeleteUser200ResponseData](docs/DeleteUser200ResponseData.md)
 - [DeleteUser200ResponseDataDeletedUser](docs/DeleteUser200ResponseDataDeletedUser.md)
 - [DemoteToNode200Response](docs/DemoteToNode200Response.md)
 - [Directive](docs/Directive.md)
 - [DirectiveDetails200Response](docs/DirectiveDetails200Response.md)
 - [DirectiveNew](docs/DirectiveNew.md)
 - [DirectiveNodeCompliance](docs/DirectiveNodeCompliance.md)
 - [DirectiveNodeComplianceComplianceDetails](docs/DirectiveNodeComplianceComplianceDetails.md)
 - [DirectiveRuleCompliance](docs/DirectiveRuleCompliance.md)
 - [DirectiveRuleComplianceComponentsInner](docs/DirectiveRuleComplianceComponentsInner.md)
 - [DirectiveTagsInner](docs/DirectiveTagsInner.md)
 - [EditorTechnique](docs/EditorTechnique.md)
 - [EditorTechniqueCallsInner](docs/EditorTechniqueCallsInner.md)
 - [FileWatcherRestart200Response](docs/FileWatcherRestart200Response.md)
 - [FileWatcherStart200Response](docs/FileWatcherStart200Response.md)
 - [FileWatcherStop200Response](docs/FileWatcherStop200Response.md)
 - [GetAllCampaignEvents200Response](docs/GetAllCampaignEvents200Response.md)
 - [GetAllCampaignEvents200ResponseData](docs/GetAllCampaignEvents200ResponseData.md)
 - [GetAllCve200Response](docs/GetAllCve200Response.md)
 - [GetAllCve200ResponseData](docs/GetAllCve200ResponseData.md)
 - [GetAllDataSources200Response](docs/GetAllDataSources200Response.md)
 - [GetAllDataSources200ResponseData](docs/GetAllDataSources200ResponseData.md)
 - [GetAllSecrets200Response](docs/GetAllSecrets200Response.md)
 - [GetAllSecrets200ResponseData](docs/GetAllSecrets200ResponseData.md)
 - [GetAllSecrets200ResponseDataSecretsInner](docs/GetAllSecrets200ResponseDataSecretsInner.md)
 - [GetAllSettings200Response](docs/GetAllSettings200Response.md)
 - [GetAllSettings200ResponseData](docs/GetAllSettings200ResponseData.md)
 - [GetAllSettings200ResponseDataSettings](docs/GetAllSettings200ResponseDataSettings.md)
 - [GetAllSettings200ResponseDataSettingsAllowedNetworksInner](docs/GetAllSettings200ResponseDataSettingsAllowedNetworksInner.md)
 - [GetAllowedNetworks200Response](docs/GetAllowedNetworks200Response.md)
 - [GetAllowedNetworks200ResponseData](docs/GetAllowedNetworks200ResponseData.md)
 - [GetAllowedNetworks200ResponseDataSettings](docs/GetAllowedNetworks200ResponseDataSettings.md)
 - [GetBrandingConf200Response](docs/GetBrandingConf200Response.md)
 - [GetBrandingConf200ResponseData](docs/GetBrandingConf200ResponseData.md)
 - [GetCVECheckConfiguration200Response](docs/GetCVECheckConfiguration200Response.md)
 - [GetCVECheckConfiguration200ResponseData](docs/GetCVECheckConfiguration200ResponseData.md)
 - [GetCVEList200Response](docs/GetCVEList200Response.md)
 - [GetCVEListRequest](docs/GetCVEListRequest.md)
 - [GetCampaign200Response](docs/GetCampaign200Response.md)
 - [GetCampaignEventResult200Response](docs/GetCampaignEventResult200Response.md)
 - [GetCampaignEventResult200ResponseData](docs/GetCampaignEventResult200ResponseData.md)
 - [GetCampaignEventResultForNode200Response](docs/GetCampaignEventResultForNode200Response.md)
 - [GetCampaignEventResultForNode200ResponseData](docs/GetCampaignEventResultForNode200ResponseData.md)
 - [GetCampaignHistory200Response](docs/GetCampaignHistory200Response.md)
 - [GetCampaignHistory200ResponseData](docs/GetCampaignHistory200ResponseData.md)
 - [GetCve200Response](docs/GetCve200Response.md)
 - [GetDataSource200Response](docs/GetDataSource200Response.md)
 - [GetDirectiveComplianceId200Response](docs/GetDirectiveComplianceId200Response.md)
 - [GetDirectivesCompliance200Response](docs/GetDirectivesCompliance200Response.md)
 - [GetDirectivesCompliance200ResponseData](docs/GetDirectivesCompliance200ResponseData.md)
 - [GetDirectivesCompliance200ResponseDataDirectivesCompliance](docs/GetDirectivesCompliance200ResponseDataDirectivesCompliance.md)
 - [GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails](docs/GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails.md)
 - [GetEventsCampaign200Response](docs/GetEventsCampaign200Response.md)
 - [GetGlobalCompliance200Response](docs/GetGlobalCompliance200Response.md)
 - [GetGlobalCompliance200ResponseData](docs/GetGlobalCompliance200ResponseData.md)
 - [GetGlobalCompliance200ResponseDataGlobalCompliance](docs/GetGlobalCompliance200ResponseDataGlobalCompliance.md)
 - [GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails](docs/GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails.md)
 - [GetGroupCategoryDetails200Response](docs/GetGroupCategoryDetails200Response.md)
 - [GetGroupTree200Response](docs/GetGroupTree200Response.md)
 - [GetGroupTree200ResponseData](docs/GetGroupTree200ResponseData.md)
 - [GetHealthcheckResult200Response](docs/GetHealthcheckResult200Response.md)
 - [GetLastCVECheck200Response](docs/GetLastCVECheck200Response.md)
 - [GetLastCVECheck200ResponseData](docs/GetLastCVECheck200ResponseData.md)
 - [GetNodeCompliance200Response](docs/GetNodeCompliance200Response.md)
 - [GetNodesCompliance200Response](docs/GetNodesCompliance200Response.md)
 - [GetNodesCompliance200ResponseData](docs/GetNodesCompliance200ResponseData.md)
 - [GetNodesCompliance200ResponseDataNodesInner](docs/GetNodesCompliance200ResponseDataNodesInner.md)
 - [GetNodesStatus200Response](docs/GetNodesStatus200Response.md)
 - [GetNodesStatus200ResponseData](docs/GetNodesStatus200ResponseData.md)
 - [GetNodesStatus200ResponseDataNodesInner](docs/GetNodesStatus200ResponseDataNodesInner.md)
 - [GetRole200Response](docs/GetRole200Response.md)
 - [GetRole200ResponseDataInner](docs/GetRole200ResponseDataInner.md)
 - [GetRuleCategoryDetails200Response](docs/GetRuleCategoryDetails200Response.md)
 - [GetRuleCategoryDetails200ResponseData](docs/GetRuleCategoryDetails200ResponseData.md)
 - [GetRuleCompliance200Response](docs/GetRuleCompliance200Response.md)
 - [GetRuleTree200Response](docs/GetRuleTree200Response.md)
 - [GetRuleTree200ResponseData](docs/GetRuleTree200ResponseData.md)
 - [GetRulesCompliance200Response](docs/GetRulesCompliance200Response.md)
 - [GetRulesCompliance200ResponseData](docs/GetRulesCompliance200ResponseData.md)
 - [GetRulesCompliance200ResponseDataRulesInner](docs/GetRulesCompliance200ResponseDataRulesInner.md)
 - [GetSecret200Response](docs/GetSecret200Response.md)
 - [GetSetting200Response](docs/GetSetting200Response.md)
 - [GetSetting200ResponseData](docs/GetSetting200ResponseData.md)
 - [GetStatus200Response](docs/GetStatus200Response.md)
 - [GetStatus200ResponseData](docs/GetStatus200ResponseData.md)
 - [GetSystemInfo200Response](docs/GetSystemInfo200Response.md)
 - [GetSystemInfo200ResponseData](docs/GetSystemInfo200ResponseData.md)
 - [GetSystemInfo200ResponseDataRudder](docs/GetSystemInfo200ResponseDataRudder.md)
 - [GetTechniqueAllVersion200Response](docs/GetTechniqueAllVersion200Response.md)
 - [GetTechniqueAllVersion200ResponseData](docs/GetTechniqueAllVersion200ResponseData.md)
 - [GetTechniqueAllVersion200ResponseDataTechniquesInner](docs/GetTechniqueAllVersion200ResponseDataTechniquesInner.md)
 - [GetTechniquesResources200Response](docs/GetTechniquesResources200Response.md)
 - [GetTechniquesResources200ResponseData](docs/GetTechniquesResources200ResponseData.md)
 - [GetUserInfo200Response](docs/GetUserInfo200Response.md)
 - [GetUserInfo200ResponseData](docs/GetUserInfo200ResponseData.md)
 - [Group](docs/Group.md)
 - [GroupCategory](docs/GroupCategory.md)
 - [GroupCategoryUpdate](docs/GroupCategoryUpdate.md)
 - [GroupDetails200Response](docs/GroupDetails200Response.md)
 - [GroupNew](docs/GroupNew.md)
 - [GroupNewQuery](docs/GroupNewQuery.md)
 - [GroupPropertiesInner](docs/GroupPropertiesInner.md)
 - [GroupQuery](docs/GroupQuery.md)
 - [GroupQueryWhereInner](docs/GroupQueryWhereInner.md)
 - [GroupUpdate](docs/GroupUpdate.md)
 - [Import200Response](docs/Import200Response.md)
 - [Import200ResponseData](docs/Import200ResponseData.md)
 - [ListAcceptedNodes200Response](docs/ListAcceptedNodes200Response.md)
 - [ListAcceptedNodes200ResponseData](docs/ListAcceptedNodes200ResponseData.md)
 - [ListArchives200Response](docs/ListArchives200Response.md)
 - [ListArchives200ResponseData](docs/ListArchives200ResponseData.md)
 - [ListArchives200ResponseDataFullInner](docs/ListArchives200ResponseDataFullInner.md)
 - [ListChangeRequests200Response](docs/ListChangeRequests200Response.md)
 - [ListChangeRequests200ResponseData](docs/ListChangeRequests200ResponseData.md)
 - [ListDirectives200Response](docs/ListDirectives200Response.md)
 - [ListDirectives200ResponseData](docs/ListDirectives200ResponseData.md)
 - [ListGroups200Response](docs/ListGroups200Response.md)
 - [ListGroups200ResponseData](docs/ListGroups200ResponseData.md)
 - [ListParameters200Response](docs/ListParameters200Response.md)
 - [ListParameters200ResponseData](docs/ListParameters200ResponseData.md)
 - [ListPendingNodes200Response](docs/ListPendingNodes200Response.md)
 - [ListRules200Response](docs/ListRules200Response.md)
 - [ListRules200ResponseData](docs/ListRules200ResponseData.md)
 - [ListTechniqueVersionDirectives200Response](docs/ListTechniqueVersionDirectives200Response.md)
 - [ListTechniques200Response](docs/ListTechniques200Response.md)
 - [ListTechniques200ResponseData](docs/ListTechniques200ResponseData.md)
 - [ListTechniquesDirectives200Response](docs/ListTechniquesDirectives200Response.md)
 - [ListTechniquesVersions200Response](docs/ListTechniquesVersions200Response.md)
 - [ListTechniquesVersions200ResponseData](docs/ListTechniquesVersions200ResponseData.md)
 - [ListUsers200Response](docs/ListUsers200Response.md)
 - [Logo](docs/Logo.md)
 - [MethodParameter](docs/MethodParameter.md)
 - [MethodParameterConstraints](docs/MethodParameterConstraints.md)
 - [Methods](docs/Methods.md)
 - [Methods200Response](docs/Methods200Response.md)
 - [Methods200ResponseData](docs/Methods200ResponseData.md)
 - [MethodsCondition](docs/MethodsCondition.md)
 - [MethodsDeprecated](docs/MethodsDeprecated.md)
 - [ModifyAllowedNetworks200Response](docs/ModifyAllowedNetworks200Response.md)
 - [ModifyAllowedNetworks200ResponseData](docs/ModifyAllowedNetworks200ResponseData.md)
 - [ModifyAllowedNetworksRequest](docs/ModifyAllowedNetworksRequest.md)
 - [ModifyAllowedNetworksRequestAllowedNetworks](docs/ModifyAllowedNetworksRequestAllowedNetworks.md)
 - [ModifySetting200Response](docs/ModifySetting200Response.md)
 - [ModifySettingRequest](docs/ModifySettingRequest.md)
 - [NodeAddInner](docs/NodeAddInner.md)
 - [NodeAddInnerPropertiesInner](docs/NodeAddInnerPropertiesInner.md)
 - [NodeComplianceComponent](docs/NodeComplianceComponent.md)
 - [NodeComplianceComponentValuesInner](docs/NodeComplianceComponentValuesInner.md)
 - [NodeComplianceComponentValuesInnerReportsInner](docs/NodeComplianceComponentValuesInnerReportsInner.md)
 - [NodeDetails200Response](docs/NodeDetails200Response.md)
 - [NodeFull](docs/NodeFull.md)
 - [NodeFullBios](docs/NodeFullBios.md)
 - [NodeFullControllersInner](docs/NodeFullControllersInner.md)
 - [NodeFullEnvironmentVariablesInner](docs/NodeFullEnvironmentVariablesInner.md)
 - [NodeFullFileSystemsInner](docs/NodeFullFileSystemsInner.md)
 - [NodeFullMachine](docs/NodeFullMachine.md)
 - [NodeFullManagementTechnologyDetails](docs/NodeFullManagementTechnologyDetails.md)
 - [NodeFullManagementTechnologyInner](docs/NodeFullManagementTechnologyInner.md)
 - [NodeFullMemoriesInner](docs/NodeFullMemoriesInner.md)
 - [NodeFullNetworkInterfacesInner](docs/NodeFullNetworkInterfacesInner.md)
 - [NodeFullOs](docs/NodeFullOs.md)
 - [NodeFullPortsInner](docs/NodeFullPortsInner.md)
 - [NodeFullProcessesInner](docs/NodeFullProcessesInner.md)
 - [NodeFullProcessorsInner](docs/NodeFullProcessorsInner.md)
 - [NodeFullSlotsInner](docs/NodeFullSlotsInner.md)
 - [NodeFullSoftwareInner](docs/NodeFullSoftwareInner.md)
 - [NodeFullSoftwareInnerLicense](docs/NodeFullSoftwareInnerLicense.md)
 - [NodeFullSoftwareUpdateInner](docs/NodeFullSoftwareUpdateInner.md)
 - [NodeFullSoundInner](docs/NodeFullSoundInner.md)
 - [NodeFullStorageInner](docs/NodeFullStorageInner.md)
 - [NodeFullTimezone](docs/NodeFullTimezone.md)
 - [NodeFullVideosInner](docs/NodeFullVideosInner.md)
 - [NodeFullVirtualMachinesInner](docs/NodeFullVirtualMachinesInner.md)
 - [NodeInheritedProperties](docs/NodeInheritedProperties.md)
 - [NodeInheritedProperties200Response](docs/NodeInheritedProperties200Response.md)
 - [NodeInheritedPropertiesPropertiesInner](docs/NodeInheritedPropertiesPropertiesInner.md)
 - [NodeInheritedPropertiesPropertiesInnerHierarchyInner](docs/NodeInheritedPropertiesPropertiesInnerHierarchyInner.md)
 - [NodeSettings](docs/NodeSettings.md)
 - [Os](docs/Os.md)
 - [Parameter](docs/Parameter.md)
 - [ParameterDetails200Response](docs/ParameterDetails200Response.md)
 - [PromoteToRelay200Response](docs/PromoteToRelay200Response.md)
 - [PurgeSoftware200Response](docs/PurgeSoftware200Response.md)
 - [QueueInformation200Response](docs/QueueInformation200Response.md)
 - [QueueInformation200ResponseData](docs/QueueInformation200ResponseData.md)
 - [ReadCVEfromFS200Response](docs/ReadCVEfromFS200Response.md)
 - [RegeneratePolicies200Response](docs/RegeneratePolicies200Response.md)
 - [RegeneratePolicies200ResponseData](docs/RegeneratePolicies200ResponseData.md)
 - [ReloadAll200Response](docs/ReloadAll200Response.md)
 - [ReloadAll200ResponseData](docs/ReloadAll200ResponseData.md)
 - [ReloadAllDatasourcesAllNodes200Response](docs/ReloadAllDatasourcesAllNodes200Response.md)
 - [ReloadAllDatasourcesOneNode200Response](docs/ReloadAllDatasourcesOneNode200Response.md)
 - [ReloadGroup200Response](docs/ReloadGroup200Response.md)
 - [ReloadGroups200Response](docs/ReloadGroups200Response.md)
 - [ReloadGroups200ResponseData](docs/ReloadGroups200ResponseData.md)
 - [ReloadOneDatasourceAllNodes200Response](docs/ReloadOneDatasourceAllNodes200Response.md)
 - [ReloadOneDatasourceOneNode200Response](docs/ReloadOneDatasourceOneNode200Response.md)
 - [ReloadTechniques200Response](docs/ReloadTechniques200Response.md)
 - [ReloadTechniques200ResponseData](docs/ReloadTechniques200ResponseData.md)
 - [ReloadUserConf200Response](docs/ReloadUserConf200Response.md)
 - [ReloadUserConf200ResponseData](docs/ReloadUserConf200ResponseData.md)
 - [ReloadUserConf200ResponseDataReload](docs/ReloadUserConf200ResponseDataReload.md)
 - [RemoveValidatedUser200Response](docs/RemoveValidatedUser200Response.md)
 - [RestoreArchive200Response](docs/RestoreArchive200Response.md)
 - [RestoreArchive200ResponseData](docs/RestoreArchive200ResponseData.md)
 - [Rule](docs/Rule.md)
 - [RuleCategory](docs/RuleCategory.md)
 - [RuleCategoryUpdate](docs/RuleCategoryUpdate.md)
 - [RuleComplianceComponent](docs/RuleComplianceComponent.md)
 - [RuleComplianceComponentComplianceDetails](docs/RuleComplianceComponentComplianceDetails.md)
 - [RuleComplianceComponentComponentsInner](docs/RuleComplianceComponentComponentsInner.md)
 - [RuleComplianceComponentComponentsInnerValuesInner](docs/RuleComplianceComponentComponentsInnerValuesInner.md)
 - [RuleComplianceComponentComponentsInnerValuesInnerReportsInner](docs/RuleComplianceComponentComponentsInnerValuesInnerReportsInner.md)
 - [RuleDetails200Response](docs/RuleDetails200Response.md)
 - [RuleNew](docs/RuleNew.md)
 - [RuleTarget](docs/RuleTarget.md)
 - [RuleTargetsInner](docs/RuleTargetsInner.md)
 - [RuleTargetsInnerExclude](docs/RuleTargetsInnerExclude.md)
 - [RuleTargetsInnerInclude](docs/RuleTargetsInnerInclude.md)
 - [RuleWithCategory](docs/RuleWithCategory.md)
 - [SaveCampaign200Response](docs/SaveCampaign200Response.md)
 - [SaveCampaignEvent200Response](docs/SaveCampaignEvent200Response.md)
 - [SaveWorkflowUser200Response](docs/SaveWorkflowUser200Response.md)
 - [SaveWorkflowUserRequest](docs/SaveWorkflowUserRequest.md)
 - [ScheduleCampaign200Response](docs/ScheduleCampaign200Response.md)
 - [Secrets](docs/Secrets.md)
 - [SetAllowedNetworks200Response](docs/SetAllowedNetworks200Response.md)
 - [SetAllowedNetworks200ResponseData](docs/SetAllowedNetworks200ResponseData.md)
 - [SetAllowedNetworksRequest](docs/SetAllowedNetworksRequest.md)
 - [TechniqueBlock](docs/TechniqueBlock.md)
 - [TechniqueBlockReportingLogic](docs/TechniqueBlockReportingLogic.md)
 - [TechniqueCategories200Response](docs/TechniqueCategories200Response.md)
 - [TechniqueCategories200ResponseData](docs/TechniqueCategories200ResponseData.md)
 - [TechniqueCategory](docs/TechniqueCategory.md)
 - [TechniqueMethodCall](docs/TechniqueMethodCall.md)
 - [TechniqueMethodCallParametersInner](docs/TechniqueMethodCallParametersInner.md)
 - [TechniqueParameter](docs/TechniqueParameter.md)
 - [TechniqueResource](docs/TechniqueResource.md)
 - [TechniqueRevisions200Response](docs/TechniqueRevisions200Response.md)
 - [TechniqueRevisions200ResponseData](docs/TechniqueRevisions200ResponseData.md)
 - [TechniquesResourcesInner](docs/TechniquesResourcesInner.md)
 - [TechniquesRevisionsInner](docs/TechniquesRevisionsInner.md)
 - [TechniquesVersionsInner](docs/TechniquesVersionsInner.md)
 - [Timezone](docs/Timezone.md)
 - [UpdateBRandingConf200Response](docs/UpdateBRandingConf200Response.md)
 - [UpdateCVE200Response](docs/UpdateCVE200Response.md)
 - [UpdateCVE200ResponseData](docs/UpdateCVE200ResponseData.md)
 - [UpdateCVECheckConfiguration200Response](docs/UpdateCVECheckConfiguration200Response.md)
 - [UpdateCVECheckConfigurationRequest](docs/UpdateCVECheckConfigurationRequest.md)
 - [UpdateCVERequest](docs/UpdateCVERequest.md)
 - [UpdateChangeRequest200Response](docs/UpdateChangeRequest200Response.md)
 - [UpdateChangeRequestRequest](docs/UpdateChangeRequestRequest.md)
 - [UpdateDataSource200Response](docs/UpdateDataSource200Response.md)
 - [UpdateDirective200Response](docs/UpdateDirective200Response.md)
 - [UpdateGroup200Response](docs/UpdateGroup200Response.md)
 - [UpdateGroupCategory200Response](docs/UpdateGroupCategory200Response.md)
 - [UpdateNode200Response](docs/UpdateNode200Response.md)
 - [UpdateParameter200Response](docs/UpdateParameter200Response.md)
 - [UpdatePolicies200Response](docs/UpdatePolicies200Response.md)
 - [UpdateRule200Response](docs/UpdateRule200Response.md)
 - [UpdateRule200ResponseData](docs/UpdateRule200ResponseData.md)
 - [UpdateRuleCategory200Response](docs/UpdateRuleCategory200Response.md)
 - [UpdateSecret200Response](docs/UpdateSecret200Response.md)
 - [UpdateUser200Response](docs/UpdateUser200Response.md)
 - [UpdateUser200ResponseData](docs/UpdateUser200ResponseData.md)
 - [UpdateUser200ResponseDataUpdatedUser](docs/UpdateUser200ResponseDataUpdatedUser.md)
 - [UploadInventory200Response](docs/UploadInventory200Response.md)
 - [Users](docs/Users.md)
 - [ValidatedUser](docs/ValidatedUser.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="API-Tokens"></a>
### API-Tokens

- **Type**: API key
- **API key parameter name**: X-API-Token
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

dev@rudder.io

