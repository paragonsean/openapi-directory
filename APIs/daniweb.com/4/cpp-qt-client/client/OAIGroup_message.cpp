/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGroup_message.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroup_message::OAIGroup_message(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroup_message::OAIGroup_message() {
    this->initializeModel();
}

OAIGroup_message::~OAIGroup_message() {}

void OAIGroup_message::initializeModel() {

    m_author_isSet = false;
    m_author_isValid = false;

    m_group_isSet = false;
    m_group_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_seen_isSet = false;
    m_last_seen_isValid = false;

    m_moderated_isSet = false;
    m_moderated_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIGroup_message::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroup_message::fromJsonObject(QJsonObject json) {

    m_author_isValid = ::OpenAPI::fromJsonValue(m_author, json[QString("author")]);
    m_author_isSet = !json[QString("author")].isNull() && m_author_isValid;

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_seen_isValid = ::OpenAPI::fromJsonValue(m_last_seen, json[QString("last_seen")]);
    m_last_seen_isSet = !json[QString("last_seen")].isNull() && m_last_seen_isValid;

    m_moderated_isValid = ::OpenAPI::fromJsonValue(m_moderated, json[QString("moderated")]);
    m_moderated_isSet = !json[QString("moderated")].isNull() && m_moderated_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIGroup_message::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroup_message::asJsonObject() const {
    QJsonObject obj;
    if (m_author.isSet()) {
        obj.insert(QString("author"), ::OpenAPI::toJsonValue(m_author));
    }
    if (m_group.isSet()) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_seen.isSet()) {
        obj.insert(QString("last_seen"), ::OpenAPI::toJsonValue(m_last_seen));
    }
    if (m_moderated.isSet()) {
        obj.insert(QString("moderated"), ::OpenAPI::toJsonValue(m_moderated));
    }
    if (m_text.isSet()) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIUser OAIGroup_message::getAuthor() const {
    return m_author;
}
void OAIGroup_message::setAuthor(const OAIUser &author) {
    m_author = author;
    m_author_isSet = true;
}

bool OAIGroup_message::is_author_Set() const{
    return m_author_isSet;
}

bool OAIGroup_message::is_author_Valid() const{
    return m_author_isValid;
}

OAIGroup OAIGroup_message::getGroup() const {
    return m_group;
}
void OAIGroup_message::setGroup(const OAIGroup &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAIGroup_message::is_group_Set() const{
    return m_group_isSet;
}

bool OAIGroup_message::is_group_Valid() const{
    return m_group_isValid;
}

double OAIGroup_message::getId() const {
    return m_id;
}
void OAIGroup_message::setId(const double &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGroup_message::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGroup_message::is_id_Valid() const{
    return m_id_isValid;
}

OAIGroup_message_last_seen OAIGroup_message::getLastSeen() const {
    return m_last_seen;
}
void OAIGroup_message::setLastSeen(const OAIGroup_message_last_seen &last_seen) {
    m_last_seen = last_seen;
    m_last_seen_isSet = true;
}

bool OAIGroup_message::is_last_seen_Set() const{
    return m_last_seen_isSet;
}

bool OAIGroup_message::is_last_seen_Valid() const{
    return m_last_seen_isValid;
}

OAIGroup_message_moderated OAIGroup_message::getModerated() const {
    return m_moderated;
}
void OAIGroup_message::setModerated(const OAIGroup_message_moderated &moderated) {
    m_moderated = moderated;
    m_moderated_isSet = true;
}

bool OAIGroup_message::is_moderated_Set() const{
    return m_moderated_isSet;
}

bool OAIGroup_message::is_moderated_Valid() const{
    return m_moderated_isValid;
}

OAIGroup_message_text OAIGroup_message::getText() const {
    return m_text;
}
void OAIGroup_message::setText(const OAIGroup_message_text &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIGroup_message::is_text_Set() const{
    return m_text_isSet;
}

bool OAIGroup_message::is_text_Valid() const{
    return m_text_isValid;
}

QDateTime OAIGroup_message::getTimestamp() const {
    return m_timestamp;
}
void OAIGroup_message::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIGroup_message::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIGroup_message::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIGroup_message::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_author.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_group.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_seen.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_moderated.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_text.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGroup_message::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
