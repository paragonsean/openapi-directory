/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPeriodicTimerSourceInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPeriodicTimerSourceInfo::OAIPeriodicTimerSourceInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPeriodicTimerSourceInfo::OAIPeriodicTimerSourceInfo() {
    this->initializeModel();
}

OAIPeriodicTimerSourceInfo::~OAIPeriodicTimerSourceInfo() {}

void OAIPeriodicTimerSourceInfo::initializeModel() {

    m_schedule_isSet = false;
    m_schedule_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_topic_isSet = false;
    m_topic_isValid = false;
}

void OAIPeriodicTimerSourceInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPeriodicTimerSourceInfo::fromJsonObject(QJsonObject json) {

    m_schedule_isValid = ::OpenAPI::fromJsonValue(m_schedule, json[QString("schedule")]);
    m_schedule_isSet = !json[QString("schedule")].isNull() && m_schedule_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_topic_isValid = ::OpenAPI::fromJsonValue(m_topic, json[QString("topic")]);
    m_topic_isSet = !json[QString("topic")].isNull() && m_topic_isValid;
}

QString OAIPeriodicTimerSourceInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPeriodicTimerSourceInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_schedule_isSet) {
        obj.insert(QString("schedule"), ::OpenAPI::toJsonValue(m_schedule));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_topic_isSet) {
        obj.insert(QString("topic"), ::OpenAPI::toJsonValue(m_topic));
    }
    return obj;
}

QString OAIPeriodicTimerSourceInfo::getSchedule() const {
    return m_schedule;
}
void OAIPeriodicTimerSourceInfo::setSchedule(const QString &schedule) {
    m_schedule = schedule;
    m_schedule_isSet = true;
}

bool OAIPeriodicTimerSourceInfo::is_schedule_Set() const{
    return m_schedule_isSet;
}

bool OAIPeriodicTimerSourceInfo::is_schedule_Valid() const{
    return m_schedule_isValid;
}

QDateTime OAIPeriodicTimerSourceInfo::getStartTime() const {
    return m_start_time;
}
void OAIPeriodicTimerSourceInfo::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIPeriodicTimerSourceInfo::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIPeriodicTimerSourceInfo::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAIPeriodicTimerSourceInfo::getTopic() const {
    return m_topic;
}
void OAIPeriodicTimerSourceInfo::setTopic(const QString &topic) {
    m_topic = topic;
    m_topic_isSet = true;
}

bool OAIPeriodicTimerSourceInfo::is_topic_Set() const{
    return m_topic_isSet;
}

bool OAIPeriodicTimerSourceInfo::is_topic_Valid() const{
    return m_topic_isValid;
}

bool OAIPeriodicTimerSourceInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_schedule_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_topic_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPeriodicTimerSourceInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_schedule_isValid && m_start_time_isValid && true;
}

} // namespace OpenAPI
