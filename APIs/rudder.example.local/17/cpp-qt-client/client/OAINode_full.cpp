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

#include "OAINode_full.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINode_full::OAINode_full(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINode_full::OAINode_full() {
    this->initializeModel();
}

OAINode_full::~OAINode_full() {}

void OAINode_full::initializeModel() {

    m_accounts_isSet = false;
    m_accounts_isValid = false;

    m_architecture_description_isSet = false;
    m_architecture_description_isValid = false;

    m_bios_isSet = false;
    m_bios_isValid = false;

    m_controllers_isSet = false;
    m_controllers_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_environment_variables_isSet = false;
    m_environment_variables_isValid = false;

    m_file_systems_isSet = false;
    m_file_systems_isValid = false;

    m_hostname_isSet = false;
    m_hostname_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_ip_addresses_isSet = false;
    m_ip_addresses_isValid = false;

    m_last_inventory_date_isSet = false;
    m_last_inventory_date_isValid = false;

    m_last_run_date_isSet = false;
    m_last_run_date_isValid = false;

    m_machine_isSet = false;
    m_machine_isValid = false;

    m_management_technology_isSet = false;
    m_management_technology_isValid = false;

    m_management_technology_details_isSet = false;
    m_management_technology_details_isValid = false;

    m_memories_isSet = false;
    m_memories_isValid = false;

    m_network_interfaces_isSet = false;
    m_network_interfaces_isValid = false;

    m_os_isSet = false;
    m_os_isValid = false;

    m_policy_mode_isSet = false;
    m_policy_mode_isValid = false;

    m_policy_server_id_isSet = false;
    m_policy_server_id_isValid = false;

    m_ports_isSet = false;
    m_ports_isValid = false;

    m_processes_isSet = false;
    m_processes_isValid = false;

    m_processors_isSet = false;
    m_processors_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_ram_isSet = false;
    m_ram_isValid = false;

    m_r_slots_isSet = false;
    m_r_slots_isValid = false;

    m_software_isSet = false;
    m_software_isValid = false;

    m_software_update_isSet = false;
    m_software_update_isValid = false;

    m_sound_isSet = false;
    m_sound_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_storage_isSet = false;
    m_storage_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;

    m_videos_isSet = false;
    m_videos_isValid = false;

    m_virtual_machines_isSet = false;
    m_virtual_machines_isValid = false;
}

