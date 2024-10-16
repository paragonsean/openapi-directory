/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExportBlobConfiguration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExportBlobConfiguration::OAIExportBlobConfiguration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExportBlobConfiguration::OAIExportBlobConfiguration() {
    this->initializeModel();
}

OAIExportBlobConfiguration::~OAIExportBlobConfiguration() {}

void OAIExportBlobConfiguration::initializeModel() {

    m_blob_path_format_kind_isSet = false;
    m_blob_path_format_kind_isValid = false;

    m_backfill_isSet = false;
    m_backfill_isValid = false;

    m_export_entities_isSet = false;
    m_export_entities_isValid = false;

    m_resource_group_isSet = false;
    m_resource_group_isValid = false;

    m_resource_name_isSet = false;
    m_resource_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIExportBlobConfiguration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExportBlobConfiguration::fromJsonObject(QJsonObject json) {

    m_blob_path_format_kind_isValid = ::OpenAPI::fromJsonValue(m_blob_path_format_kind, json[QString("blob_path_format_kind")]);
    m_blob_path_format_kind_isSet = !json[QString("blob_path_format_kind")].isNull() && m_blob_path_format_kind_isValid;

    m_backfill_isValid = ::OpenAPI::fromJsonValue(m_backfill, json[QString("backfill")]);
    m_backfill_isSet = !json[QString("backfill")].isNull() && m_backfill_isValid;

    m_export_entities_isValid = ::OpenAPI::fromJsonValue(m_export_entities, json[QString("export_entities")]);
    m_export_entities_isSet = !json[QString("export_entities")].isNull() && m_export_entities_isValid;

    m_resource_group_isValid = ::OpenAPI::fromJsonValue(m_resource_group, json[QString("resource_group")]);
    m_resource_group_isSet = !json[QString("resource_group")].isNull() && m_resource_group_isValid;

    m_resource_name_isValid = ::OpenAPI::fromJsonValue(m_resource_name, json[QString("resource_name")]);
    m_resource_name_isSet = !json[QString("resource_name")].isNull() && m_resource_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIExportBlobConfiguration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExportBlobConfiguration::asJsonObject() const {
    QJsonObject obj;
    if (m_blob_path_format_kind_isSet) {
        obj.insert(QString("blob_path_format_kind"), ::OpenAPI::toJsonValue(m_blob_path_format_kind));
    }
    if (m_backfill_isSet) {
        obj.insert(QString("backfill"), ::OpenAPI::toJsonValue(m_backfill));
    }
    if (m_export_entities.size() > 0) {
        obj.insert(QString("export_entities"), ::OpenAPI::toJsonValue(m_export_entities));
    }
    if (m_resource_group_isSet) {
        obj.insert(QString("resource_group"), ::OpenAPI::toJsonValue(m_resource_group));
    }
    if (m_resource_name_isSet) {
        obj.insert(QString("resource_name"), ::OpenAPI::toJsonValue(m_resource_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIExportBlobConfiguration::getBlobPathFormatKind() const {
    return m_blob_path_format_kind;
}
void OAIExportBlobConfiguration::setBlobPathFormatKind(const QString &blob_path_format_kind) {
    m_blob_path_format_kind = blob_path_format_kind;
    m_blob_path_format_kind_isSet = true;
}

bool OAIExportBlobConfiguration::is_blob_path_format_kind_Set() const{
    return m_blob_path_format_kind_isSet;
}

bool OAIExportBlobConfiguration::is_blob_path_format_kind_Valid() const{
    return m_blob_path_format_kind_isValid;
}

bool OAIExportBlobConfiguration::isBackfill() const {
    return m_backfill;
}
void OAIExportBlobConfiguration::setBackfill(const bool &backfill) {
    m_backfill = backfill;
    m_backfill_isSet = true;
}

bool OAIExportBlobConfiguration::is_backfill_Set() const{
    return m_backfill_isSet;
}

bool OAIExportBlobConfiguration::is_backfill_Valid() const{
    return m_backfill_isValid;
}

QList<QString> OAIExportBlobConfiguration::getExportEntities() const {
    return m_export_entities;
}
void OAIExportBlobConfiguration::setExportEntities(const QList<QString> &export_entities) {
    m_export_entities = export_entities;
    m_export_entities_isSet = true;
}

bool OAIExportBlobConfiguration::is_export_entities_Set() const{
    return m_export_entities_isSet;
}

bool OAIExportBlobConfiguration::is_export_entities_Valid() const{
    return m_export_entities_isValid;
}

QString OAIExportBlobConfiguration::getResourceGroup() const {
    return m_resource_group;
}
void OAIExportBlobConfiguration::setResourceGroup(const QString &resource_group) {
    m_resource_group = resource_group;
    m_resource_group_isSet = true;
}

bool OAIExportBlobConfiguration::is_resource_group_Set() const{
    return m_resource_group_isSet;
}

bool OAIExportBlobConfiguration::is_resource_group_Valid() const{
    return m_resource_group_isValid;
}

QString OAIExportBlobConfiguration::getResourceName() const {
    return m_resource_name;
}
void OAIExportBlobConfiguration::setResourceName(const QString &resource_name) {
    m_resource_name = resource_name;
    m_resource_name_isSet = true;
}

bool OAIExportBlobConfiguration::is_resource_name_Set() const{
    return m_resource_name_isSet;
}

bool OAIExportBlobConfiguration::is_resource_name_Valid() const{
    return m_resource_name_isValid;
}

QString OAIExportBlobConfiguration::getType() const {
    return m_type;
}
void OAIExportBlobConfiguration::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIExportBlobConfiguration::is_type_Set() const{
    return m_type_isSet;
}

bool OAIExportBlobConfiguration::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIExportBlobConfiguration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_blob_path_format_kind_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_backfill_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_export_entities.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExportBlobConfiguration::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && true;
}

} // namespace OpenAPI
