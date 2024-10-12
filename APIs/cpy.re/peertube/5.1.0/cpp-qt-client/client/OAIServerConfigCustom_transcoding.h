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
 * OAIServerConfigCustom_transcoding.h
 *
 * Settings pertaining to transcoding jobs
 */

#ifndef OAIServerConfigCustom_transcoding_H
#define OAIServerConfigCustom_transcoding_H

#include <QJsonObject>

#include "OAIServerConfigCustom_transcoding_hls.h"
#include "OAIServerConfigCustom_transcoding_resolutions.h"
#include "OAIServerConfigCustom_transcoding_webtorrent.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIServerConfigCustom_transcoding_hls;
class OAIServerConfigCustom_transcoding_resolutions;
class OAIServerConfigCustom_transcoding_webtorrent;

class OAIServerConfigCustom_transcoding : public OAIObject {
public:
    OAIServerConfigCustom_transcoding();
    OAIServerConfigCustom_transcoding(QString json);
    ~OAIServerConfigCustom_transcoding() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowAdditionalExtensions() const;
    void setAllowAdditionalExtensions(const bool &allow_additional_extensions);
    bool is_allow_additional_extensions_Set() const;
    bool is_allow_additional_extensions_Valid() const;

    bool isAllowAudioFiles() const;
    void setAllowAudioFiles(const bool &allow_audio_files);
    bool is_allow_audio_files_Set() const;
    bool is_allow_audio_files_Valid() const;

    double getConcurrency() const;
    void setConcurrency(const double &concurrency);
    bool is_concurrency_Set() const;
    bool is_concurrency_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    OAIServerConfigCustom_transcoding_hls getHls() const;
    void setHls(const OAIServerConfigCustom_transcoding_hls &hls);
    bool is_hls_Set() const;
    bool is_hls_Valid() const;

    QString getProfile() const;
    void setProfile(const QString &profile);
    bool is_profile_Set() const;
    bool is_profile_Valid() const;

    OAIServerConfigCustom_transcoding_resolutions getResolutions() const;
    void setResolutions(const OAIServerConfigCustom_transcoding_resolutions &resolutions);
    bool is_resolutions_Set() const;
    bool is_resolutions_Valid() const;

    qint32 getThreads() const;
    void setThreads(const qint32 &threads);
    bool is_threads_Set() const;
    bool is_threads_Valid() const;

    OAIServerConfigCustom_transcoding_webtorrent getWebtorrent() const;
    void setWebtorrent(const OAIServerConfigCustom_transcoding_webtorrent &webtorrent);
    bool is_webtorrent_Set() const;
    bool is_webtorrent_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_additional_extensions;
    bool m_allow_additional_extensions_isSet;
    bool m_allow_additional_extensions_isValid;

    bool m_allow_audio_files;
    bool m_allow_audio_files_isSet;
    bool m_allow_audio_files_isValid;

    double m_concurrency;
    bool m_concurrency_isSet;
    bool m_concurrency_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    OAIServerConfigCustom_transcoding_hls m_hls;
    bool m_hls_isSet;
    bool m_hls_isValid;

    QString m_profile;
    bool m_profile_isSet;
    bool m_profile_isValid;

    OAIServerConfigCustom_transcoding_resolutions m_resolutions;
    bool m_resolutions_isSet;
    bool m_resolutions_isValid;

    qint32 m_threads;
    bool m_threads_isSet;
    bool m_threads_isValid;

    OAIServerConfigCustom_transcoding_webtorrent m_webtorrent;
    bool m_webtorrent_isSet;
    bool m_webtorrent_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServerConfigCustom_transcoding)

#endif // OAIServerConfigCustom_transcoding_H
