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

/*
 * OAIServerStats.h
 *
 * 
 */

#ifndef OAIServerStats_H
#define OAIServerStats_H

#include <QJsonObject>

#include "OAIServerStats_videosRedundancy_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIServerStats_videosRedundancy_inner;

class OAIServerStats : public OAIObject {
public:
    OAIServerStats();
    OAIServerStats(QString json);
    ~OAIServerStats() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getActivityPubMessagesProcessedPerSecond() const;
    void setActivityPubMessagesProcessedPerSecond(const double &activity_pub_messages_processed_per_second);
    bool is_activity_pub_messages_processed_per_second_Set() const;
    bool is_activity_pub_messages_processed_per_second_Valid() const;

    double getTotalActivityPubMessagesErrors() const;
    void setTotalActivityPubMessagesErrors(const double &total_activity_pub_messages_errors);
    bool is_total_activity_pub_messages_errors_Set() const;
    bool is_total_activity_pub_messages_errors_Valid() const;

    double getTotalActivityPubMessagesProcessed() const;
    void setTotalActivityPubMessagesProcessed(const double &total_activity_pub_messages_processed);
    bool is_total_activity_pub_messages_processed_Set() const;
    bool is_total_activity_pub_messages_processed_Valid() const;

    double getTotalActivityPubMessagesSuccesses() const;
    void setTotalActivityPubMessagesSuccesses(const double &total_activity_pub_messages_successes);
    bool is_total_activity_pub_messages_successes_Set() const;
    bool is_total_activity_pub_messages_successes_Valid() const;

    double getTotalActivityPubMessagesWaiting() const;
    void setTotalActivityPubMessagesWaiting(const double &total_activity_pub_messages_waiting);
    bool is_total_activity_pub_messages_waiting_Set() const;
    bool is_total_activity_pub_messages_waiting_Valid() const;

    double getTotalDailyActiveUsers() const;
    void setTotalDailyActiveUsers(const double &total_daily_active_users);
    bool is_total_daily_active_users_Set() const;
    bool is_total_daily_active_users_Valid() const;

    double getTotalInstanceFollowers() const;
    void setTotalInstanceFollowers(const double &total_instance_followers);
    bool is_total_instance_followers_Set() const;
    bool is_total_instance_followers_Valid() const;

    double getTotalInstanceFollowing() const;
    void setTotalInstanceFollowing(const double &total_instance_following);
    bool is_total_instance_following_Set() const;
    bool is_total_instance_following_Valid() const;

    double getTotalLocalDailyActiveVideoChannels() const;
    void setTotalLocalDailyActiveVideoChannels(const double &total_local_daily_active_video_channels);
    bool is_total_local_daily_active_video_channels_Set() const;
    bool is_total_local_daily_active_video_channels_Valid() const;

    double getTotalLocalMonthlyActiveVideoChannels() const;
    void setTotalLocalMonthlyActiveVideoChannels(const double &total_local_monthly_active_video_channels);
    bool is_total_local_monthly_active_video_channels_Set() const;
    bool is_total_local_monthly_active_video_channels_Valid() const;

    double getTotalLocalPlaylists() const;
    void setTotalLocalPlaylists(const double &total_local_playlists);
    bool is_total_local_playlists_Set() const;
    bool is_total_local_playlists_Valid() const;

    double getTotalLocalVideoChannels() const;
    void setTotalLocalVideoChannels(const double &total_local_video_channels);
    bool is_total_local_video_channels_Set() const;
    bool is_total_local_video_channels_Valid() const;

    double getTotalLocalVideoComments() const;
    void setTotalLocalVideoComments(const double &total_local_video_comments);
    bool is_total_local_video_comments_Set() const;
    bool is_total_local_video_comments_Valid() const;

    double getTotalLocalVideoFilesSize() const;
    void setTotalLocalVideoFilesSize(const double &total_local_video_files_size);
    bool is_total_local_video_files_size_Set() const;
    bool is_total_local_video_files_size_Valid() const;

    double getTotalLocalVideoViews() const;
    void setTotalLocalVideoViews(const double &total_local_video_views);
    bool is_total_local_video_views_Set() const;
    bool is_total_local_video_views_Valid() const;

    double getTotalLocalVideos() const;
    void setTotalLocalVideos(const double &total_local_videos);
    bool is_total_local_videos_Set() const;
    bool is_total_local_videos_Valid() const;

    double getTotalLocalWeeklyActiveVideoChannels() const;
    void setTotalLocalWeeklyActiveVideoChannels(const double &total_local_weekly_active_video_channels);
    bool is_total_local_weekly_active_video_channels_Set() const;
    bool is_total_local_weekly_active_video_channels_Valid() const;

