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
import AcceptChangeRequest200Response from '../model/AcceptChangeRequest200Response';
import AcceptChangeRequestRequest from '../model/AcceptChangeRequestRequest';
import ChangeRequestDetails200Response from '../model/ChangeRequestDetails200Response';
import DeclineChangeRequest200Response from '../model/DeclineChangeRequest200Response';
import ListChangeRequests200Response from '../model/ListChangeRequests200Response';
import ListUsers200Response from '../model/ListUsers200Response';
import RemoveValidatedUser200Response from '../model/RemoveValidatedUser200Response';
import SaveWorkflowUser200Response from '../model/SaveWorkflowUser200Response';
import SaveWorkflowUserRequest from '../model/SaveWorkflowUserRequest';
import UpdateChangeRequest200Response from '../model/UpdateChangeRequest200Response';
import UpdateChangeRequestRequest from '../model/UpdateChangeRequestRequest';

/**
* ChangeRequests service.
* @module api/ChangeRequestsApi
* @version 17
*/
export default class ChangeRequestsApi {

    /**
    * Constructs a new ChangeRequestsApi. 
    * @alias module:api/ChangeRequestsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the acceptChangeRequest operation.
     * @callback module:api/ChangeRequestsApi~acceptChangeRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AcceptChangeRequest200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Accept a request details
     * Accept a change request
     * @param {Number} changeRequestId 
     * @param {module:model/AcceptChangeRequestRequest} acceptChangeRequestRequest 
     * @param {module:api/ChangeRequestsApi~acceptChangeRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AcceptChangeRequest200Response}
     */
    acceptChangeRequest(changeRequestId, acceptChangeRequestRequest, callback) {
      let postBody = acceptChangeRequestRequest;
      // verify the required parameter 'changeRequestId' is set
      if (changeRequestId === undefined || changeRequestId === null) {
        throw new Error("Missing the required parameter 'changeRequestId' when calling acceptChangeRequest");
      }
      // verify the required parameter 'acceptChangeRequestRequest' is set
      if (acceptChangeRequestRequest === undefined || acceptChangeRequestRequest === null) {
        throw new Error("Missing the required parameter 'acceptChangeRequestRequest' when calling acceptChangeRequest");
      }

      let pathParams = {
        'changeRequestId': changeRequestId
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
      let returnType = AcceptChangeRequest200Response;
      return this.apiClient.callApi(
        '/changeRequests/{changeRequestId}/accept', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changeRequestDetails operation.
     * @callback module:api/ChangeRequestsApi~changeRequestDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ChangeRequestDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a change request details
     * Get a change request details
     * @param {Number} changeRequestId 
     * @param {module:api/ChangeRequestsApi~changeRequestDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ChangeRequestDetails200Response}
     */
    changeRequestDetails(changeRequestId, callback) {
      let postBody = null;
      // verify the required parameter 'changeRequestId' is set
      if (changeRequestId === undefined || changeRequestId === null) {
        throw new Error("Missing the required parameter 'changeRequestId' when calling changeRequestDetails");
      }

      let pathParams = {
        'changeRequestId': changeRequestId
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
      let returnType = ChangeRequestDetails200Response;
      return this.apiClient.callApi(
        '/changeRequests/{changeRequestId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the declineChangeRequest operation.
     * @callback module:api/ChangeRequestsApi~declineChangeRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeclineChangeRequest200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Decline a request details
     * Refuse a change request
     * @param {Number} changeRequestId 
     * @param {module:api/ChangeRequestsApi~declineChangeRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeclineChangeRequest200Response}
     */
    declineChangeRequest(changeRequestId, callback) {
      let postBody = null;
      // verify the required parameter 'changeRequestId' is set
      if (changeRequestId === undefined || changeRequestId === null) {
        throw new Error("Missing the required parameter 'changeRequestId' when calling declineChangeRequest");
      }

      let pathParams = {
        'changeRequestId': changeRequestId
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
      let returnType = DeclineChangeRequest200Response;
      return this.apiClient.callApi(
        '/changeRequests/{changeRequestId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listChangeRequests operation.
     * @callback module:api/ChangeRequestsApi~listChangeRequestsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListChangeRequests200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all change requests
     * List all change requests
     * @param {module:api/ChangeRequestsApi~listChangeRequestsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListChangeRequests200Response}
     */
    listChangeRequests(callback) {
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
      let returnType = ListChangeRequests200Response;
      return this.apiClient.callApi(
        '/api/changeRequests', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listUsers operation.
     * @callback module:api/ChangeRequestsApi~listUsersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListUsers200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List user
     * List all validated and unvalidated users
     * @param {module:api/ChangeRequestsApi~listUsersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListUsers200Response}
     */
    listUsers(callback) {
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
      let returnType = ListUsers200Response;
      return this.apiClient.callApi(
        '/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeValidatedUser operation.
     * @callback module:api/ChangeRequestsApi~removeValidatedUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RemoveValidatedUser200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove an user from validated user list
     * The user is again subject to workflow validation
     * @param {String} username Username of an user (unique)
     * @param {module:api/ChangeRequestsApi~removeValidatedUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RemoveValidatedUser200Response}
     */
    removeValidatedUser(username, callback) {
      let postBody = null;
      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling removeValidatedUser");
      }

      let pathParams = {
        'username': username
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
      let returnType = RemoveValidatedUser200Response;
      return this.apiClient.callApi(
        '/validatedUsers/{username}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the saveWorkflowUser operation.
     * @callback module:api/ChangeRequestsApi~saveWorkflowUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SaveWorkflowUser200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update validated user list
     * Add and remove user from validated users
     * @param {module:model/SaveWorkflowUserRequest} saveWorkflowUserRequest 
     * @param {module:api/ChangeRequestsApi~saveWorkflowUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SaveWorkflowUser200Response}
     */
    saveWorkflowUser(saveWorkflowUserRequest, callback) {
      let postBody = saveWorkflowUserRequest;
      // verify the required parameter 'saveWorkflowUserRequest' is set
      if (saveWorkflowUserRequest === undefined || saveWorkflowUserRequest === null) {
        throw new Error("Missing the required parameter 'saveWorkflowUserRequest' when calling saveWorkflowUser");
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
      let returnType = SaveWorkflowUser200Response;
      return this.apiClient.callApi(
        '/validatedUsers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateChangeRequest operation.
     * @callback module:api/ChangeRequestsApi~updateChangeRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateChangeRequest200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a request details
     * Update a change request
     * @param {Number} changeRequestId 
     * @param {module:model/UpdateChangeRequestRequest} updateChangeRequestRequest 
     * @param {module:api/ChangeRequestsApi~updateChangeRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateChangeRequest200Response}
     */
    updateChangeRequest(changeRequestId, updateChangeRequestRequest, callback) {
      let postBody = updateChangeRequestRequest;
      // verify the required parameter 'changeRequestId' is set
      if (changeRequestId === undefined || changeRequestId === null) {
        throw new Error("Missing the required parameter 'changeRequestId' when calling updateChangeRequest");
      }
      // verify the required parameter 'updateChangeRequestRequest' is set
      if (updateChangeRequestRequest === undefined || updateChangeRequestRequest === null) {
        throw new Error("Missing the required parameter 'updateChangeRequestRequest' when calling updateChangeRequest");
      }

      let pathParams = {
        'changeRequestId': changeRequestId
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
      let returnType = UpdateChangeRequest200Response;
      return this.apiClient.callApi(
        '/changeRequests/{changeRequestId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
