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

#include "OAIStanding.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStanding::OAIStanding(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStanding::OAIStanding() {
    this->initializeModel();
}

OAIStanding::~OAIStanding() {}

void OAIStanding::initializeModel() {

    m_conference_isSet = false;
    m_conference_isValid = false;

    m_conference_losses_isSet = false;
    m_conference_losses_isValid = false;

    m_conference_rank_isSet = false;
    m_conference_rank_isValid = false;

    m_conference_ties_isSet = false;
    m_conference_ties_isValid = false;

    m_conference_wins_isSet = false;
    m_conference_wins_isValid = false;

    m_division_isSet = false;
    m_division_isValid = false;

    m_division_losses_isSet = false;
    m_division_losses_isValid = false;

    m_division_rank_isSet = false;
    m_division_rank_isValid = false;

    m_division_ties_isSet = false;
    m_division_ties_isValid = false;

    m_division_wins_isSet = false;
    m_division_wins_isValid = false;

    m_global_team_id_isSet = false;
    m_global_team_id_isValid = false;

    m_losses_isSet = false;
    m_losses_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_net_points_isSet = false;
    m_net_points_isValid = false;

    m_percentage_isSet = false;
    m_percentage_isValid = false;

    m_points_against_isSet = false;
    m_points_against_isValid = false;

    m_points_for_isSet = false;
    m_points_for_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_ties_isSet = false;
    m_ties_isValid = false;

    m_touchdowns_isSet = false;
    m_touchdowns_isValid = false;

    m_wins_isSet = false;
    m_wins_isValid = false;
}

void OAIStanding::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStanding::fromJsonObject(QJsonObject json) {

    m_conference_isValid = ::OpenAPI::fromJsonValue(m_conference, json[QString("Conference")]);
    m_conference_isSet = !json[QString("Conference")].isNull() && m_conference_isValid;

    m_conference_losses_isValid = ::OpenAPI::fromJsonValue(m_conference_losses, json[QString("ConferenceLosses")]);
    m_conference_losses_isSet = !json[QString("ConferenceLosses")].isNull() && m_conference_losses_isValid;

    m_conference_rank_isValid = ::OpenAPI::fromJsonValue(m_conference_rank, json[QString("ConferenceRank")]);
    m_conference_rank_isSet = !json[QString("ConferenceRank")].isNull() && m_conference_rank_isValid;

    m_conference_ties_isValid = ::OpenAPI::fromJsonValue(m_conference_ties, json[QString("ConferenceTies")]);
    m_conference_ties_isSet = !json[QString("ConferenceTies")].isNull() && m_conference_ties_isValid;

    m_conference_wins_isValid = ::OpenAPI::fromJsonValue(m_conference_wins, json[QString("ConferenceWins")]);
    m_conference_wins_isSet = !json[QString("ConferenceWins")].isNull() && m_conference_wins_isValid;

    m_division_isValid = ::OpenAPI::fromJsonValue(m_division, json[QString("Division")]);
    m_division_isSet = !json[QString("Division")].isNull() && m_division_isValid;

    m_division_losses_isValid = ::OpenAPI::fromJsonValue(m_division_losses, json[QString("DivisionLosses")]);
    m_division_losses_isSet = !json[QString("DivisionLosses")].isNull() && m_division_losses_isValid;

    m_division_rank_isValid = ::OpenAPI::fromJsonValue(m_division_rank, json[QString("DivisionRank")]);
    m_division_rank_isSet = !json[QString("DivisionRank")].isNull() && m_division_rank_isValid;

    m_division_ties_isValid = ::OpenAPI::fromJsonValue(m_division_ties, json[QString("DivisionTies")]);
    m_division_ties_isSet = !json[QString("DivisionTies")].isNull() && m_division_ties_isValid;

    m_division_wins_isValid = ::OpenAPI::fromJsonValue(m_division_wins, json[QString("DivisionWins")]);
    m_division_wins_isSet = !json[QString("DivisionWins")].isNull() && m_division_wins_isValid;

    m_global_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_team_id, json[QString("GlobalTeamID")]);
    m_global_team_id_isSet = !json[QString("GlobalTeamID")].isNull() && m_global_team_id_isValid;

    m_losses_isValid = ::OpenAPI::fromJsonValue(m_losses, json[QString("Losses")]);
    m_losses_isSet = !json[QString("Losses")].isNull() && m_losses_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_net_points_isValid = ::OpenAPI::fromJsonValue(m_net_points, json[QString("NetPoints")]);
    m_net_points_isSet = !json[QString("NetPoints")].isNull() && m_net_points_isValid;

    m_percentage_isValid = ::OpenAPI::fromJsonValue(m_percentage, json[QString("Percentage")]);
    m_percentage_isSet = !json[QString("Percentage")].isNull() && m_percentage_isValid;

    m_points_against_isValid = ::OpenAPI::fromJsonValue(m_points_against, json[QString("PointsAgainst")]);
    m_points_against_isSet = !json[QString("PointsAgainst")].isNull() && m_points_against_isValid;

    m_points_for_isValid = ::OpenAPI::fromJsonValue(m_points_for, json[QString("PointsFor")]);
    m_points_for_isSet = !json[QString("PointsFor")].isNull() && m_points_for_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;

    m_ties_isValid = ::OpenAPI::fromJsonValue(m_ties, json[QString("Ties")]);
    m_ties_isSet = !json[QString("Ties")].isNull() && m_ties_isValid;

    m_touchdowns_isValid = ::OpenAPI::fromJsonValue(m_touchdowns, json[QString("Touchdowns")]);
    m_touchdowns_isSet = !json[QString("Touchdowns")].isNull() && m_touchdowns_isValid;

    m_wins_isValid = ::OpenAPI::fromJsonValue(m_wins, json[QString("Wins")]);
    m_wins_isSet = !json[QString("Wins")].isNull() && m_wins_isValid;
}