void OAINode_full::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINode_full::fromJsonObject(QJsonObject json) {

    m_accounts_isValid = ::OpenAPI::fromJsonValue(m_accounts, json[QString("accounts")]);
    m_accounts_isSet = !json[QString("accounts")].isNull() && m_accounts_isValid;

    m_architecture_description_isValid = ::OpenAPI::fromJsonValue(m_architecture_description, json[QString("architectureDescription")]);
    m_architecture_description_isSet = !json[QString("architectureDescription")].isNull() && m_architecture_description_isValid;

    m_bios_isValid = ::OpenAPI::fromJsonValue(m_bios, json[QString("bios")]);
    m_bios_isSet = !json[QString("bios")].isNull() && m_bios_isValid;

    m_controllers_isValid = ::OpenAPI::fromJsonValue(m_controllers, json[QString("controllers")]);
    m_controllers_isSet = !json[QString("controllers")].isNull() && m_controllers_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_environment_variables_isValid = ::OpenAPI::fromJsonValue(m_environment_variables, json[QString("environmentVariables")]);
    m_environment_variables_isSet = !json[QString("environmentVariables")].isNull() && m_environment_variables_isValid;

    m_file_systems_isValid = ::OpenAPI::fromJsonValue(m_file_systems, json[QString("fileSystems")]);
    m_file_systems_isSet = !json[QString("fileSystems")].isNull() && m_file_systems_isValid;

    m_hostname_isValid = ::OpenAPI::fromJsonValue(m_hostname, json[QString("hostname")]);
    m_hostname_isSet = !json[QString("hostname")].isNull() && m_hostname_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_ip_addresses_isValid = ::OpenAPI::fromJsonValue(m_ip_addresses, json[QString("ipAddresses")]);
    m_ip_addresses_isSet = !json[QString("ipAddresses")].isNull() && m_ip_addresses_isValid;

    m_last_inventory_date_isValid = ::OpenAPI::fromJsonValue(m_last_inventory_date, json[QString("lastInventoryDate")]);
    m_last_inventory_date_isSet = !json[QString("lastInventoryDate")].isNull() && m_last_inventory_date_isValid;

    m_last_run_date_isValid = ::OpenAPI::fromJsonValue(m_last_run_date, json[QString("lastRunDate")]);
    m_last_run_date_isSet = !json[QString("lastRunDate")].isNull() && m_last_run_date_isValid;

    m_machine_isValid = ::OpenAPI::fromJsonValue(m_machine, json[QString("machine")]);
    m_machine_isSet = !json[QString("machine")].isNull() && m_machine_isValid;

    m_management_technology_isValid = ::OpenAPI::fromJsonValue(m_management_technology, json[QString("managementTechnology")]);
    m_management_technology_isSet = !json[QString("managementTechnology")].isNull() && m_management_technology_isValid;

    m_management_technology_details_isValid = ::OpenAPI::fromJsonValue(m_management_technology_details, json[QString("managementTechnologyDetails")]);
    m_management_technology_details_isSet = !json[QString("managementTechnologyDetails")].isNull() && m_management_technology_details_isValid;

    m_memories_isValid = ::OpenAPI::fromJsonValue(m_memories, json[QString("memories")]);
    m_memories_isSet = !json[QString("memories")].isNull() && m_memories_isValid;

    m_network_interfaces_isValid = ::OpenAPI::fromJsonValue(m_network_interfaces, json[QString("networkInterfaces")]);
    m_network_interfaces_isSet = !json[QString("networkInterfaces")].isNull() && m_network_interfaces_isValid;

    m_os_isValid = ::OpenAPI::fromJsonValue(m_os, json[QString("os")]);
    m_os_isSet = !json[QString("os")].isNull() && m_os_isValid;

    m_policy_mode_isValid = ::OpenAPI::fromJsonValue(m_policy_mode, json[QString("policyMode")]);
    m_policy_mode_isSet = !json[QString("policyMode")].isNull() && m_policy_mode_isValid;

    m_policy_server_id_isValid = ::OpenAPI::fromJsonValue(m_policy_server_id, json[QString("policyServerId")]);
    m_policy_server_id_isSet = !json[QString("policyServerId")].isNull() && m_policy_server_id_isValid;

    m_ports_isValid = ::OpenAPI::fromJsonValue(m_ports, json[QString("ports")]);
    m_ports_isSet = !json[QString("ports")].isNull() && m_ports_isValid;

    m_processes_isValid = ::OpenAPI::fromJsonValue(m_processes, json[QString("processes")]);
    m_processes_isSet = !json[QString("processes")].isNull() && m_processes_isValid;

    m_processors_isValid = ::OpenAPI::fromJsonValue(m_processors, json[QString("processors")]);
    m_processors_isSet = !json[QString("processors")].isNull() && m_processors_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_ram_isValid = ::OpenAPI::fromJsonValue(m_ram, json[QString("ram")]);
    m_ram_isSet = !json[QString("ram")].isNull() && m_ram_isValid;

    m_r_slots_isValid = ::OpenAPI::fromJsonValue(m_r_slots, json[QString("slots")]);
    m_r_slots_isSet = !json[QString("slots")].isNull() && m_r_slots_isValid;

    m_software_isValid = ::OpenAPI::fromJsonValue(m_software, json[QString("software")]);
    m_software_isSet = !json[QString("software")].isNull() && m_software_isValid;

    m_software_update_isValid = ::OpenAPI::fromJsonValue(m_software_update, json[QString("softwareUpdate")]);
    m_software_update_isSet = !json[QString("softwareUpdate")].isNull() && m_software_update_isValid;

    m_sound_isValid = ::OpenAPI::fromJsonValue(m_sound, json[QString("sound")]);
    m_sound_isSet = !json[QString("sound")].isNull() && m_sound_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_storage_isValid = ::OpenAPI::fromJsonValue(m_storage, json[QString("storage")]);
    m_storage_isSet = !json[QString("storage")].isNull() && m_storage_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;

    m_videos_isValid = ::OpenAPI::fromJsonValue(m_videos, json[QString("videos")]);
    m_videos_isSet = !json[QString("videos")].isNull() && m_videos_isValid;

    m_virtual_machines_isValid = ::OpenAPI::fromJsonValue(m_virtual_machines, json[QString("virtualMachines")]);
    m_virtual_machines_isSet = !json[QString("virtualMachines")].isNull() && m_virtual_machines_isValid;
}

