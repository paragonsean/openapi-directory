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

#include "OAIPatientAuthConfirmRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientAuthConfirmRequest::OAIPatientAuthConfirmRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientAuthConfirmRequest::OAIPatientAuthConfirmRequest() {
    this->initializeModel();
}

OAIPatientAuthConfirmRequest::~OAIPatientAuthConfirmRequest() {}

void OAIPatientAuthConfirmRequest::initializeModel() {

    m_credential_isSet = false;
    m_credential_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_transaction_id_isSet = false;
    m_transaction_id_isValid = false;
}

void OAIPatientAuthConfirmRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientAuthConfirmRequest::fromJsonObject(QJsonObject json) {

    m_credential_isValid = ::OpenAPI::fromJsonValue(m_credential, json[QString("credential")]);
    m_credential_isSet = !json[QString("credential")].isNull() && m_credential_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_id, json[QString("transactionId")]);
    m_transaction_id_isSet = !json[QString("transactionId")].isNull() && m_transaction_id_isValid;
}

QString OAIPatientAuthConfirmRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientAuthConfirmRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_credential.isSet()) {
        obj.insert(QString("credential"), ::OpenAPI::toJsonValue(m_credential));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    if (m_transaction_id_isSet) {
        obj.insert(QString("transactionId"), ::OpenAPI::toJsonValue(m_transaction_id));
    }
    return obj;
}

OAIPatientAuthConfirmRequest_credential OAIPatientAuthConfirmRequest::getCredential() const {
    return m_credential;
}
void OAIPatientAuthConfirmRequest::setCredential(const OAIPatientAuthConfirmRequest_credential &credential) {
    m_credential = credential;
    m_credential_isSet = true;
}

bool OAIPatientAuthConfirmRequest::is_credential_Set() const{
    return m_credential_isSet;
}

bool OAIPatientAuthConfirmRequest::is_credential_Valid() const{
    return m_credential_isValid;
}

QString OAIPatientAuthConfirmRequest::getRequestId() const {
    return m_request_id;
}
void OAIPatientAuthConfirmRequest::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientAuthConfirmRequest::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientAuthConfirmRequest::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QDateTime OAIPatientAuthConfirmRequest::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientAuthConfirmRequest::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientAuthConfirmRequest::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientAuthConfirmRequest::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAIPatientAuthConfirmRequest::getTransactionId() const {
    return m_transaction_id;
}
void OAIPatientAuthConfirmRequest::setTransactionId(const QString &transaction_id) {
    m_transaction_id = transaction_id;
    m_transaction_id_isSet = true;
}

bool OAIPatientAuthConfirmRequest::is_transaction_id_Set() const{
    return m_transaction_id_isSet;
}

bool OAIPatientAuthConfirmRequest::is_transaction_id_Valid() const{
    return m_transaction_id_isValid;
}

bool OAIPatientAuthConfirmRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_credential.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientAuthConfirmRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_credential_isValid && m_request_id_isValid && m_timestamp_isValid && m_transaction_id_isValid && true;
}

} // namespace OpenAPI
