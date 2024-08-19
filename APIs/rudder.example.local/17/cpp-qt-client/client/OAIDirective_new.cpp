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

#include "OAIDirective_new.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDirective_new::OAIDirective_new(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDirective_new::OAIDirective_new() {
    this->initializeModel();
}

OAIDirective_new::~OAIDirective_new() {}

void OAIDirective_new::initializeModel() {

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_long_description_isSet = false;
    m_long_description_isValid = false;

    m_parameters_isSet = false;
    m_parameters_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;

    m_short_description_isSet = false;
    m_short_description_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_system_isSet = false;
    m_system_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_technique_name_isSet = false;
    m_technique_name_isValid = false;

    m_technique_version_isSet = false;
    m_technique_version_isValid = false;
}

void OAIDirective_new::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDirective_new::fromJsonObject(QJsonObject json) {

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_long_description_isValid = ::OpenAPI::fromJsonValue(m_long_description, json[QString("longDescription")]);
    m_long_description_isSet = !json[QString("longDescription")].isNull() && m_long_description_isValid;

    m_parameters_isValid = ::OpenAPI::fromJsonValue(m_parameters, json[QString("parameters")]);
    m_parameters_isSet = !json[QString("parameters")].isNull() && m_parameters_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;

    m_short_description_isValid = ::OpenAPI::fromJsonValue(m_short_description, json[QString("shortDescription")]);
    m_short_description_isSet = !json[QString("shortDescription")].isNull() && m_short_description_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_system_isValid = ::OpenAPI::fromJsonValue(m_system, json[QString("system")]);
    m_system_isSet = !json[QString("system")].isNull() && m_system_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_technique_name_isValid = ::OpenAPI::fromJsonValue(m_technique_name, json[QString("techniqueName")]);
    m_technique_name_isSet = !json[QString("techniqueName")].isNull() && m_technique_name_isValid;

    m_technique_version_isValid = ::OpenAPI::fromJsonValue(m_technique_version, json[QString("techniqueVersion")]);
    m_technique_version_isSet = !json[QString("techniqueVersion")].isNull() && m_technique_version_isValid;
}

QString OAIDirective_new::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDirective_new::asJsonObject() const {
    QJsonObject obj;
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_long_description_isSet) {
        obj.insert(QString("longDescription"), ::OpenAPI::toJsonValue(m_long_description));
    }
    if (m_parameters_isSet) {
        obj.insert(QString("parameters"), ::OpenAPI::toJsonValue(m_parameters));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    if (m_short_description_isSet) {
        obj.insert(QString("shortDescription"), ::OpenAPI::toJsonValue(m_short_description));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_system_isSet) {
        obj.insert(QString("system"), ::OpenAPI::toJsonValue(m_system));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_technique_name_isSet) {
        obj.insert(QString("techniqueName"), ::OpenAPI::toJsonValue(m_technique_name));
    }
    if (m_technique_version_isSet) {
        obj.insert(QString("techniqueVersion"), ::OpenAPI::toJsonValue(m_technique_version));
    }
    return obj;
}

QString OAIDirective_new::getDisplayName() const {
    return m_display_name;
}
void OAIDirective_new::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIDirective_new::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIDirective_new::is_display_name_Valid() const{
    return m_display_name_isValid;
}

bool OAIDirective_new::isEnabled() const {
    return m_enabled;
}
void OAIDirective_new::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIDirective_new::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIDirective_new::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIDirective_new::getId() const {
    return m_id;
}
void OAIDirective_new::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDirective_new::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDirective_new::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIDirective_new::getLongDescription() const {
    return m_long_description;
}
void OAIDirective_new::setLongDescription(const QString &long_description) {
    m_long_description = long_description;
    m_long_description_isSet = true;
}

bool OAIDirective_new::is_long_description_Set() const{
    return m_long_description_isSet;
}

bool OAIDirective_new::is_long_description_Valid() const{
    return m_long_description_isValid;
}

OAIObject OAIDirective_new::getParameters() const {
    return m_parameters;
}
void OAIDirective_new::setParameters(const OAIObject &parameters) {
    m_parameters = parameters;
    m_parameters_isSet = true;
}

bool OAIDirective_new::is_parameters_Set() const{
    return m_parameters_isSet;
}

bool OAIDirective_new::is_parameters_Valid() const{
    return m_parameters_isValid;
}

qint32 OAIDirective_new::getPriority() const {
    return m_priority;
}
void OAIDirective_new::setPriority(const qint32 &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAIDirective_new::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAIDirective_new::is_priority_Valid() const{
    return m_priority_isValid;
}

QString OAIDirective_new::getShortDescription() const {
    return m_short_description;
}
void OAIDirective_new::setShortDescription(const QString &short_description) {
    m_short_description = short_description;
    m_short_description_isSet = true;
}

bool OAIDirective_new::is_short_description_Set() const{
    return m_short_description_isSet;
}

bool OAIDirective_new::is_short_description_Valid() const{
    return m_short_description_isValid;
}

QString OAIDirective_new::getSource() const {
    return m_source;
}
void OAIDirective_new::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIDirective_new::is_source_Set() const{
    return m_source_isSet;
}

bool OAIDirective_new::is_source_Valid() const{
    return m_source_isValid;
}

bool OAIDirective_new::isSystem() const {
    return m_system;
}
void OAIDirective_new::setSystem(const bool &system) {
    m_system = system;
    m_system_isSet = true;
}

bool OAIDirective_new::is_system_Set() const{
    return m_system_isSet;
}

bool OAIDirective_new::is_system_Valid() const{
    return m_system_isValid;
}

QList<OAIDirective_tags_inner> OAIDirective_new::getTags() const {
    return m_tags;
}
void OAIDirective_new::setTags(const QList<OAIDirective_tags_inner> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIDirective_new::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIDirective_new::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIDirective_new::getTechniqueName() const {
    return m_technique_name;
}
void OAIDirective_new::setTechniqueName(const QString &technique_name) {
    m_technique_name = technique_name;
    m_technique_name_isSet = true;
}

bool OAIDirective_new::is_technique_name_Set() const{
    return m_technique_name_isSet;
}

bool OAIDirective_new::is_technique_name_Valid() const{
    return m_technique_name_isValid;
}

QString OAIDirective_new::getTechniqueVersion() const {
    return m_technique_version;
}
void OAIDirective_new::setTechniqueVersion(const QString &technique_version) {
    m_technique_version = technique_version;
    m_technique_version_isSet = true;
}

bool OAIDirective_new::is_technique_version_Set() const{
    return m_technique_version_isSet;
}

bool OAIDirective_new::is_technique_version_Valid() const{
    return m_technique_version_isValid;
}

bool OAIDirective_new::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_long_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parameters_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_system_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_technique_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_technique_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDirective_new::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
