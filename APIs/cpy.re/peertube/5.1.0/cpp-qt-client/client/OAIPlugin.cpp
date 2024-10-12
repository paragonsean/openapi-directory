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

#include "OAIPlugin.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlugin::OAIPlugin(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlugin::OAIPlugin() {
    this->initializeModel();
}

OAIPlugin::~OAIPlugin() {}

void OAIPlugin::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_homepage_isSet = false;
    m_homepage_isValid = false;

    m_latest_version_isSet = false;
    m_latest_version_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_peertube_engine_isSet = false;
    m_peertube_engine_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_uninstalled_isSet = false;
    m_uninstalled_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIPlugin::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlugin::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_homepage_isValid = ::OpenAPI::fromJsonValue(m_homepage, json[QString("homepage")]);
    m_homepage_isSet = !json[QString("homepage")].isNull() && m_homepage_isValid;

    m_latest_version_isValid = ::OpenAPI::fromJsonValue(m_latest_version, json[QString("latestVersion")]);
    m_latest_version_isSet = !json[QString("latestVersion")].isNull() && m_latest_version_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_peertube_engine_isValid = ::OpenAPI::fromJsonValue(m_peertube_engine, json[QString("peertubeEngine")]);
    m_peertube_engine_isSet = !json[QString("peertubeEngine")].isNull() && m_peertube_engine_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_uninstalled_isValid = ::OpenAPI::fromJsonValue(m_uninstalled, json[QString("uninstalled")]);
    m_uninstalled_isSet = !json[QString("uninstalled")].isNull() && m_uninstalled_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIPlugin::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlugin::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_homepage_isSet) {
        obj.insert(QString("homepage"), ::OpenAPI::toJsonValue(m_homepage));
    }
    if (m_latest_version_isSet) {
        obj.insert(QString("latestVersion"), ::OpenAPI::toJsonValue(m_latest_version));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_peertube_engine_isSet) {
        obj.insert(QString("peertubeEngine"), ::OpenAPI::toJsonValue(m_peertube_engine));
    }
    if (m_settings.size() > 0) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_uninstalled_isSet) {
        obj.insert(QString("uninstalled"), ::OpenAPI::toJsonValue(m_uninstalled));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QDateTime OAIPlugin::getCreatedAt() const {
    return m_created_at;
}
void OAIPlugin::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIPlugin::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIPlugin::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIPlugin::getDescription() const {
    return m_description;
}
void OAIPlugin::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPlugin::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPlugin::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIPlugin::isEnabled() const {
    return m_enabled;
}
void OAIPlugin::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIPlugin::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIPlugin::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIPlugin::getHomepage() const {
    return m_homepage;
}
void OAIPlugin::setHomepage(const QString &homepage) {
    m_homepage = homepage;
    m_homepage_isSet = true;
}

bool OAIPlugin::is_homepage_Set() const{
    return m_homepage_isSet;
}

bool OAIPlugin::is_homepage_Valid() const{
    return m_homepage_isValid;
}

QString OAIPlugin::getLatestVersion() const {
    return m_latest_version;
}
void OAIPlugin::setLatestVersion(const QString &latest_version) {
    m_latest_version = latest_version;
    m_latest_version_isSet = true;
}

bool OAIPlugin::is_latest_version_Set() const{
    return m_latest_version_isSet;
}

bool OAIPlugin::is_latest_version_Valid() const{
    return m_latest_version_isValid;
}

QString OAIPlugin::getName() const {
    return m_name;
}
void OAIPlugin::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPlugin::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPlugin::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIPlugin::getPeertubeEngine() const {
    return m_peertube_engine;
}
void OAIPlugin::setPeertubeEngine(const QString &peertube_engine) {
    m_peertube_engine = peertube_engine;
    m_peertube_engine_isSet = true;
}

bool OAIPlugin::is_peertube_engine_Set() const{
    return m_peertube_engine_isSet;
}

bool OAIPlugin::is_peertube_engine_Valid() const{
    return m_peertube_engine_isValid;
}

QMap<QString, QJsonValue> OAIPlugin::getSettings() const {
    return m_settings;
}
void OAIPlugin::setSettings(const QMap<QString, QJsonValue> &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAIPlugin::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAIPlugin::is_settings_Valid() const{
    return m_settings_isValid;
}

qint32 OAIPlugin::getType() const {
    return m_type;
}
void OAIPlugin::setType(const qint32 &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPlugin::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPlugin::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPlugin::isUninstalled() const {
    return m_uninstalled;
}
void OAIPlugin::setUninstalled(const bool &uninstalled) {
    m_uninstalled = uninstalled;
    m_uninstalled_isSet = true;
}

bool OAIPlugin::is_uninstalled_Set() const{
    return m_uninstalled_isSet;
}

bool OAIPlugin::is_uninstalled_Valid() const{
    return m_uninstalled_isValid;
}

QDateTime OAIPlugin::getUpdatedAt() const {
    return m_updated_at;
}
void OAIPlugin::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIPlugin::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIPlugin::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIPlugin::getVersion() const {
    return m_version;
}
void OAIPlugin::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIPlugin::is_version_Set() const{
    return m_version_isSet;
}

bool OAIPlugin::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIPlugin::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_homepage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latest_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_peertube_engine_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uninstalled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlugin::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
