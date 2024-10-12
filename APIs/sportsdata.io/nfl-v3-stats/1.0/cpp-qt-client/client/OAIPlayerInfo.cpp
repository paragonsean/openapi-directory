/**
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlayerInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayerInfo::OAIPlayerInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayerInfo::OAIPlayerInfo() {
    this->initializeModel();
}

OAIPlayerInfo::~OAIPlayerInfo() {}

void OAIPlayerInfo::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;
}

void OAIPlayerInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayerInfo::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;
}

QString OAIPlayerInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayerInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_position_isSet) {
        obj.insert(QString("Position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    return obj;
}

QString OAIPlayerInfo::getName() const {
    return m_name;
}
void OAIPlayerInfo::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPlayerInfo::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPlayerInfo::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIPlayerInfo::getPlayerId() const {
    return m_player_id;
}
void OAIPlayerInfo::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIPlayerInfo::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIPlayerInfo::is_player_id_Valid() const{
    return m_player_id_isValid;
}

QString OAIPlayerInfo::getPosition() const {
    return m_position;
}
void OAIPlayerInfo::setPosition(const QString &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIPlayerInfo::is_position_Set() const{
    return m_position_isSet;
}

bool OAIPlayerInfo::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIPlayerInfo::getTeam() const {
    return m_team;
}
void OAIPlayerInfo::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIPlayerInfo::is_team_Set() const{
    return m_team_isSet;
}

bool OAIPlayerInfo::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAIPlayerInfo::getTeamId() const {
    return m_team_id;
}
void OAIPlayerInfo::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAIPlayerInfo::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAIPlayerInfo::is_team_id_Valid() const{
    return m_team_id_isValid;
}

bool OAIPlayerInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlayerInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
