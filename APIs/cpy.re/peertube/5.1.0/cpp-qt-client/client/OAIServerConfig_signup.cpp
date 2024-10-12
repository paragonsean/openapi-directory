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

#include "OAIServerConfig_signup.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfig_signup::OAIServerConfig_signup(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfig_signup::OAIServerConfig_signup() {
    this->initializeModel();
}

OAIServerConfig_signup::~OAIServerConfig_signup() {}

void OAIServerConfig_signup::initializeModel() {

    m_allowed_isSet = false;
    m_allowed_isValid = false;

    m_allowed_for_current_ip_isSet = false;
    m_allowed_for_current_ip_isValid = false;

    m_requires_email_verification_isSet = false;
    m_requires_email_verification_isValid = false;
}

void OAIServerConfig_signup::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfig_signup::fromJsonObject(QJsonObject json) {

    m_allowed_isValid = ::OpenAPI::fromJsonValue(m_allowed, json[QString("allowed")]);
    m_allowed_isSet = !json[QString("allowed")].isNull() && m_allowed_isValid;

    m_allowed_for_current_ip_isValid = ::OpenAPI::fromJsonValue(m_allowed_for_current_ip, json[QString("allowedForCurrentIP")]);
    m_allowed_for_current_ip_isSet = !json[QString("allowedForCurrentIP")].isNull() && m_allowed_for_current_ip_isValid;

    m_requires_email_verification_isValid = ::OpenAPI::fromJsonValue(m_requires_email_verification, json[QString("requiresEmailVerification")]);
    m_requires_email_verification_isSet = !json[QString("requiresEmailVerification")].isNull() && m_requires_email_verification_isValid;
}

QString OAIServerConfig_signup::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfig_signup::asJsonObject() const {
    QJsonObject obj;
    if (m_allowed_isSet) {
        obj.insert(QString("allowed"), ::OpenAPI::toJsonValue(m_allowed));
    }
    if (m_allowed_for_current_ip_isSet) {
        obj.insert(QString("allowedForCurrentIP"), ::OpenAPI::toJsonValue(m_allowed_for_current_ip));
    }
    if (m_requires_email_verification_isSet) {
        obj.insert(QString("requiresEmailVerification"), ::OpenAPI::toJsonValue(m_requires_email_verification));
    }
    return obj;
}

bool OAIServerConfig_signup::isAllowed() const {
    return m_allowed;
}
void OAIServerConfig_signup::setAllowed(const bool &allowed) {
    m_allowed = allowed;
    m_allowed_isSet = true;
}

bool OAIServerConfig_signup::is_allowed_Set() const{
    return m_allowed_isSet;
}

bool OAIServerConfig_signup::is_allowed_Valid() const{
    return m_allowed_isValid;
}

bool OAIServerConfig_signup::isAllowedForCurrentIp() const {
    return m_allowed_for_current_ip;
}
void OAIServerConfig_signup::setAllowedForCurrentIp(const bool &allowed_for_current_ip) {
    m_allowed_for_current_ip = allowed_for_current_ip;
    m_allowed_for_current_ip_isSet = true;
}

bool OAIServerConfig_signup::is_allowed_for_current_ip_Set() const{
    return m_allowed_for_current_ip_isSet;
}

bool OAIServerConfig_signup::is_allowed_for_current_ip_Valid() const{
    return m_allowed_for_current_ip_isValid;
}

bool OAIServerConfig_signup::isRequiresEmailVerification() const {
    return m_requires_email_verification;
}
void OAIServerConfig_signup::setRequiresEmailVerification(const bool &requires_email_verification) {
    m_requires_email_verification = requires_email_verification;
    m_requires_email_verification_isSet = true;
}

bool OAIServerConfig_signup::is_requires_email_verification_Set() const{
    return m_requires_email_verification_isSet;
}

bool OAIServerConfig_signup::is_requires_email_verification_Valid() const{
    return m_requires_email_verification_isValid;
}

bool OAIServerConfig_signup::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allowed_for_current_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requires_email_verification_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerConfig_signup::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
