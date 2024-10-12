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

#include "OAIConsentArtefactResponse_consent.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsentArtefactResponse_consent::OAIConsentArtefactResponse_consent(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsentArtefactResponse_consent::OAIConsentArtefactResponse_consent() {
    this->initializeModel();
}

OAIConsentArtefactResponse_consent::~OAIConsentArtefactResponse_consent() {}

void OAIConsentArtefactResponse_consent::initializeModel() {

    m_consent_detail_isSet = false;
    m_consent_detail_isValid = false;

    m_signature_isSet = false;
    m_signature_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIConsentArtefactResponse_consent::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConsentArtefactResponse_consent::fromJsonObject(QJsonObject json) {

    m_consent_detail_isValid = ::OpenAPI::fromJsonValue(m_consent_detail, json[QString("consentDetail")]);
    m_consent_detail_isSet = !json[QString("consentDetail")].isNull() && m_consent_detail_isValid;

    m_signature_isValid = ::OpenAPI::fromJsonValue(m_signature, json[QString("signature")]);
    m_signature_isSet = !json[QString("signature")].isNull() && m_signature_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIConsentArtefactResponse_consent::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConsentArtefactResponse_consent::asJsonObject() const {
    QJsonObject obj;
    if (m_consent_detail.isSet()) {
        obj.insert(QString("consentDetail"), ::OpenAPI::toJsonValue(m_consent_detail));
    }
    if (m_signature_isSet) {
        obj.insert(QString("signature"), ::OpenAPI::toJsonValue(m_signature));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

OAIConsentArtefactResponse_consent_consentDetail OAIConsentArtefactResponse_consent::getConsentDetail() const {
    return m_consent_detail;
}
void OAIConsentArtefactResponse_consent::setConsentDetail(const OAIConsentArtefactResponse_consent_consentDetail &consent_detail) {
    m_consent_detail = consent_detail;
    m_consent_detail_isSet = true;
}

bool OAIConsentArtefactResponse_consent::is_consent_detail_Set() const{
    return m_consent_detail_isSet;
}

bool OAIConsentArtefactResponse_consent::is_consent_detail_Valid() const{
    return m_consent_detail_isValid;
}

QString OAIConsentArtefactResponse_consent::getSignature() const {
    return m_signature;
}
void OAIConsentArtefactResponse_consent::setSignature(const QString &signature) {
    m_signature = signature;
    m_signature_isSet = true;
}

bool OAIConsentArtefactResponse_consent::is_signature_Set() const{
    return m_signature_isSet;
}

bool OAIConsentArtefactResponse_consent::is_signature_Valid() const{
    return m_signature_isValid;
}

OAIConsentStatus OAIConsentArtefactResponse_consent::getStatus() const {
    return m_status;
}
void OAIConsentArtefactResponse_consent::setStatus(const OAIConsentStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIConsentArtefactResponse_consent::is_status_Set() const{
    return m_status_isSet;
}

bool OAIConsentArtefactResponse_consent::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIConsentArtefactResponse_consent::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_consent_detail.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_signature_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConsentArtefactResponse_consent::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_consent_detail_isValid && m_signature_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
