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

/*
 * OAIGetAllSettings_200_response_data_settings.h
 *
 * 
 */

#ifndef OAIGetAllSettings_200_response_data_settings_H
#define OAIGetAllSettings_200_response_data_settings_H

#include <QJsonObject>

#include "OAIGetAllSettings_200_response_data_settings_allowed_networks_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetAllSettings_200_response_data_settings_allowed_networks_inner;

class OAIGetAllSettings_200_response_data_settings : public OAIObject {
public:
    OAIGetAllSettings_200_response_data_settings();
    OAIGetAllSettings_200_response_data_settings(QString json);
    ~OAIGetAllSettings_200_response_data_settings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIGetAllSettings_200_response_data_settings_allowed_networks_inner> getAllowedNetworks() const;
    void setAllowedNetworks(const QList<OAIGetAllSettings_200_response_data_settings_allowed_networks_inner> &allowed_networks);
    bool is_allowed_networks_Set() const;
    bool is_allowed_networks_Valid() const;

    QString getChangeMessagePrompt() const;
    void setChangeMessagePrompt(const QString &change_message_prompt);
    bool is_change_message_prompt_Set() const;
    bool is_change_message_prompt_Valid() const;

    bool isDisplayRecentChangesGraphs() const;
    void setDisplayRecentChangesGraphs(const bool &display_recent_changes_graphs);
    bool is_display_recent_changes_graphs_Set() const;
    bool is_display_recent_changes_graphs_Valid() const;

    bool isEnableChangeMessage() const;
    void setEnableChangeMessage(const bool &enable_change_message);
    bool is_enable_change_message_Set() const;
    bool is_enable_change_message_Valid() const;

    bool isEnableChangeRequest() const;
    void setEnableChangeRequest(const bool &enable_change_request);
    bool is_enable_change_request_Set() const;
    bool is_enable_change_request_Valid() const;

    QString getEnableJavascriptDirectives() const;
    void setEnableJavascriptDirectives(const QString &enable_javascript_directives);
    bool is_enable_javascript_directives_Set() const;
    bool is_enable_javascript_directives_Valid() const;

    bool isEnableSelfDeployment() const;
    void setEnableSelfDeployment(const bool &enable_self_deployment);
    bool is_enable_self_deployment_Set() const;
    bool is_enable_self_deployment_Valid() const;

    bool isEnableSelfValidation() const;
    void setEnableSelfValidation(const bool &enable_self_validation);
    bool is_enable_self_validation_Set() const;
    bool is_enable_self_validation_Valid() const;

    qint32 getFirstRunHour() const;
    void setFirstRunHour(const qint32 &first_run_hour);
    bool is_first_run_hour_Set() const;
    bool is_first_run_hour_Valid() const;

    qint32 getFirstRunMinute() const;
    void setFirstRunMinute(const qint32 &first_run_minute);
    bool is_first_run_minute_Set() const;
    bool is_first_run_minute_Valid() const;

    QString getGlobalPolicyMode() const;
    void setGlobalPolicyMode(const QString &global_policy_mode);
    bool is_global_policy_mode_Set() const;
    bool is_global_policy_mode_Valid() const;

    bool isGlobalPolicyModeOverridable() const;
    void setGlobalPolicyModeOverridable(const bool &global_policy_mode_overridable);
    bool is_global_policy_mode_overridable_Set() const;
    bool is_global_policy_mode_overridable_Valid() const;

    qint32 getHeartbeatFrequency() const;
    void setHeartbeatFrequency(const qint32 &heartbeat_frequency);
    bool is_heartbeat_frequency_Set() const;
    bool is_heartbeat_frequency_Valid() const;

    bool isMandatoryChangeMessage() const;
    void setMandatoryChangeMessage(const bool &mandatory_change_message);
    bool is_mandatory_change_message_Set() const;
    bool is_mandatory_change_message_Valid() const;

    qint32 getModifiedFileTtl() const;
    void setModifiedFileTtl(const qint32 &modified_file_ttl);
    bool is_modified_file_ttl_Set() const;
    bool is_modified_file_ttl_Valid() const;

