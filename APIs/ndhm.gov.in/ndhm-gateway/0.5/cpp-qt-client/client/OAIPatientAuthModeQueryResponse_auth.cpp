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

#include "OAIPatientAuthModeQueryResponse_auth.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientAuthModeQueryResponse_auth::OAIPatientAuthModeQueryResponse_auth(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientAuthModeQueryResponse_auth::OAIPatientAuthModeQueryResponse_auth() {
    this->initializeModel();
}

OAIPatientAuthModeQueryResponse_auth::~OAIPatientAuthModeQueryResponse_auth() {}

void OAIPatientAuthModeQueryResponse_auth::initializeModel() {

    m_modes_isSet = false;
    m_modes_isValid = false;

    m_purpose_isSet = false;
    m_purpose_isValid = false;
}

void OAIPatientAuthModeQueryResponse_auth::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientAuthModeQueryResponse_auth::fromJsonObject(QJsonObject json) {

    m_modes_isValid = ::OpenAPI::fromJsonValue(m_modes, json[QString("modes")]);
    m_modes_isSet = !json[QString("modes")].isNull() && m_modes_isValid;

    m_purpose_isValid = ::OpenAPI::fromJsonValue(m_purpose, json[QString("purpose")]);
    m_purpose_isSet = !json[QString("purpose")].isNull() && m_purpose_isValid;
}

QString OAIPatientAuthModeQueryResponse_auth::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientAuthModeQueryResponse_auth::asJsonObject() const {
    QJsonObject obj;
    if (m_modes.size() > 0) {
        obj.insert(QString("modes"), ::OpenAPI::toJsonValue(m_modes));
    }
    if (m_purpose.isSet()) {
        obj.insert(QString("purpose"), ::OpenAPI::toJsonValue(m_purpose));
    }
    return obj;
}

QList<OAIAuthenticationMode> OAIPatientAuthModeQueryResponse_auth::getModes() const {
    return m_modes;
}
void OAIPatientAuthModeQueryResponse_auth::setModes(const QList<OAIAuthenticationMode> &modes) {
    m_modes = modes;
    m_modes_isSet = true;
}

bool OAIPatientAuthModeQueryResponse_auth::is_modes_Set() const{
    return m_modes_isSet;
}

bool OAIPatientAuthModeQueryResponse_auth::is_modes_Valid() const{
    return m_modes_isValid;
}

OAIPatientAuthPurpose OAIPatientAuthModeQueryResponse_auth::getPurpose() const {
    return m_purpose;
}
void OAIPatientAuthModeQueryResponse_auth::setPurpose(const OAIPatientAuthPurpose &purpose) {
    m_purpose = purpose;
    m_purpose_isSet = true;
}

bool OAIPatientAuthModeQueryResponse_auth::is_purpose_Set() const{
    return m_purpose_isSet;
}

bool OAIPatientAuthModeQueryResponse_auth::is_purpose_Valid() const{
    return m_purpose_isValid;
}

bool OAIPatientAuthModeQueryResponse_auth::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_modes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_purpose.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientAuthModeQueryResponse_auth::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_modes_isValid && m_purpose_isValid && true;
}

} // namespace OpenAPI
