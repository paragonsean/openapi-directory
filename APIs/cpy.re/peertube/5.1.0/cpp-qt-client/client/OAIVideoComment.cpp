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

#include "OAIVideoComment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoComment::OAIVideoComment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoComment::OAIVideoComment() {
    this->initializeModel();
}

OAIVideoComment::~OAIVideoComment() {}

void OAIVideoComment::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_deleted_at_isSet = false;
    m_deleted_at_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_in_reply_to_comment_id_isSet = false;
    m_in_reply_to_comment_id_isValid = false;

    m_is_deleted_isSet = false;
    m_is_deleted_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_thread_id_isSet = false;
    m_thread_id_isValid = false;

    m_total_replies_isSet = false;
    m_total_replies_isValid = false;

    m_total_replies_from_video_author_isSet = false;
    m_total_replies_from_video_author_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_video_id_isSet = false;
    m_video_id_isValid = false;
}

void OAIVideoComment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoComment::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_deleted_at_isValid = ::OpenAPI::fromJsonValue(m_deleted_at, json[QString("deletedAt")]);
    m_deleted_at_isSet = !json[QString("deletedAt")].isNull() && m_deleted_at_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_in_reply_to_comment_id_isValid = ::OpenAPI::fromJsonValue(m_in_reply_to_comment_id, json[QString("inReplyToCommentId")]);
    m_in_reply_to_comment_id_isSet = !json[QString("inReplyToCommentId")].isNull() && m_in_reply_to_comment_id_isValid;

    m_is_deleted_isValid = ::OpenAPI::fromJsonValue(m_is_deleted, json[QString("isDeleted")]);
    m_is_deleted_isSet = !json[QString("isDeleted")].isNull() && m_is_deleted_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_thread_id_isValid = ::OpenAPI::fromJsonValue(m_thread_id, json[QString("threadId")]);
    m_thread_id_isSet = !json[QString("threadId")].isNull() && m_thread_id_isValid;

    m_total_replies_isValid = ::OpenAPI::fromJsonValue(m_total_replies, json[QString("totalReplies")]);
    m_total_replies_isSet = !json[QString("totalReplies")].isNull() && m_total_replies_isValid;

    m_total_replies_from_video_author_isValid = ::OpenAPI::fromJsonValue(m_total_replies_from_video_author, json[QString("totalRepliesFromVideoAuthor")]);
    m_total_replies_from_video_author_isSet = !json[QString("totalRepliesFromVideoAuthor")].isNull() && m_total_replies_from_video_author_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_video_id_isValid = ::OpenAPI::fromJsonValue(m_video_id, json[QString("videoId")]);
    m_video_id_isSet = !json[QString("videoId")].isNull() && m_video_id_isValid;
}

QString OAIVideoComment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoComment::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_deleted_at_isSet) {
        obj.insert(QString("deletedAt"), ::OpenAPI::toJsonValue(m_deleted_at));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_in_reply_to_comment_id_isSet) {
        obj.insert(QString("inReplyToCommentId"), ::OpenAPI::toJsonValue(m_in_reply_to_comment_id));
    }
    if (m_is_deleted_isSet) {
        obj.insert(QString("isDeleted"), ::OpenAPI::toJsonValue(m_is_deleted));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_thread_id_isSet) {
        obj.insert(QString("threadId"), ::OpenAPI::toJsonValue(m_thread_id));
    }
    if (m_total_replies_isSet) {
        obj.insert(QString("totalReplies"), ::OpenAPI::toJsonValue(m_total_replies));
    }
    if (m_total_replies_from_video_author_isSet) {
        obj.insert(QString("totalRepliesFromVideoAuthor"), ::OpenAPI::toJsonValue(m_total_replies_from_video_author));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_video_id_isSet) {
        obj.insert(QString("videoId"), ::OpenAPI::toJsonValue(m_video_id));
    }
    return obj;
}

