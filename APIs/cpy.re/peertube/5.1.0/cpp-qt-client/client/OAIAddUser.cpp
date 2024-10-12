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

#include "OAIAddUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddUser::OAIAddUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddUser::OAIAddUser() {
    this->initializeModel();
}

OAIAddUser::~OAIAddUser() {}

void OAIAddUser::initializeModel() {

    m_admin_flags_isSet = false;
    m_admin_flags_isValid = false;

    m_channel_name_isSet = false;
    m_channel_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_video_quota_isSet = false;
    m_video_quota_isValid = false;

    m_video_quota_daily_isSet = false;
    m_video_quota_daily_isValid = false;
}

void OAIAddUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddUser::fromJsonObject(QJsonObject json) {

    m_admin_flags_isValid = ::OpenAPI::fromJsonValue(m_admin_flags, json[QString("adminFlags")]);
    m_admin_flags_isSet = !json[QString("adminFlags")].isNull() && m_admin_flags_isValid;

    m_channel_name_isValid = ::OpenAPI::fromJsonValue(m_channel_name, json[QString("channelName")]);
    m_channel_name_isSet = !json[QString("channelName")].isNull() && m_channel_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_video_quota_isValid = ::OpenAPI::fromJsonValue(m_video_quota, json[QString("videoQuota")]);
    m_video_quota_isSet = !json[QString("videoQuota")].isNull() && m_video_quota_isValid;

    m_video_quota_daily_isValid = ::OpenAPI::fromJsonValue(m_video_quota_daily, json[QString("videoQuotaDaily")]);
    m_video_quota_daily_isSet = !json[QString("videoQuotaDaily")].isNull() && m_video_quota_daily_isValid;
}

QString OAIAddUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddUser::asJsonObject() const {
    QJsonObject obj;
    if (m_admin_flags.isSet()) {
        obj.insert(QString("adminFlags"), ::OpenAPI::toJsonValue(m_admin_flags));
    }
    if (m_channel_name_isSet) {
        obj.insert(QString("channelName"), ::OpenAPI::toJsonValue(m_channel_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_role.isSet()) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_video_quota_isSet) {
        obj.insert(QString("videoQuota"), ::OpenAPI::toJsonValue(m_video_quota));
    }
    if (m_video_quota_daily_isSet) {
        obj.insert(QString("videoQuotaDaily"), ::OpenAPI::toJsonValue(m_video_quota_daily));
    }
    return obj;
}

OAIUserAdminFlags OAIAddUser::getAdminFlags() const {
    return m_admin_flags;
}
void OAIAddUser::setAdminFlags(const OAIUserAdminFlags &admin_flags) {
    m_admin_flags = admin_flags;
    m_admin_flags_isSet = true;
}

bool OAIAddUser::is_admin_flags_Set() const{
    return m_admin_flags_isSet;
}

bool OAIAddUser::is_admin_flags_Valid() const{
    return m_admin_flags_isValid;
}

QString OAIAddUser::getChannelName() const {
    return m_channel_name;
}
void OAIAddUser::setChannelName(const QString &channel_name) {
    m_channel_name = channel_name;
    m_channel_name_isSet = true;
}

bool OAIAddUser::is_channel_name_Set() const{
    return m_channel_name_isSet;
}

bool OAIAddUser::is_channel_name_Valid() const{
    return m_channel_name_isValid;
}

QString OAIAddUser::getEmail() const {
    return m_email;
}
void OAIAddUser::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAddUser::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAddUser::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIAddUser::getPassword() const {
    return m_password;
}
void OAIAddUser::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIAddUser::is_password_Set() const{
    return m_password_isSet;
}

bool OAIAddUser::is_password_Valid() const{
    return m_password_isValid;
}

OAIUserRole OAIAddUser::getRole() const {
    return m_role;
}
void OAIAddUser::setRole(const OAIUserRole &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIAddUser::is_role_Set() const{
    return m_role_isSet;
}

bool OAIAddUser::is_role_Valid() const{
    return m_role_isValid;
}

QString OAIAddUser::getUsername() const {
    return m_username;
}
void OAIAddUser::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIAddUser::is_username_Set() const{
    return m_username_isSet;
}

bool OAIAddUser::is_username_Valid() const{
    return m_username_isValid;
}

qint32 OAIAddUser::getVideoQuota() const {
    return m_video_quota;
}
void OAIAddUser::setVideoQuota(const qint32 &video_quota) {
    m_video_quota = video_quota;
    m_video_quota_isSet = true;
}

bool OAIAddUser::is_video_quota_Set() const{
    return m_video_quota_isSet;
}

bool OAIAddUser::is_video_quota_Valid() const{
    return m_video_quota_isValid;
}

qint32 OAIAddUser::getVideoQuotaDaily() const {
    return m_video_quota_daily;
}
void OAIAddUser::setVideoQuotaDaily(const qint32 &video_quota_daily) {
    m_video_quota_daily = video_quota_daily;
    m_video_quota_daily_isSet = true;
}

bool OAIAddUser::is_video_quota_daily_Set() const{
    return m_video_quota_daily_isSet;
}

bool OAIAddUser::is_video_quota_daily_Valid() const{
    return m_video_quota_daily_isValid;
}

bool OAIAddUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_admin_flags.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_role.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
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

bool OAIAddUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_isValid && m_password_isValid && m_role_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
