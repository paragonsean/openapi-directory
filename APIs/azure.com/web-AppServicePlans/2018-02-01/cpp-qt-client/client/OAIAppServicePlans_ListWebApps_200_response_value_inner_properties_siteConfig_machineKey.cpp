/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::initializeModel() {

    m_decryption_isSet = false;
    m_decryption_isValid = false;

    m_decryption_key_isSet = false;
    m_decryption_key_isValid = false;

    m_validation_isSet = false;
    m_validation_isValid = false;

    m_validation_key_isSet = false;
    m_validation_key_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::fromJsonObject(QJsonObject json) {

    m_decryption_isValid = ::OpenAPI::fromJsonValue(m_decryption, json[QString("decryption")]);
    m_decryption_isSet = !json[QString("decryption")].isNull() && m_decryption_isValid;

    m_decryption_key_isValid = ::OpenAPI::fromJsonValue(m_decryption_key, json[QString("decryptionKey")]);
    m_decryption_key_isSet = !json[QString("decryptionKey")].isNull() && m_decryption_key_isValid;

    m_validation_isValid = ::OpenAPI::fromJsonValue(m_validation, json[QString("validation")]);
    m_validation_isSet = !json[QString("validation")].isNull() && m_validation_isValid;

    m_validation_key_isValid = ::OpenAPI::fromJsonValue(m_validation_key, json[QString("validationKey")]);
    m_validation_key_isSet = !json[QString("validationKey")].isNull() && m_validation_key_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::asJsonObject() const {
    QJsonObject obj;
    if (m_decryption_isSet) {
        obj.insert(QString("decryption"), ::OpenAPI::toJsonValue(m_decryption));
    }
    if (m_decryption_key_isSet) {
        obj.insert(QString("decryptionKey"), ::OpenAPI::toJsonValue(m_decryption_key));
    }
    if (m_validation_isSet) {
        obj.insert(QString("validation"), ::OpenAPI::toJsonValue(m_validation));
    }
    if (m_validation_key_isSet) {
        obj.insert(QString("validationKey"), ::OpenAPI::toJsonValue(m_validation_key));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::getDecryption() const {
    return m_decryption;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::setDecryption(const QString &decryption) {
    m_decryption = decryption;
    m_decryption_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_decryption_Set() const{
    return m_decryption_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_decryption_Valid() const{
    return m_decryption_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::getDecryptionKey() const {
    return m_decryption_key;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::setDecryptionKey(const QString &decryption_key) {
    m_decryption_key = decryption_key;
    m_decryption_key_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_decryption_key_Set() const{
    return m_decryption_key_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_decryption_key_Valid() const{
    return m_decryption_key_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::getValidation() const {
    return m_validation;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::setValidation(const QString &validation) {
    m_validation = validation;
    m_validation_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_validation_Set() const{
    return m_validation_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_validation_Valid() const{
    return m_validation_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::getValidationKey() const {
    return m_validation_key;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::setValidationKey(const QString &validation_key) {
    m_validation_key = validation_key;
    m_validation_key_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_validation_key_Set() const{
    return m_validation_key_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::is_validation_key_Valid() const{
    return m_validation_key_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_decryption_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_decryption_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validation_key_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_machineKey::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
