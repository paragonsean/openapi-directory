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
 * OAIUser.h
 *
 * 
 */

#ifndef OAIUser_H
#define OAIUser_H

#include <QJsonObject>

#include "OAIAccount.h"
#include "OAINSFWPolicy.h"
#include "OAIUser_role.h"
#include "OAIVideoChannel.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAccount;
class OAIUser_role;
class OAIVideoChannel;

class OAIUser : public OAIObject {
public:
    OAIUser();
    OAIUser(QString json);
    ~OAIUser() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAccount getAccount() const;
    void setAccount(const OAIAccount &account);
    bool is_account_Set() const;
    bool is_account_Valid() const;

    bool isAutoPlayNextVideo() const;
    void setAutoPlayNextVideo(const bool &auto_play_next_video);
    bool is_auto_play_next_video_Set() const;
    bool is_auto_play_next_video_Valid() const;

    bool isAutoPlayNextVideoPlaylist() const;
    void setAutoPlayNextVideoPlaylist(const bool &auto_play_next_video_playlist);
    bool is_auto_play_next_video_playlist_Set() const;
    bool is_auto_play_next_video_playlist_Valid() const;

    bool isAutoPlayVideo() const;
    void setAutoPlayVideo(const bool &auto_play_video);
    bool is_auto_play_video_Set() const;
    bool is_auto_play_video_Valid() const;

    bool isBlocked() const;
    void setBlocked(const bool &blocked);
    bool is_blocked_Set() const;
    bool is_blocked_Valid() const;

    QString getBlockedReason() const;
    void setBlockedReason(const QString &blocked_reason);
    bool is_blocked_reason_Set() const;
    bool is_blocked_reason_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    bool isEmailVerified() const;
    void setEmailVerified(const bool &email_verified);
    bool is_email_verified_Set() const;
    bool is_email_verified_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QDateTime getLastLoginDate() const;
    void setLastLoginDate(const QDateTime &last_login_date);
    bool is_last_login_date_Set() const;
    bool is_last_login_date_Valid() const;

    bool isNoAccountSetupWarningModal() const;
    void setNoAccountSetupWarningModal(const bool &no_account_setup_warning_modal);
    bool is_no_account_setup_warning_modal_Set() const;
    bool is_no_account_setup_warning_modal_Valid() const;

    bool isNoInstanceConfigWarningModal() const;
    void setNoInstanceConfigWarningModal(const bool &no_instance_config_warning_modal);
    bool is_no_instance_config_warning_modal_Set() const;
    bool is_no_instance_config_warning_modal_Valid() const;

    bool isNoWelcomeModal() const;
    void setNoWelcomeModal(const bool &no_welcome_modal);
    bool is_no_welcome_modal_Set() const;
    bool is_no_welcome_modal_Valid() const;

    OAINSFWPolicy getNsfwPolicy() const;
    void setNsfwPolicy(const OAINSFWPolicy &nsfw_policy);
    bool is_nsfw_policy_Set() const;
    bool is_nsfw_policy_Valid() const;

    bool isP2pEnabled() const;
    void setP2pEnabled(const bool &p2p_enabled);
    bool is_p2p_enabled_Set() const;
    bool is_p2p_enabled_Valid() const;

    QString getPluginAuth() const;
    void setPluginAuth(const QString &plugin_auth);
    bool is_plugin_auth_Set() const;
    bool is_plugin_auth_Valid() const;

    OAIUser_role getRole() const;
    void setRole(const OAIUser_role &role);
    bool is_role_Set() const;
    bool is_role_Valid() const;

    QString getTheme() const;
    void setTheme(const QString &theme);
    bool is_theme_Set() const;
    bool is_theme_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    QList<OAIVideoChannel> getVideoChannels() const;
    void setVideoChannels(const QList<OAIVideoChannel> &video_channels);
    bool is_video_channels_Set() const;
    bool is_video_channels_Valid() const;

    qint32 getVideoQuota() const;
    void setVideoQuota(const qint32 &video_quota);
    bool is_video_quota_Set() const;
    bool is_video_quota_Valid() const;

    qint32 getVideoQuotaDaily() const;
    void setVideoQuotaDaily(const qint32 &video_quota_daily);
    bool is_video_quota_daily_Set() const;
    bool is_video_quota_daily_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAccount m_account;
    bool m_account_isSet;
    bool m_account_isValid;

    bool m_auto_play_next_video;
    bool m_auto_play_next_video_isSet;
    bool m_auto_play_next_video_isValid;

    bool m_auto_play_next_video_playlist;
    bool m_auto_play_next_video_playlist_isSet;
    bool m_auto_play_next_video_playlist_isValid;

    bool m_auto_play_video;
    bool m_auto_play_video_isSet;
    bool m_auto_play_video_isValid;

    bool m_blocked;
    bool m_blocked_isSet;
    bool m_blocked_isValid;

    QString m_blocked_reason;
    bool m_blocked_reason_isSet;
    bool m_blocked_reason_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    bool m_email_verified;
    bool m_email_verified_isSet;
    bool m_email_verified_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QDateTime m_last_login_date;
    bool m_last_login_date_isSet;
    bool m_last_login_date_isValid;

    bool m_no_account_setup_warning_modal;
    bool m_no_account_setup_warning_modal_isSet;
    bool m_no_account_setup_warning_modal_isValid;

    bool m_no_instance_config_warning_modal;
    bool m_no_instance_config_warning_modal_isSet;
    bool m_no_instance_config_warning_modal_isValid;

    bool m_no_welcome_modal;
    bool m_no_welcome_modal_isSet;
    bool m_no_welcome_modal_isValid;

    OAINSFWPolicy m_nsfw_policy;
    bool m_nsfw_policy_isSet;
    bool m_nsfw_policy_isValid;

    bool m_p2p_enabled;
    bool m_p2p_enabled_isSet;
    bool m_p2p_enabled_isValid;

    QString m_plugin_auth;
    bool m_plugin_auth_isSet;
    bool m_plugin_auth_isValid;

    OAIUser_role m_role;
    bool m_role_isSet;
    bool m_role_isValid;

    QString m_theme;
    bool m_theme_isSet;
    bool m_theme_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;

    QList<OAIVideoChannel> m_video_channels;
    bool m_video_channels_isSet;
    bool m_video_channels_isValid;

    qint32 m_video_quota;
    bool m_video_quota_isSet;
    bool m_video_quota_isValid;

    qint32 m_video_quota_daily;
    bool m_video_quota_daily_isSet;
    bool m_video_quota_daily_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUser)

#endif // OAIUser_H