QString OAINode_full::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINode_full::asJsonObject() const {
    QJsonObject obj;
    if (m_accounts.size() > 0) {
        obj.insert(QString("accounts"), ::OpenAPI::toJsonValue(m_accounts));
    }
    if (m_architecture_description_isSet) {
        obj.insert(QString("architectureDescription"), ::OpenAPI::toJsonValue(m_architecture_description));
    }
    if (m_bios.isSet()) {
        obj.insert(QString("bios"), ::OpenAPI::toJsonValue(m_bios));
    }
    if (m_controllers.size() > 0) {
        obj.insert(QString("controllers"), ::OpenAPI::toJsonValue(m_controllers));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_environment_variables.size() > 0) {
        obj.insert(QString("environmentVariables"), ::OpenAPI::toJsonValue(m_environment_variables));
    }
    if (m_file_systems.size() > 0) {
        obj.insert(QString("fileSystems"), ::OpenAPI::toJsonValue(m_file_systems));
    }
    if (m_hostname_isSet) {
        obj.insert(QString("hostname"), ::OpenAPI::toJsonValue(m_hostname));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_ip_addresses.size() > 0) {
        obj.insert(QString("ipAddresses"), ::OpenAPI::toJsonValue(m_ip_addresses));
    }
    if (m_last_inventory_date_isSet) {
        obj.insert(QString("lastInventoryDate"), ::OpenAPI::toJsonValue(m_last_inventory_date));
    }
    if (m_last_run_date_isSet) {
        obj.insert(QString("lastRunDate"), ::OpenAPI::toJsonValue(m_last_run_date));
    }
    if (m_machine.isSet()) {
        obj.insert(QString("machine"), ::OpenAPI::toJsonValue(m_machine));
    }
    if (m_management_technology.size() > 0) {
        obj.insert(QString("managementTechnology"), ::OpenAPI::toJsonValue(m_management_technology));
    }
    if (m_management_technology_details.isSet()) {
        obj.insert(QString("managementTechnologyDetails"), ::OpenAPI::toJsonValue(m_management_technology_details));
    }
    if (m_memories.size() > 0) {
        obj.insert(QString("memories"), ::OpenAPI::toJsonValue(m_memories));
    }
    if (m_network_interfaces.size() > 0) {
        obj.insert(QString("networkInterfaces"), ::OpenAPI::toJsonValue(m_network_interfaces));
    }
    if (m_os.isSet()) {
        obj.insert(QString("os"), ::OpenAPI::toJsonValue(m_os));
    }
    if (m_policy_mode_isSet) {
        obj.insert(QString("policyMode"), ::OpenAPI::toJsonValue(m_policy_mode));
    }
    if (m_policy_server_id_isSet) {
        obj.insert(QString("policyServerId"), ::OpenAPI::toJsonValue(m_policy_server_id));
    }
    if (m_ports.size() > 0) {
        obj.insert(QString("ports"), ::OpenAPI::toJsonValue(m_ports));
    }
    if (m_processes.size() > 0) {
        obj.insert(QString("processes"), ::OpenAPI::toJsonValue(m_processes));
    }
    if (m_processors.size() > 0) {
        obj.insert(QString("processors"), ::OpenAPI::toJsonValue(m_processors));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_ram_isSet) {
        obj.insert(QString("ram"), ::OpenAPI::toJsonValue(m_ram));
    }
    if (m_r_slots.size() > 0) {
        obj.insert(QString("slots"), ::OpenAPI::toJsonValue(m_r_slots));
    }
    if (m_software.size() > 0) {
        obj.insert(QString("software"), ::OpenAPI::toJsonValue(m_software));
    }
    if (m_software_update.size() > 0) {
        obj.insert(QString("softwareUpdate"), ::OpenAPI::toJsonValue(m_software_update));
    }
    if (m_sound.size() > 0) {
        obj.insert(QString("sound"), ::OpenAPI::toJsonValue(m_sound));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_storage.size() > 0) {
        obj.insert(QString("storage"), ::OpenAPI::toJsonValue(m_storage));
    }
    if (m_timezone.isSet()) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
    }
    if (m_videos.size() > 0) {
        obj.insert(QString("videos"), ::OpenAPI::toJsonValue(m_videos));
    }
    if (m_virtual_machines.size() > 0) {
        obj.insert(QString("virtualMachines"), ::OpenAPI::toJsonValue(m_virtual_machines));
    }
    return obj;
}

