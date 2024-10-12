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

#include "OAIParentType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIParentType::OAIParentType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIParentType::OAIParentType() {
    this->initializeModel();
}

OAIParentType::~OAIParentType() {}

void OAIParentType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIParentType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIParentType::fromJson(QString jsonString) {
    
    if ( jsonString.compare(QString::number(1), Qt::CaseInsensitive) == 0) {
        m_value = eOAIParentType::_1;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare(QString::number(2), Qt::CaseInsensitive) == 0) {
        m_value = eOAIParentType::_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare(QString::number(3), Qt::CaseInsensitive) == 0) {
        m_value = eOAIParentType::_3;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIParentType::fromJsonValue(QJsonValue json) {
m_value = static_cast<eOAIParentType>(json.toInt());
}

QString OAIParentType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIParentType::_1:
            val = QString::number(1);
            break;
        case eOAIParentType::_2:
            val = QString::number(2);
            break;
        case eOAIParentType::_3:
            val = QString::number(3);
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIParentType::asJsonValue() const {
    
    return QJsonValue(static_cast<int>(m_value));
}


OAIParentType::eOAIParentType OAIParentType::getValue() const {
    return m_value;
}

void OAIParentType::setValue(const OAIParentType::eOAIParentType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIParentType::isSet() const {
    
    return m_value_isSet;
}

bool OAIParentType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
