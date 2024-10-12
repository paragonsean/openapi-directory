/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2015-05-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISyncFullSchemaTableColumn.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISyncFullSchemaTableColumn::OAISyncFullSchemaTableColumn(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISyncFullSchemaTableColumn::OAISyncFullSchemaTableColumn() {
    this->initializeModel();
}

OAISyncFullSchemaTableColumn::~OAISyncFullSchemaTableColumn() {}

void OAISyncFullSchemaTableColumn::initializeModel() {

    m_data_size_isSet = false;
    m_data_size_isValid = false;

    m_data_type_isSet = false;
    m_data_type_isValid = false;

    m_error_id_isSet = false;
    m_error_id_isValid = false;

    m_has_error_isSet = false;
    m_has_error_isValid = false;

    m_is_primary_key_isSet = false;
    m_is_primary_key_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_quoted_name_isSet = false;
    m_quoted_name_isValid = false;
}

void OAISyncFullSchemaTableColumn::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISyncFullSchemaTableColumn::fromJsonObject(QJsonObject json) {

    m_data_size_isValid = ::OpenAPI::fromJsonValue(m_data_size, json[QString("dataSize")]);
    m_data_size_isSet = !json[QString("dataSize")].isNull() && m_data_size_isValid;

    m_data_type_isValid = ::OpenAPI::fromJsonValue(m_data_type, json[QString("dataType")]);
    m_data_type_isSet = !json[QString("dataType")].isNull() && m_data_type_isValid;

    m_error_id_isValid = ::OpenAPI::fromJsonValue(m_error_id, json[QString("errorId")]);
    m_error_id_isSet = !json[QString("errorId")].isNull() && m_error_id_isValid;

    m_has_error_isValid = ::OpenAPI::fromJsonValue(m_has_error, json[QString("hasError")]);
    m_has_error_isSet = !json[QString("hasError")].isNull() && m_has_error_isValid;

    m_is_primary_key_isValid = ::OpenAPI::fromJsonValue(m_is_primary_key, json[QString("isPrimaryKey")]);
    m_is_primary_key_isSet = !json[QString("isPrimaryKey")].isNull() && m_is_primary_key_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_quoted_name_isValid = ::OpenAPI::fromJsonValue(m_quoted_name, json[QString("quotedName")]);
    m_quoted_name_isSet = !json[QString("quotedName")].isNull() && m_quoted_name_isValid;
}

QString OAISyncFullSchemaTableColumn::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISyncFullSchemaTableColumn::asJsonObject() const {
    QJsonObject obj;
    if (m_data_size_isSet) {
        obj.insert(QString("dataSize"), ::OpenAPI::toJsonValue(m_data_size));
    }
    if (m_data_type_isSet) {
        obj.insert(QString("dataType"), ::OpenAPI::toJsonValue(m_data_type));
    }
    if (m_error_id_isSet) {
        obj.insert(QString("errorId"), ::OpenAPI::toJsonValue(m_error_id));
    }
    if (m_has_error_isSet) {
        obj.insert(QString("hasError"), ::OpenAPI::toJsonValue(m_has_error));
    }
    if (m_is_primary_key_isSet) {
        obj.insert(QString("isPrimaryKey"), ::OpenAPI::toJsonValue(m_is_primary_key));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_quoted_name_isSet) {
        obj.insert(QString("quotedName"), ::OpenAPI::toJsonValue(m_quoted_name));
    }
    return obj;
}

QString OAISyncFullSchemaTableColumn::getDataSize() const {
    return m_data_size;
}
void OAISyncFullSchemaTableColumn::setDataSize(const QString &data_size) {
    m_data_size = data_size;
    m_data_size_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_data_size_Set() const{
    return m_data_size_isSet;
}

bool OAISyncFullSchemaTableColumn::is_data_size_Valid() const{
    return m_data_size_isValid;
}

QString OAISyncFullSchemaTableColumn::getDataType() const {
    return m_data_type;
}
void OAISyncFullSchemaTableColumn::setDataType(const QString &data_type) {
    m_data_type = data_type;
    m_data_type_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_data_type_Set() const{
    return m_data_type_isSet;
}

bool OAISyncFullSchemaTableColumn::is_data_type_Valid() const{
    return m_data_type_isValid;
}

QString OAISyncFullSchemaTableColumn::getErrorId() const {
    return m_error_id;
}
void OAISyncFullSchemaTableColumn::setErrorId(const QString &error_id) {
    m_error_id = error_id;
    m_error_id_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_error_id_Set() const{
    return m_error_id_isSet;
}

bool OAISyncFullSchemaTableColumn::is_error_id_Valid() const{
    return m_error_id_isValid;
}

bool OAISyncFullSchemaTableColumn::isHasError() const {
    return m_has_error;
}
void OAISyncFullSchemaTableColumn::setHasError(const bool &has_error) {
    m_has_error = has_error;
    m_has_error_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_has_error_Set() const{
    return m_has_error_isSet;
}

bool OAISyncFullSchemaTableColumn::is_has_error_Valid() const{
    return m_has_error_isValid;
}

bool OAISyncFullSchemaTableColumn::isIsPrimaryKey() const {
    return m_is_primary_key;
}
void OAISyncFullSchemaTableColumn::setIsPrimaryKey(const bool &is_primary_key) {
    m_is_primary_key = is_primary_key;
    m_is_primary_key_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_is_primary_key_Set() const{
    return m_is_primary_key_isSet;
}

bool OAISyncFullSchemaTableColumn::is_is_primary_key_Valid() const{
    return m_is_primary_key_isValid;
}

QString OAISyncFullSchemaTableColumn::getName() const {
    return m_name;
}
void OAISyncFullSchemaTableColumn::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_name_Set() const{
    return m_name_isSet;
}

bool OAISyncFullSchemaTableColumn::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISyncFullSchemaTableColumn::getQuotedName() const {
    return m_quoted_name;
}
void OAISyncFullSchemaTableColumn::setQuotedName(const QString &quoted_name) {
    m_quoted_name = quoted_name;
    m_quoted_name_isSet = true;
}

bool OAISyncFullSchemaTableColumn::is_quoted_name_Set() const{
    return m_quoted_name_isSet;
}

bool OAISyncFullSchemaTableColumn::is_quoted_name_Valid() const{
    return m_quoted_name_isValid;
}

bool OAISyncFullSchemaTableColumn::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_primary_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quoted_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISyncFullSchemaTableColumn::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
