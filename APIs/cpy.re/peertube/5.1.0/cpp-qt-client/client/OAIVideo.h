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
 * OAIVideo.h
 *
 * 
 */

#ifndef OAIVideo_H
#define OAIVideo_H

#include <QJsonObject>

#include "OAIAccountSummary.h"
#include "OAIVideoChannelSummary.h"
#include "OAIVideoConstantNumber_Category.h"
#include "OAIVideoConstantNumber_Licence.h"
#include "OAIVideoConstantString_Language.h"
#include "OAIVideoPrivacyConstant.h"
#include "OAIVideoScheduledUpdate.h"
#include "OAIVideoStateConstant.h"
#include "OAIVideo_userHistory.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAccountSummary;
class OAIVideoConstantNumber_Category;
class OAIVideoChannelSummary;
class OAIVideoConstantString_Language;
class OAIVideoConstantNumber_Licence;
class OAIVideoPrivacyConstant;
class OAIVideoScheduledUpdate;
class OAIVideoStateConstant;
class OAIVideo_userHistory;

class OAIVideo : public OAIObject {
public:
    OAIVideo();
    OAIVideo(QString json);
    ~OAIVideo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAccountSummary getAccount() const;
    void setAccount(const OAIAccountSummary &account);
    bool is_account_Set() const;
    bool is_account_Valid() const;

    bool isBlacklisted() const;
    void setBlacklisted(const bool &blacklisted);
    bool is_blacklisted_Set() const;
    bool is_blacklisted_Valid() const;

    QString getBlacklistedReason() const;
    void setBlacklistedReason(const QString &blacklisted_reason);
    bool is_blacklisted_reason_Set() const;
    bool is_blacklisted_reason_Valid() const;

