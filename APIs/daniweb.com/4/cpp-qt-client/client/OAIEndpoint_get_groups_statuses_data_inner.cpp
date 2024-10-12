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

#include "OAIEndpoint_get_groups_statuses_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_get_groups_statuses_data_inner::OAIEndpoint_get_groups_statuses_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_get_groups_statuses_data_inner::OAIEndpoint_get_groups_statuses_data_inner() {
    this->initializeModel();
}

OAIEndpoint_get_groups_statuses_data_inner::~OAIEndpoint_get_groups_statuses_data_inner() {}

void OAIEndpoint_get_groups_statuses_data_inner::initializeModel() {

    m_earliest_unseen_message_isSet = false;
    m_earliest_unseen_message_isValid = false;

    m_group_isSet = false;
    m_group_isValid = false;

    m_new_message_count_isSet = false;
    m_new_message_count_isValid = false;
}

void OAIEndpoint_get_groups_statuses_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_get_groups_statuses_data_inner::fromJsonObject(QJsonObject json) {

    m_earliest_unseen_message_isValid = ::OpenAPI::fromJsonValue(m_earliest_unseen_message, json[QString("earliest_unseen_message")]);
    m_earliest_unseen_message_isSet = !json[QString("earliest_unseen_message")].isNull() && m_earliest_unseen_message_isValid;

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_new_message_count_isValid = ::OpenAPI::fromJsonValue(m_new_message_count, json[QString("new_message_count")]);
    m_new_message_count_isSet = !json[QString("new_message_count")].isNull() && m_new_message_count_isValid;
}

QString OAIEndpoint_get_groups_statuses_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_get_groups_statuses_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_earliest_unseen_message.isSet()) {
        obj.insert(QString("earliest_unseen_message"), ::OpenAPI::toJsonValue(m_earliest_unseen_message));
    }
    if (m_group.isSet()) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_new_message_count_isSet) {
        obj.insert(QString("new_message_count"), ::OpenAPI::toJsonValue(m_new_message_count));
    }
    return obj;
}

OAIGroup_message OAIEndpoint_get_groups_statuses_data_inner::getEarliestUnseenMessage() const {
    return m_earliest_unseen_message;
}
void OAIEndpoint_get_groups_statuses_data_inner::setEarliestUnseenMessage(const OAIGroup_message &earliest_unseen_message) {
    m_earliest_unseen_message = earliest_unseen_message;
    m_earliest_unseen_message_isSet = true;
}

bool OAIEndpoint_get_groups_statuses_data_inner::is_earliest_unseen_message_Set() const{
    return m_earliest_unseen_message_isSet;
}

bool OAIEndpoint_get_groups_statuses_data_inner::is_earliest_unseen_message_Valid() const{
    return m_earliest_unseen_message_isValid;
}

OAIGroup OAIEndpoint_get_groups_statuses_data_inner::getGroup() const {
    return m_group;
}
void OAIEndpoint_get_groups_statuses_data_inner::setGroup(const OAIGroup &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAIEndpoint_get_groups_statuses_data_inner::is_group_Set() const{
    return m_group_isSet;
}

bool OAIEndpoint_get_groups_statuses_data_inner::is_group_Valid() const{
    return m_group_isValid;
}

double OAIEndpoint_get_groups_statuses_data_inner::getNewMessageCount() const {
    return m_new_message_count;
}
void OAIEndpoint_get_groups_statuses_data_inner::setNewMessageCount(const double &new_message_count) {
    m_new_message_count = new_message_count;
    m_new_message_count_isSet = true;
}

bool OAIEndpoint_get_groups_statuses_data_inner::is_new_message_count_Set() const{
    return m_new_message_count_isSet;
}

bool OAIEndpoint_get_groups_statuses_data_inner::is_new_message_count_Valid() const{
    return m_new_message_count_isValid;
}

bool OAIEndpoint_get_groups_statuses_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_earliest_unseen_message.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_group.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_message_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_get_groups_statuses_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
