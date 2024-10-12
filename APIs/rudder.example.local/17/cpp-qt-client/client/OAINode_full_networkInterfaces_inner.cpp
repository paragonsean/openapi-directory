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

#include "OAINode_full_networkInterfaces_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINode_full_networkInterfaces_inner::OAINode_full_networkInterfaces_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINode_full_networkInterfaces_inner::OAINode_full_networkInterfaces_inner() {
    this->initializeModel();
}

OAINode_full_networkInterfaces_inner::~OAINode_full_networkInterfaces_inner() {}

void OAINode_full_networkInterfaces_inner::initializeModel() {

    m_dhcp_server_isSet = false;
    m_dhcp_server_isValid = false;

    m_ip_addresses_isSet = false;
    m_ip_addresses_isValid = false;

    m_mac_address_isSet = false;
    m_mac_address_isValid = false;

    m_mask_isSet = false;
    m_mask_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_speed_isSet = false;
    m_speed_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAINode_full_networkInterfaces_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINode_full_networkInterfaces_inner::fromJsonObject(QJsonObject json) {

    m_dhcp_server_isValid = ::OpenAPI::fromJsonValue(m_dhcp_server, json[QString("dhcpServer")]);
    m_dhcp_server_isSet = !json[QString("dhcpServer")].isNull() && m_dhcp_server_isValid;

    m_ip_addresses_isValid = ::OpenAPI::fromJsonValue(m_ip_addresses, json[QString("ipAddresses")]);
    m_ip_addresses_isSet = !json[QString("ipAddresses")].isNull() && m_ip_addresses_isValid;

    m_mac_address_isValid = ::OpenAPI::fromJsonValue(m_mac_address, json[QString("macAddress")]);
    m_mac_address_isSet = !json[QString("macAddress")].isNull() && m_mac_address_isValid;

    m_mask_isValid = ::OpenAPI::fromJsonValue(m_mask, json[QString("mask")]);
    m_mask_isSet = !json[QString("mask")].isNull() && m_mask_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_speed_isValid = ::OpenAPI::fromJsonValue(m_speed, json[QString("speed")]);
    m_speed_isSet = !json[QString("speed")].isNull() && m_speed_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAINode_full_networkInterfaces_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINode_full_networkInterfaces_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_dhcp_server_isSet) {
        obj.insert(QString("dhcpServer"), ::OpenAPI::toJsonValue(m_dhcp_server));
    }
    if (m_ip_addresses.size() > 0) {
        obj.insert(QString("ipAddresses"), ::OpenAPI::toJsonValue(m_ip_addresses));
    }
    if (m_mac_address_isSet) {
        obj.insert(QString("macAddress"), ::OpenAPI::toJsonValue(m_mac_address));
    }
    if (m_mask.size() > 0) {
        obj.insert(QString("mask"), ::OpenAPI::toJsonValue(m_mask));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_speed_isSet) {
        obj.insert(QString("speed"), ::OpenAPI::toJsonValue(m_speed));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAINode_full_networkInterfaces_inner::getDhcpServer() const {
    return m_dhcp_server;
}
void OAINode_full_networkInterfaces_inner::setDhcpServer(const QString &dhcp_server) {
    m_dhcp_server = dhcp_server;
    m_dhcp_server_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_dhcp_server_Set() const{
    return m_dhcp_server_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_dhcp_server_Valid() const{
    return m_dhcp_server_isValid;
}

QList<QString> OAINode_full_networkInterfaces_inner::getIpAddresses() const {
    return m_ip_addresses;
}
void OAINode_full_networkInterfaces_inner::setIpAddresses(const QList<QString> &ip_addresses) {
    m_ip_addresses = ip_addresses;
    m_ip_addresses_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_ip_addresses_Set() const{
    return m_ip_addresses_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_ip_addresses_Valid() const{
    return m_ip_addresses_isValid;
}

QString OAINode_full_networkInterfaces_inner::getMacAddress() const {
    return m_mac_address;
}
void OAINode_full_networkInterfaces_inner::setMacAddress(const QString &mac_address) {
    m_mac_address = mac_address;
    m_mac_address_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_mac_address_Set() const{
    return m_mac_address_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_mac_address_Valid() const{
    return m_mac_address_isValid;
}

QList<QString> OAINode_full_networkInterfaces_inner::getMask() const {
    return m_mask;
}
void OAINode_full_networkInterfaces_inner::setMask(const QList<QString> &mask) {
    m_mask = mask;
    m_mask_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_mask_Set() const{
    return m_mask_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_mask_Valid() const{
    return m_mask_isValid;
}

QString OAINode_full_networkInterfaces_inner::getName() const {
    return m_name;
}
void OAINode_full_networkInterfaces_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAINode_full_networkInterfaces_inner::getSpeed() const {
    return m_speed;
}
void OAINode_full_networkInterfaces_inner::setSpeed(const QString &speed) {
    m_speed = speed;
    m_speed_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_speed_Set() const{
    return m_speed_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_speed_Valid() const{
    return m_speed_isValid;
}

QString OAINode_full_networkInterfaces_inner::getStatus() const {
    return m_status;
}
void OAINode_full_networkInterfaces_inner::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_status_Set() const{
    return m_status_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_status_Valid() const{
    return m_status_isValid;
}

QString OAINode_full_networkInterfaces_inner::getType() const {
    return m_type;
}
void OAINode_full_networkInterfaces_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAINode_full_networkInterfaces_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAINode_full_networkInterfaces_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAINode_full_networkInterfaces_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dhcp_server_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_mac_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mask.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_speed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINode_full_networkInterfaces_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
