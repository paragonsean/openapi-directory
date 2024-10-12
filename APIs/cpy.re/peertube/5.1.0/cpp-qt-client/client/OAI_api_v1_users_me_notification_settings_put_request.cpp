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

#include "OAI_api_v1_users_me_notification_settings_put_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_v1_users_me_notification_settings_put_request::OAI_api_v1_users_me_notification_settings_put_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_v1_users_me_notification_settings_put_request::OAI_api_v1_users_me_notification_settings_put_request() {
    this->initializeModel();
}

OAI_api_v1_users_me_notification_settings_put_request::~OAI_api_v1_users_me_notification_settings_put_request() {}

void OAI_api_v1_users_me_notification_settings_put_request::initializeModel() {

    m_abuse_as_moderator_isSet = false;
    m_abuse_as_moderator_isValid = false;

    m_auto_instance_following_isSet = false;
    m_auto_instance_following_isValid = false;

    m_blacklist_on_my_video_isSet = false;
    m_blacklist_on_my_video_isValid = false;

    m_comment_mention_isSet = false;
    m_comment_mention_isValid = false;

    m_my_video_import_finished_isSet = false;
    m_my_video_import_finished_isValid = false;

    m_my_video_published_isSet = false;
    m_my_video_published_isValid = false;

    m_new_comment_on_my_video_isSet = false;
    m_new_comment_on_my_video_isValid = false;

    m_new_follow_isSet = false;
    m_new_follow_isValid = false;

    m_new_instance_follower_isSet = false;
    m_new_instance_follower_isValid = false;

    m_new_user_registration_isSet = false;
    m_new_user_registration_isValid = false;

    m_new_video_from_subscription_isSet = false;
    m_new_video_from_subscription_isValid = false;

    m_video_auto_blacklist_as_moderator_isSet = false;
    m_video_auto_blacklist_as_moderator_isValid = false;
}

void OAI_api_v1_users_me_notification_settings_put_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_v1_users_me_notification_settings_put_request::fromJsonObject(QJsonObject json) {

    m_abuse_as_moderator_isValid = ::OpenAPI::fromJsonValue(m_abuse_as_moderator, json[QString("abuseAsModerator")]);
    m_abuse_as_moderator_isSet = !json[QString("abuseAsModerator")].isNull() && m_abuse_as_moderator_isValid;

    m_auto_instance_following_isValid = ::OpenAPI::fromJsonValue(m_auto_instance_following, json[QString("autoInstanceFollowing")]);
    m_auto_instance_following_isSet = !json[QString("autoInstanceFollowing")].isNull() && m_auto_instance_following_isValid;

    m_blacklist_on_my_video_isValid = ::OpenAPI::fromJsonValue(m_blacklist_on_my_video, json[QString("blacklistOnMyVideo")]);
    m_blacklist_on_my_video_isSet = !json[QString("blacklistOnMyVideo")].isNull() && m_blacklist_on_my_video_isValid;

    m_comment_mention_isValid = ::OpenAPI::fromJsonValue(m_comment_mention, json[QString("commentMention")]);
    m_comment_mention_isSet = !json[QString("commentMention")].isNull() && m_comment_mention_isValid;

    m_my_video_import_finished_isValid = ::OpenAPI::fromJsonValue(m_my_video_import_finished, json[QString("myVideoImportFinished")]);
    m_my_video_import_finished_isSet = !json[QString("myVideoImportFinished")].isNull() && m_my_video_import_finished_isValid;

    m_my_video_published_isValid = ::OpenAPI::fromJsonValue(m_my_video_published, json[QString("myVideoPublished")]);
    m_my_video_published_isSet = !json[QString("myVideoPublished")].isNull() && m_my_video_published_isValid;

    m_new_comment_on_my_video_isValid = ::OpenAPI::fromJsonValue(m_new_comment_on_my_video, json[QString("newCommentOnMyVideo")]);
    m_new_comment_on_my_video_isSet = !json[QString("newCommentOnMyVideo")].isNull() && m_new_comment_on_my_video_isValid;

    m_new_follow_isValid = ::OpenAPI::fromJsonValue(m_new_follow, json[QString("newFollow")]);
    m_new_follow_isSet = !json[QString("newFollow")].isNull() && m_new_follow_isValid;

    m_new_instance_follower_isValid = ::OpenAPI::fromJsonValue(m_new_instance_follower, json[QString("newInstanceFollower")]);
    m_new_instance_follower_isSet = !json[QString("newInstanceFollower")].isNull() && m_new_instance_follower_isValid;

    m_new_user_registration_isValid = ::OpenAPI::fromJsonValue(m_new_user_registration, json[QString("newUserRegistration")]);
    m_new_user_registration_isSet = !json[QString("newUserRegistration")].isNull() && m_new_user_registration_isValid;

    m_new_video_from_subscription_isValid = ::OpenAPI::fromJsonValue(m_new_video_from_subscription, json[QString("newVideoFromSubscription")]);
    m_new_video_from_subscription_isSet = !json[QString("newVideoFromSubscription")].isNull() && m_new_video_from_subscription_isValid;

    m_video_auto_blacklist_as_moderator_isValid = ::OpenAPI::fromJsonValue(m_video_auto_blacklist_as_moderator, json[QString("videoAutoBlacklistAsModerator")]);
    m_video_auto_blacklist_as_moderator_isSet = !json[QString("videoAutoBlacklistAsModerator")].isNull() && m_video_auto_blacklist_as_moderator_isValid;
}

