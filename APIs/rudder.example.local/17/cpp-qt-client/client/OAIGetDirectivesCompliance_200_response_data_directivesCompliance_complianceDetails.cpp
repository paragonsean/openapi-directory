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

#include "OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails() {
    this->initializeModel();
}

OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::~OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails() {}

void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_no_report_isSet = false;
    m_no_report_isValid = false;

    m_success_already_ok_isSet = false;
    m_success_already_ok_isValid = false;

    m_success_not_applicable_isSet = false;
    m_success_not_applicable_isValid = false;

    m_success_repaired_isSet = false;
    m_success_repaired_isValid = false;

    m_unexpected_missing_component_isSet = false;
    m_unexpected_missing_component_isValid = false;

    m_unexpected_unknown_component_isSet = false;
    m_unexpected_unknown_component_isValid = false;
}

void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_no_report_isValid = ::OpenAPI::fromJsonValue(m_no_report, json[QString("noReport")]);
    m_no_report_isSet = !json[QString("noReport")].isNull() && m_no_report_isValid;

    m_success_already_ok_isValid = ::OpenAPI::fromJsonValue(m_success_already_ok, json[QString("successAlreadyOK")]);
    m_success_already_ok_isSet = !json[QString("successAlreadyOK")].isNull() && m_success_already_ok_isValid;

    m_success_not_applicable_isValid = ::OpenAPI::fromJsonValue(m_success_not_applicable, json[QString("successNotApplicable")]);
    m_success_not_applicable_isSet = !json[QString("successNotApplicable")].isNull() && m_success_not_applicable_isValid;

    m_success_repaired_isValid = ::OpenAPI::fromJsonValue(m_success_repaired, json[QString("successRepaired")]);
    m_success_repaired_isSet = !json[QString("successRepaired")].isNull() && m_success_repaired_isValid;

    m_unexpected_missing_component_isValid = ::OpenAPI::fromJsonValue(m_unexpected_missing_component, json[QString("unexpectedMissingComponent")]);
    m_unexpected_missing_component_isSet = !json[QString("unexpectedMissingComponent")].isNull() && m_unexpected_missing_component_isValid;

    m_unexpected_unknown_component_isValid = ::OpenAPI::fromJsonValue(m_unexpected_unknown_component, json[QString("unexpectedUnknownComponent")]);
    m_unexpected_unknown_component_isSet = !json[QString("unexpectedUnknownComponent")].isNull() && m_unexpected_unknown_component_isValid;
}

QString OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_no_report_isSet) {
        obj.insert(QString("noReport"), ::OpenAPI::toJsonValue(m_no_report));
    }
    if (m_success_already_ok_isSet) {
        obj.insert(QString("successAlreadyOK"), ::OpenAPI::toJsonValue(m_success_already_ok));
    }
    if (m_success_not_applicable_isSet) {
        obj.insert(QString("successNotApplicable"), ::OpenAPI::toJsonValue(m_success_not_applicable));
    }
    if (m_success_repaired_isSet) {
        obj.insert(QString("successRepaired"), ::OpenAPI::toJsonValue(m_success_repaired));
    }
    if (m_unexpected_missing_component_isSet) {
        obj.insert(QString("unexpectedMissingComponent"), ::OpenAPI::toJsonValue(m_unexpected_missing_component));
    }
    if (m_unexpected_unknown_component_isSet) {
        obj.insert(QString("unexpectedUnknownComponent"), ::OpenAPI::toJsonValue(m_unexpected_unknown_component));
    }
    return obj;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getError() const {
    return m_error;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setError(const float &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_error_Set() const{
    return m_error_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_error_Valid() const{
    return m_error_isValid;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getNoReport() const {
    return m_no_report;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setNoReport(const float &no_report) {
    m_no_report = no_report;
    m_no_report_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_no_report_Set() const{
    return m_no_report_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_no_report_Valid() const{
    return m_no_report_isValid;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getSuccessAlreadyOk() const {
    return m_success_already_ok;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setSuccessAlreadyOk(const float &success_already_ok) {
    m_success_already_ok = success_already_ok;
    m_success_already_ok_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_success_already_ok_Set() const{
    return m_success_already_ok_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_success_already_ok_Valid() const{
    return m_success_already_ok_isValid;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getSuccessNotApplicable() const {
    return m_success_not_applicable;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setSuccessNotApplicable(const float &success_not_applicable) {
    m_success_not_applicable = success_not_applicable;
    m_success_not_applicable_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_success_not_applicable_Set() const{
    return m_success_not_applicable_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_success_not_applicable_Valid() const{
    return m_success_not_applicable_isValid;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getSuccessRepaired() const {
    return m_success_repaired;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setSuccessRepaired(const float &success_repaired) {
    m_success_repaired = success_repaired;
    m_success_repaired_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_success_repaired_Set() const{
    return m_success_repaired_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_success_repaired_Valid() const{
    return m_success_repaired_isValid;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getUnexpectedMissingComponent() const {
    return m_unexpected_missing_component;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setUnexpectedMissingComponent(const float &unexpected_missing_component) {
    m_unexpected_missing_component = unexpected_missing_component;
    m_unexpected_missing_component_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_unexpected_missing_component_Set() const{
    return m_unexpected_missing_component_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_unexpected_missing_component_Valid() const{
    return m_unexpected_missing_component_isValid;
}

float OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::getUnexpectedUnknownComponent() const {
    return m_unexpected_unknown_component;
}
void OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::setUnexpectedUnknownComponent(const float &unexpected_unknown_component) {
    m_unexpected_unknown_component = unexpected_unknown_component;
    m_unexpected_unknown_component_isSet = true;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_unexpected_unknown_component_Set() const{
    return m_unexpected_unknown_component_isSet;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::is_unexpected_unknown_component_Valid() const{
    return m_unexpected_unknown_component_isValid;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_report_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_already_ok_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_not_applicable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_repaired_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unexpected_missing_component_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unexpected_unknown_component_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetDirectivesCompliance_200_response_data_directivesCompliance_complianceDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