    OAIVideoConstantNumber_Category getCategory() const;
    void setCategory(const OAIVideoConstantNumber_Category &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    OAIVideoChannelSummary getChannel() const;
    void setChannel(const OAIVideoChannelSummary &channel);
    bool is_channel_Set() const;
    bool is_channel_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    qint32 getDislikes() const;
    void setDislikes(const qint32 &dislikes);
    bool is_dislikes_Set() const;
    bool is_dislikes_Valid() const;

    qint32 getDuration() const;
    void setDuration(const qint32 &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getEmbedPath() const;
    void setEmbedPath(const QString &embed_path);
    bool is_embed_path_Set() const;
    bool is_embed_path_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsLive() const;
    void setIsLive(const bool &is_live);
    bool is_is_live_Set() const;
    bool is_is_live_Valid() const;

    bool isIsLocal() const;
    void setIsLocal(const bool &is_local);
    bool is_is_local_Set() const;
    bool is_is_local_Valid() const;

    OAIVideoConstantString_Language getLanguage() const;
    void setLanguage(const OAIVideoConstantString_Language &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    OAIVideoConstantNumber_Licence getLicence() const;
    void setLicence(const OAIVideoConstantNumber_Licence &licence);
    bool is_licence_Set() const;
    bool is_licence_Valid() const;

    qint32 getLikes() const;
    void setLikes(const qint32 &likes);
    bool is_likes_Set() const;
    bool is_likes_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isNsfw() const;
    void setNsfw(const bool &nsfw);
    bool is_nsfw_Set() const;
    bool is_nsfw_Valid() const;

    QDateTime getOriginallyPublishedAt() const;
    void setOriginallyPublishedAt(const QDateTime &originally_published_at);
    bool is_originally_published_at_Set() const;
    bool is_originally_published_at_Valid() const;

    QString getPreviewPath() const;
    void setPreviewPath(const QString &preview_path);
    bool is_preview_path_Set() const;
    bool is_preview_path_Valid() const;

    OAIVideoPrivacyConstant getPrivacy() const;
    void setPrivacy(const OAIVideoPrivacyConstant &privacy);
    bool is_privacy_Set() const;
    bool is_privacy_Valid() const;

    QDateTime getPublishedAt() const;
    void setPublishedAt(const QDateTime &published_at);
    bool is_published_at_Set() const;
    bool is_published_at_Valid() const;

    OAIVideoScheduledUpdate getScheduledUpdate() const;
    void setScheduledUpdate(const OAIVideoScheduledUpdate &scheduled_update);
    bool is_scheduled_update_Set() const;
    bool is_scheduled_update_Valid() const;

    QString getShortUuid() const;
    void setShortUuid(const QString &short_uuid);
    bool is_short_uuid_Set() const;
    bool is_short_uuid_Valid() const;

    OAIVideoStateConstant getState() const;
    void setState(const OAIVideoStateConstant &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getThumbnailPath() const;
    void setThumbnailPath(const QString &thumbnail_path);
    bool is_thumbnail_path_Set() const;
    bool is_thumbnail_path_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    OAIVideo_userHistory getUserHistory() const;
    void setUserHistory(const OAIVideo_userHistory &user_history);
    bool is_user_history_Set() const;
    bool is_user_history_Valid() const;

    QString getUuid() const;
    void setUuid(const QString &uuid);
    bool is_uuid_Set() const;
    bool is_uuid_Valid() const;

    qint32 getViews() const;
    void setViews(const qint32 &views);
    bool is_views_Set() const;
    bool is_views_Valid() const;

    bool isWaitTranscoding() const;
    void setWaitTranscoding(const bool &wait_transcoding);
    bool is_wait_transcoding_Set() const;
    bool is_wait_transcoding_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAccountSummary m_account;
    bool m_account_isSet;
    bool m_account_isValid;

    bool m_blacklisted;
    bool m_blacklisted_isSet;
    bool m_blacklisted_isValid;

    QString m_blacklisted_reason;
    bool m_blacklisted_reason_isSet;
    bool m_blacklisted_reason_isValid;

    OAIVideoConstantNumber_Category m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    OAIVideoChannelSummary m_channel;
    bool m_channel_isSet;
    bool m_channel_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    qint32 m_dislikes;
    bool m_dislikes_isSet;
    bool m_dislikes_isValid;

    qint32 m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_embed_path;
    bool m_embed_path_isSet;
    bool m_embed_path_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_live;
    bool m_is_live_isSet;
    bool m_is_live_isValid;

    bool m_is_local;
    bool m_is_local_isSet;
    bool m_is_local_isValid;

    OAIVideoConstantString_Language m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    OAIVideoConstantNumber_Licence m_licence;
    bool m_licence_isSet;
    bool m_licence_isValid;

    qint32 m_likes;
    bool m_likes_isSet;
    bool m_likes_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_nsfw;
    bool m_nsfw_isSet;
    bool m_nsfw_isValid;

    QDateTime m_originally_published_at;
    bool m_originally_published_at_isSet;
    bool m_originally_published_at_isValid;

    QString m_preview_path;
    bool m_preview_path_isSet;
    bool m_preview_path_isValid;

    OAIVideoPrivacyConstant m_privacy;
    bool m_privacy_isSet;
    bool m_privacy_isValid;

    QDateTime m_published_at;
    bool m_published_at_isSet;
    bool m_published_at_isValid;

    OAIVideoScheduledUpdate m_scheduled_update;
    bool m_scheduled_update_isSet;
    bool m_scheduled_update_isValid;

    QString m_short_uuid;
    bool m_short_uuid_isSet;
    bool m_short_uuid_isValid;

    OAIVideoStateConstant m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_thumbnail_path;
    bool m_thumbnail_path_isSet;
    bool m_thumbnail_path_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    OAIVideo_userHistory m_user_history;
    bool m_user_history_isSet;
    bool m_user_history_isValid;

    QString m_uuid;
    bool m_uuid_isSet;
    bool m_uuid_isValid;

    qint32 m_views;
    bool m_views_isSet;
    bool m_views_isValid;

    bool m_wait_transcoding;
    bool m_wait_transcoding_isSet;
    bool m_wait_transcoding_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVideo)

#endif // OAIVideo_H