    bool isNodeAcceptDuplicatedHostname() const;
    void setNodeAcceptDuplicatedHostname(const bool &node_accept_duplicated_hostname);
    bool is_node_accept_duplicated_hostname_Set() const;
    bool is_node_accept_duplicated_hostname_Valid() const;

    QString getNodeOnacceptDefaultPolicyMode() const;
    void setNodeOnacceptDefaultPolicyMode(const QString &node_onaccept_default_policy_mode);
    bool is_node_onaccept_default_policy_mode_Set() const;
    bool is_node_onaccept_default_policy_mode_Valid() const;

    QString getNodeOnacceptDefaultState() const;
    void setNodeOnacceptDefaultState(const QString &node_onaccept_default_state);
    bool is_node_onaccept_default_state_Set() const;
    bool is_node_onaccept_default_state_Valid() const;

    qint32 getOutputFileTtl() const;
    void setOutputFileTtl(const qint32 &output_file_ttl);
    bool is_output_file_ttl_Set() const;
    bool is_output_file_ttl_Valid() const;

    QString getRelayServerSynchronizationMethod() const;
    void setRelayServerSynchronizationMethod(const QString &relay_server_synchronization_method);
    bool is_relay_server_synchronization_method_Set() const;
    bool is_relay_server_synchronization_method_Valid() const;

    bool isRelayServerSynchronizePolicies() const;
    void setRelayServerSynchronizePolicies(const bool &relay_server_synchronize_policies);
    bool is_relay_server_synchronize_policies_Set() const;
    bool is_relay_server_synchronize_policies_Valid() const;

    bool isRelayServerSynchronizeSharedFiles() const;
    void setRelayServerSynchronizeSharedFiles(const bool &relay_server_synchronize_shared_files);
    bool is_relay_server_synchronize_shared_files_Set() const;
    bool is_relay_server_synchronize_shared_files_Valid() const;

    QString getReportingMode() const;
    void setReportingMode(const QString &reporting_mode);
    bool is_reporting_mode_Set() const;
    bool is_reporting_mode_Valid() const;

    bool isRequireTimeSynchronization() const;
    void setRequireTimeSynchronization(const bool &require_time_synchronization);
    bool is_require_time_synchronization_Set() const;
    bool is_require_time_synchronization_Valid() const;

    bool isRudderComputeChanges() const;
    void setRudderComputeChanges(const bool &rudder_compute_changes);
    bool is_rudder_compute_changes_Set() const;
    bool is_rudder_compute_changes_Valid() const;

    QString getRudderComputeDyngroupsMaxParallelism() const;
    void setRudderComputeDyngroupsMaxParallelism(const QString &rudder_compute_dyngroups_max_parallelism);
    bool is_rudder_compute_dyngroups_max_parallelism_Set() const;
    bool is_rudder_compute_dyngroups_max_parallelism_Valid() const;

    bool isRudderGenerationComputeDyngroups() const;
    void setRudderGenerationComputeDyngroups(const bool &rudder_generation_compute_dyngroups);
    bool is_rudder_generation_compute_dyngroups_Set() const;
    bool is_rudder_generation_compute_dyngroups_Valid() const;

    bool isRudderGenerationContinueOnError() const;
    void setRudderGenerationContinueOnError(const bool &rudder_generation_continue_on_error);
    bool is_rudder_generation_continue_on_error_Set() const;
    bool is_rudder_generation_continue_on_error_Valid() const;

    QString getRudderGenerationDelay() const;
    void setRudderGenerationDelay(const QString &rudder_generation_delay);
    bool is_rudder_generation_delay_Set() const;
    bool is_rudder_generation_delay_Valid() const;

    qint32 getRudderGenerationJsTimeout() const;
    void setRudderGenerationJsTimeout(const qint32 &rudder_generation_js_timeout);
    bool is_rudder_generation_js_timeout_Set() const;
    bool is_rudder_generation_js_timeout_Valid() const;

    QString getRudderGenerationMaxParallelism() const;
    void setRudderGenerationMaxParallelism(const QString &rudder_generation_max_parallelism);
    bool is_rudder_generation_max_parallelism_Set() const;
    bool is_rudder_generation_max_parallelism_Valid() const;

