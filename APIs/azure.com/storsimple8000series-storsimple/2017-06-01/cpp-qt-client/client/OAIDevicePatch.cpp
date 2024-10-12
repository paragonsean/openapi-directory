/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDevicePatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDevicePatch::OAIDevicePatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDevicePatch::OAIDevicePatch() {
    this->initializeModel();
}

OAIDevicePatch::~OAIDevicePatch() {}

void OAIDevicePatch::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIDevicePatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDevicePatch::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIDevicePatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDevicePatch::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIDevicePatchProperties OAIDevicePatch::getProperties() const {
    return m_properties;
}
void OAIDevicePatch::setProperties(const OAIDevicePatchProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIDevicePatch::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIDevicePatch::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIDevicePatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDevicePatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_properties_isValid && true;
}

} // namespace OpenAPI
