/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResourceState.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResourceState::OAIResourceState(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResourceState::OAIResourceState() {
    this->initializeModel();
}

OAIResourceState::~OAIResourceState() {}

void OAIResourceState::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIResourceState::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIResourceState::fromJson(QString jsonString) {
    
    if ( jsonString.compare("Creating", Qt::CaseInsensitive) == 0) {
        m_value = eOAIResourceState::CREATING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Enabling", Qt::CaseInsensitive) == 0) {
        m_value = eOAIResourceState::ENABLING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Enabled", Qt::CaseInsensitive) == 0) {
        m_value = eOAIResourceState::ENABLED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Disabling", Qt::CaseInsensitive) == 0) {
        m_value = eOAIResourceState::DISABLING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Disabled", Qt::CaseInsensitive) == 0) {
        m_value = eOAIResourceState::DISABLED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Deleting", Qt::CaseInsensitive) == 0) {
        m_value = eOAIResourceState::DELETING;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIResourceState::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIResourceState::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIResourceState::CREATING:
            val = "Creating";
            break;
        case eOAIResourceState::ENABLING:
            val = "Enabling";
            break;
        case eOAIResourceState::ENABLED:
            val = "Enabled";
            break;
        case eOAIResourceState::DISABLING:
            val = "Disabling";
            break;
        case eOAIResourceState::DISABLED:
            val = "Disabled";
            break;
        case eOAIResourceState::DELETING:
            val = "Deleting";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIResourceState::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIResourceState::eOAIResourceState OAIResourceState::getValue() const {
    return m_value;
}

void OAIResourceState::setValue(const OAIResourceState::eOAIResourceState& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIResourceState::isSet() const {
    
    return m_value_isSet;
}

bool OAIResourceState::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
