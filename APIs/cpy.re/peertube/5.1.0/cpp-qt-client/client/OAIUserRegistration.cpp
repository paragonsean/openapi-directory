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

#include "OAIUserRegistration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserRegistration::OAIUserRegistration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserRegistration::OAIUserRegistration() {
    this->initializeModel();
}

OAIUserRegistration::~OAIUserRegistration() {}

void OAIUserRegistration::initializeModel() {

    m_account_display_name_isSet = false;
    m_account_display_name_isValid = false;

    m_channel_display_name_isSet = false;
    m_channel_display_name_isValid = false;

    m_channel_handle_isSet = false;
    m_channel_handle_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_email_verified_isSet = false;
    m_email_verified_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_moderation_response_isSet = false;
    m_moderation_response_isValid = false;

    m_registration_reason_isSet = false;
    m_registration_reason_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_user_isSet = false;
    m_user_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIUserRegistration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserRegistration::fromJsonObject(QJsonObject json) {

    m_account_display_name_isValid = ::OpenAPI::fromJsonValue(m_account_display_name, json[QString("accountDisplayName")]);
    m_account_display_name_isSet = !json[QString("accountDisplayName")].isNull() && m_account_display_name_isValid;

    m_channel_display_name_isValid = ::OpenAPI::fromJsonValue(m_channel_display_name, json[QString("channelDisplayName")]);
    m_channel_display_name_isSet = !json[QString("channelDisplayName")].isNull() && m_channel_display_name_isValid;

    m_channel_handle_isValid = ::OpenAPI::fromJsonValue(m_channel_handle, json[QString("channelHandle")]);
    m_channel_handle_isSet = !json[QString("channelHandle")].isNull() && m_channel_handle_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_email_verified_isValid = ::OpenAPI::fromJsonValue(m_email_verified, json[QString("emailVerified")]);
    m_email_verified_isSet = !json[QString("emailVerified")].isNull() && m_email_verified_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_moderation_response_isValid = ::OpenAPI::fromJsonValue(m_moderation_response, json[QString("moderationResponse")]);
    m_moderation_response_isSet = !json[QString("moderationResponse")].isNull() && m_moderation_response_isValid;

    m_registration_reason_isValid = ::OpenAPI::fromJsonValue(m_registration_reason, json[QString("registrationReason")]);
    m_registration_reason_isSet = !json[QString("registrationReason")].isNull() && m_registration_reason_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_user_isValid = ::OpenAPI::fromJsonValue(m_user, json[QString("user")]);
    m_user_isSet = !json[QString("user")].isNull() && m_user_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIUserRegistration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserRegistration::asJsonObject() const {
    QJsonObject obj;
    if (m_account_display_name_isSet) {
        obj.insert(QString("accountDisplayName"), ::OpenAPI::toJsonValue(m_account_display_name));
    }
    if (m_channel_display_name_isSet) {
        obj.insert(QString("channelDisplayName"), ::OpenAPI::toJsonValue(m_channel_display_name));
    }
    if (m_channel_handle_isSet) {
        obj.insert(QString("channelHandle"), ::OpenAPI::toJsonValue(m_channel_handle));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_email_verified_isSet) {
        obj.insert(QString("emailVerified"), ::OpenAPI::toJsonValue(m_email_verified));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_moderation_response_isSet) {
        obj.insert(QString("moderationResponse"), ::OpenAPI::toJsonValue(m_moderation_response));
    }
    if (m_registration_reason_isSet) {
        obj.insert(QString("registrationReason"), ::OpenAPI::toJsonValue(m_registration_reason));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_user.isSet()) {
        obj.insert(QString("user"), ::OpenAPI::toJsonValue(m_user));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIUserRegistration::getAccountDisplayName() const {
    return m_account_display_name;
}
void OAIUserRegistration::setAccountDisplayName(const QString &account_display_name) {
    m_account_display_name = account_display_name;
    m_account_display_name_isSet = true;
}

bool OAIUserRegistration::is_account_display_name_Set() const{
    return m_account_display_name_isSet;
}

bool OAIUserRegistration::is_account_display_name_Valid() const{
    return m_account_display_name_isValid;
}

QString OAIUserRegistration::getChannelDisplayName() const {
    return m_channel_display_name;
}
void OAIUserRegistration::setChannelDisplayName(const QString &channel_display_name) {
    m_channel_display_name = channel_display_name;
    m_channel_display_name_isSet = true;
}

bool OAIUserRegistration::is_channel_display_name_Set() const{
    return m_channel_display_name_isSet;
}

bool OAIUserRegistration::is_channel_display_name_Valid() const{
    return m_channel_display_name_isValid;
}

QString OAIUserRegistration::getChannelHandle() const {
    return m_channel_handle;
}
void OAIUserRegistration::setChannelHandle(const QString &channel_handle) {
    m_channel_handle = channel_handle;
    m_channel_handle_isSet = true;
}

bool OAIUserRegistration::is_channel_handle_Set() const{
    return m_channel_handle_isSet;
}

bool OAIUserRegistration::is_channel_handle_Valid() const{
    return m_channel_handle_isValid;
}

QDateTime OAIUserRegistration::getCreatedAt() const {
    return m_created_at;
}
void OAIUserRegistration::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIUserRegistration::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIUserRegistration::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIUserRegistration::getEmail() const {
    return m_email;
}
void OAIUserRegistration::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUserRegistration::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUserRegistration::is_email_Valid() const{
    return m_email_isValid;
}

bool OAIUserRegistration::isEmailVerified() const {
    return m_email_verified;
}
void OAIUserRegistration::setEmailVerified(const bool &email_verified) {
    m_email_verified = email_verified;
    m_email_verified_isSet = true;
}

bool OAIUserRegistration::is_email_verified_Set() const{
    return m_email_verified_isSet;
}

bool OAIUserRegistration::is_email_verified_Valid() const{
    return m_email_verified_isValid;
}

qint32 OAIUserRegistration::getId() const {
    return m_id;
}
void OAIUserRegistration::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIUserRegistration::is_id_Set() const{
    return m_id_isSet;
}

bool OAIUserRegistration::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIUserRegistration::getModerationResponse() const {
    return m_moderation_response;
}
void OAIUserRegistration::setModerationResponse(const QString &moderation_response) {
    m_moderation_response = moderation_response;
    m_moderation_response_isSet = true;
}

bool OAIUserRegistration::is_moderation_response_Set() const{
    return m_moderation_response_isSet;
}

bool OAIUserRegistration::is_moderation_response_Valid() const{
    return m_moderation_response_isValid;
}

QString OAIUserRegistration::getRegistrationReason() const {
    return m_registration_reason;
}
void OAIUserRegistration::setRegistrationReason(const QString &registration_reason) {
    m_registration_reason = registration_reason;
    m_registration_reason_isSet = true;
}

bool OAIUserRegistration::is_registration_reason_Set() const{
    return m_registration_reason_isSet;
}

bool OAIUserRegistration::is_registration_reason_Valid() const{
    return m_registration_reason_isValid;
}

OAIUserRegistration_state OAIUserRegistration::getState() const {
    return m_state;
}
void OAIUserRegistration::setState(const OAIUserRegistration_state &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIUserRegistration::is_state_Set() const{
    return m_state_isSet;
}

bool OAIUserRegistration::is_state_Valid() const{
    return m_state_isValid;
}

QDateTime OAIUserRegistration::getUpdatedAt() const {
    return m_updated_at;
}
void OAIUserRegistration::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIUserRegistration::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIUserRegistration::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAIUserRegistration_user OAIUserRegistration::getUser() const {
    return m_user;
}
void OAIUserRegistration::setUser(const OAIUserRegistration_user &user) {
    m_user = user;
    m_user_isSet = true;
}

bool OAIUserRegistration::is_user_Set() const{
    return m_user_isSet;
}

bool OAIUserRegistration::is_user_Valid() const{
    return m_user_isValid;
}

QString OAIUserRegistration::getUsername() const {
    return m_username;
}
void OAIUserRegistration::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIUserRegistration::is_username_Set() const{
    return m_username_isSet;
}

bool OAIUserRegistration::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIUserRegistration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel_handle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
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

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_moderation_response_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_registration_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserRegistration::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
