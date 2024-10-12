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

#include "OAIVideoDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoDetails::OAIVideoDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoDetails::OAIVideoDetails() {
    this->initializeModel();
}

OAIVideoDetails::~OAIVideoDetails() {}

void OAIVideoDetails::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_blacklisted_isSet = false;
    m_blacklisted_isValid = false;

    m_blacklisted_reason_isSet = false;
    m_blacklisted_reason_isValid = false;

    m_category_isSet = false;
    m_category_isValid = false;

    m_channel_isSet = false;
    m_channel_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_dislikes_isSet = false;
    m_dislikes_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_embed_path_isSet = false;
    m_embed_path_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_live_isSet = false;
    m_is_live_isValid = false;

    m_is_local_isSet = false;
    m_is_local_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_licence_isSet = false;
    m_licence_isValid = false;

    m_likes_isSet = false;
    m_likes_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_nsfw_isSet = false;
    m_nsfw_isValid = false;

    m_originally_published_at_isSet = false;
    m_originally_published_at_isValid = false;

    m_preview_path_isSet = false;
    m_preview_path_isValid = false;

    m_privacy_isSet = false;
    m_privacy_isValid = false;

    m_published_at_isSet = false;
    m_published_at_isValid = false;

    m_scheduled_update_isSet = false;
    m_scheduled_update_isValid = false;

    m_short_uuid_isSet = false;
    m_short_uuid_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_thumbnail_path_isSet = false;
    m_thumbnail_path_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_user_history_isSet = false;
    m_user_history_isValid = false;

    m_uuid_isSet = false;
    m_uuid_isValid = false;

    m_views_isSet = false;
    m_views_isValid = false;

    m_wait_transcoding_isSet = false;
    m_wait_transcoding_isValid = false;

    m_comments_enabled_isSet = false;
    m_comments_enabled_isValid = false;

    m_description_path_isSet = false;
    m_description_path_isValid = false;

    m_download_enabled_isSet = false;
    m_download_enabled_isValid = false;

    m_files_isSet = false;
    m_files_isValid = false;

    m_streaming_playlists_isSet = false;
    m_streaming_playlists_isValid = false;

    m_support_isSet = false;
    m_support_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_tracker_urls_isSet = false;
    m_tracker_urls_isValid = false;

    m_viewers_isSet = false;
    m_viewers_isValid = false;
}

void OAIVideoDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoDetails::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_blacklisted_isValid = ::OpenAPI::fromJsonValue(m_blacklisted, json[QString("blacklisted")]);
    m_blacklisted_isSet = !json[QString("blacklisted")].isNull() && m_blacklisted_isValid;

    m_blacklisted_reason_isValid = ::OpenAPI::fromJsonValue(m_blacklisted_reason, json[QString("blacklistedReason")]);
    m_blacklisted_reason_isSet = !json[QString("blacklistedReason")].isNull() && m_blacklisted_reason_isValid;

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_channel_isValid = ::OpenAPI::fromJsonValue(m_channel, json[QString("channel")]);
    m_channel_isSet = !json[QString("channel")].isNull() && m_channel_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_dislikes_isValid = ::OpenAPI::fromJsonValue(m_dislikes, json[QString("dislikes")]);
    m_dislikes_isSet = !json[QString("dislikes")].isNull() && m_dislikes_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_embed_path_isValid = ::OpenAPI::fromJsonValue(m_embed_path, json[QString("embedPath")]);
    m_embed_path_isSet = !json[QString("embedPath")].isNull() && m_embed_path_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_live_isValid = ::OpenAPI::fromJsonValue(m_is_live, json[QString("isLive")]);
    m_is_live_isSet = !json[QString("isLive")].isNull() && m_is_live_isValid;

    m_is_local_isValid = ::OpenAPI::fromJsonValue(m_is_local, json[QString("isLocal")]);
    m_is_local_isSet = !json[QString("isLocal")].isNull() && m_is_local_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_licence_isValid = ::OpenAPI::fromJsonValue(m_licence, json[QString("licence")]);
    m_licence_isSet = !json[QString("licence")].isNull() && m_licence_isValid;

    m_likes_isValid = ::OpenAPI::fromJsonValue(m_likes, json[QString("likes")]);
    m_likes_isSet = !json[QString("likes")].isNull() && m_likes_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_nsfw_isValid = ::OpenAPI::fromJsonValue(m_nsfw, json[QString("nsfw")]);
    m_nsfw_isSet = !json[QString("nsfw")].isNull() && m_nsfw_isValid;

    m_originally_published_at_isValid = ::OpenAPI::fromJsonValue(m_originally_published_at, json[QString("originallyPublishedAt")]);
    m_originally_published_at_isSet = !json[QString("originallyPublishedAt")].isNull() && m_originally_published_at_isValid;

    m_preview_path_isValid = ::OpenAPI::fromJsonValue(m_preview_path, json[QString("previewPath")]);
    m_preview_path_isSet = !json[QString("previewPath")].isNull() && m_preview_path_isValid;

    m_privacy_isValid = ::OpenAPI::fromJsonValue(m_privacy, json[QString("privacy")]);
    m_privacy_isSet = !json[QString("privacy")].isNull() && m_privacy_isValid;

    m_published_at_isValid = ::OpenAPI::fromJsonValue(m_published_at, json[QString("publishedAt")]);
    m_published_at_isSet = !json[QString("publishedAt")].isNull() && m_published_at_isValid;

    m_scheduled_update_isValid = ::OpenAPI::fromJsonValue(m_scheduled_update, json[QString("scheduledUpdate")]);
    m_scheduled_update_isSet = !json[QString("scheduledUpdate")].isNull() && m_scheduled_update_isValid;

    m_short_uuid_isValid = ::OpenAPI::fromJsonValue(m_short_uuid, json[QString("shortUUID")]);
    m_short_uuid_isSet = !json[QString("shortUUID")].isNull() && m_short_uuid_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_thumbnail_path_isValid = ::OpenAPI::fromJsonValue(m_thumbnail_path, json[QString("thumbnailPath")]);
    m_thumbnail_path_isSet = !json[QString("thumbnailPath")].isNull() && m_thumbnail_path_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_user_history_isValid = ::OpenAPI::fromJsonValue(m_user_history, json[QString("userHistory")]);
    m_user_history_isSet = !json[QString("userHistory")].isNull() && m_user_history_isValid;

    m_uuid_isValid = ::OpenAPI::fromJsonValue(m_uuid, json[QString("uuid")]);
    m_uuid_isSet = !json[QString("uuid")].isNull() && m_uuid_isValid;

    m_views_isValid = ::OpenAPI::fromJsonValue(m_views, json[QString("views")]);
    m_views_isSet = !json[QString("views")].isNull() && m_views_isValid;

    m_wait_transcoding_isValid = ::OpenAPI::fromJsonValue(m_wait_transcoding, json[QString("waitTranscoding")]);
    m_wait_transcoding_isSet = !json[QString("waitTranscoding")].isNull() && m_wait_transcoding_isValid;

    m_comments_enabled_isValid = ::OpenAPI::fromJsonValue(m_comments_enabled, json[QString("commentsEnabled")]);
    m_comments_enabled_isSet = !json[QString("commentsEnabled")].isNull() && m_comments_enabled_isValid;

    m_description_path_isValid = ::OpenAPI::fromJsonValue(m_description_path, json[QString("descriptionPath")]);
    m_description_path_isSet = !json[QString("descriptionPath")].isNull() && m_description_path_isValid;

    m_download_enabled_isValid = ::OpenAPI::fromJsonValue(m_download_enabled, json[QString("downloadEnabled")]);
    m_download_enabled_isSet = !json[QString("downloadEnabled")].isNull() && m_download_enabled_isValid;

    m_files_isValid = ::OpenAPI::fromJsonValue(m_files, json[QString("files")]);
    m_files_isSet = !json[QString("files")].isNull() && m_files_isValid;

    m_streaming_playlists_isValid = ::OpenAPI::fromJsonValue(m_streaming_playlists, json[QString("streamingPlaylists")]);
    m_streaming_playlists_isSet = !json[QString("streamingPlaylists")].isNull() && m_streaming_playlists_isValid;

    m_support_isValid = ::OpenAPI::fromJsonValue(m_support, json[QString("support")]);
    m_support_isSet = !json[QString("support")].isNull() && m_support_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_tracker_urls_isValid = ::OpenAPI::fromJsonValue(m_tracker_urls, json[QString("trackerUrls")]);
    m_tracker_urls_isSet = !json[QString("trackerUrls")].isNull() && m_tracker_urls_isValid;

    m_viewers_isValid = ::OpenAPI::fromJsonValue(m_viewers, json[QString("viewers")]);
    m_viewers_isSet = !json[QString("viewers")].isNull() && m_viewers_isValid;
}

