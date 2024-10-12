/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITimeMachine_PointDailyStatsTemperatureData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITimeMachine_PointDailyStatsTemperatureData::OAITimeMachine_PointDailyStatsTemperatureData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITimeMachine_PointDailyStatsTemperatureData::OAITimeMachine_PointDailyStatsTemperatureData() {
    this->initializeModel();
}

OAITimeMachine_PointDailyStatsTemperatureData::~OAITimeMachine_PointDailyStatsTemperatureData() {}

void OAITimeMachine_PointDailyStatsTemperatureData::initializeModel() {

    m_avg_isSet = false;
    m_avg_isValid = false;

    m_avg_max_isSet = false;
    m_avg_max_isValid = false;

    m_avg_min_isSet = false;
    m_avg_min_isValid = false;

    m_record_max_isSet = false;
    m_record_max_isValid = false;

    m_record_min_isSet = false;
    m_record_min_isValid = false;
}

void OAITimeMachine_PointDailyStatsTemperatureData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITimeMachine_PointDailyStatsTemperatureData::fromJsonObject(QJsonObject json) {

    m_avg_isValid = ::OpenAPI::fromJsonValue(m_avg, json[QString("avg")]);
    m_avg_isSet = !json[QString("avg")].isNull() && m_avg_isValid;

    m_avg_max_isValid = ::OpenAPI::fromJsonValue(m_avg_max, json[QString("avg_max")]);
    m_avg_max_isSet = !json[QString("avg_max")].isNull() && m_avg_max_isValid;

    m_avg_min_isValid = ::OpenAPI::fromJsonValue(m_avg_min, json[QString("avg_min")]);
    m_avg_min_isSet = !json[QString("avg_min")].isNull() && m_avg_min_isValid;

    m_record_max_isValid = ::OpenAPI::fromJsonValue(m_record_max, json[QString("record_max")]);
    m_record_max_isSet = !json[QString("record_max")].isNull() && m_record_max_isValid;

    m_record_min_isValid = ::OpenAPI::fromJsonValue(m_record_min, json[QString("record_min")]);
    m_record_min_isSet = !json[QString("record_min")].isNull() && m_record_min_isValid;
}

QString OAITimeMachine_PointDailyStatsTemperatureData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITimeMachine_PointDailyStatsTemperatureData::asJsonObject() const {
    QJsonObject obj;
    if (m_avg_isSet) {
        obj.insert(QString("avg"), ::OpenAPI::toJsonValue(m_avg));
    }
    if (m_avg_max_isSet) {
        obj.insert(QString("avg_max"), ::OpenAPI::toJsonValue(m_avg_max));
    }
    if (m_avg_min_isSet) {
        obj.insert(QString("avg_min"), ::OpenAPI::toJsonValue(m_avg_min));
    }
    if (m_record_max_isSet) {
        obj.insert(QString("record_max"), ::OpenAPI::toJsonValue(m_record_max));
    }
    if (m_record_min_isSet) {
        obj.insert(QString("record_min"), ::OpenAPI::toJsonValue(m_record_min));
    }
    return obj;
}

double OAITimeMachine_PointDailyStatsTemperatureData::getAvg() const {
    return m_avg;
}
void OAITimeMachine_PointDailyStatsTemperatureData::setAvg(const double &avg) {
    m_avg = avg;
    m_avg_isSet = true;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_avg_Set() const{
    return m_avg_isSet;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_avg_Valid() const{
    return m_avg_isValid;
}

double OAITimeMachine_PointDailyStatsTemperatureData::getAvgMax() const {
    return m_avg_max;
}
void OAITimeMachine_PointDailyStatsTemperatureData::setAvgMax(const double &avg_max) {
    m_avg_max = avg_max;
    m_avg_max_isSet = true;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_avg_max_Set() const{
    return m_avg_max_isSet;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_avg_max_Valid() const{
    return m_avg_max_isValid;
}

double OAITimeMachine_PointDailyStatsTemperatureData::getAvgMin() const {
    return m_avg_min;
}
void OAITimeMachine_PointDailyStatsTemperatureData::setAvgMin(const double &avg_min) {
    m_avg_min = avg_min;
    m_avg_min_isSet = true;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_avg_min_Set() const{
    return m_avg_min_isSet;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_avg_min_Valid() const{
    return m_avg_min_isValid;
}

double OAITimeMachine_PointDailyStatsTemperatureData::getRecordMax() const {
    return m_record_max;
}
void OAITimeMachine_PointDailyStatsTemperatureData::setRecordMax(const double &record_max) {
    m_record_max = record_max;
    m_record_max_isSet = true;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_record_max_Set() const{
    return m_record_max_isSet;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_record_max_Valid() const{
    return m_record_max_isValid;
}

double OAITimeMachine_PointDailyStatsTemperatureData::getRecordMin() const {
    return m_record_min;
}
void OAITimeMachine_PointDailyStatsTemperatureData::setRecordMin(const double &record_min) {
    m_record_min = record_min;
    m_record_min_isSet = true;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_record_min_Set() const{
    return m_record_min_isSet;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::is_record_min_Valid() const{
    return m_record_min_isValid;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_avg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_avg_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_avg_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_min_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITimeMachine_PointDailyStatsTemperatureData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
