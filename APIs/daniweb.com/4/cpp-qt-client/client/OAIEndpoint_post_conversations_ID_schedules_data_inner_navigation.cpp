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

#include "OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation() {
    this->initializeModel();
}

OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::~OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation() {}

void OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::initializeModel() {

    m_earliest_date_isSet = false;
    m_earliest_date_isValid = false;

    m_next_date_isSet = false;
    m_next_date_isValid = false;

    m_previous_date_isSet = false;
    m_previous_date_isValid = false;
}

void OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::fromJsonObject(QJsonObject json) {

    m_earliest_date_isValid = ::OpenAPI::fromJsonValue(m_earliest_date, json[QString("earliest_date")]);
    m_earliest_date_isSet = !json[QString("earliest_date")].isNull() && m_earliest_date_isValid;

    m_next_date_isValid = ::OpenAPI::fromJsonValue(m_next_date, json[QString("next_date")]);
    m_next_date_isSet = !json[QString("next_date")].isNull() && m_next_date_isValid;

    m_previous_date_isValid = ::OpenAPI::fromJsonValue(m_previous_date, json[QString("previous_date")]);
    m_previous_date_isSet = !json[QString("previous_date")].isNull() && m_previous_date_isValid;
}

QString OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::asJsonObject() const {
    QJsonObject obj;
    if (m_earliest_date_isSet) {
        obj.insert(QString("earliest_date"), ::OpenAPI::toJsonValue(m_earliest_date));
    }
    if (m_next_date_isSet) {
        obj.insert(QString("next_date"), ::OpenAPI::toJsonValue(m_next_date));
    }
    if (m_previous_date_isSet) {
        obj.insert(QString("previous_date"), ::OpenAPI::toJsonValue(m_previous_date));
    }
    return obj;
}

QDate OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::getEarliestDate() const {
    return m_earliest_date;
}
void OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::setEarliestDate(const QDate &earliest_date) {
    m_earliest_date = earliest_date;
    m_earliest_date_isSet = true;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::is_earliest_date_Set() const{
    return m_earliest_date_isSet;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::is_earliest_date_Valid() const{
    return m_earliest_date_isValid;
}

QDate OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::getNextDate() const {
    return m_next_date;
}
void OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::setNextDate(const QDate &next_date) {
    m_next_date = next_date;
    m_next_date_isSet = true;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::is_next_date_Set() const{
    return m_next_date_isSet;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::is_next_date_Valid() const{
    return m_next_date_isValid;
}

QDate OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::getPreviousDate() const {
    return m_previous_date;
}
void OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::setPreviousDate(const QDate &previous_date) {
    m_previous_date = previous_date;
    m_previous_date_isSet = true;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::is_previous_date_Set() const{
    return m_previous_date_isSet;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::is_previous_date_Valid() const{
    return m_previous_date_isValid;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_earliest_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_previous_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_post_conversations_ID_schedules_data_inner_navigation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
