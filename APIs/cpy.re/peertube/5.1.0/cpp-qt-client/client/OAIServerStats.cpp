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

#include "OAIServerStats.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerStats::OAIServerStats(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerStats::OAIServerStats() {
    this->initializeModel();
}

OAIServerStats::~OAIServerStats() {}

void OAIServerStats::initializeModel() {

    m_activity_pub_messages_processed_per_second_isSet = false;
    m_activity_pub_messages_processed_per_second_isValid = false;

    m_total_activity_pub_messages_errors_isSet = false;
    m_total_activity_pub_messages_errors_isValid = false;

    m_total_activity_pub_messages_processed_isSet = false;
    m_total_activity_pub_messages_processed_isValid = false;

    m_total_activity_pub_messages_successes_isSet = false;
    m_total_activity_pub_messages_successes_isValid = false;

    m_total_activity_pub_messages_waiting_isSet = false;
    m_total_activity_pub_messages_waiting_isValid = false;

    m_total_daily_active_users_isSet = false;
    m_total_daily_active_users_isValid = false;

    m_total_instance_followers_isSet = false;
    m_total_instance_followers_isValid = false;

    m_total_instance_following_isSet = false;
    m_total_instance_following_isValid = false;

    m_total_local_daily_active_video_channels_isSet = false;
    m_total_local_daily_active_video_channels_isValid = false;

    m_total_local_monthly_active_video_channels_isSet = false;
    m_total_local_monthly_active_video_channels_isValid = false;

    m_total_local_playlists_isSet = false;
    m_total_local_playlists_isValid = false;

    m_total_local_video_channels_isSet = false;
    m_total_local_video_channels_isValid = false;

    m_total_local_video_comments_isSet = false;
    m_total_local_video_comments_isValid = false;

    m_total_local_video_files_size_isSet = false;
    m_total_local_video_files_size_isValid = false;

    m_total_local_video_views_isSet = false;
    m_total_local_video_views_isValid = false;

    m_total_local_videos_isSet = false;
    m_total_local_videos_isValid = false;

    m_total_local_weekly_active_video_channels_isSet = false;
    m_total_local_weekly_active_video_channels_isValid = false;

    m_total_monthly_active_users_isSet = false;
    m_total_monthly_active_users_isValid = false;

    m_total_users_isSet = false;
    m_total_users_isValid = false;

    m_total_video_comments_isSet = false;
    m_total_video_comments_isValid = false;

    m_total_videos_isSet = false;
    m_total_videos_isValid = false;

    m_total_weekly_active_users_isSet = false;
    m_total_weekly_active_users_isValid = false;

    m_videos_redundancy_isSet = false;
    m_videos_redundancy_isValid = false;
}

