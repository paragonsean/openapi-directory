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
import CreateRule200Response from '../model/CreateRule200Response';
import CreateRuleCategory200Response from '../model/CreateRuleCategory200Response';
import DeleteRule200Response from '../model/DeleteRule200Response';
import DeleteRuleCategory200Response from '../model/DeleteRuleCategory200Response';
import GetRuleCategoryDetails200Response from '../model/GetRuleCategoryDetails200Response';
import GetRuleTree200Response from '../model/GetRuleTree200Response';
import ListRules200Response from '../model/ListRules200Response';
import RuleCategory from '../model/RuleCategory';
import RuleCategoryUpdate from '../model/RuleCategoryUpdate';
import RuleDetails200Response from '../model/RuleDetails200Response';
import RuleNew from '../model/RuleNew';
import RuleWithCategory from '../model/RuleWithCategory';
import UpdateRule200Response from '../model/UpdateRule200Response';
import UpdateRuleCategory200Response from '../model/UpdateRuleCategory200Response';

/**
* Rules service.
* @module api/RulesApi
* @version 17
*/
export default class RulesApi {

    /**
    * Constructs a new RulesApi. 
    * @alias module:api/RulesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createRule operation.
     * @callback module:api/RulesApi~createRuleCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRule200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a rule
     * Create a new rule. You can specify a source rule to clone it.
     * @param {Object} opts Optional parameters
     * @param {module:model/RuleNew} [ruleNew] 
     * @param {module:api/RulesApi~createRuleCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRule200Response}
     */
    createRule(opts, callback) {
      opts = opts || {};
      let postBody = opts['ruleNew'];

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
      let returnType = CreateRule200Response;
      return this.apiClient.callApi(
        '/rules', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createRuleCategory operation.
     * @callback module:api/RulesApi~createRuleCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRuleCategory200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a rule category
     * Create a new rule category
     * @param {module:model/RuleCategory} ruleCategory 
     * @param {module:api/RulesApi~createRuleCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRuleCategory200Response}
     */
    createRuleCategory(ruleCategory, callback) {
      let postBody = ruleCategory;
      // verify the required parameter 'ruleCategory' is set
      if (ruleCategory === undefined || ruleCategory === null) {
        throw new Error("Missing the required parameter 'ruleCategory' when calling createRuleCategory");
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
      let returnType = CreateRuleCategory200Response;
      return this.apiClient.callApi(
        '/rules/categories', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRule operation.
     * @callback module:api/RulesApi~deleteRuleCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteRule200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a rule
     * Delete a rule.
     * @param {String} ruleId Id of the target rule
     * @param {module:api/RulesApi~deleteRuleCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteRule200Response}
     */
    deleteRule(ruleId, callback) {
      let postBody = null;
      // verify the required parameter 'ruleId' is set
      if (ruleId === undefined || ruleId === null) {
        throw new Error("Missing the required parameter 'ruleId' when calling deleteRule");
      }

      let pathParams = {
        'ruleId': ruleId
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
      let returnType = DeleteRule200Response;
      return this.apiClient.callApi(
        '/rules/{ruleId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRuleCategory operation.
     * @callback module:api/RulesApi~deleteRuleCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteRuleCategory200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete group category
     * Delete a group category. It must have no child groups and no children categories.
     * @param {String} ruleCategoryId 
     * @param {module:api/RulesApi~deleteRuleCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteRuleCategory200Response}
     */
    deleteRuleCategory(ruleCategoryId, callback) {
      let postBody = null;
      // verify the required parameter 'ruleCategoryId' is set
      if (ruleCategoryId === undefined || ruleCategoryId === null) {
        throw new Error("Missing the required parameter 'ruleCategoryId' when calling deleteRuleCategory");
      }

      let pathParams = {
        'ruleCategoryId': ruleCategoryId
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
      let returnType = DeleteRuleCategory200Response;
      return this.apiClient.callApi(
        '/rules/categories/{ruleCategoryId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRuleCategoryDetails operation.
     * @callback module:api/RulesApi~getRuleCategoryDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRuleCategoryDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get rule category details
     * Get detailed information about a rule category
     * @param {String} ruleCategoryId 
     * @param {module:api/RulesApi~getRuleCategoryDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRuleCategoryDetails200Response}
     */
    getRuleCategoryDetails(ruleCategoryId, callback) {
      let postBody = null;
      // verify the required parameter 'ruleCategoryId' is set
      if (ruleCategoryId === undefined || ruleCategoryId === null) {
        throw new Error("Missing the required parameter 'ruleCategoryId' when calling getRuleCategoryDetails");
      }

      let pathParams = {
        'ruleCategoryId': ruleCategoryId
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
      let returnType = GetRuleCategoryDetails200Response;
      return this.apiClient.callApi(
        '/rules/categories/{ruleCategoryId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRuleTree operation.
     * @callback module:api/RulesApi~getRuleTreeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRuleTree200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get rules tree
     * Get all available rules and their categories in a tree
     * @param {module:api/RulesApi~getRuleTreeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRuleTree200Response}
     */
    getRuleTree(callback) {
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
      let returnType = GetRuleTree200Response;
      return this.apiClient.callApi(
        '/rules/tree', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRules operation.
     * @callback module:api/RulesApi~listRulesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRules200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all rules
     * List all rules
     * @param {module:api/RulesApi~listRulesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRules200Response}
     */
    listRules(callback) {
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
      let returnType = ListRules200Response;
      return this.apiClient.callApi(
        '/rules', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ruleDetails operation.
     * @callback module:api/RulesApi~ruleDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RuleDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a rule details
     * Get the details of a rule
     * @param {String} ruleId Id of the target rule
     * @param {module:api/RulesApi~ruleDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RuleDetails200Response}
     */
    ruleDetails(ruleId, callback) {
      let postBody = null;
      // verify the required parameter 'ruleId' is set
      if (ruleId === undefined || ruleId === null) {
        throw new Error("Missing the required parameter 'ruleId' when calling ruleDetails");
      }

      let pathParams = {
        'ruleId': ruleId
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
      let returnType = RuleDetails200Response;
      return this.apiClient.callApi(
        '/rules/{ruleId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateRule operation.
     * @callback module:api/RulesApi~updateRuleCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateRule200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a rule details
     * Update the details of a rule
     * @param {String} ruleId Id of the target rule
     * @param {module:model/RuleWithCategory} ruleWithCategory 
     * @param {module:api/RulesApi~updateRuleCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateRule200Response}
     */
    updateRule(ruleId, ruleWithCategory, callback) {
      let postBody = ruleWithCategory;
      // verify the required parameter 'ruleId' is set
      if (ruleId === undefined || ruleId === null) {
        throw new Error("Missing the required parameter 'ruleId' when calling updateRule");
      }
      // verify the required parameter 'ruleWithCategory' is set
      if (ruleWithCategory === undefined || ruleWithCategory === null) {
        throw new Error("Missing the required parameter 'ruleWithCategory' when calling updateRule");
      }

      let pathParams = {
        'ruleId': ruleId
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
      let returnType = UpdateRule200Response;
      return this.apiClient.callApi(
        '/rules/{ruleId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateRuleCategory operation.
     * @callback module:api/RulesApi~updateRuleCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateRuleCategory200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update rule category details
     * Update detailed information about a rule category
     * @param {String} ruleCategoryId 
     * @param {module:model/RuleCategoryUpdate} ruleCategoryUpdate 
     * @param {module:api/RulesApi~updateRuleCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateRuleCategory200Response}
     */
    updateRuleCategory(ruleCategoryId, ruleCategoryUpdate, callback) {
      let postBody = ruleCategoryUpdate;
      // verify the required parameter 'ruleCategoryId' is set
      if (ruleCategoryId === undefined || ruleCategoryId === null) {
        throw new Error("Missing the required parameter 'ruleCategoryId' when calling updateRuleCategory");
      }
      // verify the required parameter 'ruleCategoryUpdate' is set
      if (ruleCategoryUpdate === undefined || ruleCategoryUpdate === null) {
        throw new Error("Missing the required parameter 'ruleCategoryUpdate' when calling updateRuleCategory");
      }

      let pathParams = {
        'ruleCategoryId': ruleCategoryId
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
      let returnType = UpdateRuleCategory200Response;
      return this.apiClient.callApi(
        '/rules/categories/{ruleCategoryId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
