/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHistoryResponseItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHistoryResponseItem::OAIHistoryResponseItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHistoryResponseItem::OAIHistoryResponseItem() {
    this->initializeModel();
}

OAIHistoryResponseItem::~OAIHistoryResponseItem() {}

void OAIHistoryResponseItem::initializeModel() {

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAIHistoryResponseItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHistoryResponseItem::fromJsonObject(QJsonObject json) {

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("Comment")]);
    m_comment_isSet = !json[QString("Comment")].isNull() && m_comment_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("Created")]);
    m_created_isSet = !json[QString("Created")].isNull() && m_created_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("CreatedBy")]);
    m_created_by_isSet = !json[QString("CreatedBy")].isNull() && m_created_by_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("Size")]);
    m_size_isSet = !json[QString("Size")].isNull() && m_size_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("Tags")]);
    m_tags_isSet = !json[QString("Tags")].isNull() && m_tags_isValid;
}

QString OAIHistoryResponseItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHistoryResponseItem::asJsonObject() const {
    QJsonObject obj;
    if (m_comment_isSet) {
        obj.insert(QString("Comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_created_isSet) {
        obj.insert(QString("Created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("CreatedBy"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_size_isSet) {
        obj.insert(QString("Size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("Tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

QString OAIHistoryResponseItem::getComment() const {
    return m_comment;
}
void OAIHistoryResponseItem::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAIHistoryResponseItem::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAIHistoryResponseItem::is_comment_Valid() const{
    return m_comment_isValid;
}

qint64 OAIHistoryResponseItem::getCreated() const {
    return m_created;
}
void OAIHistoryResponseItem::setCreated(const qint64 &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIHistoryResponseItem::is_created_Set() const{
    return m_created_isSet;
}

bool OAIHistoryResponseItem::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIHistoryResponseItem::getCreatedBy() const {
    return m_created_by;
}
void OAIHistoryResponseItem::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIHistoryResponseItem::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIHistoryResponseItem::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QString OAIHistoryResponseItem::getId() const {
    return m_id;
}
void OAIHistoryResponseItem::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIHistoryResponseItem::is_id_Set() const{
    return m_id_isSet;
}

bool OAIHistoryResponseItem::is_id_Valid() const{
    return m_id_isValid;
}

qint64 OAIHistoryResponseItem::getSize() const {
    return m_size;
}
void OAIHistoryResponseItem::setSize(const qint64 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIHistoryResponseItem::is_size_Set() const{
    return m_size_isSet;
}

bool OAIHistoryResponseItem::is_size_Valid() const{
    return m_size_isValid;
}

QList<QString> OAIHistoryResponseItem::getTags() const {
    return m_tags;
}
void OAIHistoryResponseItem::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIHistoryResponseItem::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIHistoryResponseItem::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAIHistoryResponseItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHistoryResponseItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_comment_isValid && m_created_isValid && m_created_by_isValid && m_id_isValid && m_size_isValid && m_tags_isValid && true;
}

} // namespace OpenAPI
