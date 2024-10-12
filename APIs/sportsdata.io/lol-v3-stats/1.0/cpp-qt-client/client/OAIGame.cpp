/**
 * LoL v3 Stats
 * LoL v3 Stats
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGame.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGame::OAIGame(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGame::OAIGame() {
    this->initializeModel();
}

OAIGame::~OAIGame() {}

void OAIGame::initializeModel() {

    m_best_of_isSet = false;
    m_best_of_isValid = false;

    m_date_time_isSet = false;
    m_date_time_isValid = false;

    m_day_isSet = false;
    m_day_isValid = false;

    m_draw_money_line_isSet = false;
    m_draw_money_line_isValid = false;

    m_game_id_isSet = false;
    m_game_id_isValid = false;

    m_group_isSet = false;
    m_group_isValid = false;

    m_is_closed_isSet = false;
    m_is_closed_isValid = false;

    m_point_spread_isSet = false;
    m_point_spread_isValid = false;

    m_round_id_isSet = false;
    m_round_id_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_team_aid_isSet = false;
    m_team_aid_isValid = false;

    m_team_a_key_isSet = false;
    m_team_a_key_isValid = false;

    m_team_a_money_line_isSet = false;
    m_team_a_money_line_isValid = false;

    m_team_a_name_isSet = false;
    m_team_a_name_isValid = false;

    m_team_a_point_spread_payout_isSet = false;
    m_team_a_point_spread_payout_isValid = false;

    m_team_a_score_isSet = false;
    m_team_a_score_isValid = false;

    m_team_bid_isSet = false;
    m_team_bid_isValid = false;

    m_team_b_key_isSet = false;
    m_team_b_key_isValid = false;

    m_team_b_money_line_isSet = false;
    m_team_b_money_line_isValid = false;

    m_team_b_name_isSet = false;
    m_team_b_name_isValid = false;

    m_team_b_point_spread_payout_isSet = false;
    m_team_b_point_spread_payout_isValid = false;

    m_team_b_score_isSet = false;
    m_team_b_score_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;

    m_updated_utc_isSet = false;
    m_updated_utc_isValid = false;

    m_venue_id_isSet = false;
    m_venue_id_isValid = false;

    m_venue_type_isSet = false;
    m_venue_type_isValid = false;

    m_week_isSet = false;
    m_week_isValid = false;

    m_winner_isSet = false;
    m_winner_isValid = false;
}

void OAIGame::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGame::fromJsonObject(QJsonObject json) {

    m_best_of_isValid = ::OpenAPI::fromJsonValue(m_best_of, json[QString("BestOf")]);
    m_best_of_isSet = !json[QString("BestOf")].isNull() && m_best_of_isValid;

    m_date_time_isValid = ::OpenAPI::fromJsonValue(m_date_time, json[QString("DateTime")]);
    m_date_time_isSet = !json[QString("DateTime")].isNull() && m_date_time_isValid;

    m_day_isValid = ::OpenAPI::fromJsonValue(m_day, json[QString("Day")]);
    m_day_isSet = !json[QString("Day")].isNull() && m_day_isValid;

    m_draw_money_line_isValid = ::OpenAPI::fromJsonValue(m_draw_money_line, json[QString("DrawMoneyLine")]);
    m_draw_money_line_isSet = !json[QString("DrawMoneyLine")].isNull() && m_draw_money_line_isValid;

    m_game_id_isValid = ::OpenAPI::fromJsonValue(m_game_id, json[QString("GameId")]);
    m_game_id_isSet = !json[QString("GameId")].isNull() && m_game_id_isValid;

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("Group")]);
    m_group_isSet = !json[QString("Group")].isNull() && m_group_isValid;

    m_is_closed_isValid = ::OpenAPI::fromJsonValue(m_is_closed, json[QString("IsClosed")]);
    m_is_closed_isSet = !json[QString("IsClosed")].isNull() && m_is_closed_isValid;

    m_point_spread_isValid = ::OpenAPI::fromJsonValue(m_point_spread, json[QString("PointSpread")]);
    m_point_spread_isSet = !json[QString("PointSpread")].isNull() && m_point_spread_isValid;

    m_round_id_isValid = ::OpenAPI::fromJsonValue(m_round_id, json[QString("RoundId")]);
    m_round_id_isSet = !json[QString("RoundId")].isNull() && m_round_id_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_team_aid_isValid = ::OpenAPI::fromJsonValue(m_team_aid, json[QString("TeamAId")]);
    m_team_aid_isSet = !json[QString("TeamAId")].isNull() && m_team_aid_isValid;

    m_team_a_key_isValid = ::OpenAPI::fromJsonValue(m_team_a_key, json[QString("TeamAKey")]);
    m_team_a_key_isSet = !json[QString("TeamAKey")].isNull() && m_team_a_key_isValid;

    m_team_a_money_line_isValid = ::OpenAPI::fromJsonValue(m_team_a_money_line, json[QString("TeamAMoneyLine")]);
    m_team_a_money_line_isSet = !json[QString("TeamAMoneyLine")].isNull() && m_team_a_money_line_isValid;

    m_team_a_name_isValid = ::OpenAPI::fromJsonValue(m_team_a_name, json[QString("TeamAName")]);
    m_team_a_name_isSet = !json[QString("TeamAName")].isNull() && m_team_a_name_isValid;

    m_team_a_point_spread_payout_isValid = ::OpenAPI::fromJsonValue(m_team_a_point_spread_payout, json[QString("TeamAPointSpreadPayout")]);
    m_team_a_point_spread_payout_isSet = !json[QString("TeamAPointSpreadPayout")].isNull() && m_team_a_point_spread_payout_isValid;

    m_team_a_score_isValid = ::OpenAPI::fromJsonValue(m_team_a_score, json[QString("TeamAScore")]);
    m_team_a_score_isSet = !json[QString("TeamAScore")].isNull() && m_team_a_score_isValid;

    m_team_bid_isValid = ::OpenAPI::fromJsonValue(m_team_bid, json[QString("TeamBId")]);
    m_team_bid_isSet = !json[QString("TeamBId")].isNull() && m_team_bid_isValid;

    m_team_b_key_isValid = ::OpenAPI::fromJsonValue(m_team_b_key, json[QString("TeamBKey")]);
    m_team_b_key_isSet = !json[QString("TeamBKey")].isNull() && m_team_b_key_isValid;

    m_team_b_money_line_isValid = ::OpenAPI::fromJsonValue(m_team_b_money_line, json[QString("TeamBMoneyLine")]);
    m_team_b_money_line_isSet = !json[QString("TeamBMoneyLine")].isNull() && m_team_b_money_line_isValid;

    m_team_b_name_isValid = ::OpenAPI::fromJsonValue(m_team_b_name, json[QString("TeamBName")]);
    m_team_b_name_isSet = !json[QString("TeamBName")].isNull() && m_team_b_name_isValid;

    m_team_b_point_spread_payout_isValid = ::OpenAPI::fromJsonValue(m_team_b_point_spread_payout, json[QString("TeamBPointSpreadPayout")]);
    m_team_b_point_spread_payout_isSet = !json[QString("TeamBPointSpreadPayout")].isNull() && m_team_b_point_spread_payout_isValid;

    m_team_b_score_isValid = ::OpenAPI::fromJsonValue(m_team_b_score, json[QString("TeamBScore")]);
    m_team_b_score_isSet = !json[QString("TeamBScore")].isNull() && m_team_b_score_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;

    m_updated_utc_isValid = ::OpenAPI::fromJsonValue(m_updated_utc, json[QString("UpdatedUtc")]);
    m_updated_utc_isSet = !json[QString("UpdatedUtc")].isNull() && m_updated_utc_isValid;

    m_venue_id_isValid = ::OpenAPI::fromJsonValue(m_venue_id, json[QString("VenueId")]);
    m_venue_id_isSet = !json[QString("VenueId")].isNull() && m_venue_id_isValid;

    m_venue_type_isValid = ::OpenAPI::fromJsonValue(m_venue_type, json[QString("VenueType")]);
    m_venue_type_isSet = !json[QString("VenueType")].isNull() && m_venue_type_isValid;

    m_week_isValid = ::OpenAPI::fromJsonValue(m_week, json[QString("Week")]);
    m_week_isSet = !json[QString("Week")].isNull() && m_week_isValid;

    m_winner_isValid = ::OpenAPI::fromJsonValue(m_winner, json[QString("Winner")]);
    m_winner_isSet = !json[QString("Winner")].isNull() && m_winner_isValid;
}

QString OAIGame::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGame::asJsonObject() const {
    QJsonObject obj;
    if (m_best_of_isSet) {
        obj.insert(QString("BestOf"), ::OpenAPI::toJsonValue(m_best_of));
    }
    if (m_date_time_isSet) {
        obj.insert(QString("DateTime"), ::OpenAPI::toJsonValue(m_date_time));
    }
    if (m_day_isSet) {
        obj.insert(QString("Day"), ::OpenAPI::toJsonValue(m_day));
    }
    if (m_draw_money_line_isSet) {
        obj.insert(QString("DrawMoneyLine"), ::OpenAPI::toJsonValue(m_draw_money_line));
    }
    if (m_game_id_isSet) {
        obj.insert(QString("GameId"), ::OpenAPI::toJsonValue(m_game_id));
    }
    if (m_group_isSet) {
        obj.insert(QString("Group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_is_closed_isSet) {
        obj.insert(QString("IsClosed"), ::OpenAPI::toJsonValue(m_is_closed));
    }
    if (m_point_spread_isSet) {
        obj.insert(QString("PointSpread"), ::OpenAPI::toJsonValue(m_point_spread));
    }
    if (m_round_id_isSet) {
        obj.insert(QString("RoundId"), ::OpenAPI::toJsonValue(m_round_id));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_team_aid_isSet) {
        obj.insert(QString("TeamAId"), ::OpenAPI::toJsonValue(m_team_aid));
    }
    if (m_team_a_key_isSet) {
        obj.insert(QString("TeamAKey"), ::OpenAPI::toJsonValue(m_team_a_key));
    }
    if (m_team_a_money_line_isSet) {
        obj.insert(QString("TeamAMoneyLine"), ::OpenAPI::toJsonValue(m_team_a_money_line));
    }
    if (m_team_a_name_isSet) {
        obj.insert(QString("TeamAName"), ::OpenAPI::toJsonValue(m_team_a_name));
    }
    if (m_team_a_point_spread_payout_isSet) {
        obj.insert(QString("TeamAPointSpreadPayout"), ::OpenAPI::toJsonValue(m_team_a_point_spread_payout));
    }
    if (m_team_a_score_isSet) {
        obj.insert(QString("TeamAScore"), ::OpenAPI::toJsonValue(m_team_a_score));
    }
    if (m_team_bid_isSet) {
        obj.insert(QString("TeamBId"), ::OpenAPI::toJsonValue(m_team_bid));
    }
    if (m_team_b_key_isSet) {
        obj.insert(QString("TeamBKey"), ::OpenAPI::toJsonValue(m_team_b_key));
    }
    if (m_team_b_money_line_isSet) {
        obj.insert(QString("TeamBMoneyLine"), ::OpenAPI::toJsonValue(m_team_b_money_line));
    }
    if (m_team_b_name_isSet) {
        obj.insert(QString("TeamBName"), ::OpenAPI::toJsonValue(m_team_b_name));
    }
    if (m_team_b_point_spread_payout_isSet) {
        obj.insert(QString("TeamBPointSpreadPayout"), ::OpenAPI::toJsonValue(m_team_b_point_spread_payout));
    }
    if (m_team_b_score_isSet) {
        obj.insert(QString("TeamBScore"), ::OpenAPI::toJsonValue(m_team_b_score));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    if (m_updated_utc_isSet) {
        obj.insert(QString("UpdatedUtc"), ::OpenAPI::toJsonValue(m_updated_utc));
    }
    if (m_venue_id_isSet) {
        obj.insert(QString("VenueId"), ::OpenAPI::toJsonValue(m_venue_id));
    }
    if (m_venue_type_isSet) {
        obj.insert(QString("VenueType"), ::OpenAPI::toJsonValue(m_venue_type));
    }
    if (m_week_isSet) {
        obj.insert(QString("Week"), ::OpenAPI::toJsonValue(m_week));
    }
    if (m_winner_isSet) {
        obj.insert(QString("Winner"), ::OpenAPI::toJsonValue(m_winner));
    }
    return obj;
}

QString OAIGame::getBestOf() const {
    return m_best_of;
}
void OAIGame::setBestOf(const QString &best_of) {
    m_best_of = best_of;
    m_best_of_isSet = true;
}

bool OAIGame::is_best_of_Set() const{
    return m_best_of_isSet;
}

bool OAIGame::is_best_of_Valid() const{
    return m_best_of_isValid;
}

QString OAIGame::getDateTime() const {
    return m_date_time;
}
void OAIGame::setDateTime(const QString &date_time) {
    m_date_time = date_time;
    m_date_time_isSet = true;
}

bool OAIGame::is_date_time_Set() const{
    return m_date_time_isSet;
}

bool OAIGame::is_date_time_Valid() const{
    return m_date_time_isValid;
}

QString OAIGame::getDay() const {
    return m_day;
}
void OAIGame::setDay(const QString &day) {
    m_day = day;
    m_day_isSet = true;
}

bool OAIGame::is_day_Set() const{
    return m_day_isSet;
}

bool OAIGame::is_day_Valid() const{
    return m_day_isValid;
}

qint32 OAIGame::getDrawMoneyLine() const {
    return m_draw_money_line;
}
void OAIGame::setDrawMoneyLine(const qint32 &draw_money_line) {
    m_draw_money_line = draw_money_line;
    m_draw_money_line_isSet = true;
}

bool OAIGame::is_draw_money_line_Set() const{
    return m_draw_money_line_isSet;
}

bool OAIGame::is_draw_money_line_Valid() const{
    return m_draw_money_line_isValid;
}

qint32 OAIGame::getGameId() const {
    return m_game_id;
}
void OAIGame::setGameId(const qint32 &game_id) {
    m_game_id = game_id;
    m_game_id_isSet = true;
}

bool OAIGame::is_game_id_Set() const{
    return m_game_id_isSet;
}

bool OAIGame::is_game_id_Valid() const{
    return m_game_id_isValid;
}

QString OAIGame::getGroup() const {
    return m_group;
}
void OAIGame::setGroup(const QString &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAIGame::is_group_Set() const{
    return m_group_isSet;
}

bool OAIGame::is_group_Valid() const{
    return m_group_isValid;
}

bool OAIGame::isIsClosed() const {
    return m_is_closed;
}
void OAIGame::setIsClosed(const bool &is_closed) {
    m_is_closed = is_closed;
    m_is_closed_isSet = true;
}

bool OAIGame::is_is_closed_Set() const{
    return m_is_closed_isSet;
}

bool OAIGame::is_is_closed_Valid() const{
    return m_is_closed_isValid;
}

double OAIGame::getPointSpread() const {
    return m_point_spread;
}
void OAIGame::setPointSpread(const double &point_spread) {
    m_point_spread = point_spread;
    m_point_spread_isSet = true;
}

bool OAIGame::is_point_spread_Set() const{
    return m_point_spread_isSet;
}

bool OAIGame::is_point_spread_Valid() const{
    return m_point_spread_isValid;
}

qint32 OAIGame::getRoundId() const {
    return m_round_id;
}
void OAIGame::setRoundId(const qint32 &round_id) {
    m_round_id = round_id;
    m_round_id_isSet = true;
}

bool OAIGame::is_round_id_Set() const{
    return m_round_id_isSet;
}

bool OAIGame::is_round_id_Valid() const{
    return m_round_id_isValid;
}

qint32 OAIGame::getSeason() const {
    return m_season;
}
void OAIGame::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIGame::is_season_Set() const{
    return m_season_isSet;
}

bool OAIGame::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAIGame::getSeasonType() const {
    return m_season_type;
}
void OAIGame::setSeasonType(const qint32 &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAIGame::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAIGame::is_season_type_Valid() const{
    return m_season_type_isValid;
}

QString OAIGame::getStatus() const {
    return m_status;
}
void OAIGame::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIGame::is_status_Set() const{
    return m_status_isSet;
}

bool OAIGame::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIGame::getTeamAid() const {
    return m_team_aid;
}
void OAIGame::setTeamAid(const qint32 &team_aid) {
    m_team_aid = team_aid;
    m_team_aid_isSet = true;
}

bool OAIGame::is_team_aid_Set() const{
    return m_team_aid_isSet;
}

bool OAIGame::is_team_aid_Valid() const{
    return m_team_aid_isValid;
}

QString OAIGame::getTeamAKey() const {
    return m_team_a_key;
}
void OAIGame::setTeamAKey(const QString &team_a_key) {
    m_team_a_key = team_a_key;
    m_team_a_key_isSet = true;
}

bool OAIGame::is_team_a_key_Set() const{
    return m_team_a_key_isSet;
}

bool OAIGame::is_team_a_key_Valid() const{
    return m_team_a_key_isValid;
}

qint32 OAIGame::getTeamAMoneyLine() const {
    return m_team_a_money_line;
}
void OAIGame::setTeamAMoneyLine(const qint32 &team_a_money_line) {
    m_team_a_money_line = team_a_money_line;
    m_team_a_money_line_isSet = true;
}

bool OAIGame::is_team_a_money_line_Set() const{
    return m_team_a_money_line_isSet;
}

bool OAIGame::is_team_a_money_line_Valid() const{
    return m_team_a_money_line_isValid;
}

QString OAIGame::getTeamAName() const {
    return m_team_a_name;
}
void OAIGame::setTeamAName(const QString &team_a_name) {
    m_team_a_name = team_a_name;
    m_team_a_name_isSet = true;
}

bool OAIGame::is_team_a_name_Set() const{
    return m_team_a_name_isSet;
}

bool OAIGame::is_team_a_name_Valid() const{
    return m_team_a_name_isValid;
}

qint32 OAIGame::getTeamAPointSpreadPayout() const {
    return m_team_a_point_spread_payout;
}
void OAIGame::setTeamAPointSpreadPayout(const qint32 &team_a_point_spread_payout) {
    m_team_a_point_spread_payout = team_a_point_spread_payout;
    m_team_a_point_spread_payout_isSet = true;
}

bool OAIGame::is_team_a_point_spread_payout_Set() const{
    return m_team_a_point_spread_payout_isSet;
}

bool OAIGame::is_team_a_point_spread_payout_Valid() const{
    return m_team_a_point_spread_payout_isValid;
}

qint32 OAIGame::getTeamAScore() const {
    return m_team_a_score;
}
void OAIGame::setTeamAScore(const qint32 &team_a_score) {
    m_team_a_score = team_a_score;
    m_team_a_score_isSet = true;
}

bool OAIGame::is_team_a_score_Set() const{
    return m_team_a_score_isSet;
}

bool OAIGame::is_team_a_score_Valid() const{
    return m_team_a_score_isValid;
}

qint32 OAIGame::getTeamBid() const {
    return m_team_bid;
}
void OAIGame::setTeamBid(const qint32 &team_bid) {
    m_team_bid = team_bid;
    m_team_bid_isSet = true;
}

bool OAIGame::is_team_bid_Set() const{
    return m_team_bid_isSet;
}

bool OAIGame::is_team_bid_Valid() const{
    return m_team_bid_isValid;
}

QString OAIGame::getTeamBKey() const {
    return m_team_b_key;
}
void OAIGame::setTeamBKey(const QString &team_b_key) {
    m_team_b_key = team_b_key;
    m_team_b_key_isSet = true;
}

bool OAIGame::is_team_b_key_Set() const{
    return m_team_b_key_isSet;
}

bool OAIGame::is_team_b_key_Valid() const{
    return m_team_b_key_isValid;
}

qint32 OAIGame::getTeamBMoneyLine() const {
    return m_team_b_money_line;
}
void OAIGame::setTeamBMoneyLine(const qint32 &team_b_money_line) {
    m_team_b_money_line = team_b_money_line;
    m_team_b_money_line_isSet = true;
}

bool OAIGame::is_team_b_money_line_Set() const{
    return m_team_b_money_line_isSet;
}

bool OAIGame::is_team_b_money_line_Valid() const{
    return m_team_b_money_line_isValid;
}

QString OAIGame::getTeamBName() const {
    return m_team_b_name;
}
void OAIGame::setTeamBName(const QString &team_b_name) {
    m_team_b_name = team_b_name;
    m_team_b_name_isSet = true;
}

bool OAIGame::is_team_b_name_Set() const{
    return m_team_b_name_isSet;
}

bool OAIGame::is_team_b_name_Valid() const{
    return m_team_b_name_isValid;
}

qint32 OAIGame::getTeamBPointSpreadPayout() const {
    return m_team_b_point_spread_payout;
}
void OAIGame::setTeamBPointSpreadPayout(const qint32 &team_b_point_spread_payout) {
    m_team_b_point_spread_payout = team_b_point_spread_payout;
    m_team_b_point_spread_payout_isSet = true;
}

bool OAIGame::is_team_b_point_spread_payout_Set() const{
    return m_team_b_point_spread_payout_isSet;
}

bool OAIGame::is_team_b_point_spread_payout_Valid() const{
    return m_team_b_point_spread_payout_isValid;
}

qint32 OAIGame::getTeamBScore() const {
    return m_team_b_score;
}
void OAIGame::setTeamBScore(const qint32 &team_b_score) {
    m_team_b_score = team_b_score;
    m_team_b_score_isSet = true;
}

bool OAIGame::is_team_b_score_Set() const{
    return m_team_b_score_isSet;
}

bool OAIGame::is_team_b_score_Valid() const{
    return m_team_b_score_isValid;
}

QString OAIGame::getUpdated() const {
    return m_updated;
}
void OAIGame::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIGame::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIGame::is_updated_Valid() const{
    return m_updated_isValid;
}

QString OAIGame::getUpdatedUtc() const {
    return m_updated_utc;
}
void OAIGame::setUpdatedUtc(const QString &updated_utc) {
    m_updated_utc = updated_utc;
    m_updated_utc_isSet = true;
}

bool OAIGame::is_updated_utc_Set() const{
    return m_updated_utc_isSet;
}

bool OAIGame::is_updated_utc_Valid() const{
    return m_updated_utc_isValid;
}

qint32 OAIGame::getVenueId() const {
    return m_venue_id;
}
void OAIGame::setVenueId(const qint32 &venue_id) {
    m_venue_id = venue_id;
    m_venue_id_isSet = true;
}

bool OAIGame::is_venue_id_Set() const{
    return m_venue_id_isSet;
}

bool OAIGame::is_venue_id_Valid() const{
    return m_venue_id_isValid;
}

QString OAIGame::getVenueType() const {
    return m_venue_type;
}
void OAIGame::setVenueType(const QString &venue_type) {
    m_venue_type = venue_type;
    m_venue_type_isSet = true;
}

bool OAIGame::is_venue_type_Set() const{
    return m_venue_type_isSet;
}

bool OAIGame::is_venue_type_Valid() const{
    return m_venue_type_isValid;
}

qint32 OAIGame::getWeek() const {
    return m_week;
}
void OAIGame::setWeek(const qint32 &week) {
    m_week = week;
    m_week_isSet = true;
}

bool OAIGame::is_week_Set() const{
    return m_week_isSet;
}

bool OAIGame::is_week_Valid() const{
    return m_week_isValid;
}

QString OAIGame::getWinner() const {
    return m_winner;
}
void OAIGame::setWinner(const QString &winner) {
    m_winner = winner;
    m_winner_isSet = true;
}

bool OAIGame::is_winner_Set() const{
    return m_winner_isSet;
}

bool OAIGame::is_winner_Valid() const{
    return m_winner_isValid;
}

bool OAIGame::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_best_of_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_draw_money_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_closed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_point_spread_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_round_id_isSet) {
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

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_aid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_a_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_a_money_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_a_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_a_point_spread_payout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_a_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_bid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_b_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_b_money_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_b_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_b_point_spread_payout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_b_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_utc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_venue_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_venue_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_week_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGame::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