    double getTotalMonthlyActiveUsers() const;
    void setTotalMonthlyActiveUsers(const double &total_monthly_active_users);
    bool is_total_monthly_active_users_Set() const;
    bool is_total_monthly_active_users_Valid() const;

    double getTotalUsers() const;
    void setTotalUsers(const double &total_users);
    bool is_total_users_Set() const;
    bool is_total_users_Valid() const;

    double getTotalVideoComments() const;
    void setTotalVideoComments(const double &total_video_comments);
    bool is_total_video_comments_Set() const;
    bool is_total_video_comments_Valid() const;

    double getTotalVideos() const;
    void setTotalVideos(const double &total_videos);
    bool is_total_videos_Set() const;
    bool is_total_videos_Valid() const;

    double getTotalWeeklyActiveUsers() const;
    void setTotalWeeklyActiveUsers(const double &total_weekly_active_users);
    bool is_total_weekly_active_users_Set() const;
    bool is_total_weekly_active_users_Valid() const;

    QList<OAIServerStats_videosRedundancy_inner> getVideosRedundancy() const;
    void setVideosRedundancy(const QList<OAIServerStats_videosRedundancy_inner> &videos_redundancy);
    bool is_videos_redundancy_Set() const;
    bool is_videos_redundancy_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_activity_pub_messages_processed_per_second;
    bool m_activity_pub_messages_processed_per_second_isSet;
    bool m_activity_pub_messages_processed_per_second_isValid;

    double m_total_activity_pub_messages_errors;
    bool m_total_activity_pub_messages_errors_isSet;
    bool m_total_activity_pub_messages_errors_isValid;

    double m_total_activity_pub_messages_processed;
    bool m_total_activity_pub_messages_processed_isSet;
    bool m_total_activity_pub_messages_processed_isValid;

    double m_total_activity_pub_messages_successes;
    bool m_total_activity_pub_messages_successes_isSet;
    bool m_total_activity_pub_messages_successes_isValid;

    double m_total_activity_pub_messages_waiting;
    bool m_total_activity_pub_messages_waiting_isSet;
    bool m_total_activity_pub_messages_waiting_isValid;

    double m_total_daily_active_users;
    bool m_total_daily_active_users_isSet;
    bool m_total_daily_active_users_isValid;

    double m_total_instance_followers;
    bool m_total_instance_followers_isSet;
    bool m_total_instance_followers_isValid;

    double m_total_instance_following;
    bool m_total_instance_following_isSet;
    bool m_total_instance_following_isValid;

    double m_total_local_daily_active_video_channels;
    bool m_total_local_daily_active_video_channels_isSet;
    bool m_total_local_daily_active_video_channels_isValid;

    double m_total_local_monthly_active_video_channels;
    bool m_total_local_monthly_active_video_channels_isSet;
    bool m_total_local_monthly_active_video_channels_isValid;

    double m_total_local_playlists;
    bool m_total_local_playlists_isSet;
    bool m_total_local_playlists_isValid;

    double m_total_local_video_channels;
    bool m_total_local_video_channels_isSet;
    bool m_total_local_video_channels_isValid;

    double m_total_local_video_comments;
    bool m_total_local_video_comments_isSet;
    bool m_total_local_video_comments_isValid;

    double m_total_local_video_files_size;
    bool m_total_local_video_files_size_isSet;
    bool m_total_local_video_files_size_isValid;

    double m_total_local_video_views;
    bool m_total_local_video_views_isSet;
    bool m_total_local_video_views_isValid;

    double m_total_local_videos;
    bool m_total_local_videos_isSet;
    bool m_total_local_videos_isValid;

    double m_total_local_weekly_active_video_channels;
    bool m_total_local_weekly_active_video_channels_isSet;
    bool m_total_local_weekly_active_video_channels_isValid;

    double m_total_monthly_active_users;
    bool m_total_monthly_active_users_isSet;
    bool m_total_monthly_active_users_isValid;

    double m_total_users;
    bool m_total_users_isSet;
    bool m_total_users_isValid;

    double m_total_video_comments;
    bool m_total_video_comments_isSet;
    bool m_total_video_comments_isValid;

    double m_total_videos;
    bool m_total_videos_isSet;
    bool m_total_videos_isValid;

    double m_total_weekly_active_users;
    bool m_total_weekly_active_users_isSet;
    bool m_total_weekly_active_users_isValid;

    QList<OAIServerStats_videosRedundancy_inner> m_videos_redundancy;
    bool m_videos_redundancy_isSet;
    bool m_videos_redundancy_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServerStats)

#endif // OAIServerStats_H
