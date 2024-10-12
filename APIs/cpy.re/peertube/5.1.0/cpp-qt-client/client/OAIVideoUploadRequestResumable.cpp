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

#include "OAIVideoUploadRequestResumable.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoUploadRequestResumable::OAIVideoUploadRequestResumable(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoUploadRequestResumable::OAIVideoUploadRequestResumable() {
    this->initializeModel();
}

OAIVideoUploadRequestResumable::~OAIVideoUploadRequestResumable() {}

void OAIVideoUploadRequestResumable::initializeModel() {

    m_category_isSet = false;
    m_category_isValid = false;

    m_channel_id_isSet = false;
    m_channel_id_isValid = false;

    m_comments_enabled_isSet = false;
    m_comments_enabled_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_download_enabled_isSet = false;
    m_download_enabled_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_licence_isSet = false;
    m_licence_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_nsfw_isSet = false;
    m_nsfw_isValid = false;

    m_originally_published_at_isSet = false;
    m_originally_published_at_isValid = false;

    m_previewfile_isSet = false;
    m_previewfile_isValid = false;

    m_privacy_isSet = false;
    m_privacy_isValid = false;

    m_schedule_update_isSet = false;
    m_schedule_update_isValid = false;

    m_support_isSet = false;
    m_support_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_thumbnailfile_isSet = false;
    m_thumbnailfile_isValid = false;

    m_wait_transcoding_isSet = false;
    m_wait_transcoding_isValid = false;

    m_filename_isSet = false;
    m_filename_isValid = false;
}

void OAIVideoUploadRequestResumable::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoUploadRequestResumable::fromJsonObject(QJsonObject json) {

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_channel_id_isValid = ::OpenAPI::fromJsonValue(m_channel_id, json[QString("channelId")]);
    m_channel_id_isSet = !json[QString("channelId")].isNull() && m_channel_id_isValid;

    m_comments_enabled_isValid = ::OpenAPI::fromJsonValue(m_comments_enabled, json[QString("commentsEnabled")]);
    m_comments_enabled_isSet = !json[QString("commentsEnabled")].isNull() && m_comments_enabled_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_download_enabled_isValid = ::OpenAPI::fromJsonValue(m_download_enabled, json[QString("downloadEnabled")]);
    m_download_enabled_isSet = !json[QString("downloadEnabled")].isNull() && m_download_enabled_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_licence_isValid = ::OpenAPI::fromJsonValue(m_licence, json[QString("licence")]);
    m_licence_isSet = !json[QString("licence")].isNull() && m_licence_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_nsfw_isValid = ::OpenAPI::fromJsonValue(m_nsfw, json[QString("nsfw")]);
    m_nsfw_isSet = !json[QString("nsfw")].isNull() && m_nsfw_isValid;

    m_originally_published_at_isValid = ::OpenAPI::fromJsonValue(m_originally_published_at, json[QString("originallyPublishedAt")]);
    m_originally_published_at_isSet = !json[QString("originallyPublishedAt")].isNull() && m_originally_published_at_isValid;

    m_previewfile_isValid = ::OpenAPI::fromJsonValue(m_previewfile, json[QString("previewfile")]);
    m_previewfile_isSet = !json[QString("previewfile")].isNull() && m_previewfile_isValid;

    m_privacy_isValid = ::OpenAPI::fromJsonValue(m_privacy, json[QString("privacy")]);
    m_privacy_isSet = !json[QString("privacy")].isNull() && m_privacy_isValid;

    m_schedule_update_isValid = ::OpenAPI::fromJsonValue(m_schedule_update, json[QString("scheduleUpdate")]);
    m_schedule_update_isSet = !json[QString("scheduleUpdate")].isNull() && m_schedule_update_isValid;

    m_support_isValid = ::OpenAPI::fromJsonValue(m_support, json[QString("support")]);
    m_support_isSet = !json[QString("support")].isNull() && m_support_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_thumbnailfile_isValid = ::OpenAPI::fromJsonValue(m_thumbnailfile, json[QString("thumbnailfile")]);
    m_thumbnailfile_isSet = !json[QString("thumbnailfile")].isNull() && m_thumbnailfile_isValid;

    m_wait_transcoding_isValid = ::OpenAPI::fromJsonValue(m_wait_transcoding, json[QString("waitTranscoding")]);
    m_wait_transcoding_isSet = !json[QString("waitTranscoding")].isNull() && m_wait_transcoding_isValid;

    m_filename_isValid = ::OpenAPI::fromJsonValue(m_filename, json[QString("filename")]);
    m_filename_isSet = !json[QString("filename")].isNull() && m_filename_isValid;
}

