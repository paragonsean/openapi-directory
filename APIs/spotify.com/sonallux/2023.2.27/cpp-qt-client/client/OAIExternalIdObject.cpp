/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExternalIdObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExternalIdObject::OAIExternalIdObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExternalIdObject::OAIExternalIdObject() {
    this->initializeModel();
}

OAIExternalIdObject::~OAIExternalIdObject() {}

void OAIExternalIdObject::initializeModel() {

    m_ean_isSet = false;
    m_ean_isValid = false;

    m_isrc_isSet = false;
    m_isrc_isValid = false;

    m_upc_isSet = false;
    m_upc_isValid = false;
}

void OAIExternalIdObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExternalIdObject::fromJsonObject(QJsonObject json) {

    m_ean_isValid = ::OpenAPI::fromJsonValue(m_ean, json[QString("ean")]);
    m_ean_isSet = !json[QString("ean")].isNull() && m_ean_isValid;

    m_isrc_isValid = ::OpenAPI::fromJsonValue(m_isrc, json[QString("isrc")]);
    m_isrc_isSet = !json[QString("isrc")].isNull() && m_isrc_isValid;

    m_upc_isValid = ::OpenAPI::fromJsonValue(m_upc, json[QString("upc")]);
    m_upc_isSet = !json[QString("upc")].isNull() && m_upc_isValid;
}

QString OAIExternalIdObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExternalIdObject::asJsonObject() const {
    QJsonObject obj;
    if (m_ean_isSet) {
        obj.insert(QString("ean"), ::OpenAPI::toJsonValue(m_ean));
    }
    if (m_isrc_isSet) {
        obj.insert(QString("isrc"), ::OpenAPI::toJsonValue(m_isrc));
    }
    if (m_upc_isSet) {
        obj.insert(QString("upc"), ::OpenAPI::toJsonValue(m_upc));
    }
    return obj;
}

QString OAIExternalIdObject::getEan() const {
    return m_ean;
}
void OAIExternalIdObject::setEan(const QString &ean) {
    m_ean = ean;
    m_ean_isSet = true;
}

bool OAIExternalIdObject::is_ean_Set() const{
    return m_ean_isSet;
}

bool OAIExternalIdObject::is_ean_Valid() const{
    return m_ean_isValid;
}

QString OAIExternalIdObject::getIsrc() const {
    return m_isrc;
}
void OAIExternalIdObject::setIsrc(const QString &isrc) {
    m_isrc = isrc;
    m_isrc_isSet = true;
}

bool OAIExternalIdObject::is_isrc_Set() const{
    return m_isrc_isSet;
}

bool OAIExternalIdObject::is_isrc_Valid() const{
    return m_isrc_isValid;
}

QString OAIExternalIdObject::getUpc() const {
    return m_upc;
}
void OAIExternalIdObject::setUpc(const QString &upc) {
    m_upc = upc;
    m_upc_isSet = true;
}

bool OAIExternalIdObject::is_upc_Set() const{
    return m_upc_isSet;
}

bool OAIExternalIdObject::is_upc_Valid() const{
    return m_upc_isValid;
}

bool OAIExternalIdObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ean_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_isrc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upc_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExternalIdObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