QString OAIStanding::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStanding::asJsonObject() const {
    QJsonObject obj;
    if (m_conference_isSet) {
        obj.insert(QString("Conference"), ::OpenAPI::toJsonValue(m_conference));
    }
    if (m_conference_losses_isSet) {
        obj.insert(QString("ConferenceLosses"), ::OpenAPI::toJsonValue(m_conference_losses));
    }
    if (m_conference_rank_isSet) {
        obj.insert(QString("ConferenceRank"), ::OpenAPI::toJsonValue(m_conference_rank));
    }
    if (m_conference_ties_isSet) {
        obj.insert(QString("ConferenceTies"), ::OpenAPI::toJsonValue(m_conference_ties));
    }
    if (m_conference_wins_isSet) {
        obj.insert(QString("ConferenceWins"), ::OpenAPI::toJsonValue(m_conference_wins));
    }
    if (m_division_isSet) {
        obj.insert(QString("Division"), ::OpenAPI::toJsonValue(m_division));
    }
    if (m_division_losses_isSet) {
        obj.insert(QString("DivisionLosses"), ::OpenAPI::toJsonValue(m_division_losses));
    }
    if (m_division_rank_isSet) {
        obj.insert(QString("DivisionRank"), ::OpenAPI::toJsonValue(m_division_rank));
    }
    if (m_division_ties_isSet) {
        obj.insert(QString("DivisionTies"), ::OpenAPI::toJsonValue(m_division_ties));
    }
    if (m_division_wins_isSet) {
        obj.insert(QString("DivisionWins"), ::OpenAPI::toJsonValue(m_division_wins));
    }
    if (m_global_team_id_isSet) {
        obj.insert(QString("GlobalTeamID"), ::OpenAPI::toJsonValue(m_global_team_id));
    }
    if (m_losses_isSet) {
        obj.insert(QString("Losses"), ::OpenAPI::toJsonValue(m_losses));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_net_points_isSet) {
        obj.insert(QString("NetPoints"), ::OpenAPI::toJsonValue(m_net_points));
    }
    if (m_percentage_isSet) {
        obj.insert(QString("Percentage"), ::OpenAPI::toJsonValue(m_percentage));
    }
    if (m_points_against_isSet) {
        obj.insert(QString("PointsAgainst"), ::OpenAPI::toJsonValue(m_points_against));
    }
    if (m_points_for_isSet) {
        obj.insert(QString("PointsFor"), ::OpenAPI::toJsonValue(m_points_for));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_ties_isSet) {
        obj.insert(QString("Ties"), ::OpenAPI::toJsonValue(m_ties));
    }
    if (m_touchdowns_isSet) {
        obj.insert(QString("Touchdowns"), ::OpenAPI::toJsonValue(m_touchdowns));
    }
    if (m_wins_isSet) {
        obj.insert(QString("Wins"), ::OpenAPI::toJsonValue(m_wins));
    }
    return obj;
}

QString OAIStanding::getConference() const {
    return m_conference;
}
void OAIStanding::setConference(const QString &conference) {
    m_conference = conference;
    m_conference_isSet = true;
}

