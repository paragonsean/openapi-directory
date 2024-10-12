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
 * OAINode_full.h
 *
 * 
 */

#ifndef OAINode_full_H
#define OAINode_full_H

#include <QJsonObject>

#include "OAINode_add_inner_properties_inner.h"
#include "OAINode_full_bios.h"
#include "OAINode_full_controllers_inner.h"
#include "OAINode_full_environmentVariables_inner.h"
#include "OAINode_full_fileSystems_inner.h"
#include "OAINode_full_machine.h"
#include "OAINode_full_managementTechnologyDetails.h"
#include "OAINode_full_managementTechnology_inner.h"
#include "OAINode_full_memories_inner.h"
#include "OAINode_full_networkInterfaces_inner.h"
#include "OAINode_full_os.h"
#include "OAINode_full_ports_inner.h"
#include "OAINode_full_processes_inner.h"
#include "OAINode_full_processors_inner.h"
#include "OAINode_full_slots_inner.h"
#include "OAINode_full_softwareUpdate_inner.h"
#include "OAINode_full_software_inner.h"
#include "OAINode_full_sound_inner.h"
#include "OAINode_full_storage_inner.h"
#include "OAINode_full_timezone.h"
#include "OAINode_full_videos_inner.h"
#include "OAINode_full_virtualMachines_inner.h"
#include <QDate>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINode_full_bios;
class OAINode_full_controllers_inner;
class OAINode_full_environmentVariables_inner;
class OAINode_full_fileSystems_inner;
class OAINode_full_machine;
class OAINode_full_managementTechnology_inner;
class OAINode_full_managementTechnologyDetails;
class OAINode_full_memories_inner;
class OAINode_full_networkInterfaces_inner;
class OAINode_full_os;
class OAINode_full_ports_inner;
class OAINode_full_processes_inner;
class OAINode_full_processors_inner;
class OAINode_add_inner_properties_inner;
class OAINode_full_slots_inner;
class OAINode_full_software_inner;
class OAINode_full_softwareUpdate_inner;
class OAINode_full_sound_inner;
class OAINode_full_storage_inner;
class OAINode_full_timezone;
class OAINode_full_videos_inner;
class OAINode_full_virtualMachines_inner;

class OAINode_full : public OAIObject {
public:
    OAINode_full();
    OAINode_full(QString json);
    ~OAINode_full() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAccounts() const;
    void setAccounts(const QList<QString> &accounts);
    bool is_accounts_Set() const;
    bool is_accounts_Valid() const;

    QString getArchitectureDescription() const;
    void setArchitectureDescription(const QString &architecture_description);
    bool is_architecture_description_Set() const;
    bool is_architecture_description_Valid() const;

    OAINode_full_bios getBios() const;
    void setBios(const OAINode_full_bios &bios);
    bool is_bios_Set() const;
    bool is_bios_Valid() const;

    QList<OAINode_full_controllers_inner> getControllers() const;
    void setControllers(const QList<OAINode_full_controllers_inner> &controllers);
    bool is_controllers_Set() const;
    bool is_controllers_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QList<OAINode_full_environmentVariables_inner> getEnvironmentVariables() const;
    void setEnvironmentVariables(const QList<OAINode_full_environmentVariables_inner> &environment_variables);
    bool is_environment_variables_Set() const;
    bool is_environment_variables_Valid() const;

    QList<OAINode_full_fileSystems_inner> getFileSystems() const;
    void setFileSystems(const QList<OAINode_full_fileSystems_inner> &file_systems);
    bool is_file_systems_Set() const;
    bool is_file_systems_Valid() const;

    QString getHostname() const;
    void setHostname(const QString &hostname);
    bool is_hostname_Set() const;
    bool is_hostname_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<QString> getIpAddresses() const;
    void setIpAddresses(const QList<QString> &ip_addresses);
    bool is_ip_addresses_Set() const;
    bool is_ip_addresses_Valid() const;

    QDate getLastInventoryDate() const;
    void setLastInventoryDate(const QDate &last_inventory_date);
    bool is_last_inventory_date_Set() const;
    bool is_last_inventory_date_Valid() const;

