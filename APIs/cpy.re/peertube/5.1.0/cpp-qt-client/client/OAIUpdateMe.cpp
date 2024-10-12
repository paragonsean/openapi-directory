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

#include "OAIUpdateMe.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateMe::OAIUpdateMe(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateMe::OAIUpdateMe() {
    this->initializeModel();
}

OAIUpdateMe::~OAIUpdateMe() {}

void OAIUpdateMe::initializeModel() {

    m_auto_play_next_video_isSet = false;
    m_auto_play_next_video_isValid = false;

    m_auto_play_next_video_playlist_isSet = false;
    m_auto_play_next_video_playlist_isValid = false;

    m_auto_play_video_isSet = false;
    m_auto_play_video_isValid = false;

    m_current_password_isSet = false;
    m_current_password_isValid = false;

    m_display_nsfw_isSet = false;
    m_display_nsfw_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_no_account_setup_warning_modal_isSet = false;
    m_no_account_setup_warning_modal_isValid = false;

    m_no_instance_config_warning_modal_isSet = false;
    m_no_instance_config_warning_modal_isValid = false;

    m_no_welcome_modal_isSet = false;
    m_no_welcome_modal_isValid = false;

    m_p2p_enabled_isSet = false;
    m_p2p_enabled_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_video_languages_isSet = false;
    m_video_languages_isValid = false;

    m_videos_history_enabled_isSet = false;
    m_videos_history_enabled_isValid = false;
}

void OAIUpdateMe::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateMe::fromJsonObject(QJsonObject json) {

    m_auto_play_next_video_isValid = ::OpenAPI::fromJsonValue(m_auto_play_next_video, json[QString("autoPlayNextVideo")]);
    m_auto_play_next_video_isSet = !json[QString("autoPlayNextVideo")].isNull() && m_auto_play_next_video_isValid;

    m_auto_play_next_video_playlist_isValid = ::OpenAPI::fromJsonValue(m_auto_play_next_video_playlist, json[QString("autoPlayNextVideoPlaylist")]);
    m_auto_play_next_video_playlist_isSet = !json[QString("autoPlayNextVideoPlaylist")].isNull() && m_auto_play_next_video_playlist_isValid;

    m_auto_play_video_isValid = ::OpenAPI::fromJsonValue(m_auto_play_video, json[QString("autoPlayVideo")]);
    m_auto_play_video_isSet = !json[QString("autoPlayVideo")].isNull() && m_auto_play_video_isValid;

    m_current_password_isValid = ::OpenAPI::fromJsonValue(m_current_password, json[QString("currentPassword")]);
    m_current_password_isSet = !json[QString("currentPassword")].isNull() && m_current_password_isValid;

    m_display_nsfw_isValid = ::OpenAPI::fromJsonValue(m_display_nsfw, json[QString("displayNSFW")]);
    m_display_nsfw_isSet = !json[QString("displayNSFW")].isNull() && m_display_nsfw_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_no_account_setup_warning_modal_isValid = ::OpenAPI::fromJsonValue(m_no_account_setup_warning_modal, json[QString("noAccountSetupWarningModal")]);
    m_no_account_setup_warning_modal_isSet = !json[QString("noAccountSetupWarningModal")].isNull() && m_no_account_setup_warning_modal_isValid;

    m_no_instance_config_warning_modal_isValid = ::OpenAPI::fromJsonValue(m_no_instance_config_warning_modal, json[QString("noInstanceConfigWarningModal")]);
    m_no_instance_config_warning_modal_isSet = !json[QString("noInstanceConfigWarningModal")].isNull() && m_no_instance_config_warning_modal_isValid;

    m_no_welcome_modal_isValid = ::OpenAPI::fromJsonValue(m_no_welcome_modal, json[QString("noWelcomeModal")]);
    m_no_welcome_modal_isSet = !json[QString("noWelcomeModal")].isNull() && m_no_welcome_modal_isValid;

    m_p2p_enabled_isValid = ::OpenAPI::fromJsonValue(m_p2p_enabled, json[QString("p2pEnabled")]);
    m_p2p_enabled_isSet = !json[QString("p2pEnabled")].isNull() && m_p2p_enabled_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_video_languages_isValid = ::OpenAPI::fromJsonValue(m_video_languages, json[QString("videoLanguages")]);
    m_video_languages_isSet = !json[QString("videoLanguages")].isNull() && m_video_languages_isValid;

    m_videos_history_enabled_isValid = ::OpenAPI::fromJsonValue(m_videos_history_enabled, json[QString("videosHistoryEnabled")]);
    m_videos_history_enabled_isSet = !json[QString("videosHistoryEnabled")].isNull() && m_videos_history_enabled_isValid;
}

