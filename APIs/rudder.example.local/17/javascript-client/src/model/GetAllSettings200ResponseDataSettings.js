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

import ApiClient from '../ApiClient';
import GetAllSettings200ResponseDataSettingsAllowedNetworksInner from './GetAllSettings200ResponseDataSettingsAllowedNetworksInner';

/**
 * The GetAllSettings200ResponseDataSettings model module.
 * @module model/GetAllSettings200ResponseDataSettings
 * @version 17
 */
class GetAllSettings200ResponseDataSettings {
    /**
     * Constructs a new <code>GetAllSettings200ResponseDataSettings</code>.
     * @alias module:model/GetAllSettings200ResponseDataSettings
     */
    constructor() { 
        
        GetAllSettings200ResponseDataSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['node_accept_duplicated_hostname'] = false;
        obj['rudder_compute_changes'] = true;
        obj['rudder_compute_dyngroups_max_parallelism'] = '1';
        obj['rudder_generation_compute_dyngroups'] = true;
        obj['rudder_generation_continue_on_error'] = false;
        obj['rudder_generation_delay'] = '0 seconds';
        obj['rudder_generation_js_timeout'] = 30;
        obj['rudder_generation_max_parallelism'] = 'x0.5';
        obj['rudder_generation_policy'] = 'all';
        obj['rudder_save_db_compliance_details'] = false;
        obj['rudder_save_db_compliance_levels'] = true;
        obj['rudder_verify_certificates'] = false;
        obj['unexpected_unbound_var_values'] = true;
    }

