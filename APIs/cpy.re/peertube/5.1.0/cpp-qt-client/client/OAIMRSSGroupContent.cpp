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

#include "OAIMRSSGroupContent.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMRSSGroupContent::OAIMRSSGroupContent(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMRSSGroupContent::OAIMRSSGroupContent() {
    this->initializeModel();
}

OAIMRSSGroupContent::~OAIMRSSGroupContent() {}

void OAIMRSSGroupContent::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_file_size_isSet = false;
    m_file_size_isValid = false;

    m_framerate_isSet = false;
    m_framerate_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_lang_isSet = false;
    m_lang_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIMRSSGroupContent::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMRSSGroupContent::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_file_size_isValid = ::OpenAPI::fromJsonValue(m_file_size, json[QString("fileSize")]);
    m_file_size_isSet = !json[QString("fileSize")].isNull() && m_file_size_isValid;

    m_framerate_isValid = ::OpenAPI::fromJsonValue(m_framerate, json[QString("framerate")]);
    m_framerate_isSet = !json[QString("framerate")].isNull() && m_framerate_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_lang_isValid = ::OpenAPI::fromJsonValue(m_lang, json[QString("lang")]);
    m_lang_isSet = !json[QString("lang")].isNull() && m_lang_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIMRSSGroupContent::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMRSSGroupContent::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_file_size_isSet) {
        obj.insert(QString("fileSize"), ::OpenAPI::toJsonValue(m_file_size));
    }
    if (m_framerate_isSet) {
        obj.insert(QString("framerate"), ::OpenAPI::toJsonValue(m_framerate));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_lang_isSet) {
        obj.insert(QString("lang"), ::OpenAPI::toJsonValue(m_lang));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

qint32 OAIMRSSGroupContent::getDuration() const {
    return m_duration;
}
void OAIMRSSGroupContent::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIMRSSGroupContent::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIMRSSGroupContent::is_duration_Valid() const{
    return m_duration_isValid;
}

qint32 OAIMRSSGroupContent::getFileSize() const {
    return m_file_size;
}
void OAIMRSSGroupContent::setFileSize(const qint32 &file_size) {
    m_file_size = file_size;
    m_file_size_isSet = true;
}

bool OAIMRSSGroupContent::is_file_size_Set() const{
    return m_file_size_isSet;
}

bool OAIMRSSGroupContent::is_file_size_Valid() const{
    return m_file_size_isValid;
}

qint32 OAIMRSSGroupContent::getFramerate() const {
    return m_framerate;
}
void OAIMRSSGroupContent::setFramerate(const qint32 &framerate) {
    m_framerate = framerate;
    m_framerate_isSet = true;
}

bool OAIMRSSGroupContent::is_framerate_Set() const{
    return m_framerate_isSet;
}

bool OAIMRSSGroupContent::is_framerate_Valid() const{
    return m_framerate_isValid;
}

qint32 OAIMRSSGroupContent::getHeight() const {
    return m_height;
}
void OAIMRSSGroupContent::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIMRSSGroupContent::is_height_Set() const{
    return m_height_isSet;
}

bool OAIMRSSGroupContent::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIMRSSGroupContent::getLang() const {
    return m_lang;
}
void OAIMRSSGroupContent::setLang(const QString &lang) {
    m_lang = lang;
    m_lang_isSet = true;
}

bool OAIMRSSGroupContent::is_lang_Set() const{
    return m_lang_isSet;
}

bool OAIMRSSGroupContent::is_lang_Valid() const{
    return m_lang_isValid;
}

QString OAIMRSSGroupContent::getType() const {
    return m_type;
}
void OAIMRSSGroupContent::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIMRSSGroupContent::is_type_Set() const{
    return m_type_isSet;
}

bool OAIMRSSGroupContent::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIMRSSGroupContent::getUrl() const {
    return m_url;
}
void OAIMRSSGroupContent::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIMRSSGroupContent::is_url_Set() const{
    return m_url_isSet;
}

bool OAIMRSSGroupContent::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIMRSSGroupContent::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_framerate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lang_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMRSSGroupContent::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
