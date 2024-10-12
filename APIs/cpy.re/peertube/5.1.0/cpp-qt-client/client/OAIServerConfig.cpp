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

#include "OAIServerConfig.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfig::OAIServerConfig(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfig::OAIServerConfig() {
    this->initializeModel();
}

OAIServerConfig::~OAIServerConfig() {}

void OAIServerConfig::initializeModel() {

    m_auto_blacklist_isSet = false;
    m_auto_blacklist_isValid = false;

    m_avatar_isSet = false;
    m_avatar_isValid = false;

    m_contact_form_isSet = false;
    m_contact_form_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_followings_isSet = false;
    m_followings_isValid = false;

    m_homepage_isSet = false;
    m_homepage_isValid = false;

    m_import_isSet = false;
    m_import_isValid = false;

    m_instance_isSet = false;
    m_instance_isValid = false;

    m_plugin_isSet = false;
    m_plugin_isValid = false;

    m_search_isSet = false;
    m_search_isValid = false;

    m_server_commit_isSet = false;
    m_server_commit_isValid = false;

    m_server_version_isSet = false;
    m_server_version_isValid = false;

    m_signup_isSet = false;
    m_signup_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_tracker_isSet = false;
    m_tracker_isValid = false;

    m_transcoding_isSet = false;
    m_transcoding_isValid = false;

    m_trending_isSet = false;
    m_trending_isValid = false;

    m_user_isSet = false;
    m_user_isValid = false;

    m_video_isSet = false;
    m_video_isValid = false;

    m_video_caption_isSet = false;
    m_video_caption_isValid = false;
}

void OAIServerConfig::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfig::fromJsonObject(QJsonObject json) {

    m_auto_blacklist_isValid = ::OpenAPI::fromJsonValue(m_auto_blacklist, json[QString("autoBlacklist")]);
    m_auto_blacklist_isSet = !json[QString("autoBlacklist")].isNull() && m_auto_blacklist_isValid;

    m_avatar_isValid = ::OpenAPI::fromJsonValue(m_avatar, json[QString("avatar")]);
    m_avatar_isSet = !json[QString("avatar")].isNull() && m_avatar_isValid;

    m_contact_form_isValid = ::OpenAPI::fromJsonValue(m_contact_form, json[QString("contactForm")]);
    m_contact_form_isSet = !json[QString("contactForm")].isNull() && m_contact_form_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_followings_isValid = ::OpenAPI::fromJsonValue(m_followings, json[QString("followings")]);
    m_followings_isSet = !json[QString("followings")].isNull() && m_followings_isValid;

    m_homepage_isValid = ::OpenAPI::fromJsonValue(m_homepage, json[QString("homepage")]);
    m_homepage_isSet = !json[QString("homepage")].isNull() && m_homepage_isValid;

    m_import_isValid = ::OpenAPI::fromJsonValue(m_import, json[QString("import")]);
    m_import_isSet = !json[QString("import")].isNull() && m_import_isValid;

    m_instance_isValid = ::OpenAPI::fromJsonValue(m_instance, json[QString("instance")]);
    m_instance_isSet = !json[QString("instance")].isNull() && m_instance_isValid;

    m_plugin_isValid = ::OpenAPI::fromJsonValue(m_plugin, json[QString("plugin")]);
    m_plugin_isSet = !json[QString("plugin")].isNull() && m_plugin_isValid;

    m_search_isValid = ::OpenAPI::fromJsonValue(m_search, json[QString("search")]);
    m_search_isSet = !json[QString("search")].isNull() && m_search_isValid;

    m_server_commit_isValid = ::OpenAPI::fromJsonValue(m_server_commit, json[QString("serverCommit")]);
    m_server_commit_isSet = !json[QString("serverCommit")].isNull() && m_server_commit_isValid;

    m_server_version_isValid = ::OpenAPI::fromJsonValue(m_server_version, json[QString("serverVersion")]);
    m_server_version_isSet = !json[QString("serverVersion")].isNull() && m_server_version_isValid;

    m_signup_isValid = ::OpenAPI::fromJsonValue(m_signup, json[QString("signup")]);
    m_signup_isSet = !json[QString("signup")].isNull() && m_signup_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_tracker_isValid = ::OpenAPI::fromJsonValue(m_tracker, json[QString("tracker")]);
    m_tracker_isSet = !json[QString("tracker")].isNull() && m_tracker_isValid;

    m_transcoding_isValid = ::OpenAPI::fromJsonValue(m_transcoding, json[QString("transcoding")]);
    m_transcoding_isSet = !json[QString("transcoding")].isNull() && m_transcoding_isValid;

    m_trending_isValid = ::OpenAPI::fromJsonValue(m_trending, json[QString("trending")]);
    m_trending_isSet = !json[QString("trending")].isNull() && m_trending_isValid;

    m_user_isValid = ::OpenAPI::fromJsonValue(m_user, json[QString("user")]);
    m_user_isSet = !json[QString("user")].isNull() && m_user_isValid;

    m_video_isValid = ::OpenAPI::fromJsonValue(m_video, json[QString("video")]);
    m_video_isSet = !json[QString("video")].isNull() && m_video_isValid;

    m_video_caption_isValid = ::OpenAPI::fromJsonValue(m_video_caption, json[QString("videoCaption")]);
    m_video_caption_isSet = !json[QString("videoCaption")].isNull() && m_video_caption_isValid;
}

