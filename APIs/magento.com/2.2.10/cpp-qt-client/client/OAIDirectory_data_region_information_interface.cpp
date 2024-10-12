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

#include "OAIDirectory_data_region_information_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDirectory_data_region_information_interface::OAIDirectory_data_region_information_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDirectory_data_region_information_interface::OAIDirectory_data_region_information_interface() {
    this->initializeModel();
}

OAIDirectory_data_region_information_interface::~OAIDirectory_data_region_information_interface() {}

void OAIDirectory_data_region_information_interface::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIDirectory_data_region_information_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDirectory_data_region_information_interface::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIDirectory_data_region_information_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDirectory_data_region_information_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIDirectory_data_region_information_interface::getCode() const {
    return m_code;
}
void OAIDirectory_data_region_information_interface::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIDirectory_data_region_information_interface::is_code_Set() const{
    return m_code_isSet;
}

bool OAIDirectory_data_region_information_interface::is_code_Valid() const{
    return m_code_isValid;
}

OAIObject OAIDirectory_data_region_information_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAIDirectory_data_region_information_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAIDirectory_data_region_information_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAIDirectory_data_region_information_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

QString OAIDirectory_data_region_information_interface::getId() const {
    return m_id;
}
void OAIDirectory_data_region_information_interface::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDirectory_data_region_information_interface::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDirectory_data_region_information_interface::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIDirectory_data_region_information_interface::getName() const {
    return m_name;
}
void OAIDirectory_data_region_information_interface::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDirectory_data_region_information_interface::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDirectory_data_region_information_interface::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIDirectory_data_region_information_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDirectory_data_region_information_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_id_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