bool OAIStanding::is_conference_Set() const{
    return m_conference_isSet;
}

bool OAIStanding::is_conference_Valid() const{
    return m_conference_isValid;
}

qint32 OAIStanding::getConferenceLosses() const {
    return m_conference_losses;
}
void OAIStanding::setConferenceLosses(const qint32 &conference_losses) {
    m_conference_losses = conference_losses;
    m_conference_losses_isSet = true;
}

bool OAIStanding::is_conference_losses_Set() const{
    return m_conference_losses_isSet;
}

bool OAIStanding::is_conference_losses_Valid() const{
    return m_conference_losses_isValid;
}

qint32 OAIStanding::getConferenceRank() const {
    return m_conference_rank;
}
void OAIStanding::setConferenceRank(const qint32 &conference_rank) {
    m_conference_rank = conference_rank;
    m_conference_rank_isSet = true;
}

bool OAIStanding::is_conference_rank_Set() const{
    return m_conference_rank_isSet;
}

bool OAIStanding::is_conference_rank_Valid() const{
    return m_conference_rank_isValid;
}

qint32 OAIStanding::getConferenceTies() const {
    return m_conference_ties;
}
void OAIStanding::setConferenceTies(const qint32 &conference_ties) {
    m_conference_ties = conference_ties;
    m_conference_ties_isSet = true;
}

bool OAIStanding::is_conference_ties_Set() const{
    return m_conference_ties_isSet;
}

bool OAIStanding::is_conference_ties_Valid() const{
    return m_conference_ties_isValid;
}

qint32 OAIStanding::getConferenceWins() const {
    return m_conference_wins;
}
void OAIStanding::setConferenceWins(const qint32 &conference_wins) {
    m_conference_wins = conference_wins;
    m_conference_wins_isSet = true;
}

bool OAIStanding::is_conference_wins_Set() const{
    return m_conference_wins_isSet;
}

bool OAIStanding::is_conference_wins_Valid() const{
    return m_conference_wins_isValid;
}

QString OAIStanding::getDivision() const {
    return m_division;
}
void OAIStanding::setDivision(const QString &division) {
    m_division = division;
    m_division_isSet = true;
}

bool OAIStanding::is_division_Set() const{
    return m_division_isSet;
}

bool OAIStanding::is_division_Valid() const{
    return m_division_isValid;
}

qint32 OAIStanding::getDivisionLosses() const {
    return m_division_losses;
}
void OAIStanding::setDivisionLosses(const qint32 &division_losses) {
    m_division_losses = division_losses;
    m_division_losses_isSet = true;
}

bool OAIStanding::is_division_losses_Set() const{
    return m_division_losses_isSet;
}

bool OAIStanding::is_division_losses_Valid() const{
    return m_division_losses_isValid;
}

qint32 OAIStanding::getDivisionRank() const {
    return m_division_rank;
}
void OAIStanding::setDivisionRank(const qint32 &division_rank) {
    m_division_rank = division_rank;
    m_division_rank_isSet = true;
}

bool OAIStanding::is_division_rank_Set() const{
    return m_division_rank_isSet;
}

bool OAIStanding::is_division_rank_Valid() const{
    return m_division_rank_isValid;
}

qint32 OAIStanding::getDivisionTies() const {
    return m_division_ties;
}
void OAIStanding::setDivisionTies(const qint32 &division_ties) {
    m_division_ties = division_ties;
    m_division_ties_isSet = true;
}

bool OAIStanding::is_division_ties_Set() const{
    return m_division_ties_isSet;
}

bool OAIStanding::is_division_ties_Valid() const{
    return m_division_ties_isValid;
}

qint32 OAIStanding::getDivisionWins() const {
    return m_division_wins;
}
void OAIStanding::setDivisionWins(const qint32 &division_wins) {
    m_division_wins = division_wins;
    m_division_wins_isSet = true;
}

bool OAIStanding::is_division_wins_Set() const{
    return m_division_wins_isSet;
}

bool OAIStanding::is_division_wins_Valid() const{
    return m_division_wins_isValid;
}

qint32 OAIStanding::getGlobalTeamId() const {
    return m_global_team_id;
}
void OAIStanding::setGlobalTeamId(const qint32 &global_team_id) {
    m_global_team_id = global_team_id;
    m_global_team_id_isSet = true;
}

bool OAIStanding::is_global_team_id_Set() const{
    return m_global_team_id_isSet;
}