    QDate getLastRunDate() const;
    void setLastRunDate(const QDate &last_run_date);
    bool is_last_run_date_Set() const;
    bool is_last_run_date_Valid() const;

    OAINode_full_machine getMachine() const;
    void setMachine(const OAINode_full_machine &machine);
    bool is_machine_Set() const;
    bool is_machine_Valid() const;

    QList<OAINode_full_managementTechnology_inner> getManagementTechnology() const;
    void setManagementTechnology(const QList<OAINode_full_managementTechnology_inner> &management_technology);
    bool is_management_technology_Set() const;
    bool is_management_technology_Valid() const;

    OAINode_full_managementTechnologyDetails getManagementTechnologyDetails() const;
    void setManagementTechnologyDetails(const OAINode_full_managementTechnologyDetails &management_technology_details);
    bool is_management_technology_details_Set() const;
    bool is_management_technology_details_Valid() const;

    QList<OAINode_full_memories_inner> getMemories() const;
    void setMemories(const QList<OAINode_full_memories_inner> &memories);
    bool is_memories_Set() const;
    bool is_memories_Valid() const;

    QList<OAINode_full_networkInterfaces_inner> getNetworkInterfaces() const;
    void setNetworkInterfaces(const QList<OAINode_full_networkInterfaces_inner> &network_interfaces);
    bool is_network_interfaces_Set() const;
    bool is_network_interfaces_Valid() const;

    OAINode_full_os getOs() const;
    void setOs(const OAINode_full_os &os);
    bool is_os_Set() const;
    bool is_os_Valid() const;

    QString getPolicyMode() const;
    void setPolicyMode(const QString &policy_mode);
    bool is_policy_mode_Set() const;
    bool is_policy_mode_Valid() const;

    QString getPolicyServerId() const;
    void setPolicyServerId(const QString &policy_server_id);
    bool is_policy_server_id_Set() const;
    bool is_policy_server_id_Valid() const;

    QList<OAINode_full_ports_inner> getPorts() const;
    void setPorts(const QList<OAINode_full_ports_inner> &ports);
    bool is_ports_Set() const;
    bool is_ports_Valid() const;

    QList<OAINode_full_processes_inner> getProcesses() const;
    void setProcesses(const QList<OAINode_full_processes_inner> &processes);
    bool is_processes_Set() const;
    bool is_processes_Valid() const;

    QList<OAINode_full_processors_inner> getProcessors() const;
    void setProcessors(const QList<OAINode_full_processors_inner> &processors);
    bool is_processors_Set() const;
    bool is_processors_Valid() const;

