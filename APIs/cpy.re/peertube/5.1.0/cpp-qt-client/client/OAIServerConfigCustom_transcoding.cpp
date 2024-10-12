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

#include "OAIServerConfigCustom_transcoding.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfigCustom_transcoding::OAIServerConfigCustom_transcoding(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfigCustom_transcoding::OAIServerConfigCustom_transcoding() {
    this->initializeModel();
}

OAIServerConfigCustom_transcoding::~OAIServerConfigCustom_transcoding() {}

void OAIServerConfigCustom_transcoding::initializeModel() {

    m_allow_additional_extensions_isSet = false;
    m_allow_additional_extensions_isValid = false;

    m_allow_audio_files_isSet = false;
    m_allow_audio_files_isValid = false;

    m_concurrency_isSet = false;
    m_concurrency_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_hls_isSet = false;
    m_hls_isValid = false;

    m_profile_isSet = false;
    m_profile_isValid = false;

    m_resolutions_isSet = false;
    m_resolutions_isValid = false;

    m_threads_isSet = false;
    m_threads_isValid = false;

    m_webtorrent_isSet = false;
    m_webtorrent_isValid = false;
}

void OAIServerConfigCustom_transcoding::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfigCustom_transcoding::fromJsonObject(QJsonObject json) {

    m_allow_additional_extensions_isValid = ::OpenAPI::fromJsonValue(m_allow_additional_extensions, json[QString("allowAdditionalExtensions")]);
    m_allow_additional_extensions_isSet = !json[QString("allowAdditionalExtensions")].isNull() && m_allow_additional_extensions_isValid;

    m_allow_audio_files_isValid = ::OpenAPI::fromJsonValue(m_allow_audio_files, json[QString("allowAudioFiles")]);
    m_allow_audio_files_isSet = !json[QString("allowAudioFiles")].isNull() && m_allow_audio_files_isValid;

    m_concurrency_isValid = ::OpenAPI::fromJsonValue(m_concurrency, json[QString("concurrency")]);
    m_concurrency_isSet = !json[QString("concurrency")].isNull() && m_concurrency_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_hls_isValid = ::OpenAPI::fromJsonValue(m_hls, json[QString("hls")]);
    m_hls_isSet = !json[QString("hls")].isNull() && m_hls_isValid;

    m_profile_isValid = ::OpenAPI::fromJsonValue(m_profile, json[QString("profile")]);
    m_profile_isSet = !json[QString("profile")].isNull() && m_profile_isValid;

    m_resolutions_isValid = ::OpenAPI::fromJsonValue(m_resolutions, json[QString("resolutions")]);
    m_resolutions_isSet = !json[QString("resolutions")].isNull() && m_resolutions_isValid;

    m_threads_isValid = ::OpenAPI::fromJsonValue(m_threads, json[QString("threads")]);
    m_threads_isSet = !json[QString("threads")].isNull() && m_threads_isValid;

    m_webtorrent_isValid = ::OpenAPI::fromJsonValue(m_webtorrent, json[QString("webtorrent")]);
    m_webtorrent_isSet = !json[QString("webtorrent")].isNull() && m_webtorrent_isValid;
}

QString OAIServerConfigCustom_transcoding::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfigCustom_transcoding::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_additional_extensions_isSet) {
        obj.insert(QString("allowAdditionalExtensions"), ::OpenAPI::toJsonValue(m_allow_additional_extensions));
    }
    if (m_allow_audio_files_isSet) {
        obj.insert(QString("allowAudioFiles"), ::OpenAPI::toJsonValue(m_allow_audio_files));
    }
    if (m_concurrency_isSet) {
        obj.insert(QString("concurrency"), ::OpenAPI::toJsonValue(m_concurrency));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_hls.isSet()) {
        obj.insert(QString("hls"), ::OpenAPI::toJsonValue(m_hls));
    }
    if (m_profile_isSet) {
        obj.insert(QString("profile"), ::OpenAPI::toJsonValue(m_profile));
    }
    if (m_resolutions.isSet()) {
        obj.insert(QString("resolutions"), ::OpenAPI::toJsonValue(m_resolutions));
    }
    if (m_threads_isSet) {
        obj.insert(QString("threads"), ::OpenAPI::toJsonValue(m_threads));
    }
    if (m_webtorrent.isSet()) {
        obj.insert(QString("webtorrent"), ::OpenAPI::toJsonValue(m_webtorrent));
    }
    return obj;
}