QString OAIUpdateMe::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateMe::asJsonObject() const {
    QJsonObject obj;
    if (m_auto_play_next_video_isSet) {
        obj.insert(QString("autoPlayNextVideo"), ::OpenAPI::toJsonValue(m_auto_play_next_video));
    }
    if (m_auto_play_next_video_playlist_isSet) {
        obj.insert(QString("autoPlayNextVideoPlaylist"), ::OpenAPI::toJsonValue(m_auto_play_next_video_playlist));
    }
    if (m_auto_play_video_isSet) {
        obj.insert(QString("autoPlayVideo"), ::OpenAPI::toJsonValue(m_auto_play_video));
    }
    if (m_current_password_isSet) {
        obj.insert(QString("currentPassword"), ::OpenAPI::toJsonValue(m_current_password));
    }
    if (m_display_nsfw_isSet) {
        obj.insert(QString("displayNSFW"), ::OpenAPI::toJsonValue(m_display_nsfw));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
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
    if (m_p2p_enabled_isSet) {
        obj.insert(QString("p2pEnabled"), ::OpenAPI::toJsonValue(m_p2p_enabled));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_theme_isSet) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_video_languages.size() > 0) {
        obj.insert(QString("videoLanguages"), ::OpenAPI::toJsonValue(m_video_languages));
    }
    if (m_videos_history_enabled_isSet) {
        obj.insert(QString("videosHistoryEnabled"), ::OpenAPI::toJsonValue(m_videos_history_enabled));
    }
    return obj;
}

bool OAIUpdateMe::isAutoPlayNextVideo() const {
    return m_auto_play_next_video;
}
void OAIUpdateMe::setAutoPlayNextVideo(const bool &auto_play_next_video) {
    m_auto_play_next_video = auto_play_next_video;
    m_auto_play_next_video_isSet = true;
}

bool OAIUpdateMe::is_auto_play_next_video_Set() const{
    return m_auto_play_next_video_isSet;
}

bool OAIUpdateMe::is_auto_play_next_video_Valid() const{
    return m_auto_play_next_video_isValid;
}

bool OAIUpdateMe::isAutoPlayNextVideoPlaylist() const {
    return m_auto_play_next_video_playlist;
}
void OAIUpdateMe::setAutoPlayNextVideoPlaylist(const bool &auto_play_next_video_playlist) {
    m_auto_play_next_video_playlist = auto_play_next_video_playlist;
    m_auto_play_next_video_playlist_isSet = true;
}

bool OAIUpdateMe::is_auto_play_next_video_playlist_Set() const{
    return m_auto_play_next_video_playlist_isSet;
}

bool OAIUpdateMe::is_auto_play_next_video_playlist_Valid() const{
    return m_auto_play_next_video_playlist_isValid;
}

bool OAIUpdateMe::isAutoPlayVideo() const {
    return m_auto_play_video;
}
void OAIUpdateMe::setAutoPlayVideo(const bool &auto_play_video) {
    m_auto_play_video = auto_play_video;
    m_auto_play_video_isSet = true;
}

bool OAIUpdateMe::is_auto_play_video_Set() const{
    return m_auto_play_video_isSet;
}

bool OAIUpdateMe::is_auto_play_video_Valid() const{
    return m_auto_play_video_isValid;
}

QString OAIUpdateMe::getCurrentPassword() const {
    return m_current_password;
}
void OAIUpdateMe::setCurrentPassword(const QString &current_password) {
    m_current_password = current_password;
    m_current_password_isSet = true;
}

bool OAIUpdateMe::is_current_password_Set() const{
    return m_current_password_isSet;
}

bool OAIUpdateMe::is_current_password_Valid() const{
    return m_current_password_isValid;
}

QString OAIUpdateMe::getDisplayNsfw() const {
    return m_display_nsfw;
}
void OAIUpdateMe::setDisplayNsfw(const QString &display_nsfw) {
    m_display_nsfw = display_nsfw;
    m_display_nsfw_isSet = true;
}

bool OAIUpdateMe::is_display_nsfw_Set() const{
    return m_display_nsfw_isSet;
}

bool OAIUpdateMe::is_display_nsfw_Valid() const{
    return m_display_nsfw_isValid;
}

