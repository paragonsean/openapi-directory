/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateNetworkSsidSplashSettings_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSsidSplashSettings_request::OAIUpdateNetworkSsidSplashSettings_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSsidSplashSettings_request::OAIUpdateNetworkSsidSplashSettings_request() {
    this->initializeModel();
}

OAIUpdateNetworkSsidSplashSettings_request::~OAIUpdateNetworkSsidSplashSettings_request() {}

void OAIUpdateNetworkSsidSplashSettings_request::initializeModel() {

    m_splash_url_isSet = false;
    m_splash_url_isValid = false;

    m_use_splash_url_isSet = false;
    m_use_splash_url_isValid = false;
}

void OAIUpdateNetworkSsidSplashSettings_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSsidSplashSettings_request::fromJsonObject(QJsonObject json) {

    m_splash_url_isValid = ::OpenAPI::fromJsonValue(m_splash_url, json[QString("splashUrl")]);
    m_splash_url_isSet = !json[QString("splashUrl")].isNull() && m_splash_url_isValid;

    m_use_splash_url_isValid = ::OpenAPI::fromJsonValue(m_use_splash_url, json[QString("useSplashUrl")]);
    m_use_splash_url_isSet = !json[QString("useSplashUrl")].isNull() && m_use_splash_url_isValid;
}

QString OAIUpdateNetworkSsidSplashSettings_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSsidSplashSettings_request::asJsonObject() const {
    QJsonObject obj;
    if (m_splash_url_isSet) {
        obj.insert(QString("splashUrl"), ::OpenAPI::toJsonValue(m_splash_url));
    }
    if (m_use_splash_url_isSet) {
        obj.insert(QString("useSplashUrl"), ::OpenAPI::toJsonValue(m_use_splash_url));
    }
    return obj;
}

QString OAIUpdateNetworkSsidSplashSettings_request::getSplashUrl() const {
    return m_splash_url;
}
void OAIUpdateNetworkSsidSplashSettings_request::setSplashUrl(const QString &splash_url) {
    m_splash_url = splash_url;
    m_splash_url_isSet = true;
}

bool OAIUpdateNetworkSsidSplashSettings_request::is_splash_url_Set() const{
    return m_splash_url_isSet;
}

bool OAIUpdateNetworkSsidSplashSettings_request::is_splash_url_Valid() const{
    return m_splash_url_isValid;
}

bool OAIUpdateNetworkSsidSplashSettings_request::isUseSplashUrl() const {
    return m_use_splash_url;
}
void OAIUpdateNetworkSsidSplashSettings_request::setUseSplashUrl(const bool &use_splash_url) {
    m_use_splash_url = use_splash_url;
    m_use_splash_url_isSet = true;
}

bool OAIUpdateNetworkSsidSplashSettings_request::is_use_splash_url_Set() const{
    return m_use_splash_url_isSet;
}

bool OAIUpdateNetworkSsidSplashSettings_request::is_use_splash_url_Valid() const{
    return m_use_splash_url_isValid;
}

bool OAIUpdateNetworkSsidSplashSettings_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_splash_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_splash_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSsidSplashSettings_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
