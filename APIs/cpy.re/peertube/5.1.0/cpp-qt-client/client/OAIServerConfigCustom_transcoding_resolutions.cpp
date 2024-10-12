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

#include "OAIServerConfigCustom_transcoding_resolutions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfigCustom_transcoding_resolutions::OAIServerConfigCustom_transcoding_resolutions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfigCustom_transcoding_resolutions::OAIServerConfigCustom_transcoding_resolutions() {
    this->initializeModel();
}

OAIServerConfigCustom_transcoding_resolutions::~OAIServerConfigCustom_transcoding_resolutions() {}

void OAIServerConfigCustom_transcoding_resolutions::initializeModel() {

    m_r_0p_isSet = false;
    m_r_0p_isValid = false;

    m_r_1080p_isSet = false;
    m_r_1080p_isValid = false;

    m_r_1440p_isSet = false;
    m_r_1440p_isValid = false;

    m_r_144p_isSet = false;
    m_r_144p_isValid = false;

    m_r_2160p_isSet = false;
    m_r_2160p_isValid = false;

    m_r_240p_isSet = false;
    m_r_240p_isValid = false;

    m_r_360p_isSet = false;
    m_r_360p_isValid = false;

    m_r_480p_isSet = false;
    m_r_480p_isValid = false;

    m_r_720p_isSet = false;
    m_r_720p_isValid = false;
}

void OAIServerConfigCustom_transcoding_resolutions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfigCustom_transcoding_resolutions::fromJsonObject(QJsonObject json) {

    m_r_0p_isValid = ::OpenAPI::fromJsonValue(m_r_0p, json[QString("0p")]);
    m_r_0p_isSet = !json[QString("0p")].isNull() && m_r_0p_isValid;

    m_r_1080p_isValid = ::OpenAPI::fromJsonValue(m_r_1080p, json[QString("1080p")]);
    m_r_1080p_isSet = !json[QString("1080p")].isNull() && m_r_1080p_isValid;

    m_r_1440p_isValid = ::OpenAPI::fromJsonValue(m_r_1440p, json[QString("1440p")]);
    m_r_1440p_isSet = !json[QString("1440p")].isNull() && m_r_1440p_isValid;

    m_r_144p_isValid = ::OpenAPI::fromJsonValue(m_r_144p, json[QString("144p")]);
    m_r_144p_isSet = !json[QString("144p")].isNull() && m_r_144p_isValid;

    m_r_2160p_isValid = ::OpenAPI::fromJsonValue(m_r_2160p, json[QString("2160p")]);
    m_r_2160p_isSet = !json[QString("2160p")].isNull() && m_r_2160p_isValid;

    m_r_240p_isValid = ::OpenAPI::fromJsonValue(m_r_240p, json[QString("240p")]);
    m_r_240p_isSet = !json[QString("240p")].isNull() && m_r_240p_isValid;

    m_r_360p_isValid = ::OpenAPI::fromJsonValue(m_r_360p, json[QString("360p")]);
    m_r_360p_isSet = !json[QString("360p")].isNull() && m_r_360p_isValid;

    m_r_480p_isValid = ::OpenAPI::fromJsonValue(m_r_480p, json[QString("480p")]);
    m_r_480p_isSet = !json[QString("480p")].isNull() && m_r_480p_isValid;

    m_r_720p_isValid = ::OpenAPI::fromJsonValue(m_r_720p, json[QString("720p")]);
    m_r_720p_isSet = !json[QString("720p")].isNull() && m_r_720p_isValid;
}

QString OAIServerConfigCustom_transcoding_resolutions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfigCustom_transcoding_resolutions::asJsonObject() const {
    QJsonObject obj;
    if (m_r_0p_isSet) {
        obj.insert(QString("0p"), ::OpenAPI::toJsonValue(m_r_0p));
    }
    if (m_r_1080p_isSet) {
        obj.insert(QString("1080p"), ::OpenAPI::toJsonValue(m_r_1080p));
    }
    if (m_r_1440p_isSet) {
        obj.insert(QString("1440p"), ::OpenAPI::toJsonValue(m_r_1440p));
    }
    if (m_r_144p_isSet) {
        obj.insert(QString("144p"), ::OpenAPI::toJsonValue(m_r_144p));
    }
    if (m_r_2160p_isSet) {
        obj.insert(QString("2160p"), ::OpenAPI::toJsonValue(m_r_2160p));
    }
    if (m_r_240p_isSet) {
        obj.insert(QString("240p"), ::OpenAPI::toJsonValue(m_r_240p));
    }
    if (m_r_360p_isSet) {
        obj.insert(QString("360p"), ::OpenAPI::toJsonValue(m_r_360p));
    }
    if (m_r_480p_isSet) {
        obj.insert(QString("480p"), ::OpenAPI::toJsonValue(m_r_480p));
    }
    if (m_r_720p_isSet) {
        obj.insert(QString("720p"), ::OpenAPI::toJsonValue(m_r_720p));
    }
    return obj;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR0p() const {
    return m_r_0p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR0p(const bool &r_0p) {
    m_r_0p = r_0p;
    m_r_0p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_0p_Set() const{
    return m_r_0p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_0p_Valid() const{
    return m_r_0p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR1080p() const {
    return m_r_1080p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR1080p(const bool &r_1080p) {
    m_r_1080p = r_1080p;
    m_r_1080p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_1080p_Set() const{
    return m_r_1080p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_1080p_Valid() const{
    return m_r_1080p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR1440p() const {
    return m_r_1440p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR1440p(const bool &r_1440p) {
    m_r_1440p = r_1440p;
    m_r_1440p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_1440p_Set() const{
    return m_r_1440p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_1440p_Valid() const{
    return m_r_1440p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR144p() const {
    return m_r_144p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR144p(const bool &r_144p) {
    m_r_144p = r_144p;
    m_r_144p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_144p_Set() const{
    return m_r_144p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_144p_Valid() const{
    return m_r_144p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR2160p() const {
    return m_r_2160p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR2160p(const bool &r_2160p) {
    m_r_2160p = r_2160p;
    m_r_2160p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_2160p_Set() const{
    return m_r_2160p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_2160p_Valid() const{
    return m_r_2160p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR240p() const {
    return m_r_240p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR240p(const bool &r_240p) {
    m_r_240p = r_240p;
    m_r_240p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_240p_Set() const{
    return m_r_240p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_240p_Valid() const{
    return m_r_240p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR360p() const {
    return m_r_360p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR360p(const bool &r_360p) {
    m_r_360p = r_360p;
    m_r_360p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_360p_Set() const{
    return m_r_360p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_360p_Valid() const{
    return m_r_360p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR480p() const {
    return m_r_480p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR480p(const bool &r_480p) {
    m_r_480p = r_480p;
    m_r_480p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_480p_Set() const{
    return m_r_480p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_480p_Valid() const{
    return m_r_480p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isR720p() const {
    return m_r_720p;
}
void OAIServerConfigCustom_transcoding_resolutions::setR720p(const bool &r_720p) {
    m_r_720p = r_720p;
    m_r_720p_isSet = true;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_720p_Set() const{
    return m_r_720p_isSet;
}

bool OAIServerConfigCustom_transcoding_resolutions::is_r_720p_Valid() const{
    return m_r_720p_isValid;
}

bool OAIServerConfigCustom_transcoding_resolutions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_0p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_1080p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_1440p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_144p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_2160p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_240p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_360p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_480p_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_720p_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerConfigCustom_transcoding_resolutions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