OAIAccount OAIVideoComment::getAccount() const {
    return m_account;
}
void OAIVideoComment::setAccount(const OAIAccount &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAIVideoComment::is_account_Set() const{
    return m_account_isSet;
}

bool OAIVideoComment::is_account_Valid() const{
    return m_account_isValid;
}

QDateTime OAIVideoComment::getCreatedAt() const {
    return m_created_at;
}
void OAIVideoComment::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideoComment::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideoComment::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QDateTime OAIVideoComment::getDeletedAt() const {
    return m_deleted_at;
}
void OAIVideoComment::setDeletedAt(const QDateTime &deleted_at) {
    m_deleted_at = deleted_at;
    m_deleted_at_isSet = true;
}

bool OAIVideoComment::is_deleted_at_Set() const{
    return m_deleted_at_isSet;
}

bool OAIVideoComment::is_deleted_at_Valid() const{
    return m_deleted_at_isValid;
}

qint32 OAIVideoComment::getId() const {
    return m_id;
}
void OAIVideoComment::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoComment::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoComment::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIVideoComment::getInReplyToCommentId() const {
    return m_in_reply_to_comment_id;
}
void OAIVideoComment::setInReplyToCommentId(const qint32 &in_reply_to_comment_id) {
    m_in_reply_to_comment_id = in_reply_to_comment_id;
    m_in_reply_to_comment_id_isSet = true;
}

bool OAIVideoComment::is_in_reply_to_comment_id_Set() const{
    return m_in_reply_to_comment_id_isSet;
}

bool OAIVideoComment::is_in_reply_to_comment_id_Valid() const{
    return m_in_reply_to_comment_id_isValid;
}

bool OAIVideoComment::isIsDeleted() const {
    return m_is_deleted;
}
void OAIVideoComment::setIsDeleted(const bool &is_deleted) {
    m_is_deleted = is_deleted;
    m_is_deleted_isSet = true;
}

bool OAIVideoComment::is_is_deleted_Set() const{
    return m_is_deleted_isSet;
}

bool OAIVideoComment::is_is_deleted_Valid() const{
    return m_is_deleted_isValid;
}

QString OAIVideoComment::getText() const {
    return m_text;
}
void OAIVideoComment::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIVideoComment::is_text_Set() const{
    return m_text_isSet;
}

bool OAIVideoComment::is_text_Valid() const{
    return m_text_isValid;
}

qint32 OAIVideoComment::getThreadId() const {
    return m_thread_id;
}
void OAIVideoComment::setThreadId(const qint32 &thread_id) {
    m_thread_id = thread_id;
    m_thread_id_isSet = true;
}

bool OAIVideoComment::is_thread_id_Set() const{
    return m_thread_id_isSet;
}

bool OAIVideoComment::is_thread_id_Valid() const{
    return m_thread_id_isValid;
}

qint32 OAIVideoComment::getTotalReplies() const {
    return m_total_replies;
}
void OAIVideoComment::setTotalReplies(const qint32 &total_replies) {
    m_total_replies = total_replies;
    m_total_replies_isSet = true;
}

bool OAIVideoComment::is_total_replies_Set() const{
    return m_total_replies_isSet;
}

bool OAIVideoComment::is_total_replies_Valid() const{
    return m_total_replies_isValid;
}

qint32 OAIVideoComment::getTotalRepliesFromVideoAuthor() const {
    return m_total_replies_from_video_author;
}
void OAIVideoComment::setTotalRepliesFromVideoAuthor(const qint32 &total_replies_from_video_author) {
    m_total_replies_from_video_author = total_replies_from_video_author;
    m_total_replies_from_video_author_isSet = true;
}

bool OAIVideoComment::is_total_replies_from_video_author_Set() const{
    return m_total_replies_from_video_author_isSet;
}

bool OAIVideoComment::is_total_replies_from_video_author_Valid() const{
    return m_total_replies_from_video_author_isValid;
}

QDateTime OAIVideoComment::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVideoComment::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVideoComment::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVideoComment::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIVideoComment::getUrl() const {
    return m_url;
}
void OAIVideoComment::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIVideoComment::is_url_Set() const{
    return m_url_isSet;
}

bool OAIVideoComment::is_url_Valid() const{
    return m_url_isValid;
}

qint32 OAIVideoComment::getVideoId() const {
    return m_video_id;
}
void OAIVideoComment::setVideoId(const qint32 &video_id) {
    m_video_id = video_id;
    m_video_id_isSet = true;
}

bool OAIVideoComment::is_video_id_Set() const{
    return m_video_id_isSet;
}

bool OAIVideoComment::is_video_id_Valid() const{
    return m_video_id_isValid;
}

bool OAIVideoComment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_in_reply_to_comment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thread_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_replies_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_replies_from_video_author_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoComment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