QString OAIVideoUploadRequestResumable::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoUploadRequestResumable::asJsonObject() const {
    QJsonObject obj;
    if (m_category_isSet) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_channel_id_isSet) {
        obj.insert(QString("channelId"), ::OpenAPI::toJsonValue(m_channel_id));
    }
    if (m_comments_enabled_isSet) {
        obj.insert(QString("commentsEnabled"), ::OpenAPI::toJsonValue(m_comments_enabled));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_download_enabled_isSet) {
        obj.insert(QString("downloadEnabled"), ::OpenAPI::toJsonValue(m_download_enabled));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_licence_isSet) {
        obj.insert(QString("licence"), ::OpenAPI::toJsonValue(m_licence));
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
    if (m_previewfile.isSet()) {
        obj.insert(QString("previewfile"), ::OpenAPI::toJsonValue(m_previewfile));
    }
    if (m_privacy.isSet()) {
        obj.insert(QString("privacy"), ::OpenAPI::toJsonValue(m_privacy));
    }
    if (m_schedule_update.isSet()) {
        obj.insert(QString("scheduleUpdate"), ::OpenAPI::toJsonValue(m_schedule_update));
    }
    if (m_support_isSet) {
        obj.insert(QString("support"), ::OpenAPI::toJsonValue(m_support));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_thumbnailfile.isSet()) {
        obj.insert(QString("thumbnailfile"), ::OpenAPI::toJsonValue(m_thumbnailfile));
    }
    if (m_wait_transcoding_isSet) {
        obj.insert(QString("waitTranscoding"), ::OpenAPI::toJsonValue(m_wait_transcoding));
    }
    if (m_filename_isSet) {
        obj.insert(QString("filename"), ::OpenAPI::toJsonValue(m_filename));
    }
    return obj;
}

