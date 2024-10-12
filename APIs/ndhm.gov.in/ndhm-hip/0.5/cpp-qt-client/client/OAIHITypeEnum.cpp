/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHITypeEnum.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHITypeEnum::OAIHITypeEnum(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHITypeEnum::OAIHITypeEnum() {
    this->initializeModel();
}

OAIHITypeEnum::~OAIHITypeEnum() {}

void OAIHITypeEnum::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIHITypeEnum::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIHITypeEnum::fromJson(QString jsonString) {
    
    if ( jsonString.compare("OPConsultation", Qt::CaseInsensitive) == 0) {
        m_value = eOAIHITypeEnum::OPCONSULTATION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Prescription", Qt::CaseInsensitive) == 0) {
        m_value = eOAIHITypeEnum::PRESCRIPTION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DischargeSummary", Qt::CaseInsensitive) == 0) {
        m_value = eOAIHITypeEnum::DISCHARGESUMMARY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DiagnosticReport", Qt::CaseInsensitive) == 0) {
        m_value = eOAIHITypeEnum::DIAGNOSTICREPORT;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIHITypeEnum::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIHITypeEnum::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIHITypeEnum::OPCONSULTATION:
            val = "OPConsultation";
            break;
        case eOAIHITypeEnum::PRESCRIPTION:
            val = "Prescription";
            break;
        case eOAIHITypeEnum::DISCHARGESUMMARY:
            val = "DischargeSummary";
            break;
        case eOAIHITypeEnum::DIAGNOSTICREPORT:
            val = "DiagnosticReport";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIHITypeEnum::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIHITypeEnum::eOAIHITypeEnum OAIHITypeEnum::getValue() const {
    return m_value;
}

void OAIHITypeEnum::setValue(const OAIHITypeEnum::eOAIHITypeEnum& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIHITypeEnum::isSet() const {
    
    return m_value_isSet;
}

bool OAIHITypeEnum::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
