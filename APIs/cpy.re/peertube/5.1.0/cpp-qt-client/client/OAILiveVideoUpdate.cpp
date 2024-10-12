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

#include "OAILiveVideoUpdate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILiveVideoUpdate::OAILiveVideoUpdate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILiveVideoUpdate::OAILiveVideoUpdate() {
    this->initializeModel();
}

OAILiveVideoUpdate::~OAILiveVideoUpdate() {}

void OAILiveVideoUpdate::initializeModel() {

    m_latency_mode_isSet = false;
    m_latency_mode_isValid = false;

    m_permanent_live_isSet = false;
    m_permanent_live_isValid = false;

    m_replay_settings_isSet = false;
    m_replay_settings_isValid = false;

    m_save_replay_isSet = false;
    m_save_replay_isValid = false;
}

void OAILiveVideoUpdate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILiveVideoUpdate::fromJsonObject(QJsonObject json) {

    m_latency_mode_isValid = ::OpenAPI::fromJsonValue(m_latency_mode, json[QString("latencyMode")]);
    m_latency_mode_isSet = !json[QString("latencyMode")].isNull() && m_latency_mode_isValid;

    m_permanent_live_isValid = ::OpenAPI::fromJsonValue(m_permanent_live, json[QString("permanentLive")]);
    m_permanent_live_isSet = !json[QString("permanentLive")].isNull() && m_permanent_live_isValid;

    m_replay_settings_isValid = ::OpenAPI::fromJsonValue(m_replay_settings, json[QString("replaySettings")]);
    m_replay_settings_isSet = !json[QString("replaySettings")].isNull() && m_replay_settings_isValid;

    m_save_replay_isValid = ::OpenAPI::fromJsonValue(m_save_replay, json[QString("saveReplay")]);
    m_save_replay_isSet = !json[QString("saveReplay")].isNull() && m_save_replay_isValid;
}

QString OAILiveVideoUpdate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILiveVideoUpdate::asJsonObject() const {
    QJsonObject obj;
    if (m_latency_mode.isSet()) {
        obj.insert(QString("latencyMode"), ::OpenAPI::toJsonValue(m_latency_mode));
    }
    if (m_permanent_live_isSet) {
        obj.insert(QString("permanentLive"), ::OpenAPI::toJsonValue(m_permanent_live));
    }
    if (m_replay_settings.isSet()) {
        obj.insert(QString("replaySettings"), ::OpenAPI::toJsonValue(m_replay_settings));
    }
    if (m_save_replay_isSet) {
        obj.insert(QString("saveReplay"), ::OpenAPI::toJsonValue(m_save_replay));
    }
    return obj;
}

OAILiveVideoLatencyMode OAILiveVideoUpdate::getLatencyMode() const {
    return m_latency_mode;
}
void OAILiveVideoUpdate::setLatencyMode(const OAILiveVideoLatencyMode &latency_mode) {
    m_latency_mode = latency_mode;
    m_latency_mode_isSet = true;
}

bool OAILiveVideoUpdate::is_latency_mode_Set() const{
    return m_latency_mode_isSet;
}

bool OAILiveVideoUpdate::is_latency_mode_Valid() const{
    return m_latency_mode_isValid;
}

bool OAILiveVideoUpdate::isPermanentLive() const {
    return m_permanent_live;
}
void OAILiveVideoUpdate::setPermanentLive(const bool &permanent_live) {
    m_permanent_live = permanent_live;
    m_permanent_live_isSet = true;
}

bool OAILiveVideoUpdate::is_permanent_live_Set() const{
    return m_permanent_live_isSet;
}

bool OAILiveVideoUpdate::is_permanent_live_Valid() const{
    return m_permanent_live_isValid;
}

OAILiveVideoReplaySettings OAILiveVideoUpdate::getReplaySettings() const {
    return m_replay_settings;
}
void OAILiveVideoUpdate::setReplaySettings(const OAILiveVideoReplaySettings &replay_settings) {
    m_replay_settings = replay_settings;
    m_replay_settings_isSet = true;
}

bool OAILiveVideoUpdate::is_replay_settings_Set() const{
    return m_replay_settings_isSet;
}

bool OAILiveVideoUpdate::is_replay_settings_Valid() const{
    return m_replay_settings_isValid;
}

bool OAILiveVideoUpdate::isSaveReplay() const {
    return m_save_replay;
}
void OAILiveVideoUpdate::setSaveReplay(const bool &save_replay) {
    m_save_replay = save_replay;
    m_save_replay_isSet = true;
}

bool OAILiveVideoUpdate::is_save_replay_Set() const{
    return m_save_replay_isSet;
}

bool OAILiveVideoUpdate::is_save_replay_Valid() const{
    return m_save_replay_isValid;
}

bool OAILiveVideoUpdate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_latency_mode.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_permanent_live_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_replay_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_save_replay_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILiveVideoUpdate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
