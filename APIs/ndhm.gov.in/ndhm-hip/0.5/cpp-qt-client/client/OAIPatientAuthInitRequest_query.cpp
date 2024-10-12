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

#include "OAIPatientAuthInitRequest_query.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientAuthInitRequest_query::OAIPatientAuthInitRequest_query(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientAuthInitRequest_query::OAIPatientAuthInitRequest_query() {
    this->initializeModel();
}

OAIPatientAuthInitRequest_query::~OAIPatientAuthInitRequest_query() {}

void OAIPatientAuthInitRequest_query::initializeModel() {

    m_auth_mode_isSet = false;
    m_auth_mode_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_purpose_isSet = false;
    m_purpose_isValid = false;

    m_requester_isSet = false;
    m_requester_isValid = false;
}

void OAIPatientAuthInitRequest_query::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientAuthInitRequest_query::fromJsonObject(QJsonObject json) {

    m_auth_mode_isValid = ::OpenAPI::fromJsonValue(m_auth_mode, json[QString("authMode")]);
    m_auth_mode_isSet = !json[QString("authMode")].isNull() && m_auth_mode_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_purpose_isValid = ::OpenAPI::fromJsonValue(m_purpose, json[QString("purpose")]);
    m_purpose_isSet = !json[QString("purpose")].isNull() && m_purpose_isValid;

    m_requester_isValid = ::OpenAPI::fromJsonValue(m_requester, json[QString("requester")]);
    m_requester_isSet = !json[QString("requester")].isNull() && m_requester_isValid;
}

QString OAIPatientAuthInitRequest_query::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientAuthInitRequest_query::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_mode.isSet()) {
        obj.insert(QString("authMode"), ::OpenAPI::toJsonValue(m_auth_mode));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_purpose.isSet()) {
        obj.insert(QString("purpose"), ::OpenAPI::toJsonValue(m_purpose));
    }
    if (m_requester.isSet()) {
        obj.insert(QString("requester"), ::OpenAPI::toJsonValue(m_requester));
    }
    return obj;
}

OAIAuthenticationMode OAIPatientAuthInitRequest_query::getAuthMode() const {
    return m_auth_mode;
}
void OAIPatientAuthInitRequest_query::setAuthMode(const OAIAuthenticationMode &auth_mode) {
    m_auth_mode = auth_mode;
    m_auth_mode_isSet = true;
}

bool OAIPatientAuthInitRequest_query::is_auth_mode_Set() const{
    return m_auth_mode_isSet;
}

bool OAIPatientAuthInitRequest_query::is_auth_mode_Valid() const{
    return m_auth_mode_isValid;
}

QString OAIPatientAuthInitRequest_query::getId() const {
    return m_id;
}
void OAIPatientAuthInitRequest_query::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatientAuthInitRequest_query::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatientAuthInitRequest_query::is_id_Valid() const{
    return m_id_isValid;
}

OAIPatientAuthPurpose OAIPatientAuthInitRequest_query::getPurpose() const {
    return m_purpose;
}
void OAIPatientAuthInitRequest_query::setPurpose(const OAIPatientAuthPurpose &purpose) {
    m_purpose = purpose;
    m_purpose_isSet = true;
}

bool OAIPatientAuthInitRequest_query::is_purpose_Set() const{
    return m_purpose_isSet;
}

bool OAIPatientAuthInitRequest_query::is_purpose_Valid() const{
    return m_purpose_isValid;
}

OAIPatientAuthInitRequest_query_requester OAIPatientAuthInitRequest_query::getRequester() const {
    return m_requester;
}
void OAIPatientAuthInitRequest_query::setRequester(const OAIPatientAuthInitRequest_query_requester &requester) {
    m_requester = requester;
    m_requester_isSet = true;
}

bool OAIPatientAuthInitRequest_query::is_requester_Set() const{
    return m_requester_isSet;
}

bool OAIPatientAuthInitRequest_query::is_requester_Valid() const{
    return m_requester_isValid;
}

bool OAIPatientAuthInitRequest_query::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_mode.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purpose.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_requester.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientAuthInitRequest_query::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_purpose_isValid && m_requester_isValid && true;
}

} // namespace OpenAPI
