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
 * OAIVideoUploadRequestResumable.h
 *
 * 
 */

#ifndef OAIVideoUploadRequestResumable_H
#define OAIVideoUploadRequestResumable_H

#include <QJsonObject>

#include "OAIHttpFileElement.h"
#include "OAIVideoPrivacySet.h"
#include "OAIVideoScheduledUpdate.h"
#include <QDateTime>
#include <QSet>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVideoScheduledUpdate;

class OAIVideoUploadRequestResumable : public OAIObject {
public:
    OAIVideoUploadRequestResumable();
    OAIVideoUploadRequestResumable(QString json);
    ~OAIVideoUploadRequestResumable() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCategory() const;
    void setCategory(const qint32 &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    qint32 getChannelId() const;
    void setChannelId(const qint32 &channel_id);
    bool is_channel_id_Set() const;
    bool is_channel_id_Valid() const;

    bool isCommentsEnabled() const;
    void setCommentsEnabled(const bool &comments_enabled);
    bool is_comments_enabled_Set() const;
    bool is_comments_enabled_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isDownloadEnabled() const;
    void setDownloadEnabled(const bool &download_enabled);
    bool is_download_enabled_Set() const;
    bool is_download_enabled_Valid() const;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    qint32 getLicence() const;
    void setLicence(const qint32 &licence);
    bool is_licence_Set() const;
    bool is_licence_Valid() const;

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

    OAIHttpFileElement getPreviewfile() const;
    void setPreviewfile(const OAIHttpFileElement &previewfile);
    bool is_previewfile_Set() const;
    bool is_previewfile_Valid() const;

    OAIVideoPrivacySet getPrivacy() const;
    void setPrivacy(const OAIVideoPrivacySet &privacy);
    bool is_privacy_Set() const;
    bool is_privacy_Valid() const;

    OAIVideoScheduledUpdate getScheduleUpdate() const;
    void setScheduleUpdate(const OAIVideoScheduledUpdate &schedule_update);
    bool is_schedule_update_Set() const;
    bool is_schedule_update_Valid() const;

    QString getSupport() const;
    void setSupport(const QString &support);
    bool is_support_Set() const;
    bool is_support_Valid() const;

    QSet<QString> getTags() const;
    void setTags(const QSet<QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    OAIHttpFileElement getThumbnailfile() const;
    void setThumbnailfile(const OAIHttpFileElement &thumbnailfile);
    bool is_thumbnailfile_Set() const;
    bool is_thumbnailfile_Valid() const;

    bool isWaitTranscoding() const;
    void setWaitTranscoding(const bool &wait_transcoding);
    bool is_wait_transcoding_Set() const;
    bool is_wait_transcoding_Valid() const;

    QString getFilename() const;
    void setFilename(const QString &filename);
    bool is_filename_Set() const;
    bool is_filename_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    qint32 m_channel_id;
    bool m_channel_id_isSet;
    bool m_channel_id_isValid;

    bool m_comments_enabled;
    bool m_comments_enabled_isSet;
    bool m_comments_enabled_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_download_enabled;
    bool m_download_enabled_isSet;
    bool m_download_enabled_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    qint32 m_licence;
    bool m_licence_isSet;
    bool m_licence_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_nsfw;
    bool m_nsfw_isSet;
    bool m_nsfw_isValid;

    QDateTime m_originally_published_at;
    bool m_originally_published_at_isSet;
    bool m_originally_published_at_isValid;

    OAIHttpFileElement m_previewfile;
    bool m_previewfile_isSet;
    bool m_previewfile_isValid;

    OAIVideoPrivacySet m_privacy;
    bool m_privacy_isSet;
    bool m_privacy_isValid;

    OAIVideoScheduledUpdate m_schedule_update;
    bool m_schedule_update_isSet;
    bool m_schedule_update_isValid;

    QString m_support;
    bool m_support_isSet;
    bool m_support_isValid;

    QSet<QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    OAIHttpFileElement m_thumbnailfile;
    bool m_thumbnailfile_isSet;
    bool m_thumbnailfile_isValid;

    bool m_wait_transcoding;
    bool m_wait_transcoding_isSet;
    bool m_wait_transcoding_isValid;

    QString m_filename;
    bool m_filename_isSet;
    bool m_filename_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVideoUploadRequestResumable)

#endif // OAIVideoUploadRequestResumable_H
