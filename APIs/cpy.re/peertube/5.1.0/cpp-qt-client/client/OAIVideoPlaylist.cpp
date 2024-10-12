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

#include "OAIVideoPlaylist.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoPlaylist::OAIVideoPlaylist(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoPlaylist::OAIVideoPlaylist() {
    this->initializeModel();
}

OAIVideoPlaylist::~OAIVideoPlaylist() {}

void OAIVideoPlaylist::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_local_isSet = false;
    m_is_local_isValid = false;

    m_owner_account_isSet = false;
    m_owner_account_isValid = false;

    m_privacy_isSet = false;
    m_privacy_isValid = false;

    m_short_uuid_isSet = false;
    m_short_uuid_isValid = false;

    m_thumbnail_path_isSet = false;
    m_thumbnail_path_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_uuid_isSet = false;
    m_uuid_isValid = false;

    m_video_channel_isSet = false;
    m_video_channel_isValid = false;

    m_video_length_isSet = false;
    m_video_length_isValid = false;
}

void OAIVideoPlaylist::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoPlaylist::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_local_isValid = ::OpenAPI::fromJsonValue(m_is_local, json[QString("isLocal")]);
    m_is_local_isSet = !json[QString("isLocal")].isNull() && m_is_local_isValid;

    m_owner_account_isValid = ::OpenAPI::fromJsonValue(m_owner_account, json[QString("ownerAccount")]);
    m_owner_account_isSet = !json[QString("ownerAccount")].isNull() && m_owner_account_isValid;

    m_privacy_isValid = ::OpenAPI::fromJsonValue(m_privacy, json[QString("privacy")]);
    m_privacy_isSet = !json[QString("privacy")].isNull() && m_privacy_isValid;

    m_short_uuid_isValid = ::OpenAPI::fromJsonValue(m_short_uuid, json[QString("shortUUID")]);
    m_short_uuid_isSet = !json[QString("shortUUID")].isNull() && m_short_uuid_isValid;

    m_thumbnail_path_isValid = ::OpenAPI::fromJsonValue(m_thumbnail_path, json[QString("thumbnailPath")]);
    m_thumbnail_path_isSet = !json[QString("thumbnailPath")].isNull() && m_thumbnail_path_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_uuid_isValid = ::OpenAPI::fromJsonValue(m_uuid, json[QString("uuid")]);
    m_uuid_isSet = !json[QString("uuid")].isNull() && m_uuid_isValid;

    m_video_channel_isValid = ::OpenAPI::fromJsonValue(m_video_channel, json[QString("videoChannel")]);
    m_video_channel_isSet = !json[QString("videoChannel")].isNull() && m_video_channel_isValid;

    m_video_length_isValid = ::OpenAPI::fromJsonValue(m_video_length, json[QString("videoLength")]);
    m_video_length_isSet = !json[QString("videoLength")].isNull() && m_video_length_isValid;
}

QString OAIVideoPlaylist::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoPlaylist::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_local_isSet) {
        obj.insert(QString("isLocal"), ::OpenAPI::toJsonValue(m_is_local));
    }
    if (m_owner_account.isSet()) {
        obj.insert(QString("ownerAccount"), ::OpenAPI::toJsonValue(m_owner_account));
    }
    if (m_privacy.isSet()) {
        obj.insert(QString("privacy"), ::OpenAPI::toJsonValue(m_privacy));
    }
    if (m_short_uuid_isSet) {
        obj.insert(QString("shortUUID"), ::OpenAPI::toJsonValue(m_short_uuid));
    }
    if (m_thumbnail_path_isSet) {
        obj.insert(QString("thumbnailPath"), ::OpenAPI::toJsonValue(m_thumbnail_path));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_uuid_isSet) {
        obj.insert(QString("uuid"), ::OpenAPI::toJsonValue(m_uuid));
    }
    if (m_video_channel.isSet()) {
        obj.insert(QString("videoChannel"), ::OpenAPI::toJsonValue(m_video_channel));
    }
    if (m_video_length_isSet) {
        obj.insert(QString("videoLength"), ::OpenAPI::toJsonValue(m_video_length));
    }
    return obj;
}

QDateTime OAIVideoPlaylist::getCreatedAt() const {
    return m_created_at;
}
void OAIVideoPlaylist::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideoPlaylist::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideoPlaylist::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIVideoPlaylist::getDescription() const {
    return m_description;
}
void OAIVideoPlaylist::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideoPlaylist::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideoPlaylist::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIVideoPlaylist::getDisplayName() const {
    return m_display_name;
}
void OAIVideoPlaylist::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIVideoPlaylist::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIVideoPlaylist::is_display_name_Valid() const{
    return m_display_name_isValid;
}

