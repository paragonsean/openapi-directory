/**
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStrategyResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStrategyResponse::OAIStrategyResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStrategyResponse::OAIStrategyResponse() {
    this->initializeModel();
}

OAIStrategyResponse::~OAIStrategyResponse() {}

void OAIStrategyResponse::initializeModel() {

    m_crc_isSet = false;
    m_crc_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_running_charts_isSet = false;
    m_running_charts_isValid = false;

    m_strategy_name_isSet = false;
    m_strategy_name_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;
}

void OAIStrategyResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStrategyResponse::fromJsonObject(QJsonObject json) {

    m_crc_isValid = ::OpenAPI::fromJsonValue(m_crc, json[QString("crc")]);
    m_crc_isSet = !json[QString("crc")].isNull() && m_crc_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_running_charts_isValid = ::OpenAPI::fromJsonValue(m_running_charts, json[QString("runningCharts")]);
    m_running_charts_isSet = !json[QString("runningCharts")].isNull() && m_running_charts_isValid;

    m_strategy_name_isValid = ::OpenAPI::fromJsonValue(m_strategy_name, json[QString("strategyName")]);
    m_strategy_name_isSet = !json[QString("strategyName")].isNull() && m_strategy_name_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;
}

QString OAIStrategyResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStrategyResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_crc_isSet) {
        obj.insert(QString("crc"), ::OpenAPI::toJsonValue(m_crc));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_running_charts_isSet) {
        obj.insert(QString("runningCharts"), ::OpenAPI::toJsonValue(m_running_charts));
    }
    if (m_strategy_name_isSet) {
        obj.insert(QString("strategyName"), ::OpenAPI::toJsonValue(m_strategy_name));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    return obj;
}

QString OAIStrategyResponse::getCrc() const {
    return m_crc;
}
void OAIStrategyResponse::setCrc(const QString &crc) {
    m_crc = crc;
    m_crc_isSet = true;
}

bool OAIStrategyResponse::is_crc_Set() const{
    return m_crc_isSet;
}

bool OAIStrategyResponse::is_crc_Valid() const{
    return m_crc_isValid;
}

QString OAIStrategyResponse::getDate() const {
    return m_date;
}
void OAIStrategyResponse::setDate(const QString &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIStrategyResponse::is_date_Set() const{
    return m_date_isSet;
}

bool OAIStrategyResponse::is_date_Valid() const{
    return m_date_isValid;
}

qint32 OAIStrategyResponse::getRunningCharts() const {
    return m_running_charts;
}
void OAIStrategyResponse::setRunningCharts(const qint32 &running_charts) {
    m_running_charts = running_charts;
    m_running_charts_isSet = true;
}

bool OAIStrategyResponse::is_running_charts_Set() const{
    return m_running_charts_isSet;
}

bool OAIStrategyResponse::is_running_charts_Valid() const{
    return m_running_charts_isValid;
}

QString OAIStrategyResponse::getStrategyName() const {
    return m_strategy_name;
}
void OAIStrategyResponse::setStrategyName(const QString &strategy_name) {
    m_strategy_name = strategy_name;
    m_strategy_name_isSet = true;
}

bool OAIStrategyResponse::is_strategy_name_Set() const{
    return m_strategy_name_isSet;
}

bool OAIStrategyResponse::is_strategy_name_Valid() const{
    return m_strategy_name_isValid;
}

QString OAIStrategyResponse::getTime() const {
    return m_time;
}
void OAIStrategyResponse::setTime(const QString &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIStrategyResponse::is_time_Set() const{
    return m_time_isSet;
}

bool OAIStrategyResponse::is_time_Valid() const{
    return m_time_isValid;
}

bool OAIStrategyResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_crc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_running_charts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_strategy_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStrategyResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
