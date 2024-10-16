/**
 * Soccer v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGoal.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGoal::OAIGoal(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGoal::OAIGoal() {
    this->initializeModel();
}

OAIGoal::~OAIGoal() {}

void OAIGoal::initializeModel() {

    m_assisted_by_player_id1_isSet = false;
    m_assisted_by_player_id1_isValid = false;

    m_assisted_by_player_id2_isSet = false;
    m_assisted_by_player_id2_isValid = false;

    m_assisted_by_player_name1_isSet = false;
    m_assisted_by_player_name1_isValid = false;

    m_assisted_by_player_name2_isSet = false;
    m_assisted_by_player_name2_isValid = false;

    m_game_id_isSet = false;
    m_game_id_isValid = false;

    m_game_minute_isSet = false;
    m_game_minute_isValid = false;

    m_game_minute_extra_isSet = false;
    m_game_minute_extra_isValid = false;

    m_goal_id_isSet = false;
    m_goal_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIGoal::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGoal::fromJsonObject(QJsonObject json) {

    m_assisted_by_player_id1_isValid = ::OpenAPI::fromJsonValue(m_assisted_by_player_id1, json[QString("AssistedByPlayerId1")]);
    m_assisted_by_player_id1_isSet = !json[QString("AssistedByPlayerId1")].isNull() && m_assisted_by_player_id1_isValid;

    m_assisted_by_player_id2_isValid = ::OpenAPI::fromJsonValue(m_assisted_by_player_id2, json[QString("AssistedByPlayerId2")]);
    m_assisted_by_player_id2_isSet = !json[QString("AssistedByPlayerId2")].isNull() && m_assisted_by_player_id2_isValid;

    m_assisted_by_player_name1_isValid = ::OpenAPI::fromJsonValue(m_assisted_by_player_name1, json[QString("AssistedByPlayerName1")]);
    m_assisted_by_player_name1_isSet = !json[QString("AssistedByPlayerName1")].isNull() && m_assisted_by_player_name1_isValid;

    m_assisted_by_player_name2_isValid = ::OpenAPI::fromJsonValue(m_assisted_by_player_name2, json[QString("AssistedByPlayerName2")]);
    m_assisted_by_player_name2_isSet = !json[QString("AssistedByPlayerName2")].isNull() && m_assisted_by_player_name2_isValid;

    m_game_id_isValid = ::OpenAPI::fromJsonValue(m_game_id, json[QString("GameId")]);
    m_game_id_isSet = !json[QString("GameId")].isNull() && m_game_id_isValid;

    m_game_minute_isValid = ::OpenAPI::fromJsonValue(m_game_minute, json[QString("GameMinute")]);
    m_game_minute_isSet = !json[QString("GameMinute")].isNull() && m_game_minute_isValid;

    m_game_minute_extra_isValid = ::OpenAPI::fromJsonValue(m_game_minute_extra, json[QString("GameMinuteExtra")]);
    m_game_minute_extra_isSet = !json[QString("GameMinuteExtra")].isNull() && m_game_minute_extra_isValid;

    m_goal_id_isValid = ::OpenAPI::fromJsonValue(m_goal_id, json[QString("GoalId")]);
    m_goal_id_isSet = !json[QString("GoalId")].isNull() && m_goal_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerId")]);
    m_player_id_isSet = !json[QString("PlayerId")].isNull() && m_player_id_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamId")]);
    m_team_id_isSet = !json[QString("TeamId")].isNull() && m_team_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;
}

QString OAIGoal::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGoal::asJsonObject() const {
    QJsonObject obj;
    if (m_assisted_by_player_id1_isSet) {
        obj.insert(QString("AssistedByPlayerId1"), ::OpenAPI::toJsonValue(m_assisted_by_player_id1));
    }
    if (m_assisted_by_player_id2_isSet) {
        obj.insert(QString("AssistedByPlayerId2"), ::OpenAPI::toJsonValue(m_assisted_by_player_id2));
    }
    if (m_assisted_by_player_name1_isSet) {
        obj.insert(QString("AssistedByPlayerName1"), ::OpenAPI::toJsonValue(m_assisted_by_player_name1));
    }
    if (m_assisted_by_player_name2_isSet) {
        obj.insert(QString("AssistedByPlayerName2"), ::OpenAPI::toJsonValue(m_assisted_by_player_name2));
    }
    if (m_game_id_isSet) {
        obj.insert(QString("GameId"), ::OpenAPI::toJsonValue(m_game_id));
    }
    if (m_game_minute_isSet) {
        obj.insert(QString("GameMinute"), ::OpenAPI::toJsonValue(m_game_minute));
    }
    if (m_game_minute_extra_isSet) {
        obj.insert(QString("GameMinuteExtra"), ::OpenAPI::toJsonValue(m_game_minute_extra));
    }
    if (m_goal_id_isSet) {
        obj.insert(QString("GoalId"), ::OpenAPI::toJsonValue(m_goal_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerId"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamId"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAIGoal::getAssistedByPlayerId1() const {
    return m_assisted_by_player_id1;
}
void OAIGoal::setAssistedByPlayerId1(const qint32 &assisted_by_player_id1) {
    m_assisted_by_player_id1 = assisted_by_player_id1;
    m_assisted_by_player_id1_isSet = true;
}

bool OAIGoal::is_assisted_by_player_id1_Set() const{
    return m_assisted_by_player_id1_isSet;
}

bool OAIGoal::is_assisted_by_player_id1_Valid() const{
    return m_assisted_by_player_id1_isValid;
}

qint32 OAIGoal::getAssistedByPlayerId2() const {
    return m_assisted_by_player_id2;
}
void OAIGoal::setAssistedByPlayerId2(const qint32 &assisted_by_player_id2) {
    m_assisted_by_player_id2 = assisted_by_player_id2;
    m_assisted_by_player_id2_isSet = true;
}

bool OAIGoal::is_assisted_by_player_id2_Set() const{
    return m_assisted_by_player_id2_isSet;
}

bool OAIGoal::is_assisted_by_player_id2_Valid() const{
    return m_assisted_by_player_id2_isValid;
}

QString OAIGoal::getAssistedByPlayerName1() const {
    return m_assisted_by_player_name1;
}
void OAIGoal::setAssistedByPlayerName1(const QString &assisted_by_player_name1) {
    m_assisted_by_player_name1 = assisted_by_player_name1;
    m_assisted_by_player_name1_isSet = true;
}

bool OAIGoal::is_assisted_by_player_name1_Set() const{
    return m_assisted_by_player_name1_isSet;
}

bool OAIGoal::is_assisted_by_player_name1_Valid() const{
    return m_assisted_by_player_name1_isValid;
}

QString OAIGoal::getAssistedByPlayerName2() const {
    return m_assisted_by_player_name2;
}
void OAIGoal::setAssistedByPlayerName2(const QString &assisted_by_player_name2) {
    m_assisted_by_player_name2 = assisted_by_player_name2;
    m_assisted_by_player_name2_isSet = true;
}

bool OAIGoal::is_assisted_by_player_name2_Set() const{
    return m_assisted_by_player_name2_isSet;
}

bool OAIGoal::is_assisted_by_player_name2_Valid() const{
    return m_assisted_by_player_name2_isValid;
}

qint32 OAIGoal::getGameId() const {
    return m_game_id;
}
void OAIGoal::setGameId(const qint32 &game_id) {
    m_game_id = game_id;
    m_game_id_isSet = true;
}

bool OAIGoal::is_game_id_Set() const{
    return m_game_id_isSet;
}

bool OAIGoal::is_game_id_Valid() const{
    return m_game_id_isValid;
}

qint32 OAIGoal::getGameMinute() const {
    return m_game_minute;
}
void OAIGoal::setGameMinute(const qint32 &game_minute) {
    m_game_minute = game_minute;
    m_game_minute_isSet = true;
}

bool OAIGoal::is_game_minute_Set() const{
    return m_game_minute_isSet;
}

bool OAIGoal::is_game_minute_Valid() const{
    return m_game_minute_isValid;
}

qint32 OAIGoal::getGameMinuteExtra() const {
    return m_game_minute_extra;
}
void OAIGoal::setGameMinuteExtra(const qint32 &game_minute_extra) {
    m_game_minute_extra = game_minute_extra;
    m_game_minute_extra_isSet = true;
}

bool OAIGoal::is_game_minute_extra_Set() const{
    return m_game_minute_extra_isSet;
}

bool OAIGoal::is_game_minute_extra_Valid() const{
    return m_game_minute_extra_isValid;
}

qint32 OAIGoal::getGoalId() const {
    return m_goal_id;
}
void OAIGoal::setGoalId(const qint32 &goal_id) {
    m_goal_id = goal_id;
    m_goal_id_isSet = true;
}

bool OAIGoal::is_goal_id_Set() const{
    return m_goal_id_isSet;
}

bool OAIGoal::is_goal_id_Valid() const{
    return m_goal_id_isValid;
}

QString OAIGoal::getName() const {
    return m_name;
}
void OAIGoal::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGoal::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGoal::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIGoal::getPlayerId() const {
    return m_player_id;
}
void OAIGoal::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIGoal::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIGoal::is_player_id_Valid() const{
    return m_player_id_isValid;
}

qint32 OAIGoal::getTeamId() const {
    return m_team_id;
}
void OAIGoal::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAIGoal::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAIGoal::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QString OAIGoal::getType() const {
    return m_type;
}
void OAIGoal::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGoal::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGoal::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGoal::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_assisted_by_player_id1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_assisted_by_player_id2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_assisted_by_player_name1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_assisted_by_player_name2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_minute_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_minute_extra_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_goal_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGoal::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
