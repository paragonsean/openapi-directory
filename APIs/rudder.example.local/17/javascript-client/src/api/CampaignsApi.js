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
import AllCampaigns200Response from '../model/AllCampaigns200Response';
import CampaignDetails from '../model/CampaignDetails';
import DeleteCampaign200Response from '../model/DeleteCampaign200Response';
import DeleteCampaignEvent200Response from '../model/DeleteCampaignEvent200Response';
import GetAllCampaignEvents200Response from '../model/GetAllCampaignEvents200Response';
import GetCampaign200Response from '../model/GetCampaign200Response';
import GetEventsCampaign200Response from '../model/GetEventsCampaign200Response';
import SaveCampaign200Response from '../model/SaveCampaign200Response';
import SaveCampaignEvent200Response from '../model/SaveCampaignEvent200Response';
import ScheduleCampaign200Response from '../model/ScheduleCampaign200Response';

/**
* Campaigns service.
* @module api/CampaignsApi
* @version 17
*/
export default class CampaignsApi {

    /**
    * Constructs a new CampaignsApi. 
    * @alias module:api/CampaignsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the allCampaigns operation.
     * @callback module:api/CampaignsApi~allCampaignsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AllCampaigns200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all campaigns details
     * Get all campaigns details
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [campaignType] Type of the campaigns we want
     * @param {module:model/String} [status] Status of the campaigns we want
     * @param {module:api/CampaignsApi~allCampaignsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AllCampaigns200Response}
     */
    allCampaigns(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'campaignType': opts['campaignType'],
        'status': opts['status']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AllCampaigns200Response;
      return this.apiClient.callApi(
        '/campaigns', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteCampaign operation.
     * @callback module:api/CampaignsApi~deleteCampaignCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteCampaign200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a campaign
     * Delete a campaign
     * @param {String} id Id of the campaign
     * @param {module:api/CampaignsApi~deleteCampaignCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteCampaign200Response}
     */
    deleteCampaign(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteCampaign");
      }

      let pathParams = {
        'id': id
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
      let returnType = DeleteCampaign200Response;
      return this.apiClient.callApi(
        '/campaigns/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteCampaignEvent operation.
     * @callback module:api/CampaignsApi~deleteCampaignEventCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteCampaignEvent200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a campaign event details
     * Delete a campaign event details
     * @param {String} id Id of the campaign event
     * @param {module:api/CampaignsApi~deleteCampaignEventCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteCampaignEvent200Response}
     */
    deleteCampaignEvent(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteCampaignEvent");
      }

      let pathParams = {
        'id': id
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
      let returnType = DeleteCampaignEvent200Response;
      return this.apiClient.callApi(
        '/campaigns/events/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllCampaignEvents operation.
     * @callback module:api/CampaignsApi~getAllCampaignEventsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAllCampaignEvents200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all campaign events
     * Get all campaign events
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [campaignType] Type of the campaigns we want
     * @param {module:model/String} [state] Status of the campaign events we want
     * @param {module:model/String} [campaignId] id of the campaigns we want
     * @param {Number} [limit] Max number of elements in response
     * @param {Number} [offset] Offset of data in response (skip X elements)
     * @param {Date} [before] 
     * @param {Date} [after] 
     * @param {String} [order] 
     * @param {module:model/String} [asc] 
     * @param {module:api/CampaignsApi~getAllCampaignEventsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAllCampaignEvents200Response}
     */
    getAllCampaignEvents(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'campaignType': opts['campaignType'],
        'state': opts['state'],
        'campaignId': opts['campaignId'],
        'limit': opts['limit'],
        'offset': opts['offset'],
        'before': opts['before'],
        'after': opts['after'],
        'order': opts['order'],
        'asc': opts['asc']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetAllCampaignEvents200Response;
      return this.apiClient.callApi(
        '/campaigns/events', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCampaign operation.
     * @callback module:api/CampaignsApi~getCampaignCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCampaign200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a campaign details
     * Get a campaign details
     * @param {String} id Id of the campaign
     * @param {module:api/CampaignsApi~getCampaignCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCampaign200Response}
     */
    getCampaign(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getCampaign");
      }

      let pathParams = {
        'id': id
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
      let returnType = GetCampaign200Response;
      return this.apiClient.callApi(
        '/campaigns/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCampaignEvent operation.
     * @callback module:api/CampaignsApi~getCampaignEventCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAllCampaignEvents200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a campaign event details
     * Get a campaign event details
     * @param {String} id Id of the campaign event
     * @param {module:api/CampaignsApi~getCampaignEventCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAllCampaignEvents200Response}
     */
    getCampaignEvent(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getCampaignEvent");
      }

      let pathParams = {
        'id': id
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
      let returnType = GetAllCampaignEvents200Response;
      return this.apiClient.callApi(
        '/campaigns/events/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEventsCampaign operation.
     * @callback module:api/CampaignsApi~getEventsCampaignCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEventsCampaign200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get campaign events for a campaign
     * Get campaign events for a campaign
     * @param {String} id Id of the campaign
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [campaignType] Type of the campaigns we want
     * @param {module:model/String} [state] Status of the campaign events we want
     * @param {Number} [limit] Max number of elements in response
     * @param {Number} [offset] Offset of data in response (skip X elements)
     * @param {Date} [before] 
     * @param {Date} [after] 
     * @param {String} [order] 
     * @param {module:model/String} [asc] 
     * @param {module:api/CampaignsApi~getEventsCampaignCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEventsCampaign200Response}
     */
    getEventsCampaign(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getEventsCampaign");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'campaignType': opts['campaignType'],
        'state': opts['state'],
        'limit': opts['limit'],
        'offset': opts['offset'],
        'before': opts['before'],
        'after': opts['after'],
        'order': opts['order'],
        'asc': opts['asc']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['API-Tokens'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetEventsCampaign200Response;
      return this.apiClient.callApi(
        '/campaigns/{id}/events', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the saveCampaign operation.
     * @callback module:api/CampaignsApi~saveCampaignCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SaveCampaign200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Save a campaign
     * Save a campaign details
     * @param {module:model/CampaignDetails} campaignDetails 
     * @param {module:api/CampaignsApi~saveCampaignCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SaveCampaign200Response}
     */
    saveCampaign(campaignDetails, callback) {
      let postBody = campaignDetails;
      // verify the required parameter 'campaignDetails' is set
      if (campaignDetails === undefined || campaignDetails === null) {
        throw new Error("Missing the required parameter 'campaignDetails' when calling saveCampaign");
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
      let returnType = SaveCampaign200Response;
      return this.apiClient.callApi(
        '/campaigns', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the saveCampaignEvent operation.
     * @callback module:api/CampaignsApi~saveCampaignEventCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SaveCampaignEvent200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing event
     * Update an existing event
     * @param {String} id Id of the campaign event
     * @param {module:api/CampaignsApi~saveCampaignEventCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SaveCampaignEvent200Response}
     */
    saveCampaignEvent(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling saveCampaignEvent");
      }

      let pathParams = {
        'id': id
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
      let returnType = SaveCampaignEvent200Response;
      return this.apiClient.callApi(
        '/campaigns/events/{id}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the scheduleCampaign operation.
     * @callback module:api/CampaignsApi~scheduleCampaignCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScheduleCampaign200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Schedule a campaign event for a campaign
     * Schedule a campaign event for a campaign
     * @param {String} id Id of the campaign
     * @param {module:api/CampaignsApi~scheduleCampaignCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScheduleCampaign200Response}
     */
    scheduleCampaign(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling scheduleCampaign");
      }

      let pathParams = {
        'id': id
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
      let returnType = ScheduleCampaign200Response;
      return this.apiClient.callApi(
        '/campaigns/{id}/schedule', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
