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

#include "OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner() {
    this->initializeModel();
}

OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::~OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner() {}

void OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::getName() const {
    return m_name;
}
void OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::getValue() const {
    return m_value;
}
void OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDeviceCameraCustomAnalytics_request_parameters_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