void OAIServerStats::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerStats::fromJsonObject(QJsonObject json) {

    m_activity_pub_messages_processed_per_second_isValid = ::OpenAPI::fromJsonValue(m_activity_pub_messages_processed_per_second, json[QString("activityPubMessagesProcessedPerSecond")]);
    m_activity_pub_messages_processed_per_second_isSet = !json[QString("activityPubMessagesProcessedPerSecond")].isNull() && m_activity_pub_messages_processed_per_second_isValid;

    m_total_activity_pub_messages_errors_isValid = ::OpenAPI::fromJsonValue(m_total_activity_pub_messages_errors, json[QString("totalActivityPubMessagesErrors")]);
    m_total_activity_pub_messages_errors_isSet = !json[QString("totalActivityPubMessagesErrors")].isNull() && m_total_activity_pub_messages_errors_isValid;

    m_total_activity_pub_messages_processed_isValid = ::OpenAPI::fromJsonValue(m_total_activity_pub_messages_processed, json[QString("totalActivityPubMessagesProcessed")]);
    m_total_activity_pub_messages_processed_isSet = !json[QString("totalActivityPubMessagesProcessed")].isNull() && m_total_activity_pub_messages_processed_isValid;

    m_total_activity_pub_messages_successes_isValid = ::OpenAPI::fromJsonValue(m_total_activity_pub_messages_successes, json[QString("totalActivityPubMessagesSuccesses")]);
    m_total_activity_pub_messages_successes_isSet = !json[QString("totalActivityPubMessagesSuccesses")].isNull() && m_total_activity_pub_messages_successes_isValid;

    m_total_activity_pub_messages_waiting_isValid = ::OpenAPI::fromJsonValue(m_total_activity_pub_messages_waiting, json[QString("totalActivityPubMessagesWaiting")]);
    m_total_activity_pub_messages_waiting_isSet = !json[QString("totalActivityPubMessagesWaiting")].isNull() && m_total_activity_pub_messages_waiting_isValid;

    m_total_daily_active_users_isValid = ::OpenAPI::fromJsonValue(m_total_daily_active_users, json[QString("totalDailyActiveUsers")]);
    m_total_daily_active_users_isSet = !json[QString("totalDailyActiveUsers")].isNull() && m_total_daily_active_users_isValid;

    m_total_instance_followers_isValid = ::OpenAPI::fromJsonValue(m_total_instance_followers, json[QString("totalInstanceFollowers")]);
    m_total_instance_followers_isSet = !json[QString("totalInstanceFollowers")].isNull() && m_total_instance_followers_isValid;

    m_total_instance_following_isValid = ::OpenAPI::fromJsonValue(m_total_instance_following, json[QString("totalInstanceFollowing")]);
    m_total_instance_following_isSet = !json[QString("totalInstanceFollowing")].isNull() && m_total_instance_following_isValid;

    m_total_local_daily_active_video_channels_isValid = ::OpenAPI::fromJsonValue(m_total_local_daily_active_video_channels, json[QString("totalLocalDailyActiveVideoChannels")]);
    m_total_local_daily_active_video_channels_isSet = !json[QString("totalLocalDailyActiveVideoChannels")].isNull() && m_total_local_daily_active_video_channels_isValid;

    m_total_local_monthly_active_video_channels_isValid = ::OpenAPI::fromJsonValue(m_total_local_monthly_active_video_channels, json[QString("totalLocalMonthlyActiveVideoChannels")]);
    m_total_local_monthly_active_video_channels_isSet = !json[QString("totalLocalMonthlyActiveVideoChannels")].isNull() && m_total_local_monthly_active_video_channels_isValid;

    m_total_local_playlists_isValid = ::OpenAPI::fromJsonValue(m_total_local_playlists, json[QString("totalLocalPlaylists")]);
    m_total_local_playlists_isSet = !json[QString("totalLocalPlaylists")].isNull() && m_total_local_playlists_isValid;

    m_total_local_video_channels_isValid = ::OpenAPI::fromJsonValue(m_total_local_video_channels, json[QString("totalLocalVideoChannels")]);
    m_total_local_video_channels_isSet = !json[QString("totalLocalVideoChannels")].isNull() && m_total_local_video_channels_isValid;

    m_total_local_video_comments_isValid = ::OpenAPI::fromJsonValue(m_total_local_video_comments, json[QString("totalLocalVideoComments")]);
    m_total_local_video_comments_isSet = !json[QString("totalLocalVideoComments")].isNull() && m_total_local_video_comments_isValid;

    m_total_local_video_files_size_isValid = ::OpenAPI::fromJsonValue(m_total_local_video_files_size, json[QString("totalLocalVideoFilesSize")]);
    m_total_local_video_files_size_isSet = !json[QString("totalLocalVideoFilesSize")].isNull() && m_total_local_video_files_size_isValid;

    m_total_local_video_views_isValid = ::OpenAPI::fromJsonValue(m_total_local_video_views, json[QString("totalLocalVideoViews")]);
    m_total_local_video_views_isSet = !json[QString("totalLocalVideoViews")].isNull() && m_total_local_video_views_isValid;

    m_total_local_videos_isValid = ::OpenAPI::fromJsonValue(m_total_local_videos, json[QString("totalLocalVideos")]);
    m_total_local_videos_isSet = !json[QString("totalLocalVideos")].isNull() && m_total_local_videos_isValid;

    m_total_local_weekly_active_video_channels_isValid = ::OpenAPI::fromJsonValue(m_total_local_weekly_active_video_channels, json[QString("totalLocalWeeklyActiveVideoChannels")]);
    m_total_local_weekly_active_video_channels_isSet = !json[QString("totalLocalWeeklyActiveVideoChannels")].isNull() && m_total_local_weekly_active_video_channels_isValid;

    m_total_monthly_active_users_isValid = ::OpenAPI::fromJsonValue(m_total_monthly_active_users, json[QString("totalMonthlyActiveUsers")]);
    m_total_monthly_active_users_isSet = !json[QString("totalMonthlyActiveUsers")].isNull() && m_total_monthly_active_users_isValid;

    m_total_users_isValid = ::OpenAPI::fromJsonValue(m_total_users, json[QString("totalUsers")]);
    m_total_users_isSet = !json[QString("totalUsers")].isNull() && m_total_users_isValid;

    m_total_video_comments_isValid = ::OpenAPI::fromJsonValue(m_total_video_comments, json[QString("totalVideoComments")]);
    m_total_video_comments_isSet = !json[QString("totalVideoComments")].isNull() && m_total_video_comments_isValid;

    m_total_videos_isValid = ::OpenAPI::fromJsonValue(m_total_videos, json[QString("totalVideos")]);
    m_total_videos_isSet = !json[QString("totalVideos")].isNull() && m_total_videos_isValid;

    m_total_weekly_active_users_isValid = ::OpenAPI::fromJsonValue(m_total_weekly_active_users, json[QString("totalWeeklyActiveUsers")]);
    m_total_weekly_active_users_isSet = !json[QString("totalWeeklyActiveUsers")].isNull() && m_total_weekly_active_users_isValid;

    m_videos_redundancy_isValid = ::OpenAPI::fromJsonValue(m_videos_redundancy, json[QString("videosRedundancy")]);
    m_videos_redundancy_isSet = !json[QString("videosRedundancy")].isNull() && m_videos_redundancy_isValid;
}

