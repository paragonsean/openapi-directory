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
 * OAIPlaybackMetricCreate.h
 *
 * 
 */

#ifndef OAIPlaybackMetricCreate_H
#define OAIPlaybackMetricCreate_H

#include <QJsonObject>

#include "OAIGetLiveId_id_parameter.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlaybackMetricCreate : public OAIObject {
public:
    OAIPlaybackMetricCreate();
    OAIPlaybackMetricCreate(QString json);
    ~OAIPlaybackMetricCreate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getDownloadedBytesHttp() const;
    void setDownloadedBytesHttp(const double &downloaded_bytes_http);
    bool is_downloaded_bytes_http_Set() const;
    bool is_downloaded_bytes_http_Valid() const;

    double getDownloadedBytesP2P() const;
    void setDownloadedBytesP2P(const double &downloaded_bytes_p2_p);
    bool is_downloaded_bytes_p2_p_Set() const;
    bool is_downloaded_bytes_p2_p_Valid() const;

    double getErrors() const;
    void setErrors(const double &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    double getFps() const;
    void setFps(const double &fps);
    bool is_fps_Set() const;
    bool is_fps_Valid() const;

    QString getPlayerMode() const;
    void setPlayerMode(const QString &player_mode);
    bool is_player_mode_Set() const;
    bool is_player_mode_Valid() const;

    double getResolution() const;
    void setResolution(const double &resolution);
    bool is_resolution_Set() const;
    bool is_resolution_Valid() const;

    double getResolutionChanges() const;
    void setResolutionChanges(const double &resolution_changes);
    bool is_resolution_changes_Set() const;
    bool is_resolution_changes_Valid() const;

    double getUploadedBytesP2P() const;
    void setUploadedBytesP2P(const double &uploaded_bytes_p2_p);
    bool is_uploaded_bytes_p2_p_Set() const;
    bool is_uploaded_bytes_p2_p_Valid() const;

    OAIGetLiveId_id_parameter getVideoId() const;
    void setVideoId(const OAIGetLiveId_id_parameter &video_id);
    bool is_video_id_Set() const;
    bool is_video_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_downloaded_bytes_http;
    bool m_downloaded_bytes_http_isSet;
    bool m_downloaded_bytes_http_isValid;

    double m_downloaded_bytes_p2_p;
    bool m_downloaded_bytes_p2_p_isSet;
    bool m_downloaded_bytes_p2_p_isValid;

    double m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;

    double m_fps;
    bool m_fps_isSet;
    bool m_fps_isValid;

    QString m_player_mode;
    bool m_player_mode_isSet;
    bool m_player_mode_isValid;

    double m_resolution;
    bool m_resolution_isSet;
    bool m_resolution_isValid;

    double m_resolution_changes;
    bool m_resolution_changes_isSet;
    bool m_resolution_changes_isValid;

    double m_uploaded_bytes_p2_p;
    bool m_uploaded_bytes_p2_p_isSet;
    bool m_uploaded_bytes_p2_p_isValid;

    OAIGetLiveId_id_parameter m_video_id;
    bool m_video_id_isSet;
    bool m_video_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlaybackMetricCreate)

#endif // OAIPlaybackMetricCreate_H
