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

#include "OAIVideoChannelSync.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoChannelSync::OAIVideoChannelSync(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoChannelSync::OAIVideoChannelSync() {
    this->initializeModel();
}

OAIVideoChannelSync::~OAIVideoChannelSync() {}

void OAIVideoChannelSync::initializeModel() {

    m_channel_isSet = false;
    m_channel_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_external_channel_url_isSet = false;
    m_external_channel_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_sync_at_isSet = false;
    m_last_sync_at_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIVideoChannelSync::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoChannelSync::fromJsonObject(QJsonObject json) {

    m_channel_isValid = ::OpenAPI::fromJsonValue(m_channel, json[QString("channel")]);
    m_channel_isSet = !json[QString("channel")].isNull() && m_channel_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_external_channel_url_isValid = ::OpenAPI::fromJsonValue(m_external_channel_url, json[QString("externalChannelUrl")]);
    m_external_channel_url_isSet = !json[QString("externalChannelUrl")].isNull() && m_external_channel_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_sync_at_isValid = ::OpenAPI::fromJsonValue(m_last_sync_at, json[QString("lastSyncAt")]);
    m_last_sync_at_isSet = !json[QString("lastSyncAt")].isNull() && m_last_sync_at_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIVideoChannelSync::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoChannelSync::asJsonObject() const {
    QJsonObject obj;
    if (m_channel.isSet()) {
        obj.insert(QString("channel"), ::OpenAPI::toJsonValue(m_channel));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_external_channel_url_isSet) {
        obj.insert(QString("externalChannelUrl"), ::OpenAPI::toJsonValue(m_external_channel_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_sync_at_isSet) {
        obj.insert(QString("lastSyncAt"), ::OpenAPI::toJsonValue(m_last_sync_at));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

OAIVideoChannel OAIVideoChannelSync::getChannel() const {
    return m_channel;
}
void OAIVideoChannelSync::setChannel(const OAIVideoChannel &channel) {
    m_channel = channel;
    m_channel_isSet = true;
}

bool OAIVideoChannelSync::is_channel_Set() const{
    return m_channel_isSet;
}

bool OAIVideoChannelSync::is_channel_Valid() const{
    return m_channel_isValid;
}

QDateTime OAIVideoChannelSync::getCreatedAt() const {
    return m_created_at;
}
void OAIVideoChannelSync::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideoChannelSync::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideoChannelSync::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIVideoChannelSync::getExternalChannelUrl() const {
    return m_external_channel_url;
}
void OAIVideoChannelSync::setExternalChannelUrl(const QString &external_channel_url) {
    m_external_channel_url = external_channel_url;
    m_external_channel_url_isSet = true;
}

bool OAIVideoChannelSync::is_external_channel_url_Set() const{
    return m_external_channel_url_isSet;
}

bool OAIVideoChannelSync::is_external_channel_url_Valid() const{
    return m_external_channel_url_isValid;
}

qint32 OAIVideoChannelSync::getId() const {
    return m_id;
}
void OAIVideoChannelSync::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoChannelSync::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoChannelSync::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIVideoChannelSync::getLastSyncAt() const {
    return m_last_sync_at;
}
void OAIVideoChannelSync::setLastSyncAt(const QDateTime &last_sync_at) {
    m_last_sync_at = last_sync_at;
    m_last_sync_at_isSet = true;
}

bool OAIVideoChannelSync::is_last_sync_at_Set() const{
    return m_last_sync_at_isSet;
}

bool OAIVideoChannelSync::is_last_sync_at_Valid() const{
    return m_last_sync_at_isValid;
}

OAIVideoChannelSync_state OAIVideoChannelSync::getState() const {
    return m_state;
}
void OAIVideoChannelSync::setState(const OAIVideoChannelSync_state &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIVideoChannelSync::is_state_Set() const{
    return m_state_isSet;
}

bool OAIVideoChannelSync::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIVideoChannelSync::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_channel.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_channel_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_sync_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoChannelSync::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
