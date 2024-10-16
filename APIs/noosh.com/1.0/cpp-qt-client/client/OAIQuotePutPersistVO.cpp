/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuotePutPersistVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuotePutPersistVO::OAIQuotePutPersistVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuotePutPersistVO::OAIQuotePutPersistVO() {
    this->initializeModel();
}

OAIQuotePutPersistVO::~OAIQuotePutPersistVO() {}

void OAIQuotePutPersistVO::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_po_number_isSet = false;
    m_po_number_isValid = false;

    m_quote_id_isSet = false;
    m_quote_id_isValid = false;

    m_state_change_comments_isSet = false;
    m_state_change_comments_isValid = false;
}

void OAIQuotePutPersistVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuotePutPersistVO::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_po_number_isValid = ::OpenAPI::fromJsonValue(m_po_number, json[QString("po_number")]);
    m_po_number_isSet = !json[QString("po_number")].isNull() && m_po_number_isValid;

    m_quote_id_isValid = ::OpenAPI::fromJsonValue(m_quote_id, json[QString("quote_id")]);
    m_quote_id_isSet = !json[QString("quote_id")].isNull() && m_quote_id_isValid;

    m_state_change_comments_isValid = ::OpenAPI::fromJsonValue(m_state_change_comments, json[QString("state_change_comments")]);
    m_state_change_comments_isSet = !json[QString("state_change_comments")].isNull() && m_state_change_comments_isValid;
}

QString OAIQuotePutPersistVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuotePutPersistVO::asJsonObject() const {
    QJsonObject obj;
    if (m_action_isSet) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_po_number_isSet) {
        obj.insert(QString("po_number"), ::OpenAPI::toJsonValue(m_po_number));
    }
    if (m_quote_id_isSet) {
        obj.insert(QString("quote_id"), ::OpenAPI::toJsonValue(m_quote_id));
    }
    if (m_state_change_comments_isSet) {
        obj.insert(QString("state_change_comments"), ::OpenAPI::toJsonValue(m_state_change_comments));
    }
    return obj;
}

QString OAIQuotePutPersistVO::getAction() const {
    return m_action;
}
void OAIQuotePutPersistVO::setAction(const QString &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIQuotePutPersistVO::is_action_Set() const{
    return m_action_isSet;
}

bool OAIQuotePutPersistVO::is_action_Valid() const{
    return m_action_isValid;
}

QString OAIQuotePutPersistVO::getPoNumber() const {
    return m_po_number;
}
void OAIQuotePutPersistVO::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAIQuotePutPersistVO::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAIQuotePutPersistVO::is_po_number_Valid() const{
    return m_po_number_isValid;
}

qint64 OAIQuotePutPersistVO::getQuoteId() const {
    return m_quote_id;
}
void OAIQuotePutPersistVO::setQuoteId(const qint64 &quote_id) {
    m_quote_id = quote_id;
    m_quote_id_isSet = true;
}

bool OAIQuotePutPersistVO::is_quote_id_Set() const{
    return m_quote_id_isSet;
}

bool OAIQuotePutPersistVO::is_quote_id_Valid() const{
    return m_quote_id_isValid;
}

QString OAIQuotePutPersistVO::getStateChangeComments() const {
    return m_state_change_comments;
}
void OAIQuotePutPersistVO::setStateChangeComments(const QString &state_change_comments) {
    m_state_change_comments = state_change_comments;
    m_state_change_comments_isSet = true;
}

bool OAIQuotePutPersistVO::is_state_change_comments_Set() const{
    return m_state_change_comments_isSet;
}

bool OAIQuotePutPersistVO::is_state_change_comments_Valid() const{
    return m_state_change_comments_isValid;
}

bool OAIQuotePutPersistVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_po_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_change_comments_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuotePutPersistVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
