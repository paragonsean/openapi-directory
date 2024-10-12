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

#include "OAIVideoChannelSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoChannelSummary::OAIVideoChannelSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoChannelSummary::OAIVideoChannelSummary() {
    this->initializeModel();
}

OAIVideoChannelSummary::~OAIVideoChannelSummary() {}

void OAIVideoChannelSummary::initializeModel() {

    m_avatars_isSet = false;
    m_avatars_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_host_isSet = false;
    m_host_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIVideoChannelSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoChannelSummary::fromJsonObject(QJsonObject json) {

    m_avatars_isValid = ::OpenAPI::fromJsonValue(m_avatars, json[QString("avatars")]);
    m_avatars_isSet = !json[QString("avatars")].isNull() && m_avatars_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_host_isValid = ::OpenAPI::fromJsonValue(m_host, json[QString("host")]);
    m_host_isSet = !json[QString("host")].isNull() && m_host_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIVideoChannelSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoChannelSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_avatars.size() > 0) {
        obj.insert(QString("avatars"), ::OpenAPI::toJsonValue(m_avatars));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_host_isSet) {
        obj.insert(QString("host"), ::OpenAPI::toJsonValue(m_host));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QList<OAIActorImage> OAIVideoChannelSummary::getAvatars() const {
    return m_avatars;
}
void OAIVideoChannelSummary::setAvatars(const QList<OAIActorImage> &avatars) {
    m_avatars = avatars;
    m_avatars_isSet = true;
}

bool OAIVideoChannelSummary::is_avatars_Set() const{
    return m_avatars_isSet;
}

bool OAIVideoChannelSummary::is_avatars_Valid() const{
    return m_avatars_isValid;
}

QString OAIVideoChannelSummary::getDisplayName() const {
    return m_display_name;
}
void OAIVideoChannelSummary::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIVideoChannelSummary::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIVideoChannelSummary::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIVideoChannelSummary::getHost() const {
    return m_host;
}
void OAIVideoChannelSummary::setHost(const QString &host) {
    m_host = host;
    m_host_isSet = true;
}

bool OAIVideoChannelSummary::is_host_Set() const{
    return m_host_isSet;
}

bool OAIVideoChannelSummary::is_host_Valid() const{
    return m_host_isValid;
}

qint32 OAIVideoChannelSummary::getId() const {
    return m_id;
}
void OAIVideoChannelSummary::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoChannelSummary::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoChannelSummary::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVideoChannelSummary::getName() const {
    return m_name;
}
void OAIVideoChannelSummary::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVideoChannelSummary::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVideoChannelSummary::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIVideoChannelSummary::getUrl() const {
    return m_url;
}
void OAIVideoChannelSummary::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIVideoChannelSummary::is_url_Set() const{
    return m_url_isSet;
}

bool OAIVideoChannelSummary::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIVideoChannelSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_avatars.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_host_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIVideoChannelSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
