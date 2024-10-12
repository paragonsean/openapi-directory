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

#include "OAIEndpoint_get_groups_messages_ID.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_get_groups_messages_ID::OAIEndpoint_get_groups_messages_ID(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_get_groups_messages_ID::OAIEndpoint_get_groups_messages_ID() {
    this->initializeModel();
}

OAIEndpoint_get_groups_messages_ID::~OAIEndpoint_get_groups_messages_ID() {}

void OAIEndpoint_get_groups_messages_ID::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;
}

void OAIEndpoint_get_groups_messages_ID::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_get_groups_messages_ID::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;
}

QString OAIEndpoint_get_groups_messages_ID::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_get_groups_messages_ID::asJsonObject() const {
    QJsonObject obj;
    if (m_data.size() > 0) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    return obj;
}

QList<OAIGroup_message> OAIEndpoint_get_groups_messages_ID::getData() const {
    return m_data;
}
void OAIEndpoint_get_groups_messages_ID::setData(const QList<OAIGroup_message> &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIEndpoint_get_groups_messages_ID::is_data_Set() const{
    return m_data_isSet;
}

bool OAIEndpoint_get_groups_messages_ID::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIEndpoint_get_groups_messages_ID::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_get_groups_messages_ID::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
