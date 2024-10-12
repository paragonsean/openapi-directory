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

#include "OAIEntryOptionalFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEntryOptionalFields::OAIEntryOptionalFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEntryOptionalFields::OAIEntryOptionalFields() {
    this->initializeModel();
}

OAIEntryOptionalFields::~OAIEntryOptionalFields() {}

void OAIEntryOptionalFields::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIEntryOptionalFields::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIEntryOptionalFields::fromJson(QString jsonString) {
    
    if ( jsonString.compare("None", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::NONE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AdditionalNames", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::ADDITIONALNAMES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Description", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::DESCRIPTION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MainPicture", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::MAINPICTURE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Names", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::NAMES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PVs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::PVS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Tags", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::TAGS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WebLinks", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEntryOptionalFields::WEBLINKS;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIEntryOptionalFields::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIEntryOptionalFields::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIEntryOptionalFields::NONE:
            val = "None";
            break;
        case eOAIEntryOptionalFields::ADDITIONALNAMES:
            val = "AdditionalNames";
            break;
        case eOAIEntryOptionalFields::DESCRIPTION:
            val = "Description";
            break;
        case eOAIEntryOptionalFields::MAINPICTURE:
            val = "MainPicture";
            break;
        case eOAIEntryOptionalFields::NAMES:
            val = "Names";
            break;
        case eOAIEntryOptionalFields::PVS:
            val = "PVs";
            break;
        case eOAIEntryOptionalFields::TAGS:
            val = "Tags";
            break;
        case eOAIEntryOptionalFields::WEBLINKS:
            val = "WebLinks";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIEntryOptionalFields::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIEntryOptionalFields::eOAIEntryOptionalFields OAIEntryOptionalFields::getValue() const {
    return m_value;
}

void OAIEntryOptionalFields::setValue(const OAIEntryOptionalFields::eOAIEntryOptionalFields& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIEntryOptionalFields::isSet() const {
    
    return m_value_isSet;
}

bool OAIEntryOptionalFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