QString OAIVideoDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_blacklisted_isSet) {
        obj.insert(QString("blacklisted"), ::OpenAPI::toJsonValue(m_blacklisted));
    }
    if (m_blacklisted_reason_isSet) {
        obj.insert(QString("blacklistedReason"), ::OpenAPI::toJsonValue(m_blacklisted_reason));
    }
    if (m_category.isSet()) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_channel.isSet()) {
        obj.insert(QString("channel"), ::OpenAPI::toJsonValue(m_channel));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_dislikes_isSet) {
        obj.insert(QString("dislikes"), ::OpenAPI::toJsonValue(m_dislikes));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_embed_path_isSet) {
        obj.insert(QString("embedPath"), ::OpenAPI::toJsonValue(m_embed_path));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_live_isSet) {
        obj.insert(QString("isLive"), ::OpenAPI::toJsonValue(m_is_live));
    }
    if (m_is_local_isSet) {
        obj.insert(QString("isLocal"), ::OpenAPI::toJsonValue(m_is_local));
    }
    if (m_language.isSet()) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_licence.isSet()) {
        obj.insert(QString("licence"), ::OpenAPI::toJsonValue(m_licence));
    }
    if (m_likes_isSet) {
        obj.insert(QString("likes"), ::OpenAPI::toJsonValue(m_likes));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_nsfw_isSet) {
        obj.insert(QString("nsfw"), ::OpenAPI::toJsonValue(m_nsfw));
    }
    if (m_originally_published_at_isSet) {
        obj.insert(QString("originallyPublishedAt"), ::OpenAPI::toJsonValue(m_originally_published_at));
    }
    if (m_preview_path_isSet) {
        obj.insert(QString("previewPath"), ::OpenAPI::toJsonValue(m_preview_path));
    }
    if (m_privacy.isSet()) {
        obj.insert(QString("privacy"), ::OpenAPI::toJsonValue(m_privacy));
    }
    if (m_published_at_isSet) {
        obj.insert(QString("publishedAt"), ::OpenAPI::toJsonValue(m_published_at));
    }
    if (m_scheduled_update.isSet()) {
        obj.insert(QString("scheduledUpdate"), ::OpenAPI::toJsonValue(m_scheduled_update));
    }
    if (m_short_uuid_isSet) {
        obj.insert(QString("shortUUID"), ::OpenAPI::toJsonValue(m_short_uuid));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_thumbnail_path_isSet) {
        obj.insert(QString("thumbnailPath"), ::OpenAPI::toJsonValue(m_thumbnail_path));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_user_history.isSet()) {
        obj.insert(QString("userHistory"), ::OpenAPI::toJsonValue(m_user_history));
    }
    if (m_uuid_isSet) {
        obj.insert(QString("uuid"), ::OpenAPI::toJsonValue(m_uuid));
    }
    if (m_views_isSet) {
        obj.insert(QString("views"), ::OpenAPI::toJsonValue(m_views));
    }
    if (m_wait_transcoding_isSet) {
        obj.insert(QString("waitTranscoding"), ::OpenAPI::toJsonValue(m_wait_transcoding));
    }
    if (m_comments_enabled_isSet) {
        obj.insert(QString("commentsEnabled"), ::OpenAPI::toJsonValue(m_comments_enabled));
    }
    if (m_description_path_isSet) {
        obj.insert(QString("descriptionPath"), ::OpenAPI::toJsonValue(m_description_path));
    }
    if (m_download_enabled_isSet) {
        obj.insert(QString("downloadEnabled"), ::OpenAPI::toJsonValue(m_download_enabled));
    }
    if (m_files.size() > 0) {
        obj.insert(QString("files"), ::OpenAPI::toJsonValue(m_files));
    }
    if (m_streaming_playlists.size() > 0) {
        obj.insert(QString("streamingPlaylists"), ::OpenAPI::toJsonValue(m_streaming_playlists));
    }
    if (m_support_isSet) {
        obj.insert(QString("support"), ::OpenAPI::toJsonValue(m_support));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_tracker_urls.size() > 0) {
        obj.insert(QString("trackerUrls"), ::OpenAPI::toJsonValue(m_tracker_urls));
    }
    if (m_viewers_isSet) {
        obj.insert(QString("viewers"), ::OpenAPI::toJsonValue(m_viewers));
    }
    return obj;
}

