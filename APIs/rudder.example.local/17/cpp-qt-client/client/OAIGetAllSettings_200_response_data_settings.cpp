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
 */

#include "OAIGetAllSettings_200_response_data_settings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetAllSettings_200_response_data_settings::OAIGetAllSettings_200_response_data_settings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetAllSettings_200_response_data_settings::OAIGetAllSettings_200_response_data_settings() {
    this->initializeModel();
}

OAIGetAllSettings_200_response_data_settings::~OAIGetAllSettings_200_response_data_settings() {}

void OAIGetAllSettings_200_response_data_settings::initializeModel() {

    m_allowed_networks_isSet = false;
    m_allowed_networks_isValid = false;

    m_change_message_prompt_isSet = false;
    m_change_message_prompt_isValid = false;

    m_display_recent_changes_graphs_isSet = false;
    m_display_recent_changes_graphs_isValid = false;

    m_enable_change_message_isSet = false;
    m_enable_change_message_isValid = false;

    m_enable_change_request_isSet = false;
    m_enable_change_request_isValid = false;

    m_enable_javascript_directives_isSet = false;
    m_enable_javascript_directives_isValid = false;

    m_enable_self_deployment_isSet = false;
    m_enable_self_deployment_isValid = false;

    m_enable_self_validation_isSet = false;
    m_enable_self_validation_isValid = false;

    m_first_run_hour_isSet = false;
    m_first_run_hour_isValid = false;

    m_first_run_minute_isSet = false;
    m_first_run_minute_isValid = false;

    m_global_policy_mode_isSet = false;
    m_global_policy_mode_isValid = false;

    m_global_policy_mode_overridable_isSet = false;
    m_global_policy_mode_overridable_isValid = false;

    m_heartbeat_frequency_isSet = false;
    m_heartbeat_frequency_isValid = false;

    m_mandatory_change_message_isSet = false;
    m_mandatory_change_message_isValid = false;

    m_modified_file_ttl_isSet = false;
    m_modified_file_ttl_isValid = false;

    m_node_accept_duplicated_hostname_isSet = false;
    m_node_accept_duplicated_hostname_isValid = false;

    m_node_onaccept_default_policy_mode_isSet = false;
    m_node_onaccept_default_policy_mode_isValid = false;

    m_node_onaccept_default_state_isSet = false;
    m_node_onaccept_default_state_isValid = false;

    m_output_file_ttl_isSet = false;
    m_output_file_ttl_isValid = false;

    m_relay_server_synchronization_method_isSet = false;
    m_relay_server_synchronization_method_isValid = false;

    m_relay_server_synchronize_policies_isSet = false;
    m_relay_server_synchronize_policies_isValid = false;

    m_relay_server_synchronize_shared_files_isSet = false;
    m_relay_server_synchronize_shared_files_isValid = false;

    m_reporting_mode_isSet = false;
    m_reporting_mode_isValid = false;

    m_require_time_synchronization_isSet = false;
    m_require_time_synchronization_isValid = false;

    m_rudder_compute_changes_isSet = false;
    m_rudder_compute_changes_isValid = false;

    m_rudder_compute_dyngroups_max_parallelism_isSet = false;
    m_rudder_compute_dyngroups_max_parallelism_isValid = false;

    m_rudder_generation_compute_dyngroups_isSet = false;
    m_rudder_generation_compute_dyngroups_isValid = false;

    m_rudder_generation_continue_on_error_isSet = false;
    m_rudder_generation_continue_on_error_isValid = false;

    m_rudder_generation_delay_isSet = false;
    m_rudder_generation_delay_isValid = false;

    m_rudder_generation_js_timeout_isSet = false;
    m_rudder_generation_js_timeout_isValid = false;

    m_rudder_generation_max_parallelism_isSet = false;
    m_rudder_generation_max_parallelism_isValid = false;

    m_rudder_generation_policy_isSet = false;
    m_rudder_generation_policy_isValid = false;

    m_rudder_report_protocol_default_isSet = false;
    m_rudder_report_protocol_default_isValid = false;

    m_rudder_save_db_compliance_details_isSet = false;
    m_rudder_save_db_compliance_details_isValid = false;

    m_rudder_save_db_compliance_levels_isSet = false;
    m_rudder_save_db_compliance_levels_isValid = false;

    m_rudder_verify_certificates_isSet = false;
    m_rudder_verify_certificates_isValid = false;

    m_run_frequency_isSet = false;
    m_run_frequency_isValid = false;

    m_send_metrics_isSet = false;
    m_send_metrics_isValid = false;

    m_splay_time_isSet = false;
    m_splay_time_isValid = false;

    m_unexpected_unbound_var_values_isSet = false;
    m_unexpected_unbound_var_values_isValid = false;
}

