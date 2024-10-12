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

#include "OAIGetUser_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetUser_200_response::OAIGetUser_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetUser_200_response::OAIGetUser_200_response() {
    this->initializeModel();
}

OAIGetUser_200_response::~OAIGetUser_200_response() {}

void OAIGetUser_200_response::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_auto_play_next_video_isSet = false;
    m_auto_play_next_video_isValid = false;

    m_auto_play_next_video_playlist_isSet = false;
    m_auto_play_next_video_playlist_isValid = false;

    m_auto_play_video_isSet = false;
    m_auto_play_video_isValid = false;

    m_blocked_isSet = false;
    m_blocked_isValid = false;

    m_blocked_reason_isSet = false;
    m_blocked_reason_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_email_verified_isSet = false;
    m_email_verified_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_login_date_isSet = false;
    m_last_login_date_isValid = false;

    m_no_account_setup_warning_modal_isSet = false;
    m_no_account_setup_warning_modal_isValid = false;

    m_no_instance_config_warning_modal_isSet = false;
    m_no_instance_config_warning_modal_isValid = false;

    m_no_welcome_modal_isSet = false;
    m_no_welcome_modal_isValid = false;

    m_nsfw_policy_isSet = false;
    m_nsfw_policy_isValid = false;

    m_p2p_enabled_isSet = false;
    m_p2p_enabled_isValid = false;

    m_plugin_auth_isSet = false;
    m_plugin_auth_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_video_channels_isSet = false;
    m_video_channels_isValid = false;

    m_video_quota_isSet = false;
    m_video_quota_isValid = false;

    m_video_quota_daily_isSet = false;
    m_video_quota_daily_isValid = false;

    m_abuses_accepted_count_isSet = false;
    m_abuses_accepted_count_isValid = false;

    m_abuses_count_isSet = false;
    m_abuses_count_isValid = false;

    m_abuses_created_count_isSet = false;
    m_abuses_created_count_isValid = false;

    m_video_comments_count_isSet = false;
    m_video_comments_count_isValid = false;

    m_videos_count_isSet = false;
    m_videos_count_isValid = false;
}

