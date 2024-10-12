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

#include "OAIPoint_PointDailyAfternoonWindData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPoint_PointDailyAfternoonWindData::OAIPoint_PointDailyAfternoonWindData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPoint_PointDailyAfternoonWindData::OAIPoint_PointDailyAfternoonWindData() {
    this->initializeModel();
}

OAIPoint_PointDailyAfternoonWindData::~OAIPoint_PointDailyAfternoonWindData() {}

void OAIPoint_PointDailyAfternoonWindData::initializeModel() {

    m_angle_isSet = false;
    m_angle_isValid = false;

    m_dir_isSet = false;
    m_dir_isValid = false;

    m_gusts_isSet = false;
    m_gusts_isValid = false;

    m_speed_isSet = false;
    m_speed_isValid = false;
}

void OAIPoint_PointDailyAfternoonWindData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPoint_PointDailyAfternoonWindData::fromJsonObject(QJsonObject json) {

    m_angle_isValid = ::OpenAPI::fromJsonValue(m_angle, json[QString("angle")]);
    m_angle_isSet = !json[QString("angle")].isNull() && m_angle_isValid;

    m_dir_isValid = ::OpenAPI::fromJsonValue(m_dir, json[QString("dir")]);
    m_dir_isSet = !json[QString("dir")].isNull() && m_dir_isValid;

    m_gusts_isValid = ::OpenAPI::fromJsonValue(m_gusts, json[QString("gusts")]);
    m_gusts_isSet = !json[QString("gusts")].isNull() && m_gusts_isValid;

    m_speed_isValid = ::OpenAPI::fromJsonValue(m_speed, json[QString("speed")]);
    m_speed_isSet = !json[QString("speed")].isNull() && m_speed_isValid;
}

QString OAIPoint_PointDailyAfternoonWindData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPoint_PointDailyAfternoonWindData::asJsonObject() const {
    QJsonObject obj;
    if (m_angle_isSet) {
        obj.insert(QString("angle"), ::OpenAPI::toJsonValue(m_angle));
    }
    if (m_dir.isSet()) {
        obj.insert(QString("dir"), ::OpenAPI::toJsonValue(m_dir));
    }
    if (m_gusts_isSet) {
        obj.insert(QString("gusts"), ::OpenAPI::toJsonValue(m_gusts));
    }
    if (m_speed_isSet) {
        obj.insert(QString("speed"), ::OpenAPI::toJsonValue(m_speed));
    }
    return obj;
}

double OAIPoint_PointDailyAfternoonWindData::getAngle() const {
    return m_angle;
}
void OAIPoint_PointDailyAfternoonWindData::setAngle(const double &angle) {
    m_angle = angle;
    m_angle_isSet = true;
}

bool OAIPoint_PointDailyAfternoonWindData::is_angle_Set() const{
    return m_angle_isSet;
}

bool OAIPoint_PointDailyAfternoonWindData::is_angle_Valid() const{
    return m_angle_isValid;
}

OAIHttpFileElement OAIPoint_PointDailyAfternoonWindData::getDir() const {
    return m_dir;
}
void OAIPoint_PointDailyAfternoonWindData::setDir(const OAIHttpFileElement &dir) {
    m_dir = dir;
    m_dir_isSet = true;
}

bool OAIPoint_PointDailyAfternoonWindData::is_dir_Set() const{
    return m_dir_isSet;
}

bool OAIPoint_PointDailyAfternoonWindData::is_dir_Valid() const{
    return m_dir_isValid;
}

double OAIPoint_PointDailyAfternoonWindData::getGusts() const {
    return m_gusts;
}
void OAIPoint_PointDailyAfternoonWindData::setGusts(const double &gusts) {
    m_gusts = gusts;
    m_gusts_isSet = true;
}

bool OAIPoint_PointDailyAfternoonWindData::is_gusts_Set() const{
    return m_gusts_isSet;
}

bool OAIPoint_PointDailyAfternoonWindData::is_gusts_Valid() const{
    return m_gusts_isValid;
}

double OAIPoint_PointDailyAfternoonWindData::getSpeed() const {
    return m_speed;
}
void OAIPoint_PointDailyAfternoonWindData::setSpeed(const double &speed) {
    m_speed = speed;
    m_speed_isSet = true;
}

bool OAIPoint_PointDailyAfternoonWindData::is_speed_Set() const{
    return m_speed_isSet;
}

bool OAIPoint_PointDailyAfternoonWindData::is_speed_Valid() const{
    return m_speed_isValid;
}

bool OAIPoint_PointDailyAfternoonWindData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_angle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dir.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_gusts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_speed_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPoint_PointDailyAfternoonWindData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
