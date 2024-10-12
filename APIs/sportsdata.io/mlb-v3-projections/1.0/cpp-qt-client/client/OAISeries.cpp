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

#include "OAISeries.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISeries::OAISeries(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISeries::OAISeries() {
    this->initializeModel();
}

OAISeries::~OAISeries() {}

void OAISeries::initializeModel() {

    m_away_team_wins_isSet = false;
    m_away_team_wins_isValid = false;

    m_game_number_isSet = false;
    m_game_number_isValid = false;

    m_home_team_wins_isSet = false;
    m_home_team_wins_isValid = false;

    m_max_length_isSet = false;
    m_max_length_isValid = false;
}

void OAISeries::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISeries::fromJsonObject(QJsonObject json) {

    m_away_team_wins_isValid = ::OpenAPI::fromJsonValue(m_away_team_wins, json[QString("AwayTeamWins")]);
    m_away_team_wins_isSet = !json[QString("AwayTeamWins")].isNull() && m_away_team_wins_isValid;

    m_game_number_isValid = ::OpenAPI::fromJsonValue(m_game_number, json[QString("GameNumber")]);
    m_game_number_isSet = !json[QString("GameNumber")].isNull() && m_game_number_isValid;

    m_home_team_wins_isValid = ::OpenAPI::fromJsonValue(m_home_team_wins, json[QString("HomeTeamWins")]);
    m_home_team_wins_isSet = !json[QString("HomeTeamWins")].isNull() && m_home_team_wins_isValid;

    m_max_length_isValid = ::OpenAPI::fromJsonValue(m_max_length, json[QString("MaxLength")]);
    m_max_length_isSet = !json[QString("MaxLength")].isNull() && m_max_length_isValid;
}

QString OAISeries::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISeries::asJsonObject() const {
    QJsonObject obj;
    if (m_away_team_wins_isSet) {
        obj.insert(QString("AwayTeamWins"), ::OpenAPI::toJsonValue(m_away_team_wins));
    }
    if (m_game_number_isSet) {
        obj.insert(QString("GameNumber"), ::OpenAPI::toJsonValue(m_game_number));
    }
    if (m_home_team_wins_isSet) {
        obj.insert(QString("HomeTeamWins"), ::OpenAPI::toJsonValue(m_home_team_wins));
    }
    if (m_max_length_isSet) {
        obj.insert(QString("MaxLength"), ::OpenAPI::toJsonValue(m_max_length));
    }
    return obj;
}

qint32 OAISeries::getAwayTeamWins() const {
    return m_away_team_wins;
}
void OAISeries::setAwayTeamWins(const qint32 &away_team_wins) {
    m_away_team_wins = away_team_wins;
    m_away_team_wins_isSet = true;
}

bool OAISeries::is_away_team_wins_Set() const{
    return m_away_team_wins_isSet;
}

bool OAISeries::is_away_team_wins_Valid() const{
    return m_away_team_wins_isValid;
}

qint32 OAISeries::getGameNumber() const {
    return m_game_number;
}
void OAISeries::setGameNumber(const qint32 &game_number) {
    m_game_number = game_number;
    m_game_number_isSet = true;
}

bool OAISeries::is_game_number_Set() const{
    return m_game_number_isSet;
}

bool OAISeries::is_game_number_Valid() const{
    return m_game_number_isValid;
}

qint32 OAISeries::getHomeTeamWins() const {
    return m_home_team_wins;
}
void OAISeries::setHomeTeamWins(const qint32 &home_team_wins) {
    m_home_team_wins = home_team_wins;
    m_home_team_wins_isSet = true;
}

bool OAISeries::is_home_team_wins_Set() const{
    return m_home_team_wins_isSet;
}

bool OAISeries::is_home_team_wins_Valid() const{
    return m_home_team_wins_isValid;
}

qint32 OAISeries::getMaxLength() const {
    return m_max_length;
}
void OAISeries::setMaxLength(const qint32 &max_length) {
    m_max_length = max_length;
    m_max_length_isSet = true;
}

bool OAISeries::is_max_length_Set() const{
    return m_max_length_isSet;
}

bool OAISeries::is_max_length_Valid() const{
    return m_max_length_isValid;
}

bool OAISeries::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_away_team_wins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_wins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_length_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISeries::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
