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
import CreateGroup200Response from '../model/CreateGroup200Response';
import CreateGroupCategory200Response from '../model/CreateGroupCategory200Response';
import DeleteGroup200Response from '../model/DeleteGroup200Response';
import DeleteGroupCategory200Response from '../model/DeleteGroupCategory200Response';
import GetGroupCategoryDetails200Response from '../model/GetGroupCategoryDetails200Response';
import GetGroupTree200Response from '../model/GetGroupTree200Response';
import GroupCategory from '../model/GroupCategory';
import GroupCategoryUpdate from '../model/GroupCategoryUpdate';
import GroupDetails200Response from '../model/GroupDetails200Response';
import GroupNew from '../model/GroupNew';
import GroupUpdate from '../model/GroupUpdate';
import ListGroups200Response from '../model/ListGroups200Response';
import ReloadGroup200Response from '../model/ReloadGroup200Response';
import UpdateGroup200Response from '../model/UpdateGroup200Response';
import UpdateGroupCategory200Response from '../model/UpdateGroupCategory200Response';

/**
* Groups service.
* @module api/GroupsApi
* @version 17
*/
export default class GroupsApi {

    /**
    * Constructs a new GroupsApi. 
    * @alias module:api/GroupsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createGroup operation.
     * @callback module:api/GroupsApi~createGroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateGroup200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a group
     * Create a new group based in provided parameters
     * @param {Object} opts Optional parameters
     * @param {module:model/GroupNew} [groupNew] 
     * @param {module:api/GroupsApi~createGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateGroup200Response}
     */
    createGroup(opts, callback) {
      opts = opts || {};
      let postBody = opts['groupNew'];

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
      let returnType = CreateGroup200Response;
      return this.apiClient.callApi(
        '/groups', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createGroupCategory operation.
     * @callback module:api/GroupsApi~createGroupCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateGroupCategory200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a group category
     * Create a new group category
     * @param {module:model/GroupCategory} groupCategory 
     * @param {module:api/GroupsApi~createGroupCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateGroupCategory200Response}
     */
    createGroupCategory(groupCategory, callback) {
      let postBody = groupCategory;
      // verify the required parameter 'groupCategory' is set
      if (groupCategory === undefined || groupCategory === null) {
        throw new Error("Missing the required parameter 'groupCategory' when calling createGroupCategory");
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
      let returnType = CreateGroupCategory200Response;
      return this.apiClient.callApi(
        '/groups/categories', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteGroup operation.
     * @callback module:api/GroupsApi~deleteGroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteGroup200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a group
     * Update detailed information about a group
     * @param {String} groupId Id of the group
     * @param {module:api/GroupsApi~deleteGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteGroup200Response}
     */
    deleteGroup(groupId, callback) {
      let postBody = null;
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling deleteGroup");
      }

      let pathParams = {
        'groupId': groupId
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
      let returnType = DeleteGroup200Response;
      return this.apiClient.callApi(
        '/groups/{groupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteGroupCategory operation.
     * @callback module:api/GroupsApi~deleteGroupCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteGroupCategory200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete group category
     * Delete a group category. It must have no child groups and no children categories.
     * @param {String} groupCategoryId 
     * @param {module:api/GroupsApi~deleteGroupCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteGroupCategory200Response}
     */
    deleteGroupCategory(groupCategoryId, callback) {
      let postBody = null;
      // verify the required parameter 'groupCategoryId' is set
      if (groupCategoryId === undefined || groupCategoryId === null) {
        throw new Error("Missing the required parameter 'groupCategoryId' when calling deleteGroupCategory");
      }

      let pathParams = {
        'groupCategoryId': groupCategoryId
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
      let returnType = DeleteGroupCategory200Response;
      return this.apiClient.callApi(
        '/groups/categories/{groupCategoryId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getGroupCategoryDetails operation.
     * @callback module:api/GroupsApi~getGroupCategoryDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetGroupCategoryDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get group category details
     * Get detailed information about a group category
     * @param {String} groupCategoryId 
     * @param {module:api/GroupsApi~getGroupCategoryDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetGroupCategoryDetails200Response}
     */
    getGroupCategoryDetails(groupCategoryId, callback) {
      let postBody = null;
      // verify the required parameter 'groupCategoryId' is set
      if (groupCategoryId === undefined || groupCategoryId === null) {
        throw new Error("Missing the required parameter 'groupCategoryId' when calling getGroupCategoryDetails");
      }

      let pathParams = {
        'groupCategoryId': groupCategoryId
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
      let returnType = GetGroupCategoryDetails200Response;
      return this.apiClient.callApi(
        '/groups/categories/{groupCategoryId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getGroupTree operation.
     * @callback module:api/GroupsApi~getGroupTreeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetGroupTree200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get groups tree
     * Get all available groups and their categories in a tree
     * @param {module:api/GroupsApi~getGroupTreeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetGroupTree200Response}
     */
    getGroupTree(callback) {
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
      let returnType = GetGroupTree200Response;
      return this.apiClient.callApi(
        '/groups/tree', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the groupDetails operation.
     * @callback module:api/GroupsApi~groupDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GroupDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get group details
     * Get detailed information about a group
     * @param {String} groupId Id of the group
     * @param {module:api/GroupsApi~groupDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GroupDetails200Response}
     */
    groupDetails(groupId, callback) {
      let postBody = null;
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling groupDetails");
      }

      let pathParams = {
        'groupId': groupId
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
      let returnType = GroupDetails200Response;
      return this.apiClient.callApi(
        '/groups/{groupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listGroups operation.
     * @callback module:api/GroupsApi~listGroupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListGroups200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all groups
     * List all groups
     * @param {module:api/GroupsApi~listGroupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListGroups200Response}
     */
    listGroups(callback) {
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
      let returnType = ListGroups200Response;
      return this.apiClient.callApi(
        '/groups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reloadGroup operation.
     * @callback module:api/GroupsApi~reloadGroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReloadGroup200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reload a group
     * Recompute the content of a group
     * @param {String} groupId Id of the group
     * @param {module:api/GroupsApi~reloadGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReloadGroup200Response}
     */
    reloadGroup(groupId, callback) {
      let postBody = null;
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling reloadGroup");
      }

      let pathParams = {
        'groupId': groupId
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
      let returnType = ReloadGroup200Response;
      return this.apiClient.callApi(
        '/groups/{groupId}/reload', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateGroup operation.
     * @callback module:api/GroupsApi~updateGroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateGroup200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update group details
     * Update detailed information about a group
     * @param {String} groupId Id of the group
     * @param {module:model/GroupUpdate} groupUpdate 
     * @param {module:api/GroupsApi~updateGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateGroup200Response}
     */
    updateGroup(groupId, groupUpdate, callback) {
      let postBody = groupUpdate;
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling updateGroup");
      }
      // verify the required parameter 'groupUpdate' is set
      if (groupUpdate === undefined || groupUpdate === null) {
        throw new Error("Missing the required parameter 'groupUpdate' when calling updateGroup");
      }

      let pathParams = {
        'groupId': groupId
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
      let returnType = UpdateGroup200Response;
      return this.apiClient.callApi(
        '/groups/{groupId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateGroupCategory operation.
     * @callback module:api/GroupsApi~updateGroupCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateGroupCategory200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update group category details
     * Update detailed information about a group category
     * @param {String} groupCategoryId 
     * @param {module:model/GroupCategoryUpdate} groupCategoryUpdate 
     * @param {module:api/GroupsApi~updateGroupCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateGroupCategory200Response}
     */
    updateGroupCategory(groupCategoryId, groupCategoryUpdate, callback) {
      let postBody = groupCategoryUpdate;
      // verify the required parameter 'groupCategoryId' is set
      if (groupCategoryId === undefined || groupCategoryId === null) {
        throw new Error("Missing the required parameter 'groupCategoryId' when calling updateGroupCategory");
      }
      // verify the required parameter 'groupCategoryUpdate' is set
      if (groupCategoryUpdate === undefined || groupCategoryUpdate === null) {
        throw new Error("Missing the required parameter 'groupCategoryUpdate' when calling updateGroupCategory");
      }

      let pathParams = {
        'groupCategoryId': groupCategoryId
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
      let returnType = UpdateGroupCategory200Response;
      return this.apiClient.callApi(
        '/groups/categories/{groupCategoryId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
