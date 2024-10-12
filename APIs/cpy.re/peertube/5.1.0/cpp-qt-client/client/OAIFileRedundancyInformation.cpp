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

#include "OAIFileRedundancyInformation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFileRedundancyInformation::OAIFileRedundancyInformation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFileRedundancyInformation::OAIFileRedundancyInformation() {
    this->initializeModel();
}

OAIFileRedundancyInformation::~OAIFileRedundancyInformation() {}

void OAIFileRedundancyInformation::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_expires_on_isSet = false;
    m_expires_on_isValid = false;

    m_file_url_isSet = false;
    m_file_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_strategy_isSet = false;
    m_strategy_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIFileRedundancyInformation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFileRedundancyInformation::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_expires_on_isValid = ::OpenAPI::fromJsonValue(m_expires_on, json[QString("expiresOn")]);
    m_expires_on_isSet = !json[QString("expiresOn")].isNull() && m_expires_on_isValid;

    m_file_url_isValid = ::OpenAPI::fromJsonValue(m_file_url, json[QString("fileUrl")]);
    m_file_url_isSet = !json[QString("fileUrl")].isNull() && m_file_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_strategy_isValid = ::OpenAPI::fromJsonValue(m_strategy, json[QString("strategy")]);
    m_strategy_isSet = !json[QString("strategy")].isNull() && m_strategy_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;
}

QString OAIFileRedundancyInformation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFileRedundancyInformation::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_expires_on_isSet) {
        obj.insert(QString("expiresOn"), ::OpenAPI::toJsonValue(m_expires_on));
    }
    if (m_file_url_isSet) {
        obj.insert(QString("fileUrl"), ::OpenAPI::toJsonValue(m_file_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_strategy_isSet) {
        obj.insert(QString("strategy"), ::OpenAPI::toJsonValue(m_strategy));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QDateTime OAIFileRedundancyInformation::getCreatedAt() const {
    return m_created_at;
}
void OAIFileRedundancyInformation::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIFileRedundancyInformation::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIFileRedundancyInformation::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QDateTime OAIFileRedundancyInformation::getExpiresOn() const {
    return m_expires_on;
}
void OAIFileRedundancyInformation::setExpiresOn(const QDateTime &expires_on) {
    m_expires_on = expires_on;
    m_expires_on_isSet = true;
}

bool OAIFileRedundancyInformation::is_expires_on_Set() const{
    return m_expires_on_isSet;
}

bool OAIFileRedundancyInformation::is_expires_on_Valid() const{
    return m_expires_on_isValid;
}

QString OAIFileRedundancyInformation::getFileUrl() const {
    return m_file_url;
}
void OAIFileRedundancyInformation::setFileUrl(const QString &file_url) {
    m_file_url = file_url;
    m_file_url_isSet = true;
}

bool OAIFileRedundancyInformation::is_file_url_Set() const{
    return m_file_url_isSet;
}

bool OAIFileRedundancyInformation::is_file_url_Valid() const{
    return m_file_url_isValid;
}

qint32 OAIFileRedundancyInformation::getId() const {
    return m_id;
}
void OAIFileRedundancyInformation::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFileRedundancyInformation::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFileRedundancyInformation::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIFileRedundancyInformation::getSize() const {
    return m_size;
}
void OAIFileRedundancyInformation::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIFileRedundancyInformation::is_size_Set() const{
    return m_size_isSet;
}

bool OAIFileRedundancyInformation::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIFileRedundancyInformation::getStrategy() const {
    return m_strategy;
}
void OAIFileRedundancyInformation::setStrategy(const QString &strategy) {
    m_strategy = strategy;
    m_strategy_isSet = true;
}

bool OAIFileRedundancyInformation::is_strategy_Set() const{
    return m_strategy_isSet;
}

bool OAIFileRedundancyInformation::is_strategy_Valid() const{
    return m_strategy_isValid;
}

QDateTime OAIFileRedundancyInformation::getUpdatedAt() const {
    return m_updated_at;
}
void OAIFileRedundancyInformation::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIFileRedundancyInformation::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIFileRedundancyInformation::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIFileRedundancyInformation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_strategy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFileRedundancyInformation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
