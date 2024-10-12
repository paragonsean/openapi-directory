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

#include "OAINotification.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotification::OAINotification(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotification::OAINotification() {
    this->initializeModel();
}

OAINotification::~OAINotification() {}

void OAINotification::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_actor_follow_isSet = false;
    m_actor_follow_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_read_isSet = false;
    m_read_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_video_isSet = false;
    m_video_isValid = false;

    m_video_abuse_isSet = false;
    m_video_abuse_isValid = false;

    m_video_blacklist_isSet = false;
    m_video_blacklist_isValid = false;

    m_video_import_isSet = false;
    m_video_import_isValid = false;
}

void OAINotification::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotification::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_actor_follow_isValid = ::OpenAPI::fromJsonValue(m_actor_follow, json[QString("actorFollow")]);
    m_actor_follow_isSet = !json[QString("actorFollow")].isNull() && m_actor_follow_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_read_isValid = ::OpenAPI::fromJsonValue(m_read, json[QString("read")]);
    m_read_isSet = !json[QString("read")].isNull() && m_read_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_video_isValid = ::OpenAPI::fromJsonValue(m_video, json[QString("video")]);
    m_video_isSet = !json[QString("video")].isNull() && m_video_isValid;

    m_video_abuse_isValid = ::OpenAPI::fromJsonValue(m_video_abuse, json[QString("videoAbuse")]);
    m_video_abuse_isSet = !json[QString("videoAbuse")].isNull() && m_video_abuse_isValid;

    m_video_blacklist_isValid = ::OpenAPI::fromJsonValue(m_video_blacklist, json[QString("videoBlacklist")]);
    m_video_blacklist_isSet = !json[QString("videoBlacklist")].isNull() && m_video_blacklist_isValid;

    m_video_import_isValid = ::OpenAPI::fromJsonValue(m_video_import, json[QString("videoImport")]);
    m_video_import_isSet = !json[QString("videoImport")].isNull() && m_video_import_isValid;
}

QString OAINotification::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotification::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_actor_follow.isSet()) {
        obj.insert(QString("actorFollow"), ::OpenAPI::toJsonValue(m_actor_follow));
    }
    if (m_comment.isSet()) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_read_isSet) {
        obj.insert(QString("read"), ::OpenAPI::toJsonValue(m_read));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_video.isSet()) {
        obj.insert(QString("video"), ::OpenAPI::toJsonValue(m_video));
    }
    if (m_video_abuse.isSet()) {
        obj.insert(QString("videoAbuse"), ::OpenAPI::toJsonValue(m_video_abuse));
    }
    if (m_video_blacklist.isSet()) {
        obj.insert(QString("videoBlacklist"), ::OpenAPI::toJsonValue(m_video_blacklist));
    }
    if (m_video_import.isSet()) {
        obj.insert(QString("videoImport"), ::OpenAPI::toJsonValue(m_video_import));
    }
    return obj;
}

OAIActorInfo OAINotification::getAccount() const {
    return m_account;
}
void OAINotification::setAccount(const OAIActorInfo &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAINotification::is_account_Set() const{
    return m_account_isSet;
}

bool OAINotification::is_account_Valid() const{
    return m_account_isValid;
}

OAINotification_actorFollow OAINotification::getActorFollow() const {
    return m_actor_follow;
}
void OAINotification::setActorFollow(const OAINotification_actorFollow &actor_follow) {
    m_actor_follow = actor_follow;
    m_actor_follow_isSet = true;
}

bool OAINotification::is_actor_follow_Set() const{
    return m_actor_follow_isSet;
}

bool OAINotification::is_actor_follow_Valid() const{
    return m_actor_follow_isValid;
}

OAINotification_comment OAINotification::getComment() const {
    return m_comment;
}
void OAINotification::setComment(const OAINotification_comment &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAINotification::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAINotification::is_comment_Valid() const{
    return m_comment_isValid;
}

QDateTime OAINotification::getCreatedAt() const {
    return m_created_at;
}
void OAINotification::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAINotification::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAINotification::is_created_at_Valid() const{
    return m_created_at_isValid;
}

qint32 OAINotification::getId() const {
    return m_id;
}
void OAINotification::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAINotification::is_id_Set() const{
    return m_id_isSet;
}

bool OAINotification::is_id_Valid() const{
    return m_id_isValid;
}

bool OAINotification::isRead() const {
    return m_read;
}
void OAINotification::setRead(const bool &read) {
    m_read = read;
    m_read_isSet = true;
}

bool OAINotification::is_read_Set() const{
    return m_read_isSet;
}

bool OAINotification::is_read_Valid() const{
    return m_read_isValid;
}

qint32 OAINotification::getType() const {
    return m_type;
}
void OAINotification::setType(const qint32 &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAINotification::is_type_Set() const{
    return m_type_isSet;
}

bool OAINotification::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAINotification::getUpdatedAt() const {
    return m_updated_at;
}
void OAINotification::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAINotification::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAINotification::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAINotification_video OAINotification::getVideo() const {
    return m_video;
}
void OAINotification::setVideo(const OAINotification_video &video) {
    m_video = video;
    m_video_isSet = true;
}

bool OAINotification::is_video_Set() const{
    return m_video_isSet;
}

bool OAINotification::is_video_Valid() const{
    return m_video_isValid;
}

OAINotification_videoAbuse OAINotification::getVideoAbuse() const {
    return m_video_abuse;
}
void OAINotification::setVideoAbuse(const OAINotification_videoAbuse &video_abuse) {
    m_video_abuse = video_abuse;
    m_video_abuse_isSet = true;
}

bool OAINotification::is_video_abuse_Set() const{
    return m_video_abuse_isSet;
}

bool OAINotification::is_video_abuse_Valid() const{
    return m_video_abuse_isValid;
}

OAINotification_videoAbuse OAINotification::getVideoBlacklist() const {
    return m_video_blacklist;
}
void OAINotification::setVideoBlacklist(const OAINotification_videoAbuse &video_blacklist) {
    m_video_blacklist = video_blacklist;
    m_video_blacklist_isSet = true;
}

bool OAINotification::is_video_blacklist_Set() const{
    return m_video_blacklist_isSet;
}

bool OAINotification::is_video_blacklist_Valid() const{
    return m_video_blacklist_isValid;
}

OAINotification_videoImport OAINotification::getVideoImport() const {
    return m_video_import;
}
void OAINotification::setVideoImport(const OAINotification_videoImport &video_import) {
    m_video_import = video_import;
    m_video_import_isSet = true;
}

bool OAINotification::is_video_import_Set() const{
    return m_video_import_isSet;
}

bool OAINotification::is_video_import_Valid() const{
    return m_video_import_isValid;
}

bool OAINotification::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_actor_follow.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_abuse.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_blacklist.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_import.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotification::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
