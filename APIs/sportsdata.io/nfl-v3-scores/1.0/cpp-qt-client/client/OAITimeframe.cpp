/**
 * NFL v3 Scores
 * NFL schedules, scores, odds, weather, and news API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITimeframe.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITimeframe::OAITimeframe(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITimeframe::OAITimeframe() {
    this->initializeModel();
}

OAITimeframe::~OAITimeframe() {}

void OAITimeframe::initializeModel() {

    m_api_season_isSet = false;
    m_api_season_isValid = false;

    m_api_week_isSet = false;
    m_api_week_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_first_game_end_isSet = false;
    m_first_game_end_isValid = false;

    m_first_game_start_isSet = false;
    m_first_game_start_isValid = false;

    m_has_ended_isSet = false;
    m_has_ended_isValid = false;

    m_has_first_game_ended_isSet = false;
    m_has_first_game_ended_isValid = false;

    m_has_first_game_started_isSet = false;
    m_has_first_game_started_isValid = false;

    m_has_games_isSet = false;
    m_has_games_isValid = false;

    m_has_last_game_ended_isSet = false;
    m_has_last_game_ended_isValid = false;

    m_has_started_isSet = false;
    m_has_started_isValid = false;

    m_last_game_end_isSet = false;
    m_last_game_end_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;

    m_short_name_isSet = false;
    m_short_name_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_week_isSet = false;
    m_week_isValid = false;
}

void OAITimeframe::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITimeframe::fromJsonObject(QJsonObject json) {

    m_api_season_isValid = ::OpenAPI::fromJsonValue(m_api_season, json[QString("ApiSeason")]);
    m_api_season_isSet = !json[QString("ApiSeason")].isNull() && m_api_season_isValid;

    m_api_week_isValid = ::OpenAPI::fromJsonValue(m_api_week, json[QString("ApiWeek")]);
    m_api_week_isSet = !json[QString("ApiWeek")].isNull() && m_api_week_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("EndDate")]);
    m_end_date_isSet = !json[QString("EndDate")].isNull() && m_end_date_isValid;

    m_first_game_end_isValid = ::OpenAPI::fromJsonValue(m_first_game_end, json[QString("FirstGameEnd")]);
    m_first_game_end_isSet = !json[QString("FirstGameEnd")].isNull() && m_first_game_end_isValid;

    m_first_game_start_isValid = ::OpenAPI::fromJsonValue(m_first_game_start, json[QString("FirstGameStart")]);
    m_first_game_start_isSet = !json[QString("FirstGameStart")].isNull() && m_first_game_start_isValid;

    m_has_ended_isValid = ::OpenAPI::fromJsonValue(m_has_ended, json[QString("HasEnded")]);
    m_has_ended_isSet = !json[QString("HasEnded")].isNull() && m_has_ended_isValid;

    m_has_first_game_ended_isValid = ::OpenAPI::fromJsonValue(m_has_first_game_ended, json[QString("HasFirstGameEnded")]);
    m_has_first_game_ended_isSet = !json[QString("HasFirstGameEnded")].isNull() && m_has_first_game_ended_isValid;

    m_has_first_game_started_isValid = ::OpenAPI::fromJsonValue(m_has_first_game_started, json[QString("HasFirstGameStarted")]);
    m_has_first_game_started_isSet = !json[QString("HasFirstGameStarted")].isNull() && m_has_first_game_started_isValid;

    m_has_games_isValid = ::OpenAPI::fromJsonValue(m_has_games, json[QString("HasGames")]);
    m_has_games_isSet = !json[QString("HasGames")].isNull() && m_has_games_isValid;

    m_has_last_game_ended_isValid = ::OpenAPI::fromJsonValue(m_has_last_game_ended, json[QString("HasLastGameEnded")]);
    m_has_last_game_ended_isSet = !json[QString("HasLastGameEnded")].isNull() && m_has_last_game_ended_isValid;

    m_has_started_isValid = ::OpenAPI::fromJsonValue(m_has_started, json[QString("HasStarted")]);
    m_has_started_isSet = !json[QString("HasStarted")].isNull() && m_has_started_isValid;

    m_last_game_end_isValid = ::OpenAPI::fromJsonValue(m_last_game_end, json[QString("LastGameEnd")]);
    m_last_game_end_isSet = !json[QString("LastGameEnd")].isNull() && m_last_game_end_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;

    m_short_name_isValid = ::OpenAPI::fromJsonValue(m_short_name, json[QString("ShortName")]);
    m_short_name_isSet = !json[QString("ShortName")].isNull() && m_short_name_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("StartDate")]);
    m_start_date_isSet = !json[QString("StartDate")].isNull() && m_start_date_isValid;

    m_week_isValid = ::OpenAPI::fromJsonValue(m_week, json[QString("Week")]);
    m_week_isSet = !json[QString("Week")].isNull() && m_week_isValid;
}

QString OAITimeframe::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITimeframe::asJsonObject() const {
    QJsonObject obj;
    if (m_api_season_isSet) {
        obj.insert(QString("ApiSeason"), ::OpenAPI::toJsonValue(m_api_season));
    }
    if (m_api_week_isSet) {
        obj.insert(QString("ApiWeek"), ::OpenAPI::toJsonValue(m_api_week));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("EndDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_first_game_end_isSet) {
        obj.insert(QString("FirstGameEnd"), ::OpenAPI::toJsonValue(m_first_game_end));
    }
    if (m_first_game_start_isSet) {
        obj.insert(QString("FirstGameStart"), ::OpenAPI::toJsonValue(m_first_game_start));
    }
    if (m_has_ended_isSet) {
        obj.insert(QString("HasEnded"), ::OpenAPI::toJsonValue(m_has_ended));
    }
    if (m_has_first_game_ended_isSet) {
        obj.insert(QString("HasFirstGameEnded"), ::OpenAPI::toJsonValue(m_has_first_game_ended));
    }
    if (m_has_first_game_started_isSet) {
        obj.insert(QString("HasFirstGameStarted"), ::OpenAPI::toJsonValue(m_has_first_game_started));
    }
    if (m_has_games_isSet) {
        obj.insert(QString("HasGames"), ::OpenAPI::toJsonValue(m_has_games));
    }
    if (m_has_last_game_ended_isSet) {
        obj.insert(QString("HasLastGameEnded"), ::OpenAPI::toJsonValue(m_has_last_game_ended));
    }
    if (m_has_started_isSet) {
        obj.insert(QString("HasStarted"), ::OpenAPI::toJsonValue(m_has_started));
    }
    if (m_last_game_end_isSet) {
        obj.insert(QString("LastGameEnd"), ::OpenAPI::toJsonValue(m_last_game_end));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    if (m_short_name_isSet) {
        obj.insert(QString("ShortName"), ::OpenAPI::toJsonValue(m_short_name));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("StartDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_week_isSet) {
        obj.insert(QString("Week"), ::OpenAPI::toJsonValue(m_week));
    }
    return obj;
}

QString OAITimeframe::getApiSeason() const {
    return m_api_season;
}
void OAITimeframe::setApiSeason(const QString &api_season) {
    m_api_season = api_season;
    m_api_season_isSet = true;
}

bool OAITimeframe::is_api_season_Set() const{
    return m_api_season_isSet;
}

bool OAITimeframe::is_api_season_Valid() const{
    return m_api_season_isValid;
}

QString OAITimeframe::getApiWeek() const {
    return m_api_week;
}
void OAITimeframe::setApiWeek(const QString &api_week) {
    m_api_week = api_week;
    m_api_week_isSet = true;
}

bool OAITimeframe::is_api_week_Set() const{
    return m_api_week_isSet;
}

bool OAITimeframe::is_api_week_Valid() const{
    return m_api_week_isValid;
}

QString OAITimeframe::getEndDate() const {
    return m_end_date;
}
void OAITimeframe::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAITimeframe::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAITimeframe::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAITimeframe::getFirstGameEnd() const {
    return m_first_game_end;
}
void OAITimeframe::setFirstGameEnd(const QString &first_game_end) {
    m_first_game_end = first_game_end;
    m_first_game_end_isSet = true;
}

bool OAITimeframe::is_first_game_end_Set() const{
    return m_first_game_end_isSet;
}

bool OAITimeframe::is_first_game_end_Valid() const{
    return m_first_game_end_isValid;
}

QString OAITimeframe::getFirstGameStart() const {
    return m_first_game_start;
}
void OAITimeframe::setFirstGameStart(const QString &first_game_start) {
    m_first_game_start = first_game_start;
    m_first_game_start_isSet = true;
}

bool OAITimeframe::is_first_game_start_Set() const{
    return m_first_game_start_isSet;
}

bool OAITimeframe::is_first_game_start_Valid() const{
    return m_first_game_start_isValid;
}

bool OAITimeframe::isHasEnded() const {
    return m_has_ended;
}
void OAITimeframe::setHasEnded(const bool &has_ended) {
    m_has_ended = has_ended;
    m_has_ended_isSet = true;
}

bool OAITimeframe::is_has_ended_Set() const{
    return m_has_ended_isSet;
}

bool OAITimeframe::is_has_ended_Valid() const{
    return m_has_ended_isValid;
}

bool OAITimeframe::isHasFirstGameEnded() const {
    return m_has_first_game_ended;
}
void OAITimeframe::setHasFirstGameEnded(const bool &has_first_game_ended) {
    m_has_first_game_ended = has_first_game_ended;
    m_has_first_game_ended_isSet = true;
}

bool OAITimeframe::is_has_first_game_ended_Set() const{
    return m_has_first_game_ended_isSet;
}

bool OAITimeframe::is_has_first_game_ended_Valid() const{
    return m_has_first_game_ended_isValid;
}

bool OAITimeframe::isHasFirstGameStarted() const {
    return m_has_first_game_started;
}
void OAITimeframe::setHasFirstGameStarted(const bool &has_first_game_started) {
    m_has_first_game_started = has_first_game_started;
    m_has_first_game_started_isSet = true;
}

bool OAITimeframe::is_has_first_game_started_Set() const{
    return m_has_first_game_started_isSet;
}

bool OAITimeframe::is_has_first_game_started_Valid() const{
    return m_has_first_game_started_isValid;
}

bool OAITimeframe::isHasGames() const {
    return m_has_games;
}
void OAITimeframe::setHasGames(const bool &has_games) {
    m_has_games = has_games;
    m_has_games_isSet = true;
}

bool OAITimeframe::is_has_games_Set() const{
    return m_has_games_isSet;
}

bool OAITimeframe::is_has_games_Valid() const{
    return m_has_games_isValid;
}

bool OAITimeframe::isHasLastGameEnded() const {
    return m_has_last_game_ended;
}
void OAITimeframe::setHasLastGameEnded(const bool &has_last_game_ended) {
    m_has_last_game_ended = has_last_game_ended;
    m_has_last_game_ended_isSet = true;
}

bool OAITimeframe::is_has_last_game_ended_Set() const{
    return m_has_last_game_ended_isSet;
}

bool OAITimeframe::is_has_last_game_ended_Valid() const{
    return m_has_last_game_ended_isValid;
}

bool OAITimeframe::isHasStarted() const {
    return m_has_started;
}
void OAITimeframe::setHasStarted(const bool &has_started) {
    m_has_started = has_started;
    m_has_started_isSet = true;
}

bool OAITimeframe::is_has_started_Set() const{
    return m_has_started_isSet;
}

bool OAITimeframe::is_has_started_Valid() const{
    return m_has_started_isValid;
}

QString OAITimeframe::getLastGameEnd() const {
    return m_last_game_end;
}
void OAITimeframe::setLastGameEnd(const QString &last_game_end) {
    m_last_game_end = last_game_end;
    m_last_game_end_isSet = true;
}

bool OAITimeframe::is_last_game_end_Set() const{
    return m_last_game_end_isSet;
}

bool OAITimeframe::is_last_game_end_Valid() const{
    return m_last_game_end_isValid;
}

QString OAITimeframe::getName() const {
    return m_name;
}
void OAITimeframe::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITimeframe::is_name_Set() const{
    return m_name_isSet;
}

bool OAITimeframe::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAITimeframe::getSeason() const {
    return m_season;
}
void OAITimeframe::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAITimeframe::is_season_Set() const{
    return m_season_isSet;
}

bool OAITimeframe::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAITimeframe::getSeasonType() const {
    return m_season_type;
}
void OAITimeframe::setSeasonType(const qint32 &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAITimeframe::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAITimeframe::is_season_type_Valid() const{
    return m_season_type_isValid;
}

QString OAITimeframe::getShortName() const {
    return m_short_name;
}
void OAITimeframe::setShortName(const QString &short_name) {
    m_short_name = short_name;
    m_short_name_isSet = true;
}

bool OAITimeframe::is_short_name_Set() const{
    return m_short_name_isSet;
}

bool OAITimeframe::is_short_name_Valid() const{
    return m_short_name_isValid;
}

QString OAITimeframe::getStartDate() const {
    return m_start_date;
}
void OAITimeframe::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAITimeframe::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAITimeframe::is_start_date_Valid() const{
    return m_start_date_isValid;
}

qint32 OAITimeframe::getWeek() const {
    return m_week;
}
void OAITimeframe::setWeek(const qint32 &week) {
    m_week = week;
    m_week_isSet = true;
}

bool OAITimeframe::is_week_Set() const{
    return m_week_isSet;
}

bool OAITimeframe::is_week_Valid() const{
    return m_week_isValid;
}

bool OAITimeframe::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_api_week_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_game_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_game_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_ended_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_first_game_ended_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_first_game_started_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_games_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_last_game_ended_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_started_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_game_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_week_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITimeframe::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
