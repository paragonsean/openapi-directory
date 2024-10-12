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

#include "OAIIssueTokenRequest_metadata_rules_fees.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssueTokenRequest_metadata_rules_fees::OAIIssueTokenRequest_metadata_rules_fees(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssueTokenRequest_metadata_rules_fees::OAIIssueTokenRequest_metadata_rules_fees() {
    this->initializeModel();
}

OAIIssueTokenRequest_metadata_rules_fees::~OAIIssueTokenRequest_metadata_rules_fees() {}

void OAIIssueTokenRequest_metadata_rules_fees::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;

    m_locked_isSet = false;
    m_locked_isValid = false;
}

void OAIIssueTokenRequest_metadata_rules_fees::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssueTokenRequest_metadata_rules_fees::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_locked_isValid = ::OpenAPI::fromJsonValue(m_locked, json[QString("locked")]);
    m_locked_isSet = !json[QString("locked")].isNull() && m_locked_isValid;
}

QString OAIIssueTokenRequest_metadata_rules_fees::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssueTokenRequest_metadata_rules_fees::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_locked_isSet) {
        obj.insert(QString("locked"), ::OpenAPI::toJsonValue(m_locked));
    }
    return obj;
}

QList<OAIIssueTokenRequest_metadata_rules_fees_items_inner> OAIIssueTokenRequest_metadata_rules_fees::getItems() const {
    return m_items;
}
void OAIIssueTokenRequest_metadata_rules_fees::setItems(const QList<OAIIssueTokenRequest_metadata_rules_fees_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIIssueTokenRequest_metadata_rules_fees::is_items_Set() const{
    return m_items_isSet;
}

bool OAIIssueTokenRequest_metadata_rules_fees::is_items_Valid() const{
    return m_items_isValid;
}

bool OAIIssueTokenRequest_metadata_rules_fees::isLocked() const {
    return m_locked;
}
void OAIIssueTokenRequest_metadata_rules_fees::setLocked(const bool &locked) {
    m_locked = locked;
    m_locked_isSet = true;
}

bool OAIIssueTokenRequest_metadata_rules_fees::is_locked_Set() const{
    return m_locked_isSet;
}

bool OAIIssueTokenRequest_metadata_rules_fees::is_locked_Valid() const{
    return m_locked_isValid;
}

bool OAIIssueTokenRequest_metadata_rules_fees::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_locked_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssueTokenRequest_metadata_rules_fees::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
