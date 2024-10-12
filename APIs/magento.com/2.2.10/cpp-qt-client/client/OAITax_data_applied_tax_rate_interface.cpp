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

#include "OAITax_data_applied_tax_rate_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITax_data_applied_tax_rate_interface::OAITax_data_applied_tax_rate_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITax_data_applied_tax_rate_interface::OAITax_data_applied_tax_rate_interface() {
    this->initializeModel();
}

OAITax_data_applied_tax_rate_interface::~OAITax_data_applied_tax_rate_interface() {}

void OAITax_data_applied_tax_rate_interface::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_percent_isSet = false;
    m_percent_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAITax_data_applied_tax_rate_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITax_data_applied_tax_rate_interface::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_percent_isValid = ::OpenAPI::fromJsonValue(m_percent, json[QString("percent")]);
    m_percent_isSet = !json[QString("percent")].isNull() && m_percent_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAITax_data_applied_tax_rate_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITax_data_applied_tax_rate_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_percent_isSet) {
        obj.insert(QString("percent"), ::OpenAPI::toJsonValue(m_percent));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAITax_data_applied_tax_rate_interface::getCode() const {
    return m_code;
}
void OAITax_data_applied_tax_rate_interface::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAITax_data_applied_tax_rate_interface::is_code_Set() const{
    return m_code_isSet;
}

bool OAITax_data_applied_tax_rate_interface::is_code_Valid() const{
    return m_code_isValid;
}

OAIObject OAITax_data_applied_tax_rate_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAITax_data_applied_tax_rate_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAITax_data_applied_tax_rate_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAITax_data_applied_tax_rate_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

double OAITax_data_applied_tax_rate_interface::getPercent() const {
    return m_percent;
}
void OAITax_data_applied_tax_rate_interface::setPercent(const double &percent) {
    m_percent = percent;
    m_percent_isSet = true;
}

bool OAITax_data_applied_tax_rate_interface::is_percent_Set() const{
    return m_percent_isSet;
}

bool OAITax_data_applied_tax_rate_interface::is_percent_Valid() const{
    return m_percent_isValid;
}

QString OAITax_data_applied_tax_rate_interface::getTitle() const {
    return m_title;
}
void OAITax_data_applied_tax_rate_interface::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAITax_data_applied_tax_rate_interface::is_title_Set() const{
    return m_title_isSet;
}

bool OAITax_data_applied_tax_rate_interface::is_title_Valid() const{
    return m_title_isValid;
}

bool OAITax_data_applied_tax_rate_interface::isSet() const {
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

        if (m_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITax_data_applied_tax_rate_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
