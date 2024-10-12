/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITravelerType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITravelerType::OAITravelerType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITravelerType::OAITravelerType() {
    this->initializeModel();
}

OAITravelerType::~OAITravelerType() {}

void OAITravelerType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAITravelerType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAITravelerType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("ADULT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::ADULT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CHILD", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::CHILD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SENIOR", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::SENIOR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("YOUNG", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::YOUNG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HELD_INFANT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::HELD_INFANT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SEATED_INFANT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::SEATED_INFANT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("STUDENT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerType::STUDENT;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAITravelerType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAITravelerType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAITravelerType::ADULT:
            val = "ADULT";
            break;
        case eOAITravelerType::CHILD:
            val = "CHILD";
            break;
        case eOAITravelerType::SENIOR:
            val = "SENIOR";
            break;
        case eOAITravelerType::YOUNG:
            val = "YOUNG";
            break;
        case eOAITravelerType::HELD_INFANT:
            val = "HELD_INFANT";
            break;
        case eOAITravelerType::SEATED_INFANT:
            val = "SEATED_INFANT";
            break;
        case eOAITravelerType::STUDENT:
            val = "STUDENT";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAITravelerType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAITravelerType::eOAITravelerType OAITravelerType::getValue() const {
    return m_value;
}

void OAITravelerType::setValue(const OAITravelerType::eOAITravelerType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAITravelerType::isSet() const {
    
    return m_value_isSet;
}

bool OAITravelerType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
