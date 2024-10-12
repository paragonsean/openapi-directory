/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStorageAccountType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStorageAccountType::OAIStorageAccountType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStorageAccountType::OAIStorageAccountType() {
    this->initializeModel();
}

OAIStorageAccountType::~OAIStorageAccountType() {}

void OAIStorageAccountType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIStorageAccountType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIStorageAccountType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("Standard_LRS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStorageAccountType::STANDARD_LRS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Premium_LRS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStorageAccountType::PREMIUM_LRS;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIStorageAccountType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIStorageAccountType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIStorageAccountType::STANDARD_LRS:
            val = "Standard_LRS";
            break;
        case eOAIStorageAccountType::PREMIUM_LRS:
            val = "Premium_LRS";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIStorageAccountType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIStorageAccountType::eOAIStorageAccountType OAIStorageAccountType::getValue() const {
    return m_value;
}

void OAIStorageAccountType::setValue(const OAIStorageAccountType::eOAIStorageAccountType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIStorageAccountType::isSet() const {
    
    return m_value_isSet;
}

bool OAIStorageAccountType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