void OAIGetUser_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetUser_200_response::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_auto_play_next_video_isValid = ::OpenAPI::fromJsonValue(m_auto_play_next_video, json[QString("autoPlayNextVideo")]);
    m_auto_play_next_video_isSet = !json[QString("autoPlayNextVideo")].isNull() && m_auto_play_next_video_isValid;

    m_auto_play_next_video_playlist_isValid = ::OpenAPI::fromJsonValue(m_auto_play_next_video_playlist, json[QString("autoPlayNextVideoPlaylist")]);
    m_auto_play_next_video_playlist_isSet = !json[QString("autoPlayNextVideoPlaylist")].isNull() && m_auto_play_next_video_playlist_isValid;

    m_auto_play_video_isValid = ::OpenAPI::fromJsonValue(m_auto_play_video, json[QString("autoPlayVideo")]);
    m_auto_play_video_isSet = !json[QString("autoPlayVideo")].isNull() && m_auto_play_video_isValid;

    m_blocked_isValid = ::OpenAPI::fromJsonValue(m_blocked, json[QString("blocked")]);
    m_blocked_isSet = !json[QString("blocked")].isNull() && m_blocked_isValid;

    m_blocked_reason_isValid = ::OpenAPI::fromJsonValue(m_blocked_reason, json[QString("blockedReason")]);
    m_blocked_reason_isSet = !json[QString("blockedReason")].isNull() && m_blocked_reason_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_email_verified_isValid = ::OpenAPI::fromJsonValue(m_email_verified, json[QString("emailVerified")]);
    m_email_verified_isSet = !json[QString("emailVerified")].isNull() && m_email_verified_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_login_date_isValid = ::OpenAPI::fromJsonValue(m_last_login_date, json[QString("lastLoginDate")]);
    m_last_login_date_isSet = !json[QString("lastLoginDate")].isNull() && m_last_login_date_isValid;

    m_no_account_setup_warning_modal_isValid = ::OpenAPI::fromJsonValue(m_no_account_setup_warning_modal, json[QString("noAccountSetupWarningModal")]);
    m_no_account_setup_warning_modal_isSet = !json[QString("noAccountSetupWarningModal")].isNull() && m_no_account_setup_warning_modal_isValid;

    m_no_instance_config_warning_modal_isValid = ::OpenAPI::fromJsonValue(m_no_instance_config_warning_modal, json[QString("noInstanceConfigWarningModal")]);
    m_no_instance_config_warning_modal_isSet = !json[QString("noInstanceConfigWarningModal")].isNull() && m_no_instance_config_warning_modal_isValid;

    m_no_welcome_modal_isValid = ::OpenAPI::fromJsonValue(m_no_welcome_modal, json[QString("noWelcomeModal")]);
    m_no_welcome_modal_isSet = !json[QString("noWelcomeModal")].isNull() && m_no_welcome_modal_isValid;

    m_nsfw_policy_isValid = ::OpenAPI::fromJsonValue(m_nsfw_policy, json[QString("nsfwPolicy")]);
    m_nsfw_policy_isSet = !json[QString("nsfwPolicy")].isNull() && m_nsfw_policy_isValid;

    m_p2p_enabled_isValid = ::OpenAPI::fromJsonValue(m_p2p_enabled, json[QString("p2pEnabled")]);
    m_p2p_enabled_isSet = !json[QString("p2pEnabled")].isNull() && m_p2p_enabled_isValid;

    m_plugin_auth_isValid = ::OpenAPI::fromJsonValue(m_plugin_auth, json[QString("pluginAuth")]);
    m_plugin_auth_isSet = !json[QString("pluginAuth")].isNull() && m_plugin_auth_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_video_channels_isValid = ::OpenAPI::fromJsonValue(m_video_channels, json[QString("videoChannels")]);
    m_video_channels_isSet = !json[QString("videoChannels")].isNull() && m_video_channels_isValid;

    m_video_quota_isValid = ::OpenAPI::fromJsonValue(m_video_quota, json[QString("videoQuota")]);
    m_video_quota_isSet = !json[QString("videoQuota")].isNull() && m_video_quota_isValid;

    m_video_quota_daily_isValid = ::OpenAPI::fromJsonValue(m_video_quota_daily, json[QString("videoQuotaDaily")]);
    m_video_quota_daily_isSet = !json[QString("videoQuotaDaily")].isNull() && m_video_quota_daily_isValid;

    m_abuses_accepted_count_isValid = ::OpenAPI::fromJsonValue(m_abuses_accepted_count, json[QString("abusesAcceptedCount")]);
    m_abuses_accepted_count_isSet = !json[QString("abusesAcceptedCount")].isNull() && m_abuses_accepted_count_isValid;

    m_abuses_count_isValid = ::OpenAPI::fromJsonValue(m_abuses_count, json[QString("abusesCount")]);
    m_abuses_count_isSet = !json[QString("abusesCount")].isNull() && m_abuses_count_isValid;

    m_abuses_created_count_isValid = ::OpenAPI::fromJsonValue(m_abuses_created_count, json[QString("abusesCreatedCount")]);
    m_abuses_created_count_isSet = !json[QString("abusesCreatedCount")].isNull() && m_abuses_created_count_isValid;

    m_video_comments_count_isValid = ::OpenAPI::fromJsonValue(m_video_comments_count, json[QString("videoCommentsCount")]);
    m_video_comments_count_isSet = !json[QString("videoCommentsCount")].isNull() && m_video_comments_count_isValid;

    m_videos_count_isValid = ::OpenAPI::fromJsonValue(m_videos_count, json[QString("videosCount")]);
    m_videos_count_isSet = !json[QString("videosCount")].isNull() && m_videos_count_isValid;
}

