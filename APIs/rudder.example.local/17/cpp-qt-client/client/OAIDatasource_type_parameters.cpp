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

#include "OAIDatasource_type_parameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDatasource_type_parameters::OAIDatasource_type_parameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDatasource_type_parameters::OAIDatasource_type_parameters() {
    this->initializeModel();
}

OAIDatasource_type_parameters::~OAIDatasource_type_parameters() {}

void OAIDatasource_type_parameters::initializeModel() {

    m_check_ssl_isSet = false;
    m_check_ssl_isValid = false;

    m_headers_isSet = false;
    m_headers_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;

    m_request_method_isSet = false;
    m_request_method_isValid = false;

    m_request_mode_isSet = false;
    m_request_mode_isValid = false;

    m_request_timeout_isSet = false;
    m_request_timeout_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIDatasource_type_parameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDatasource_type_parameters::fromJsonObject(QJsonObject json) {

    m_check_ssl_isValid = ::OpenAPI::fromJsonValue(m_check_ssl, json[QString("checkSsl")]);
    m_check_ssl_isSet = !json[QString("checkSsl")].isNull() && m_check_ssl_isValid;

    m_headers_isValid = ::OpenAPI::fromJsonValue(m_headers, json[QString("headers")]);
    m_headers_isSet = !json[QString("headers")].isNull() && m_headers_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;

    m_request_method_isValid = ::OpenAPI::fromJsonValue(m_request_method, json[QString("requestMethod")]);
    m_request_method_isSet = !json[QString("requestMethod")].isNull() && m_request_method_isValid;

    m_request_mode_isValid = ::OpenAPI::fromJsonValue(m_request_mode, json[QString("requestMode")]);
    m_request_mode_isSet = !json[QString("requestMode")].isNull() && m_request_mode_isValid;

    m_request_timeout_isValid = ::OpenAPI::fromJsonValue(m_request_timeout, json[QString("requestTimeout")]);
    m_request_timeout_isSet = !json[QString("requestTimeout")].isNull() && m_request_timeout_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIDatasource_type_parameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDatasource_type_parameters::asJsonObject() const {
    QJsonObject obj;
    if (m_check_ssl_isSet) {
        obj.insert(QString("checkSsl"), ::OpenAPI::toJsonValue(m_check_ssl));
    }
    if (m_headers.size() > 0) {
        obj.insert(QString("headers"), ::OpenAPI::toJsonValue(m_headers));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    if (m_request_method_isSet) {
        obj.insert(QString("requestMethod"), ::OpenAPI::toJsonValue(m_request_method));
    }
    if (m_request_mode.isSet()) {
        obj.insert(QString("requestMode"), ::OpenAPI::toJsonValue(m_request_mode));
    }
    if (m_request_timeout_isSet) {
        obj.insert(QString("requestTimeout"), ::OpenAPI::toJsonValue(m_request_timeout));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

bool OAIDatasource_type_parameters::isCheckSsl() const {
    return m_check_ssl;
}
void OAIDatasource_type_parameters::setCheckSsl(const bool &check_ssl) {
    m_check_ssl = check_ssl;
    m_check_ssl_isSet = true;
}

bool OAIDatasource_type_parameters::is_check_ssl_Set() const{
    return m_check_ssl_isSet;
}

bool OAIDatasource_type_parameters::is_check_ssl_Valid() const{
    return m_check_ssl_isValid;
}

QList<OAIDatasource_type_parameters_headers_inner> OAIDatasource_type_parameters::getHeaders() const {
    return m_headers;
}
void OAIDatasource_type_parameters::setHeaders(const QList<OAIDatasource_type_parameters_headers_inner> &headers) {
    m_headers = headers;
    m_headers_isSet = true;
}

bool OAIDatasource_type_parameters::is_headers_Set() const{
    return m_headers_isSet;
}

bool OAIDatasource_type_parameters::is_headers_Valid() const{
    return m_headers_isValid;
}

QString OAIDatasource_type_parameters::getPath() const {
    return m_path;
}
void OAIDatasource_type_parameters::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAIDatasource_type_parameters::is_path_Set() const{
    return m_path_isSet;
}

bool OAIDatasource_type_parameters::is_path_Valid() const{
    return m_path_isValid;
}

QString OAIDatasource_type_parameters::getRequestMethod() const {
    return m_request_method;
}
void OAIDatasource_type_parameters::setRequestMethod(const QString &request_method) {
    m_request_method = request_method;
    m_request_method_isSet = true;
}

bool OAIDatasource_type_parameters::is_request_method_Set() const{
    return m_request_method_isSet;
}

bool OAIDatasource_type_parameters::is_request_method_Valid() const{
    return m_request_method_isValid;
}

OAIDatasource_type_parameters_requestMode OAIDatasource_type_parameters::getRequestMode() const {
    return m_request_mode;
}
void OAIDatasource_type_parameters::setRequestMode(const OAIDatasource_type_parameters_requestMode &request_mode) {
    m_request_mode = request_mode;
    m_request_mode_isSet = true;
}

bool OAIDatasource_type_parameters::is_request_mode_Set() const{
    return m_request_mode_isSet;
}

bool OAIDatasource_type_parameters::is_request_mode_Valid() const{
    return m_request_mode_isValid;
}

qint32 OAIDatasource_type_parameters::getRequestTimeout() const {
    return m_request_timeout;
}
void OAIDatasource_type_parameters::setRequestTimeout(const qint32 &request_timeout) {
    m_request_timeout = request_timeout;
    m_request_timeout_isSet = true;
}

bool OAIDatasource_type_parameters::is_request_timeout_Set() const{
    return m_request_timeout_isSet;
}

bool OAIDatasource_type_parameters::is_request_timeout_Valid() const{
    return m_request_timeout_isValid;
}

QString OAIDatasource_type_parameters::getUrl() const {
    return m_url;
}
void OAIDatasource_type_parameters::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIDatasource_type_parameters::is_url_Set() const{
    return m_url_isSet;
}

bool OAIDatasource_type_parameters::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIDatasource_type_parameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_check_ssl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_headers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_mode.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDatasource_type_parameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
