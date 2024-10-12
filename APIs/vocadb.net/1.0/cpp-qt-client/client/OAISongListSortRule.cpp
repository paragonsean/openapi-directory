/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISongListSortRule.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISongListSortRule::OAISongListSortRule(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISongListSortRule::OAISongListSortRule() {
    this->initializeModel();
}

OAISongListSortRule::~OAISongListSortRule() {}

void OAISongListSortRule::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAISongListSortRule::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAISongListSortRule::fromJson(QString jsonString) {
    
    if ( jsonString.compare("None", Qt::CaseInsensitive) == 0) {
        m_value = eOAISongListSortRule::NONE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Name", Qt::CaseInsensitive) == 0) {
        m_value = eOAISongListSortRule::NAME;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Date", Qt::CaseInsensitive) == 0) {
        m_value = eOAISongListSortRule::DATE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CreateDate", Qt::CaseInsensitive) == 0) {
        m_value = eOAISongListSortRule::CREATEDATE;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAISongListSortRule::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAISongListSortRule::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAISongListSortRule::NONE:
            val = "None";
            break;
        case eOAISongListSortRule::NAME:
            val = "Name";
            break;
        case eOAISongListSortRule::DATE:
            val = "Date";
            break;
        case eOAISongListSortRule::CREATEDATE:
            val = "CreateDate";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAISongListSortRule::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAISongListSortRule::eOAISongListSortRule OAISongListSortRule::getValue() const {
    return m_value;
}

void OAISongListSortRule::setValue(const OAISongListSortRule::eOAISongListSortRule& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAISongListSortRule::isSet() const {
    
    return m_value_isSet;
}

bool OAISongListSortRule::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
