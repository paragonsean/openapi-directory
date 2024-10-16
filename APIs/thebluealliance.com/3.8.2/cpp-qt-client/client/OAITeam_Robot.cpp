/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITeam_Robot.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITeam_Robot::OAITeam_Robot(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITeam_Robot::OAITeam_Robot() {
    this->initializeModel();
}

OAITeam_Robot::~OAITeam_Robot() {}

void OAITeam_Robot::initializeModel() {

    m_key_isSet = false;
    m_key_isValid = false;

    m_robot_name_isSet = false;
    m_robot_name_isValid = false;

    m_team_key_isSet = false;
    m_team_key_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAITeam_Robot::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITeam_Robot::fromJsonObject(QJsonObject json) {

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_robot_name_isValid = ::OpenAPI::fromJsonValue(m_robot_name, json[QString("robot_name")]);
    m_robot_name_isSet = !json[QString("robot_name")].isNull() && m_robot_name_isValid;

    m_team_key_isValid = ::OpenAPI::fromJsonValue(m_team_key, json[QString("team_key")]);
    m_team_key_isSet = !json[QString("team_key")].isNull() && m_team_key_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAITeam_Robot::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITeam_Robot::asJsonObject() const {
    QJsonObject obj;
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_robot_name_isSet) {
        obj.insert(QString("robot_name"), ::OpenAPI::toJsonValue(m_robot_name));
    }
    if (m_team_key_isSet) {
        obj.insert(QString("team_key"), ::OpenAPI::toJsonValue(m_team_key));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

QString OAITeam_Robot::getKey() const {
    return m_key;
}
void OAITeam_Robot::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAITeam_Robot::is_key_Set() const{
    return m_key_isSet;
}

bool OAITeam_Robot::is_key_Valid() const{
    return m_key_isValid;
}

QString OAITeam_Robot::getRobotName() const {
    return m_robot_name;
}
void OAITeam_Robot::setRobotName(const QString &robot_name) {
    m_robot_name = robot_name;
    m_robot_name_isSet = true;
}

bool OAITeam_Robot::is_robot_name_Set() const{
    return m_robot_name_isSet;
}

bool OAITeam_Robot::is_robot_name_Valid() const{
    return m_robot_name_isValid;
}

QString OAITeam_Robot::getTeamKey() const {
    return m_team_key;
}
void OAITeam_Robot::setTeamKey(const QString &team_key) {
    m_team_key = team_key;
    m_team_key_isSet = true;
}

bool OAITeam_Robot::is_team_key_Set() const{
    return m_team_key_isSet;
}

bool OAITeam_Robot::is_team_key_Valid() const{
    return m_team_key_isValid;
}

qint32 OAITeam_Robot::getYear() const {
    return m_year;
}
void OAITeam_Robot::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAITeam_Robot::is_year_Set() const{
    return m_year_isSet;
}

bool OAITeam_Robot::is_year_Valid() const{
    return m_year_isValid;
}

bool OAITeam_Robot::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_robot_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITeam_Robot::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_key_isValid && m_robot_name_isValid && m_team_key_isValid && m_year_isValid && true;
}

} // namespace OpenAPI