QString OAIServerStats::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerStats::asJsonObject() const {
    QJsonObject obj;
    if (m_activity_pub_messages_processed_per_second_isSet) {
        obj.insert(QString("activityPubMessagesProcessedPerSecond"), ::OpenAPI::toJsonValue(m_activity_pub_messages_processed_per_second));
    }
    if (m_total_activity_pub_messages_errors_isSet) {
        obj.insert(QString("totalActivityPubMessagesErrors"), ::OpenAPI::toJsonValue(m_total_activity_pub_messages_errors));
    }
    if (m_total_activity_pub_messages_processed_isSet) {
        obj.insert(QString("totalActivityPubMessagesProcessed"), ::OpenAPI::toJsonValue(m_total_activity_pub_messages_processed));
    }
    if (m_total_activity_pub_messages_successes_isSet) {
        obj.insert(QString("totalActivityPubMessagesSuccesses"), ::OpenAPI::toJsonValue(m_total_activity_pub_messages_successes));
    }
    if (m_total_activity_pub_messages_waiting_isSet) {
        obj.insert(QString("totalActivityPubMessagesWaiting"), ::OpenAPI::toJsonValue(m_total_activity_pub_messages_waiting));
    }
    if (m_total_daily_active_users_isSet) {
        obj.insert(QString("totalDailyActiveUsers"), ::OpenAPI::toJsonValue(m_total_daily_active_users));
    }
    if (m_total_instance_followers_isSet) {
        obj.insert(QString("totalInstanceFollowers"), ::OpenAPI::toJsonValue(m_total_instance_followers));
    }
    if (m_total_instance_following_isSet) {
        obj.insert(QString("totalInstanceFollowing"), ::OpenAPI::toJsonValue(m_total_instance_following));
    }
    if (m_total_local_daily_active_video_channels_isSet) {
        obj.insert(QString("totalLocalDailyActiveVideoChannels"), ::OpenAPI::toJsonValue(m_total_local_daily_active_video_channels));
    }
    if (m_total_local_monthly_active_video_channels_isSet) {
        obj.insert(QString("totalLocalMonthlyActiveVideoChannels"), ::OpenAPI::toJsonValue(m_total_local_monthly_active_video_channels));
    }
    if (m_total_local_playlists_isSet) {
        obj.insert(QString("totalLocalPlaylists"), ::OpenAPI::toJsonValue(m_total_local_playlists));
    }
    if (m_total_local_video_channels_isSet) {
        obj.insert(QString("totalLocalVideoChannels"), ::OpenAPI::toJsonValue(m_total_local_video_channels));
    }
    if (m_total_local_video_comments_isSet) {
        obj.insert(QString("totalLocalVideoComments"), ::OpenAPI::toJsonValue(m_total_local_video_comments));
    }
    if (m_total_local_video_files_size_isSet) {
        obj.insert(QString("totalLocalVideoFilesSize"), ::OpenAPI::toJsonValue(m_total_local_video_files_size));
    }
    if (m_total_local_video_views_isSet) {
        obj.insert(QString("totalLocalVideoViews"), ::OpenAPI::toJsonValue(m_total_local_video_views));
    }
    if (m_total_local_videos_isSet) {
        obj.insert(QString("totalLocalVideos"), ::OpenAPI::toJsonValue(m_total_local_videos));
    }
    if (m_total_local_weekly_active_video_channels_isSet) {
        obj.insert(QString("totalLocalWeeklyActiveVideoChannels"), ::OpenAPI::toJsonValue(m_total_local_weekly_active_video_channels));
    }
    if (m_total_monthly_active_users_isSet) {
        obj.insert(QString("totalMonthlyActiveUsers"), ::OpenAPI::toJsonValue(m_total_monthly_active_users));
    }
    if (m_total_users_isSet) {
        obj.insert(QString("totalUsers"), ::OpenAPI::toJsonValue(m_total_users));
    }
    if (m_total_video_comments_isSet) {
        obj.insert(QString("totalVideoComments"), ::OpenAPI::toJsonValue(m_total_video_comments));
    }
    if (m_total_videos_isSet) {
        obj.insert(QString("totalVideos"), ::OpenAPI::toJsonValue(m_total_videos));
    }
    if (m_total_weekly_active_users_isSet) {
        obj.insert(QString("totalWeeklyActiveUsers"), ::OpenAPI::toJsonValue(m_total_weekly_active_users));
    }
    if (m_videos_redundancy.size() > 0) {
        obj.insert(QString("videosRedundancy"), ::OpenAPI::toJsonValue(m_videos_redundancy));
    }
    return obj;
}

