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

#include "OAIDiscussionFolderContract.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiscussionFolderContract::OAIDiscussionFolderContract(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiscussionFolderContract::OAIDiscussionFolderContract() {
    this->initializeModel();
}

OAIDiscussionFolderContract::~OAIDiscussionFolderContract() {}

void OAIDiscussionFolderContract::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_topic_author_isSet = false;
    m_last_topic_author_isValid = false;

    m_last_topic_date_isSet = false;
    m_last_topic_date_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_topic_count_isSet = false;
    m_topic_count_isValid = false;
}

void OAIDiscussionFolderContract::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiscussionFolderContract::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_topic_author_isValid = ::OpenAPI::fromJsonValue(m_last_topic_author, json[QString("lastTopicAuthor")]);
    m_last_topic_author_isSet = !json[QString("lastTopicAuthor")].isNull() && m_last_topic_author_isValid;

    m_last_topic_date_isValid = ::OpenAPI::fromJsonValue(m_last_topic_date, json[QString("lastTopicDate")]);
    m_last_topic_date_isSet = !json[QString("lastTopicDate")].isNull() && m_last_topic_date_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_topic_count_isValid = ::OpenAPI::fromJsonValue(m_topic_count, json[QString("topicCount")]);
    m_topic_count_isSet = !json[QString("topicCount")].isNull() && m_topic_count_isValid;
}

QString OAIDiscussionFolderContract::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiscussionFolderContract::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_topic_author.isSet()) {
        obj.insert(QString("lastTopicAuthor"), ::OpenAPI::toJsonValue(m_last_topic_author));
    }
    if (m_last_topic_date_isSet) {
        obj.insert(QString("lastTopicDate"), ::OpenAPI::toJsonValue(m_last_topic_date));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_topic_count_isSet) {
        obj.insert(QString("topicCount"), ::OpenAPI::toJsonValue(m_topic_count));
    }
    return obj;
}

QString OAIDiscussionFolderContract::getDescription() const {
    return m_description;
}
void OAIDiscussionFolderContract::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIDiscussionFolderContract::is_description_Set() const{
    return m_description_isSet;
}

bool OAIDiscussionFolderContract::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIDiscussionFolderContract::getId() const {
    return m_id;
}
void OAIDiscussionFolderContract::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDiscussionFolderContract::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDiscussionFolderContract::is_id_Valid() const{
    return m_id_isValid;
}

OAIUserForApiContract OAIDiscussionFolderContract::getLastTopicAuthor() const {
    return m_last_topic_author;
}
void OAIDiscussionFolderContract::setLastTopicAuthor(const OAIUserForApiContract &last_topic_author) {
    m_last_topic_author = last_topic_author;
    m_last_topic_author_isSet = true;
}

bool OAIDiscussionFolderContract::is_last_topic_author_Set() const{
    return m_last_topic_author_isSet;
}

bool OAIDiscussionFolderContract::is_last_topic_author_Valid() const{
    return m_last_topic_author_isValid;
}

QDateTime OAIDiscussionFolderContract::getLastTopicDate() const {
    return m_last_topic_date;
}
void OAIDiscussionFolderContract::setLastTopicDate(const QDateTime &last_topic_date) {
    m_last_topic_date = last_topic_date;
    m_last_topic_date_isSet = true;
}

bool OAIDiscussionFolderContract::is_last_topic_date_Set() const{
    return m_last_topic_date_isSet;
}

bool OAIDiscussionFolderContract::is_last_topic_date_Valid() const{
    return m_last_topic_date_isValid;
}

QString OAIDiscussionFolderContract::getName() const {
    return m_name;
}
void OAIDiscussionFolderContract::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDiscussionFolderContract::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDiscussionFolderContract::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIDiscussionFolderContract::getTopicCount() const {
    return m_topic_count;
}
void OAIDiscussionFolderContract::setTopicCount(const qint32 &topic_count) {
    m_topic_count = topic_count;
    m_topic_count_isSet = true;
}

bool OAIDiscussionFolderContract::is_topic_count_Set() const{
    return m_topic_count_isSet;
}

bool OAIDiscussionFolderContract::is_topic_count_Valid() const{
    return m_topic_count_isValid;
}

bool OAIDiscussionFolderContract::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_topic_author.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_topic_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_topic_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiscussionFolderContract::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
