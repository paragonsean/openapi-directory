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

#include "OAICompany_data_company_extension_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompany_data_company_extension_interface::OAICompany_data_company_extension_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompany_data_company_extension_interface::OAICompany_data_company_extension_interface() {
    this->initializeModel();
}

OAICompany_data_company_extension_interface::~OAICompany_data_company_extension_interface() {}

void OAICompany_data_company_extension_interface::initializeModel() {

    m_applicable_payment_method_isSet = false;
    m_applicable_payment_method_isValid = false;

    m_available_payment_methods_isSet = false;
    m_available_payment_methods_isValid = false;

    m_quote_config_isSet = false;
    m_quote_config_isValid = false;

    m_use_config_settings_isSet = false;
    m_use_config_settings_isValid = false;
}

void OAICompany_data_company_extension_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompany_data_company_extension_interface::fromJsonObject(QJsonObject json) {

    m_applicable_payment_method_isValid = ::OpenAPI::fromJsonValue(m_applicable_payment_method, json[QString("applicable_payment_method")]);
    m_applicable_payment_method_isSet = !json[QString("applicable_payment_method")].isNull() && m_applicable_payment_method_isValid;

    m_available_payment_methods_isValid = ::OpenAPI::fromJsonValue(m_available_payment_methods, json[QString("available_payment_methods")]);
    m_available_payment_methods_isSet = !json[QString("available_payment_methods")].isNull() && m_available_payment_methods_isValid;

    m_quote_config_isValid = ::OpenAPI::fromJsonValue(m_quote_config, json[QString("quote_config")]);
    m_quote_config_isSet = !json[QString("quote_config")].isNull() && m_quote_config_isValid;

    m_use_config_settings_isValid = ::OpenAPI::fromJsonValue(m_use_config_settings, json[QString("use_config_settings")]);
    m_use_config_settings_isSet = !json[QString("use_config_settings")].isNull() && m_use_config_settings_isValid;
}

QString OAICompany_data_company_extension_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompany_data_company_extension_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_applicable_payment_method_isSet) {
        obj.insert(QString("applicable_payment_method"), ::OpenAPI::toJsonValue(m_applicable_payment_method));
    }
    if (m_available_payment_methods_isSet) {
        obj.insert(QString("available_payment_methods"), ::OpenAPI::toJsonValue(m_available_payment_methods));
    }
    if (m_quote_config.isSet()) {
        obj.insert(QString("quote_config"), ::OpenAPI::toJsonValue(m_quote_config));
    }
    if (m_use_config_settings_isSet) {
        obj.insert(QString("use_config_settings"), ::OpenAPI::toJsonValue(m_use_config_settings));
    }
    return obj;
}

qint32 OAICompany_data_company_extension_interface::getApplicablePaymentMethod() const {
    return m_applicable_payment_method;
}
void OAICompany_data_company_extension_interface::setApplicablePaymentMethod(const qint32 &applicable_payment_method) {
    m_applicable_payment_method = applicable_payment_method;
    m_applicable_payment_method_isSet = true;
}

bool OAICompany_data_company_extension_interface::is_applicable_payment_method_Set() const{
    return m_applicable_payment_method_isSet;
}

bool OAICompany_data_company_extension_interface::is_applicable_payment_method_Valid() const{
    return m_applicable_payment_method_isValid;
}

QString OAICompany_data_company_extension_interface::getAvailablePaymentMethods() const {
    return m_available_payment_methods;
}
void OAICompany_data_company_extension_interface::setAvailablePaymentMethods(const QString &available_payment_methods) {
    m_available_payment_methods = available_payment_methods;
    m_available_payment_methods_isSet = true;
}

bool OAICompany_data_company_extension_interface::is_available_payment_methods_Set() const{
    return m_available_payment_methods_isSet;
}

bool OAICompany_data_company_extension_interface::is_available_payment_methods_Valid() const{
    return m_available_payment_methods_isValid;
}

OAINegotiable_quote_data_company_quote_config_interface OAICompany_data_company_extension_interface::getQuoteConfig() const {
    return m_quote_config;
}
void OAICompany_data_company_extension_interface::setQuoteConfig(const OAINegotiable_quote_data_company_quote_config_interface &quote_config) {
    m_quote_config = quote_config;
    m_quote_config_isSet = true;
}

bool OAICompany_data_company_extension_interface::is_quote_config_Set() const{
    return m_quote_config_isSet;
}

bool OAICompany_data_company_extension_interface::is_quote_config_Valid() const{
    return m_quote_config_isValid;
}

qint32 OAICompany_data_company_extension_interface::getUseConfigSettings() const {
    return m_use_config_settings;
}
void OAICompany_data_company_extension_interface::setUseConfigSettings(const qint32 &use_config_settings) {
    m_use_config_settings = use_config_settings;
    m_use_config_settings_isSet = true;
}

bool OAICompany_data_company_extension_interface::is_use_config_settings_Set() const{
    return m_use_config_settings_isSet;
}

bool OAICompany_data_company_extension_interface::is_use_config_settings_Valid() const{
    return m_use_config_settings_isValid;
}

bool OAICompany_data_company_extension_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_applicable_payment_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_payment_methods_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_config.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_settings_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICompany_data_company_extension_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