double OAIServerStats::getActivityPubMessagesProcessedPerSecond() const {
    return m_activity_pub_messages_processed_per_second;
}
void OAIServerStats::setActivityPubMessagesProcessedPerSecond(const double &activity_pub_messages_processed_per_second) {
    m_activity_pub_messages_processed_per_second = activity_pub_messages_processed_per_second;
    m_activity_pub_messages_processed_per_second_isSet = true;
}

bool OAIServerStats::is_activity_pub_messages_processed_per_second_Set() const{
    return m_activity_pub_messages_processed_per_second_isSet;
}

bool OAIServerStats::is_activity_pub_messages_processed_per_second_Valid() const{
    return m_activity_pub_messages_processed_per_second_isValid;
}

double OAIServerStats::getTotalActivityPubMessagesErrors() const {
    return m_total_activity_pub_messages_errors;
}
void OAIServerStats::setTotalActivityPubMessagesErrors(const double &total_activity_pub_messages_errors) {
    m_total_activity_pub_messages_errors = total_activity_pub_messages_errors;
    m_total_activity_pub_messages_errors_isSet = true;
}

bool OAIServerStats::is_total_activity_pub_messages_errors_Set() const{
    return m_total_activity_pub_messages_errors_isSet;
}

bool OAIServerStats::is_total_activity_pub_messages_errors_Valid() const{
    return m_total_activity_pub_messages_errors_isValid;
}

double OAIServerStats::getTotalActivityPubMessagesProcessed() const {
    return m_total_activity_pub_messages_processed;
}
void OAIServerStats::setTotalActivityPubMessagesProcessed(const double &total_activity_pub_messages_processed) {
    m_total_activity_pub_messages_processed = total_activity_pub_messages_processed;
    m_total_activity_pub_messages_processed_isSet = true;
}

