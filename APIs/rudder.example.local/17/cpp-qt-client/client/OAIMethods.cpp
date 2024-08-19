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

#include "OAIMethods.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMethods::OAIMethods(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMethods::OAIMethods() {
    this->initializeModel();
}

OAIMethods::~OAIMethods() {}

void OAIMethods::initializeModel() {

    m_agents_isSet = false;
    m_agents_isValid = false;

    m_category_isSet = false;
    m_category_isValid = false;

    m_condition_isSet = false;
    m_condition_isValid = false;

    m_deprecated_isSet = false;
    m_deprecated_isValid = false;

    m_desc_isSet = false;
    m_desc_isValid = false;

    m_documentation_isSet = false;
    m_documentation_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parameters_isSet = false;
    m_parameters_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIMethods::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMethods::fromJsonObject(QJsonObject json) {

    m_agents_isValid = ::OpenAPI::fromJsonValue(m_agents, json[QString("agents")]);
    m_agents_isSet = !json[QString("agents")].isNull() && m_agents_isValid;

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_condition_isValid = ::OpenAPI::fromJsonValue(m_condition, json[QString("condition")]);
    m_condition_isSet = !json[QString("condition")].isNull() && m_condition_isValid;

    m_deprecated_isValid = ::OpenAPI::fromJsonValue(m_deprecated, json[QString("deprecated")]);
    m_deprecated_isSet = !json[QString("deprecated")].isNull() && m_deprecated_isValid;

    m_desc_isValid = ::OpenAPI::fromJsonValue(m_desc, json[QString("desc")]);
    m_desc_isSet = !json[QString("desc")].isNull() && m_desc_isValid;

    m_documentation_isValid = ::OpenAPI::fromJsonValue(m_documentation, json[QString("documentation")]);
    m_documentation_isSet = !json[QString("documentation")].isNull() && m_documentation_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parameters_isValid = ::OpenAPI::fromJsonValue(m_parameters, json[QString("parameters")]);
    m_parameters_isSet = !json[QString("parameters")].isNull() && m_parameters_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIMethods::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMethods::asJsonObject() const {
    QJsonObject obj;
    if (m_agents.size() > 0) {
        obj.insert(QString("agents"), ::OpenAPI::toJsonValue(m_agents));
    }
    if (m_category_isSet) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_condition.isSet()) {
        obj.insert(QString("condition"), ::OpenAPI::toJsonValue(m_condition));
    }
    if (m_deprecated.isSet()) {
        obj.insert(QString("deprecated"), ::OpenAPI::toJsonValue(m_deprecated));
    }
    if (m_desc_isSet) {
        obj.insert(QString("desc"), ::OpenAPI::toJsonValue(m_desc));
    }
    if (m_documentation_isSet) {
        obj.insert(QString("documentation"), ::OpenAPI::toJsonValue(m_documentation));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parameters.size() > 0) {
        obj.insert(QString("parameters"), ::OpenAPI::toJsonValue(m_parameters));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QList<QString> OAIMethods::getAgents() const {
    return m_agents;
}
void OAIMethods::setAgents(const QList<QString> &agents) {
    m_agents = agents;
    m_agents_isSet = true;
}

bool OAIMethods::is_agents_Set() const{
    return m_agents_isSet;
}

bool OAIMethods::is_agents_Valid() const{
    return m_agents_isValid;
}

QString OAIMethods::getCategory() const {
    return m_category;
}
void OAIMethods::setCategory(const QString &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIMethods::is_category_Set() const{
    return m_category_isSet;
}

bool OAIMethods::is_category_Valid() const{
    return m_category_isValid;
}

OAIMethods_condition OAIMethods::getCondition() const {
    return m_condition;
}
void OAIMethods::setCondition(const OAIMethods_condition &condition) {
    m_condition = condition;
    m_condition_isSet = true;
}

bool OAIMethods::is_condition_Set() const{
    return m_condition_isSet;
}

bool OAIMethods::is_condition_Valid() const{
    return m_condition_isValid;
}

OAIMethods_deprecated OAIMethods::getDeprecated() const {
    return m_deprecated;
}
void OAIMethods::setDeprecated(const OAIMethods_deprecated &deprecated) {
    m_deprecated = deprecated;
    m_deprecated_isSet = true;
}

bool OAIMethods::is_deprecated_Set() const{
    return m_deprecated_isSet;
}

bool OAIMethods::is_deprecated_Valid() const{
    return m_deprecated_isValid;
}

QString OAIMethods::getDesc() const {
    return m_desc;
}
void OAIMethods::setDesc(const QString &desc) {
    m_desc = desc;
    m_desc_isSet = true;
}

bool OAIMethods::is_desc_Set() const{
    return m_desc_isSet;
}

bool OAIMethods::is_desc_Valid() const{
    return m_desc_isValid;
}

QString OAIMethods::getDocumentation() const {
    return m_documentation;
}
void OAIMethods::setDocumentation(const QString &documentation) {
    m_documentation = documentation;
    m_documentation_isSet = true;
}

bool OAIMethods::is_documentation_Set() const{
    return m_documentation_isSet;
}

bool OAIMethods::is_documentation_Valid() const{
    return m_documentation_isValid;
}

QString OAIMethods::getId() const {
    return m_id;
}
void OAIMethods::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIMethods::is_id_Set() const{
    return m_id_isSet;
}

bool OAIMethods::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIMethods::getName() const {
    return m_name;
}
void OAIMethods::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIMethods::is_name_Set() const{
    return m_name_isSet;
}

bool OAIMethods::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIMethod_parameter> OAIMethods::getParameters() const {
    return m_parameters;
}
void OAIMethods::setParameters(const QList<OAIMethod_parameter> &parameters) {
    m_parameters = parameters;
    m_parameters_isSet = true;
}

bool OAIMethods::is_parameters_Set() const{
    return m_parameters_isSet;
}

bool OAIMethods::is_parameters_Valid() const{
    return m_parameters_isValid;
}

QString OAIMethods::getVersion() const {
    return m_version;
}
void OAIMethods::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIMethods::is_version_Set() const{
    return m_version_isSet;
}

bool OAIMethods::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIMethods::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agents.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_condition.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_deprecated.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_desc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_documentation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parameters.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMethods::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_agents_isValid && m_category_isValid && m_condition_isValid && m_deprecated_isValid && m_desc_isValid && m_documentation_isValid && m_id_isValid && m_name_isValid && m_parameters_isValid && m_version_isValid && true;
}

} // namespace OpenAPI