QString OAIUpdateMe::getDisplayName() const {
    return m_display_name;
}
void OAIUpdateMe::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIUpdateMe::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIUpdateMe::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIUpdateMe::getEmail() const {
    return m_email;
}
void OAIUpdateMe::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUpdateMe::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUpdateMe::is_email_Valid() const{
    return m_email_isValid;
}

bool OAIUpdateMe::isNoAccountSetupWarningModal() const {
    return m_no_account_setup_warning_modal;
}
void OAIUpdateMe::setNoAccountSetupWarningModal(const bool &no_account_setup_warning_modal) {
    m_no_account_setup_warning_modal = no_account_setup_warning_modal;
    m_no_account_setup_warning_modal_isSet = true;
}

bool OAIUpdateMe::is_no_account_setup_warning_modal_Set() const{
    return m_no_account_setup_warning_modal_isSet;
}

bool OAIUpdateMe::is_no_account_setup_warning_modal_Valid() const{
    return m_no_account_setup_warning_modal_isValid;
}

bool OAIUpdateMe::isNoInstanceConfigWarningModal() const {
    return m_no_instance_config_warning_modal;
}
void OAIUpdateMe::setNoInstanceConfigWarningModal(const bool &no_instance_config_warning_modal) {
    m_no_instance_config_warning_modal = no_instance_config_warning_modal;
    m_no_instance_config_warning_modal_isSet = true;
}

bool OAIUpdateMe::is_no_instance_config_warning_modal_Set() const{
    return m_no_instance_config_warning_modal_isSet;
}

bool OAIUpdateMe::is_no_instance_config_warning_modal_Valid() const{
    return m_no_instance_config_warning_modal_isValid;
}

bool OAIUpdateMe::isNoWelcomeModal() const {
    return m_no_welcome_modal;
}
void OAIUpdateMe::setNoWelcomeModal(const bool &no_welcome_modal) {
    m_no_welcome_modal = no_welcome_modal;
    m_no_welcome_modal_isSet = true;
}

bool OAIUpdateMe::is_no_welcome_modal_Set() const{
    return m_no_welcome_modal_isSet;
}

bool OAIUpdateMe::is_no_welcome_modal_Valid() const{
    return m_no_welcome_modal_isValid;
}

bool OAIUpdateMe::isP2pEnabled() const {
    return m_p2p_enabled;
}
void OAIUpdateMe::setP2pEnabled(const bool &p2p_enabled) {
    m_p2p_enabled = p2p_enabled;
    m_p2p_enabled_isSet = true;
}

bool OAIUpdateMe::is_p2p_enabled_Set() const{
    return m_p2p_enabled_isSet;
}

bool OAIUpdateMe::is_p2p_enabled_Valid() const{
    return m_p2p_enabled_isValid;
}

QString OAIUpdateMe::getPassword() const {
    return m_password;
}
void OAIUpdateMe::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIUpdateMe::is_password_Set() const{
    return m_password_isSet;
}

bool OAIUpdateMe::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIUpdateMe::getTheme() const {
    return m_theme;
}
void OAIUpdateMe::setTheme(const QString &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAIUpdateMe::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAIUpdateMe::is_theme_Valid() const{
    return m_theme_isValid;
}

QList<QString> OAIUpdateMe::getVideoLanguages() const {
    return m_video_languages;
}
void OAIUpdateMe::setVideoLanguages(const QList<QString> &video_languages) {
    m_video_languages = video_languages;
    m_video_languages_isSet = true;
}

bool OAIUpdateMe::is_video_languages_Set() const{
    return m_video_languages_isSet;
}

bool OAIUpdateMe::is_video_languages_Valid() const{
    return m_video_languages_isValid;
}

bool OAIUpdateMe::isVideosHistoryEnabled() const {
    return m_videos_history_enabled;
}
void OAIUpdateMe::setVideosHistoryEnabled(const bool &videos_history_enabled) {
    m_videos_history_enabled = videos_history_enabled;
    m_videos_history_enabled_isSet = true;
}

bool OAIUpdateMe::is_videos_history_enabled_Set() const{
    return m_videos_history_enabled_isSet;
}

bool OAIUpdateMe::is_videos_history_enabled_Valid() const{
    return m_videos_history_enabled_isValid;
}

bool OAIUpdateMe::isSet() const {
    bool isObjectUpdated = false;
    do {
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

        if (m_current_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_nsfw_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
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

        if (m_p2p_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_videos_history_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateMe::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