    /**
     * Constructs a <code>GetAllSettings200ResponseDataSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetAllSettings200ResponseDataSettings} obj Optional instance to populate.
     * @return {module:model/GetAllSettings200ResponseDataSettings} The populated <code>GetAllSettings200ResponseDataSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetAllSettings200ResponseDataSettings();

            if (data.hasOwnProperty('allowed_networks')) {
                obj['allowed_networks'] = ApiClient.convertToType(data['allowed_networks'], [GetAllSettings200ResponseDataSettingsAllowedNetworksInner]);
            }
            if (data.hasOwnProperty('change_message_prompt')) {
                obj['change_message_prompt'] = ApiClient.convertToType(data['change_message_prompt'], 'String');
            }
            if (data.hasOwnProperty('display_recent_changes_graphs')) {
                obj['display_recent_changes_graphs'] = ApiClient.convertToType(data['display_recent_changes_graphs'], 'Boolean');
            }
            if (data.hasOwnProperty('enable_change_message')) {
                obj['enable_change_message'] = ApiClient.convertToType(data['enable_change_message'], 'Boolean');
            }
            if (data.hasOwnProperty('enable_change_request')) {
                obj['enable_change_request'] = ApiClient.convertToType(data['enable_change_request'], 'Boolean');
            }
            if (data.hasOwnProperty('enable_javascript_directives')) {
                obj['enable_javascript_directives'] = ApiClient.convertToType(data['enable_javascript_directives'], 'String');
            }
            if (data.hasOwnProperty('enable_self_deployment')) {
                obj['enable_self_deployment'] = ApiClient.convertToType(data['enable_self_deployment'], 'Boolean');
            }
            if (data.hasOwnProperty('enable_self_validation')) {
                obj['enable_self_validation'] = ApiClient.convertToType(data['enable_self_validation'], 'Boolean');
            }
            if (data.hasOwnProperty('first_run_hour')) {
                obj['first_run_hour'] = ApiClient.convertToType(data['first_run_hour'], 'Number');
            }
            if (data.hasOwnProperty('first_run_minute')) {
                obj['first_run_minute'] = ApiClient.convertToType(data['first_run_minute'], 'Number');
            }
            if (data.hasOwnProperty('global_policy_mode')) {
                obj['global_policy_mode'] = ApiClient.convertToType(data['global_policy_mode'], 'String');
            }
            if (data.hasOwnProperty('global_policy_mode_overridable')) {
                obj['global_policy_mode_overridable'] = ApiClient.convertToType(data['global_policy_mode_overridable'], 'Boolean');
            }
            if (data.hasOwnProperty('heartbeat_frequency')) {
                obj['heartbeat_frequency'] = ApiClient.convertToType(data['heartbeat_frequency'], 'Number');
            }
            if (data.hasOwnProperty('mandatory_change_message')) {
                obj['mandatory_change_message'] = ApiClient.convertToType(data['mandatory_change_message'], 'Boolean');
            }
            if (data.hasOwnProperty('modified_file_ttl')) {
                obj['modified_file_ttl'] = ApiClient.convertToType(data['modified_file_ttl'], 'Number');
            }
            if (data.hasOwnProperty('node_accept_duplicated_hostname')) {
                obj['node_accept_duplicated_hostname'] = ApiClient.convertToType(data['node_accept_duplicated_hostname'], 'Boolean');
            }
            if (data.hasOwnProperty('node_onaccept_default_policyMode')) {
                obj['node_onaccept_default_policyMode'] = ApiClient.convertToType(data['node_onaccept_default_policyMode'], 'String');
            }
            if (data.hasOwnProperty('node_onaccept_default_state')) {
                obj['node_onaccept_default_state'] = ApiClient.convertToType(data['node_onaccept_default_state'], 'String');
            }
            if (data.hasOwnProperty('output_file_ttl')) {
                obj['output_file_ttl'] = ApiClient.convertToType(data['output_file_ttl'], 'Number');
            }
            if (data.hasOwnProperty('relay_server_synchronization_method')) {
                obj['relay_server_synchronization_method'] = ApiClient.convertToType(data['relay_server_synchronization_method'], 'String');
            }
            if (data.hasOwnProperty('relay_server_synchronize_policies')) {
                obj['relay_server_synchronize_policies'] = ApiClient.convertToType(data['relay_server_synchronize_policies'], 'Boolean');
            }
            if (data.hasOwnProperty('relay_server_synchronize_shared_files')) {
                obj['relay_server_synchronize_shared_files'] = ApiClient.convertToType(data['relay_server_synchronize_shared_files'], 'Boolean');
            }
            if (data.hasOwnProperty('reporting_mode')) {
                obj['reporting_mode'] = ApiClient.convertToType(data['reporting_mode'], 'String');
            }
            if (data.hasOwnProperty('require_time_synchronization')) {
                obj['require_time_synchronization'] = ApiClient.convertToType(data['require_time_synchronization'], 'Boolean');
            }
            if (data.hasOwnProperty('rudder_compute_changes')) {
                obj['rudder_compute_changes'] = ApiClient.convertToType(data['rudder_compute_changes'], 'Boolean');
            }
            if (data.hasOwnProperty('rudder_compute_dyngroups_max_parallelism')) {
                obj['rudder_compute_dyngroups_max_parallelism'] = ApiClient.convertToType(data['rudder_compute_dyngroups_max_parallelism'], 'String');
            }
            if (data.hasOwnProperty('rudder_generation_compute_dyngroups')) {
                obj['rudder_generation_compute_dyngroups'] = ApiClient.convertToType(data['rudder_generation_compute_dyngroups'], 'Boolean');
            }
            if (data.hasOwnProperty('rudder_generation_continue_on_error')) {
                obj['rudder_generation_continue_on_error'] = ApiClient.convertToType(data['rudder_generation_continue_on_error'], 'Boolean');
            }
            if (data.hasOwnProperty('rudder_generation_delay')) {
                obj['rudder_generation_delay'] = ApiClient.convertToType(data['rudder_generation_delay'], 'String');
            }
            if (data.hasOwnProperty('rudder_generation_js_timeout')) {
                obj['rudder_generation_js_timeout'] = ApiClient.convertToType(data['rudder_generation_js_timeout'], 'Number');
            }
            if (data.hasOwnProperty('rudder_generation_max_parallelism')) {
                obj['rudder_generation_max_parallelism'] = ApiClient.convertToType(data['rudder_generation_max_parallelism'], 'String');
            }
            if (data.hasOwnProperty('rudder_generation_policy')) {
                obj['rudder_generation_policy'] = ApiClient.convertToType(data['rudder_generation_policy'], 'String');
            }
            if (data.hasOwnProperty('rudder_report_protocol_default')) {
                obj['rudder_report_protocol_default'] = ApiClient.convertToType(data['rudder_report_protocol_default'], 'String');
            }
            if (data.hasOwnProperty('rudder_save_db_compliance_details')) {
                obj['rudder_save_db_compliance_details'] = ApiClient.convertToType(data['rudder_save_db_compliance_details'], 'Boolean');
            }
            if (data.hasOwnProperty('rudder_save_db_compliance_levels')) {
                obj['rudder_save_db_compliance_levels'] = ApiClient.convertToType(data['rudder_save_db_compliance_levels'], 'Boolean');
            }
            if (data.hasOwnProperty('rudder_verify_certificates')) {
                obj['rudder_verify_certificates'] = ApiClient.convertToType(data['rudder_verify_certificates'], 'Boolean');
            }
            if (data.hasOwnProperty('run_frequency')) {
                obj['run_frequency'] = ApiClient.convertToType(data['run_frequency'], 'Number');
            }
            if (data.hasOwnProperty('send_metrics')) {
                obj['send_metrics'] = ApiClient.convertToType(data['send_metrics'], 'String');
            }
            if (data.hasOwnProperty('splay_time')) {
                obj['splay_time'] = ApiClient.convertToType(data['splay_time'], 'Number');
            }
            if (data.hasOwnProperty('unexpected_unbound_var_values')) {
                obj['unexpected_unbound_var_values'] = ApiClient.convertToType(data['unexpected_unbound_var_values'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetAllSettings200ResponseDataSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetAllSettings200ResponseDataSettings</code>.
     */
    static validateJSON(data) {
        if (data['allowed_networks']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['allowed_networks'])) {
                throw new Error("Expected the field `allowed_networks` to be an array in the JSON data but got " + data['allowed_networks']);
            }
            // validate the optional field `allowed_networks` (array)
            for (const item of data['allowed_networks']) {
                GetAllSettings200ResponseDataSettingsAllowedNetworksInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['change_message_prompt'] && !(typeof data['change_message_prompt'] === 'string' || data['change_message_prompt'] instanceof String)) {
            throw new Error("Expected the field `change_message_prompt` to be a primitive type in the JSON string but got " + data['change_message_prompt']);
        }
        // ensure the json data is a string
        if (data['enable_javascript_directives'] && !(typeof data['enable_javascript_directives'] === 'string' || data['enable_javascript_directives'] instanceof String)) {
            throw new Error("Expected the field `enable_javascript_directives` to be a primitive type in the JSON string but got " + data['enable_javascript_directives']);
        }
        // ensure the json data is a string
        if (data['global_policy_mode'] && !(typeof data['global_policy_mode'] === 'string' || data['global_policy_mode'] instanceof String)) {
            throw new Error("Expected the field `global_policy_mode` to be a primitive type in the JSON string but got " + data['global_policy_mode']);
        }
        // ensure the json data is a string
        if (data['node_onaccept_default_policyMode'] && !(typeof data['node_onaccept_default_policyMode'] === 'string' || data['node_onaccept_default_policyMode'] instanceof String)) {
            throw new Error("Expected the field `node_onaccept_default_policyMode` to be a primitive type in the JSON string but got " + data['node_onaccept_default_policyMode']);
        }
        // ensure the json data is a string
        if (data['node_onaccept_default_state'] && !(typeof data['node_onaccept_default_state'] === 'string' || data['node_onaccept_default_state'] instanceof String)) {
            throw new Error("Expected the field `node_onaccept_default_state` to be a primitive type in the JSON string but got " + data['node_onaccept_default_state']);
        }
        // ensure the json data is a string
        if (data['relay_server_synchronization_method'] && !(typeof data['relay_server_synchronization_method'] === 'string' || data['relay_server_synchronization_method'] instanceof String)) {
            throw new Error("Expected the field `relay_server_synchronization_method` to be a primitive type in the JSON string but got " + data['relay_server_synchronization_method']);
        }
        // ensure the json data is a string
        if (data['reporting_mode'] && !(typeof data['reporting_mode'] === 'string' || data['reporting_mode'] instanceof String)) {
            throw new Error("Expected the field `reporting_mode` to be a primitive type in the JSON string but got " + data['reporting_mode']);
        }
        // ensure the json data is a string
        if (data['rudder_compute_dyngroups_max_parallelism'] && !(typeof data['rudder_compute_dyngroups_max_parallelism'] === 'string' || data['rudder_compute_dyngroups_max_parallelism'] instanceof String)) {
            throw new Error("Expected the field `rudder_compute_dyngroups_max_parallelism` to be a primitive type in the JSON string but got " + data['rudder_compute_dyngroups_max_parallelism']);
        }
        // ensure the json data is a string
        if (data['rudder_generation_delay'] && !(typeof data['rudder_generation_delay'] === 'string' || data['rudder_generation_delay'] instanceof String)) {
            throw new Error("Expected the field `rudder_generation_delay` to be a primitive type in the JSON string but got " + data['rudder_generation_delay']);
        }
        // ensure the json data is a string
        if (data['rudder_generation_max_parallelism'] && !(typeof data['rudder_generation_max_parallelism'] === 'string' || data['rudder_generation_max_parallelism'] instanceof String)) {
            throw new Error("Expected the field `rudder_generation_max_parallelism` to be a primitive type in the JSON string but got " + data['rudder_generation_max_parallelism']);
        }
        // ensure the json data is a string
        if (data['rudder_generation_policy'] && !(typeof data['rudder_generation_policy'] === 'string' || data['rudder_generation_policy'] instanceof String)) {
            throw new Error("Expected the field `rudder_generation_policy` to be a primitive type in the JSON string but got " + data['rudder_generation_policy']);
        }
        // ensure the json data is a string
        if (data['rudder_report_protocol_default'] && !(typeof data['rudder_report_protocol_default'] === 'string' || data['rudder_report_protocol_default'] instanceof String)) {
            throw new Error("Expected the field `rudder_report_protocol_default` to be a primitive type in the JSON string but got " + data['rudder_report_protocol_default']);
        }
        // ensure the json data is a string
        if (data['send_metrics'] && !(typeof data['send_metrics'] === 'string' || data['send_metrics'] instanceof String)) {
            throw new Error("Expected the field `send_metrics` to be a primitive type in the JSON string but got " + data['send_metrics']);
        }