QString OAI_api_v1_users_me_notification_settings_put_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_v1_users_me_notification_settings_put_request::asJsonObject() const {
    QJsonObject obj;
    if (m_abuse_as_moderator_isSet) {
        obj.insert(QString("abuseAsModerator"), ::OpenAPI::toJsonValue(m_abuse_as_moderator));
    }
    if (m_auto_instance_following_isSet) {
        obj.insert(QString("autoInstanceFollowing"), ::OpenAPI::toJsonValue(m_auto_instance_following));
    }
    if (m_blacklist_on_my_video_isSet) {
        obj.insert(QString("blacklistOnMyVideo"), ::OpenAPI::toJsonValue(m_blacklist_on_my_video));
    }
    if (m_comment_mention_isSet) {
        obj.insert(QString("commentMention"), ::OpenAPI::toJsonValue(m_comment_mention));
    }
    if (m_my_video_import_finished_isSet) {
        obj.insert(QString("myVideoImportFinished"), ::OpenAPI::toJsonValue(m_my_video_import_finished));
    }
    if (m_my_video_published_isSet) {
        obj.insert(QString("myVideoPublished"), ::OpenAPI::toJsonValue(m_my_video_published));
    }
    if (m_new_comment_on_my_video_isSet) {
        obj.insert(QString("newCommentOnMyVideo"), ::OpenAPI::toJsonValue(m_new_comment_on_my_video));
    }
    if (m_new_follow_isSet) {
        obj.insert(QString("newFollow"), ::OpenAPI::toJsonValue(m_new_follow));
    }
    if (m_new_instance_follower_isSet) {
        obj.insert(QString("newInstanceFollower"), ::OpenAPI::toJsonValue(m_new_instance_follower));
    }
    if (m_new_user_registration_isSet) {
        obj.insert(QString("newUserRegistration"), ::OpenAPI::toJsonValue(m_new_user_registration));
    }
    if (m_new_video_from_subscription_isSet) {
        obj.insert(QString("newVideoFromSubscription"), ::OpenAPI::toJsonValue(m_new_video_from_subscription));
    }
    if (m_video_auto_blacklist_as_moderator_isSet) {
        obj.insert(QString("videoAutoBlacklistAsModerator"), ::OpenAPI::toJsonValue(m_video_auto_blacklist_as_moderator));
    }
    return obj;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getAbuseAsModerator() const {
    return m_abuse_as_moderator;
}
void OAI_api_v1_users_me_notification_settings_put_request::setAbuseAsModerator(const qint32 &abuse_as_moderator) {
    m_abuse_as_moderator = abuse_as_moderator;
    m_abuse_as_moderator_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_abuse_as_moderator_Set() const{
    return m_abuse_as_moderator_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_abuse_as_moderator_Valid() const{
    return m_abuse_as_moderator_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getAutoInstanceFollowing() const {
    return m_auto_instance_following;
}
void OAI_api_v1_users_me_notification_settings_put_request::setAutoInstanceFollowing(const qint32 &auto_instance_following) {
    m_auto_instance_following = auto_instance_following;
    m_auto_instance_following_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_auto_instance_following_Set() const{
    return m_auto_instance_following_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_auto_instance_following_Valid() const{
    return m_auto_instance_following_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getBlacklistOnMyVideo() const {
    return m_blacklist_on_my_video;
}
void OAI_api_v1_users_me_notification_settings_put_request::setBlacklistOnMyVideo(const qint32 &blacklist_on_my_video) {
    m_blacklist_on_my_video = blacklist_on_my_video;
    m_blacklist_on_my_video_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_blacklist_on_my_video_Set() const{
    return m_blacklist_on_my_video_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_blacklist_on_my_video_Valid() const{
    return m_blacklist_on_my_video_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getCommentMention() const {
    return m_comment_mention;
}
void OAI_api_v1_users_me_notification_settings_put_request::setCommentMention(const qint32 &comment_mention) {
    m_comment_mention = comment_mention;
    m_comment_mention_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_comment_mention_Set() const{
    return m_comment_mention_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_comment_mention_Valid() const{
    return m_comment_mention_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getMyVideoImportFinished() const {
    return m_my_video_import_finished;
}
void OAI_api_v1_users_me_notification_settings_put_request::setMyVideoImportFinished(const qint32 &my_video_import_finished) {
    m_my_video_import_finished = my_video_import_finished;
    m_my_video_import_finished_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_my_video_import_finished_Set() const{
    return m_my_video_import_finished_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_my_video_import_finished_Valid() const{
    return m_my_video_import_finished_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getMyVideoPublished() const {
    return m_my_video_published;
}
void OAI_api_v1_users_me_notification_settings_put_request::setMyVideoPublished(const qint32 &my_video_published) {
    m_my_video_published = my_video_published;
    m_my_video_published_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_my_video_published_Set() const{
    return m_my_video_published_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_my_video_published_Valid() const{
    return m_my_video_published_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getNewCommentOnMyVideo() const {
    return m_new_comment_on_my_video;
}
void OAI_api_v1_users_me_notification_settings_put_request::setNewCommentOnMyVideo(const qint32 &new_comment_on_my_video) {
    m_new_comment_on_my_video = new_comment_on_my_video;
    m_new_comment_on_my_video_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_comment_on_my_video_Set() const{
    return m_new_comment_on_my_video_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_comment_on_my_video_Valid() const{
    return m_new_comment_on_my_video_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getNewFollow() const {
    return m_new_follow;
}
void OAI_api_v1_users_me_notification_settings_put_request::setNewFollow(const qint32 &new_follow) {
    m_new_follow = new_follow;
    m_new_follow_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_follow_Set() const{
    return m_new_follow_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_follow_Valid() const{
    return m_new_follow_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getNewInstanceFollower() const {
    return m_new_instance_follower;
}
void OAI_api_v1_users_me_notification_settings_put_request::setNewInstanceFollower(const qint32 &new_instance_follower) {
    m_new_instance_follower = new_instance_follower;
    m_new_instance_follower_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_instance_follower_Set() const{
    return m_new_instance_follower_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_instance_follower_Valid() const{
    return m_new_instance_follower_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getNewUserRegistration() const {
    return m_new_user_registration;
}
void OAI_api_v1_users_me_notification_settings_put_request::setNewUserRegistration(const qint32 &new_user_registration) {
    m_new_user_registration = new_user_registration;
    m_new_user_registration_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_user_registration_Set() const{
    return m_new_user_registration_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_user_registration_Valid() const{
    return m_new_user_registration_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getNewVideoFromSubscription() const {
    return m_new_video_from_subscription;
}
void OAI_api_v1_users_me_notification_settings_put_request::setNewVideoFromSubscription(const qint32 &new_video_from_subscription) {
    m_new_video_from_subscription = new_video_from_subscription;
    m_new_video_from_subscription_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_video_from_subscription_Set() const{
    return m_new_video_from_subscription_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_new_video_from_subscription_Valid() const{
    return m_new_video_from_subscription_isValid;
}

qint32 OAI_api_v1_users_me_notification_settings_put_request::getVideoAutoBlacklistAsModerator() const {
    return m_video_auto_blacklist_as_moderator;
}
void OAI_api_v1_users_me_notification_settings_put_request::setVideoAutoBlacklistAsModerator(const qint32 &video_auto_blacklist_as_moderator) {
    m_video_auto_blacklist_as_moderator = video_auto_blacklist_as_moderator;
    m_video_auto_blacklist_as_moderator_isSet = true;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_video_auto_blacklist_as_moderator_Set() const{
    return m_video_auto_blacklist_as_moderator_isSet;
}

bool OAI_api_v1_users_me_notification_settings_put_request::is_video_auto_blacklist_as_moderator_Valid() const{
    return m_video_auto_blacklist_as_moderator_isValid;
}

bool OAI_api_v1_users_me_notification_settings_put_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_abuse_as_moderator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_instance_following_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blacklist_on_my_video_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment_mention_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_my_video_import_finished_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_my_video_published_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_comment_on_my_video_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_follow_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_instance_follower_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_user_registration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_video_from_subscription_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_auto_blacklist_as_moderator_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_v1_users_me_notification_settings_put_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
