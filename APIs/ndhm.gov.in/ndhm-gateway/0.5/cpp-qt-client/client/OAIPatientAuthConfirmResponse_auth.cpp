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

#include "OAIPatientAuthConfirmResponse_auth.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientAuthConfirmResponse_auth::OAIPatientAuthConfirmResponse_auth(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientAuthConfirmResponse_auth::OAIPatientAuthConfirmResponse_auth() {
    this->initializeModel();
}

OAIPatientAuthConfirmResponse_auth::~OAIPatientAuthConfirmResponse_auth() {}

void OAIPatientAuthConfirmResponse_auth::initializeModel() {

    m_access_token_isSet = false;
    m_access_token_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_validity_isSet = false;
    m_validity_isValid = false;
}

void OAIPatientAuthConfirmResponse_auth::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientAuthConfirmResponse_auth::fromJsonObject(QJsonObject json) {

    m_access_token_isValid = ::OpenAPI::fromJsonValue(m_access_token, json[QString("accessToken")]);
    m_access_token_isSet = !json[QString("accessToken")].isNull() && m_access_token_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_validity_isValid = ::OpenAPI::fromJsonValue(m_validity, json[QString("validity")]);
    m_validity_isSet = !json[QString("validity")].isNull() && m_validity_isValid;
}

QString OAIPatientAuthConfirmResponse_auth::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientAuthConfirmResponse_auth::asJsonObject() const {
    QJsonObject obj;
    if (m_access_token_isSet) {
        obj.insert(QString("accessToken"), ::OpenAPI::toJsonValue(m_access_token));
    }
    if (m_patient.isSet()) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_validity.isSet()) {
        obj.insert(QString("validity"), ::OpenAPI::toJsonValue(m_validity));
    }
    return obj;
}

QString OAIPatientAuthConfirmResponse_auth::getAccessToken() const {
    return m_access_token;
}
void OAIPatientAuthConfirmResponse_auth::setAccessToken(const QString &access_token) {
    m_access_token = access_token;
    m_access_token_isSet = true;
}

bool OAIPatientAuthConfirmResponse_auth::is_access_token_Set() const{
    return m_access_token_isSet;
}

bool OAIPatientAuthConfirmResponse_auth::is_access_token_Valid() const{
    return m_access_token_isValid;
}

OAIPatientDemographicResponse OAIPatientAuthConfirmResponse_auth::getPatient() const {
    return m_patient;
}
void OAIPatientAuthConfirmResponse_auth::setPatient(const OAIPatientDemographicResponse &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientAuthConfirmResponse_auth::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientAuthConfirmResponse_auth::is_patient_Valid() const{
    return m_patient_isValid;
}

OAIAccessTokenValidity OAIPatientAuthConfirmResponse_auth::getValidity() const {
    return m_validity;
}
void OAIPatientAuthConfirmResponse_auth::setValidity(const OAIAccessTokenValidity &validity) {
    m_validity = validity;
    m_validity_isSet = true;
}

bool OAIPatientAuthConfirmResponse_auth::is_validity_Set() const{
    return m_validity_isSet;
}

bool OAIPatientAuthConfirmResponse_auth::is_validity_Valid() const{
    return m_validity_isValid;
}

bool OAIPatientAuthConfirmResponse_auth::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_validity.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientAuthConfirmResponse_auth::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
