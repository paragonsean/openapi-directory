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

#include "OAINegotiable_quote_data_attachment_content_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINegotiable_quote_data_attachment_content_interface::OAINegotiable_quote_data_attachment_content_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINegotiable_quote_data_attachment_content_interface::OAINegotiable_quote_data_attachment_content_interface() {
    this->initializeModel();
}

OAINegotiable_quote_data_attachment_content_interface::~OAINegotiable_quote_data_attachment_content_interface() {}

void OAINegotiable_quote_data_attachment_content_interface::initializeModel() {

    m_base64_encoded_data_isSet = false;
    m_base64_encoded_data_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAINegotiable_quote_data_attachment_content_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINegotiable_quote_data_attachment_content_interface::fromJsonObject(QJsonObject json) {

    m_base64_encoded_data_isValid = ::OpenAPI::fromJsonValue(m_base64_encoded_data, json[QString("base64_encoded_data")]);
    m_base64_encoded_data_isSet = !json[QString("base64_encoded_data")].isNull() && m_base64_encoded_data_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAINegotiable_quote_data_attachment_content_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINegotiable_quote_data_attachment_content_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_base64_encoded_data_isSet) {
        obj.insert(QString("base64_encoded_data"), ::OpenAPI::toJsonValue(m_base64_encoded_data));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAINegotiable_quote_data_attachment_content_interface::getBase64EncodedData() const {
    return m_base64_encoded_data;
}
void OAINegotiable_quote_data_attachment_content_interface::setBase64EncodedData(const QString &base64_encoded_data) {
    m_base64_encoded_data = base64_encoded_data;
    m_base64_encoded_data_isSet = true;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_base64_encoded_data_Set() const{
    return m_base64_encoded_data_isSet;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_base64_encoded_data_Valid() const{
    return m_base64_encoded_data_isValid;
}

OAIObject OAINegotiable_quote_data_attachment_content_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAINegotiable_quote_data_attachment_content_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

QString OAINegotiable_quote_data_attachment_content_interface::getName() const {
    return m_name;
}
void OAINegotiable_quote_data_attachment_content_interface::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_name_Set() const{
    return m_name_isSet;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_name_Valid() const{
    return m_name_isValid;
}

QString OAINegotiable_quote_data_attachment_content_interface::getType() const {
    return m_type;
}
void OAINegotiable_quote_data_attachment_content_interface::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_type_Set() const{
    return m_type_isSet;
}

bool OAINegotiable_quote_data_attachment_content_interface::is_type_Valid() const{
    return m_type_isValid;
}

bool OAINegotiable_quote_data_attachment_content_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base64_encoded_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINegotiable_quote_data_attachment_content_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_base64_encoded_data_isValid && m_name_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