QList<QString> OAINode_full::getAccounts() const {
    return m_accounts;
}
void OAINode_full::setAccounts(const QList<QString> &accounts) {
    m_accounts = accounts;
    m_accounts_isSet = true;
}

bool OAINode_full::is_accounts_Set() const{
    return m_accounts_isSet;
}

bool OAINode_full::is_accounts_Valid() const{
    return m_accounts_isValid;
}

QString OAINode_full::getArchitectureDescription() const {
    return m_architecture_description;
}
void OAINode_full::setArchitectureDescription(const QString &architecture_description) {
    m_architecture_description = architecture_description;
    m_architecture_description_isSet = true;
}

bool OAINode_full::is_architecture_description_Set() const{
    return m_architecture_description_isSet;
}

bool OAINode_full::is_architecture_description_Valid() const{
    return m_architecture_description_isValid;
}

OAINode_full_bios OAINode_full::getBios() const {
    return m_bios;
}
void OAINode_full::setBios(const OAINode_full_bios &bios) {
    m_bios = bios;
    m_bios_isSet = true;
}

bool OAINode_full::is_bios_Set() const{
    return m_bios_isSet;
}

bool OAINode_full::is_bios_Valid() const{
    return m_bios_isValid;
}

QList<OAINode_full_controllers_inner> OAINode_full::getControllers() const {
    return m_controllers;
}
void OAINode_full::setControllers(const QList<OAINode_full_controllers_inner> &controllers) {
    m_controllers = controllers;
    m_controllers_isSet = true;
}

bool OAINode_full::is_controllers_Set() const{
    return m_controllers_isSet;
}

bool OAINode_full::is_controllers_Valid() const{
    return m_controllers_isValid;
}

QString OAINode_full::getDescription() const {
    return m_description;
}
void OAINode_full::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAINode_full::is_description_Set() const{
    return m_description_isSet;
}

bool OAINode_full::is_description_Valid() const{
    return m_description_isValid;
}

QList<OAINode_full_environmentVariables_inner> OAINode_full::getEnvironmentVariables() const {
    return m_environment_variables;
}
void OAINode_full::setEnvironmentVariables(const QList<OAINode_full_environmentVariables_inner> &environment_variables) {
    m_environment_variables = environment_variables;
    m_environment_variables_isSet = true;
}

bool OAINode_full::is_environment_variables_Set() const{
    return m_environment_variables_isSet;
}

bool OAINode_full::is_environment_variables_Valid() const{
    return m_environment_variables_isValid;
}

QList<OAINode_full_fileSystems_inner> OAINode_full::getFileSystems() const {
    return m_file_systems;
}
void OAINode_full::setFileSystems(const QList<OAINode_full_fileSystems_inner> &file_systems) {
    m_file_systems = file_systems;
    m_file_systems_isSet = true;
}

bool OAINode_full::is_file_systems_Set() const{
    return m_file_systems_isSet;
}

