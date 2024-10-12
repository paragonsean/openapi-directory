/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
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
