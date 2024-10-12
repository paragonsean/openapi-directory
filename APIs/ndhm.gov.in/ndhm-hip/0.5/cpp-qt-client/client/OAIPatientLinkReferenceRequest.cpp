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

#include "OAIPatientLinkReferenceRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientLinkReferenceRequest::OAIPatientLinkReferenceRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientLinkReferenceRequest::OAIPatientLinkReferenceRequest() {
    this->initializeModel();
}

OAIPatientLinkReferenceRequest::~OAIPatientLinkReferenceRequest() {}

void OAIPatientLinkReferenceRequest::initializeModel() {

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_transaction_id_isSet = false;
    m_transaction_id_isValid = false;
}

void OAIPatientLinkReferenceRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientLinkReferenceRequest::fromJsonObject(QJsonObject json) {

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_id, json[QString("transactionId")]);
    m_transaction_id_isSet = !json[QString("transactionId")].isNull() && m_transaction_id_isValid;
}

QString OAIPatientLinkReferenceRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientLinkReferenceRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_patient.isSet()) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
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

OAIPatientLinkReferenceRequest_patient OAIPatientLinkReferenceRequest::getPatient() const {
    return m_patient;
}
void OAIPatientLinkReferenceRequest::setPatient(const OAIPatientLinkReferenceRequest_patient &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientLinkReferenceRequest::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientLinkReferenceRequest::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIPatientLinkReferenceRequest::getRequestId() const {
    return m_request_id;
}
void OAIPatientLinkReferenceRequest::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientLinkReferenceRequest::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientLinkReferenceRequest::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QDateTime OAIPatientLinkReferenceRequest::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientLinkReferenceRequest::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientLinkReferenceRequest::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientLinkReferenceRequest::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAIPatientLinkReferenceRequest::getTransactionId() const {
    return m_transaction_id;
}
void OAIPatientLinkReferenceRequest::setTransactionId(const QString &transaction_id) {
    m_transaction_id = transaction_id;
    m_transaction_id_isSet = true;
}

bool OAIPatientLinkReferenceRequest::is_transaction_id_Set() const{
    return m_transaction_id_isSet;
}

bool OAIPatientLinkReferenceRequest::is_transaction_id_Valid() const{
    return m_transaction_id_isValid;
}

bool OAIPatientLinkReferenceRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_patient.isSet()) {
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

bool OAIPatientLinkReferenceRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_patient_isValid && m_request_id_isValid && m_timestamp_isValid && m_transaction_id_isValid && true;
}

} // namespace OpenAPI
