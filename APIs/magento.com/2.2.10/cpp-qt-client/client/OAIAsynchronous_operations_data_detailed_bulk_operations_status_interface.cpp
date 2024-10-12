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

#include "OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface() {
    this->initializeModel();
}

OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::~OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface() {}

void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::initializeModel() {

    m_bulk_id_isSet = false;
    m_bulk_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_operation_count_isSet = false;
    m_operation_count_isValid = false;

    m_operations_list_isSet = false;
    m_operations_list_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::fromJsonObject(QJsonObject json) {

    m_bulk_id_isValid = ::OpenAPI::fromJsonValue(m_bulk_id, json[QString("bulk_id")]);
    m_bulk_id_isSet = !json[QString("bulk_id")].isNull() && m_bulk_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_operation_count_isValid = ::OpenAPI::fromJsonValue(m_operation_count, json[QString("operation_count")]);
    m_operation_count_isSet = !json[QString("operation_count")].isNull() && m_operation_count_isValid;

    m_operations_list_isValid = ::OpenAPI::fromJsonValue(m_operations_list, json[QString("operations_list")]);
    m_operations_list_isSet = !json[QString("operations_list")].isNull() && m_operations_list_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("start_time")]);
    m_start_time_isSet = !json[QString("start_time")].isNull() && m_start_time_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_bulk_id_isSet) {
        obj.insert(QString("bulk_id"), ::OpenAPI::toJsonValue(m_bulk_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_operation_count_isSet) {
        obj.insert(QString("operation_count"), ::OpenAPI::toJsonValue(m_operation_count));
    }
    if (m_operations_list.size() > 0) {
        obj.insert(QString("operations_list"), ::OpenAPI::toJsonValue(m_operations_list));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("start_time"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getBulkId() const {
    return m_bulk_id;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setBulkId(const QString &bulk_id) {
    m_bulk_id = bulk_id;
    m_bulk_id_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_bulk_id_Set() const{
    return m_bulk_id_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_bulk_id_Valid() const{
    return m_bulk_id_isValid;
}

QString OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getDescription() const {
    return m_description;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_description_Valid() const{
    return m_description_isValid;
}

OAIObject OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

qint32 OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getOperationCount() const {
    return m_operation_count;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setOperationCount(const qint32 &operation_count) {
    m_operation_count = operation_count;
    m_operation_count_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_operation_count_Set() const{
    return m_operation_count_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_operation_count_Valid() const{
    return m_operation_count_isValid;
}

QList<OAIAsynchronous_operations_data_detailed_operation_status_interface> OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getOperationsList() const {
    return m_operations_list;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setOperationsList(const QList<OAIAsynchronous_operations_data_detailed_operation_status_interface> &operations_list) {
    m_operations_list = operations_list;
    m_operations_list_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_operations_list_Set() const{
    return m_operations_list_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_operations_list_Valid() const{
    return m_operations_list_isValid;
}

QString OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getStartTime() const {
    return m_start_time;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setStartTime(const QString &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_start_time_Valid() const{
    return m_start_time_isValid;
}

qint32 OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::getUserId() const {
    return m_user_id;
}
void OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::setUserId(const qint32 &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bulk_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operations_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_bulk_id_isValid && m_description_isValid && m_operation_count_isValid && m_operations_list_isValid && m_start_time_isValid && m_user_id_isValid && true;
}

} // namespace OpenAPI
