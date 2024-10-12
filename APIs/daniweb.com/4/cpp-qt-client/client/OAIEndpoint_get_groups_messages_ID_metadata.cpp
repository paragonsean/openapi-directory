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

#include "OAIEndpoint_get_groups_messages_ID_metadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_get_groups_messages_ID_metadata::OAIEndpoint_get_groups_messages_ID_metadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_get_groups_messages_ID_metadata::OAIEndpoint_get_groups_messages_ID_metadata() {
    this->initializeModel();
}

OAIEndpoint_get_groups_messages_ID_metadata::~OAIEndpoint_get_groups_messages_ID_metadata() {}

void OAIEndpoint_get_groups_messages_ID_metadata::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_pagination_isSet = false;
    m_pagination_isValid = false;
}

void OAIEndpoint_get_groups_messages_ID_metadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_get_groups_messages_ID_metadata::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_pagination_isValid = ::OpenAPI::fromJsonValue(m_pagination, json[QString("pagination")]);
    m_pagination_isSet = !json[QString("pagination")].isNull() && m_pagination_isValid;
}

QString OAIEndpoint_get_groups_messages_ID_metadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_get_groups_messages_ID_metadata::asJsonObject() const {
    QJsonObject obj;
    if (m_data.size() > 0) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_pagination.isSet()) {
        obj.insert(QString("pagination"), ::OpenAPI::toJsonValue(m_pagination));
    }
    return obj;
}

QList<OAIGroup_message_data> OAIEndpoint_get_groups_messages_ID_metadata::getData() const {
    return m_data;
}
void OAIEndpoint_get_groups_messages_ID_metadata::setData(const QList<OAIGroup_message_data> &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIEndpoint_get_groups_messages_ID_metadata::is_data_Set() const{
    return m_data_isSet;
}

bool OAIEndpoint_get_groups_messages_ID_metadata::is_data_Valid() const{
    return m_data_isValid;
}

OAIApi_pagination OAIEndpoint_get_groups_messages_ID_metadata::getPagination() const {
    return m_pagination;
}
void OAIEndpoint_get_groups_messages_ID_metadata::setPagination(const OAIApi_pagination &pagination) {
    m_pagination = pagination;
    m_pagination_isSet = true;
}

bool OAIEndpoint_get_groups_messages_ID_metadata::is_pagination_Set() const{
    return m_pagination_isSet;
}

bool OAIEndpoint_get_groups_messages_ID_metadata::is_pagination_Valid() const{
    return m_pagination_isValid;
}

bool OAIEndpoint_get_groups_messages_ID_metadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_pagination.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_get_groups_messages_ID_metadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