bool OAIServerStats::is_total_activity_pub_messages_processed_Set() const{
    return m_total_activity_pub_messages_processed_isSet;
}

bool OAIServerStats::is_total_activity_pub_messages_processed_Valid() const{
    return m_total_activity_pub_messages_processed_isValid;
}

double OAIServerStats::getTotalActivityPubMessagesSuccesses() const {
    return m_total_activity_pub_messages_successes;
}
void OAIServerStats::setTotalActivityPubMessagesSuccesses(const double &total_activity_pub_messages_successes) {
    m_total_activity_pub_messages_successes = total_activity_pub_messages_successes;
    m_total_activity_pub_messages_successes_isSet = true;
}

bool OAIServerStats::is_total_activity_pub_messages_successes_Set() const{
    return m_total_activity_pub_messages_successes_isSet;
}

bool OAIServerStats::is_total_activity_pub_messages_successes_Valid() const{
    return m_total_activity_pub_messages_successes_isValid;
}

double OAIServerStats::getTotalActivityPubMessagesWaiting() const {
    return m_total_activity_pub_messages_waiting;
}
void OAIServerStats::setTotalActivityPubMessagesWaiting(const double &total_activity_pub_messages_waiting) {
    m_total_activity_pub_messages_waiting = total_activity_pub_messages_waiting;
    m_total_activity_pub_messages_waiting_isSet = true;
}

bool OAIServerStats::is_total_activity_pub_messages_waiting_Set() const{
    return m_total_activity_pub_messages_waiting_isSet;
}

bool OAIServerStats::is_total_activity_pub_messages_waiting_Valid() const{
    return m_total_activity_pub_messages_waiting_isValid;
}

double OAIServerStats::getTotalDailyActiveUsers() const {
    return m_total_daily_active_users;
}
void OAIServerStats::setTotalDailyActiveUsers(const double &total_daily_active_users) {
    m_total_daily_active_users = total_daily_active_users;
    m_total_daily_active_users_isSet = true;
}

bool OAIServerStats::is_total_daily_active_users_Set() const{
    return m_total_daily_active_users_isSet;
}

bool OAIServerStats::is_total_daily_active_users_Valid() const{
    return m_total_daily_active_users_isValid;
}

double OAIServerStats::getTotalInstanceFollowers() const {
    return m_total_instance_followers;
}
void OAIServerStats::setTotalInstanceFollowers(const double &total_instance_followers) {
    m_total_instance_followers = total_instance_followers;
    m_total_instance_followers_isSet = true;
}

bool OAIServerStats::is_total_instance_followers_Set() const{
    return m_total_instance_followers_isSet;
}

bool OAIServerStats::is_total_instance_followers_Valid() const{
    return m_total_instance_followers_isValid;
}

double OAIServerStats::getTotalInstanceFollowing() const {
    return m_total_instance_following;
}
void OAIServerStats::setTotalInstanceFollowing(const double &total_instance_following) {
    m_total_instance_following = total_instance_following;
    m_total_instance_following_isSet = true;
}

bool OAIServerStats::is_total_instance_following_Set() const{
    return m_total_instance_following_isSet;
}

bool OAIServerStats::is_total_instance_following_Valid() const{
    return m_total_instance_following_isValid;
}

double OAIServerStats::getTotalLocalDailyActiveVideoChannels() const {
    return m_total_local_daily_active_video_channels;
}
void OAIServerStats::setTotalLocalDailyActiveVideoChannels(const double &total_local_daily_active_video_channels) {
    m_total_local_daily_active_video_channels = total_local_daily_active_video_channels;
    m_total_local_daily_active_video_channels_isSet = true;
}

bool OAIServerStats::is_total_local_daily_active_video_channels_Set() const{
    return m_total_local_daily_active_video_channels_isSet;
}

bool OAIServerStats::is_total_local_daily_active_video_channels_Valid() const{
    return m_total_local_daily_active_video_channels_isValid;
}