        return true;
    }


}



/**
 * List of allowed networks for each policy server (root and relays)
 * @member {Array.<module:model/GetAllSettings200ResponseDataSettingsAllowedNetworksInner>} allowed_networks
 */
GetAllSettings200ResponseDataSettings.prototype['allowed_networks'] = undefined;

/**
 * Explanation to display
 * @member {String} change_message_prompt
 */
GetAllSettings200ResponseDataSettings.prototype['change_message_prompt'] = undefined;

/**
 * Display changes graphs
 * @member {Boolean} display_recent_changes_graphs
 */
GetAllSettings200ResponseDataSettings.prototype['display_recent_changes_graphs'] = undefined;

/**
 * Enable change audit logs
 * @member {Boolean} enable_change_message
 */
GetAllSettings200ResponseDataSettings.prototype['enable_change_message'] = undefined;

/**
 * Enable Change Requests
 * @member {Boolean} enable_change_request
 */
GetAllSettings200ResponseDataSettings.prototype['enable_change_request'] = undefined;

/**
 * Enable script evaluation in Directives
 * @member {String} enable_javascript_directives
 */
GetAllSettings200ResponseDataSettings.prototype['enable_javascript_directives'] = undefined;

/**
 * Allow self deployment
 * @member {Boolean} enable_self_deployment
 */
