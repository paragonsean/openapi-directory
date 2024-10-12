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
 * OAIVideoPlaylist.h
 *
 * 
 */

#ifndef OAIVideoPlaylist_H
#define OAIVideoPlaylist_H

#include <QJsonObject>

#include "OAIAccountSummary.h"
#include "OAIVideoChannelSummary.h"
#include "OAIVideoPlaylistPrivacyConstant.h"
#include "OAIVideoPlaylistTypeConstant.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAccountSummary;
class OAIVideoPlaylistPrivacyConstant;
class OAIVideoPlaylistTypeConstant;
class OAIVideoChannelSummary;

class OAIVideoPlaylist : public OAIObject {
public:
    OAIVideoPlaylist();
    OAIVideoPlaylist(QString json);
    ~OAIVideoPlaylist() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsLocal() const;
    void setIsLocal(const bool &is_local);
    bool is_is_local_Set() const;
    bool is_is_local_Valid() const;

    OAIAccountSummary getOwnerAccount() const;
    void setOwnerAccount(const OAIAccountSummary &owner_account);
    bool is_owner_account_Set() const;
    bool is_owner_account_Valid() const;

    OAIVideoPlaylistPrivacyConstant getPrivacy() const;
    void setPrivacy(const OAIVideoPlaylistPrivacyConstant &privacy);
    bool is_privacy_Set() const;
    bool is_privacy_Valid() const;

    QString getShortUuid() const;
    void setShortUuid(const QString &short_uuid);
    bool is_short_uuid_Set() const;
    bool is_short_uuid_Valid() const;

    QString getThumbnailPath() const;
    void setThumbnailPath(const QString &thumbnail_path);
    bool is_thumbnail_path_Set() const;
    bool is_thumbnail_path_Valid() const;

    OAIVideoPlaylistTypeConstant getType() const;
    void setType(const OAIVideoPlaylistTypeConstant &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QString getUuid() const;
    void setUuid(const QString &uuid);
    bool is_uuid_Set() const;
    bool is_uuid_Valid() const;

    OAIVideoChannelSummary getVideoChannel() const;
    void setVideoChannel(const OAIVideoChannelSummary &video_channel);
    bool is_video_channel_Set() const;
    bool is_video_channel_Valid() const;

    qint32 getVideoLength() const;
    void setVideoLength(const qint32 &video_length);
    bool is_video_length_Set() const;
    bool is_video_length_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_local;
    bool m_is_local_isSet;
    bool m_is_local_isValid;

    OAIAccountSummary m_owner_account;
    bool m_owner_account_isSet;
    bool m_owner_account_isValid;

    OAIVideoPlaylistPrivacyConstant m_privacy;
    bool m_privacy_isSet;
    bool m_privacy_isValid;

    QString m_short_uuid;
    bool m_short_uuid_isSet;
    bool m_short_uuid_isValid;

    QString m_thumbnail_path;
    bool m_thumbnail_path_isSet;
    bool m_thumbnail_path_isValid;

    OAIVideoPlaylistTypeConstant m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QString m_uuid;
    bool m_uuid_isSet;
    bool m_uuid_isValid;

    OAIVideoChannelSummary m_video_channel;
    bool m_video_channel_isSet;
    bool m_video_channel_isValid;

    qint32 m_video_length;
    bool m_video_length_isSet;
    bool m_video_length_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVideoPlaylist)

#endif // OAIVideoPlaylist_H
