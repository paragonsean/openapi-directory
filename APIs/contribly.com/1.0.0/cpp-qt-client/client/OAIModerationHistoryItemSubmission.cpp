/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIModerationHistoryItemSubmission.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIModerationHistoryItemSubmission::OAIModerationHistoryItemSubmission(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIModerationHistoryItemSubmission::OAIModerationHistoryItemSubmission() {
    this->initializeModel();
}

OAIModerationHistoryItemSubmission::~OAIModerationHistoryItemSubmission() {}

void OAIModerationHistoryItemSubmission::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;
}

void OAIModerationHistoryItemSubmission::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIModerationHistoryItemSubmission::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;
}

QString OAIModerationHistoryItemSubmission::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIModerationHistoryItemSubmission::asJsonObject() const {
    QJsonObject obj;
    if (m_action.isSet()) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    return obj;
}

OAIModerationAction OAIModerationHistoryItemSubmission::getAction() const {
    return m_action;
}
void OAIModerationHistoryItemSubmission::setAction(const OAIModerationAction &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIModerationHistoryItemSubmission::is_action_Set() const{
    return m_action_isSet;
}

bool OAIModerationHistoryItemSubmission::is_action_Valid() const{
    return m_action_isValid;
}

QString OAIModerationHistoryItemSubmission::getNotes() const {
    return m_notes;
}
void OAIModerationHistoryItemSubmission::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIModerationHistoryItemSubmission::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIModerationHistoryItemSubmission::is_notes_Valid() const{
    return m_notes_isValid;
}

bool OAIModerationHistoryItemSubmission::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIModerationHistoryItemSubmission::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