bool OAIStanding::is_global_team_id_Valid() const{
    return m_global_team_id_isValid;
}

qint32 OAIStanding::getLosses() const {
    return m_losses;
}
void OAIStanding::setLosses(const qint32 &losses) {
    m_losses = losses;
    m_losses_isSet = true;
}

bool OAIStanding::is_losses_Set() const{
    return m_losses_isSet;
}

bool OAIStanding::is_losses_Valid() const{
    return m_losses_isValid;
}

QString OAIStanding::getName() const {
    return m_name;
}
void OAIStanding::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIStanding::is_name_Set() const{
    return m_name_isSet;
}

bool OAIStanding::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIStanding::getNetPoints() const {
    return m_net_points;
}
void OAIStanding::setNetPoints(const qint32 &net_points) {
    m_net_points = net_points;
    m_net_points_isSet = true;
}

bool OAIStanding::is_net_points_Set() const{
    return m_net_points_isSet;
}

bool OAIStanding::is_net_points_Valid() const{
    return m_net_points_isValid;
}

double OAIStanding::getPercentage() const {
    return m_percentage;
}
void OAIStanding::setPercentage(const double &percentage) {
    m_percentage = percentage;
    m_percentage_isSet = true;
}

bool OAIStanding::is_percentage_Set() const{
    return m_percentage_isSet;
}

bool OAIStanding::is_percentage_Valid() const{
    return m_percentage_isValid;
}

qint32 OAIStanding::getPointsAgainst() const {
    return m_points_against;
}
void OAIStanding::setPointsAgainst(const qint32 &points_against) {
    m_points_against = points_against;
    m_points_against_isSet = true;
}

bool OAIStanding::is_points_against_Set() const{
    return m_points_against_isSet;
}

bool OAIStanding::is_points_against_Valid() const{
    return m_points_against_isValid;
}

qint32 OAIStanding::getPointsFor() const {
    return m_points_for;
}
void OAIStanding::setPointsFor(const qint32 &points_for) {
    m_points_for = points_for;
    m_points_for_isSet = true;
}

bool OAIStanding::is_points_for_Set() const{
    return m_points_for_isSet;
}

bool OAIStanding::is_points_for_Valid() const{
    return m_points_for_isValid;
}

qint32 OAIStanding::getSeason() const {
    return m_season;
}
void OAIStanding::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIStanding::is_season_Set() const{
    return m_season_isSet;
}

bool OAIStanding::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAIStanding::getSeasonType() const {
    return m_season_type;
}
void OAIStanding::setSeasonType(const qint32 &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAIStanding::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAIStanding::is_season_type_Valid() const{
    return m_season_type_isValid;
}

QString OAIStanding::getTeam() const {
    return m_team;
}
void OAIStanding::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIStanding::is_team_Set() const{
    return m_team_isSet;
}

bool OAIStanding::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAIStanding::getTeamId() const {
    return m_team_id;
}
void OAIStanding::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAIStanding::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAIStanding::is_team_id_Valid() const{
    return m_team_id_isValid;
}

qint32 OAIStanding::getTies() const {
    return m_ties;
}
void OAIStanding::setTies(const qint32 &ties) {
    m_ties = ties;
    m_ties_isSet = true;
}

bool OAIStanding::is_ties_Set() const{
    return m_ties_isSet;
}

bool OAIStanding::is_ties_Valid() const{
    return m_ties_isValid;
}

qint32 OAIStanding::getTouchdowns() const {
    return m_touchdowns;
}
void OAIStanding::setTouchdowns(const qint32 &touchdowns) {
    m_touchdowns = touchdowns;
    m_touchdowns_isSet = true;
}

bool OAIStanding::is_touchdowns_Set() const{
    return m_touchdowns_isSet;
}

bool OAIStanding::is_touchdowns_Valid() const{
    return m_touchdowns_isValid;
}

qint32 OAIStanding::getWins() const {
    return m_wins;
}
void OAIStanding::setWins(const qint32 &wins) {
    m_wins = wins;
    m_wins_isSet = true;
}

bool OAIStanding::is_wins_Set() const{
    return m_wins_isSet;
}

bool OAIStanding::is_wins_Valid() const{
    return m_wins_isValid;
}

bool OAIStanding::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_conference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_losses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_rank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_ties_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_wins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_losses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_rank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_ties_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_wins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_losses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_points_against_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_points_for_isSet) {
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

        if (m_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ties_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_touchdowns_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wins_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStanding::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
