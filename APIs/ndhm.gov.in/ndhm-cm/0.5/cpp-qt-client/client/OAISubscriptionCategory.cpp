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

#include "OAISubscriptionCategory.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionCategory::OAISubscriptionCategory(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionCategory::OAISubscriptionCategory() {
    this->initializeModel();
}

OAISubscriptionCategory::~OAISubscriptionCategory() {}

void OAISubscriptionCategory::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAISubscriptionCategory::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAISubscriptionCategory::fromJson(QString jsonString) {
    
    if ( jsonString.compare("LINK", Qt::CaseInsensitive) == 0) {
        m_value = eOAISubscriptionCategory::LINK;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAISubscriptionCategory::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAISubscriptionCategory::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAISubscriptionCategory::LINK:
            val = "LINK";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAISubscriptionCategory::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAISubscriptionCategory::eOAISubscriptionCategory OAISubscriptionCategory::getValue() const {
    return m_value;
}

void OAISubscriptionCategory::setValue(const OAISubscriptionCategory::eOAISubscriptionCategory& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAISubscriptionCategory::isSet() const {
    
    return m_value_isSet;
}

bool OAISubscriptionCategory::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