    QString getRudderGenerationPolicy() const;
    void setRudderGenerationPolicy(const QString &rudder_generation_policy);
    bool is_rudder_generation_policy_Set() const;
    bool is_rudder_generation_policy_Valid() const;

    QString getRudderReportProtocolDefault() const;
    void setRudderReportProtocolDefault(const QString &rudder_report_protocol_default);
    bool is_rudder_report_protocol_default_Set() const;
    bool is_rudder_report_protocol_default_Valid() const;

    bool isRudderSaveDbComplianceDetails() const;
    void setRudderSaveDbComplianceDetails(const bool &rudder_save_db_compliance_details);
    bool is_rudder_save_db_compliance_details_Set() const;
    bool is_rudder_save_db_compliance_details_Valid() const;

    bool isRudderSaveDbComplianceLevels() const;
    void setRudderSaveDbComplianceLevels(const bool &rudder_save_db_compliance_levels);
    bool is_rudder_save_db_compliance_levels_Set() const;
    bool is_rudder_save_db_compliance_levels_Valid() const;

    bool isRudderVerifyCertificates() const;
    void setRudderVerifyCertificates(const bool &rudder_verify_certificates);
    bool is_rudder_verify_certificates_Set() const;
    bool is_rudder_verify_certificates_Valid() const;

    qint32 getRunFrequency() const;
    void setRunFrequency(const qint32 &run_frequency);
    bool is_run_frequency_Set() const;
    bool is_run_frequency_Valid() const;

    QString getSendMetrics() const;
    void setSendMetrics(const QString &send_metrics);
    bool is_send_metrics_Set() const;
    bool is_send_metrics_Valid() const;

    qint32 getSplayTime() const;
    void setSplayTime(const qint32 &splay_time);
    bool is_splay_time_Set() const;
    bool is_splay_time_Valid() const;

    bool isUnexpectedUnboundVarValues() const;
    void setUnexpectedUnboundVarValues(const bool &unexpected_unbound_var_values);
    bool is_unexpected_unbound_var_values_Set() const;
    bool is_unexpected_unbound_var_values_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIGetAllSettings_200_response_data_settings_allowed_networks_inner> m_allowed_networks;
    bool m_allowed_networks_isSet;
    bool m_allowed_networks_isValid;

    QString m_change_message_prompt;
    bool m_change_message_prompt_isSet;
    bool m_change_message_prompt_isValid;

    bool m_display_recent_changes_graphs;
    bool m_display_recent_changes_graphs_isSet;
    bool m_display_recent_changes_graphs_isValid;

    bool m_enable_change_message;
    bool m_enable_change_message_isSet;
    bool m_enable_change_message_isValid;

    bool m_enable_change_request;
    bool m_enable_change_request_isSet;
    bool m_enable_change_request_isValid;

    QString m_enable_javascript_directives;
    bool m_enable_javascript_directives_isSet;
    bool m_enable_javascript_directives_isValid;

    bool m_enable_self_deployment;
    bool m_enable_self_deployment_isSet;
    bool m_enable_self_deployment_isValid;

    bool m_enable_self_validation;
    bool m_enable_self_validation_isSet;
    bool m_enable_self_validation_isValid;

    qint32 m_first_run_hour;
    bool m_first_run_hour_isSet;
    bool m_first_run_hour_isValid;

    qint32 m_first_run_minute;
    bool m_first_run_minute_isSet;
    bool m_first_run_minute_isValid;

    QString m_global_policy_mode;
    bool m_global_policy_mode_isSet;
    bool m_global_policy_mode_isValid;

    bool m_global_policy_mode_overridable;
    bool m_global_policy_mode_overridable_isSet;
    bool m_global_policy_mode_overridable_isValid;

    qint32 m_heartbeat_frequency;
    bool m_heartbeat_frequency_isSet;
    bool m_heartbeat_frequency_isValid;

    bool m_mandatory_change_message;
    bool m_mandatory_change_message_isSet;
    bool m_mandatory_change_message_isValid;

