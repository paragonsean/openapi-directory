/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISales_data_shipment_package_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISales_data_shipment_package_interface::OAISales_data_shipment_package_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISales_data_shipment_package_interface::OAISales_data_shipment_package_interface() {
    this->initializeModel();
}

OAISales_data_shipment_package_interface::~OAISales_data_shipment_package_interface() {}

void OAISales_data_shipment_package_interface::initializeModel() {

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;
}

void OAISales_data_shipment_package_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISales_data_shipment_package_interface::fromJsonObject(QJsonObject json) {

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;
}

QString OAISales_data_shipment_package_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISales_data_shipment_package_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    return obj;
}

OAIObject OAISales_data_shipment_package_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAISales_data_shipment_package_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAISales_data_shipment_package_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAISales_data_shipment_package_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

bool OAISales_data_shipment_package_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISales_data_shipment_package_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
