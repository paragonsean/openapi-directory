/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAsynchronous_operations_data_detailed_operation_status_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAsynchronous_operations_data_detailed_operation_status_interface::OAIAsynchronous_operations_data_detailed_operation_status_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAsynchronous_operations_data_detailed_operation_status_interface::OAIAsynchronous_operations_data_detailed_operation_status_interface() {
    this->initializeModel();
}

OAIAsynchronous_operations_data_detailed_operation_status_interface::~OAIAsynchronous_operations_data_detailed_operation_status_interface() {}

void OAIAsynchronous_operations_data_detailed_operation_status_interface::initializeModel() {

    m_bulk_uuid_isSet = false;
    m_bulk_uuid_isValid = false;

    m_error_code_isSet = false;
    m_error_code_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_result_message_isSet = false;
    m_result_message_isValid = false;

    m_result_serialized_data_isSet = false;
    m_result_serialized_data_isValid = false;

    m_serialized_data_isSet = false;
    m_serialized_data_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_topic_name_isSet = false;
    m_topic_name_isValid = false;
}

void OAIAsynchronous_operations_data_detailed_operation_status_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAsynchronous_operations_data_detailed_operation_status_interface::fromJsonObject(QJsonObject json) {

    m_bulk_uuid_isValid = ::OpenAPI::fromJsonValue(m_bulk_uuid, json[QString("bulk_uuid")]);
    m_bulk_uuid_isSet = !json[QString("bulk_uuid")].isNull() && m_bulk_uuid_isValid;

    m_error_code_isValid = ::OpenAPI::fromJsonValue(m_error_code, json[QString("error_code")]);
    m_error_code_isSet = !json[QString("error_code")].isNull() && m_error_code_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_result_message_isValid = ::OpenAPI::fromJsonValue(m_result_message, json[QString("result_message")]);
    m_result_message_isSet = !json[QString("result_message")].isNull() && m_result_message_isValid;

    m_result_serialized_data_isValid = ::OpenAPI::fromJsonValue(m_result_serialized_data, json[QString("result_serialized_data")]);
    m_result_serialized_data_isSet = !json[QString("result_serialized_data")].isNull() && m_result_serialized_data_isValid;

    m_serialized_data_isValid = ::OpenAPI::fromJsonValue(m_serialized_data, json[QString("serialized_data")]);
    m_serialized_data_isSet = !json[QString("serialized_data")].isNull() && m_serialized_data_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_topic_name_isValid = ::OpenAPI::fromJsonValue(m_topic_name, json[QString("topic_name")]);
    m_topic_name_isSet = !json[QString("topic_name")].isNull() && m_topic_name_isValid;
}

QString OAIAsynchronous_operations_data_detailed_operation_status_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAsynchronous_operations_data_detailed_operation_status_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_bulk_uuid_isSet) {
        obj.insert(QString("bulk_uuid"), ::OpenAPI::toJsonValue(m_bulk_uuid));
    }
    if (m_error_code_isSet) {
        obj.insert(QString("error_code"), ::OpenAPI::toJsonValue(m_error_code));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_result_message_isSet) {
        obj.insert(QString("result_message"), ::OpenAPI::toJsonValue(m_result_message));
    }
    if (m_result_serialized_data_isSet) {
        obj.insert(QString("result_serialized_data"), ::OpenAPI::toJsonValue(m_result_serialized_data));
    }
    if (m_serialized_data_isSet) {
        obj.insert(QString("serialized_data"), ::OpenAPI::toJsonValue(m_serialized_data));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_topic_name_isSet) {
        obj.insert(QString("topic_name"), ::OpenAPI::toJsonValue(m_topic_name));
    }
    return obj;
}

QString OAIAsynchronous_operations_data_detailed_operation_status_interface::getBulkUuid() const {
    return m_bulk_uuid;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setBulkUuid(const QString &bulk_uuid) {
    m_bulk_uuid = bulk_uuid;
    m_bulk_uuid_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_bulk_uuid_Set() const{
    return m_bulk_uuid_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_bulk_uuid_Valid() const{
    return m_bulk_uuid_isValid;
}

qint32 OAIAsynchronous_operations_data_detailed_operation_status_interface::getErrorCode() const {
    return m_error_code;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setErrorCode(const qint32 &error_code) {
    m_error_code = error_code;
    m_error_code_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_error_code_Set() const{
    return m_error_code_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_error_code_Valid() const{
    return m_error_code_isValid;
}

OAIObject OAIAsynchronous_operations_data_detailed_operation_status_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

qint32 OAIAsynchronous_operations_data_detailed_operation_status_interface::getId() const {
    return m_id;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAsynchronous_operations_data_detailed_operation_status_interface::getResultMessage() const {
    return m_result_message;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setResultMessage(const QString &result_message) {
    m_result_message = result_message;
    m_result_message_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_result_message_Set() const{
    return m_result_message_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_result_message_Valid() const{
    return m_result_message_isValid;
}

QString OAIAsynchronous_operations_data_detailed_operation_status_interface::getResultSerializedData() const {
    return m_result_serialized_data;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setResultSerializedData(const QString &result_serialized_data) {
    m_result_serialized_data = result_serialized_data;
    m_result_serialized_data_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_result_serialized_data_Set() const{
    return m_result_serialized_data_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_result_serialized_data_Valid() const{
    return m_result_serialized_data_isValid;
}

QString OAIAsynchronous_operations_data_detailed_operation_status_interface::getSerializedData() const {
    return m_serialized_data;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setSerializedData(const QString &serialized_data) {
    m_serialized_data = serialized_data;
    m_serialized_data_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_serialized_data_Set() const{
    return m_serialized_data_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_serialized_data_Valid() const{
    return m_serialized_data_isValid;
}

qint32 OAIAsynchronous_operations_data_detailed_operation_status_interface::getStatus() const {
    return m_status;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIAsynchronous_operations_data_detailed_operation_status_interface::getTopicName() const {
    return m_topic_name;
}
void OAIAsynchronous_operations_data_detailed_operation_status_interface::setTopicName(const QString &topic_name) {
    m_topic_name = topic_name;
    m_topic_name_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_topic_name_Set() const{
    return m_topic_name_isSet;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::is_topic_name_Valid() const{
    return m_topic_name_isValid;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bulk_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_serialized_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serialized_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_topic_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAsynchronous_operations_data_detailed_operation_status_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_bulk_uuid_isValid && m_error_code_isValid && m_id_isValid && m_result_message_isValid && m_result_serialized_data_isValid && m_serialized_data_isValid && m_status_isValid && m_topic_name_isValid && true;
}

} // namespace OpenAPI