GetAllSettings200ResponseDataSettings.prototype['enable_self_deployment'] = undefined;

/**
 * Allow self validation
 * @member {Boolean} enable_self_validation
 */
GetAllSettings200ResponseDataSettings.prototype['enable_self_validation'] = undefined;

/**
 * First agent run time - hour
 * @member {Number} first_run_hour
 */
GetAllSettings200ResponseDataSettings.prototype['first_run_hour'] = undefined;

/**
 * First agent run time - minute
 * @member {Number} first_run_minute
 */
GetAllSettings200ResponseDataSettings.prototype['first_run_minute'] = undefined;

/**
 * Define the default setting for global policy mode
 * @member {module:model/GetAllSettings200ResponseDataSettings.GlobalPolicyModeEnum} global_policy_mode
 */
GetAllSettings200ResponseDataSettings.prototype['global_policy_mode'] = undefined;

/**
 * Allow overrides on this default setting
 * @member {Boolean} global_policy_mode_overridable
 */
GetAllSettings200ResponseDataSettings.prototype['global_policy_mode_overridable'] = undefined;

/**
 * Send heartbeat every heartbeat_frequency runs (only on **changes-only** compliance mode)
 * @member {Number} heartbeat_frequency
 */
GetAllSettings200ResponseDataSettings.prototype['heartbeat_frequency'] = undefined;

/**
 * Make message mandatory
 * @member {Boolean} mandatory_change_message
 */
GetAllSettings200ResponseDataSettings.prototype['mandatory_change_message'] = undefined;

/**
 * Number of days to retain modified files
 * @member {Number} modified_file_ttl
 */
GetAllSettings200ResponseDataSettings.prototype['modified_file_ttl'] = undefined;

/**
 * Allow acceptation of a pending node when another one with the same hostname is already accepted
 * @member {Boolean} node_accept_duplicated_hostname
 * @default false
 */
GetAllSettings200ResponseDataSettings.prototype['node_accept_duplicated_hostname'] = false;

