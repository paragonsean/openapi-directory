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

#include "OAIUpdateUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateUser::OAIUpdateUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateUser::OAIUpdateUser() {
    this->initializeModel();
}

OAIUpdateUser::~OAIUpdateUser() {}

void OAIUpdateUser::initializeModel() {

    m_admin_flags_isSet = false;
    m_admin_flags_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_email_verified_isSet = false;
    m_email_verified_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_plugin_auth_isSet = false;
    m_plugin_auth_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_video_quota_isSet = false;
    m_video_quota_isValid = false;

    m_video_quota_daily_isSet = false;
    m_video_quota_daily_isValid = false;
}

void OAIUpdateUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateUser::fromJsonObject(QJsonObject json) {

    m_admin_flags_isValid = ::OpenAPI::fromJsonValue(m_admin_flags, json[QString("adminFlags")]);
    m_admin_flags_isSet = !json[QString("adminFlags")].isNull() && m_admin_flags_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_email_verified_isValid = ::OpenAPI::fromJsonValue(m_email_verified, json[QString("emailVerified")]);
    m_email_verified_isSet = !json[QString("emailVerified")].isNull() && m_email_verified_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_plugin_auth_isValid = ::OpenAPI::fromJsonValue(m_plugin_auth, json[QString("pluginAuth")]);
    m_plugin_auth_isSet = !json[QString("pluginAuth")].isNull() && m_plugin_auth_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_video_quota_isValid = ::OpenAPI::fromJsonValue(m_video_quota, json[QString("videoQuota")]);
    m_video_quota_isSet = !json[QString("videoQuota")].isNull() && m_video_quota_isValid;

    m_video_quota_daily_isValid = ::OpenAPI::fromJsonValue(m_video_quota_daily, json[QString("videoQuotaDaily")]);
    m_video_quota_daily_isSet = !json[QString("videoQuotaDaily")].isNull() && m_video_quota_daily_isValid;
}

QString OAIUpdateUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateUser::asJsonObject() const {
    QJsonObject obj;
    if (m_admin_flags.isSet()) {
        obj.insert(QString("adminFlags"), ::OpenAPI::toJsonValue(m_admin_flags));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_email_verified_isSet) {
        obj.insert(QString("emailVerified"), ::OpenAPI::toJsonValue(m_email_verified));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_plugin_auth_isSet) {
        obj.insert(QString("pluginAuth"), ::OpenAPI::toJsonValue(m_plugin_auth));
    }
    if (m_role.isSet()) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_video_quota_isSet) {
        obj.insert(QString("videoQuota"), ::OpenAPI::toJsonValue(m_video_quota));
    }
    if (m_video_quota_daily_isSet) {
        obj.insert(QString("videoQuotaDaily"), ::OpenAPI::toJsonValue(m_video_quota_daily));
    }
    return obj;
}

OAIUserAdminFlags OAIUpdateUser::getAdminFlags() const {
    return m_admin_flags;
}
void OAIUpdateUser::setAdminFlags(const OAIUserAdminFlags &admin_flags) {
    m_admin_flags = admin_flags;
    m_admin_flags_isSet = true;
}

bool OAIUpdateUser::is_admin_flags_Set() const{
    return m_admin_flags_isSet;
}

bool OAIUpdateUser::is_admin_flags_Valid() const{
    return m_admin_flags_isValid;
}

QString OAIUpdateUser::getEmail() const {
    return m_email;
}
void OAIUpdateUser::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUpdateUser::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUpdateUser::is_email_Valid() const{
    return m_email_isValid;
}

bool OAIUpdateUser::isEmailVerified() const {
    return m_email_verified;
}
void OAIUpdateUser::setEmailVerified(const bool &email_verified) {
    m_email_verified = email_verified;
    m_email_verified_isSet = true;
}

bool OAIUpdateUser::is_email_verified_Set() const{
    return m_email_verified_isSet;
}

bool OAIUpdateUser::is_email_verified_Valid() const{
    return m_email_verified_isValid;
}

QString OAIUpdateUser::getPassword() const {
    return m_password;
}
void OAIUpdateUser::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIUpdateUser::is_password_Set() const{
    return m_password_isSet;
}

bool OAIUpdateUser::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIUpdateUser::getPluginAuth() const {
    return m_plugin_auth;
}
void OAIUpdateUser::setPluginAuth(const QString &plugin_auth) {
    m_plugin_auth = plugin_auth;
    m_plugin_auth_isSet = true;
}

bool OAIUpdateUser::is_plugin_auth_Set() const{
    return m_plugin_auth_isSet;
}

bool OAIUpdateUser::is_plugin_auth_Valid() const{
    return m_plugin_auth_isValid;
}

OAIUserRole OAIUpdateUser::getRole() const {
    return m_role;
}
void OAIUpdateUser::setRole(const OAIUserRole &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIUpdateUser::is_role_Set() const{
    return m_role_isSet;
}

bool OAIUpdateUser::is_role_Valid() const{
    return m_role_isValid;
}

qint32 OAIUpdateUser::getVideoQuota() const {
    return m_video_quota;
}
void OAIUpdateUser::setVideoQuota(const qint32 &video_quota) {
    m_video_quota = video_quota;
    m_video_quota_isSet = true;
}

bool OAIUpdateUser::is_video_quota_Set() const{
    return m_video_quota_isSet;
}

bool OAIUpdateUser::is_video_quota_Valid() const{
    return m_video_quota_isValid;
}

qint32 OAIUpdateUser::getVideoQuotaDaily() const {
    return m_video_quota_daily;
}
void OAIUpdateUser::setVideoQuotaDaily(const qint32 &video_quota_daily) {
    m_video_quota_daily = video_quota_daily;
    m_video_quota_daily_isSet = true;
}

bool OAIUpdateUser::is_video_quota_daily_Set() const{
    return m_video_quota_daily_isSet;
}

bool OAIUpdateUser::is_video_quota_daily_Valid() const{
    return m_video_quota_daily_isValid;
}

bool OAIUpdateUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_admin_flags.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_plugin_auth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_role.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_quota_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_quota_daily_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
