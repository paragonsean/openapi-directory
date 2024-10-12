/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConsentStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsentStatus::OAIConsentStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsentStatus::OAIConsentStatus() {
    this->initializeModel();
}

OAIConsentStatus::~OAIConsentStatus() {}

void OAIConsentStatus::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIConsentStatus::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIConsentStatus::fromJson(QString jsonString) {
    
    if ( jsonString.compare("GRANTED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIConsentStatus::GRANTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EXPIRED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIConsentStatus::EXPIRED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DENIED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIConsentStatus::DENIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("REQUESTED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIConsentStatus::REQUESTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("REVOKED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIConsentStatus::REVOKED;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIConsentStatus::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIConsentStatus::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIConsentStatus::GRANTED:
            val = "GRANTED";
            break;
        case eOAIConsentStatus::EXPIRED:
            val = "EXPIRED";
            break;
        case eOAIConsentStatus::DENIED:
            val = "DENIED";
            break;
        case eOAIConsentStatus::REQUESTED:
            val = "REQUESTED";
            break;
        case eOAIConsentStatus::REVOKED:
            val = "REVOKED";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIConsentStatus::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIConsentStatus::eOAIConsentStatus OAIConsentStatus::getValue() const {
    return m_value;
}

void OAIConsentStatus::setValue(const OAIConsentStatus::eOAIConsentStatus& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIConsentStatus::isSet() const {
    
    return m_value_isSet;
}

bool OAIConsentStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
