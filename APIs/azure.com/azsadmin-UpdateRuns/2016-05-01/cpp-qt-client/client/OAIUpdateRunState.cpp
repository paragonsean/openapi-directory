/**
 * UpdateAdminClient
 * Update run operation endpoints and objects.
 *
 * The version of the OpenAPI document: 2016-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateRunState.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateRunState::OAIUpdateRunState(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateRunState::OAIUpdateRunState() {
    this->initializeModel();
}

OAIUpdateRunState::~OAIUpdateRunState() {}

void OAIUpdateRunState::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIUpdateRunState::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIUpdateRunState::fromJson(QString jsonString) {
    
    if ( jsonString.compare("Unknown", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUpdateRunState::UNKNOWN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Succeeded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUpdateRunState::SUCCEEDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("InProgress", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUpdateRunState::INPROGRESS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Failed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUpdateRunState::FAILED;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIUpdateRunState::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIUpdateRunState::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIUpdateRunState::UNKNOWN:
            val = "Unknown";
            break;
        case eOAIUpdateRunState::SUCCEEDED:
            val = "Succeeded";
            break;
        case eOAIUpdateRunState::INPROGRESS:
            val = "InProgress";
            break;
        case eOAIUpdateRunState::FAILED:
            val = "Failed";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIUpdateRunState::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIUpdateRunState::eOAIUpdateRunState OAIUpdateRunState::getValue() const {
    return m_value;
}

void OAIUpdateRunState::setValue(const OAIUpdateRunState::eOAIUpdateRunState& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIUpdateRunState::isSet() const {
    
    return m_value_isSet;
}

bool OAIUpdateRunState::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