bool OAINode_full::is_file_systems_Valid() const{
    return m_file_systems_isValid;
}

QString OAINode_full::getHostname() const {
    return m_hostname;
}
void OAINode_full::setHostname(const QString &hostname) {
    m_hostname = hostname;
    m_hostname_isSet = true;
}

bool OAINode_full::is_hostname_Set() const{
    return m_hostname_isSet;
}

bool OAINode_full::is_hostname_Valid() const{
    return m_hostname_isValid;
}

QString OAINode_full::getId() const {
    return m_id;
}
void OAINode_full::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAINode_full::is_id_Set() const{
    return m_id_isSet;
}

bool OAINode_full::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAINode_full::getIpAddresses() const {
    return m_ip_addresses;
}
void OAINode_full::setIpAddresses(const QList<QString> &ip_addresses) {
    m_ip_addresses = ip_addresses;
    m_ip_addresses_isSet = true;
}

bool OAINode_full::is_ip_addresses_Set() const{
    return m_ip_addresses_isSet;
}

bool OAINode_full::is_ip_addresses_Valid() const{
    return m_ip_addresses_isValid;
}

QDate OAINode_full::getLastInventoryDate() const {
    return m_last_inventory_date;
}
void OAINode_full::setLastInventoryDate(const QDate &last_inventory_date) {
    m_last_inventory_date = last_inventory_date;
    m_last_inventory_date_isSet = true;
}

bool OAINode_full::is_last_inventory_date_Set() const{
    return m_last_inventory_date_isSet;
}

bool OAINode_full::is_last_inventory_date_Valid() const{
    return m_last_inventory_date_isValid;
}

QDate OAINode_full::getLastRunDate() const {
    return m_last_run_date;
}
void OAINode_full::setLastRunDate(const QDate &last_run_date) {
    m_last_run_date = last_run_date;
    m_last_run_date_isSet = true;
}

bool OAINode_full::is_last_run_date_Set() const{
    return m_last_run_date_isSet;
}

bool OAINode_full::is_last_run_date_Valid() const{
    return m_last_run_date_isValid;
}

OAINode_full_machine OAINode_full::getMachine() const {
    return m_machine;
}
void OAINode_full::setMachine(const OAINode_full_machine &machine) {
    m_machine = machine;
    m_machine_isSet = true;
}

bool OAINode_full::is_machine_Set() const{
    return m_machine_isSet;
}

bool OAINode_full::is_machine_Valid() const{
    return m_machine_isValid;
}

QList<OAINode_full_managementTechnology_inner> OAINode_full::getManagementTechnology() const {
    return m_management_technology;
}
void OAINode_full::setManagementTechnology(const QList<OAINode_full_managementTechnology_inner> &management_technology) {
    m_management_technology = management_technology;
    m_management_technology_isSet = true;
}

bool OAINode_full::is_management_technology_Set() const{
    return m_management_technology_isSet;
}

bool OAINode_full::is_management_technology_Valid() const{
    return m_management_technology_isValid;
}

OAINode_full_managementTechnologyDetails OAINode_full::getManagementTechnologyDetails() const {
    return m_management_technology_details;
}
void OAINode_full::setManagementTechnologyDetails(const OAINode_full_managementTechnologyDetails &management_technology_details) {
    m_management_technology_details = management_technology_details;
    m_management_technology_details_isSet = true;
}

bool OAINode_full::is_management_technology_details_Set() const{
    return m_management_technology_details_isSet;
}

bool OAINode_full::is_management_technology_details_Valid() const{
    return m_management_technology_details_isValid;
}

QList<OAINode_full_memories_inner> OAINode_full::getMemories() const {
    return m_memories;
}
void OAINode_full::setMemories(const QList<OAINode_full_memories_inner> &memories) {
    m_memories = memories;
    m_memories_isSet = true;
}

bool OAINode_full::is_memories_Set() const{
    return m_memories_isSet;
}

bool OAINode_full::is_memories_Valid() const{
    return m_memories_isValid;
}