qint32 OAIVideoPlaylist::getId() const {
    return m_id;
}
void OAIVideoPlaylist::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoPlaylist::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoPlaylist::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIVideoPlaylist::isIsLocal() const {
    return m_is_local;
}
void OAIVideoPlaylist::setIsLocal(const bool &is_local) {
    m_is_local = is_local;
    m_is_local_isSet = true;
}

bool OAIVideoPlaylist::is_is_local_Set() const{
    return m_is_local_isSet;
}

bool OAIVideoPlaylist::is_is_local_Valid() const{
    return m_is_local_isValid;
}

OAIAccountSummary OAIVideoPlaylist::getOwnerAccount() const {
    return m_owner_account;
}
void OAIVideoPlaylist::setOwnerAccount(const OAIAccountSummary &owner_account) {
    m_owner_account = owner_account;
    m_owner_account_isSet = true;
}

bool OAIVideoPlaylist::is_owner_account_Set() const{
    return m_owner_account_isSet;
}

bool OAIVideoPlaylist::is_owner_account_Valid() const{
    return m_owner_account_isValid;
}

OAIVideoPlaylistPrivacyConstant OAIVideoPlaylist::getPrivacy() const {
    return m_privacy;
}
void OAIVideoPlaylist::setPrivacy(const OAIVideoPlaylistPrivacyConstant &privacy) {
    m_privacy = privacy;
    m_privacy_isSet = true;
}

bool OAIVideoPlaylist::is_privacy_Set() const{
    return m_privacy_isSet;
}

bool OAIVideoPlaylist::is_privacy_Valid() const{
    return m_privacy_isValid;
}

QString OAIVideoPlaylist::getShortUuid() const {
    return m_short_uuid;
}
void OAIVideoPlaylist::setShortUuid(const QString &short_uuid) {
    m_short_uuid = short_uuid;
    m_short_uuid_isSet = true;
}

bool OAIVideoPlaylist::is_short_uuid_Set() const{
    return m_short_uuid_isSet;
}

bool OAIVideoPlaylist::is_short_uuid_Valid() const{
    return m_short_uuid_isValid;
}

QString OAIVideoPlaylist::getThumbnailPath() const {
    return m_thumbnail_path;
}
void OAIVideoPlaylist::setThumbnailPath(const QString &thumbnail_path) {
    m_thumbnail_path = thumbnail_path;
    m_thumbnail_path_isSet = true;
}

bool OAIVideoPlaylist::is_thumbnail_path_Set() const{
    return m_thumbnail_path_isSet;
}

bool OAIVideoPlaylist::is_thumbnail_path_Valid() const{
    return m_thumbnail_path_isValid;
}

OAIVideoPlaylistTypeConstant OAIVideoPlaylist::getType() const {
    return m_type;
}
void OAIVideoPlaylist::setType(const OAIVideoPlaylistTypeConstant &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIVideoPlaylist::is_type_Set() const{
    return m_type_isSet;
}

bool OAIVideoPlaylist::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAIVideoPlaylist::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVideoPlaylist::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVideoPlaylist::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVideoPlaylist::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIVideoPlaylist::getUuid() const {
    return m_uuid;
}
void OAIVideoPlaylist::setUuid(const QString &uuid) {
    m_uuid = uuid;
    m_uuid_isSet = true;
}

bool OAIVideoPlaylist::is_uuid_Set() const{
    return m_uuid_isSet;
}

bool OAIVideoPlaylist::is_uuid_Valid() const{
    return m_uuid_isValid;
}

OAIVideoChannelSummary OAIVideoPlaylist::getVideoChannel() const {
    return m_video_channel;
}
void OAIVideoPlaylist::setVideoChannel(const OAIVideoChannelSummary &video_channel) {
    m_video_channel = video_channel;
    m_video_channel_isSet = true;
}

bool OAIVideoPlaylist::is_video_channel_Set() const{
    return m_video_channel_isSet;
}

bool OAIVideoPlaylist::is_video_channel_Valid() const{
    return m_video_channel_isValid;
}

qint32 OAIVideoPlaylist::getVideoLength() const {
    return m_video_length;
}
void OAIVideoPlaylist::setVideoLength(const qint32 &video_length) {
    m_video_length = video_length;
    m_video_length_isSet = true;
}

bool OAIVideoPlaylist::is_video_length_Set() const{
    return m_video_length_isSet;
}

bool OAIVideoPlaylist::is_video_length_Valid() const{
    return m_video_length_isValid;
}

bool OAIVideoPlaylist::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_local_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_privacy.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_channel.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_length_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoPlaylist::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