/**
 * Default policy mode for accepted node
 * @member {module:model/GetAllSettings200ResponseDataSettings.NodeOnacceptDefaultPolicyModeEnum} node_onaccept_default_policyMode
 */
GetAllSettings200ResponseDataSettings.prototype['node_onaccept_default_policyMode'] = undefined;

/**
 * Set default state for node when they are accepted within Rudder
 * @member {module:model/GetAllSettings200ResponseDataSettings.NodeOnacceptDefaultStateEnum} node_onaccept_default_state
 */
GetAllSettings200ResponseDataSettings.prototype['node_onaccept_default_state'] = undefined;

/**
 * Number of days to retain agent output files
 * @member {Number} output_file_ttl
 */
GetAllSettings200ResponseDataSettings.prototype['output_file_ttl'] = undefined;

/**
 * Method used to synchronize data between server and relays, either \"classic\" (agent protocol, default), \"rsync\" (use rsync to synchronize, that you'll need to be manually set up), or \"disabled\" (use third party system to transmit data)
 * @member {module:model/GetAllSettings200ResponseDataSettings.RelayServerSynchronizationMethodEnum} relay_server_synchronization_method
 */
GetAllSettings200ResponseDataSettings.prototype['relay_server_synchronization_method'] = undefined;

/**
 * If **rsync** is set as a synchronization method, use rsync to synchronize policies between Rudder server and relays. If false, you'll have to synchronize policies yourself.
 * @member {Boolean} relay_server_synchronize_policies
 */
GetAllSettings200ResponseDataSettings.prototype['relay_server_synchronize_policies'] = undefined;

/**
 * If **rsync** is set as a synchronization method, use rsync to synchronize shared files between Rudder server and relays. If false, you'll have to synchronize shared files yourself.
 * @member {Boolean} relay_server_synchronize_shared_files
 */
GetAllSettings200ResponseDataSettings.prototype['relay_server_synchronize_shared_files'] = undefined;

/**
 * Compliance reporting mode
 * @member {module:model/GetAllSettings200ResponseDataSettings.ReportingModeEnum} reporting_mode
 */
GetAllSettings200ResponseDataSettings.prototype['reporting_mode'] = undefined;

/**
 * Require time synchronization between nodes and policy server
 * @member {Boolean} require_time_synchronization
 */
GetAllSettings200ResponseDataSettings.prototype['require_time_synchronization'] = undefined;

/**
 * Compute list of changes (repaired reports) per rule
 * @member {Boolean} rudder_compute_changes
 * @default true
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_compute_changes'] = true;

/**
 * Set the parallelism to compute dynamic group, as a number of thread (i.e. 4), or a multiplicative of the number of core (x0.5)
 * @member {String} rudder_compute_dyngroups_max_parallelism
 * @default '1'
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_compute_dyngroups_max_parallelism'] = '1';

/**
 * Recompute all dynamic groups at the start of policy generation
 * @member {Boolean} rudder_generation_compute_dyngroups
 * @default true
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_generation_compute_dyngroups'] = true;

/**
 * Policy generation continues on error during NodeConfiguration evaluation
 * @member {Boolean} rudder_generation_continue_on_error
 * @default false
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_generation_continue_on_error'] = false;

/**
 * Set a delay before starting policy generation, this will allow you to accumulate changes before they are deployed to Nodes, and can also lessen webapp resources needs. The value is a number followed by the time unit needed (seconds/s, minutes/m, hours/h ...), ie \"5m\" for 5 minutes
 * @member {String} rudder_generation_delay
 * @default '0 seconds'
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_generation_delay'] = '0 seconds';

/**
 * Policy generation JS evaluation of directive parameter timeout in seconds
 * @member {Number} rudder_generation_js_timeout
 * @default 30
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_generation_js_timeout'] = 30;

/**
 * Set the policy generation parallelism, either as an number of thread (i.e. 4), or a multiplicative of the number of core (x0.5)
 * @member {String} rudder_generation_max_parallelism
 * @default 'x0.5'
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_generation_max_parallelism'] = 'x0.5';

/**
 * Should policy generation be triggered automatically after a change (value 'all'), or should we wait until a manual launch (through api or UI, value 'onlyManual') or even no policy generation at all (value \"none\")
 * @member {String} rudder_generation_policy
 * @default 'all'
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_generation_policy'] = 'all';

/**
 * Default reporting protocol used
 * @member {module:model/GetAllSettings200ResponseDataSettings.RudderReportProtocolDefaultEnum} rudder_report_protocol_default
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_report_protocol_default'] = undefined;

/**
 * Store all compliance details in database
 * @member {Boolean} rudder_save_db_compliance_details
 * @default false
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_save_db_compliance_details'] = false;

/**
 * Store all compliance levels in database
 * @member {Boolean} rudder_save_db_compliance_levels
 * @default true
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_save_db_compliance_levels'] = true;

/**
 * Enforce certificate validation in all HTTPS calls
 * @member {Boolean} rudder_verify_certificates
 * @default false
 */