QString OAIServerConfig::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfig::asJsonObject() const {
    QJsonObject obj;
    if (m_auto_blacklist.isSet()) {
        obj.insert(QString("autoBlacklist"), ::OpenAPI::toJsonValue(m_auto_blacklist));
    }
    if (m_avatar.isSet()) {
        obj.insert(QString("avatar"), ::OpenAPI::toJsonValue(m_avatar));
    }
    if (m_contact_form.isSet()) {
        obj.insert(QString("contactForm"), ::OpenAPI::toJsonValue(m_contact_form));
    }
    if (m_email.isSet()) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_followings.isSet()) {
        obj.insert(QString("followings"), ::OpenAPI::toJsonValue(m_followings));
    }
    if (m_homepage.isSet()) {
        obj.insert(QString("homepage"), ::OpenAPI::toJsonValue(m_homepage));
    }
    if (m_import.isSet()) {
        obj.insert(QString("import"), ::OpenAPI::toJsonValue(m_import));
    }
    if (m_instance.isSet()) {
        obj.insert(QString("instance"), ::OpenAPI::toJsonValue(m_instance));
    }
    if (m_plugin.isSet()) {
        obj.insert(QString("plugin"), ::OpenAPI::toJsonValue(m_plugin));
    }
    if (m_search.isSet()) {
        obj.insert(QString("search"), ::OpenAPI::toJsonValue(m_search));
    }
    if (m_server_commit_isSet) {
        obj.insert(QString("serverCommit"), ::OpenAPI::toJsonValue(m_server_commit));
    }
    if (m_server_version_isSet) {
        obj.insert(QString("serverVersion"), ::OpenAPI::toJsonValue(m_server_version));
    }
    if (m_signup.isSet()) {
        obj.insert(QString("signup"), ::OpenAPI::toJsonValue(m_signup));
    }
    if (m_theme.isSet()) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_tracker.isSet()) {
        obj.insert(QString("tracker"), ::OpenAPI::toJsonValue(m_tracker));
    }
    if (m_transcoding.isSet()) {
        obj.insert(QString("transcoding"), ::OpenAPI::toJsonValue(m_transcoding));
    }
    if (m_trending.isSet()) {
        obj.insert(QString("trending"), ::OpenAPI::toJsonValue(m_trending));
    }
    if (m_user.isSet()) {
        obj.insert(QString("user"), ::OpenAPI::toJsonValue(m_user));
    }
    if (m_video.isSet()) {
        obj.insert(QString("video"), ::OpenAPI::toJsonValue(m_video));
    }
    if (m_video_caption.isSet()) {
        obj.insert(QString("videoCaption"), ::OpenAPI::toJsonValue(m_video_caption));
    }
    return obj;
}

OAIServerConfig_autoBlacklist OAIServerConfig::getAutoBlacklist() const {
    return m_auto_blacklist;
}
void OAIServerConfig::setAutoBlacklist(const OAIServerConfig_autoBlacklist &auto_blacklist) {
    m_auto_blacklist = auto_blacklist;
    m_auto_blacklist_isSet = true;
}