qint32 OAIVideoUploadRequestResumable::getCategory() const {
    return m_category;
}
void OAIVideoUploadRequestResumable::setCategory(const qint32 &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_category_Set() const{
    return m_category_isSet;
}

bool OAIVideoUploadRequestResumable::is_category_Valid() const{
    return m_category_isValid;
}

qint32 OAIVideoUploadRequestResumable::getChannelId() const {
    return m_channel_id;
}
void OAIVideoUploadRequestResumable::setChannelId(const qint32 &channel_id) {
    m_channel_id = channel_id;
    m_channel_id_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_channel_id_Set() const{
    return m_channel_id_isSet;
}

bool OAIVideoUploadRequestResumable::is_channel_id_Valid() const{
    return m_channel_id_isValid;
}

bool OAIVideoUploadRequestResumable::isCommentsEnabled() const {
    return m_comments_enabled;
}
void OAIVideoUploadRequestResumable::setCommentsEnabled(const bool &comments_enabled) {
    m_comments_enabled = comments_enabled;
    m_comments_enabled_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_comments_enabled_Set() const{
    return m_comments_enabled_isSet;
}

bool OAIVideoUploadRequestResumable::is_comments_enabled_Valid() const{
    return m_comments_enabled_isValid;
}

QString OAIVideoUploadRequestResumable::getDescription() const {
    return m_description;
}
void OAIVideoUploadRequestResumable::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideoUploadRequestResumable::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIVideoUploadRequestResumable::isDownloadEnabled() const {
    return m_download_enabled;
}
void OAIVideoUploadRequestResumable::setDownloadEnabled(const bool &download_enabled) {
    m_download_enabled = download_enabled;
    m_download_enabled_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_download_enabled_Set() const{
    return m_download_enabled_isSet;
}

bool OAIVideoUploadRequestResumable::is_download_enabled_Valid() const{
    return m_download_enabled_isValid;
}

QString OAIVideoUploadRequestResumable::getLanguage() const {
    return m_language;
}
void OAIVideoUploadRequestResumable::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_language_Set() const{
    return m_language_isSet;
}

bool OAIVideoUploadRequestResumable::is_language_Valid() const{
    return m_language_isValid;
}

qint32 OAIVideoUploadRequestResumable::getLicence() const {
    return m_licence;
}
void OAIVideoUploadRequestResumable::setLicence(const qint32 &licence) {
    m_licence = licence;
    m_licence_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_licence_Set() const{
    return m_licence_isSet;
}

bool OAIVideoUploadRequestResumable::is_licence_Valid() const{
    return m_licence_isValid;
}

QString OAIVideoUploadRequestResumable::getName() const {
    return m_name;
}
void OAIVideoUploadRequestResumable::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVideoUploadRequestResumable::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIVideoUploadRequestResumable::isNsfw() const {
    return m_nsfw;
}
void OAIVideoUploadRequestResumable::setNsfw(const bool &nsfw) {
    m_nsfw = nsfw;
    m_nsfw_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_nsfw_Set() const{
    return m_nsfw_isSet;
}

bool OAIVideoUploadRequestResumable::is_nsfw_Valid() const{
    return m_nsfw_isValid;
}

QDateTime OAIVideoUploadRequestResumable::getOriginallyPublishedAt() const {
    return m_originally_published_at;
}
void OAIVideoUploadRequestResumable::setOriginallyPublishedAt(const QDateTime &originally_published_at) {
    m_originally_published_at = originally_published_at;
    m_originally_published_at_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_originally_published_at_Set() const{
    return m_originally_published_at_isSet;
}

bool OAIVideoUploadRequestResumable::is_originally_published_at_Valid() const{
    return m_originally_published_at_isValid;
}

OAIHttpFileElement OAIVideoUploadRequestResumable::getPreviewfile() const {
    return m_previewfile;
}
void OAIVideoUploadRequestResumable::setPreviewfile(const OAIHttpFileElement &previewfile) {
    m_previewfile = previewfile;
    m_previewfile_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_previewfile_Set() const{
    return m_previewfile_isSet;
}

bool OAIVideoUploadRequestResumable::is_previewfile_Valid() const{
    return m_previewfile_isValid;
}

OAIVideoPrivacySet OAIVideoUploadRequestResumable::getPrivacy() const {
    return m_privacy;
}
void OAIVideoUploadRequestResumable::setPrivacy(const OAIVideoPrivacySet &privacy) {
    m_privacy = privacy;
    m_privacy_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_privacy_Set() const{
    return m_privacy_isSet;
}

bool OAIVideoUploadRequestResumable::is_privacy_Valid() const{
    return m_privacy_isValid;
}

OAIVideoScheduledUpdate OAIVideoUploadRequestResumable::getScheduleUpdate() const {
    return m_schedule_update;
}
void OAIVideoUploadRequestResumable::setScheduleUpdate(const OAIVideoScheduledUpdate &schedule_update) {
    m_schedule_update = schedule_update;
    m_schedule_update_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_schedule_update_Set() const{
    return m_schedule_update_isSet;
}

bool OAIVideoUploadRequestResumable::is_schedule_update_Valid() const{
    return m_schedule_update_isValid;
}

QString OAIVideoUploadRequestResumable::getSupport() const {
    return m_support;
}
void OAIVideoUploadRequestResumable::setSupport(const QString &support) {
    m_support = support;
    m_support_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_support_Set() const{
    return m_support_isSet;
}

bool OAIVideoUploadRequestResumable::is_support_Valid() const{
    return m_support_isValid;
}

QSet<QString> OAIVideoUploadRequestResumable::getTags() const {
    return m_tags;
}
void OAIVideoUploadRequestResumable::setTags(const QSet<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIVideoUploadRequestResumable::is_tags_Valid() const{
    return m_tags_isValid;
}

OAIHttpFileElement OAIVideoUploadRequestResumable::getThumbnailfile() const {
    return m_thumbnailfile;
}
void OAIVideoUploadRequestResumable::setThumbnailfile(const OAIHttpFileElement &thumbnailfile) {
    m_thumbnailfile = thumbnailfile;
    m_thumbnailfile_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_thumbnailfile_Set() const{
    return m_thumbnailfile_isSet;
}

bool OAIVideoUploadRequestResumable::is_thumbnailfile_Valid() const{
    return m_thumbnailfile_isValid;
}

bool OAIVideoUploadRequestResumable::isWaitTranscoding() const {
    return m_wait_transcoding;
}
void OAIVideoUploadRequestResumable::setWaitTranscoding(const bool &wait_transcoding) {
    m_wait_transcoding = wait_transcoding;
    m_wait_transcoding_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_wait_transcoding_Set() const{
    return m_wait_transcoding_isSet;
}

bool OAIVideoUploadRequestResumable::is_wait_transcoding_Valid() const{
    return m_wait_transcoding_isValid;
}

QString OAIVideoUploadRequestResumable::getFilename() const {
    return m_filename;
}
void OAIVideoUploadRequestResumable::setFilename(const QString &filename) {
    m_filename = filename;
    m_filename_isSet = true;
}

bool OAIVideoUploadRequestResumable::is_filename_Set() const{
    return m_filename_isSet;
}

bool OAIVideoUploadRequestResumable::is_filename_Valid() const{
    return m_filename_isValid;
}

bool OAIVideoUploadRequestResumable::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_download_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_licence_isSet) {
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

        if (m_previewfile.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_privacy.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_update.isSet()) {
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

        if (m_thumbnailfile.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_wait_transcoding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filename_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoUploadRequestResumable::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_channel_id_isValid && m_name_isValid && m_filename_isValid && true;
}

} // namespace OpenAPI
