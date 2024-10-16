/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUseType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUseType::OAIUseType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUseType::OAIUseType() {
    this->initializeModel();
}

OAIUseType::~OAIUseType() {}

void OAIUseType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIUseType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIUseType::fromJson(QString jsonString) {
    
    if ( jsonString.compare(QString::number(1), Qt::CaseInsensitive) == 0) {
        m_value = eOAIUseType::_1;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare(QString::number(2), Qt::CaseInsensitive) == 0) {
        m_value = eOAIUseType::_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare(QString::number(3), Qt::CaseInsensitive) == 0) {
        m_value = eOAIUseType::_3;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare(QString::number(4), Qt::CaseInsensitive) == 0) {
        m_value = eOAIUseType::_4;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIUseType::fromJsonValue(QJsonValue json) {
m_value = static_cast<eOAIUseType>(json.toInt());
}

QString OAIUseType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIUseType::_1:
            val = QString::number(1);
            break;
        case eOAIUseType::_2:
            val = QString::number(2);
            break;
        case eOAIUseType::_3:
            val = QString::number(3);
            break;
        case eOAIUseType::_4:
            val = QString::number(4);
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIUseType::asJsonValue() const {
    
    return QJsonValue(static_cast<int>(m_value));
}


OAIUseType::eOAIUseType OAIUseType::getValue() const {
    return m_value;
}

void OAIUseType::setValue(const OAIUseType::eOAIUseType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIUseType::isSet() const {
    
    return m_value_isSet;
}

bool OAIUseType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