bool OAIServerConfig::is_auto_blacklist_Set() const{
    return m_auto_blacklist_isSet;
}

bool OAIServerConfig::is_auto_blacklist_Valid() const{
    return m_auto_blacklist_isValid;
}

OAIServerConfig_avatar OAIServerConfig::getAvatar() const {
    return m_avatar;
}
void OAIServerConfig::setAvatar(const OAIServerConfig_avatar &avatar) {
    m_avatar = avatar;
    m_avatar_isSet = true;
}

bool OAIServerConfig::is_avatar_Set() const{
    return m_avatar_isSet;
}

bool OAIServerConfig::is_avatar_Valid() const{
    return m_avatar_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfig::getContactForm() const {
    return m_contact_form;
}
void OAIServerConfig::setContactForm(const OAIServerConfig_autoBlacklist_videos_ofUsers &contact_form) {
    m_contact_form = contact_form;
    m_contact_form_isSet = true;
}

bool OAIServerConfig::is_contact_form_Set() const{
    return m_contact_form_isSet;
}

bool OAIServerConfig::is_contact_form_Valid() const{
    return m_contact_form_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfig::getEmail() const {
    return m_email;
}
void OAIServerConfig::setEmail(const OAIServerConfig_autoBlacklist_videos_ofUsers &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIServerConfig::is_email_Set() const{
    return m_email_isSet;
}

bool OAIServerConfig::is_email_Valid() const{
    return m_email_isValid;
}

OAIServerConfig_followings OAIServerConfig::getFollowings() const {
    return m_followings;
}
void OAIServerConfig::setFollowings(const OAIServerConfig_followings &followings) {
    m_followings = followings;
    m_followings_isSet = true;
}

bool OAIServerConfig::is_followings_Set() const{
    return m_followings_isSet;
}

bool OAIServerConfig::is_followings_Valid() const{
    return m_followings_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfig::getHomepage() const {
    return m_homepage;
}
void OAIServerConfig::setHomepage(const OAIServerConfig_autoBlacklist_videos_ofUsers &homepage) {
    m_homepage = homepage;
    m_homepage_isSet = true;
}

bool OAIServerConfig::is_homepage_Set() const{
    return m_homepage_isSet;
}

bool OAIServerConfig::is_homepage_Valid() const{
    return m_homepage_isValid;
}

OAIServerConfig_import OAIServerConfig::getImport() const {
    return m_import;
}
void OAIServerConfig::setImport(const OAIServerConfig_import &import) {
    m_import = import;
    m_import_isSet = true;
}

bool OAIServerConfig::is_import_Set() const{
    return m_import_isSet;
}

bool OAIServerConfig::is_import_Valid() const{
    return m_import_isValid;
}

OAIServerConfig_instance OAIServerConfig::getInstance() const {
    return m_instance;
}
void OAIServerConfig::setInstance(const OAIServerConfig_instance &instance) {
    m_instance = instance;
    m_instance_isSet = true;
}

bool OAIServerConfig::is_instance_Set() const{
    return m_instance_isSet;
}

bool OAIServerConfig::is_instance_Valid() const{
    return m_instance_isValid;
}

OAIServerConfig_plugin OAIServerConfig::getPlugin() const {
    return m_plugin;
}
void OAIServerConfig::setPlugin(const OAIServerConfig_plugin &plugin) {
    m_plugin = plugin;
    m_plugin_isSet = true;
}

bool OAIServerConfig::is_plugin_Set() const{
    return m_plugin_isSet;
}

bool OAIServerConfig::is_plugin_Valid() const{
    return m_plugin_isValid;
}

OAIServerConfig_search OAIServerConfig::getSearch() const {
    return m_search;
}
void OAIServerConfig::setSearch(const OAIServerConfig_search &search) {
    m_search = search;
    m_search_isSet = true;
}

bool OAIServerConfig::is_search_Set() const{
    return m_search_isSet;
}

bool OAIServerConfig::is_search_Valid() const{
    return m_search_isValid;
}

QString OAIServerConfig::getServerCommit() const {
    return m_server_commit;
}
void OAIServerConfig::setServerCommit(const QString &server_commit) {
    m_server_commit = server_commit;
    m_server_commit_isSet = true;
}

bool OAIServerConfig::is_server_commit_Set() const{
    return m_server_commit_isSet;
}

bool OAIServerConfig::is_server_commit_Valid() const{
    return m_server_commit_isValid;
}

QString OAIServerConfig::getServerVersion() const {
    return m_server_version;
}
void OAIServerConfig::setServerVersion(const QString &server_version) {
    m_server_version = server_version;
    m_server_version_isSet = true;
}

bool OAIServerConfig::is_server_version_Set() const{
    return m_server_version_isSet;
}

bool OAIServerConfig::is_server_version_Valid() const{
    return m_server_version_isValid;
}

OAIServerConfig_signup OAIServerConfig::getSignup() const {
    return m_signup;
}
void OAIServerConfig::setSignup(const OAIServerConfig_signup &signup) {
    m_signup = signup;
    m_signup_isSet = true;
}

bool OAIServerConfig::is_signup_Set() const{
    return m_signup_isSet;
}

bool OAIServerConfig::is_signup_Valid() const{
    return m_signup_isValid;
}

OAIServerConfig_plugin OAIServerConfig::getTheme() const {
    return m_theme;
}
void OAIServerConfig::setTheme(const OAIServerConfig_plugin &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAIServerConfig::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAIServerConfig::is_theme_Valid() const{
    return m_theme_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfig::getTracker() const {
    return m_tracker;
}
void OAIServerConfig::setTracker(const OAIServerConfig_autoBlacklist_videos_ofUsers &tracker) {
    m_tracker = tracker;
    m_tracker_isSet = true;
}

bool OAIServerConfig::is_tracker_Set() const{
    return m_tracker_isSet;
}

bool OAIServerConfig::is_tracker_Valid() const{
    return m_tracker_isValid;
}

OAIServerConfig_transcoding OAIServerConfig::getTranscoding() const {
    return m_transcoding;
}
void OAIServerConfig::setTranscoding(const OAIServerConfig_transcoding &transcoding) {
    m_transcoding = transcoding;
    m_transcoding_isSet = true;
}

bool OAIServerConfig::is_transcoding_Set() const{
    return m_transcoding_isSet;
}

bool OAIServerConfig::is_transcoding_Valid() const{
    return m_transcoding_isValid;
}

OAIServerConfig_trending OAIServerConfig::getTrending() const {
    return m_trending;
}
void OAIServerConfig::setTrending(const OAIServerConfig_trending &trending) {
    m_trending = trending;
    m_trending_isSet = true;
}

bool OAIServerConfig::is_trending_Set() const{
    return m_trending_isSet;
}

bool OAIServerConfig::is_trending_Valid() const{
    return m_trending_isValid;
}

OAIServerConfig_user OAIServerConfig::getUser() const {
    return m_user;
}
void OAIServerConfig::setUser(const OAIServerConfig_user &user) {
    m_user = user;
    m_user_isSet = true;
}

bool OAIServerConfig::is_user_Set() const{
    return m_user_isSet;
}

bool OAIServerConfig::is_user_Valid() const{
    return m_user_isValid;
}

OAIServerConfig_video OAIServerConfig::getVideo() const {
    return m_video;
}
void OAIServerConfig::setVideo(const OAIServerConfig_video &video) {
    m_video = video;
    m_video_isSet = true;
}

bool OAIServerConfig::is_video_Set() const{
    return m_video_isSet;
}

bool OAIServerConfig::is_video_Valid() const{
    return m_video_isValid;
}

OAIServerConfig_videoCaption OAIServerConfig::getVideoCaption() const {
    return m_video_caption;
}
void OAIServerConfig::setVideoCaption(const OAIServerConfig_videoCaption &video_caption) {
    m_video_caption = video_caption;
    m_video_caption_isSet = true;
}

bool OAIServerConfig::is_video_caption_Set() const{
    return m_video_caption_isSet;
}

bool OAIServerConfig::is_video_caption_Valid() const{
    return m_video_caption_isValid;
}

bool OAIServerConfig::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auto_blacklist.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_avatar.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_form.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_email.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_followings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_homepage.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_import.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_instance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_plugin.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_search.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_commit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_signup.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracker.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_transcoding.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_trending.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_caption.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerConfig::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
