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
import ApplyPolicyAllNodes200Response from '../model/ApplyPolicyAllNodes200Response';
import ChangePendingNodeStatus200Response from '../model/ChangePendingNodeStatus200Response';
import ChangePendingNodeStatusRequest from '../model/ChangePendingNodeStatusRequest';
import CreateNodes200Response from '../model/CreateNodes200Response';
import DeleteNode200Response from '../model/DeleteNode200Response';
import GetNodesStatus200Response from '../model/GetNodesStatus200Response';
import ListAcceptedNodes200Response from '../model/ListAcceptedNodes200Response';
import ListPendingNodes200Response from '../model/ListPendingNodes200Response';
import NodeAddInner from '../model/NodeAddInner';
import NodeDetails200Response from '../model/NodeDetails200Response';
import NodeInheritedProperties200Response from '../model/NodeInheritedProperties200Response';
import NodeSettings from '../model/NodeSettings';
import UpdateNode200Response from '../model/UpdateNode200Response';

/**
* Nodes service.
* @module api/NodesApi
* @version 17
*/
export default class NodesApi {

    /**
    * Constructs a new NodesApi. 
    * @alias module:api/NodesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the applyPolicy operation.
     * @callback module:api/NodesApi~applyPolicyCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trigger an agent run
     * This API allows to trigger an agent run on the target node. Response is a stream of the actual agent run on the node.
     * @param {String} nodeId Id of the target node
     * @param {module:api/NodesApi~applyPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    applyPolicy(nodeId, callback) {
      let postBody = null;
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling applyPolicy");
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
      let accepts = ['text/plain'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/nodes/{nodeId}/applyPolicy', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the applyPolicyAllNodes operation.
     * @callback module:api/NodesApi~applyPolicyAllNodesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApplyPolicyAllNodes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trigger an agent run on all nodes
     * This API allows to trigger an agent run on all nodes. Response contains a json stating if agent could be started on each node, but not if the run went fine and do not display any output from it. You can see the result of the run in Rudder web interface or in the each agent logs.
     * @param {module:api/NodesApi~applyPolicyAllNodesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApplyPolicyAllNodes200Response}
     */
    applyPolicyAllNodes(callback) {
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
      let returnType = ApplyPolicyAllNodes200Response;
      return this.apiClient.callApi(
        '/nodes/applyPolicy', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changePendingNodeStatus operation.
     * @callback module:api/NodesApi~changePendingNodeStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ChangePendingNodeStatus200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update pending Node status
     * Accept or refuse a pending node
     * @param {String} nodeId Id of the target node
     * @param {Object} opts Optional parameters
     * @param {module:model/ChangePendingNodeStatusRequest} [changePendingNodeStatusRequest] 
     * @param {module:api/NodesApi~changePendingNodeStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ChangePendingNodeStatus200Response}
     */
    changePendingNodeStatus(nodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['changePendingNodeStatusRequest'];
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling changePendingNodeStatus");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ChangePendingNodeStatus200Response;
      return this.apiClient.callApi(
        '/nodes/pending/{nodeId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createNodes operation.
     * @callback module:api/NodesApi~createNodesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateNodes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create one or several new nodes
     * Use the provided array of node information to create new nodes
     * @param {Array.<module:model/NodeAddInner>} nodeAddInner 
     * @param {module:api/NodesApi~createNodesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateNodes200Response}
     */
    createNodes(nodeAddInner, callback) {
      let postBody = nodeAddInner;
      // verify the required parameter 'nodeAddInner' is set
      if (nodeAddInner === undefined || nodeAddInner === null) {
        throw new Error("Missing the required parameter 'nodeAddInner' when calling createNodes");
      }

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
      let returnType = CreateNodes200Response;
      return this.apiClient.callApi(
        '/nodes', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNode operation.
     * @callback module:api/NodesApi~deleteNodeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteNode200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a node
     * Remove a node from the Rudder server. It won't be managed anymore.
     * @param {String} nodeId Id of the target node
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [mode = 'move')] Deletion mode to use, either move to trash ('move', default) or erase ('erase')
     * @param {module:api/NodesApi~deleteNodeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteNode200Response}
     */
    deleteNode(nodeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling deleteNode");
      }

      let pathParams = {
        'nodeId': nodeId
      };
      let queryParams = {
        'mode': opts['mode']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteNode200Response;
      return this.apiClient.callApi(
        '/nodes/{nodeId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNodesStatus operation.
     * @callback module:api/NodesApi~getNodesStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNodesStatus200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get nodes acceptation status
     * Get acceptation status (pending, accepted, deleted, unknown) of a list of nodes
     * @param {String} ids Comma separated list of node Ids
     * @param {module:api/NodesApi~getNodesStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNodesStatus200Response}
     */
    getNodesStatus(ids, callback) {
      let postBody = null;
      // verify the required parameter 'ids' is set
      if (ids === undefined || ids === null) {
        throw new Error("Missing the required parameter 'ids' when calling getNodesStatus");
      }

      let pathParams = {
      };
      let queryParams = {
        'ids': ids
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetNodesStatus200Response;
      return this.apiClient.callApi(
        '/nodes/status', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listAcceptedNodes operation.
     * @callback module:api/NodesApi~listAcceptedNodesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListAcceptedNodes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List managed nodes
     * Get information about the nodes managed by the target server
     * @param {Object} opts Optional parameters
     * @param {String} [include = 'default')] Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
     * @param {Object} [query] The criterion you want to find for your nodes. Replaces the `where`, `composition` and `select` parameters in a single parameter.
     * @param {Array.<Object>} [where] The criterion you want to find for your nodes
     * @param {module:model/String} [composition = 'and')] Boolean operator to use between each  `where` criteria.
     * @param {String} [select = 'node')] What kind of data we want to include. Here we can get policy servers/relay by setting `nodeAndPolicyServer`. Only used if `where` is defined.
     * @param {module:api/NodesApi~listAcceptedNodesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListAcceptedNodes200Response}
     */
    listAcceptedNodes(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'include': opts['include'],
        'query': opts['query'],
        'where': this.apiClient.buildCollectionParam(opts['where'], 'csv'),
        'composition': opts['composition'],
        'select': opts['select']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListAcceptedNodes200Response;
      return this.apiClient.callApi(
        '/nodes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPendingNodes operation.
     * @callback module:api/NodesApi~listPendingNodesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPendingNodes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List pending nodes
     * Get information about the nodes pending acceptation
     * @param {Object} opts Optional parameters
     * @param {String} [include = 'default')] Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
     * @param {Object} [query] The criterion you want to find for your nodes. Replaces the `where`, `composition` and `select` parameters in a single parameter.
     * @param {Array.<Object>} [where] The criterion you want to find for your nodes
     * @param {module:model/String} [composition = 'and')] Boolean operator to use between each  `where` criteria.
     * @param {String} [select = 'node')] What kind of data we want to include. Here we can get policy servers/relay by setting `nodeAndPolicyServer`. Only used if `where` is defined.
     * @param {module:api/NodesApi~listPendingNodesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPendingNodes200Response}
     */
    listPendingNodes(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'include': opts['include'],
        'query': opts['query'],
        'where': this.apiClient.buildCollectionParam(opts['where'], 'csv'),
        'composition': opts['composition'],
        'select': opts['select']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListPendingNodes200Response;
      return this.apiClient.callApi(
        '/nodes/pending', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the nodeDetails operation.
     * @callback module:api/NodesApi~nodeDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NodeDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get information about a node
     * Get details about a given node
     * @param {String} nodeId Id of the target node
     * @param {Object} opts Optional parameters
     * @param {String} [include = 'default')] Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
     * @param {module:api/NodesApi~nodeDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NodeDetails200Response}
     */
    nodeDetails(nodeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling nodeDetails");
      }

      let pathParams = {
        'nodeId': nodeId
      };
      let queryParams = {
        'include': opts['include']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = NodeDetails200Response;
      return this.apiClient.callApi(
        '/nodes/{nodeId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the nodeInheritedProperties operation.
     * @callback module:api/NodesApi~nodeInheritedPropertiesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NodeInheritedProperties200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get inherited node properties for a node
     * This API returns all node properties for a node, including group inherited ones.
     * @param {String} nodeId Id of the target node
     * @param {module:api/NodesApi~nodeInheritedPropertiesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NodeInheritedProperties200Response}
     */
    nodeInheritedProperties(nodeId, callback) {
      let postBody = null;
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling nodeInheritedProperties");
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
      let returnType = NodeInheritedProperties200Response;
      return this.apiClient.callApi(
        '/nodes/{nodeId}/inheritedProperties', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNode operation.
     * @callback module:api/NodesApi~updateNodeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateNode200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update node settings and properties
     * Update node settings and properties
     * @param {String} nodeId Id of the target node
     * @param {Object} opts Optional parameters
     * @param {module:model/NodeSettings} [nodeSettings] 
     * @param {module:api/NodesApi~updateNodeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateNode200Response}
     */
    updateNode(nodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['nodeSettings'];
      // verify the required parameter 'nodeId' is set
      if (nodeId === undefined || nodeId === null) {
        throw new Error("Missing the required parameter 'nodeId' when calling updateNode");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateNode200Response;
      return this.apiClient.callApi(
        '/nodes/{nodeId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