QString OAIGetUser_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetUser_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_auto_play_next_video_isSet) {
        obj.insert(QString("autoPlayNextVideo"), ::OpenAPI::toJsonValue(m_auto_play_next_video));
    }
    if (m_auto_play_next_video_playlist_isSet) {
        obj.insert(QString("autoPlayNextVideoPlaylist"), ::OpenAPI::toJsonValue(m_auto_play_next_video_playlist));
    }
    if (m_auto_play_video_isSet) {
        obj.insert(QString("autoPlayVideo"), ::OpenAPI::toJsonValue(m_auto_play_video));
    }
    if (m_blocked_isSet) {
        obj.insert(QString("blocked"), ::OpenAPI::toJsonValue(m_blocked));
    }
    if (m_blocked_reason_isSet) {
        obj.insert(QString("blockedReason"), ::OpenAPI::toJsonValue(m_blocked_reason));
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
    if (m_last_login_date_isSet) {
        obj.insert(QString("lastLoginDate"), ::OpenAPI::toJsonValue(m_last_login_date));
    }
    if (m_no_account_setup_warning_modal_isSet) {
        obj.insert(QString("noAccountSetupWarningModal"), ::OpenAPI::toJsonValue(m_no_account_setup_warning_modal));
    }
    if (m_no_instance_config_warning_modal_isSet) {
        obj.insert(QString("noInstanceConfigWarningModal"), ::OpenAPI::toJsonValue(m_no_instance_config_warning_modal));
    }
    if (m_no_welcome_modal_isSet) {
        obj.insert(QString("noWelcomeModal"), ::OpenAPI::toJsonValue(m_no_welcome_modal));
    }
    if (m_nsfw_policy.isSet()) {
        obj.insert(QString("nsfwPolicy"), ::OpenAPI::toJsonValue(m_nsfw_policy));
    }
    if (m_p2p_enabled_isSet) {
        obj.insert(QString("p2pEnabled"), ::OpenAPI::toJsonValue(m_p2p_enabled));
    }
    if (m_plugin_auth_isSet) {
        obj.insert(QString("pluginAuth"), ::OpenAPI::toJsonValue(m_plugin_auth));
    }
    if (m_role.isSet()) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_theme_isSet) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_video_channels.size() > 0) {
        obj.insert(QString("videoChannels"), ::OpenAPI::toJsonValue(m_video_channels));
    }
    if (m_video_quota_isSet) {
        obj.insert(QString("videoQuota"), ::OpenAPI::toJsonValue(m_video_quota));
    }
    if (m_video_quota_daily_isSet) {
        obj.insert(QString("videoQuotaDaily"), ::OpenAPI::toJsonValue(m_video_quota_daily));
    }
    if (m_abuses_accepted_count_isSet) {
        obj.insert(QString("abusesAcceptedCount"), ::OpenAPI::toJsonValue(m_abuses_accepted_count));
    }
    if (m_abuses_count_isSet) {
        obj.insert(QString("abusesCount"), ::OpenAPI::toJsonValue(m_abuses_count));
    }
    if (m_abuses_created_count_isSet) {
        obj.insert(QString("abusesCreatedCount"), ::OpenAPI::toJsonValue(m_abuses_created_count));
    }
    if (m_video_comments_count_isSet) {
        obj.insert(QString("videoCommentsCount"), ::OpenAPI::toJsonValue(m_video_comments_count));
    }
    if (m_videos_count_isSet) {
        obj.insert(QString("videosCount"), ::OpenAPI::toJsonValue(m_videos_count));
    }
    return obj;
}

