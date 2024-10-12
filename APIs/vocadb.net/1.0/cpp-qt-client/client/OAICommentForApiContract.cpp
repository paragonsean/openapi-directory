/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICommentForApiContract.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommentForApiContract::OAICommentForApiContract(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommentForApiContract::OAICommentForApiContract() {
    this->initializeModel();
}

OAICommentForApiContract::~OAICommentForApiContract() {}

void OAICommentForApiContract::initializeModel() {

    m_author_isSet = false;
    m_author_isValid = false;

    m_author_name_isSet = false;
    m_author_name_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_entry_isSet = false;
    m_entry_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAICommentForApiContract::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommentForApiContract::fromJsonObject(QJsonObject json) {

    m_author_isValid = ::OpenAPI::fromJsonValue(m_author, json[QString("author")]);
    m_author_isSet = !json[QString("author")].isNull() && m_author_isValid;

    m_author_name_isValid = ::OpenAPI::fromJsonValue(m_author_name, json[QString("authorName")]);
    m_author_name_isSet = !json[QString("authorName")].isNull() && m_author_name_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_entry_isValid = ::OpenAPI::fromJsonValue(m_entry, json[QString("entry")]);
    m_entry_isSet = !json[QString("entry")].isNull() && m_entry_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAICommentForApiContract::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommentForApiContract::asJsonObject() const {
    QJsonObject obj;
    if (m_author.isSet()) {
        obj.insert(QString("author"), ::OpenAPI::toJsonValue(m_author));
    }
    if (m_author_name_isSet) {
        obj.insert(QString("authorName"), ::OpenAPI::toJsonValue(m_author_name));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_entry.isSet()) {
        obj.insert(QString("entry"), ::OpenAPI::toJsonValue(m_entry));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

OAIUserForApiContract OAICommentForApiContract::getAuthor() const {
    return m_author;
}
void OAICommentForApiContract::setAuthor(const OAIUserForApiContract &author) {
    m_author = author;
    m_author_isSet = true;
}

bool OAICommentForApiContract::is_author_Set() const{
    return m_author_isSet;
}

bool OAICommentForApiContract::is_author_Valid() const{
    return m_author_isValid;
}

QString OAICommentForApiContract::getAuthorName() const {
    return m_author_name;
}
void OAICommentForApiContract::setAuthorName(const QString &author_name) {
    m_author_name = author_name;
    m_author_name_isSet = true;
}

bool OAICommentForApiContract::is_author_name_Set() const{
    return m_author_name_isSet;
}

bool OAICommentForApiContract::is_author_name_Valid() const{
    return m_author_name_isValid;
}

QDateTime OAICommentForApiContract::getCreated() const {
    return m_created;
}
void OAICommentForApiContract::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAICommentForApiContract::is_created_Set() const{
    return m_created_isSet;
}

bool OAICommentForApiContract::is_created_Valid() const{
    return m_created_isValid;
}

OAIEntryForApiContract OAICommentForApiContract::getEntry() const {
    return m_entry;
}
void OAICommentForApiContract::setEntry(const OAIEntryForApiContract &entry) {
    m_entry = entry;
    m_entry_isSet = true;
}

bool OAICommentForApiContract::is_entry_Set() const{
    return m_entry_isSet;
}

bool OAICommentForApiContract::is_entry_Valid() const{
    return m_entry_isValid;
}

qint32 OAICommentForApiContract::getId() const {
    return m_id;
}
void OAICommentForApiContract::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICommentForApiContract::is_id_Set() const{
    return m_id_isSet;
}

bool OAICommentForApiContract::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICommentForApiContract::getMessage() const {
    return m_message;
}
void OAICommentForApiContract::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAICommentForApiContract::is_message_Set() const{
    return m_message_isSet;
}

bool OAICommentForApiContract::is_message_Valid() const{
    return m_message_isValid;
}

bool OAICommentForApiContract::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_author.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_author_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entry.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICommentForApiContract::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
