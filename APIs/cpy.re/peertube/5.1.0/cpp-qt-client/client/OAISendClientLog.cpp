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

#include "OAISendClientLog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISendClientLog::OAISendClientLog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISendClientLog::OAISendClientLog() {
    this->initializeModel();
}

OAISendClientLog::~OAISendClientLog() {}

void OAISendClientLog::initializeModel() {

    m_level_isSet = false;
    m_level_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_meta_isSet = false;
    m_meta_isValid = false;

    m_stack_trace_isSet = false;
    m_stack_trace_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_user_agent_isSet = false;
    m_user_agent_isValid = false;
}

void OAISendClientLog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISendClientLog::fromJsonObject(QJsonObject json) {

    m_level_isValid = ::OpenAPI::fromJsonValue(m_level, json[QString("level")]);
    m_level_isSet = !json[QString("level")].isNull() && m_level_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_meta_isValid = ::OpenAPI::fromJsonValue(m_meta, json[QString("meta")]);
    m_meta_isSet = !json[QString("meta")].isNull() && m_meta_isValid;

    m_stack_trace_isValid = ::OpenAPI::fromJsonValue(m_stack_trace, json[QString("stackTrace")]);
    m_stack_trace_isSet = !json[QString("stackTrace")].isNull() && m_stack_trace_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_user_agent_isValid = ::OpenAPI::fromJsonValue(m_user_agent, json[QString("userAgent")]);
    m_user_agent_isSet = !json[QString("userAgent")].isNull() && m_user_agent_isValid;
}

QString OAISendClientLog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISendClientLog::asJsonObject() const {
    QJsonObject obj;
    if (m_level_isSet) {
        obj.insert(QString("level"), ::OpenAPI::toJsonValue(m_level));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_meta_isSet) {
        obj.insert(QString("meta"), ::OpenAPI::toJsonValue(m_meta));
    }
    if (m_stack_trace_isSet) {
        obj.insert(QString("stackTrace"), ::OpenAPI::toJsonValue(m_stack_trace));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_user_agent_isSet) {
        obj.insert(QString("userAgent"), ::OpenAPI::toJsonValue(m_user_agent));
    }
    return obj;
}

QString OAISendClientLog::getLevel() const {
    return m_level;
}
void OAISendClientLog::setLevel(const QString &level) {
    m_level = level;
    m_level_isSet = true;
}

bool OAISendClientLog::is_level_Set() const{
    return m_level_isSet;
}

bool OAISendClientLog::is_level_Valid() const{
    return m_level_isValid;
}

QString OAISendClientLog::getMessage() const {
    return m_message;
}
void OAISendClientLog::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAISendClientLog::is_message_Set() const{
    return m_message_isSet;
}

bool OAISendClientLog::is_message_Valid() const{
    return m_message_isValid;
}

QString OAISendClientLog::getMeta() const {
    return m_meta;
}
void OAISendClientLog::setMeta(const QString &meta) {
    m_meta = meta;
    m_meta_isSet = true;
}

bool OAISendClientLog::is_meta_Set() const{
    return m_meta_isSet;
}

bool OAISendClientLog::is_meta_Valid() const{
    return m_meta_isValid;
}

QString OAISendClientLog::getStackTrace() const {
    return m_stack_trace;
}
void OAISendClientLog::setStackTrace(const QString &stack_trace) {
    m_stack_trace = stack_trace;
    m_stack_trace_isSet = true;
}

bool OAISendClientLog::is_stack_trace_Set() const{
    return m_stack_trace_isSet;
}

bool OAISendClientLog::is_stack_trace_Valid() const{
    return m_stack_trace_isValid;
}

QString OAISendClientLog::getUrl() const {
    return m_url;
}
void OAISendClientLog::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAISendClientLog::is_url_Set() const{
    return m_url_isSet;
}

bool OAISendClientLog::is_url_Valid() const{
    return m_url_isValid;
}

QString OAISendClientLog::getUserAgent() const {
    return m_user_agent;
}
void OAISendClientLog::setUserAgent(const QString &user_agent) {
    m_user_agent = user_agent;
    m_user_agent_isSet = true;
}

bool OAISendClientLog::is_user_agent_Set() const{
    return m_user_agent_isSet;
}

bool OAISendClientLog::is_user_agent_Valid() const{
    return m_user_agent_isValid;
}

bool OAISendClientLog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stack_trace_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_agent_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISendClientLog::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_level_isValid && m_message_isValid && m_url_isValid && true;
}

} // namespace OpenAPI
