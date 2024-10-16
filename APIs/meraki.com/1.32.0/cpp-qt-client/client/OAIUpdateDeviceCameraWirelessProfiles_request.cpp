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

#include "OAIUpdateDeviceCameraWirelessProfiles_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDeviceCameraWirelessProfiles_request::OAIUpdateDeviceCameraWirelessProfiles_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDeviceCameraWirelessProfiles_request::OAIUpdateDeviceCameraWirelessProfiles_request() {
    this->initializeModel();
}

OAIUpdateDeviceCameraWirelessProfiles_request::~OAIUpdateDeviceCameraWirelessProfiles_request() {}

void OAIUpdateDeviceCameraWirelessProfiles_request::initializeModel() {

    m_ids_isSet = false;
    m_ids_isValid = false;
}

void OAIUpdateDeviceCameraWirelessProfiles_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDeviceCameraWirelessProfiles_request::fromJsonObject(QJsonObject json) {

    m_ids_isValid = ::OpenAPI::fromJsonValue(m_ids, json[QString("ids")]);
    m_ids_isSet = !json[QString("ids")].isNull() && m_ids_isValid;
}

QString OAIUpdateDeviceCameraWirelessProfiles_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDeviceCameraWirelessProfiles_request::asJsonObject() const {
    QJsonObject obj;
    if (m_ids.isSet()) {
        obj.insert(QString("ids"), ::OpenAPI::toJsonValue(m_ids));
    }
    return obj;
}

OAIUpdateDeviceCameraWirelessProfiles_request_ids OAIUpdateDeviceCameraWirelessProfiles_request::getIds() const {
    return m_ids;
}
void OAIUpdateDeviceCameraWirelessProfiles_request::setIds(const OAIUpdateDeviceCameraWirelessProfiles_request_ids &ids) {
    m_ids = ids;
    m_ids_isSet = true;
}

bool OAIUpdateDeviceCameraWirelessProfiles_request::is_ids_Set() const{
    return m_ids_isSet;
}

bool OAIUpdateDeviceCameraWirelessProfiles_request::is_ids_Valid() const{
    return m_ids_isValid;
}

bool OAIUpdateDeviceCameraWirelessProfiles_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ids.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDeviceCameraWirelessProfiles_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_ids_isValid && true;
}

} // namespace OpenAPI
