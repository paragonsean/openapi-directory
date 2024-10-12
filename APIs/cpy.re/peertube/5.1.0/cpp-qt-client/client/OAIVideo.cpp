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

#include "OAIVideo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideo::OAIVideo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideo::OAIVideo() {
    this->initializeModel();
}

OAIVideo::~OAIVideo() {}

void OAIVideo::initializeModel() {

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
}

void OAIVideo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideo::fromJsonObject(QJsonObject json) {

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
}

QString OAIVideo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideo::asJsonObject() const {
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
    return obj;
}

OAIAccountSummary OAIVideo::getAccount() const {
    return m_account;
}
void OAIVideo::setAccount(const OAIAccountSummary &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAIVideo::is_account_Set() const{
    return m_account_isSet;
}

bool OAIVideo::is_account_Valid() const{
    return m_account_isValid;
}

bool OAIVideo::isBlacklisted() const {
    return m_blacklisted;
}
void OAIVideo::setBlacklisted(const bool &blacklisted) {
    m_blacklisted = blacklisted;
    m_blacklisted_isSet = true;
}

bool OAIVideo::is_blacklisted_Set() const{
    return m_blacklisted_isSet;
}

bool OAIVideo::is_blacklisted_Valid() const{
    return m_blacklisted_isValid;
}

QString OAIVideo::getBlacklistedReason() const {
    return m_blacklisted_reason;
}
void OAIVideo::setBlacklistedReason(const QString &blacklisted_reason) {
    m_blacklisted_reason = blacklisted_reason;
    m_blacklisted_reason_isSet = true;
}

bool OAIVideo::is_blacklisted_reason_Set() const{
    return m_blacklisted_reason_isSet;
}

bool OAIVideo::is_blacklisted_reason_Valid() const{
    return m_blacklisted_reason_isValid;
}

OAIVideoConstantNumber_Category OAIVideo::getCategory() const {
    return m_category;
}
void OAIVideo::setCategory(const OAIVideoConstantNumber_Category &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIVideo::is_category_Set() const{
    return m_category_isSet;
}

bool OAIVideo::is_category_Valid() const{
    return m_category_isValid;
}

OAIVideoChannelSummary OAIVideo::getChannel() const {
    return m_channel;
}
void OAIVideo::setChannel(const OAIVideoChannelSummary &channel) {
    m_channel = channel;
    m_channel_isSet = true;
}

bool OAIVideo::is_channel_Set() const{
    return m_channel_isSet;
}

bool OAIVideo::is_channel_Valid() const{
    return m_channel_isValid;
}

QDateTime OAIVideo::getCreatedAt() const {
    return m_created_at;
}
void OAIVideo::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideo::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideo::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIVideo::getDescription() const {
    return m_description;
}
void OAIVideo::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideo::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideo::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIVideo::getDislikes() const {
    return m_dislikes;
}
void OAIVideo::setDislikes(const qint32 &dislikes) {
    m_dislikes = dislikes;
    m_dislikes_isSet = true;
}

bool OAIVideo::is_dislikes_Set() const{
    return m_dislikes_isSet;
}

bool OAIVideo::is_dislikes_Valid() const{
    return m_dislikes_isValid;
}

qint32 OAIVideo::getDuration() const {
    return m_duration;
}
void OAIVideo::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIVideo::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIVideo::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIVideo::getEmbedPath() const {
    return m_embed_path;
}
void OAIVideo::setEmbedPath(const QString &embed_path) {
    m_embed_path = embed_path;
    m_embed_path_isSet = true;
}

bool OAIVideo::is_embed_path_Set() const{
    return m_embed_path_isSet;
}

bool OAIVideo::is_embed_path_Valid() const{
    return m_embed_path_isValid;
}

qint32 OAIVideo::getId() const {
    return m_id;
}
void OAIVideo::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideo::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideo::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIVideo::isIsLive() const {
    return m_is_live;
}
void OAIVideo::setIsLive(const bool &is_live) {
    m_is_live = is_live;
    m_is_live_isSet = true;
}

bool OAIVideo::is_is_live_Set() const{
    return m_is_live_isSet;
}

bool OAIVideo::is_is_live_Valid() const{
    return m_is_live_isValid;
}

bool OAIVideo::isIsLocal() const {
    return m_is_local;
}
void OAIVideo::setIsLocal(const bool &is_local) {
    m_is_local = is_local;
    m_is_local_isSet = true;
}

bool OAIVideo::is_is_local_Set() const{
    return m_is_local_isSet;
}

bool OAIVideo::is_is_local_Valid() const{
    return m_is_local_isValid;
}

OAIVideoConstantString_Language OAIVideo::getLanguage() const {
    return m_language;
}
void OAIVideo::setLanguage(const OAIVideoConstantString_Language &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIVideo::is_language_Set() const{
    return m_language_isSet;
}

bool OAIVideo::is_language_Valid() const{
    return m_language_isValid;
}

OAIVideoConstantNumber_Licence OAIVideo::getLicence() const {
    return m_licence;
}
void OAIVideo::setLicence(const OAIVideoConstantNumber_Licence &licence) {
    m_licence = licence;
    m_licence_isSet = true;
}

bool OAIVideo::is_licence_Set() const{
    return m_licence_isSet;
}

bool OAIVideo::is_licence_Valid() const{
    return m_licence_isValid;
}

qint32 OAIVideo::getLikes() const {
    return m_likes;
}
void OAIVideo::setLikes(const qint32 &likes) {
    m_likes = likes;
    m_likes_isSet = true;
}

bool OAIVideo::is_likes_Set() const{
    return m_likes_isSet;
}

bool OAIVideo::is_likes_Valid() const{
    return m_likes_isValid;
}

QString OAIVideo::getName() const {
    return m_name;
}
void OAIVideo::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVideo::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVideo::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIVideo::isNsfw() const {
    return m_nsfw;
}
void OAIVideo::setNsfw(const bool &nsfw) {
    m_nsfw = nsfw;
    m_nsfw_isSet = true;
}

bool OAIVideo::is_nsfw_Set() const{
    return m_nsfw_isSet;
}

bool OAIVideo::is_nsfw_Valid() const{
    return m_nsfw_isValid;
}

QDateTime OAIVideo::getOriginallyPublishedAt() const {
    return m_originally_published_at;
}
void OAIVideo::setOriginallyPublishedAt(const QDateTime &originally_published_at) {
    m_originally_published_at = originally_published_at;
    m_originally_published_at_isSet = true;
}

bool OAIVideo::is_originally_published_at_Set() const{
    return m_originally_published_at_isSet;
}

bool OAIVideo::is_originally_published_at_Valid() const{
    return m_originally_published_at_isValid;
}

QString OAIVideo::getPreviewPath() const {
    return m_preview_path;
}
void OAIVideo::setPreviewPath(const QString &preview_path) {
    m_preview_path = preview_path;
    m_preview_path_isSet = true;
}

bool OAIVideo::is_preview_path_Set() const{
    return m_preview_path_isSet;
}

bool OAIVideo::is_preview_path_Valid() const{
    return m_preview_path_isValid;
}

OAIVideoPrivacyConstant OAIVideo::getPrivacy() const {
    return m_privacy;
}
void OAIVideo::setPrivacy(const OAIVideoPrivacyConstant &privacy) {
    m_privacy = privacy;
    m_privacy_isSet = true;
}

bool OAIVideo::is_privacy_Set() const{
    return m_privacy_isSet;
}

bool OAIVideo::is_privacy_Valid() const{
    return m_privacy_isValid;
}

QDateTime OAIVideo::getPublishedAt() const {
    return m_published_at;
}
void OAIVideo::setPublishedAt(const QDateTime &published_at) {
    m_published_at = published_at;
    m_published_at_isSet = true;
}

bool OAIVideo::is_published_at_Set() const{
    return m_published_at_isSet;
}

bool OAIVideo::is_published_at_Valid() const{
    return m_published_at_isValid;
}

OAIVideoScheduledUpdate OAIVideo::getScheduledUpdate() const {
    return m_scheduled_update;
}
void OAIVideo::setScheduledUpdate(const OAIVideoScheduledUpdate &scheduled_update) {
    m_scheduled_update = scheduled_update;
    m_scheduled_update_isSet = true;
}

bool OAIVideo::is_scheduled_update_Set() const{
    return m_scheduled_update_isSet;
}

bool OAIVideo::is_scheduled_update_Valid() const{
    return m_scheduled_update_isValid;
}

QString OAIVideo::getShortUuid() const {
    return m_short_uuid;
}
void OAIVideo::setShortUuid(const QString &short_uuid) {
    m_short_uuid = short_uuid;
    m_short_uuid_isSet = true;
}

bool OAIVideo::is_short_uuid_Set() const{
    return m_short_uuid_isSet;
}

bool OAIVideo::is_short_uuid_Valid() const{
    return m_short_uuid_isValid;
}

OAIVideoStateConstant OAIVideo::getState() const {
    return m_state;
}
void OAIVideo::setState(const OAIVideoStateConstant &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIVideo::is_state_Set() const{
    return m_state_isSet;
}

bool OAIVideo::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIVideo::getThumbnailPath() const {
    return m_thumbnail_path;
}
void OAIVideo::setThumbnailPath(const QString &thumbnail_path) {
    m_thumbnail_path = thumbnail_path;
    m_thumbnail_path_isSet = true;
}

bool OAIVideo::is_thumbnail_path_Set() const{
    return m_thumbnail_path_isSet;
}

bool OAIVideo::is_thumbnail_path_Valid() const{
    return m_thumbnail_path_isValid;
}

QDateTime OAIVideo::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVideo::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVideo::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVideo::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAIVideo_userHistory OAIVideo::getUserHistory() const {
    return m_user_history;
}
void OAIVideo::setUserHistory(const OAIVideo_userHistory &user_history) {
    m_user_history = user_history;
    m_user_history_isSet = true;
}

bool OAIVideo::is_user_history_Set() const{
    return m_user_history_isSet;
}

bool OAIVideo::is_user_history_Valid() const{
    return m_user_history_isValid;
}

QString OAIVideo::getUuid() const {
    return m_uuid;
}
void OAIVideo::setUuid(const QString &uuid) {
    m_uuid = uuid;
    m_uuid_isSet = true;
}

bool OAIVideo::is_uuid_Set() const{
    return m_uuid_isSet;
}

bool OAIVideo::is_uuid_Valid() const{
    return m_uuid_isValid;
}

qint32 OAIVideo::getViews() const {
    return m_views;
}
void OAIVideo::setViews(const qint32 &views) {
    m_views = views;
    m_views_isSet = true;
}

bool OAIVideo::is_views_Set() const{
    return m_views_isSet;
}

bool OAIVideo::is_views_Valid() const{
    return m_views_isValid;
}

bool OAIVideo::isWaitTranscoding() const {
    return m_wait_transcoding;
}
void OAIVideo::setWaitTranscoding(const bool &wait_transcoding) {
    m_wait_transcoding = wait_transcoding;
    m_wait_transcoding_isSet = true;
}

bool OAIVideo::is_wait_transcoding_Set() const{
    return m_wait_transcoding_isSet;
}

bool OAIVideo::is_wait_transcoding_Valid() const{
    return m_wait_transcoding_isValid;
}

bool OAIVideo::isSet() const {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIVideo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
