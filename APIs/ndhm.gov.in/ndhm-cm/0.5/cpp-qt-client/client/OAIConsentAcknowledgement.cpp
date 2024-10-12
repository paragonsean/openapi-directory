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

#include "OAIConsentAcknowledgement.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsentAcknowledgement::OAIConsentAcknowledgement(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsentAcknowledgement::OAIConsentAcknowledgement() {
    this->initializeModel();
}

OAIConsentAcknowledgement::~OAIConsentAcknowledgement() {}

void OAIConsentAcknowledgement::initializeModel() {

    m_consent_id_isSet = false;
    m_consent_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIConsentAcknowledgement::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConsentAcknowledgement::fromJsonObject(QJsonObject json) {

    m_consent_id_isValid = ::OpenAPI::fromJsonValue(m_consent_id, json[QString("consentId")]);
    m_consent_id_isSet = !json[QString("consentId")].isNull() && m_consent_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIConsentAcknowledgement::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConsentAcknowledgement::asJsonObject() const {
    QJsonObject obj;
    if (m_consent_id_isSet) {
        obj.insert(QString("consentId"), ::OpenAPI::toJsonValue(m_consent_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIConsentAcknowledgement::getConsentId() const {
    return m_consent_id;
}
void OAIConsentAcknowledgement::setConsentId(const QString &consent_id) {
    m_consent_id = consent_id;
    m_consent_id_isSet = true;
}

bool OAIConsentAcknowledgement::is_consent_id_Set() const{
    return m_consent_id_isSet;
}

bool OAIConsentAcknowledgement::is_consent_id_Valid() const{
    return m_consent_id_isValid;
}

QString OAIConsentAcknowledgement::getStatus() const {
    return m_status;
}
void OAIConsentAcknowledgement::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIConsentAcknowledgement::is_status_Set() const{
    return m_status_isSet;
}

bool OAIConsentAcknowledgement::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIConsentAcknowledgement::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_consent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConsentAcknowledgement::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_consent_id_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
