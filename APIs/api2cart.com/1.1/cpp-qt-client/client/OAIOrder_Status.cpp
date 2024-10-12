/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOrder_Status.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrder_Status::OAIOrder_Status(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrder_Status::OAIOrder_Status() {
    this->initializeModel();
}

OAIOrder_Status::~OAIOrder_Status() {}

void OAIOrder_Status::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_history_isSet = false;
    m_history_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_refund_info_isSet = false;
    m_refund_info_isValid = false;
}

void OAIOrder_Status::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrder_Status::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_history_isValid = ::OpenAPI::fromJsonValue(m_history, json[QString("history")]);
    m_history_isSet = !json[QString("history")].isNull() && m_history_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_refund_info_isValid = ::OpenAPI::fromJsonValue(m_refund_info, json[QString("refund_info")]);
    m_refund_info_isSet = !json[QString("refund_info")].isNull() && m_refund_info_isValid;
}

QString OAIOrder_Status::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrder_Status::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_history.size() > 0) {
        obj.insert(QString("history"), ::OpenAPI::toJsonValue(m_history));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_refund_info.isSet()) {
        obj.insert(QString("refund_info"), ::OpenAPI::toJsonValue(m_refund_info));
    }
    return obj;
}

OAIObject OAIOrder_Status::getAdditionalFields() const {
    return m_additional_fields;
}
void OAIOrder_Status::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAIOrder_Status::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAIOrder_Status::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

OAIObject OAIOrder_Status::getCustomFields() const {
    return m_custom_fields;
}
void OAIOrder_Status::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIOrder_Status::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIOrder_Status::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QList<OAIOrder_Status_HistoryItem> OAIOrder_Status::getHistory() const {
    return m_history;
}
void OAIOrder_Status::setHistory(const QList<OAIOrder_Status_HistoryItem> &history) {
    m_history = history;
    m_history_isSet = true;
}

bool OAIOrder_Status::is_history_Set() const{
    return m_history_isSet;
}

bool OAIOrder_Status::is_history_Valid() const{
    return m_history_isValid;
}

QString OAIOrder_Status::getId() const {
    return m_id;
}
void OAIOrder_Status::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrder_Status::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrder_Status::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrder_Status::getName() const {
    return m_name;
}
void OAIOrder_Status::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrder_Status::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrder_Status::is_name_Valid() const{
    return m_name_isValid;
}

OAIOrder_Status_Refund OAIOrder_Status::getRefundInfo() const {
    return m_refund_info;
}
void OAIOrder_Status::setRefundInfo(const OAIOrder_Status_Refund &refund_info) {
    m_refund_info = refund_info;
    m_refund_info_isSet = true;
}

bool OAIOrder_Status::is_refund_info_Set() const{
    return m_refund_info_isSet;
}

bool OAIOrder_Status::is_refund_info_Valid() const{
    return m_refund_info_isValid;
}

bool OAIOrder_Status::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_history.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refund_info.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrder_Status::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
