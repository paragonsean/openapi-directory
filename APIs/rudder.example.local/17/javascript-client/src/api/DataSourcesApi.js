/**
 * Rudder API
 * Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like `/api/version/function`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) => 404 not found curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules ```  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules # Wrong => Error response indicating which versions are available curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules ```  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   <h4>Existing versions</h4> <table>   <thead>     <tr>       <th style=\"width: 20%\">Version</th>       <th style=\"width: 20%\">Rudder versions it appeared in</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">1</td>       <td class=\"code\">Never released (for internal use only)</td>       <td>Experimental version</td>     </tr>     <tr>       <td class=\"code\">2 to 10 (deprecated)</td>       <td class=\"code\">4.3 and before</td>       <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>     </tr>     <tr>       <td class=\"code\">11</td>       <td class=\"code\">5.0</td>       <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>     </tr>     <tr>       <td class=\"code\">12</td>       <td class=\"code\">6.0 and 6.1</td>       <td>Node key management</td>     </tr>     <tr>       <td class=\"code\">13</td>       <td class=\"code\">6.2</td>       <td><ul>         <li>Node status endpoint</li>         <li>System health check</li>         <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">14</td>       <td class=\"code\">7.0</td>       <td><ul>         <li>Secret management</li>         <li>Directive tree</li>         <li>Improve techniques management</li>         <li>Demote a relay</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">15</td>       <td class=\"code\">7.1</td>       <td><ul>         <li>Package updates in nodes</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">16</td>       <td class=\"code\">7.2</td>       <td><ul>         <li>Create node API included from plugin</li>         <li>Configuration archive import/export</li>       </ul></td>     </tr>   </tbody> </table>   ## Response format  All responses from the API are in the JSON format.  ```json {   \"action\": \"The name of the called function\",   \"id\": \"The ID of the element you want, if relevant\",   \"result\": \"The result of your action: success or error\",   \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",   \"errorDetails\": \"Only present if this is an error, it contains the error message\" } ```   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can't be submitted in a JSON form.  #### Available for all requests  <table>   <thead>     <tr>       <th style=\"width: 30%\">Field</th>       <th style=\"width: 10%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">prettify</td>       <td><b>boolean</b><br><i>optional</i></td>       <td>         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         <p class=\"default-value\">Default value: <code>false</code></p>       </td>     </tr>   </tbody> </table>   #### Available for modification requests (PUT/POST/DELETE)  <table>   <thead>     <tr>       <th style=\"width: 25%\">Field</th>       <th style=\"width: 12%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">reason</td>       <td><b>string</b><br><i>optional</i> or <i>required</i></td>       <td>         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestName</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         <p class=\"default-value\">Default value: <code>A default string for each function</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestDescription</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request description, is used only if workflows are enabled.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>   </tbody> </table>   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  ```bash # Get the Rule of ID \"id\" curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id ```    CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a `curl` `POST` request, that header can be provided with the `-H` parameter:  ```bash curl -X POST -H \"Content-Type: application/json\" ... ```  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.  The (human readable) format is:  ```json {   \"key1\": \"value1\",   \"key2\": false,   \"key3\": 42 } ```   Here is an example with inlined data:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id}   -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}' ```  You can also pass a supply the JSON in a file:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam ```  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\" curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\" ```  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  ``` key=value ```  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\" ```  * As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json ``` 
 *
 * The version of the OpenAPI document: 17
 * Contact: dev@rudder.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreateDataSource200Response from '../model/CreateDataSource200Response';
import Datasource from '../model/Datasource';
import DeleteDataSource200Response from '../model/DeleteDataSource200Response';
import GetAllDataSources200Response from '../model/GetAllDataSources200Response';
import GetDataSource200Response from '../model/GetDataSource200Response';
import ReloadAllDatasourcesAllNodes200Response from '../model/ReloadAllDatasourcesAllNodes200Response';
import ReloadAllDatasourcesOneNode200Response from '../model/ReloadAllDatasourcesOneNode200Response';
import ReloadOneDatasourceAllNodes200Response from '../model/ReloadOneDatasourceAllNodes200Response';
import ReloadOneDatasourceOneNode200Response from '../model/ReloadOneDatasourceOneNode200Response';
import UpdateDataSource200Response from '../model/UpdateDataSource200Response';

/**
* DataSources service.
* @module api/DataSourcesApi
* @version 17
*/
export default class DataSourcesApi {