OAIAccount OAIVideoDetails::getAccount() const {
    return m_account;
}
void OAIVideoDetails::setAccount(const OAIAccount &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAIVideoDetails::is_account_Set() const{
    return m_account_isSet;
}

bool OAIVideoDetails::is_account_Valid() const{
    return m_account_isValid;
}

bool OAIVideoDetails::isBlacklisted() const {
    return m_blacklisted;
}
void OAIVideoDetails::setBlacklisted(const bool &blacklisted) {
    m_blacklisted = blacklisted;
    m_blacklisted_isSet = true;
}

bool OAIVideoDetails::is_blacklisted_Set() const{
    return m_blacklisted_isSet;
}

bool OAIVideoDetails::is_blacklisted_Valid() const{
    return m_blacklisted_isValid;
}

QString OAIVideoDetails::getBlacklistedReason() const {
    return m_blacklisted_reason;
}
void OAIVideoDetails::setBlacklistedReason(const QString &blacklisted_reason) {
    m_blacklisted_reason = blacklisted_reason;
    m_blacklisted_reason_isSet = true;
}

bool OAIVideoDetails::is_blacklisted_reason_Set() const{
    return m_blacklisted_reason_isSet;
}

bool OAIVideoDetails::is_blacklisted_reason_Valid() const{
    return m_blacklisted_reason_isValid;
}

OAIVideoConstantNumber_Category OAIVideoDetails::getCategory() const {
    return m_category;
}
void OAIVideoDetails::setCategory(const OAIVideoConstantNumber_Category &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIVideoDetails::is_category_Set() const{
    return m_category_isSet;
}

bool OAIVideoDetails::is_category_Valid() const{
    return m_category_isValid;
}

OAIVideoChannel OAIVideoDetails::getChannel() const {
    return m_channel;
}
void OAIVideoDetails::setChannel(const OAIVideoChannel &channel) {
    m_channel = channel;
    m_channel_isSet = true;
}

bool OAIVideoDetails::is_channel_Set() const{
    return m_channel_isSet;
}

bool OAIVideoDetails::is_channel_Valid() const{
    return m_channel_isValid;
}

QDateTime OAIVideoDetails::getCreatedAt() const {
    return m_created_at;
}
void OAIVideoDetails::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideoDetails::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideoDetails::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIVideoDetails::getDescription() const {
    return m_description;
}
void OAIVideoDetails::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideoDetails::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideoDetails::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIVideoDetails::getDislikes() const {
    return m_dislikes;
}
void OAIVideoDetails::setDislikes(const qint32 &dislikes) {
    m_dislikes = dislikes;
    m_dislikes_isSet = true;
}

bool OAIVideoDetails::is_dislikes_Set() const{
    return m_dislikes_isSet;
}

bool OAIVideoDetails::is_dislikes_Valid() const{
    return m_dislikes_isValid;
}

qint32 OAIVideoDetails::getDuration() const {
    return m_duration;
}
void OAIVideoDetails::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIVideoDetails::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIVideoDetails::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIVideoDetails::getEmbedPath() const {
    return m_embed_path;
}
void OAIVideoDetails::setEmbedPath(const QString &embed_path) {
    m_embed_path = embed_path;
    m_embed_path_isSet = true;
}

bool OAIVideoDetails::is_embed_path_Set() const{
    return m_embed_path_isSet;
}

bool OAIVideoDetails::is_embed_path_Valid() const{
    return m_embed_path_isValid;
}

qint32 OAIVideoDetails::getId() const {
    return m_id;
}
void OAIVideoDetails::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoDetails::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoDetails::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIVideoDetails::isIsLive() const {
    return m_is_live;
}
void OAIVideoDetails::setIsLive(const bool &is_live) {
    m_is_live = is_live;
    m_is_live_isSet = true;
}

bool OAIVideoDetails::is_is_live_Set() const{
    return m_is_live_isSet;
}

bool OAIVideoDetails::is_is_live_Valid() const{
    return m_is_live_isValid;
}

bool OAIVideoDetails::isIsLocal() const {
    return m_is_local;
}
void OAIVideoDetails::setIsLocal(const bool &is_local) {
    m_is_local = is_local;
    m_is_local_isSet = true;
}

bool OAIVideoDetails::is_is_local_Set() const{
    return m_is_local_isSet;
}

bool OAIVideoDetails::is_is_local_Valid() const{
    return m_is_local_isValid;
}

OAIVideoConstantString_Language OAIVideoDetails::getLanguage() const {
    return m_language;
}
void OAIVideoDetails::setLanguage(const OAIVideoConstantString_Language &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIVideoDetails::is_language_Set() const{
    return m_language_isSet;
}

bool OAIVideoDetails::is_language_Valid() const{
    return m_language_isValid;
}

OAIVideoConstantNumber_Licence OAIVideoDetails::getLicence() const {
    return m_licence;
}
void OAIVideoDetails::setLicence(const OAIVideoConstantNumber_Licence &licence) {
    m_licence = licence;
    m_licence_isSet = true;
}

bool OAIVideoDetails::is_licence_Set() const{
    return m_licence_isSet;
}

bool OAIVideoDetails::is_licence_Valid() const{
    return m_licence_isValid;
}

qint32 OAIVideoDetails::getLikes() const {
    return m_likes;
}
void OAIVideoDetails::setLikes(const qint32 &likes) {
    m_likes = likes;
    m_likes_isSet = true;
}

bool OAIVideoDetails::is_likes_Set() const{
    return m_likes_isSet;
}

bool OAIVideoDetails::is_likes_Valid() const{
    return m_likes_isValid;
}

QString OAIVideoDetails::getName() const {
    return m_name;
}
void OAIVideoDetails::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVideoDetails::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVideoDetails::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIVideoDetails::isNsfw() const {
    return m_nsfw;
}
void OAIVideoDetails::setNsfw(const bool &nsfw) {
    m_nsfw = nsfw;
    m_nsfw_isSet = true;
}

bool OAIVideoDetails::is_nsfw_Set() const{
    return m_nsfw_isSet;
}

bool OAIVideoDetails::is_nsfw_Valid() const{
    return m_nsfw_isValid;
}

QDateTime OAIVideoDetails::getOriginallyPublishedAt() const {
    return m_originally_published_at;
}
void OAIVideoDetails::setOriginallyPublishedAt(const QDateTime &originally_published_at) {
    m_originally_published_at = originally_published_at;
    m_originally_published_at_isSet = true;
}

bool OAIVideoDetails::is_originally_published_at_Set() const{
    return m_originally_published_at_isSet;
}

bool OAIVideoDetails::is_originally_published_at_Valid() const{
    return m_originally_published_at_isValid;
}

QString OAIVideoDetails::getPreviewPath() const {
    return m_preview_path;
}
void OAIVideoDetails::setPreviewPath(const QString &preview_path) {
    m_preview_path = preview_path;
    m_preview_path_isSet = true;
}

bool OAIVideoDetails::is_preview_path_Set() const{
    return m_preview_path_isSet;
}

bool OAIVideoDetails::is_preview_path_Valid() const{
    return m_preview_path_isValid;
}

OAIVideoPrivacyConstant OAIVideoDetails::getPrivacy() const {
    return m_privacy;
}
void OAIVideoDetails::setPrivacy(const OAIVideoPrivacyConstant &privacy) {
    m_privacy = privacy;
    m_privacy_isSet = true;
}

bool OAIVideoDetails::is_privacy_Set() const{
    return m_privacy_isSet;
}

bool OAIVideoDetails::is_privacy_Valid() const{
    return m_privacy_isValid;
}

QDateTime OAIVideoDetails::getPublishedAt() const {
    return m_published_at;
}
void OAIVideoDetails::setPublishedAt(const QDateTime &published_at) {
    m_published_at = published_at;
    m_published_at_isSet = true;
}

bool OAIVideoDetails::is_published_at_Set() const{
    return m_published_at_isSet;
}

bool OAIVideoDetails::is_published_at_Valid() const{
    return m_published_at_isValid;
}

OAIVideoScheduledUpdate OAIVideoDetails::getScheduledUpdate() const {
    return m_scheduled_update;
}
void OAIVideoDetails::setScheduledUpdate(const OAIVideoScheduledUpdate &scheduled_update) {
    m_scheduled_update = scheduled_update;
    m_scheduled_update_isSet = true;
}

bool OAIVideoDetails::is_scheduled_update_Set() const{
    return m_scheduled_update_isSet;
}

bool OAIVideoDetails::is_scheduled_update_Valid() const{
    return m_scheduled_update_isValid;
}

QString OAIVideoDetails::getShortUuid() const {
    return m_short_uuid;
}
void OAIVideoDetails::setShortUuid(const QString &short_uuid) {
    m_short_uuid = short_uuid;
    m_short_uuid_isSet = true;
}

bool OAIVideoDetails::is_short_uuid_Set() const{
    return m_short_uuid_isSet;
}

bool OAIVideoDetails::is_short_uuid_Valid() const{
    return m_short_uuid_isValid;
}

OAIVideoStateConstant OAIVideoDetails::getState() const {
    return m_state;
}
void OAIVideoDetails::setState(const OAIVideoStateConstant &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIVideoDetails::is_state_Set() const{
    return m_state_isSet;
}

bool OAIVideoDetails::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIVideoDetails::getThumbnailPath() const {
    return m_thumbnail_path;
}
void OAIVideoDetails::setThumbnailPath(const QString &thumbnail_path) {
    m_thumbnail_path = thumbnail_path;
    m_thumbnail_path_isSet = true;
}

bool OAIVideoDetails::is_thumbnail_path_Set() const{
    return m_thumbnail_path_isSet;
}

bool OAIVideoDetails::is_thumbnail_path_Valid() const{
    return m_thumbnail_path_isValid;
}

QDateTime OAIVideoDetails::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVideoDetails::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVideoDetails::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVideoDetails::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAIVideo_userHistory OAIVideoDetails::getUserHistory() const {
    return m_user_history;
}
void OAIVideoDetails::setUserHistory(const OAIVideo_userHistory &user_history) {
    m_user_history = user_history;
    m_user_history_isSet = true;
}

bool OAIVideoDetails::is_user_history_Set() const{
    return m_user_history_isSet;
}

bool OAIVideoDetails::is_user_history_Valid() const{
    return m_user_history_isValid;
}

QString OAIVideoDetails::getUuid() const {
    return m_uuid;
}
void OAIVideoDetails::setUuid(const QString &uuid) {
    m_uuid = uuid;
    m_uuid_isSet = true;
}

bool OAIVideoDetails::is_uuid_Set() const{
    return m_uuid_isSet;
}

bool OAIVideoDetails::is_uuid_Valid() const{
    return m_uuid_isValid;
}

qint32 OAIVideoDetails::getViews() const {
    return m_views;
}
void OAIVideoDetails::setViews(const qint32 &views) {
    m_views = views;
    m_views_isSet = true;
}

bool OAIVideoDetails::is_views_Set() const{
    return m_views_isSet;
}

bool OAIVideoDetails::is_views_Valid() const{
    return m_views_isValid;
}

bool OAIVideoDetails::isWaitTranscoding() const {
    return m_wait_transcoding;
}
void OAIVideoDetails::setWaitTranscoding(const bool &wait_transcoding) {
    m_wait_transcoding = wait_transcoding;
    m_wait_transcoding_isSet = true;
}

bool OAIVideoDetails::is_wait_transcoding_Set() const{
    return m_wait_transcoding_isSet;
}

bool OAIVideoDetails::is_wait_transcoding_Valid() const{
    return m_wait_transcoding_isValid;
}

bool OAIVideoDetails::isCommentsEnabled() const {
    return m_comments_enabled;
}
void OAIVideoDetails::setCommentsEnabled(const bool &comments_enabled) {
    m_comments_enabled = comments_enabled;
    m_comments_enabled_isSet = true;
}

bool OAIVideoDetails::is_comments_enabled_Set() const{
    return m_comments_enabled_isSet;
}

bool OAIVideoDetails::is_comments_enabled_Valid() const{
    return m_comments_enabled_isValid;
}

QString OAIVideoDetails::getDescriptionPath() const {
    return m_description_path;
}
void OAIVideoDetails::setDescriptionPath(const QString &description_path) {
    m_description_path = description_path;
    m_description_path_isSet = true;
}

bool OAIVideoDetails::is_description_path_Set() const{
    return m_description_path_isSet;
}

bool OAIVideoDetails::is_description_path_Valid() const{
    return m_description_path_isValid;
}

bool OAIVideoDetails::isDownloadEnabled() const {
    return m_download_enabled;
}
void OAIVideoDetails::setDownloadEnabled(const bool &download_enabled) {
    m_download_enabled = download_enabled;
    m_download_enabled_isSet = true;
}

bool OAIVideoDetails::is_download_enabled_Set() const{
    return m_download_enabled_isSet;
}

bool OAIVideoDetails::is_download_enabled_Valid() const{
    return m_download_enabled_isValid;
}

QList<OAIVideoFile> OAIVideoDetails::getFiles() const {
    return m_files;
}
void OAIVideoDetails::setFiles(const QList<OAIVideoFile> &files) {
    m_files = files;
    m_files_isSet = true;
}

bool OAIVideoDetails::is_files_Set() const{
    return m_files_isSet;
}

bool OAIVideoDetails::is_files_Valid() const{
    return m_files_isValid;
}

QList<OAIVideoStreamingPlaylists> OAIVideoDetails::getStreamingPlaylists() const {
    return m_streaming_playlists;
}
void OAIVideoDetails::setStreamingPlaylists(const QList<OAIVideoStreamingPlaylists> &streaming_playlists) {
    m_streaming_playlists = streaming_playlists;
    m_streaming_playlists_isSet = true;
}

bool OAIVideoDetails::is_streaming_playlists_Set() const{
    return m_streaming_playlists_isSet;
}

bool OAIVideoDetails::is_streaming_playlists_Valid() const{
    return m_streaming_playlists_isValid;
}

QString OAIVideoDetails::getSupport() const {
    return m_support;
}
void OAIVideoDetails::setSupport(const QString &support) {
    m_support = support;
    m_support_isSet = true;
}

bool OAIVideoDetails::is_support_Set() const{
    return m_support_isSet;
}

bool OAIVideoDetails::is_support_Valid() const{
    return m_support_isValid;
}

QList<QString> OAIVideoDetails::getTags() const {
    return m_tags;
}
void OAIVideoDetails::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIVideoDetails::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIVideoDetails::is_tags_Valid() const{
    return m_tags_isValid;
}

QList<QString> OAIVideoDetails::getTrackerUrls() const {
    return m_tracker_urls;
}
void OAIVideoDetails::setTrackerUrls(const QList<QString> &tracker_urls) {
    m_tracker_urls = tracker_urls;
    m_tracker_urls_isSet = true;
}

bool OAIVideoDetails::is_tracker_urls_Set() const{
    return m_tracker_urls_isSet;
}

bool OAIVideoDetails::is_tracker_urls_Valid() const{
    return m_tracker_urls_isValid;
}

qint32 OAIVideoDetails::getViewers() const {
    return m_viewers;
}
void OAIVideoDetails::setViewers(const qint32 &viewers) {
    m_viewers = viewers;
    m_viewers_isSet = true;
}

bool OAIVideoDetails::is_viewers_Set() const{
    return m_viewers_isSet;
}

bool OAIVideoDetails::is_viewers_Valid() const{
    return m_viewers_isValid;
}

bool OAIVideoDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_blacklisted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blacklisted_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dislikes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_embed_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_live_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_local_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_licence.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_likes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nsfw_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_originally_published_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preview_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_privacy.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_published_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_update.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_history.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_views_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wait_transcoding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_download_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_files.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_streaming_playlists.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_support_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracker_urls.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_viewers_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
