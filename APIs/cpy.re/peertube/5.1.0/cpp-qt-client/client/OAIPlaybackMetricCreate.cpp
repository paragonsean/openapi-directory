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

#include "OAIPlaybackMetricCreate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaybackMetricCreate::OAIPlaybackMetricCreate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaybackMetricCreate::OAIPlaybackMetricCreate() {
    this->initializeModel();
}

OAIPlaybackMetricCreate::~OAIPlaybackMetricCreate() {}

void OAIPlaybackMetricCreate::initializeModel() {

    m_downloaded_bytes_http_isSet = false;
    m_downloaded_bytes_http_isValid = false;

    m_downloaded_bytes_p2_p_isSet = false;
    m_downloaded_bytes_p2_p_isValid = false;

    m_errors_isSet = false;
    m_errors_isValid = false;

    m_fps_isSet = false;
    m_fps_isValid = false;

    m_player_mode_isSet = false;
    m_player_mode_isValid = false;

    m_resolution_isSet = false;
    m_resolution_isValid = false;

    m_resolution_changes_isSet = false;
    m_resolution_changes_isValid = false;

    m_uploaded_bytes_p2_p_isSet = false;
    m_uploaded_bytes_p2_p_isValid = false;

    m_video_id_isSet = false;
    m_video_id_isValid = false;
}

void OAIPlaybackMetricCreate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaybackMetricCreate::fromJsonObject(QJsonObject json) {

    m_downloaded_bytes_http_isValid = ::OpenAPI::fromJsonValue(m_downloaded_bytes_http, json[QString("downloadedBytesHTTP")]);
    m_downloaded_bytes_http_isSet = !json[QString("downloadedBytesHTTP")].isNull() && m_downloaded_bytes_http_isValid;

    m_downloaded_bytes_p2_p_isValid = ::OpenAPI::fromJsonValue(m_downloaded_bytes_p2_p, json[QString("downloadedBytesP2P")]);
    m_downloaded_bytes_p2_p_isSet = !json[QString("downloadedBytesP2P")].isNull() && m_downloaded_bytes_p2_p_isValid;

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("errors")]);
    m_errors_isSet = !json[QString("errors")].isNull() && m_errors_isValid;

    m_fps_isValid = ::OpenAPI::fromJsonValue(m_fps, json[QString("fps")]);
    m_fps_isSet = !json[QString("fps")].isNull() && m_fps_isValid;

    m_player_mode_isValid = ::OpenAPI::fromJsonValue(m_player_mode, json[QString("playerMode")]);
    m_player_mode_isSet = !json[QString("playerMode")].isNull() && m_player_mode_isValid;

    m_resolution_isValid = ::OpenAPI::fromJsonValue(m_resolution, json[QString("resolution")]);
    m_resolution_isSet = !json[QString("resolution")].isNull() && m_resolution_isValid;

    m_resolution_changes_isValid = ::OpenAPI::fromJsonValue(m_resolution_changes, json[QString("resolutionChanges")]);
    m_resolution_changes_isSet = !json[QString("resolutionChanges")].isNull() && m_resolution_changes_isValid;

    m_uploaded_bytes_p2_p_isValid = ::OpenAPI::fromJsonValue(m_uploaded_bytes_p2_p, json[QString("uploadedBytesP2P")]);
    m_uploaded_bytes_p2_p_isSet = !json[QString("uploadedBytesP2P")].isNull() && m_uploaded_bytes_p2_p_isValid;

    m_video_id_isValid = ::OpenAPI::fromJsonValue(m_video_id, json[QString("videoId")]);
    m_video_id_isSet = !json[QString("videoId")].isNull() && m_video_id_isValid;
}