bool OAIServerConfigCustom_transcoding::isAllowAdditionalExtensions() const {
    return m_allow_additional_extensions;
}
void OAIServerConfigCustom_transcoding::setAllowAdditionalExtensions(const bool &allow_additional_extensions) {
    m_allow_additional_extensions = allow_additional_extensions;
    m_allow_additional_extensions_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_allow_additional_extensions_Set() const{
    return m_allow_additional_extensions_isSet;
}

bool OAIServerConfigCustom_transcoding::is_allow_additional_extensions_Valid() const{
    return m_allow_additional_extensions_isValid;
}

bool OAIServerConfigCustom_transcoding::isAllowAudioFiles() const {
    return m_allow_audio_files;
}
void OAIServerConfigCustom_transcoding::setAllowAudioFiles(const bool &allow_audio_files) {
    m_allow_audio_files = allow_audio_files;
    m_allow_audio_files_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_allow_audio_files_Set() const{
    return m_allow_audio_files_isSet;
}

bool OAIServerConfigCustom_transcoding::is_allow_audio_files_Valid() const{
    return m_allow_audio_files_isValid;
}

double OAIServerConfigCustom_transcoding::getConcurrency() const {
    return m_concurrency;
}
void OAIServerConfigCustom_transcoding::setConcurrency(const double &concurrency) {
    m_concurrency = concurrency;
    m_concurrency_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_concurrency_Set() const{
    return m_concurrency_isSet;
}

bool OAIServerConfigCustom_transcoding::is_concurrency_Valid() const{
    return m_concurrency_isValid;
}

bool OAIServerConfigCustom_transcoding::isEnabled() const {
    return m_enabled;
}
void OAIServerConfigCustom_transcoding::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIServerConfigCustom_transcoding::is_enabled_Valid() const{
    return m_enabled_isValid;
}

OAIServerConfigCustom_transcoding_hls OAIServerConfigCustom_transcoding::getHls() const {
    return m_hls;
}
void OAIServerConfigCustom_transcoding::setHls(const OAIServerConfigCustom_transcoding_hls &hls) {
    m_hls = hls;
    m_hls_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_hls_Set() const{
    return m_hls_isSet;
}

bool OAIServerConfigCustom_transcoding::is_hls_Valid() const{
    return m_hls_isValid;
}

QString OAIServerConfigCustom_transcoding::getProfile() const {
    return m_profile;
}
void OAIServerConfigCustom_transcoding::setProfile(const QString &profile) {
    m_profile = profile;
    m_profile_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_profile_Set() const{
    return m_profile_isSet;
}

bool OAIServerConfigCustom_transcoding::is_profile_Valid() const{
    return m_profile_isValid;
}

OAIServerConfigCustom_transcoding_resolutions OAIServerConfigCustom_transcoding::getResolutions() const {
    return m_resolutions;
}
void OAIServerConfigCustom_transcoding::setResolutions(const OAIServerConfigCustom_transcoding_resolutions &resolutions) {
    m_resolutions = resolutions;
    m_resolutions_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_resolutions_Set() const{
    return m_resolutions_isSet;
}

bool OAIServerConfigCustom_transcoding::is_resolutions_Valid() const{
    return m_resolutions_isValid;
}

qint32 OAIServerConfigCustom_transcoding::getThreads() const {
    return m_threads;
}
void OAIServerConfigCustom_transcoding::setThreads(const qint32 &threads) {
    m_threads = threads;
    m_threads_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_threads_Set() const{
    return m_threads_isSet;
}

bool OAIServerConfigCustom_transcoding::is_threads_Valid() const{
    return m_threads_isValid;
}

OAIServerConfigCustom_transcoding_webtorrent OAIServerConfigCustom_transcoding::getWebtorrent() const {
    return m_webtorrent;
}
void OAIServerConfigCustom_transcoding::setWebtorrent(const OAIServerConfigCustom_transcoding_webtorrent &webtorrent) {
    m_webtorrent = webtorrent;
    m_webtorrent_isSet = true;
}

bool OAIServerConfigCustom_transcoding::is_webtorrent_Set() const{
    return m_webtorrent_isSet;
}

bool OAIServerConfigCustom_transcoding::is_webtorrent_Valid() const{
    return m_webtorrent_isValid;
}

bool OAIServerConfigCustom_transcoding::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_additional_extensions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allow_audio_files_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_concurrency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hls.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolutions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_threads_isSet) {
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

bool OAIServerConfigCustom_transcoding::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
