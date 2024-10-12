/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAutomatedProcessCode.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAutomatedProcessCode::OAIAutomatedProcessCode(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAutomatedProcessCode::OAIAutomatedProcessCode() {
    this->initializeModel();
}

OAIAutomatedProcessCode::~OAIAutomatedProcessCode() {}

void OAIAutomatedProcessCode::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIAutomatedProcessCode::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIAutomatedProcessCode::fromJson(QString jsonString) {
    
    if ( jsonString.compare("IMMEDIATE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAutomatedProcessCode::IMMEDIATE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DELAYED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAutomatedProcessCode::DELAYED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ERROR", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAutomatedProcessCode::ERROR;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIAutomatedProcessCode::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIAutomatedProcessCode::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIAutomatedProcessCode::IMMEDIATE:
            val = "IMMEDIATE";
            break;
        case eOAIAutomatedProcessCode::DELAYED:
            val = "DELAYED";
            break;
        case eOAIAutomatedProcessCode::ERROR:
            val = "ERROR";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIAutomatedProcessCode::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIAutomatedProcessCode::eOAIAutomatedProcessCode OAIAutomatedProcessCode::getValue() const {
    return m_value;
}

void OAIAutomatedProcessCode::setValue(const OAIAutomatedProcessCode::eOAIAutomatedProcessCode& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIAutomatedProcessCode::isSet() const {
    
    return m_value_isSet;
}

bool OAIAutomatedProcessCode::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
