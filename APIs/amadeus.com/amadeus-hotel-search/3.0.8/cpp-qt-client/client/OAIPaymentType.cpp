/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPaymentType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentType::OAIPaymentType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentType::OAIPaymentType() {
    this->initializeModel();
}

OAIPaymentType::~OAIPaymentType() {}

void OAIPaymentType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIPaymentType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIPaymentType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("GUARANTEE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentType::GUARANTEE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DEPOSIT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentType::DEPOSIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PREPAY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentType::PREPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HOLDTIME", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentType::HOLDTIME;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIPaymentType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIPaymentType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIPaymentType::GUARANTEE:
            val = "GUARANTEE";
            break;
        case eOAIPaymentType::DEPOSIT:
            val = "DEPOSIT";
            break;
        case eOAIPaymentType::PREPAY:
            val = "PREPAY";
            break;
        case eOAIPaymentType::HOLDTIME:
            val = "HOLDTIME";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIPaymentType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIPaymentType::eOAIPaymentType OAIPaymentType::getValue() const {
    return m_value;
}

void OAIPaymentType::setValue(const OAIPaymentType::eOAIPaymentType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIPaymentType::isSet() const {
    
    return m_value_isSet;
}

bool OAIPaymentType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