double OAIServerStats::getTotalLocalMonthlyActiveVideoChannels() const {
    return m_total_local_monthly_active_video_channels;
}
void OAIServerStats::setTotalLocalMonthlyActiveVideoChannels(const double &total_local_monthly_active_video_channels) {
    m_total_local_monthly_active_video_channels = total_local_monthly_active_video_channels;
    m_total_local_monthly_active_video_channels_isSet = true;
}

bool OAIServerStats::is_total_local_monthly_active_video_channels_Set() const{
    return m_total_local_monthly_active_video_channels_isSet;
}

bool OAIServerStats::is_total_local_monthly_active_video_channels_Valid() const{
    return m_total_local_monthly_active_video_channels_isValid;
}

double OAIServerStats::getTotalLocalPlaylists() const {
    return m_total_local_playlists;
}
void OAIServerStats::setTotalLocalPlaylists(const double &total_local_playlists) {
    m_total_local_playlists = total_local_playlists;
    m_total_local_playlists_isSet = true;
}

bool OAIServerStats::is_total_local_playlists_Set() const{
    return m_total_local_playlists_isSet;
}

bool OAIServerStats::is_total_local_playlists_Valid() const{
    return m_total_local_playlists_isValid;
}

double OAIServerStats::getTotalLocalVideoChannels() const {
    return m_total_local_video_channels;
}
void OAIServerStats::setTotalLocalVideoChannels(const double &total_local_video_channels) {
    m_total_local_video_channels = total_local_video_channels;
    m_total_local_video_channels_isSet = true;
}

bool OAIServerStats::is_total_local_video_channels_Set() const{
    return m_total_local_video_channels_isSet;
}

bool OAIServerStats::is_total_local_video_channels_Valid() const{
    return m_total_local_video_channels_isValid;
}

double OAIServerStats::getTotalLocalVideoComments() const {
    return m_total_local_video_comments;
}
void OAIServerStats::setTotalLocalVideoComments(const double &total_local_video_comments) {
    m_total_local_video_comments = total_local_video_comments;
    m_total_local_video_comments_isSet = true;
}

bool OAIServerStats::is_total_local_video_comments_Set() const{
    return m_total_local_video_comments_isSet;
}

bool OAIServerStats::is_total_local_video_comments_Valid() const{
    return m_total_local_video_comments_isValid;
}

double OAIServerStats::getTotalLocalVideoFilesSize() const {
    return m_total_local_video_files_size;
}
void OAIServerStats::setTotalLocalVideoFilesSize(const double &total_local_video_files_size) {
    m_total_local_video_files_size = total_local_video_files_size;
    m_total_local_video_files_size_isSet = true;
}

bool OAIServerStats::is_total_local_video_files_size_Set() const{
    return m_total_local_video_files_size_isSet;
}

bool OAIServerStats::is_total_local_video_files_size_Valid() const{
    return m_total_local_video_files_size_isValid;
}

double OAIServerStats::getTotalLocalVideoViews() const {
    return m_total_local_video_views;
}
void OAIServerStats::setTotalLocalVideoViews(const double &total_local_video_views) {
    m_total_local_video_views = total_local_video_views;
    m_total_local_video_views_isSet = true;
}

bool OAIServerStats::is_total_local_video_views_Set() const{
    return m_total_local_video_views_isSet;
}

bool OAIServerStats::is_total_local_video_views_Valid() const{
    return m_total_local_video_views_isValid;
}

double OAIServerStats::getTotalLocalVideos() const {
    return m_total_local_videos;
}
void OAIServerStats::setTotalLocalVideos(const double &total_local_videos) {
    m_total_local_videos = total_local_videos;
    m_total_local_videos_isSet = true;
}

bool OAIServerStats::is_total_local_videos_Set() const{
    return m_total_local_videos_isSet;
}

bool OAIServerStats::is_total_local_videos_Valid() const{
    return m_total_local_videos_isValid;
}

double OAIServerStats::getTotalLocalWeeklyActiveVideoChannels() const {
    return m_total_local_weekly_active_video_channels;
}
void OAIServerStats::setTotalLocalWeeklyActiveVideoChannels(const double &total_local_weekly_active_video_channels) {
    m_total_local_weekly_active_video_channels = total_local_weekly_active_video_channels;
    m_total_local_weekly_active_video_channels_isSet = true;
}

