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

#include "OAIPoint_PointDailyAfternoonProbData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPoint_PointDailyAfternoonProbData::OAIPoint_PointDailyAfternoonProbData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPoint_PointDailyAfternoonProbData::OAIPoint_PointDailyAfternoonProbData() {
    this->initializeModel();
}

OAIPoint_PointDailyAfternoonProbData::~OAIPoint_PointDailyAfternoonProbData() {}

void OAIPoint_PointDailyAfternoonProbData::initializeModel() {

    m_freeze_isSet = false;
    m_freeze_isValid = false;

    m_precipitation_isSet = false;
    m_precipitation_isValid = false;

    m_storm_isSet = false;
    m_storm_isValid = false;
}

void OAIPoint_PointDailyAfternoonProbData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPoint_PointDailyAfternoonProbData::fromJsonObject(QJsonObject json) {

    m_freeze_isValid = ::OpenAPI::fromJsonValue(m_freeze, json[QString("freeze")]);
    m_freeze_isSet = !json[QString("freeze")].isNull() && m_freeze_isValid;

    m_precipitation_isValid = ::OpenAPI::fromJsonValue(m_precipitation, json[QString("precipitation")]);
    m_precipitation_isSet = !json[QString("precipitation")].isNull() && m_precipitation_isValid;

    m_storm_isValid = ::OpenAPI::fromJsonValue(m_storm, json[QString("storm")]);
    m_storm_isSet = !json[QString("storm")].isNull() && m_storm_isValid;
}

QString OAIPoint_PointDailyAfternoonProbData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPoint_PointDailyAfternoonProbData::asJsonObject() const {
    QJsonObject obj;
    if (m_freeze_isSet) {
        obj.insert(QString("freeze"), ::OpenAPI::toJsonValue(m_freeze));
    }
    if (m_precipitation_isSet) {
        obj.insert(QString("precipitation"), ::OpenAPI::toJsonValue(m_precipitation));
    }
    if (m_storm_isSet) {
        obj.insert(QString("storm"), ::OpenAPI::toJsonValue(m_storm));
    }
    return obj;
}

double OAIPoint_PointDailyAfternoonProbData::getFreeze() const {
    return m_freeze;
}
void OAIPoint_PointDailyAfternoonProbData::setFreeze(const double &freeze) {
    m_freeze = freeze;
    m_freeze_isSet = true;
}

bool OAIPoint_PointDailyAfternoonProbData::is_freeze_Set() const{
    return m_freeze_isSet;
}

bool OAIPoint_PointDailyAfternoonProbData::is_freeze_Valid() const{
    return m_freeze_isValid;
}

qint32 OAIPoint_PointDailyAfternoonProbData::getPrecipitation() const {
    return m_precipitation;
}
void OAIPoint_PointDailyAfternoonProbData::setPrecipitation(const qint32 &precipitation) {
    m_precipitation = precipitation;
    m_precipitation_isSet = true;
}

bool OAIPoint_PointDailyAfternoonProbData::is_precipitation_Set() const{
    return m_precipitation_isSet;
}

bool OAIPoint_PointDailyAfternoonProbData::is_precipitation_Valid() const{
    return m_precipitation_isValid;
}

double OAIPoint_PointDailyAfternoonProbData::getStorm() const {
    return m_storm;
}
void OAIPoint_PointDailyAfternoonProbData::setStorm(const double &storm) {
    m_storm = storm;
    m_storm_isSet = true;
}

bool OAIPoint_PointDailyAfternoonProbData::is_storm_Set() const{
    return m_storm_isSet;
}

bool OAIPoint_PointDailyAfternoonProbData::is_storm_Valid() const{
    return m_storm_isValid;
}

bool OAIPoint_PointDailyAfternoonProbData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_freeze_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_precipitation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storm_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPoint_PointDailyAfternoonProbData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