QList<OAINode_full_networkInterfaces_inner> OAINode_full::getNetworkInterfaces() const {
    return m_network_interfaces;
}
void OAINode_full::setNetworkInterfaces(const QList<OAINode_full_networkInterfaces_inner> &network_interfaces) {
    m_network_interfaces = network_interfaces;
    m_network_interfaces_isSet = true;
}

bool OAINode_full::is_network_interfaces_Set() const{
    return m_network_interfaces_isSet;
}

bool OAINode_full::is_network_interfaces_Valid() const{
    return m_network_interfaces_isValid;
}

OAINode_full_os OAINode_full::getOs() const {
    return m_os;
}
void OAINode_full::setOs(const OAINode_full_os &os) {
    m_os = os;
    m_os_isSet = true;
}

bool OAINode_full::is_os_Set() const{
    return m_os_isSet;
}

bool OAINode_full::is_os_Valid() const{
    return m_os_isValid;
}

QString OAINode_full::getPolicyMode() const {
    return m_policy_mode;
}
void OAINode_full::setPolicyMode(const QString &policy_mode) {
    m_policy_mode = policy_mode;
    m_policy_mode_isSet = true;
}

bool OAINode_full::is_policy_mode_Set() const{
    return m_policy_mode_isSet;
}

bool OAINode_full::is_policy_mode_Valid() const{
    return m_policy_mode_isValid;
}

QString OAINode_full::getPolicyServerId() const {
    return m_policy_server_id;
}
void OAINode_full::setPolicyServerId(const QString &policy_server_id) {
    m_policy_server_id = policy_server_id;
    m_policy_server_id_isSet = true;
}

bool OAINode_full::is_policy_server_id_Set() const{
    return m_policy_server_id_isSet;
}

bool OAINode_full::is_policy_server_id_Valid() const{
    return m_policy_server_id_isValid;
}

QList<OAINode_full_ports_inner> OAINode_full::getPorts() const {
    return m_ports;
}
void OAINode_full::setPorts(const QList<OAINode_full_ports_inner> &ports) {
    m_ports = ports;
    m_ports_isSet = true;
}

bool OAINode_full::is_ports_Set() const{
    return m_ports_isSet;
}

bool OAINode_full::is_ports_Valid() const{
    return m_ports_isValid;
}

QList<OAINode_full_processes_inner> OAINode_full::getProcesses() const {
    return m_processes;
}
void OAINode_full::setProcesses(const QList<OAINode_full_processes_inner> &processes) {
    m_processes = processes;
    m_processes_isSet = true;
}

bool OAINode_full::is_processes_Set() const{
    return m_processes_isSet;
}

bool OAINode_full::is_processes_Valid() const{
    return m_processes_isValid;
}

QList<OAINode_full_processors_inner> OAINode_full::getProcessors() const {
    return m_processors;
}
void OAINode_full::setProcessors(const QList<OAINode_full_processors_inner> &processors) {
    m_processors = processors;
    m_processors_isSet = true;
}

bool OAINode_full::is_processors_Set() const{
    return m_processors_isSet;
}

bool OAINode_full::is_processors_Valid() const{
    return m_processors_isValid;
}

