/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFeeType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeeType::OAIFeeType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeeType::OAIFeeType() {
    this->initializeModel();
}

OAIFeeType::~OAIFeeType() {}

void OAIFeeType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIFeeType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIFeeType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("TICKETING", Qt::CaseInsensitive) == 0) {
        m_value = eOAIFeeType::TICKETING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FORM_OF_PAYMENT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIFeeType::FORM_OF_PAYMENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SUPPLIER", Qt::CaseInsensitive) == 0) {
        m_value = eOAIFeeType::SUPPLIER;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIFeeType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIFeeType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIFeeType::TICKETING:
            val = "TICKETING";
            break;
        case eOAIFeeType::FORM_OF_PAYMENT:
            val = "FORM_OF_PAYMENT";
            break;
        case eOAIFeeType::SUPPLIER:
            val = "SUPPLIER";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIFeeType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIFeeType::eOAIFeeType OAIFeeType::getValue() const {
    return m_value;
}

void OAIFeeType::setValue(const OAIFeeType::eOAIFeeType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIFeeType::isSet() const {
    
    return m_value_isSet;
}

bool OAIFeeType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
