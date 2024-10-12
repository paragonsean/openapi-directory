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

#include "OAIServerStats_videosRedundancy_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerStats_videosRedundancy_inner::OAIServerStats_videosRedundancy_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerStats_videosRedundancy_inner::OAIServerStats_videosRedundancy_inner() {
    this->initializeModel();
}

OAIServerStats_videosRedundancy_inner::~OAIServerStats_videosRedundancy_inner() {}

void OAIServerStats_videosRedundancy_inner::initializeModel() {

    m_strategy_isSet = false;
    m_strategy_isValid = false;

    m_total_size_isSet = false;
    m_total_size_isValid = false;

    m_total_used_isSet = false;
    m_total_used_isValid = false;

    m_total_video_files_isSet = false;
    m_total_video_files_isValid = false;

    m_total_videos_isSet = false;
    m_total_videos_isValid = false;
}

void OAIServerStats_videosRedundancy_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerStats_videosRedundancy_inner::fromJsonObject(QJsonObject json) {

    m_strategy_isValid = ::OpenAPI::fromJsonValue(m_strategy, json[QString("strategy")]);
    m_strategy_isSet = !json[QString("strategy")].isNull() && m_strategy_isValid;

    m_total_size_isValid = ::OpenAPI::fromJsonValue(m_total_size, json[QString("totalSize")]);
    m_total_size_isSet = !json[QString("totalSize")].isNull() && m_total_size_isValid;

    m_total_used_isValid = ::OpenAPI::fromJsonValue(m_total_used, json[QString("totalUsed")]);
    m_total_used_isSet = !json[QString("totalUsed")].isNull() && m_total_used_isValid;

    m_total_video_files_isValid = ::OpenAPI::fromJsonValue(m_total_video_files, json[QString("totalVideoFiles")]);
    m_total_video_files_isSet = !json[QString("totalVideoFiles")].isNull() && m_total_video_files_isValid;

    m_total_videos_isValid = ::OpenAPI::fromJsonValue(m_total_videos, json[QString("totalVideos")]);
    m_total_videos_isSet = !json[QString("totalVideos")].isNull() && m_total_videos_isValid;
}

QString OAIServerStats_videosRedundancy_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerStats_videosRedundancy_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_strategy_isSet) {
        obj.insert(QString("strategy"), ::OpenAPI::toJsonValue(m_strategy));
    }
    if (m_total_size_isSet) {
        obj.insert(QString("totalSize"), ::OpenAPI::toJsonValue(m_total_size));
    }
    if (m_total_used_isSet) {
        obj.insert(QString("totalUsed"), ::OpenAPI::toJsonValue(m_total_used));
    }
    if (m_total_video_files_isSet) {
        obj.insert(QString("totalVideoFiles"), ::OpenAPI::toJsonValue(m_total_video_files));
    }
    if (m_total_videos_isSet) {
        obj.insert(QString("totalVideos"), ::OpenAPI::toJsonValue(m_total_videos));
    }
    return obj;
}

QString OAIServerStats_videosRedundancy_inner::getStrategy() const {
    return m_strategy;
}
void OAIServerStats_videosRedundancy_inner::setStrategy(const QString &strategy) {
    m_strategy = strategy;
    m_strategy_isSet = true;
}

bool OAIServerStats_videosRedundancy_inner::is_strategy_Set() const{
    return m_strategy_isSet;
}

bool OAIServerStats_videosRedundancy_inner::is_strategy_Valid() const{
    return m_strategy_isValid;
}

double OAIServerStats_videosRedundancy_inner::getTotalSize() const {
    return m_total_size;
}
void OAIServerStats_videosRedundancy_inner::setTotalSize(const double &total_size) {
    m_total_size = total_size;
    m_total_size_isSet = true;
}

bool OAIServerStats_videosRedundancy_inner::is_total_size_Set() const{
    return m_total_size_isSet;
}

bool OAIServerStats_videosRedundancy_inner::is_total_size_Valid() const{
    return m_total_size_isValid;
}

double OAIServerStats_videosRedundancy_inner::getTotalUsed() const {
    return m_total_used;
}
void OAIServerStats_videosRedundancy_inner::setTotalUsed(const double &total_used) {
    m_total_used = total_used;
    m_total_used_isSet = true;
}

bool OAIServerStats_videosRedundancy_inner::is_total_used_Set() const{
    return m_total_used_isSet;
}

bool OAIServerStats_videosRedundancy_inner::is_total_used_Valid() const{
    return m_total_used_isValid;
}

double OAIServerStats_videosRedundancy_inner::getTotalVideoFiles() const {
    return m_total_video_files;
}
void OAIServerStats_videosRedundancy_inner::setTotalVideoFiles(const double &total_video_files) {
    m_total_video_files = total_video_files;
    m_total_video_files_isSet = true;
}

bool OAIServerStats_videosRedundancy_inner::is_total_video_files_Set() const{
    return m_total_video_files_isSet;
}

bool OAIServerStats_videosRedundancy_inner::is_total_video_files_Valid() const{
    return m_total_video_files_isValid;
}

double OAIServerStats_videosRedundancy_inner::getTotalVideos() const {
    return m_total_videos;
}
void OAIServerStats_videosRedundancy_inner::setTotalVideos(const double &total_videos) {
    m_total_videos = total_videos;
    m_total_videos_isSet = true;
}

bool OAIServerStats_videosRedundancy_inner::is_total_videos_Set() const{
    return m_total_videos_isSet;
}

bool OAIServerStats_videosRedundancy_inner::is_total_videos_Valid() const{
    return m_total_videos_isValid;
}

bool OAIServerStats_videosRedundancy_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_strategy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_used_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_video_files_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_videos_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerStats_videosRedundancy_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
