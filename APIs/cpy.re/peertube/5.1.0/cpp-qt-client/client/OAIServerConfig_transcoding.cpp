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

#include "OAIServerConfig_transcoding.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfig_transcoding::OAIServerConfig_transcoding(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfig_transcoding::OAIServerConfig_transcoding() {
    this->initializeModel();
}

OAIServerConfig_transcoding::~OAIServerConfig_transcoding() {}

void OAIServerConfig_transcoding::initializeModel() {

    m_enabled_resolutions_isSet = false;
    m_enabled_resolutions_isValid = false;

    m_hls_isSet = false;
    m_hls_isValid = false;

    m_webtorrent_isSet = false;
    m_webtorrent_isValid = false;
}

void OAIServerConfig_transcoding::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfig_transcoding::fromJsonObject(QJsonObject json) {

    m_enabled_resolutions_isValid = ::OpenAPI::fromJsonValue(m_enabled_resolutions, json[QString("enabledResolutions")]);
    m_enabled_resolutions_isSet = !json[QString("enabledResolutions")].isNull() && m_enabled_resolutions_isValid;

    m_hls_isValid = ::OpenAPI::fromJsonValue(m_hls, json[QString("hls")]);
    m_hls_isSet = !json[QString("hls")].isNull() && m_hls_isValid;

    m_webtorrent_isValid = ::OpenAPI::fromJsonValue(m_webtorrent, json[QString("webtorrent")]);
    m_webtorrent_isSet = !json[QString("webtorrent")].isNull() && m_webtorrent_isValid;
}

QString OAIServerConfig_transcoding::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfig_transcoding::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_resolutions.size() > 0) {
        obj.insert(QString("enabledResolutions"), ::OpenAPI::toJsonValue(m_enabled_resolutions));
    }
    if (m_hls.isSet()) {
        obj.insert(QString("hls"), ::OpenAPI::toJsonValue(m_hls));
    }
    if (m_webtorrent.isSet()) {
        obj.insert(QString("webtorrent"), ::OpenAPI::toJsonValue(m_webtorrent));
    }
    return obj;
}

QList<qint32> OAIServerConfig_transcoding::getEnabledResolutions() const {
    return m_enabled_resolutions;
}
void OAIServerConfig_transcoding::setEnabledResolutions(const QList<qint32> &enabled_resolutions) {
    m_enabled_resolutions = enabled_resolutions;
    m_enabled_resolutions_isSet = true;
}

bool OAIServerConfig_transcoding::is_enabled_resolutions_Set() const{
    return m_enabled_resolutions_isSet;
}

bool OAIServerConfig_transcoding::is_enabled_resolutions_Valid() const{
    return m_enabled_resolutions_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfig_transcoding::getHls() const {
    return m_hls;
}
void OAIServerConfig_transcoding::setHls(const OAIServerConfig_autoBlacklist_videos_ofUsers &hls) {
    m_hls = hls;
    m_hls_isSet = true;
}

bool OAIServerConfig_transcoding::is_hls_Set() const{
    return m_hls_isSet;
}

bool OAIServerConfig_transcoding::is_hls_Valid() const{
    return m_hls_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfig_transcoding::getWebtorrent() const {
    return m_webtorrent;
}
void OAIServerConfig_transcoding::setWebtorrent(const OAIServerConfig_autoBlacklist_videos_ofUsers &webtorrent) {
    m_webtorrent = webtorrent;
    m_webtorrent_isSet = true;
}

bool OAIServerConfig_transcoding::is_webtorrent_Set() const{
    return m_webtorrent_isSet;
}

bool OAIServerConfig_transcoding::is_webtorrent_Valid() const{
    return m_webtorrent_isValid;
}

bool OAIServerConfig_transcoding::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_resolutions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hls.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_webtorrent.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerConfig_transcoding::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
