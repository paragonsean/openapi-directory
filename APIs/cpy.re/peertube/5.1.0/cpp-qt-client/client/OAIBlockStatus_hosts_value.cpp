/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBlockStatus_hosts_value.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBlockStatus_hosts_value::OAIBlockStatus_hosts_value(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBlockStatus_hosts_value::OAIBlockStatus_hosts_value() {
    this->initializeModel();
}

OAIBlockStatus_hosts_value::~OAIBlockStatus_hosts_value() {}

void OAIBlockStatus_hosts_value::initializeModel() {

    m_blocked_by_server_isSet = false;
    m_blocked_by_server_isValid = false;

    m_blocked_by_user_isSet = false;
    m_blocked_by_user_isValid = false;
}

void OAIBlockStatus_hosts_value::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBlockStatus_hosts_value::fromJsonObject(QJsonObject json) {

    m_blocked_by_server_isValid = ::OpenAPI::fromJsonValue(m_blocked_by_server, json[QString("blockedByServer")]);
    m_blocked_by_server_isSet = !json[QString("blockedByServer")].isNull() && m_blocked_by_server_isValid;

    m_blocked_by_user_isValid = ::OpenAPI::fromJsonValue(m_blocked_by_user, json[QString("blockedByUser")]);
    m_blocked_by_user_isSet = !json[QString("blockedByUser")].isNull() && m_blocked_by_user_isValid;
}

QString OAIBlockStatus_hosts_value::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBlockStatus_hosts_value::asJsonObject() const {
    QJsonObject obj;
    if (m_blocked_by_server_isSet) {
        obj.insert(QString("blockedByServer"), ::OpenAPI::toJsonValue(m_blocked_by_server));
    }
    if (m_blocked_by_user_isSet) {
        obj.insert(QString("blockedByUser"), ::OpenAPI::toJsonValue(m_blocked_by_user));
    }
    return obj;
}

bool OAIBlockStatus_hosts_value::isBlockedByServer() const {
    return m_blocked_by_server;
}
void OAIBlockStatus_hosts_value::setBlockedByServer(const bool &blocked_by_server) {
    m_blocked_by_server = blocked_by_server;
    m_blocked_by_server_isSet = true;
}

bool OAIBlockStatus_hosts_value::is_blocked_by_server_Set() const{
    return m_blocked_by_server_isSet;
}

bool OAIBlockStatus_hosts_value::is_blocked_by_server_Valid() const{
    return m_blocked_by_server_isValid;
}

bool OAIBlockStatus_hosts_value::isBlockedByUser() const {
    return m_blocked_by_user;
}
void OAIBlockStatus_hosts_value::setBlockedByUser(const bool &blocked_by_user) {
    m_blocked_by_user = blocked_by_user;
    m_blocked_by_user_isSet = true;
}

bool OAIBlockStatus_hosts_value::is_blocked_by_user_Set() const{
    return m_blocked_by_user_isSet;
}

bool OAIBlockStatus_hosts_value::is_blocked_by_user_Valid() const{
    return m_blocked_by_user_isValid;
}

bool OAIBlockStatus_hosts_value::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_blocked_by_server_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blocked_by_user_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBlockStatus_hosts_value::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