void OAIGetAllSettings_200_response_data_settings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetAllSettings_200_response_data_settings::fromJsonObject(QJsonObject json) {

    m_allowed_networks_isValid = ::OpenAPI::fromJsonValue(m_allowed_networks, json[QString("allowed_networks")]);
    m_allowed_networks_isSet = !json[QString("allowed_networks")].isNull() && m_allowed_networks_isValid;

    m_change_message_prompt_isValid = ::OpenAPI::fromJsonValue(m_change_message_prompt, json[QString("change_message_prompt")]);
    m_change_message_prompt_isSet = !json[QString("change_message_prompt")].isNull() && m_change_message_prompt_isValid;

    m_display_recent_changes_graphs_isValid = ::OpenAPI::fromJsonValue(m_display_recent_changes_graphs, json[QString("display_recent_changes_graphs")]);
    m_display_recent_changes_graphs_isSet = !json[QString("display_recent_changes_graphs")].isNull() && m_display_recent_changes_graphs_isValid;

    m_enable_change_message_isValid = ::OpenAPI::fromJsonValue(m_enable_change_message, json[QString("enable_change_message")]);
    m_enable_change_message_isSet = !json[QString("enable_change_message")].isNull() && m_enable_change_message_isValid;

    m_enable_change_request_isValid = ::OpenAPI::fromJsonValue(m_enable_change_request, json[QString("enable_change_request")]);
    m_enable_change_request_isSet = !json[QString("enable_change_request")].isNull() && m_enable_change_request_isValid;

    m_enable_javascript_directives_isValid = ::OpenAPI::fromJsonValue(m_enable_javascript_directives, json[QString("enable_javascript_directives")]);
    m_enable_javascript_directives_isSet = !json[QString("enable_javascript_directives")].isNull() && m_enable_javascript_directives_isValid;

    m_enable_self_deployment_isValid = ::OpenAPI::fromJsonValue(m_enable_self_deployment, json[QString("enable_self_deployment")]);
    m_enable_self_deployment_isSet = !json[QString("enable_self_deployment")].isNull() && m_enable_self_deployment_isValid;

    m_enable_self_validation_isValid = ::OpenAPI::fromJsonValue(m_enable_self_validation, json[QString("enable_self_validation")]);
    m_enable_self_validation_isSet = !json[QString("enable_self_validation")].isNull() && m_enable_self_validation_isValid;

    m_first_run_hour_isValid = ::OpenAPI::fromJsonValue(m_first_run_hour, json[QString("first_run_hour")]);
    m_first_run_hour_isSet = !json[QString("first_run_hour")].isNull() && m_first_run_hour_isValid;

    m_first_run_minute_isValid = ::OpenAPI::fromJsonValue(m_first_run_minute, json[QString("first_run_minute")]);
    m_first_run_minute_isSet = !json[QString("first_run_minute")].isNull() && m_first_run_minute_isValid;

    m_global_policy_mode_isValid = ::OpenAPI::fromJsonValue(m_global_policy_mode, json[QString("global_policy_mode")]);
    m_global_policy_mode_isSet = !json[QString("global_policy_mode")].isNull() && m_global_policy_mode_isValid;

    m_global_policy_mode_overridable_isValid = ::OpenAPI::fromJsonValue(m_global_policy_mode_overridable, json[QString("global_policy_mode_overridable")]);
    m_global_policy_mode_overridable_isSet = !json[QString("global_policy_mode_overridable")].isNull() && m_global_policy_mode_overridable_isValid;

    m_heartbeat_frequency_isValid = ::OpenAPI::fromJsonValue(m_heartbeat_frequency, json[QString("heartbeat_frequency")]);
    m_heartbeat_frequency_isSet = !json[QString("heartbeat_frequency")].isNull() && m_heartbeat_frequency_isValid;

    m_mandatory_change_message_isValid = ::OpenAPI::fromJsonValue(m_mandatory_change_message, json[QString("mandatory_change_message")]);
    m_mandatory_change_message_isSet = !json[QString("mandatory_change_message")].isNull() && m_mandatory_change_message_isValid;

    m_modified_file_ttl_isValid = ::OpenAPI::fromJsonValue(m_modified_file_ttl, json[QString("modified_file_ttl")]);
    m_modified_file_ttl_isSet = !json[QString("modified_file_ttl")].isNull() && m_modified_file_ttl_isValid;

    m_node_accept_duplicated_hostname_isValid = ::OpenAPI::fromJsonValue(m_node_accept_duplicated_hostname, json[QString("node_accept_duplicated_hostname")]);
    m_node_accept_duplicated_hostname_isSet = !json[QString("node_accept_duplicated_hostname")].isNull() && m_node_accept_duplicated_hostname_isValid;

    m_node_onaccept_default_policy_mode_isValid = ::OpenAPI::fromJsonValue(m_node_onaccept_default_policy_mode, json[QString("node_onaccept_default_policyMode")]);
    m_node_onaccept_default_policy_mode_isSet = !json[QString("node_onaccept_default_policyMode")].isNull() && m_node_onaccept_default_policy_mode_isValid;

    m_node_onaccept_default_state_isValid = ::OpenAPI::fromJsonValue(m_node_onaccept_default_state, json[QString("node_onaccept_default_state")]);
    m_node_onaccept_default_state_isSet = !json[QString("node_onaccept_default_state")].isNull() && m_node_onaccept_default_state_isValid;

    m_output_file_ttl_isValid = ::OpenAPI::fromJsonValue(m_output_file_ttl, json[QString("output_file_ttl")]);
    m_output_file_ttl_isSet = !json[QString("output_file_ttl")].isNull() && m_output_file_ttl_isValid;

    m_relay_server_synchronization_method_isValid = ::OpenAPI::fromJsonValue(m_relay_server_synchronization_method, json[QString("relay_server_synchronization_method")]);
    m_relay_server_synchronization_method_isSet = !json[QString("relay_server_synchronization_method")].isNull() && m_relay_server_synchronization_method_isValid;

    m_relay_server_synchronize_policies_isValid = ::OpenAPI::fromJsonValue(m_relay_server_synchronize_policies, json[QString("relay_server_synchronize_policies")]);
    m_relay_server_synchronize_policies_isSet = !json[QString("relay_server_synchronize_policies")].isNull() && m_relay_server_synchronize_policies_isValid;

    m_relay_server_synchronize_shared_files_isValid = ::OpenAPI::fromJsonValue(m_relay_server_synchronize_shared_files, json[QString("relay_server_synchronize_shared_files")]);
    m_relay_server_synchronize_shared_files_isSet = !json[QString("relay_server_synchronize_shared_files")].isNull() && m_relay_server_synchronize_shared_files_isValid;

    m_reporting_mode_isValid = ::OpenAPI::fromJsonValue(m_reporting_mode, json[QString("reporting_mode")]);
    m_reporting_mode_isSet = !json[QString("reporting_mode")].isNull() && m_reporting_mode_isValid;

    m_require_time_synchronization_isValid = ::OpenAPI::fromJsonValue(m_require_time_synchronization, json[QString("require_time_synchronization")]);
    m_require_time_synchronization_isSet = !json[QString("require_time_synchronization")].isNull() && m_require_time_synchronization_isValid;

    m_rudder_compute_changes_isValid = ::OpenAPI::fromJsonValue(m_rudder_compute_changes, json[QString("rudder_compute_changes")]);
    m_rudder_compute_changes_isSet = !json[QString("rudder_compute_changes")].isNull() && m_rudder_compute_changes_isValid;

    m_rudder_compute_dyngroups_max_parallelism_isValid = ::OpenAPI::fromJsonValue(m_rudder_compute_dyngroups_max_parallelism, json[QString("rudder_compute_dyngroups_max_parallelism")]);
    m_rudder_compute_dyngroups_max_parallelism_isSet = !json[QString("rudder_compute_dyngroups_max_parallelism")].isNull() && m_rudder_compute_dyngroups_max_parallelism_isValid;

    m_rudder_generation_compute_dyngroups_isValid = ::OpenAPI::fromJsonValue(m_rudder_generation_compute_dyngroups, json[QString("rudder_generation_compute_dyngroups")]);
    m_rudder_generation_compute_dyngroups_isSet = !json[QString("rudder_generation_compute_dyngroups")].isNull() && m_rudder_generation_compute_dyngroups_isValid;

    m_rudder_generation_continue_on_error_isValid = ::OpenAPI::fromJsonValue(m_rudder_generation_continue_on_error, json[QString("rudder_generation_continue_on_error")]);
    m_rudder_generation_continue_on_error_isSet = !json[QString("rudder_generation_continue_on_error")].isNull() && m_rudder_generation_continue_on_error_isValid;

    m_rudder_generation_delay_isValid = ::OpenAPI::fromJsonValue(m_rudder_generation_delay, json[QString("rudder_generation_delay")]);
    m_rudder_generation_delay_isSet = !json[QString("rudder_generation_delay")].isNull() && m_rudder_generation_delay_isValid;

    m_rudder_generation_js_timeout_isValid = ::OpenAPI::fromJsonValue(m_rudder_generation_js_timeout, json[QString("rudder_generation_js_timeout")]);
    m_rudder_generation_js_timeout_isSet = !json[QString("rudder_generation_js_timeout")].isNull() && m_rudder_generation_js_timeout_isValid;

    m_rudder_generation_max_parallelism_isValid = ::OpenAPI::fromJsonValue(m_rudder_generation_max_parallelism, json[QString("rudder_generation_max_parallelism")]);
    m_rudder_generation_max_parallelism_isSet = !json[QString("rudder_generation_max_parallelism")].isNull() && m_rudder_generation_max_parallelism_isValid;

    m_rudder_generation_policy_isValid = ::OpenAPI::fromJsonValue(m_rudder_generation_policy, json[QString("rudder_generation_policy")]);
    m_rudder_generation_policy_isSet = !json[QString("rudder_generation_policy")].isNull() && m_rudder_generation_policy_isValid;

    m_rudder_report_protocol_default_isValid = ::OpenAPI::fromJsonValue(m_rudder_report_protocol_default, json[QString("rudder_report_protocol_default")]);
    m_rudder_report_protocol_default_isSet = !json[QString("rudder_report_protocol_default")].isNull() && m_rudder_report_protocol_default_isValid;

    m_rudder_save_db_compliance_details_isValid = ::OpenAPI::fromJsonValue(m_rudder_save_db_compliance_details, json[QString("rudder_save_db_compliance_details")]);
    m_rudder_save_db_compliance_details_isSet = !json[QString("rudder_save_db_compliance_details")].isNull() && m_rudder_save_db_compliance_details_isValid;

    m_rudder_save_db_compliance_levels_isValid = ::OpenAPI::fromJsonValue(m_rudder_save_db_compliance_levels, json[QString("rudder_save_db_compliance_levels")]);
    m_rudder_save_db_compliance_levels_isSet = !json[QString("rudder_save_db_compliance_levels")].isNull() && m_rudder_save_db_compliance_levels_isValid;

    m_rudder_verify_certificates_isValid = ::OpenAPI::fromJsonValue(m_rudder_verify_certificates, json[QString("rudder_verify_certificates")]);
    m_rudder_verify_certificates_isSet = !json[QString("rudder_verify_certificates")].isNull() && m_rudder_verify_certificates_isValid;

    m_run_frequency_isValid = ::OpenAPI::fromJsonValue(m_run_frequency, json[QString("run_frequency")]);
    m_run_frequency_isSet = !json[QString("run_frequency")].isNull() && m_run_frequency_isValid;

    m_send_metrics_isValid = ::OpenAPI::fromJsonValue(m_send_metrics, json[QString("send_metrics")]);
    m_send_metrics_isSet = !json[QString("send_metrics")].isNull() && m_send_metrics_isValid;

    m_splay_time_isValid = ::OpenAPI::fromJsonValue(m_splay_time, json[QString("splay_time")]);
    m_splay_time_isSet = !json[QString("splay_time")].isNull() && m_splay_time_isValid;

    m_unexpected_unbound_var_values_isValid = ::OpenAPI::fromJsonValue(m_unexpected_unbound_var_values, json[QString("unexpected_unbound_var_values")]);
    m_unexpected_unbound_var_values_isSet = !json[QString("unexpected_unbound_var_values")].isNull() && m_unexpected_unbound_var_values_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetAllSettings_200_response_data_settings::asJsonObject() const {
    QJsonObject obj;
    if (m_allowed_networks.size() > 0) {
        obj.insert(QString("allowed_networks"), ::OpenAPI::toJsonValue(m_allowed_networks));
    }
    if (m_change_message_prompt_isSet) {
        obj.insert(QString("change_message_prompt"), ::OpenAPI::toJsonValue(m_change_message_prompt));
    }
    if (m_display_recent_changes_graphs_isSet) {
        obj.insert(QString("display_recent_changes_graphs"), ::OpenAPI::toJsonValue(m_display_recent_changes_graphs));
    }
    if (m_enable_change_message_isSet) {
        obj.insert(QString("enable_change_message"), ::OpenAPI::toJsonValue(m_enable_change_message));
    }
    if (m_enable_change_request_isSet) {
        obj.insert(QString("enable_change_request"), ::OpenAPI::toJsonValue(m_enable_change_request));
    }
    if (m_enable_javascript_directives_isSet) {
        obj.insert(QString("enable_javascript_directives"), ::OpenAPI::toJsonValue(m_enable_javascript_directives));
    }
    if (m_enable_self_deployment_isSet) {
        obj.insert(QString("enable_self_deployment"), ::OpenAPI::toJsonValue(m_enable_self_deployment));
    }
    if (m_enable_self_validation_isSet) {
        obj.insert(QString("enable_self_validation"), ::OpenAPI::toJsonValue(m_enable_self_validation));
    }
    if (m_first_run_hour_isSet) {
        obj.insert(QString("first_run_hour"), ::OpenAPI::toJsonValue(m_first_run_hour));
    }
    if (m_first_run_minute_isSet) {
        obj.insert(QString("first_run_minute"), ::OpenAPI::toJsonValue(m_first_run_minute));
    }
    if (m_global_policy_mode_isSet) {
        obj.insert(QString("global_policy_mode"), ::OpenAPI::toJsonValue(m_global_policy_mode));
    }
    if (m_global_policy_mode_overridable_isSet) {
        obj.insert(QString("global_policy_mode_overridable"), ::OpenAPI::toJsonValue(m_global_policy_mode_overridable));
    }
    if (m_heartbeat_frequency_isSet) {
        obj.insert(QString("heartbeat_frequency"), ::OpenAPI::toJsonValue(m_heartbeat_frequency));
    }
    if (m_mandatory_change_message_isSet) {
        obj.insert(QString("mandatory_change_message"), ::OpenAPI::toJsonValue(m_mandatory_change_message));
    }
    if (m_modified_file_ttl_isSet) {
        obj.insert(QString("modified_file_ttl"), ::OpenAPI::toJsonValue(m_modified_file_ttl));
    }
    if (m_node_accept_duplicated_hostname_isSet) {
        obj.insert(QString("node_accept_duplicated_hostname"), ::OpenAPI::toJsonValue(m_node_accept_duplicated_hostname));
    }
    if (m_node_onaccept_default_policy_mode_isSet) {
        obj.insert(QString("node_onaccept_default_policyMode"), ::OpenAPI::toJsonValue(m_node_onaccept_default_policy_mode));
    }
    if (m_node_onaccept_default_state_isSet) {
        obj.insert(QString("node_onaccept_default_state"), ::OpenAPI::toJsonValue(m_node_onaccept_default_state));
    }
    if (m_output_file_ttl_isSet) {
        obj.insert(QString("output_file_ttl"), ::OpenAPI::toJsonValue(m_output_file_ttl));
    }
    if (m_relay_server_synchronization_method_isSet) {
        obj.insert(QString("relay_server_synchronization_method"), ::OpenAPI::toJsonValue(m_relay_server_synchronization_method));
    }
    if (m_relay_server_synchronize_policies_isSet) {
        obj.insert(QString("relay_server_synchronize_policies"), ::OpenAPI::toJsonValue(m_relay_server_synchronize_policies));
    }
    if (m_relay_server_synchronize_shared_files_isSet) {
        obj.insert(QString("relay_server_synchronize_shared_files"), ::OpenAPI::toJsonValue(m_relay_server_synchronize_shared_files));
    }
    if (m_reporting_mode_isSet) {
        obj.insert(QString("reporting_mode"), ::OpenAPI::toJsonValue(m_reporting_mode));
    }
    if (m_require_time_synchronization_isSet) {
        obj.insert(QString("require_time_synchronization"), ::OpenAPI::toJsonValue(m_require_time_synchronization));
    }
    if (m_rudder_compute_changes_isSet) {
        obj.insert(QString("rudder_compute_changes"), ::OpenAPI::toJsonValue(m_rudder_compute_changes));
    }
    if (m_rudder_compute_dyngroups_max_parallelism_isSet) {
        obj.insert(QString("rudder_compute_dyngroups_max_parallelism"), ::OpenAPI::toJsonValue(m_rudder_compute_dyngroups_max_parallelism));
    }
    if (m_rudder_generation_compute_dyngroups_isSet) {
        obj.insert(QString("rudder_generation_compute_dyngroups"), ::OpenAPI::toJsonValue(m_rudder_generation_compute_dyngroups));
    }
    if (m_rudder_generation_continue_on_error_isSet) {
        obj.insert(QString("rudder_generation_continue_on_error"), ::OpenAPI::toJsonValue(m_rudder_generation_continue_on_error));
    }
    if (m_rudder_generation_delay_isSet) {
        obj.insert(QString("rudder_generation_delay"), ::OpenAPI::toJsonValue(m_rudder_generation_delay));
    }
    if (m_rudder_generation_js_timeout_isSet) {
        obj.insert(QString("rudder_generation_js_timeout"), ::OpenAPI::toJsonValue(m_rudder_generation_js_timeout));
    }
    if (m_rudder_generation_max_parallelism_isSet) {
        obj.insert(QString("rudder_generation_max_parallelism"), ::OpenAPI::toJsonValue(m_rudder_generation_max_parallelism));
    }
    if (m_rudder_generation_policy_isSet) {
        obj.insert(QString("rudder_generation_policy"), ::OpenAPI::toJsonValue(m_rudder_generation_policy));
    }
    if (m_rudder_report_protocol_default_isSet) {
        obj.insert(QString("rudder_report_protocol_default"), ::OpenAPI::toJsonValue(m_rudder_report_protocol_default));
    }
    if (m_rudder_save_db_compliance_details_isSet) {
        obj.insert(QString("rudder_save_db_compliance_details"), ::OpenAPI::toJsonValue(m_rudder_save_db_compliance_details));
    }
    if (m_rudder_save_db_compliance_levels_isSet) {
        obj.insert(QString("rudder_save_db_compliance_levels"), ::OpenAPI::toJsonValue(m_rudder_save_db_compliance_levels));
    }
    if (m_rudder_verify_certificates_isSet) {
        obj.insert(QString("rudder_verify_certificates"), ::OpenAPI::toJsonValue(m_rudder_verify_certificates));
    }
    if (m_run_frequency_isSet) {
        obj.insert(QString("run_frequency"), ::OpenAPI::toJsonValue(m_run_frequency));
    }
    if (m_send_metrics_isSet) {
        obj.insert(QString("send_metrics"), ::OpenAPI::toJsonValue(m_send_metrics));
    }
    if (m_splay_time_isSet) {
        obj.insert(QString("splay_time"), ::OpenAPI::toJsonValue(m_splay_time));
    }
    if (m_unexpected_unbound_var_values_isSet) {
        obj.insert(QString("unexpected_unbound_var_values"), ::OpenAPI::toJsonValue(m_unexpected_unbound_var_values));
    }
    return obj;
}

QList<OAIGetAllSettings_200_response_data_settings_allowed_networks_inner> OAIGetAllSettings_200_response_data_settings::getAllowedNetworks() const {
    return m_allowed_networks;
}
void OAIGetAllSettings_200_response_data_settings::setAllowedNetworks(const QList<OAIGetAllSettings_200_response_data_settings_allowed_networks_inner> &allowed_networks) {
    m_allowed_networks = allowed_networks;
    m_allowed_networks_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_allowed_networks_Set() const{
    return m_allowed_networks_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_allowed_networks_Valid() const{
    return m_allowed_networks_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getChangeMessagePrompt() const {
    return m_change_message_prompt;
}
void OAIGetAllSettings_200_response_data_settings::setChangeMessagePrompt(const QString &change_message_prompt) {
    m_change_message_prompt = change_message_prompt;
    m_change_message_prompt_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_change_message_prompt_Set() const{
    return m_change_message_prompt_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_change_message_prompt_Valid() const{
    return m_change_message_prompt_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isDisplayRecentChangesGraphs() const {
    return m_display_recent_changes_graphs;
}
void OAIGetAllSettings_200_response_data_settings::setDisplayRecentChangesGraphs(const bool &display_recent_changes_graphs) {
    m_display_recent_changes_graphs = display_recent_changes_graphs;
    m_display_recent_changes_graphs_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_display_recent_changes_graphs_Set() const{
    return m_display_recent_changes_graphs_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_display_recent_changes_graphs_Valid() const{
    return m_display_recent_changes_graphs_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isEnableChangeMessage() const {
    return m_enable_change_message;
}
void OAIGetAllSettings_200_response_data_settings::setEnableChangeMessage(const bool &enable_change_message) {
    m_enable_change_message = enable_change_message;
    m_enable_change_message_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_change_message_Set() const{
    return m_enable_change_message_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_change_message_Valid() const{
    return m_enable_change_message_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isEnableChangeRequest() const {
    return m_enable_change_request;
}
void OAIGetAllSettings_200_response_data_settings::setEnableChangeRequest(const bool &enable_change_request) {
    m_enable_change_request = enable_change_request;
    m_enable_change_request_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_change_request_Set() const{
    return m_enable_change_request_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_change_request_Valid() const{
    return m_enable_change_request_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getEnableJavascriptDirectives() const {
    return m_enable_javascript_directives;
}
void OAIGetAllSettings_200_response_data_settings::setEnableJavascriptDirectives(const QString &enable_javascript_directives) {
    m_enable_javascript_directives = enable_javascript_directives;
    m_enable_javascript_directives_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_javascript_directives_Set() const{
    return m_enable_javascript_directives_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_javascript_directives_Valid() const{
    return m_enable_javascript_directives_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isEnableSelfDeployment() const {
    return m_enable_self_deployment;
}
void OAIGetAllSettings_200_response_data_settings::setEnableSelfDeployment(const bool &enable_self_deployment) {
    m_enable_self_deployment = enable_self_deployment;
    m_enable_self_deployment_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_self_deployment_Set() const{
    return m_enable_self_deployment_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_self_deployment_Valid() const{
    return m_enable_self_deployment_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isEnableSelfValidation() const {
    return m_enable_self_validation;
}
void OAIGetAllSettings_200_response_data_settings::setEnableSelfValidation(const bool &enable_self_validation) {
    m_enable_self_validation = enable_self_validation;
    m_enable_self_validation_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_self_validation_Set() const{
    return m_enable_self_validation_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_enable_self_validation_Valid() const{
    return m_enable_self_validation_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getFirstRunHour() const {
    return m_first_run_hour;
}
void OAIGetAllSettings_200_response_data_settings::setFirstRunHour(const qint32 &first_run_hour) {
    m_first_run_hour = first_run_hour;
    m_first_run_hour_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_first_run_hour_Set() const{
    return m_first_run_hour_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_first_run_hour_Valid() const{
    return m_first_run_hour_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getFirstRunMinute() const {
    return m_first_run_minute;
}
void OAIGetAllSettings_200_response_data_settings::setFirstRunMinute(const qint32 &first_run_minute) {
    m_first_run_minute = first_run_minute;
    m_first_run_minute_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_first_run_minute_Set() const{
    return m_first_run_minute_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_first_run_minute_Valid() const{
    return m_first_run_minute_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getGlobalPolicyMode() const {
    return m_global_policy_mode;
}
void OAIGetAllSettings_200_response_data_settings::setGlobalPolicyMode(const QString &global_policy_mode) {
    m_global_policy_mode = global_policy_mode;
    m_global_policy_mode_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_global_policy_mode_Set() const{
    return m_global_policy_mode_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_global_policy_mode_Valid() const{
    return m_global_policy_mode_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isGlobalPolicyModeOverridable() const {
    return m_global_policy_mode_overridable;
}
void OAIGetAllSettings_200_response_data_settings::setGlobalPolicyModeOverridable(const bool &global_policy_mode_overridable) {
    m_global_policy_mode_overridable = global_policy_mode_overridable;
    m_global_policy_mode_overridable_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_global_policy_mode_overridable_Set() const{
    return m_global_policy_mode_overridable_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_global_policy_mode_overridable_Valid() const{
    return m_global_policy_mode_overridable_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getHeartbeatFrequency() const {
    return m_heartbeat_frequency;
}
void OAIGetAllSettings_200_response_data_settings::setHeartbeatFrequency(const qint32 &heartbeat_frequency) {
    m_heartbeat_frequency = heartbeat_frequency;
    m_heartbeat_frequency_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_heartbeat_frequency_Set() const{
    return m_heartbeat_frequency_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_heartbeat_frequency_Valid() const{
    return m_heartbeat_frequency_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isMandatoryChangeMessage() const {
    return m_mandatory_change_message;
}
void OAIGetAllSettings_200_response_data_settings::setMandatoryChangeMessage(const bool &mandatory_change_message) {
    m_mandatory_change_message = mandatory_change_message;
    m_mandatory_change_message_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_mandatory_change_message_Set() const{
    return m_mandatory_change_message_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_mandatory_change_message_Valid() const{
    return m_mandatory_change_message_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getModifiedFileTtl() const {
    return m_modified_file_ttl;
}
void OAIGetAllSettings_200_response_data_settings::setModifiedFileTtl(const qint32 &modified_file_ttl) {
    m_modified_file_ttl = modified_file_ttl;
    m_modified_file_ttl_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_modified_file_ttl_Set() const{
    return m_modified_file_ttl_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_modified_file_ttl_Valid() const{
    return m_modified_file_ttl_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isNodeAcceptDuplicatedHostname() const {
    return m_node_accept_duplicated_hostname;
}
void OAIGetAllSettings_200_response_data_settings::setNodeAcceptDuplicatedHostname(const bool &node_accept_duplicated_hostname) {
    m_node_accept_duplicated_hostname = node_accept_duplicated_hostname;
    m_node_accept_duplicated_hostname_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_node_accept_duplicated_hostname_Set() const{
    return m_node_accept_duplicated_hostname_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_node_accept_duplicated_hostname_Valid() const{
    return m_node_accept_duplicated_hostname_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getNodeOnacceptDefaultPolicyMode() const {
    return m_node_onaccept_default_policy_mode;
}
void OAIGetAllSettings_200_response_data_settings::setNodeOnacceptDefaultPolicyMode(const QString &node_onaccept_default_policy_mode) {
    m_node_onaccept_default_policy_mode = node_onaccept_default_policy_mode;
    m_node_onaccept_default_policy_mode_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_node_onaccept_default_policy_mode_Set() const{
    return m_node_onaccept_default_policy_mode_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_node_onaccept_default_policy_mode_Valid() const{
    return m_node_onaccept_default_policy_mode_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getNodeOnacceptDefaultState() const {
    return m_node_onaccept_default_state;
}
void OAIGetAllSettings_200_response_data_settings::setNodeOnacceptDefaultState(const QString &node_onaccept_default_state) {
    m_node_onaccept_default_state = node_onaccept_default_state;
    m_node_onaccept_default_state_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_node_onaccept_default_state_Set() const{
    return m_node_onaccept_default_state_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_node_onaccept_default_state_Valid() const{
    return m_node_onaccept_default_state_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getOutputFileTtl() const {
    return m_output_file_ttl;
}
void OAIGetAllSettings_200_response_data_settings::setOutputFileTtl(const qint32 &output_file_ttl) {
    m_output_file_ttl = output_file_ttl;
    m_output_file_ttl_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_output_file_ttl_Set() const{
    return m_output_file_ttl_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_output_file_ttl_Valid() const{
    return m_output_file_ttl_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getRelayServerSynchronizationMethod() const {
    return m_relay_server_synchronization_method;
}
void OAIGetAllSettings_200_response_data_settings::setRelayServerSynchronizationMethod(const QString &relay_server_synchronization_method) {
    m_relay_server_synchronization_method = relay_server_synchronization_method;
    m_relay_server_synchronization_method_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_relay_server_synchronization_method_Set() const{
    return m_relay_server_synchronization_method_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_relay_server_synchronization_method_Valid() const{
    return m_relay_server_synchronization_method_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRelayServerSynchronizePolicies() const {
    return m_relay_server_synchronize_policies;
}
void OAIGetAllSettings_200_response_data_settings::setRelayServerSynchronizePolicies(const bool &relay_server_synchronize_policies) {
    m_relay_server_synchronize_policies = relay_server_synchronize_policies;
    m_relay_server_synchronize_policies_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_relay_server_synchronize_policies_Set() const{
    return m_relay_server_synchronize_policies_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_relay_server_synchronize_policies_Valid() const{
    return m_relay_server_synchronize_policies_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRelayServerSynchronizeSharedFiles() const {
    return m_relay_server_synchronize_shared_files;
}
void OAIGetAllSettings_200_response_data_settings::setRelayServerSynchronizeSharedFiles(const bool &relay_server_synchronize_shared_files) {
    m_relay_server_synchronize_shared_files = relay_server_synchronize_shared_files;
    m_relay_server_synchronize_shared_files_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_relay_server_synchronize_shared_files_Set() const{
    return m_relay_server_synchronize_shared_files_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_relay_server_synchronize_shared_files_Valid() const{
    return m_relay_server_synchronize_shared_files_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getReportingMode() const {
    return m_reporting_mode;
}
void OAIGetAllSettings_200_response_data_settings::setReportingMode(const QString &reporting_mode) {
    m_reporting_mode = reporting_mode;
    m_reporting_mode_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_reporting_mode_Set() const{
    return m_reporting_mode_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_reporting_mode_Valid() const{
    return m_reporting_mode_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRequireTimeSynchronization() const {
    return m_require_time_synchronization;
}
void OAIGetAllSettings_200_response_data_settings::setRequireTimeSynchronization(const bool &require_time_synchronization) {
    m_require_time_synchronization = require_time_synchronization;
    m_require_time_synchronization_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_require_time_synchronization_Set() const{
    return m_require_time_synchronization_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_require_time_synchronization_Valid() const{
    return m_require_time_synchronization_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRudderComputeChanges() const {
    return m_rudder_compute_changes;
}
void OAIGetAllSettings_200_response_data_settings::setRudderComputeChanges(const bool &rudder_compute_changes) {
    m_rudder_compute_changes = rudder_compute_changes;
    m_rudder_compute_changes_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_compute_changes_Set() const{
    return m_rudder_compute_changes_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_compute_changes_Valid() const{
    return m_rudder_compute_changes_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getRudderComputeDyngroupsMaxParallelism() const {
    return m_rudder_compute_dyngroups_max_parallelism;
}
void OAIGetAllSettings_200_response_data_settings::setRudderComputeDyngroupsMaxParallelism(const QString &rudder_compute_dyngroups_max_parallelism) {
    m_rudder_compute_dyngroups_max_parallelism = rudder_compute_dyngroups_max_parallelism;
    m_rudder_compute_dyngroups_max_parallelism_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_compute_dyngroups_max_parallelism_Set() const{
    return m_rudder_compute_dyngroups_max_parallelism_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_compute_dyngroups_max_parallelism_Valid() const{
    return m_rudder_compute_dyngroups_max_parallelism_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRudderGenerationComputeDyngroups() const {
    return m_rudder_generation_compute_dyngroups;
}
void OAIGetAllSettings_200_response_data_settings::setRudderGenerationComputeDyngroups(const bool &rudder_generation_compute_dyngroups) {
    m_rudder_generation_compute_dyngroups = rudder_generation_compute_dyngroups;
    m_rudder_generation_compute_dyngroups_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_compute_dyngroups_Set() const{
    return m_rudder_generation_compute_dyngroups_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_compute_dyngroups_Valid() const{
    return m_rudder_generation_compute_dyngroups_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRudderGenerationContinueOnError() const {
    return m_rudder_generation_continue_on_error;
}
void OAIGetAllSettings_200_response_data_settings::setRudderGenerationContinueOnError(const bool &rudder_generation_continue_on_error) {
    m_rudder_generation_continue_on_error = rudder_generation_continue_on_error;
    m_rudder_generation_continue_on_error_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_continue_on_error_Set() const{
    return m_rudder_generation_continue_on_error_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_continue_on_error_Valid() const{
    return m_rudder_generation_continue_on_error_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getRudderGenerationDelay() const {
    return m_rudder_generation_delay;
}
void OAIGetAllSettings_200_response_data_settings::setRudderGenerationDelay(const QString &rudder_generation_delay) {
    m_rudder_generation_delay = rudder_generation_delay;
    m_rudder_generation_delay_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_delay_Set() const{
    return m_rudder_generation_delay_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_delay_Valid() const{
    return m_rudder_generation_delay_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getRudderGenerationJsTimeout() const {
    return m_rudder_generation_js_timeout;
}
void OAIGetAllSettings_200_response_data_settings::setRudderGenerationJsTimeout(const qint32 &rudder_generation_js_timeout) {
    m_rudder_generation_js_timeout = rudder_generation_js_timeout;
    m_rudder_generation_js_timeout_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_js_timeout_Set() const{
    return m_rudder_generation_js_timeout_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_js_timeout_Valid() const{
    return m_rudder_generation_js_timeout_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getRudderGenerationMaxParallelism() const {
    return m_rudder_generation_max_parallelism;
}
void OAIGetAllSettings_200_response_data_settings::setRudderGenerationMaxParallelism(const QString &rudder_generation_max_parallelism) {
    m_rudder_generation_max_parallelism = rudder_generation_max_parallelism;
    m_rudder_generation_max_parallelism_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_max_parallelism_Set() const{
    return m_rudder_generation_max_parallelism_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_max_parallelism_Valid() const{
    return m_rudder_generation_max_parallelism_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getRudderGenerationPolicy() const {
    return m_rudder_generation_policy;
}
void OAIGetAllSettings_200_response_data_settings::setRudderGenerationPolicy(const QString &rudder_generation_policy) {
    m_rudder_generation_policy = rudder_generation_policy;
    m_rudder_generation_policy_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_policy_Set() const{
    return m_rudder_generation_policy_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_generation_policy_Valid() const{
    return m_rudder_generation_policy_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getRudderReportProtocolDefault() const {
    return m_rudder_report_protocol_default;
}
void OAIGetAllSettings_200_response_data_settings::setRudderReportProtocolDefault(const QString &rudder_report_protocol_default) {
    m_rudder_report_protocol_default = rudder_report_protocol_default;
    m_rudder_report_protocol_default_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_report_protocol_default_Set() const{
    return m_rudder_report_protocol_default_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_report_protocol_default_Valid() const{
    return m_rudder_report_protocol_default_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRudderSaveDbComplianceDetails() const {
    return m_rudder_save_db_compliance_details;
}
void OAIGetAllSettings_200_response_data_settings::setRudderSaveDbComplianceDetails(const bool &rudder_save_db_compliance_details) {
    m_rudder_save_db_compliance_details = rudder_save_db_compliance_details;
    m_rudder_save_db_compliance_details_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_save_db_compliance_details_Set() const{
    return m_rudder_save_db_compliance_details_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_save_db_compliance_details_Valid() const{
    return m_rudder_save_db_compliance_details_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRudderSaveDbComplianceLevels() const {
    return m_rudder_save_db_compliance_levels;
}
void OAIGetAllSettings_200_response_data_settings::setRudderSaveDbComplianceLevels(const bool &rudder_save_db_compliance_levels) {
    m_rudder_save_db_compliance_levels = rudder_save_db_compliance_levels;
    m_rudder_save_db_compliance_levels_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_save_db_compliance_levels_Set() const{
    return m_rudder_save_db_compliance_levels_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_save_db_compliance_levels_Valid() const{
    return m_rudder_save_db_compliance_levels_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isRudderVerifyCertificates() const {
    return m_rudder_verify_certificates;
}
void OAIGetAllSettings_200_response_data_settings::setRudderVerifyCertificates(const bool &rudder_verify_certificates) {
    m_rudder_verify_certificates = rudder_verify_certificates;
    m_rudder_verify_certificates_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_verify_certificates_Set() const{
    return m_rudder_verify_certificates_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_rudder_verify_certificates_Valid() const{
    return m_rudder_verify_certificates_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getRunFrequency() const {
    return m_run_frequency;
}
void OAIGetAllSettings_200_response_data_settings::setRunFrequency(const qint32 &run_frequency) {
    m_run_frequency = run_frequency;
    m_run_frequency_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_run_frequency_Set() const{
    return m_run_frequency_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_run_frequency_Valid() const{
    return m_run_frequency_isValid;
}

QString OAIGetAllSettings_200_response_data_settings::getSendMetrics() const {
    return m_send_metrics;
}
void OAIGetAllSettings_200_response_data_settings::setSendMetrics(const QString &send_metrics) {
    m_send_metrics = send_metrics;
    m_send_metrics_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_send_metrics_Set() const{
    return m_send_metrics_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_send_metrics_Valid() const{
    return m_send_metrics_isValid;
}

qint32 OAIGetAllSettings_200_response_data_settings::getSplayTime() const {
    return m_splay_time;
}
void OAIGetAllSettings_200_response_data_settings::setSplayTime(const qint32 &splay_time) {
    m_splay_time = splay_time;
    m_splay_time_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_splay_time_Set() const{
    return m_splay_time_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_splay_time_Valid() const{
    return m_splay_time_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isUnexpectedUnboundVarValues() const {
    return m_unexpected_unbound_var_values;
}
void OAIGetAllSettings_200_response_data_settings::setUnexpectedUnboundVarValues(const bool &unexpected_unbound_var_values) {
    m_unexpected_unbound_var_values = unexpected_unbound_var_values;
    m_unexpected_unbound_var_values_isSet = true;
}

bool OAIGetAllSettings_200_response_data_settings::is_unexpected_unbound_var_values_Set() const{
    return m_unexpected_unbound_var_values_isSet;
}

bool OAIGetAllSettings_200_response_data_settings::is_unexpected_unbound_var_values_Valid() const{
    return m_unexpected_unbound_var_values_isValid;
}

bool OAIGetAllSettings_200_response_data_settings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allowed_networks.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_change_message_prompt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_recent_changes_graphs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_change_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_change_request_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_javascript_directives_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_self_deployment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_self_validation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_run_hour_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_run_minute_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_policy_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_policy_mode_overridable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_heartbeat_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mandatory_change_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_file_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_node_accept_duplicated_hostname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_node_onaccept_default_policy_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_node_onaccept_default_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_file_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relay_server_synchronization_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relay_server_synchronize_policies_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relay_server_synchronize_shared_files_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reporting_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_require_time_synchronization_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_compute_changes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_compute_dyngroups_max_parallelism_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_generation_compute_dyngroups_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_generation_continue_on_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_generation_delay_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_generation_js_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_generation_max_parallelism_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_generation_policy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_report_protocol_default_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_save_db_compliance_details_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_save_db_compliance_levels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rudder_verify_certificates_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_run_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_send_metrics_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_splay_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unexpected_unbound_var_values_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetAllSettings_200_response_data_settings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