OAIAccount OAIGetUser_200_response::getAccount() const {
    return m_account;
}
void OAIGetUser_200_response::setAccount(const OAIAccount &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAIGetUser_200_response::is_account_Set() const{
    return m_account_isSet;
}

bool OAIGetUser_200_response::is_account_Valid() const{
    return m_account_isValid;
}

bool OAIGetUser_200_response::isAutoPlayNextVideo() const {
    return m_auto_play_next_video;
}
void OAIGetUser_200_response::setAutoPlayNextVideo(const bool &auto_play_next_video) {
    m_auto_play_next_video = auto_play_next_video;
    m_auto_play_next_video_isSet = true;
}

bool OAIGetUser_200_response::is_auto_play_next_video_Set() const{
    return m_auto_play_next_video_isSet;
}

bool OAIGetUser_200_response::is_auto_play_next_video_Valid() const{
    return m_auto_play_next_video_isValid;
}

bool OAIGetUser_200_response::isAutoPlayNextVideoPlaylist() const {
    return m_auto_play_next_video_playlist;
}
void OAIGetUser_200_response::setAutoPlayNextVideoPlaylist(const bool &auto_play_next_video_playlist) {
    m_auto_play_next_video_playlist = auto_play_next_video_playlist;
    m_auto_play_next_video_playlist_isSet = true;
}

bool OAIGetUser_200_response::is_auto_play_next_video_playlist_Set() const{
    return m_auto_play_next_video_playlist_isSet;
}

bool OAIGetUser_200_response::is_auto_play_next_video_playlist_Valid() const{
    return m_auto_play_next_video_playlist_isValid;
}

bool OAIGetUser_200_response::isAutoPlayVideo() const {
    return m_auto_play_video;
}
void OAIGetUser_200_response::setAutoPlayVideo(const bool &auto_play_video) {
    m_auto_play_video = auto_play_video;
    m_auto_play_video_isSet = true;
}

bool OAIGetUser_200_response::is_auto_play_video_Set() const{
    return m_auto_play_video_isSet;
}

bool OAIGetUser_200_response::is_auto_play_video_Valid() const{
    return m_auto_play_video_isValid;
}

bool OAIGetUser_200_response::isBlocked() const {
    return m_blocked;
}
void OAIGetUser_200_response::setBlocked(const bool &blocked) {
    m_blocked = blocked;
    m_blocked_isSet = true;
}

bool OAIGetUser_200_response::is_blocked_Set() const{
    return m_blocked_isSet;
}

bool OAIGetUser_200_response::is_blocked_Valid() const{
    return m_blocked_isValid;
}

QString OAIGetUser_200_response::getBlockedReason() const {
    return m_blocked_reason;
}
void OAIGetUser_200_response::setBlockedReason(const QString &blocked_reason) {
    m_blocked_reason = blocked_reason;
    m_blocked_reason_isSet = true;
}

bool OAIGetUser_200_response::is_blocked_reason_Set() const{
    return m_blocked_reason_isSet;
}

bool OAIGetUser_200_response::is_blocked_reason_Valid() const{
    return m_blocked_reason_isValid;
}

QString OAIGetUser_200_response::getCreatedAt() const {
    return m_created_at;
}
void OAIGetUser_200_response::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIGetUser_200_response::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIGetUser_200_response::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIGetUser_200_response::getEmail() const {
    return m_email;
}
void OAIGetUser_200_response::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIGetUser_200_response::is_email_Set() const{
    return m_email_isSet;
}

bool OAIGetUser_200_response::is_email_Valid() const{
    return m_email_isValid;
}

bool OAIGetUser_200_response::isEmailVerified() const {
    return m_email_verified;
}
void OAIGetUser_200_response::setEmailVerified(const bool &email_verified) {
    m_email_verified = email_verified;
    m_email_verified_isSet = true;
}

bool OAIGetUser_200_response::is_email_verified_Set() const{
    return m_email_verified_isSet;
}

bool OAIGetUser_200_response::is_email_verified_Valid() const{
    return m_email_verified_isValid;
}

qint32 OAIGetUser_200_response::getId() const {
    return m_id;
}
void OAIGetUser_200_response::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetUser_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetUser_200_response::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIGetUser_200_response::getLastLoginDate() const {
    return m_last_login_date;
}
void OAIGetUser_200_response::setLastLoginDate(const QDateTime &last_login_date) {
    m_last_login_date = last_login_date;
    m_last_login_date_isSet = true;
}

bool OAIGetUser_200_response::is_last_login_date_Set() const{
    return m_last_login_date_isSet;
}

bool OAIGetUser_200_response::is_last_login_date_Valid() const{
    return m_last_login_date_isValid;
}

bool OAIGetUser_200_response::isNoAccountSetupWarningModal() const {
    return m_no_account_setup_warning_modal;
}
void OAIGetUser_200_response::setNoAccountSetupWarningModal(const bool &no_account_setup_warning_modal) {
    m_no_account_setup_warning_modal = no_account_setup_warning_modal;
    m_no_account_setup_warning_modal_isSet = true;
}

bool OAIGetUser_200_response::is_no_account_setup_warning_modal_Set() const{
    return m_no_account_setup_warning_modal_isSet;
}

bool OAIGetUser_200_response::is_no_account_setup_warning_modal_Valid() const{
    return m_no_account_setup_warning_modal_isValid;
}

bool OAIGetUser_200_response::isNoInstanceConfigWarningModal() const {
    return m_no_instance_config_warning_modal;
}
void OAIGetUser_200_response::setNoInstanceConfigWarningModal(const bool &no_instance_config_warning_modal) {
    m_no_instance_config_warning_modal = no_instance_config_warning_modal;
    m_no_instance_config_warning_modal_isSet = true;
}

bool OAIGetUser_200_response::is_no_instance_config_warning_modal_Set() const{
    return m_no_instance_config_warning_modal_isSet;
}

bool OAIGetUser_200_response::is_no_instance_config_warning_modal_Valid() const{
    return m_no_instance_config_warning_modal_isValid;
}

bool OAIGetUser_200_response::isNoWelcomeModal() const {
    return m_no_welcome_modal;
}
void OAIGetUser_200_response::setNoWelcomeModal(const bool &no_welcome_modal) {
    m_no_welcome_modal = no_welcome_modal;
    m_no_welcome_modal_isSet = true;
}

bool OAIGetUser_200_response::is_no_welcome_modal_Set() const{
    return m_no_welcome_modal_isSet;
}

bool OAIGetUser_200_response::is_no_welcome_modal_Valid() const{
    return m_no_welcome_modal_isValid;
}

OAINSFWPolicy OAIGetUser_200_response::getNsfwPolicy() const {
    return m_nsfw_policy;
}
void OAIGetUser_200_response::setNsfwPolicy(const OAINSFWPolicy &nsfw_policy) {
    m_nsfw_policy = nsfw_policy;
    m_nsfw_policy_isSet = true;
}

bool OAIGetUser_200_response::is_nsfw_policy_Set() const{
    return m_nsfw_policy_isSet;
}

bool OAIGetUser_200_response::is_nsfw_policy_Valid() const{
    return m_nsfw_policy_isValid;
}

bool OAIGetUser_200_response::isP2pEnabled() const {
    return m_p2p_enabled;
}
void OAIGetUser_200_response::setP2pEnabled(const bool &p2p_enabled) {
    m_p2p_enabled = p2p_enabled;
    m_p2p_enabled_isSet = true;
}

bool OAIGetUser_200_response::is_p2p_enabled_Set() const{
    return m_p2p_enabled_isSet;
}

bool OAIGetUser_200_response::is_p2p_enabled_Valid() const{
    return m_p2p_enabled_isValid;
}

QString OAIGetUser_200_response::getPluginAuth() const {
    return m_plugin_auth;
}
void OAIGetUser_200_response::setPluginAuth(const QString &plugin_auth) {
    m_plugin_auth = plugin_auth;
    m_plugin_auth_isSet = true;
}

bool OAIGetUser_200_response::is_plugin_auth_Set() const{
    return m_plugin_auth_isSet;
}

bool OAIGetUser_200_response::is_plugin_auth_Valid() const{
    return m_plugin_auth_isValid;
}

OAIUser_role OAIGetUser_200_response::getRole() const {
    return m_role;
}
void OAIGetUser_200_response::setRole(const OAIUser_role &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIGetUser_200_response::is_role_Set() const{
    return m_role_isSet;
}

bool OAIGetUser_200_response::is_role_Valid() const{
    return m_role_isValid;
}

QString OAIGetUser_200_response::getTheme() const {
    return m_theme;
}
void OAIGetUser_200_response::setTheme(const QString &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAIGetUser_200_response::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAIGetUser_200_response::is_theme_Valid() const{
    return m_theme_isValid;
}

QString OAIGetUser_200_response::getUsername() const {
    return m_username;
}
void OAIGetUser_200_response::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIGetUser_200_response::is_username_Set() const{
    return m_username_isSet;
}

bool OAIGetUser_200_response::is_username_Valid() const{
    return m_username_isValid;
}

QList<OAIVideoChannel> OAIGetUser_200_response::getVideoChannels() const {
    return m_video_channels;
}
void OAIGetUser_200_response::setVideoChannels(const QList<OAIVideoChannel> &video_channels) {
    m_video_channels = video_channels;
    m_video_channels_isSet = true;
}

bool OAIGetUser_200_response::is_video_channels_Set() const{
    return m_video_channels_isSet;
}

bool OAIGetUser_200_response::is_video_channels_Valid() const{
    return m_video_channels_isValid;
}

qint32 OAIGetUser_200_response::getVideoQuota() const {
    return m_video_quota;
}
void OAIGetUser_200_response::setVideoQuota(const qint32 &video_quota) {
    m_video_quota = video_quota;
    m_video_quota_isSet = true;
}

bool OAIGetUser_200_response::is_video_quota_Set() const{
    return m_video_quota_isSet;
}

bool OAIGetUser_200_response::is_video_quota_Valid() const{
    return m_video_quota_isValid;
}

qint32 OAIGetUser_200_response::getVideoQuotaDaily() const {
    return m_video_quota_daily;
}
void OAIGetUser_200_response::setVideoQuotaDaily(const qint32 &video_quota_daily) {
    m_video_quota_daily = video_quota_daily;
    m_video_quota_daily_isSet = true;
}

bool OAIGetUser_200_response::is_video_quota_daily_Set() const{
    return m_video_quota_daily_isSet;
}

bool OAIGetUser_200_response::is_video_quota_daily_Valid() const{
    return m_video_quota_daily_isValid;
}

qint32 OAIGetUser_200_response::getAbusesAcceptedCount() const {
    return m_abuses_accepted_count;
}
void OAIGetUser_200_response::setAbusesAcceptedCount(const qint32 &abuses_accepted_count) {
    m_abuses_accepted_count = abuses_accepted_count;
    m_abuses_accepted_count_isSet = true;
}

bool OAIGetUser_200_response::is_abuses_accepted_count_Set() const{
    return m_abuses_accepted_count_isSet;
}

bool OAIGetUser_200_response::is_abuses_accepted_count_Valid() const{
    return m_abuses_accepted_count_isValid;
}

qint32 OAIGetUser_200_response::getAbusesCount() const {
    return m_abuses_count;
}
void OAIGetUser_200_response::setAbusesCount(const qint32 &abuses_count) {
    m_abuses_count = abuses_count;
    m_abuses_count_isSet = true;
}

bool OAIGetUser_200_response::is_abuses_count_Set() const{
    return m_abuses_count_isSet;
}

bool OAIGetUser_200_response::is_abuses_count_Valid() const{
    return m_abuses_count_isValid;
}

qint32 OAIGetUser_200_response::getAbusesCreatedCount() const {
    return m_abuses_created_count;
}
void OAIGetUser_200_response::setAbusesCreatedCount(const qint32 &abuses_created_count) {
    m_abuses_created_count = abuses_created_count;
    m_abuses_created_count_isSet = true;
}

bool OAIGetUser_200_response::is_abuses_created_count_Set() const{
    return m_abuses_created_count_isSet;
}

bool OAIGetUser_200_response::is_abuses_created_count_Valid() const{
    return m_abuses_created_count_isValid;
}

qint32 OAIGetUser_200_response::getVideoCommentsCount() const {
    return m_video_comments_count;
}
void OAIGetUser_200_response::setVideoCommentsCount(const qint32 &video_comments_count) {
    m_video_comments_count = video_comments_count;
    m_video_comments_count_isSet = true;
}

bool OAIGetUser_200_response::is_video_comments_count_Set() const{
    return m_video_comments_count_isSet;
}

bool OAIGetUser_200_response::is_video_comments_count_Valid() const{
    return m_video_comments_count_isValid;
}

qint32 OAIGetUser_200_response::getVideosCount() const {
    return m_videos_count;
}
void OAIGetUser_200_response::setVideosCount(const qint32 &videos_count) {
    m_videos_count = videos_count;
    m_videos_count_isSet = true;
}

bool OAIGetUser_200_response::is_videos_count_Set() const{
    return m_videos_count_isSet;
}

bool OAIGetUser_200_response::is_videos_count_Valid() const{
    return m_videos_count_isValid;
}

bool OAIGetUser_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_play_next_video_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_play_next_video_playlist_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_play_video_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blocked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blocked_reason_isSet) {
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

        if (m_last_login_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_account_setup_warning_modal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_instance_config_warning_modal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_welcome_modal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nsfw_policy.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_p2p_enabled_isSet) {
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

        if (m_theme_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_channels.size() > 0) {
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

        if (m_abuses_accepted_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_abuses_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_abuses_created_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_comments_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_videos_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetUser_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
