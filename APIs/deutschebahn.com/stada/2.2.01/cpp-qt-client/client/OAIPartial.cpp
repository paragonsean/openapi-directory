/**
 * Stationsdatenbereitstellung
 * An API providing master data for German railway stations by DB Station&Service AG.
 *
 * The version of the OpenAPI document: 2.2.01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPartial.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPartial::OAIPartial(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPartial::OAIPartial() {
    this->initializeModel();
}

OAIPartial::~OAIPartial() {}

void OAIPartial::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIPartial::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIPartial::fromJson(QString jsonString) {
    
    if ( jsonString.compare("true", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPartial::TRUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("false", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPartial::FALSE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("partial", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPartial::PARTIAL;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIPartial::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIPartial::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIPartial::TRUE:
            val = "true";
            break;
        case eOAIPartial::FALSE:
            val = "false";
            break;
        case eOAIPartial::PARTIAL:
            val = "partial";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIPartial::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIPartial::eOAIPartial OAIPartial::getValue() const {
    return m_value;
}

void OAIPartial::setValue(const OAIPartial::eOAIPartial& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIPartial::isSet() const {
    
    return m_value_isSet;
}

bool OAIPartial::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