GetAllSettings200ResponseDataSettings.prototype['rudder_verify_certificates'] = false;

/**
 * Agent run schedule - time between agent runs (in minutes)
 * @member {Number} run_frequency
 */
GetAllSettings200ResponseDataSettings.prototype['run_frequency'] = undefined;

/**
 * Send anonymous usage statistics
 * @member {String} send_metrics
 */
GetAllSettings200ResponseDataSettings.prototype['send_metrics'] = undefined;

/**
 * Maximum delay after scheduled run time (random interval)
 * @member {Number} splay_time
 */
GetAllSettings200ResponseDataSettings.prototype['splay_time'] = undefined;

/**
 * Allows multiple reports for configuration based on a multivalued variable
 * @member {Boolean} unexpected_unbound_var_values
 * @default true
 */
GetAllSettings200ResponseDataSettings.prototype['unexpected_unbound_var_values'] = true;





/**
 * Allowed values for the <code>global_policy_mode</code> property.
 * @enum {String}
 * @readonly
 */
GetAllSettings200ResponseDataSettings['GlobalPolicyModeEnum'] = {

    /**
     * value: "enforce"
     * @const
     */
    "enforce": "enforce",

    /**
     * value: "audit"
     * @const
     */
    "audit": "audit"
};


/**
 * Allowed values for the <code>node_onaccept_default_policyMode</code> property.
 * @enum {String}
 * @readonly
 */
GetAllSettings200ResponseDataSettings['NodeOnacceptDefaultPolicyModeEnum'] = {

    /**
     * value: "default"
     * @const
     */
    "default": "default",

    /**
     * value: "enforce"
     * @const
     */
    "enforce": "enforce",

    /**
     * value: "audit"
     * @const
     */
    "audit": "audit"
};


/**
 * Allowed values for the <code>node_onaccept_default_state</code> property.
 * @enum {String}
 * @readonly
 */
GetAllSettings200ResponseDataSettings['NodeOnacceptDefaultStateEnum'] = {

    /**
     * value: "enabled"
     * @const
     */
    "enabled": "enabled",

    /**
     * value: "ignored"
     * @const
     */
    "ignored": "ignored",

    /**
     * value: "empty-policies"
     * @const
     */
    "empty-policies": "empty-policies",

    /**
     * value: "initializing"
     * @const
     */
    "initializing": "initializing",

    /**
     * value: "preparing-eol"
     * @const
     */
    "preparing-eol": "preparing-eol"
};


/**
 * Allowed values for the <code>relay_server_synchronization_method</code> property.
 * @enum {String}
 * @readonly
 */
GetAllSettings200ResponseDataSettings['RelayServerSynchronizationMethodEnum'] = {

    /**
     * value: "classic"
     * @const
     */
    "classic": "classic",

    /**
     * value: "rsync"
     * @const
     */
    "rsync": "rsync",

    /**
     * value: "disabled"
     * @const
     */
    "disabled": "disabled"
};


/**
 * Allowed values for the <code>reporting_mode</code> property.
 * @enum {String}
 * @readonly
 */
GetAllSettings200ResponseDataSettings['ReportingModeEnum'] = {

    /**
     * value: "full-compliance"
     * @const
     */
    "full-compliance": "full-compliance",

    /**
     * value: "changes-only"
     * @const
     */
    "changes-only": "changes-only",

    /**
     * value: "reports-disabled"
     * @const
     */
    "reports-disabled": "reports-disabled"
};


/**
 * Allowed values for the <code>rudder_report_protocol_default</code> property.
 * @enum {String}
 * @readonly
 */
GetAllSettings200ResponseDataSettings['RudderReportProtocolDefaultEnum'] = {

    /**
     * value: "HTTPS"
     * @const
     */
    "HTTPS": "HTTPS",

    /**
     * value: "SYSLOG"
     * @const
     */
    "SYSLOG": "SYSLOG"
};



export default GetAllSettings200ResponseDataSettings;

