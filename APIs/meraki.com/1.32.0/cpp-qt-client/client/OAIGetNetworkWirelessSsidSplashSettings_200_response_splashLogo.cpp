/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo() {
    this->initializeModel();
}

OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::~OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo() {}

void OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::initializeModel() {

    m_extension_isSet = false;
    m_extension_isValid = false;

    m_md5_isSet = false;
    m_md5_isValid = false;
}

void OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::fromJsonObject(QJsonObject json) {

    m_extension_isValid = ::OpenAPI::fromJsonValue(m_extension, json[QString("extension")]);
    m_extension_isSet = !json[QString("extension")].isNull() && m_extension_isValid;

    m_md5_isValid = ::OpenAPI::fromJsonValue(m_md5, json[QString("md5")]);
    m_md5_isSet = !json[QString("md5")].isNull() && m_md5_isValid;
}

QString OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::asJsonObject() const {
    QJsonObject obj;
    if (m_extension_isSet) {
        obj.insert(QString("extension"), ::OpenAPI::toJsonValue(m_extension));
    }
    if (m_md5_isSet) {
        obj.insert(QString("md5"), ::OpenAPI::toJsonValue(m_md5));
    }
    return obj;
}

QString OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::getExtension() const {
    return m_extension;
}
void OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::setExtension(const QString &extension) {
    m_extension = extension;
    m_extension_isSet = true;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::is_extension_Set() const{
    return m_extension_isSet;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::is_extension_Valid() const{
    return m_extension_isValid;
}

QString OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::getMd5() const {
    return m_md5;
}
void OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::setMd5(const QString &md5) {
    m_md5 = md5;
    m_md5_isSet = true;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::is_md5_Set() const{
    return m_md5_isSet;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::is_md5_Valid() const{
    return m_md5_isValid;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_md5_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_splashLogo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