bool OAIServerStats::is_total_local_weekly_active_video_channels_Set() const{
    return m_total_local_weekly_active_video_channels_isSet;
}

bool OAIServerStats::is_total_local_weekly_active_video_channels_Valid() const{
    return m_total_local_weekly_active_video_channels_isValid;
}

double OAIServerStats::getTotalMonthlyActiveUsers() const {
    return m_total_monthly_active_users;
}
void OAIServerStats::setTotalMonthlyActiveUsers(const double &total_monthly_active_users) {
    m_total_monthly_active_users = total_monthly_active_users;
    m_total_monthly_active_users_isSet = true;
}

bool OAIServerStats::is_total_monthly_active_users_Set() const{
    return m_total_monthly_active_users_isSet;
}

bool OAIServerStats::is_total_monthly_active_users_Valid() const{
    return m_total_monthly_active_users_isValid;
}

double OAIServerStats::getTotalUsers() const {
    return m_total_users;
}
void OAIServerStats::setTotalUsers(const double &total_users) {
    m_total_users = total_users;
    m_total_users_isSet = true;
}

bool OAIServerStats::is_total_users_Set() const{
    return m_total_users_isSet;
}

bool OAIServerStats::is_total_users_Valid() const{
    return m_total_users_isValid;
}

double OAIServerStats::getTotalVideoComments() const {
    return m_total_video_comments;
}
void OAIServerStats::setTotalVideoComments(const double &total_video_comments) {
    m_total_video_comments = total_video_comments;
    m_total_video_comments_isSet = true;
}

bool OAIServerStats::is_total_video_comments_Set() const{
    return m_total_video_comments_isSet;
}

bool OAIServerStats::is_total_video_comments_Valid() const{
    return m_total_video_comments_isValid;
}

double OAIServerStats::getTotalVideos() const {
    return m_total_videos;
}
void OAIServerStats::setTotalVideos(const double &total_videos) {
    m_total_videos = total_videos;
    m_total_videos_isSet = true;
}

bool OAIServerStats::is_total_videos_Set() const{
    return m_total_videos_isSet;
}

bool OAIServerStats::is_total_videos_Valid() const{
    return m_total_videos_isValid;
}

double OAIServerStats::getTotalWeeklyActiveUsers() const {
    return m_total_weekly_active_users;
}
void OAIServerStats::setTotalWeeklyActiveUsers(const double &total_weekly_active_users) {
    m_total_weekly_active_users = total_weekly_active_users;
    m_total_weekly_active_users_isSet = true;
}

bool OAIServerStats::is_total_weekly_active_users_Set() const{
    return m_total_weekly_active_users_isSet;
}

bool OAIServerStats::is_total_weekly_active_users_Valid() const{
    return m_total_weekly_active_users_isValid;
}

QList<OAIServerStats_videosRedundancy_inner> OAIServerStats::getVideosRedundancy() const {
    return m_videos_redundancy;
}
void OAIServerStats::setVideosRedundancy(const QList<OAIServerStats_videosRedundancy_inner> &videos_redundancy) {
    m_videos_redundancy = videos_redundancy;
    m_videos_redundancy_isSet = true;
}

bool OAIServerStats::is_videos_redundancy_Set() const{
    return m_videos_redundancy_isSet;
}

bool OAIServerStats::is_videos_redundancy_Valid() const{
    return m_videos_redundancy_isValid;
}

bool OAIServerStats::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activity_pub_messages_processed_per_second_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_activity_pub_messages_errors_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_activity_pub_messages_processed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_activity_pub_messages_successes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_activity_pub_messages_waiting_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_daily_active_users_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_instance_followers_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_instance_following_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_daily_active_video_channels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_monthly_active_video_channels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_playlists_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_video_channels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_video_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_video_files_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_video_views_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_videos_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_local_weekly_active_video_channels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_monthly_active_users_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_users_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_video_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_videos_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_weekly_active_users_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_videos_redundancy.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerStats::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
