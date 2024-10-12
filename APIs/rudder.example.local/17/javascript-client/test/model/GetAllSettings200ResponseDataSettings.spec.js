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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.RudderApi);
  }
}(this, function(expect, RudderApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new RudderApi.GetAllSettings200ResponseDataSettings();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('GetAllSettings200ResponseDataSettings', function() {
    it('should create an instance of GetAllSettings200ResponseDataSettings', function() {
      // uncomment below and update the code to test GetAllSettings200ResponseDataSettings
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be.a(RudderApi.GetAllSettings200ResponseDataSettings);
    });

    it('should have the property allowedNetworks (base name: "allowed_networks")', function() {
      // uncomment below and update the code to test the property allowedNetworks
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property changeMessagePrompt (base name: "change_message_prompt")', function() {
      // uncomment below and update the code to test the property changeMessagePrompt
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property displayRecentChangesGraphs (base name: "display_recent_changes_graphs")', function() {
      // uncomment below and update the code to test the property displayRecentChangesGraphs
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableChangeMessage (base name: "enable_change_message")', function() {
      // uncomment below and update the code to test the property enableChangeMessage
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableChangeRequest (base name: "enable_change_request")', function() {
      // uncomment below and update the code to test the property enableChangeRequest
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableJavascriptDirectives (base name: "enable_javascript_directives")', function() {
      // uncomment below and update the code to test the property enableJavascriptDirectives
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableSelfDeployment (base name: "enable_self_deployment")', function() {
      // uncomment below and update the code to test the property enableSelfDeployment
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableSelfValidation (base name: "enable_self_validation")', function() {
      // uncomment below and update the code to test the property enableSelfValidation
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property firstRunHour (base name: "first_run_hour")', function() {
      // uncomment below and update the code to test the property firstRunHour
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property firstRunMinute (base name: "first_run_minute")', function() {
      // uncomment below and update the code to test the property firstRunMinute
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property globalPolicyMode (base name: "global_policy_mode")', function() {
      // uncomment below and update the code to test the property globalPolicyMode
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property globalPolicyModeOverridable (base name: "global_policy_mode_overridable")', function() {
      // uncomment below and update the code to test the property globalPolicyModeOverridable
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property heartbeatFrequency (base name: "heartbeat_frequency")', function() {
      // uncomment below and update the code to test the property heartbeatFrequency
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property mandatoryChangeMessage (base name: "mandatory_change_message")', function() {
      // uncomment below and update the code to test the property mandatoryChangeMessage
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property modifiedFileTtl (base name: "modified_file_ttl")', function() {
      // uncomment below and update the code to test the property modifiedFileTtl
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property nodeAcceptDuplicatedHostname (base name: "node_accept_duplicated_hostname")', function() {
      // uncomment below and update the code to test the property nodeAcceptDuplicatedHostname
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property nodeOnacceptDefaultPolicyMode (base name: "node_onaccept_default_policyMode")', function() {
      // uncomment below and update the code to test the property nodeOnacceptDefaultPolicyMode
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property nodeOnacceptDefaultState (base name: "node_onaccept_default_state")', function() {
      // uncomment below and update the code to test the property nodeOnacceptDefaultState
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property outputFileTtl (base name: "output_file_ttl")', function() {
      // uncomment below and update the code to test the property outputFileTtl
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property relayServerSynchronizationMethod (base name: "relay_server_synchronization_method")', function() {
      // uncomment below and update the code to test the property relayServerSynchronizationMethod
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property relayServerSynchronizePolicies (base name: "relay_server_synchronize_policies")', function() {
      // uncomment below and update the code to test the property relayServerSynchronizePolicies
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property relayServerSynchronizeSharedFiles (base name: "relay_server_synchronize_shared_files")', function() {
      // uncomment below and update the code to test the property relayServerSynchronizeSharedFiles
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property reportingMode (base name: "reporting_mode")', function() {
      // uncomment below and update the code to test the property reportingMode
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property requireTimeSynchronization (base name: "require_time_synchronization")', function() {
      // uncomment below and update the code to test the property requireTimeSynchronization
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderComputeChanges (base name: "rudder_compute_changes")', function() {
      // uncomment below and update the code to test the property rudderComputeChanges
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderComputeDyngroupsMaxParallelism (base name: "rudder_compute_dyngroups_max_parallelism")', function() {
      // uncomment below and update the code to test the property rudderComputeDyngroupsMaxParallelism
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderGenerationComputeDyngroups (base name: "rudder_generation_compute_dyngroups")', function() {
      // uncomment below and update the code to test the property rudderGenerationComputeDyngroups
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderGenerationContinueOnError (base name: "rudder_generation_continue_on_error")', function() {
      // uncomment below and update the code to test the property rudderGenerationContinueOnError
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderGenerationDelay (base name: "rudder_generation_delay")', function() {
      // uncomment below and update the code to test the property rudderGenerationDelay
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderGenerationJsTimeout (base name: "rudder_generation_js_timeout")', function() {
      // uncomment below and update the code to test the property rudderGenerationJsTimeout
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderGenerationMaxParallelism (base name: "rudder_generation_max_parallelism")', function() {
      // uncomment below and update the code to test the property rudderGenerationMaxParallelism
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderGenerationPolicy (base name: "rudder_generation_policy")', function() {
      // uncomment below and update the code to test the property rudderGenerationPolicy
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderReportProtocolDefault (base name: "rudder_report_protocol_default")', function() {
      // uncomment below and update the code to test the property rudderReportProtocolDefault
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderSaveDbComplianceDetails (base name: "rudder_save_db_compliance_details")', function() {
      // uncomment below and update the code to test the property rudderSaveDbComplianceDetails
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderSaveDbComplianceLevels (base name: "rudder_save_db_compliance_levels")', function() {
      // uncomment below and update the code to test the property rudderSaveDbComplianceLevels
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property rudderVerifyCertificates (base name: "rudder_verify_certificates")', function() {
      // uncomment below and update the code to test the property rudderVerifyCertificates
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property runFrequency (base name: "run_frequency")', function() {
      // uncomment below and update the code to test the property runFrequency
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property sendMetrics (base name: "send_metrics")', function() {
      // uncomment below and update the code to test the property sendMetrics
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property splayTime (base name: "splay_time")', function() {
      // uncomment below and update the code to test the property splayTime
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

    it('should have the property unexpectedUnboundVarValues (base name: "unexpected_unbound_var_values")', function() {
      // uncomment below and update the code to test the property unexpectedUnboundVarValues
      //var instance = new RudderApi.GetAllSettings200ResponseDataSettings();
      //expect(instance).to.be();
    });

  });

}));