QString OAIPlaybackMetricCreate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaybackMetricCreate::asJsonObject() const {
    QJsonObject obj;
    if (m_downloaded_bytes_http_isSet) {
        obj.insert(QString("downloadedBytesHTTP"), ::OpenAPI::toJsonValue(m_downloaded_bytes_http));
    }
    if (m_downloaded_bytes_p2_p_isSet) {
        obj.insert(QString("downloadedBytesP2P"), ::OpenAPI::toJsonValue(m_downloaded_bytes_p2_p));
    }
    if (m_errors_isSet) {
        obj.insert(QString("errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    if (m_fps_isSet) {
        obj.insert(QString("fps"), ::OpenAPI::toJsonValue(m_fps));
    }
    if (m_player_mode_isSet) {
        obj.insert(QString("playerMode"), ::OpenAPI::toJsonValue(m_player_mode));
    }
    if (m_resolution_isSet) {
        obj.insert(QString("resolution"), ::OpenAPI::toJsonValue(m_resolution));
    }
    if (m_resolution_changes_isSet) {
        obj.insert(QString("resolutionChanges"), ::OpenAPI::toJsonValue(m_resolution_changes));
    }
    if (m_uploaded_bytes_p2_p_isSet) {
        obj.insert(QString("uploadedBytesP2P"), ::OpenAPI::toJsonValue(m_uploaded_bytes_p2_p));
    }
    if (m_video_id.isSet()) {
        obj.insert(QString("videoId"), ::OpenAPI::toJsonValue(m_video_id));
    }
    return obj;
}

double OAIPlaybackMetricCreate::getDownloadedBytesHttp() const {
    return m_downloaded_bytes_http;
}
void OAIPlaybackMetricCreate::setDownloadedBytesHttp(const double &downloaded_bytes_http) {
    m_downloaded_bytes_http = downloaded_bytes_http;
    m_downloaded_bytes_http_isSet = true;
}

bool OAIPlaybackMetricCreate::is_downloaded_bytes_http_Set() const{
    return m_downloaded_bytes_http_isSet;
}

bool OAIPlaybackMetricCreate::is_downloaded_bytes_http_Valid() const{
    return m_downloaded_bytes_http_isValid;
}

double OAIPlaybackMetricCreate::getDownloadedBytesP2P() const {
    return m_downloaded_bytes_p2_p;
}
void OAIPlaybackMetricCreate::setDownloadedBytesP2P(const double &downloaded_bytes_p2_p) {
    m_downloaded_bytes_p2_p = downloaded_bytes_p2_p;
    m_downloaded_bytes_p2_p_isSet = true;
}

bool OAIPlaybackMetricCreate::is_downloaded_bytes_p2_p_Set() const{
    return m_downloaded_bytes_p2_p_isSet;
}

bool OAIPlaybackMetricCreate::is_downloaded_bytes_p2_p_Valid() const{
    return m_downloaded_bytes_p2_p_isValid;
}

double OAIPlaybackMetricCreate::getErrors() const {
    return m_errors;
}
void OAIPlaybackMetricCreate::setErrors(const double &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAIPlaybackMetricCreate::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAIPlaybackMetricCreate::is_errors_Valid() const{
    return m_errors_isValid;
}

double OAIPlaybackMetricCreate::getFps() const {
    return m_fps;
}
void OAIPlaybackMetricCreate::setFps(const double &fps) {
    m_fps = fps;
    m_fps_isSet = true;
}

bool OAIPlaybackMetricCreate::is_fps_Set() const{
    return m_fps_isSet;
}

bool OAIPlaybackMetricCreate::is_fps_Valid() const{
    return m_fps_isValid;
}

QString OAIPlaybackMetricCreate::getPlayerMode() const {
    return m_player_mode;
}
void OAIPlaybackMetricCreate::setPlayerMode(const QString &player_mode) {
    m_player_mode = player_mode;
    m_player_mode_isSet = true;
}

bool OAIPlaybackMetricCreate::is_player_mode_Set() const{
    return m_player_mode_isSet;
}

bool OAIPlaybackMetricCreate::is_player_mode_Valid() const{
    return m_player_mode_isValid;
}

double OAIPlaybackMetricCreate::getResolution() const {
    return m_resolution;
}
void OAIPlaybackMetricCreate::setResolution(const double &resolution) {
    m_resolution = resolution;
    m_resolution_isSet = true;
}

bool OAIPlaybackMetricCreate::is_resolution_Set() const{
    return m_resolution_isSet;
}

bool OAIPlaybackMetricCreate::is_resolution_Valid() const{
    return m_resolution_isValid;
}

double OAIPlaybackMetricCreate::getResolutionChanges() const {
    return m_resolution_changes;
}
void OAIPlaybackMetricCreate::setResolutionChanges(const double &resolution_changes) {
    m_resolution_changes = resolution_changes;
    m_resolution_changes_isSet = true;
}

bool OAIPlaybackMetricCreate::is_resolution_changes_Set() const{
    return m_resolution_changes_isSet;
}

bool OAIPlaybackMetricCreate::is_resolution_changes_Valid() const{
    return m_resolution_changes_isValid;
}

double OAIPlaybackMetricCreate::getUploadedBytesP2P() const {
    return m_uploaded_bytes_p2_p;
}
void OAIPlaybackMetricCreate::setUploadedBytesP2P(const double &uploaded_bytes_p2_p) {
    m_uploaded_bytes_p2_p = uploaded_bytes_p2_p;
    m_uploaded_bytes_p2_p_isSet = true;
}

bool OAIPlaybackMetricCreate::is_uploaded_bytes_p2_p_Set() const{
    return m_uploaded_bytes_p2_p_isSet;
}

bool OAIPlaybackMetricCreate::is_uploaded_bytes_p2_p_Valid() const{
    return m_uploaded_bytes_p2_p_isValid;
}

OAIGetLiveId_id_parameter OAIPlaybackMetricCreate::getVideoId() const {
    return m_video_id;
}
void OAIPlaybackMetricCreate::setVideoId(const OAIGetLiveId_id_parameter &video_id) {
    m_video_id = video_id;
    m_video_id_isSet = true;
}

bool OAIPlaybackMetricCreate::is_video_id_Set() const{
    return m_video_id_isSet;
}

bool OAIPlaybackMetricCreate::is_video_id_Valid() const{
    return m_video_id_isValid;
}

bool OAIPlaybackMetricCreate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_downloaded_bytes_http_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_downloaded_bytes_p2_p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_errors_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fps_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolution_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolution_changes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uploaded_bytes_p2_p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_id.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaybackMetricCreate::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_downloaded_bytes_http_isValid && m_downloaded_bytes_p2_p_isValid && m_errors_isValid && m_player_mode_isValid && m_resolution_changes_isValid && m_uploaded_bytes_p2_p_isValid && m_video_id_isValid && true;
}

} // namespace OpenAPI
