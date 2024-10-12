/**
 * MLB v3 Stats
 * MLB scores, stats, and news API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDfsSlatePlayer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDfsSlatePlayer::OAIDfsSlatePlayer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDfsSlatePlayer::OAIDfsSlatePlayer() {
    this->initializeModel();
}

OAIDfsSlatePlayer::~OAIDfsSlatePlayer() {}

void OAIDfsSlatePlayer::initializeModel() {

    m_operator_player_id_isSet = false;
    m_operator_player_id_isValid = false;

    m_operator_player_name_isSet = false;
    m_operator_player_name_isValid = false;

    m_operator_position_isSet = false;
    m_operator_position_isValid = false;

    m_operator_roster_slots_isSet = false;
    m_operator_roster_slots_isValid = false;

    m_operator_salary_isSet = false;
    m_operator_salary_isValid = false;

    m_operator_slate_player_id_isSet = false;
    m_operator_slate_player_id_isValid = false;

    m_player_game_projection_stat_id_isSet = false;
    m_player_game_projection_stat_id_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_removed_by_operator_isSet = false;
    m_removed_by_operator_isValid = false;

    m_slate_game_id_isSet = false;
    m_slate_game_id_isValid = false;

    m_slate_id_isSet = false;
    m_slate_id_isValid = false;

    m_slate_player_id_isSet = false;
    m_slate_player_id_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;
}

void OAIDfsSlatePlayer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDfsSlatePlayer::fromJsonObject(QJsonObject json) {

    m_operator_player_id_isValid = ::OpenAPI::fromJsonValue(m_operator_player_id, json[QString("OperatorPlayerID")]);
    m_operator_player_id_isSet = !json[QString("OperatorPlayerID")].isNull() && m_operator_player_id_isValid;

    m_operator_player_name_isValid = ::OpenAPI::fromJsonValue(m_operator_player_name, json[QString("OperatorPlayerName")]);
    m_operator_player_name_isSet = !json[QString("OperatorPlayerName")].isNull() && m_operator_player_name_isValid;

    m_operator_position_isValid = ::OpenAPI::fromJsonValue(m_operator_position, json[QString("OperatorPosition")]);
    m_operator_position_isSet = !json[QString("OperatorPosition")].isNull() && m_operator_position_isValid;

    m_operator_roster_slots_isValid = ::OpenAPI::fromJsonValue(m_operator_roster_slots, json[QString("OperatorRosterSlots")]);
    m_operator_roster_slots_isSet = !json[QString("OperatorRosterSlots")].isNull() && m_operator_roster_slots_isValid;

    m_operator_salary_isValid = ::OpenAPI::fromJsonValue(m_operator_salary, json[QString("OperatorSalary")]);
    m_operator_salary_isSet = !json[QString("OperatorSalary")].isNull() && m_operator_salary_isValid;

    m_operator_slate_player_id_isValid = ::OpenAPI::fromJsonValue(m_operator_slate_player_id, json[QString("OperatorSlatePlayerID")]);
    m_operator_slate_player_id_isSet = !json[QString("OperatorSlatePlayerID")].isNull() && m_operator_slate_player_id_isValid;

    m_player_game_projection_stat_id_isValid = ::OpenAPI::fromJsonValue(m_player_game_projection_stat_id, json[QString("PlayerGameProjectionStatID")]);
    m_player_game_projection_stat_id_isSet = !json[QString("PlayerGameProjectionStatID")].isNull() && m_player_game_projection_stat_id_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_removed_by_operator_isValid = ::OpenAPI::fromJsonValue(m_removed_by_operator, json[QString("RemovedByOperator")]);
    m_removed_by_operator_isSet = !json[QString("RemovedByOperator")].isNull() && m_removed_by_operator_isValid;

    m_slate_game_id_isValid = ::OpenAPI::fromJsonValue(m_slate_game_id, json[QString("SlateGameID")]);
    m_slate_game_id_isSet = !json[QString("SlateGameID")].isNull() && m_slate_game_id_isValid;

    m_slate_id_isValid = ::OpenAPI::fromJsonValue(m_slate_id, json[QString("SlateID")]);
    m_slate_id_isSet = !json[QString("SlateID")].isNull() && m_slate_id_isValid;

    m_slate_player_id_isValid = ::OpenAPI::fromJsonValue(m_slate_player_id, json[QString("SlatePlayerID")]);
    m_slate_player_id_isSet = !json[QString("SlatePlayerID")].isNull() && m_slate_player_id_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;
}

QString OAIDfsSlatePlayer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDfsSlatePlayer::asJsonObject() const {
    QJsonObject obj;
    if (m_operator_player_id_isSet) {
        obj.insert(QString("OperatorPlayerID"), ::OpenAPI::toJsonValue(m_operator_player_id));
    }
    if (m_operator_player_name_isSet) {
        obj.insert(QString("OperatorPlayerName"), ::OpenAPI::toJsonValue(m_operator_player_name));
    }
    if (m_operator_position_isSet) {
        obj.insert(QString("OperatorPosition"), ::OpenAPI::toJsonValue(m_operator_position));
    }
    if (m_operator_roster_slots.size() > 0) {
        obj.insert(QString("OperatorRosterSlots"), ::OpenAPI::toJsonValue(m_operator_roster_slots));
    }
    if (m_operator_salary_isSet) {
        obj.insert(QString("OperatorSalary"), ::OpenAPI::toJsonValue(m_operator_salary));
    }
    if (m_operator_slate_player_id_isSet) {
        obj.insert(QString("OperatorSlatePlayerID"), ::OpenAPI::toJsonValue(m_operator_slate_player_id));
    }
    if (m_player_game_projection_stat_id_isSet) {
        obj.insert(QString("PlayerGameProjectionStatID"), ::OpenAPI::toJsonValue(m_player_game_projection_stat_id));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_removed_by_operator_isSet) {
        obj.insert(QString("RemovedByOperator"), ::OpenAPI::toJsonValue(m_removed_by_operator));
    }
    if (m_slate_game_id_isSet) {
        obj.insert(QString("SlateGameID"), ::OpenAPI::toJsonValue(m_slate_game_id));
    }
    if (m_slate_id_isSet) {
        obj.insert(QString("SlateID"), ::OpenAPI::toJsonValue(m_slate_id));
    }
    if (m_slate_player_id_isSet) {
        obj.insert(QString("SlatePlayerID"), ::OpenAPI::toJsonValue(m_slate_player_id));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    return obj;
}

QString OAIDfsSlatePlayer::getOperatorPlayerId() const {
    return m_operator_player_id;
}
void OAIDfsSlatePlayer::setOperatorPlayerId(const QString &operator_player_id) {
    m_operator_player_id = operator_player_id;
    m_operator_player_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_operator_player_id_Set() const{
    return m_operator_player_id_isSet;
}

bool OAIDfsSlatePlayer::is_operator_player_id_Valid() const{
    return m_operator_player_id_isValid;
}

QString OAIDfsSlatePlayer::getOperatorPlayerName() const {
    return m_operator_player_name;
}
void OAIDfsSlatePlayer::setOperatorPlayerName(const QString &operator_player_name) {
    m_operator_player_name = operator_player_name;
    m_operator_player_name_isSet = true;
}

bool OAIDfsSlatePlayer::is_operator_player_name_Set() const{
    return m_operator_player_name_isSet;
}

bool OAIDfsSlatePlayer::is_operator_player_name_Valid() const{
    return m_operator_player_name_isValid;
}

QString OAIDfsSlatePlayer::getOperatorPosition() const {
    return m_operator_position;
}
void OAIDfsSlatePlayer::setOperatorPosition(const QString &operator_position) {
    m_operator_position = operator_position;
    m_operator_position_isSet = true;
}

bool OAIDfsSlatePlayer::is_operator_position_Set() const{
    return m_operator_position_isSet;
}

bool OAIDfsSlatePlayer::is_operator_position_Valid() const{
    return m_operator_position_isValid;
}

QList<QString> OAIDfsSlatePlayer::getOperatorRosterSlots() const {
    return m_operator_roster_slots;
}
void OAIDfsSlatePlayer::setOperatorRosterSlots(const QList<QString> &operator_roster_slots) {
    m_operator_roster_slots = operator_roster_slots;
    m_operator_roster_slots_isSet = true;
}

bool OAIDfsSlatePlayer::is_operator_roster_slots_Set() const{
    return m_operator_roster_slots_isSet;
}

bool OAIDfsSlatePlayer::is_operator_roster_slots_Valid() const{
    return m_operator_roster_slots_isValid;
}

qint32 OAIDfsSlatePlayer::getOperatorSalary() const {
    return m_operator_salary;
}
void OAIDfsSlatePlayer::setOperatorSalary(const qint32 &operator_salary) {
    m_operator_salary = operator_salary;
    m_operator_salary_isSet = true;
}

bool OAIDfsSlatePlayer::is_operator_salary_Set() const{
    return m_operator_salary_isSet;
}

bool OAIDfsSlatePlayer::is_operator_salary_Valid() const{
    return m_operator_salary_isValid;
}

QString OAIDfsSlatePlayer::getOperatorSlatePlayerId() const {
    return m_operator_slate_player_id;
}
void OAIDfsSlatePlayer::setOperatorSlatePlayerId(const QString &operator_slate_player_id) {
    m_operator_slate_player_id = operator_slate_player_id;
    m_operator_slate_player_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_operator_slate_player_id_Set() const{
    return m_operator_slate_player_id_isSet;
}

bool OAIDfsSlatePlayer::is_operator_slate_player_id_Valid() const{
    return m_operator_slate_player_id_isValid;
}

qint32 OAIDfsSlatePlayer::getPlayerGameProjectionStatId() const {
    return m_player_game_projection_stat_id;
}
void OAIDfsSlatePlayer::setPlayerGameProjectionStatId(const qint32 &player_game_projection_stat_id) {
    m_player_game_projection_stat_id = player_game_projection_stat_id;
    m_player_game_projection_stat_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_player_game_projection_stat_id_Set() const{
    return m_player_game_projection_stat_id_isSet;
}

bool OAIDfsSlatePlayer::is_player_game_projection_stat_id_Valid() const{
    return m_player_game_projection_stat_id_isValid;
}

qint32 OAIDfsSlatePlayer::getPlayerId() const {
    return m_player_id;
}
void OAIDfsSlatePlayer::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIDfsSlatePlayer::is_player_id_Valid() const{
    return m_player_id_isValid;
}

bool OAIDfsSlatePlayer::isRemovedByOperator() const {
    return m_removed_by_operator;
}
void OAIDfsSlatePlayer::setRemovedByOperator(const bool &removed_by_operator) {
    m_removed_by_operator = removed_by_operator;
    m_removed_by_operator_isSet = true;
}

bool OAIDfsSlatePlayer::is_removed_by_operator_Set() const{
    return m_removed_by_operator_isSet;
}

bool OAIDfsSlatePlayer::is_removed_by_operator_Valid() const{
    return m_removed_by_operator_isValid;
}

qint32 OAIDfsSlatePlayer::getSlateGameId() const {
    return m_slate_game_id;
}
void OAIDfsSlatePlayer::setSlateGameId(const qint32 &slate_game_id) {
    m_slate_game_id = slate_game_id;
    m_slate_game_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_slate_game_id_Set() const{
    return m_slate_game_id_isSet;
}

bool OAIDfsSlatePlayer::is_slate_game_id_Valid() const{
    return m_slate_game_id_isValid;
}

qint32 OAIDfsSlatePlayer::getSlateId() const {
    return m_slate_id;
}
void OAIDfsSlatePlayer::setSlateId(const qint32 &slate_id) {
    m_slate_id = slate_id;
    m_slate_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_slate_id_Set() const{
    return m_slate_id_isSet;
}

bool OAIDfsSlatePlayer::is_slate_id_Valid() const{
    return m_slate_id_isValid;
}

qint32 OAIDfsSlatePlayer::getSlatePlayerId() const {
    return m_slate_player_id;
}
void OAIDfsSlatePlayer::setSlatePlayerId(const qint32 &slate_player_id) {
    m_slate_player_id = slate_player_id;
    m_slate_player_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_slate_player_id_Set() const{
    return m_slate_player_id_isSet;
}

bool OAIDfsSlatePlayer::is_slate_player_id_Valid() const{
    return m_slate_player_id_isValid;
}

QString OAIDfsSlatePlayer::getTeam() const {
    return m_team;
}
void OAIDfsSlatePlayer::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIDfsSlatePlayer::is_team_Set() const{
    return m_team_isSet;
}

bool OAIDfsSlatePlayer::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAIDfsSlatePlayer::getTeamId() const {
    return m_team_id;
}
void OAIDfsSlatePlayer::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAIDfsSlatePlayer::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAIDfsSlatePlayer::is_team_id_Valid() const{
    return m_team_id_isValid;
}

bool OAIDfsSlatePlayer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_operator_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_player_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_roster_slots.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_salary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_slate_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_game_projection_stat_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_removed_by_operator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slate_game_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slate_player_id_isSet) {
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

bool OAIDfsSlatePlayer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
