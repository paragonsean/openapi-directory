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

#include "OAINode_add_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINode_add_inner::OAINode_add_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINode_add_inner::OAINode_add_inner() {
    this->initializeModel();
}

OAINode_add_inner::~OAINode_add_inner() {}

void OAINode_add_inner::initializeModel() {

    m_agent_key_isSet = false;
    m_agent_key_isValid = false;

    m_hostname_isSet = false;
    m_hostname_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_ip_addresses_isSet = false;
    m_ip_addresses_isValid = false;

    m_machine_type_isSet = false;
    m_machine_type_isValid = false;

    m_os_isSet = false;
    m_os_isValid = false;

    m_policy_mode_isSet = false;
    m_policy_mode_isValid = false;

    m_policy_server_id_isSet = false;
    m_policy_server_id_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;
}

void OAINode_add_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINode_add_inner::fromJsonObject(QJsonObject json) {

    m_agent_key_isValid = ::OpenAPI::fromJsonValue(m_agent_key, json[QString("agentKey")]);
    m_agent_key_isSet = !json[QString("agentKey")].isNull() && m_agent_key_isValid;

    m_hostname_isValid = ::OpenAPI::fromJsonValue(m_hostname, json[QString("hostname")]);
    m_hostname_isSet = !json[QString("hostname")].isNull() && m_hostname_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_ip_addresses_isValid = ::OpenAPI::fromJsonValue(m_ip_addresses, json[QString("ipAddresses")]);
    m_ip_addresses_isSet = !json[QString("ipAddresses")].isNull() && m_ip_addresses_isValid;

    m_machine_type_isValid = ::OpenAPI::fromJsonValue(m_machine_type, json[QString("machineType")]);
    m_machine_type_isSet = !json[QString("machineType")].isNull() && m_machine_type_isValid;

    m_os_isValid = ::OpenAPI::fromJsonValue(m_os, json[QString("os")]);
    m_os_isSet = !json[QString("os")].isNull() && m_os_isValid;

    m_policy_mode_isValid = ::OpenAPI::fromJsonValue(m_policy_mode, json[QString("policyMode")]);
    m_policy_mode_isSet = !json[QString("policyMode")].isNull() && m_policy_mode_isValid;

    m_policy_server_id_isValid = ::OpenAPI::fromJsonValue(m_policy_server_id, json[QString("policyServerId")]);
    m_policy_server_id_isSet = !json[QString("policyServerId")].isNull() && m_policy_server_id_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;
}

QString OAINode_add_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINode_add_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_agent_key.isSet()) {
        obj.insert(QString("agentKey"), ::OpenAPI::toJsonValue(m_agent_key));
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
    if (m_machine_type_isSet) {
        obj.insert(QString("machineType"), ::OpenAPI::toJsonValue(m_machine_type));
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
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_timezone.isSet()) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
    }
    return obj;
}

OAIAgent_key OAINode_add_inner::getAgentKey() const {
    return m_agent_key;
}
void OAINode_add_inner::setAgentKey(const OAIAgent_key &agent_key) {
    m_agent_key = agent_key;
    m_agent_key_isSet = true;
}

bool OAINode_add_inner::is_agent_key_Set() const{
    return m_agent_key_isSet;
}

bool OAINode_add_inner::is_agent_key_Valid() const{
    return m_agent_key_isValid;
}

QString OAINode_add_inner::getHostname() const {
    return m_hostname;
}
void OAINode_add_inner::setHostname(const QString &hostname) {
    m_hostname = hostname;
    m_hostname_isSet = true;
}

bool OAINode_add_inner::is_hostname_Set() const{
    return m_hostname_isSet;
}

bool OAINode_add_inner::is_hostname_Valid() const{
    return m_hostname_isValid;
}

QString OAINode_add_inner::getId() const {
    return m_id;
}
void OAINode_add_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAINode_add_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAINode_add_inner::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAINode_add_inner::getIpAddresses() const {
    return m_ip_addresses;
}
void OAINode_add_inner::setIpAddresses(const QList<QString> &ip_addresses) {
    m_ip_addresses = ip_addresses;
    m_ip_addresses_isSet = true;
}

bool OAINode_add_inner::is_ip_addresses_Set() const{
    return m_ip_addresses_isSet;
}

bool OAINode_add_inner::is_ip_addresses_Valid() const{
    return m_ip_addresses_isValid;
}

QString OAINode_add_inner::getMachineType() const {
    return m_machine_type;
}
void OAINode_add_inner::setMachineType(const QString &machine_type) {
    m_machine_type = machine_type;
    m_machine_type_isSet = true;
}

bool OAINode_add_inner::is_machine_type_Set() const{
    return m_machine_type_isSet;
}

bool OAINode_add_inner::is_machine_type_Valid() const{
    return m_machine_type_isValid;
}

OAIOs OAINode_add_inner::getOs() const {
    return m_os;
}
void OAINode_add_inner::setOs(const OAIOs &os) {
    m_os = os;
    m_os_isSet = true;
}

bool OAINode_add_inner::is_os_Set() const{
    return m_os_isSet;
}

bool OAINode_add_inner::is_os_Valid() const{
    return m_os_isValid;
}

QString OAINode_add_inner::getPolicyMode() const {
    return m_policy_mode;
}
void OAINode_add_inner::setPolicyMode(const QString &policy_mode) {
    m_policy_mode = policy_mode;
    m_policy_mode_isSet = true;
}

bool OAINode_add_inner::is_policy_mode_Set() const{
    return m_policy_mode_isSet;
}

bool OAINode_add_inner::is_policy_mode_Valid() const{
    return m_policy_mode_isValid;
}

QString OAINode_add_inner::getPolicyServerId() const {
    return m_policy_server_id;
}
void OAINode_add_inner::setPolicyServerId(const QString &policy_server_id) {
    m_policy_server_id = policy_server_id;
    m_policy_server_id_isSet = true;
}

bool OAINode_add_inner::is_policy_server_id_Set() const{
    return m_policy_server_id_isSet;
}

bool OAINode_add_inner::is_policy_server_id_Valid() const{
    return m_policy_server_id_isValid;
}

QList<OAINode_add_inner_properties_inner> OAINode_add_inner::getProperties() const {
    return m_properties;
}
void OAINode_add_inner::setProperties(const QList<OAINode_add_inner_properties_inner> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAINode_add_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAINode_add_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAINode_add_inner::getState() const {
    return m_state;
}
void OAINode_add_inner::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAINode_add_inner::is_state_Set() const{
    return m_state_isSet;
}

bool OAINode_add_inner::is_state_Valid() const{
    return m_state_isValid;
}

QString OAINode_add_inner::getStatus() const {
    return m_status;
}
void OAINode_add_inner::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAINode_add_inner::is_status_Set() const{
    return m_status_isSet;
}

bool OAINode_add_inner::is_status_Valid() const{
    return m_status_isValid;
}

OAITimezone OAINode_add_inner::getTimezone() const {
    return m_timezone;
}
void OAINode_add_inner::setTimezone(const OAITimezone &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAINode_add_inner::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAINode_add_inner::is_timezone_Valid() const{
    return m_timezone_isValid;
}

bool OAINode_add_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agent_key.isSet()) {
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

        if (m_machine_type_isSet) {
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

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINode_add_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_hostname_isValid && m_id_isValid && m_ip_addresses_isValid && m_machine_type_isValid && m_os_isValid && m_properties_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
