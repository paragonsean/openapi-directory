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

#include "OAIShareProfileAcknowledgement.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShareProfileAcknowledgement::OAIShareProfileAcknowledgement(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShareProfileAcknowledgement::OAIShareProfileAcknowledgement() {
    this->initializeModel();
}

OAIShareProfileAcknowledgement::~OAIShareProfileAcknowledgement() {}

void OAIShareProfileAcknowledgement::initializeModel() {

    m_health_id_isSet = false;
    m_health_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIShareProfileAcknowledgement::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShareProfileAcknowledgement::fromJsonObject(QJsonObject json) {

    m_health_id_isValid = ::OpenAPI::fromJsonValue(m_health_id, json[QString("healthId")]);
    m_health_id_isSet = !json[QString("healthId")].isNull() && m_health_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIShareProfileAcknowledgement::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShareProfileAcknowledgement::asJsonObject() const {
    QJsonObject obj;
    if (m_health_id_isSet) {
        obj.insert(QString("healthId"), ::OpenAPI::toJsonValue(m_health_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIShareProfileAcknowledgement::getHealthId() const {
    return m_health_id;
}
void OAIShareProfileAcknowledgement::setHealthId(const QString &health_id) {
    m_health_id = health_id;
    m_health_id_isSet = true;
}

bool OAIShareProfileAcknowledgement::is_health_id_Set() const{
    return m_health_id_isSet;
}

bool OAIShareProfileAcknowledgement::is_health_id_Valid() const{
    return m_health_id_isValid;
}

QString OAIShareProfileAcknowledgement::getStatus() const {
    return m_status;
}
void OAIShareProfileAcknowledgement::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIShareProfileAcknowledgement::is_status_Set() const{
    return m_status_isSet;
}

bool OAIShareProfileAcknowledgement::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIShareProfileAcknowledgement::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_health_id_isSet) {
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

bool OAIShareProfileAcknowledgement::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_health_id_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
