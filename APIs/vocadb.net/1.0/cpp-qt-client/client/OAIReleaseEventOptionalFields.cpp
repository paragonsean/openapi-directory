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

#include "OAIReleaseEventOptionalFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReleaseEventOptionalFields::OAIReleaseEventOptionalFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReleaseEventOptionalFields::OAIReleaseEventOptionalFields() {
    this->initializeModel();
}

OAIReleaseEventOptionalFields::~OAIReleaseEventOptionalFields() {}

void OAIReleaseEventOptionalFields::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIReleaseEventOptionalFields::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIReleaseEventOptionalFields::fromJson(QString jsonString) {
    
    if ( jsonString.compare("None", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::NONE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AdditionalNames", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::ADDITIONALNAMES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Artists", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::ARTISTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Description", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::DESCRIPTION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MainPicture", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::MAINPICTURE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Names", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::NAMES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Series", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::SERIES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SongList", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::SONGLIST;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Tags", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::TAGS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Venue", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::VENUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WebLinks", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::WEBLINKS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PVs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIReleaseEventOptionalFields::PVS;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIReleaseEventOptionalFields::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIReleaseEventOptionalFields::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIReleaseEventOptionalFields::NONE:
            val = "None";
            break;
        case eOAIReleaseEventOptionalFields::ADDITIONALNAMES:
            val = "AdditionalNames";
            break;
        case eOAIReleaseEventOptionalFields::ARTISTS:
            val = "Artists";
            break;
        case eOAIReleaseEventOptionalFields::DESCRIPTION:
            val = "Description";
            break;
        case eOAIReleaseEventOptionalFields::MAINPICTURE:
            val = "MainPicture";
            break;
        case eOAIReleaseEventOptionalFields::NAMES:
            val = "Names";
            break;
        case eOAIReleaseEventOptionalFields::SERIES:
            val = "Series";
            break;
        case eOAIReleaseEventOptionalFields::SONGLIST:
            val = "SongList";
            break;
        case eOAIReleaseEventOptionalFields::TAGS:
            val = "Tags";
            break;
        case eOAIReleaseEventOptionalFields::VENUE:
            val = "Venue";
            break;
        case eOAIReleaseEventOptionalFields::WEBLINKS:
            val = "WebLinks";
            break;
        case eOAIReleaseEventOptionalFields::PVS:
            val = "PVs";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIReleaseEventOptionalFields::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIReleaseEventOptionalFields::eOAIReleaseEventOptionalFields OAIReleaseEventOptionalFields::getValue() const {
    return m_value;
}

void OAIReleaseEventOptionalFields::setValue(const OAIReleaseEventOptionalFields::eOAIReleaseEventOptionalFields& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIReleaseEventOptionalFields::isSet() const {
    
    return m_value_isSet;
}

bool OAIReleaseEventOptionalFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
