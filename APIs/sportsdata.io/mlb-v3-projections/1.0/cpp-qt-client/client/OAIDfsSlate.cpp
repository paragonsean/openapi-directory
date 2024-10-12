/**
 * MLB v3 Projections
 * MLB projections API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDfsSlate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDfsSlate::OAIDfsSlate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDfsSlate::OAIDfsSlate() {
    this->initializeModel();
}

OAIDfsSlate::~OAIDfsSlate() {}

void OAIDfsSlate::initializeModel() {

    m_dfs_slate_games_isSet = false;
    m_dfs_slate_games_isValid = false;

    m_dfs_slate_players_isSet = false;
    m_dfs_slate_players_isValid = false;

    m_is_multi_day_slate_isSet = false;
    m_is_multi_day_slate_isValid = false;

    m_number_of_games_isSet = false;
    m_number_of_games_isValid = false;

    m_r_operator_isSet = false;
    m_r_operator_isValid = false;

    m_operator_day_isSet = false;
    m_operator_day_isValid = false;

    m_operator_game_type_isSet = false;
    m_operator_game_type_isValid = false;

    m_operator_name_isSet = false;
    m_operator_name_isValid = false;

    m_operator_slate_id_isSet = false;
    m_operator_slate_id_isValid = false;

    m_operator_start_time_isSet = false;
    m_operator_start_time_isValid = false;

    m_removed_by_operator_isSet = false;
    m_removed_by_operator_isValid = false;

    m_salary_cap_isSet = false;
    m_salary_cap_isValid = false;

    m_slate_id_isSet = false;
    m_slate_id_isValid = false;

    m_slate_roster_slots_isSet = false;
    m_slate_roster_slots_isValid = false;
}

void OAIDfsSlate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDfsSlate::fromJsonObject(QJsonObject json) {

    m_dfs_slate_games_isValid = ::OpenAPI::fromJsonValue(m_dfs_slate_games, json[QString("DfsSlateGames")]);
    m_dfs_slate_games_isSet = !json[QString("DfsSlateGames")].isNull() && m_dfs_slate_games_isValid;

    m_dfs_slate_players_isValid = ::OpenAPI::fromJsonValue(m_dfs_slate_players, json[QString("DfsSlatePlayers")]);
    m_dfs_slate_players_isSet = !json[QString("DfsSlatePlayers")].isNull() && m_dfs_slate_players_isValid;

    m_is_multi_day_slate_isValid = ::OpenAPI::fromJsonValue(m_is_multi_day_slate, json[QString("IsMultiDaySlate")]);
    m_is_multi_day_slate_isSet = !json[QString("IsMultiDaySlate")].isNull() && m_is_multi_day_slate_isValid;

    m_number_of_games_isValid = ::OpenAPI::fromJsonValue(m_number_of_games, json[QString("NumberOfGames")]);
    m_number_of_games_isSet = !json[QString("NumberOfGames")].isNull() && m_number_of_games_isValid;

    m_r_operator_isValid = ::OpenAPI::fromJsonValue(m_r_operator, json[QString("Operator")]);
    m_r_operator_isSet = !json[QString("Operator")].isNull() && m_r_operator_isValid;

    m_operator_day_isValid = ::OpenAPI::fromJsonValue(m_operator_day, json[QString("OperatorDay")]);
    m_operator_day_isSet = !json[QString("OperatorDay")].isNull() && m_operator_day_isValid;

    m_operator_game_type_isValid = ::OpenAPI::fromJsonValue(m_operator_game_type, json[QString("OperatorGameType")]);
    m_operator_game_type_isSet = !json[QString("OperatorGameType")].isNull() && m_operator_game_type_isValid;

    m_operator_name_isValid = ::OpenAPI::fromJsonValue(m_operator_name, json[QString("OperatorName")]);
    m_operator_name_isSet = !json[QString("OperatorName")].isNull() && m_operator_name_isValid;

    m_operator_slate_id_isValid = ::OpenAPI::fromJsonValue(m_operator_slate_id, json[QString("OperatorSlateID")]);
    m_operator_slate_id_isSet = !json[QString("OperatorSlateID")].isNull() && m_operator_slate_id_isValid;

    m_operator_start_time_isValid = ::OpenAPI::fromJsonValue(m_operator_start_time, json[QString("OperatorStartTime")]);
    m_operator_start_time_isSet = !json[QString("OperatorStartTime")].isNull() && m_operator_start_time_isValid;

    m_removed_by_operator_isValid = ::OpenAPI::fromJsonValue(m_removed_by_operator, json[QString("RemovedByOperator")]);
    m_removed_by_operator_isSet = !json[QString("RemovedByOperator")].isNull() && m_removed_by_operator_isValid;

    m_salary_cap_isValid = ::OpenAPI::fromJsonValue(m_salary_cap, json[QString("SalaryCap")]);
    m_salary_cap_isSet = !json[QString("SalaryCap")].isNull() && m_salary_cap_isValid;

    m_slate_id_isValid = ::OpenAPI::fromJsonValue(m_slate_id, json[QString("SlateID")]);
    m_slate_id_isSet = !json[QString("SlateID")].isNull() && m_slate_id_isValid;

    m_slate_roster_slots_isValid = ::OpenAPI::fromJsonValue(m_slate_roster_slots, json[QString("SlateRosterSlots")]);
    m_slate_roster_slots_isSet = !json[QString("SlateRosterSlots")].isNull() && m_slate_roster_slots_isValid;
}

QString OAIDfsSlate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDfsSlate::asJsonObject() const {
    QJsonObject obj;
    if (m_dfs_slate_games.size() > 0) {
        obj.insert(QString("DfsSlateGames"), ::OpenAPI::toJsonValue(m_dfs_slate_games));
    }
    if (m_dfs_slate_players.size() > 0) {
        obj.insert(QString("DfsSlatePlayers"), ::OpenAPI::toJsonValue(m_dfs_slate_players));
    }
    if (m_is_multi_day_slate_isSet) {
        obj.insert(QString("IsMultiDaySlate"), ::OpenAPI::toJsonValue(m_is_multi_day_slate));
    }
    if (m_number_of_games_isSet) {
        obj.insert(QString("NumberOfGames"), ::OpenAPI::toJsonValue(m_number_of_games));
    }
    if (m_r_operator_isSet) {
        obj.insert(QString("Operator"), ::OpenAPI::toJsonValue(m_r_operator));
    }
    if (m_operator_day_isSet) {
        obj.insert(QString("OperatorDay"), ::OpenAPI::toJsonValue(m_operator_day));
    }
    if (m_operator_game_type_isSet) {
        obj.insert(QString("OperatorGameType"), ::OpenAPI::toJsonValue(m_operator_game_type));
    }
    if (m_operator_name_isSet) {
        obj.insert(QString("OperatorName"), ::OpenAPI::toJsonValue(m_operator_name));
    }
    if (m_operator_slate_id_isSet) {
        obj.insert(QString("OperatorSlateID"), ::OpenAPI::toJsonValue(m_operator_slate_id));
    }
    if (m_operator_start_time_isSet) {
        obj.insert(QString("OperatorStartTime"), ::OpenAPI::toJsonValue(m_operator_start_time));
    }
    if (m_removed_by_operator_isSet) {
        obj.insert(QString("RemovedByOperator"), ::OpenAPI::toJsonValue(m_removed_by_operator));
    }
    if (m_salary_cap_isSet) {
        obj.insert(QString("SalaryCap"), ::OpenAPI::toJsonValue(m_salary_cap));
    }
    if (m_slate_id_isSet) {
        obj.insert(QString("SlateID"), ::OpenAPI::toJsonValue(m_slate_id));
    }
    if (m_slate_roster_slots.size() > 0) {
        obj.insert(QString("SlateRosterSlots"), ::OpenAPI::toJsonValue(m_slate_roster_slots));
    }
    return obj;
}

QList<OAIDfsSlateGame> OAIDfsSlate::getDfsSlateGames() const {
    return m_dfs_slate_games;
}
void OAIDfsSlate::setDfsSlateGames(const QList<OAIDfsSlateGame> &dfs_slate_games) {
    m_dfs_slate_games = dfs_slate_games;
    m_dfs_slate_games_isSet = true;
}

bool OAIDfsSlate::is_dfs_slate_games_Set() const{
    return m_dfs_slate_games_isSet;
}

bool OAIDfsSlate::is_dfs_slate_games_Valid() const{
    return m_dfs_slate_games_isValid;
}

QList<OAIDfsSlatePlayer> OAIDfsSlate::getDfsSlatePlayers() const {
    return m_dfs_slate_players;
}
void OAIDfsSlate::setDfsSlatePlayers(const QList<OAIDfsSlatePlayer> &dfs_slate_players) {
    m_dfs_slate_players = dfs_slate_players;
    m_dfs_slate_players_isSet = true;
}

bool OAIDfsSlate::is_dfs_slate_players_Set() const{
    return m_dfs_slate_players_isSet;
}

bool OAIDfsSlate::is_dfs_slate_players_Valid() const{
    return m_dfs_slate_players_isValid;
}

bool OAIDfsSlate::isIsMultiDaySlate() const {
    return m_is_multi_day_slate;
}
void OAIDfsSlate::setIsMultiDaySlate(const bool &is_multi_day_slate) {
    m_is_multi_day_slate = is_multi_day_slate;
    m_is_multi_day_slate_isSet = true;
}

bool OAIDfsSlate::is_is_multi_day_slate_Set() const{
    return m_is_multi_day_slate_isSet;
}

bool OAIDfsSlate::is_is_multi_day_slate_Valid() const{
    return m_is_multi_day_slate_isValid;
}

qint32 OAIDfsSlate::getNumberOfGames() const {
    return m_number_of_games;
}
void OAIDfsSlate::setNumberOfGames(const qint32 &number_of_games) {
    m_number_of_games = number_of_games;
    m_number_of_games_isSet = true;
}

bool OAIDfsSlate::is_number_of_games_Set() const{
    return m_number_of_games_isSet;
}

bool OAIDfsSlate::is_number_of_games_Valid() const{
    return m_number_of_games_isValid;
}

QString OAIDfsSlate::getROperator() const {
    return m_r_operator;
}
void OAIDfsSlate::setROperator(const QString &r_operator) {
    m_r_operator = r_operator;
    m_r_operator_isSet = true;
}

bool OAIDfsSlate::is_r_operator_Set() const{
    return m_r_operator_isSet;
}

bool OAIDfsSlate::is_r_operator_Valid() const{
    return m_r_operator_isValid;
}

QString OAIDfsSlate::getOperatorDay() const {
    return m_operator_day;
}
void OAIDfsSlate::setOperatorDay(const QString &operator_day) {
    m_operator_day = operator_day;
    m_operator_day_isSet = true;
}

bool OAIDfsSlate::is_operator_day_Set() const{
    return m_operator_day_isSet;
}

bool OAIDfsSlate::is_operator_day_Valid() const{
    return m_operator_day_isValid;
}

QString OAIDfsSlate::getOperatorGameType() const {
    return m_operator_game_type;
}
void OAIDfsSlate::setOperatorGameType(const QString &operator_game_type) {
    m_operator_game_type = operator_game_type;
    m_operator_game_type_isSet = true;
}

bool OAIDfsSlate::is_operator_game_type_Set() const{
    return m_operator_game_type_isSet;
}

bool OAIDfsSlate::is_operator_game_type_Valid() const{
    return m_operator_game_type_isValid;
}

QString OAIDfsSlate::getOperatorName() const {
    return m_operator_name;
}
void OAIDfsSlate::setOperatorName(const QString &operator_name) {
    m_operator_name = operator_name;
    m_operator_name_isSet = true;
}

bool OAIDfsSlate::is_operator_name_Set() const{
    return m_operator_name_isSet;
}

bool OAIDfsSlate::is_operator_name_Valid() const{
    return m_operator_name_isValid;
}

qint32 OAIDfsSlate::getOperatorSlateId() const {
    return m_operator_slate_id;
}
void OAIDfsSlate::setOperatorSlateId(const qint32 &operator_slate_id) {
    m_operator_slate_id = operator_slate_id;
    m_operator_slate_id_isSet = true;
}

bool OAIDfsSlate::is_operator_slate_id_Set() const{
    return m_operator_slate_id_isSet;
}

bool OAIDfsSlate::is_operator_slate_id_Valid() const{
    return m_operator_slate_id_isValid;
}

QString OAIDfsSlate::getOperatorStartTime() const {
    return m_operator_start_time;
}
void OAIDfsSlate::setOperatorStartTime(const QString &operator_start_time) {
    m_operator_start_time = operator_start_time;
    m_operator_start_time_isSet = true;
}

bool OAIDfsSlate::is_operator_start_time_Set() const{
    return m_operator_start_time_isSet;
}

bool OAIDfsSlate::is_operator_start_time_Valid() const{
    return m_operator_start_time_isValid;
}

bool OAIDfsSlate::isRemovedByOperator() const {
    return m_removed_by_operator;
}
void OAIDfsSlate::setRemovedByOperator(const bool &removed_by_operator) {
    m_removed_by_operator = removed_by_operator;
    m_removed_by_operator_isSet = true;
}

bool OAIDfsSlate::is_removed_by_operator_Set() const{
    return m_removed_by_operator_isSet;
}

bool OAIDfsSlate::is_removed_by_operator_Valid() const{
    return m_removed_by_operator_isValid;
}

qint32 OAIDfsSlate::getSalaryCap() const {
    return m_salary_cap;
}
void OAIDfsSlate::setSalaryCap(const qint32 &salary_cap) {
    m_salary_cap = salary_cap;
    m_salary_cap_isSet = true;
}

bool OAIDfsSlate::is_salary_cap_Set() const{
    return m_salary_cap_isSet;
}

bool OAIDfsSlate::is_salary_cap_Valid() const{
    return m_salary_cap_isValid;
}

qint32 OAIDfsSlate::getSlateId() const {
    return m_slate_id;
}
void OAIDfsSlate::setSlateId(const qint32 &slate_id) {
    m_slate_id = slate_id;
    m_slate_id_isSet = true;
}

bool OAIDfsSlate::is_slate_id_Set() const{
    return m_slate_id_isSet;
}

bool OAIDfsSlate::is_slate_id_Valid() const{
    return m_slate_id_isValid;
}

QList<QString> OAIDfsSlate::getSlateRosterSlots() const {
    return m_slate_roster_slots;
}
void OAIDfsSlate::setSlateRosterSlots(const QList<QString> &slate_roster_slots) {
    m_slate_roster_slots = slate_roster_slots;
    m_slate_roster_slots_isSet = true;
}

bool OAIDfsSlate::is_slate_roster_slots_Set() const{
    return m_slate_roster_slots_isSet;
}

bool OAIDfsSlate::is_slate_roster_slots_Valid() const{
    return m_slate_roster_slots_isValid;
}

bool OAIDfsSlate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dfs_slate_games.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dfs_slate_players.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_multi_day_slate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_games_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_operator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_game_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_slate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_removed_by_operator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_salary_cap_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slate_roster_slots.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDfsSlate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
