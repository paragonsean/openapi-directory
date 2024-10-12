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
 * OAIVideosForXML_inner.h
 *
 * 
 */

#ifndef OAIVideosForXML_inner_H
#define OAIVideosForXML_inner_H

#include <QJsonObject>

#include "OAIVideosForXML_inner_enclosure.h"
#include "OAIVideosForXML_inner_media_community.h"
#include "OAIVideosForXML_inner_media_embed.h"
#include "OAIVideosForXML_inner_media_group_inner.h"
#include "OAIVideosForXML_inner_media_player.h"
#include "OAIVideosForXML_inner_media_thumbnail.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVideosForXML_inner_enclosure;
class OAIVideosForXML_inner_media_community;
class OAIVideosForXML_inner_media_embed;
class OAIVideosForXML_inner_media_group_inner;
class OAIVideosForXML_inner_media_player;
class OAIVideosForXML_inner_media_thumbnail;

class OAIVideosForXML_inner : public OAIObject {
public:
    OAIVideosForXML_inner();
    OAIVideosForXML_inner(QString json);
    ~OAIVideosForXML_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getContentencoded() const;
    void setContentencoded(const QString &contentencoded);
    bool is_contentencoded_Set() const;
    bool is_contentencoded_Valid() const;

    QString getDccreator() const;
    void setDccreator(const QString &dccreator);
    bool is_dccreator_Set() const;
    bool is_dccreator_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIVideosForXML_inner_enclosure getEnclosure() const;
    void setEnclosure(const OAIVideosForXML_inner_enclosure &enclosure);
    bool is_enclosure_Set() const;
    bool is_enclosure_Valid() const;

    QString getGuid() const;
    void setGuid(const QString &guid);
    bool is_guid_Set() const;
    bool is_guid_Valid() const;

    QString getLink() const;
    void setLink(const QString &link);
    bool is_link_Set() const;
    bool is_link_Valid() const;

    qint32 getMediacategory() const;
    void setMediacategory(const qint32 &mediacategory);
    bool is_mediacategory_Set() const;
    bool is_mediacategory_Valid() const;

    OAIVideosForXML_inner_media_community getMediacommunity() const;
    void setMediacommunity(const OAIVideosForXML_inner_media_community &mediacommunity);
    bool is_mediacommunity_Set() const;
    bool is_mediacommunity_Valid() const;

    QString getMediadescription() const;
    void setMediadescription(const QString &mediadescription);
    bool is_mediadescription_Set() const;
    bool is_mediadescription_Valid() const;

    OAIVideosForXML_inner_media_embed getMediaembed() const;
    void setMediaembed(const OAIVideosForXML_inner_media_embed &mediaembed);
    bool is_mediaembed_Set() const;
    bool is_mediaembed_Valid() const;

    QList<OAIVideosForXML_inner_media_group_inner> getMediagroup() const;
    void setMediagroup(const QList<OAIVideosForXML_inner_media_group_inner> &mediagroup);
    bool is_mediagroup_Set() const;
    bool is_mediagroup_Valid() const;

    OAIVideosForXML_inner_media_player getMediaplayer() const;
    void setMediaplayer(const OAIVideosForXML_inner_media_player &mediaplayer);
    bool is_mediaplayer_Set() const;
    bool is_mediaplayer_Valid() const;

    QString getMediarating() const;
    void setMediarating(const QString &mediarating);
    bool is_mediarating_Set() const;
    bool is_mediarating_Valid() const;

    OAIVideosForXML_inner_media_thumbnail getMediathumbnail() const;
    void setMediathumbnail(const OAIVideosForXML_inner_media_thumbnail &mediathumbnail);
    bool is_mediathumbnail_Set() const;
    bool is_mediathumbnail_Valid() const;

    QString getMediatitle() const;
    void setMediatitle(const QString &mediatitle);
    bool is_mediatitle_Set() const;
    bool is_mediatitle_Valid() const;

    QDateTime getPubDate() const;
    void setPubDate(const QDateTime &pub_date);
    bool is_pub_date_Set() const;
    bool is_pub_date_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_contentencoded;
    bool m_contentencoded_isSet;
    bool m_contentencoded_isValid;

    QString m_dccreator;
    bool m_dccreator_isSet;
    bool m_dccreator_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIVideosForXML_inner_enclosure m_enclosure;
    bool m_enclosure_isSet;
    bool m_enclosure_isValid;

    QString m_guid;
    bool m_guid_isSet;
    bool m_guid_isValid;

    QString m_link;
    bool m_link_isSet;
    bool m_link_isValid;

    qint32 m_mediacategory;
    bool m_mediacategory_isSet;
    bool m_mediacategory_isValid;

    OAIVideosForXML_inner_media_community m_mediacommunity;
    bool m_mediacommunity_isSet;
    bool m_mediacommunity_isValid;

    QString m_mediadescription;
    bool m_mediadescription_isSet;
    bool m_mediadescription_isValid;

    OAIVideosForXML_inner_media_embed m_mediaembed;
    bool m_mediaembed_isSet;
    bool m_mediaembed_isValid;

    QList<OAIVideosForXML_inner_media_group_inner> m_mediagroup;
    bool m_mediagroup_isSet;
    bool m_mediagroup_isValid;

    OAIVideosForXML_inner_media_player m_mediaplayer;
    bool m_mediaplayer_isSet;
    bool m_mediaplayer_isValid;

    QString m_mediarating;
    bool m_mediarating_isSet;
    bool m_mediarating_isValid;

    OAIVideosForXML_inner_media_thumbnail m_mediathumbnail;
    bool m_mediathumbnail_isSet;
    bool m_mediathumbnail_isValid;

    QString m_mediatitle;
    bool m_mediatitle_isSet;
    bool m_mediatitle_isValid;

    QDateTime m_pub_date;
    bool m_pub_date_isSet;
    bool m_pub_date_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVideosForXML_inner)

#endif // OAIVideosForXML_inner_H
