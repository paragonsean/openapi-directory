/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateFolderRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateFolderRequest::OAICreateFolderRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateFolderRequest::OAICreateFolderRequest() {
    this->initializeModel();
}

OAICreateFolderRequest::~OAICreateFolderRequest() {}

void OAICreateFolderRequest::initializeModel() {

    m_classification_isSet = false;
    m_classification_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_parent_id_isSet = false;
    m_parent_id_isValid = false;

    m_timestamp_creation_isSet = false;
    m_timestamp_creation_isValid = false;

    m_timestamp_modification_isSet = false;
    m_timestamp_modification_isValid = false;
}

void OAICreateFolderRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateFolderRequest::fromJsonObject(QJsonObject json) {

    m_classification_isValid = ::OpenAPI::fromJsonValue(m_classification, json[QString("classification")]);
    m_classification_isSet = !json[QString("classification")].isNull() && m_classification_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_parent_id_isValid = ::OpenAPI::fromJsonValue(m_parent_id, json[QString("parentId")]);
    m_parent_id_isSet = !json[QString("parentId")].isNull() && m_parent_id_isValid;

    m_timestamp_creation_isValid = ::OpenAPI::fromJsonValue(m_timestamp_creation, json[QString("timestampCreation")]);
    m_timestamp_creation_isSet = !json[QString("timestampCreation")].isNull() && m_timestamp_creation_isValid;

    m_timestamp_modification_isValid = ::OpenAPI::fromJsonValue(m_timestamp_modification, json[QString("timestampModification")]);
    m_timestamp_modification_isSet = !json[QString("timestampModification")].isNull() && m_timestamp_modification_isValid;
}

QString OAICreateFolderRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateFolderRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_classification_isSet) {
        obj.insert(QString("classification"), ::OpenAPI::toJsonValue(m_classification));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_parent_id_isSet) {
        obj.insert(QString("parentId"), ::OpenAPI::toJsonValue(m_parent_id));
    }
    if (m_timestamp_creation_isSet) {
        obj.insert(QString("timestampCreation"), ::OpenAPI::toJsonValue(m_timestamp_creation));
    }
    if (m_timestamp_modification_isSet) {
        obj.insert(QString("timestampModification"), ::OpenAPI::toJsonValue(m_timestamp_modification));
    }
    return obj;
}

qint32 OAICreateFolderRequest::getClassification() const {
    return m_classification;
}
void OAICreateFolderRequest::setClassification(const qint32 &classification) {
    m_classification = classification;
    m_classification_isSet = true;
}

bool OAICreateFolderRequest::is_classification_Set() const{
    return m_classification_isSet;
}

bool OAICreateFolderRequest::is_classification_Valid() const{
    return m_classification_isValid;
}

QString OAICreateFolderRequest::getName() const {
    return m_name;
}
void OAICreateFolderRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateFolderRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateFolderRequest::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICreateFolderRequest::getNotes() const {
    return m_notes;
}
void OAICreateFolderRequest::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAICreateFolderRequest::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAICreateFolderRequest::is_notes_Valid() const{
    return m_notes_isValid;
}

qint64 OAICreateFolderRequest::getParentId() const {
    return m_parent_id;
}
void OAICreateFolderRequest::setParentId(const qint64 &parent_id) {
    m_parent_id = parent_id;
    m_parent_id_isSet = true;
}

bool OAICreateFolderRequest::is_parent_id_Set() const{
    return m_parent_id_isSet;
}

bool OAICreateFolderRequest::is_parent_id_Valid() const{
    return m_parent_id_isValid;
}

QDateTime OAICreateFolderRequest::getTimestampCreation() const {
    return m_timestamp_creation;
}
void OAICreateFolderRequest::setTimestampCreation(const QDateTime &timestamp_creation) {
    m_timestamp_creation = timestamp_creation;
    m_timestamp_creation_isSet = true;
}

bool OAICreateFolderRequest::is_timestamp_creation_Set() const{
    return m_timestamp_creation_isSet;
}

bool OAICreateFolderRequest::is_timestamp_creation_Valid() const{
    return m_timestamp_creation_isValid;
}

QDateTime OAICreateFolderRequest::getTimestampModification() const {
    return m_timestamp_modification;
}
void OAICreateFolderRequest::setTimestampModification(const QDateTime &timestamp_modification) {
    m_timestamp_modification = timestamp_modification;
    m_timestamp_modification_isSet = true;
}

bool OAICreateFolderRequest::is_timestamp_modification_Set() const{
    return m_timestamp_modification_isSet;
}

bool OAICreateFolderRequest::is_timestamp_modification_Valid() const{
    return m_timestamp_modification_isValid;
}

bool OAICreateFolderRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_classification_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_creation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_modification_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateFolderRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_parent_id_isValid && true;
}

} // namespace OpenAPI