    QList<OAINode_add_inner_properties_inner> getProperties() const;
    void setProperties(const QList<OAINode_add_inner_properties_inner> &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    qint32 getRam() const;
    void setRam(const qint32 &ram);
    bool is_ram_Set() const;
    bool is_ram_Valid() const;

    QList<OAINode_full_slots_inner> getRSlots() const;
    void setRSlots(const QList<OAINode_full_slots_inner> &r_slots);
    bool is_r_slots_Set() const;
    bool is_r_slots_Valid() const;

    QList<OAINode_full_software_inner> getSoftware() const;
    void setSoftware(const QList<OAINode_full_software_inner> &software);
    bool is_software_Set() const;
    bool is_software_Valid() const;

    QList<OAINode_full_softwareUpdate_inner> getSoftwareUpdate() const;
    void setSoftwareUpdate(const QList<OAINode_full_softwareUpdate_inner> &software_update);
    bool is_software_update_Set() const;
    bool is_software_update_Valid() const;

    QList<OAINode_full_sound_inner> getSound() const;
    void setSound(const QList<OAINode_full_sound_inner> &sound);
    bool is_sound_Set() const;
    bool is_sound_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<OAINode_full_storage_inner> getStorage() const;
    void setStorage(const QList<OAINode_full_storage_inner> &storage);
    bool is_storage_Set() const;
    bool is_storage_Valid() const;

    OAINode_full_timezone getTimezone() const;
    void setTimezone(const OAINode_full_timezone &timezone);
    bool is_timezone_Set() const;
    bool is_timezone_Valid() const;

    QList<OAINode_full_videos_inner> getVideos() const;
    void setVideos(const QList<OAINode_full_videos_inner> &videos);
    bool is_videos_Set() const;
    bool is_videos_Valid() const;

    QList<OAINode_full_virtualMachines_inner> getVirtualMachines() const;
    void setVirtualMachines(const QList<OAINode_full_virtualMachines_inner> &virtual_machines);
    bool is_virtual_machines_Set() const;
    bool is_virtual_machines_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_accounts;
    bool m_accounts_isSet;
    bool m_accounts_isValid;

    QString m_architecture_description;
    bool m_architecture_description_isSet;
    bool m_architecture_description_isValid;

    OAINode_full_bios m_bios;
    bool m_bios_isSet;
    bool m_bios_isValid;

    QList<OAINode_full_controllers_inner> m_controllers;
    bool m_controllers_isSet;
    bool m_controllers_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QList<OAINode_full_environmentVariables_inner> m_environment_variables;
    bool m_environment_variables_isSet;
    bool m_environment_variables_isValid;

    QList<OAINode_full_fileSystems_inner> m_file_systems;
    bool m_file_systems_isSet;
    bool m_file_systems_isValid;

    QString m_hostname;
    bool m_hostname_isSet;
    bool m_hostname_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<QString> m_ip_addresses;
    bool m_ip_addresses_isSet;
    bool m_ip_addresses_isValid;

    QDate m_last_inventory_date;
    bool m_last_inventory_date_isSet;
    bool m_last_inventory_date_isValid;

    QDate m_last_run_date;
    bool m_last_run_date_isSet;
    bool m_last_run_date_isValid;

    OAINode_full_machine m_machine;
    bool m_machine_isSet;
    bool m_machine_isValid;

    QList<OAINode_full_managementTechnology_inner> m_management_technology;
    bool m_management_technology_isSet;
    bool m_management_technology_isValid;

    OAINode_full_managementTechnologyDetails m_management_technology_details;
    bool m_management_technology_details_isSet;
    bool m_management_technology_details_isValid;

    QList<OAINode_full_memories_inner> m_memories;
    bool m_memories_isSet;
    bool m_memories_isValid;

    QList<OAINode_full_networkInterfaces_inner> m_network_interfaces;
    bool m_network_interfaces_isSet;
    bool m_network_interfaces_isValid;

    OAINode_full_os m_os;
    bool m_os_isSet;
    bool m_os_isValid;

    QString m_policy_mode;
    bool m_policy_mode_isSet;
    bool m_policy_mode_isValid;

    QString m_policy_server_id;
    bool m_policy_server_id_isSet;
    bool m_policy_server_id_isValid;

    QList<OAINode_full_ports_inner> m_ports;
    bool m_ports_isSet;
    bool m_ports_isValid;

    QList<OAINode_full_processes_inner> m_processes;
    bool m_processes_isSet;
    bool m_processes_isValid;

    QList<OAINode_full_processors_inner> m_processors;
    bool m_processors_isSet;
    bool m_processors_isValid;

    QList<OAINode_add_inner_properties_inner> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    qint32 m_ram;
    bool m_ram_isSet;
    bool m_ram_isValid;

    QList<OAINode_full_slots_inner> m_r_slots;
    bool m_r_slots_isSet;
    bool m_r_slots_isValid;

    QList<OAINode_full_software_inner> m_software;
    bool m_software_isSet;
    bool m_software_isValid;

    QList<OAINode_full_softwareUpdate_inner> m_software_update;
    bool m_software_update_isSet;
    bool m_software_update_isValid;

    QList<OAINode_full_sound_inner> m_sound;
    bool m_sound_isSet;
    bool m_sound_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<OAINode_full_storage_inner> m_storage;
    bool m_storage_isSet;
    bool m_storage_isValid;

    OAINode_full_timezone m_timezone;
    bool m_timezone_isSet;
    bool m_timezone_isValid;

    QList<OAINode_full_videos_inner> m_videos;
    bool m_videos_isSet;
    bool m_videos_isValid;

    QList<OAINode_full_virtualMachines_inner> m_virtual_machines;
    bool m_virtual_machines_isSet;
    bool m_virtual_machines_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINode_full)

#endif // OAINode_full_H
