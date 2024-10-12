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

#include "OAINotification_videoImport.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotification_videoImport::OAINotification_videoImport(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotification_videoImport::OAINotification_videoImport() {
    this->initializeModel();
}

OAINotification_videoImport::~OAINotification_videoImport() {}

void OAINotification_videoImport::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_magnet_uri_isSet = false;
    m_magnet_uri_isValid = false;

    m_target_uri_isSet = false;
    m_target_uri_isValid = false;

    m_torrent_name_isSet = false;
    m_torrent_name_isValid = false;

    m_video_isSet = false;
    m_video_isValid = false;
}

void OAINotification_videoImport::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotification_videoImport::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_magnet_uri_isValid = ::OpenAPI::fromJsonValue(m_magnet_uri, json[QString("magnetUri")]);
    m_magnet_uri_isSet = !json[QString("magnetUri")].isNull() && m_magnet_uri_isValid;

    m_target_uri_isValid = ::OpenAPI::fromJsonValue(m_target_uri, json[QString("targetUri")]);
    m_target_uri_isSet = !json[QString("targetUri")].isNull() && m_target_uri_isValid;

    m_torrent_name_isValid = ::OpenAPI::fromJsonValue(m_torrent_name, json[QString("torrentName")]);
    m_torrent_name_isSet = !json[QString("torrentName")].isNull() && m_torrent_name_isValid;

    m_video_isValid = ::OpenAPI::fromJsonValue(m_video, json[QString("video")]);
    m_video_isSet = !json[QString("video")].isNull() && m_video_isValid;
}

QString OAINotification_videoImport::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotification_videoImport::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_magnet_uri_isSet) {
        obj.insert(QString("magnetUri"), ::OpenAPI::toJsonValue(m_magnet_uri));
    }
    if (m_target_uri_isSet) {
        obj.insert(QString("targetUri"), ::OpenAPI::toJsonValue(m_target_uri));
    }
    if (m_torrent_name_isSet) {
        obj.insert(QString("torrentName"), ::OpenAPI::toJsonValue(m_torrent_name));
    }
    if (m_video.isSet()) {
        obj.insert(QString("video"), ::OpenAPI::toJsonValue(m_video));
    }
    return obj;
}

qint32 OAINotification_videoImport::getId() const {
    return m_id;
}
void OAINotification_videoImport::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAINotification_videoImport::is_id_Set() const{
    return m_id_isSet;
}

bool OAINotification_videoImport::is_id_Valid() const{
    return m_id_isValid;
}

QString OAINotification_videoImport::getMagnetUri() const {
    return m_magnet_uri;
}
void OAINotification_videoImport::setMagnetUri(const QString &magnet_uri) {
    m_magnet_uri = magnet_uri;
    m_magnet_uri_isSet = true;
}

bool OAINotification_videoImport::is_magnet_uri_Set() const{
    return m_magnet_uri_isSet;
}

bool OAINotification_videoImport::is_magnet_uri_Valid() const{
    return m_magnet_uri_isValid;
}

QString OAINotification_videoImport::getTargetUri() const {
    return m_target_uri;
}
void OAINotification_videoImport::setTargetUri(const QString &target_uri) {
    m_target_uri = target_uri;
    m_target_uri_isSet = true;
}

bool OAINotification_videoImport::is_target_uri_Set() const{
    return m_target_uri_isSet;
}

bool OAINotification_videoImport::is_target_uri_Valid() const{
    return m_target_uri_isValid;
}

QString OAINotification_videoImport::getTorrentName() const {
    return m_torrent_name;
}
void OAINotification_videoImport::setTorrentName(const QString &torrent_name) {
    m_torrent_name = torrent_name;
    m_torrent_name_isSet = true;
}

bool OAINotification_videoImport::is_torrent_name_Set() const{
    return m_torrent_name_isSet;
}

bool OAINotification_videoImport::is_torrent_name_Valid() const{
    return m_torrent_name_isValid;
}

OAIVideoInfo OAINotification_videoImport::getVideo() const {
    return m_video;
}
void OAINotification_videoImport::setVideo(const OAIVideoInfo &video) {
    m_video = video;
    m_video_isSet = true;
}

bool OAINotification_videoImport::is_video_Set() const{
    return m_video_isSet;
}

bool OAINotification_videoImport::is_video_Valid() const{
    return m_video_isValid;
}

bool OAINotification_videoImport::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_magnet_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_torrent_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotification_videoImport::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