    qint32 m_modified_file_ttl;
    bool m_modified_file_ttl_isSet;
    bool m_modified_file_ttl_isValid;

    bool m_node_accept_duplicated_hostname;
    bool m_node_accept_duplicated_hostname_isSet;
    bool m_node_accept_duplicated_hostname_isValid;

    QString m_node_onaccept_default_policy_mode;
    bool m_node_onaccept_default_policy_mode_isSet;
    bool m_node_onaccept_default_policy_mode_isValid;

    QString m_node_onaccept_default_state;
    bool m_node_onaccept_default_state_isSet;
    bool m_node_onaccept_default_state_isValid;

    qint32 m_output_file_ttl;
    bool m_output_file_ttl_isSet;
    bool m_output_file_ttl_isValid;

    QString m_relay_server_synchronization_method;
    bool m_relay_server_synchronization_method_isSet;
    bool m_relay_server_synchronization_method_isValid;

    bool m_relay_server_synchronize_policies;
    bool m_relay_server_synchronize_policies_isSet;
    bool m_relay_server_synchronize_policies_isValid;

    bool m_relay_server_synchronize_shared_files;
    bool m_relay_server_synchronize_shared_files_isSet;
    bool m_relay_server_synchronize_shared_files_isValid;

    QString m_reporting_mode;
    bool m_reporting_mode_isSet;
    bool m_reporting_mode_isValid;

    bool m_require_time_synchronization;
    bool m_require_time_synchronization_isSet;
    bool m_require_time_synchronization_isValid;

    bool m_rudder_compute_changes;
    bool m_rudder_compute_changes_isSet;
    bool m_rudder_compute_changes_isValid;

    QString m_rudder_compute_dyngroups_max_parallelism;
    bool m_rudder_compute_dyngroups_max_parallelism_isSet;
    bool m_rudder_compute_dyngroups_max_parallelism_isValid;

    bool m_rudder_generation_compute_dyngroups;
    bool m_rudder_generation_compute_dyngroups_isSet;
    bool m_rudder_generation_compute_dyngroups_isValid;

    bool m_rudder_generation_continue_on_error;
    bool m_rudder_generation_continue_on_error_isSet;
    bool m_rudder_generation_continue_on_error_isValid;

    QString m_rudder_generation_delay;
    bool m_rudder_generation_delay_isSet;
    bool m_rudder_generation_delay_isValid;

    qint32 m_rudder_generation_js_timeout;
    bool m_rudder_generation_js_timeout_isSet;
    bool m_rudder_generation_js_timeout_isValid;

    QString m_rudder_generation_max_parallelism;
    bool m_rudder_generation_max_parallelism_isSet;
    bool m_rudder_generation_max_parallelism_isValid;

    QString m_rudder_generation_policy;
    bool m_rudder_generation_policy_isSet;
    bool m_rudder_generation_policy_isValid;

    QString m_rudder_report_protocol_default;
    bool m_rudder_report_protocol_default_isSet;
    bool m_rudder_report_protocol_default_isValid;

    bool m_rudder_save_db_compliance_details;
    bool m_rudder_save_db_compliance_details_isSet;
    bool m_rudder_save_db_compliance_details_isValid;

    bool m_rudder_save_db_compliance_levels;
    bool m_rudder_save_db_compliance_levels_isSet;
    bool m_rudder_save_db_compliance_levels_isValid;

    bool m_rudder_verify_certificates;
    bool m_rudder_verify_certificates_isSet;
    bool m_rudder_verify_certificates_isValid;

    qint32 m_run_frequency;
    bool m_run_frequency_isSet;
    bool m_run_frequency_isValid;

    QString m_send_metrics;
    bool m_send_metrics_isSet;
    bool m_send_metrics_isValid;

    qint32 m_splay_time;
    bool m_splay_time_isSet;
    bool m_splay_time_isValid;

    bool m_unexpected_unbound_var_values;
    bool m_unexpected_unbound_var_values_isSet;
    bool m_unexpected_unbound_var_values_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetAllSettings_200_response_data_settings)

#endif // OAIGetAllSettings_200_response_data_settings_H
