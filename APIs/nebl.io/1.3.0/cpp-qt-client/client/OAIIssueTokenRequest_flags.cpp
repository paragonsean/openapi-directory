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

#include "OAIIssueTokenRequest_flags.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssueTokenRequest_flags::OAIIssueTokenRequest_flags(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssueTokenRequest_flags::OAIIssueTokenRequest_flags() {
    this->initializeModel();
}

OAIIssueTokenRequest_flags::~OAIIssueTokenRequest_flags() {}

void OAIIssueTokenRequest_flags::initializeModel() {

    m_split_change_isSet = false;
    m_split_change_isValid = false;
}

void OAIIssueTokenRequest_flags::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssueTokenRequest_flags::fromJsonObject(QJsonObject json) {

    m_split_change_isValid = ::OpenAPI::fromJsonValue(m_split_change, json[QString("splitChange")]);
    m_split_change_isSet = !json[QString("splitChange")].isNull() && m_split_change_isValid;
}

QString OAIIssueTokenRequest_flags::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssueTokenRequest_flags::asJsonObject() const {
    QJsonObject obj;
    if (m_split_change_isSet) {
        obj.insert(QString("splitChange"), ::OpenAPI::toJsonValue(m_split_change));
    }
    return obj;
}

bool OAIIssueTokenRequest_flags::isSplitChange() const {
    return m_split_change;
}
void OAIIssueTokenRequest_flags::setSplitChange(const bool &split_change) {
    m_split_change = split_change;
    m_split_change_isSet = true;
}

bool OAIIssueTokenRequest_flags::is_split_change_Set() const{
    return m_split_change_isSet;
}

bool OAIIssueTokenRequest_flags::is_split_change_Valid() const{
    return m_split_change_isValid;
}

bool OAIIssueTokenRequest_flags::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_split_change_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssueTokenRequest_flags::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
