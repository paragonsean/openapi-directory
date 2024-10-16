/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExport_entity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExport_entity::OAIExport_entity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExport_entity::OAIExport_entity() {
    this->initializeModel();
}

OAIExport_entity::~OAIExport_entity() {}

void OAIExport_entity::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIExport_entity::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIExport_entity::fromJson(QString jsonString) {
    
    if ( jsonString.compare("crashes", Qt::CaseInsensitive) == 0) {
        m_value = eOAIExport_entity::CRASHES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("errors", Qt::CaseInsensitive) == 0) {
        m_value = eOAIExport_entity::ERRORS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("attachments", Qt::CaseInsensitive) == 0) {
        m_value = eOAIExport_entity::ATTACHMENTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("no_logs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIExport_entity::NO_LOGS;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIExport_entity::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIExport_entity::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIExport_entity::CRASHES:
            val = "crashes";
            break;
        case eOAIExport_entity::ERRORS:
            val = "errors";
            break;
        case eOAIExport_entity::ATTACHMENTS:
            val = "attachments";
            break;
        case eOAIExport_entity::NO_LOGS:
            val = "no_logs";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIExport_entity::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIExport_entity::eOAIExport_entity OAIExport_entity::getValue() const {
    return m_value;
}

void OAIExport_entity::setValue(const OAIExport_entity::eOAIExport_entity& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIExport_entity::isSet() const {
    
    return m_value_isSet;
}

bool OAIExport_entity::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
