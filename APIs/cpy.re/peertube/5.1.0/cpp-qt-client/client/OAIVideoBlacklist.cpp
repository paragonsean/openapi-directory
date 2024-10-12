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

#include "OAIVideoBlacklist.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoBlacklist::OAIVideoBlacklist(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoBlacklist::OAIVideoBlacklist() {
    this->initializeModel();
}

OAIVideoBlacklist::~OAIVideoBlacklist() {}

void OAIVideoBlacklist::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_dislikes_isSet = false;
    m_dislikes_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_likes_isSet = false;
    m_likes_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_nsfw_isSet = false;
    m_nsfw_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_uuid_isSet = false;
    m_uuid_isValid = false;

    m_video_id_isSet = false;
    m_video_id_isValid = false;

    m_views_isSet = false;
    m_views_isValid = false;
}

void OAIVideoBlacklist::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoBlacklist::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_dislikes_isValid = ::OpenAPI::fromJsonValue(m_dislikes, json[QString("dislikes")]);
    m_dislikes_isSet = !json[QString("dislikes")].isNull() && m_dislikes_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_likes_isValid = ::OpenAPI::fromJsonValue(m_likes, json[QString("likes")]);
    m_likes_isSet = !json[QString("likes")].isNull() && m_likes_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_nsfw_isValid = ::OpenAPI::fromJsonValue(m_nsfw, json[QString("nsfw")]);
    m_nsfw_isSet = !json[QString("nsfw")].isNull() && m_nsfw_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_uuid_isValid = ::OpenAPI::fromJsonValue(m_uuid, json[QString("uuid")]);
    m_uuid_isSet = !json[QString("uuid")].isNull() && m_uuid_isValid;

    m_video_id_isValid = ::OpenAPI::fromJsonValue(m_video_id, json[QString("videoId")]);
    m_video_id_isSet = !json[QString("videoId")].isNull() && m_video_id_isValid;

    m_views_isValid = ::OpenAPI::fromJsonValue(m_views, json[QString("views")]);
    m_views_isSet = !json[QString("views")].isNull() && m_views_isValid;
}

QString OAIVideoBlacklist::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoBlacklist::asJsonObject() const {
    QJsonObject obj;
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
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
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
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_uuid_isSet) {
        obj.insert(QString("uuid"), ::OpenAPI::toJsonValue(m_uuid));
    }
    if (m_video_id_isSet) {
        obj.insert(QString("videoId"), ::OpenAPI::toJsonValue(m_video_id));
    }
    if (m_views_isSet) {
        obj.insert(QString("views"), ::OpenAPI::toJsonValue(m_views));
    }
    return obj;
}

QDateTime OAIVideoBlacklist::getCreatedAt() const {
    return m_created_at;
}
void OAIVideoBlacklist::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideoBlacklist::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideoBlacklist::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIVideoBlacklist::getDescription() const {
    return m_description;
}
void OAIVideoBlacklist::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideoBlacklist::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideoBlacklist::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIVideoBlacklist::getDislikes() const {
    return m_dislikes;
}
void OAIVideoBlacklist::setDislikes(const qint32 &dislikes) {
    m_dislikes = dislikes;
    m_dislikes_isSet = true;
}

bool OAIVideoBlacklist::is_dislikes_Set() const{
    return m_dislikes_isSet;
}

bool OAIVideoBlacklist::is_dislikes_Valid() const{
    return m_dislikes_isValid;
}

qint32 OAIVideoBlacklist::getDuration() const {
    return m_duration;
}
void OAIVideoBlacklist::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIVideoBlacklist::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIVideoBlacklist::is_duration_Valid() const{
    return m_duration_isValid;
}

qint32 OAIVideoBlacklist::getId() const {
    return m_id;
}
void OAIVideoBlacklist::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoBlacklist::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoBlacklist::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIVideoBlacklist::getLikes() const {
    return m_likes;
}
void OAIVideoBlacklist::setLikes(const qint32 &likes) {
    m_likes = likes;
    m_likes_isSet = true;
}

bool OAIVideoBlacklist::is_likes_Set() const{
    return m_likes_isSet;
}

bool OAIVideoBlacklist::is_likes_Valid() const{
    return m_likes_isValid;
}

QString OAIVideoBlacklist::getName() const {
    return m_name;
}
void OAIVideoBlacklist::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVideoBlacklist::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVideoBlacklist::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIVideoBlacklist::isNsfw() const {
    return m_nsfw;
}
void OAIVideoBlacklist::setNsfw(const bool &nsfw) {
    m_nsfw = nsfw;
    m_nsfw_isSet = true;
}

bool OAIVideoBlacklist::is_nsfw_Set() const{
    return m_nsfw_isSet;
}

bool OAIVideoBlacklist::is_nsfw_Valid() const{
    return m_nsfw_isValid;
}

QDateTime OAIVideoBlacklist::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVideoBlacklist::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVideoBlacklist::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVideoBlacklist::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIVideoBlacklist::getUuid() const {
    return m_uuid;
}
void OAIVideoBlacklist::setUuid(const QString &uuid) {
    m_uuid = uuid;
    m_uuid_isSet = true;
}

bool OAIVideoBlacklist::is_uuid_Set() const{
    return m_uuid_isSet;
}

bool OAIVideoBlacklist::is_uuid_Valid() const{
    return m_uuid_isValid;
}

qint32 OAIVideoBlacklist::getVideoId() const {
    return m_video_id;
}
void OAIVideoBlacklist::setVideoId(const qint32 &video_id) {
    m_video_id = video_id;
    m_video_id_isSet = true;
}

bool OAIVideoBlacklist::is_video_id_Set() const{
    return m_video_id_isSet;
}

bool OAIVideoBlacklist::is_video_id_Valid() const{
    return m_video_id_isValid;
}

qint32 OAIVideoBlacklist::getViews() const {
    return m_views;
}
void OAIVideoBlacklist::setViews(const qint32 &views) {
    m_views = views;
    m_views_isSet = true;
}

bool OAIVideoBlacklist::is_views_Set() const{
    return m_views_isSet;
}

bool OAIVideoBlacklist::is_views_Valid() const{
    return m_views_isValid;
}

bool OAIVideoBlacklist::isSet() const {
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

        if (m_dislikes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_views_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoBlacklist::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
