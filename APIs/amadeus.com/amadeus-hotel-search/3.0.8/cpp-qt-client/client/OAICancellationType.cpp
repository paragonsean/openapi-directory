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

#include "OAICancellationType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICancellationType::OAICancellationType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICancellationType::OAICancellationType() {
    this->initializeModel();
}

OAICancellationType::~OAICancellationType() {}

void OAICancellationType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAICancellationType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAICancellationType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("FULL_STAY", Qt::CaseInsensitive) == 0) {
        m_value = eOAICancellationType::FULL_STAY;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAICancellationType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAICancellationType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAICancellationType::FULL_STAY:
            val = "FULL_STAY";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAICancellationType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAICancellationType::eOAICancellationType OAICancellationType::getValue() const {
    return m_value;
}

void OAICancellationType::setValue(const OAICancellationType::eOAICancellationType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAICancellationType::isSet() const {
    
    return m_value_isSet;
}

bool OAICancellationType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
