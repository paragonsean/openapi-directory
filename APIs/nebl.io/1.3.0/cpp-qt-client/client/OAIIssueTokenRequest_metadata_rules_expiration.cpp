/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIssueTokenRequest_metadata_rules_expiration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssueTokenRequest_metadata_rules_expiration::OAIIssueTokenRequest_metadata_rules_expiration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssueTokenRequest_metadata_rules_expiration::OAIIssueTokenRequest_metadata_rules_expiration() {
    this->initializeModel();
}

OAIIssueTokenRequest_metadata_rules_expiration::~OAIIssueTokenRequest_metadata_rules_expiration() {}

void OAIIssueTokenRequest_metadata_rules_expiration::initializeModel() {

    m_locked_isSet = false;
    m_locked_isValid = false;

    m_valid_until_isSet = false;
    m_valid_until_isValid = false;
}

void OAIIssueTokenRequest_metadata_rules_expiration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssueTokenRequest_metadata_rules_expiration::fromJsonObject(QJsonObject json) {

    m_locked_isValid = ::OpenAPI::fromJsonValue(m_locked, json[QString("locked")]);
    m_locked_isSet = !json[QString("locked")].isNull() && m_locked_isValid;

    m_valid_until_isValid = ::OpenAPI::fromJsonValue(m_valid_until, json[QString("validUntil")]);
    m_valid_until_isSet = !json[QString("validUntil")].isNull() && m_valid_until_isValid;
}

QString OAIIssueTokenRequest_metadata_rules_expiration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssueTokenRequest_metadata_rules_expiration::asJsonObject() const {
    QJsonObject obj;
    if (m_locked_isSet) {
        obj.insert(QString("locked"), ::OpenAPI::toJsonValue(m_locked));
    }
    if (m_valid_until_isSet) {
        obj.insert(QString("validUntil"), ::OpenAPI::toJsonValue(m_valid_until));
    }
    return obj;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::isLocked() const {
    return m_locked;
}
void OAIIssueTokenRequest_metadata_rules_expiration::setLocked(const bool &locked) {
    m_locked = locked;
    m_locked_isSet = true;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::is_locked_Set() const{
    return m_locked_isSet;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::is_locked_Valid() const{
    return m_locked_isValid;
}

double OAIIssueTokenRequest_metadata_rules_expiration::getValidUntil() const {
    return m_valid_until;
}
void OAIIssueTokenRequest_metadata_rules_expiration::setValidUntil(const double &valid_until) {
    m_valid_until = valid_until;
    m_valid_until_isSet = true;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::is_valid_until_Set() const{
    return m_valid_until_isSet;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::is_valid_until_Valid() const{
    return m_valid_until_isValid;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_locked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_valid_until_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssueTokenRequest_metadata_rules_expiration::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
