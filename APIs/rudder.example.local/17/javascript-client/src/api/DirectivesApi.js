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
import CheckDirective200Response from '../model/CheckDirective200Response';
import CreateDirective200Response from '../model/CreateDirective200Response';
import DeleteDirective200Response from '../model/DeleteDirective200Response';
import Directive from '../model/Directive';
import DirectiveDetails200Response from '../model/DirectiveDetails200Response';
import DirectiveNew from '../model/DirectiveNew';
import ListDirectives200Response from '../model/ListDirectives200Response';
import UpdateDirective200Response from '../model/UpdateDirective200Response';

/**
* Directives service.
* @module api/DirectivesApi
* @version 17
*/
export default class DirectivesApi {

    /**
    * Constructs a new DirectivesApi. 
    * @alias module:api/DirectivesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the checkDirective operation.
     * @callback module:api/DirectivesApi~checkDirectiveCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CheckDirective200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Check that update on a directive is valid
     * Check that update on a directive is valid
     * @param {String} directiveId Id of the directive
     * @param {module:model/Directive} directive 
     * @param {module:api/DirectivesApi~checkDirectiveCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CheckDirective200Response}
     */
    checkDirective(directiveId, directive, callback) {
      let postBody = directive;
      // verify the required parameter 'directiveId' is set
      if (directiveId === undefined || directiveId === null) {
        throw new Error("Missing the required parameter 'directiveId' when calling checkDirective");
      }
      // verify the required parameter 'directive' is set
      if (directive === undefined || directive === null) {
        throw new Error("Missing the required parameter 'directive' when calling checkDirective");
      }

      let pathParams = {
        'directiveId': directiveId
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
      let returnType = CheckDirective200Response;
      return this.apiClient.callApi(
        '/directives/{directiveId}/check', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createDirective operation.
     * @callback module:api/DirectivesApi~createDirectiveCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateDirective200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a directive
     * Create a new directive from provided parameters. You can specify a source directive to clone it.
     * @param {Object} opts Optional parameters
     * @param {module:model/DirectiveNew} [directiveNew] 
     * @param {module:api/DirectivesApi~createDirectiveCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateDirective200Response}
     */
    createDirective(opts, callback) {
      opts = opts || {};
      let postBody = opts['directiveNew'];

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
      let returnType = CreateDirective200Response;
      return this.apiClient.callApi(
        '/directives', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDirective operation.
     * @callback module:api/DirectivesApi~deleteDirectiveCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteDirective200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a directive
     * Delete a directive
     * @param {String} directiveId Id of the directive
     * @param {module:api/DirectivesApi~deleteDirectiveCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteDirective200Response}
     */
    deleteDirective(directiveId, callback) {
      let postBody = null;
      // verify the required parameter 'directiveId' is set
      if (directiveId === undefined || directiveId === null) {
        throw new Error("Missing the required parameter 'directiveId' when calling deleteDirective");
      }

      let pathParams = {
        'directiveId': directiveId
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
      let returnType = DeleteDirective200Response;
      return this.apiClient.callApi(
        '/directives/{directiveId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the directiveDetails operation.
     * @callback module:api/DirectivesApi~directiveDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DirectiveDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get directive details
     * Get all information about a given directive
     * @param {String} directiveId Id of the directive
     * @param {module:api/DirectivesApi~directiveDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DirectiveDetails200Response}
     */
    directiveDetails(directiveId, callback) {
      let postBody = null;
      // verify the required parameter 'directiveId' is set
      if (directiveId === undefined || directiveId === null) {
        throw new Error("Missing the required parameter 'directiveId' when calling directiveDetails");
      }

      let pathParams = {
        'directiveId': directiveId
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
      let returnType = DirectiveDetails200Response;
      return this.apiClient.callApi(
        '/directives/{directiveId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listDirectives operation.
     * @callback module:api/DirectivesApi~listDirectivesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListDirectives200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all directives
     * List all directives
     * @param {module:api/DirectivesApi~listDirectivesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListDirectives200Response}
     */
    listDirectives(callback) {
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
      let returnType = ListDirectives200Response;
      return this.apiClient.callApi(
        '/directives', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateDirective operation.
     * @callback module:api/DirectivesApi~updateDirectiveCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateDirective200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a directive details
     * Update directive information
     * @param {String} directiveId Id of the directive
     * @param {module:model/Directive} directive 
     * @param {module:api/DirectivesApi~updateDirectiveCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateDirective200Response}
     */
    updateDirective(directiveId, directive, callback) {
      let postBody = directive;
      // verify the required parameter 'directiveId' is set
      if (directiveId === undefined || directiveId === null) {
        throw new Error("Missing the required parameter 'directiveId' when calling updateDirective");
      }
      // verify the required parameter 'directive' is set
      if (directive === undefined || directive === null) {
        throw new Error("Missing the required parameter 'directive' when calling updateDirective");
      }

      let pathParams = {
        'directiveId': directiveId
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
      let returnType = UpdateDirective200Response;
      return this.apiClient.callApi(
        '/directives/{directiveId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