QList<OAINode_add_inner_properties_inner> OAINode_full::getProperties() const {
    return m_properties;
}
void OAINode_full::setProperties(const QList<OAINode_add_inner_properties_inner> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAINode_full::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAINode_full::is_properties_Valid() const{
    return m_properties_isValid;
}

qint32 OAINode_full::getRam() const {
    return m_ram;
}
void OAINode_full::setRam(const qint32 &ram) {
    m_ram = ram;
    m_ram_isSet = true;
}

bool OAINode_full::is_ram_Set() const{
    return m_ram_isSet;
}

bool OAINode_full::is_ram_Valid() const{
    return m_ram_isValid;
}

QList<OAINode_full_slots_inner> OAINode_full::getRSlots() const {
    return m_r_slots;
}
void OAINode_full::setRSlots(const QList<OAINode_full_slots_inner> &r_slots) {
    m_r_slots = r_slots;
    m_r_slots_isSet = true;
}

bool OAINode_full::is_r_slots_Set() const{
    return m_r_slots_isSet;
}

bool OAINode_full::is_r_slots_Valid() const{
    return m_r_slots_isValid;
}

QList<OAINode_full_software_inner> OAINode_full::getSoftware() const {
    return m_software;
}
void OAINode_full::setSoftware(const QList<OAINode_full_software_inner> &software) {
    m_software = software;
    m_software_isSet = true;
}

bool OAINode_full::is_software_Set() const{
    return m_software_isSet;
}

bool OAINode_full::is_software_Valid() const{
    return m_software_isValid;
}

QList<OAINode_full_softwareUpdate_inner> OAINode_full::getSoftwareUpdate() const {
    return m_software_update;
}
void OAINode_full::setSoftwareUpdate(const QList<OAINode_full_softwareUpdate_inner> &software_update) {
    m_software_update = software_update;
    m_software_update_isSet = true;
}

bool OAINode_full::is_software_update_Set() const{
    return m_software_update_isSet;
}

bool OAINode_full::is_software_update_Valid() const{
    return m_software_update_isValid;
}

QList<OAINode_full_sound_inner> OAINode_full::getSound() const {
    return m_sound;
}
void OAINode_full::setSound(const QList<OAINode_full_sound_inner> &sound) {
    m_sound = sound;
    m_sound_isSet = true;
}

bool OAINode_full::is_sound_Set() const{
    return m_sound_isSet;
}

bool OAINode_full::is_sound_Valid() const{
    return m_sound_isValid;
}

QString OAINode_full::getStatus() const {
    return m_status;
}
void OAINode_full::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAINode_full::is_status_Set() const{
    return m_status_isSet;
}

bool OAINode_full::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAINode_full_storage_inner> OAINode_full::getStorage() const {
    return m_storage;
}
void OAINode_full::setStorage(const QList<OAINode_full_storage_inner> &storage) {
    m_storage = storage;
    m_storage_isSet = true;
}

bool OAINode_full::is_storage_Set() const{
    return m_storage_isSet;
}

bool OAINode_full::is_storage_Valid() const{
    return m_storage_isValid;
}

OAINode_full_timezone OAINode_full::getTimezone() const {
    return m_timezone;
}
void OAINode_full::setTimezone(const OAINode_full_timezone &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAINode_full::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAINode_full::is_timezone_Valid() const{
    return m_timezone_isValid;
}

QList<OAINode_full_videos_inner> OAINode_full::getVideos() const {
    return m_videos;
}
void OAINode_full::setVideos(const QList<OAINode_full_videos_inner> &videos) {
    m_videos = videos;
    m_videos_isSet = true;
}

bool OAINode_full::is_videos_Set() const{
    return m_videos_isSet;
}

bool OAINode_full::is_videos_Valid() const{
    return m_videos_isValid;
}

QList<OAINode_full_virtualMachines_inner> OAINode_full::getVirtualMachines() const {
    return m_virtual_machines;
}
void OAINode_full::setVirtualMachines(const QList<OAINode_full_virtualMachines_inner> &virtual_machines) {
    m_virtual_machines = virtual_machines;
    m_virtual_machines_isSet = true;
}

bool OAINode_full::is_virtual_machines_Set() const{
    return m_virtual_machines_isSet;
}

bool OAINode_full::is_virtual_machines_Valid() const{
    return m_virtual_machines_isValid;
}

bool OAINode_full::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_architecture_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bios.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_controllers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_environment_variables.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_systems.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hostname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_inventory_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_run_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_machine.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_management_technology.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_management_technology_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_memories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_network_interfaces.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_os.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_policy_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_policy_server_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ports.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_processes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_processors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ram_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_slots.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_software.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_software_update.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sound.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storage.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_videos.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_virtual_machines.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINode_full::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_hostname_isValid && m_id_isValid && m_ip_addresses_isValid && m_management_technology_isValid && m_policy_server_id_isValid && m_properties_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