    /**
    * Constructs a new DataSourcesApi. 
    * @alias module:api/DataSourcesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createDataSource operation.
     * @callback module:api/DataSourcesApi~createDataSourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateDataSource200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a data source
     * Create a new data source
     * @param {Object} opts Optional parameters
     * @param {module:model/Datasource} [datasource] 
     * @param {module:api/DataSourcesApi~createDataSourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateDataSource200Response}
     */
    createDataSource(opts, callback) {
      opts = opts || {};
      let postBody = opts['datasource'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateDataSource200Response;
      return this.apiClient.callApi(
        '/datasources', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDataSource operation.
     * @callback module:api/DataSourcesApi~deleteDataSourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteDataSource200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a data source
     * Delete a data source configuration
     * @param {String} datasourceId Id of the data source
     * @param {module:api/DataSourcesApi~deleteDataSourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteDataSource200Response}
     */
    deleteDataSource(datasourceId, callback) {
      let postBody = null;
      // verify the required parameter 'datasourceId' is set
      if (datasourceId === undefined || datasourceId === null) {
        throw new Error("Missing the required parameter 'datasourceId' when calling deleteDataSource");
      }

      let pathParams = {
        'datasourceId': datasourceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteDataSource200Response;
      return this.apiClient.callApi(
        '/datasources/{datasourceId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllDataSources operation.
     * @callback module:api/DataSourcesApi~getAllDataSourcesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAllDataSources200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all data sources
     * Get the configuration of all present data sources
     * @param {module:api/DataSourcesApi~getAllDataSourcesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAllDataSources200Response}
     */
    getAllDataSources(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetAllDataSources200Response;
      return this.apiClient.callApi(
        '/datasources', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDataSource operation.
     * @callback module:api/DataSourcesApi~getDataSourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDataSource200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get data source configuration
     * Get the configuration of a data source
     * @param {String} datasourceId Id of the data source
     * @param {module:api/DataSourcesApi~getDataSourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDataSource200Response}
     */
    getDataSource(datasourceId, callback) {
      let postBody = null;
      // verify the required parameter 'datasourceId' is set
      if (datasourceId === undefined || datasourceId === null) {
        throw new Error("Missing the required parameter 'datasourceId' when calling getDataSource");
      }

      let pathParams = {
        'datasourceId': datasourceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDataSource200Response;
      return this.apiClient.callApi(
        '/datasources/{datasourceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reloadAllDatasourcesAllNodes operation.
     * @callback module:api/DataSourcesApi~reloadAllDatasourcesAllNodesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReloadAllDatasourcesAllNodes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update properties from data sources
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @param {module:api/DataSourcesApi~reloadAllDatasourcesAllNodesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReloadAllDatasourcesAllNodes200Response}
     */
    reloadAllDatasourcesAllNodes(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ReloadAllDatasourcesAllNodes200Response;
      return this.apiClient.callApi(
        '/datasources/reload', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reloadAllDatasourcesOneNode operation.
     * @callback module:api/DataSourcesApi~reloadAllDatasourcesOneNodeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReloadAllDatasourcesOneNode200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update properties for one node from all data sources
     * Update properties from all data sources on one nodes. The call is asynchronous.
     * @param {String} nodeId Id of the target node
     * @param {module:api/DataSourcesApi~reloadAllDatasourcesOneNodeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReloadAllDatasourcesOneNode200Response}
     */
    reloadAllDatasourcesOneNode(nodeId, callback) {
      let postBody = null;
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling reloadAllDatasourcesOneNode");
      }

      let pathParams = {
        'nodeId': nodeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ReloadAllDatasourcesOneNode200Response;
      return this.apiClient.callApi(
        '/nodes/{nodeId}/fetchData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reloadOneDatasourceAllNodes operation.
     * @callback module:api/DataSourcesApi~reloadOneDatasourceAllNodesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReloadOneDatasourceAllNodes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update properties from data sources
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @param {String} datasourceId Id of the data source
     * @param {module:api/DataSourcesApi~reloadOneDatasourceAllNodesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReloadOneDatasourceAllNodes200Response}
     */
    reloadOneDatasourceAllNodes(datasourceId, callback) {
      let postBody = null;
      // verify the required parameter 'datasourceId' is set
      if (datasourceId === undefined || datasourceId === null) {
        throw new Error("Missing the required parameter 'datasourceId' when calling reloadOneDatasourceAllNodes");
      }

      let pathParams = {
        'datasourceId': datasourceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ReloadOneDatasourceAllNodes200Response;
      return this.apiClient.callApi(
        '/datasources/reload/{datasourceId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reloadOneDatasourceOneNode operation.
     * @callback module:api/DataSourcesApi~reloadOneDatasourceOneNodeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReloadOneDatasourceOneNode200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update properties for one node from a data source
     * Update properties from a data source on one nodes. The call is asynchronous.
     * @param {String} nodeId Id of the target node
     * @param {String} datasourceId Id of the data source
     * @param {module:api/DataSourcesApi~reloadOneDatasourceOneNodeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReloadOneDatasourceOneNode200Response}
     */
    reloadOneDatasourceOneNode(nodeId, datasourceId, callback) {
      let postBody = null;
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling reloadOneDatasourceOneNode");
      }
      // verify the required parameter 'datasourceId' is set
      if (datasourceId === undefined || datasourceId === null) {
        throw new Error("Missing the required parameter 'datasourceId' when calling reloadOneDatasourceOneNode");
      }

      let pathParams = {
        'nodeId': nodeId,
        'datasourceId': datasourceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ReloadOneDatasourceOneNode200Response;
      return this.apiClient.callApi(
        '/nodes/{nodeId}/fetchData/{datasourceId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateDataSource operation.
     * @callback module:api/DataSourcesApi~updateDataSourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateDataSource200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a data source configuration
     * Update the configuration of a data source
     * @param {String} datasourceId Id of the data source
     * @param {Object} opts Optional parameters
     * @param {module:model/Datasource} [datasource] 
     * @param {module:api/DataSourcesApi~updateDataSourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateDataSource200Response}
     */
    updateDataSource(datasourceId, opts, callback) {
      opts = opts || {};
      let postBody = opts['datasource'];
      // verify the required parameter 'datasourceId' is set
      if (datasourceId === undefined || datasourceId === null) {
        throw new Error("Missing the required parameter 'datasourceId' when calling updateDataSource");
      }

      let pathParams = {
        'datasourceId': datasourceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateDataSource200Response;
      return this.apiClient.callApi(
        '/datasources/{datasourceId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
