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

#include "OAIUpdateNetworkClientSplashAuthorizationStatus_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkClientSplashAuthorizationStatus_request::OAIUpdateNetworkClientSplashAuthorizationStatus_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkClientSplashAuthorizationStatus_request::OAIUpdateNetworkClientSplashAuthorizationStatus_request() {
    this->initializeModel();
}

OAIUpdateNetworkClientSplashAuthorizationStatus_request::~OAIUpdateNetworkClientSplashAuthorizationStatus_request() {}

void OAIUpdateNetworkClientSplashAuthorizationStatus_request::initializeModel() {

    m_ssids_isSet = false;
    m_ssids_isValid = false;
}

void OAIUpdateNetworkClientSplashAuthorizationStatus_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkClientSplashAuthorizationStatus_request::fromJsonObject(QJsonObject json) {

    m_ssids_isValid = ::OpenAPI::fromJsonValue(m_ssids, json[QString("ssids")]);
    m_ssids_isSet = !json[QString("ssids")].isNull() && m_ssids_isValid;
}

QString OAIUpdateNetworkClientSplashAuthorizationStatus_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkClientSplashAuthorizationStatus_request::asJsonObject() const {
    QJsonObject obj;
    if (m_ssids.isSet()) {
        obj.insert(QString("ssids"), ::OpenAPI::toJsonValue(m_ssids));
    }
    return obj;
}

OAIUpdateNetworkClientSplashAuthorizationStatus_request_ssids OAIUpdateNetworkClientSplashAuthorizationStatus_request::getSsids() const {
    return m_ssids;
}
void OAIUpdateNetworkClientSplashAuthorizationStatus_request::setSsids(const OAIUpdateNetworkClientSplashAuthorizationStatus_request_ssids &ssids) {
    m_ssids = ssids;
    m_ssids_isSet = true;
}

bool OAIUpdateNetworkClientSplashAuthorizationStatus_request::is_ssids_Set() const{
    return m_ssids_isSet;
}

bool OAIUpdateNetworkClientSplashAuthorizationStatus_request::is_ssids_Valid() const{
    return m_ssids_isValid;
}

bool OAIUpdateNetworkClientSplashAuthorizationStatus_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ssids.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkClientSplashAuthorizationStatus_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_ssids_isValid && true;
}

} // namespace OpenAPI
