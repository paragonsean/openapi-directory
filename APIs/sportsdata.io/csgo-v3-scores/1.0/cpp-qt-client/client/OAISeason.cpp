/**
 * CS:GO v3 Scores
 * CS:GO v3 Scores
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISeason.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISeason::OAISeason(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISeason::OAISeason() {
    this->initializeModel();
}

OAISeason::~OAISeason() {}

void OAISeason::initializeModel() {

    m_competition_id_isSet = false;
    m_competition_id_isValid = false;

    m_competition_name_isSet = false;
    m_competition_name_isValid = false;

    m_current_season_isSet = false;
    m_current_season_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_rounds_isSet = false;
    m_rounds_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_id_isSet = false;
    m_season_id_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;
}

void OAISeason::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISeason::fromJsonObject(QJsonObject json) {

    m_competition_id_isValid = ::OpenAPI::fromJsonValue(m_competition_id, json[QString("CompetitionId")]);
    m_competition_id_isSet = !json[QString("CompetitionId")].isNull() && m_competition_id_isValid;

    m_competition_name_isValid = ::OpenAPI::fromJsonValue(m_competition_name, json[QString("CompetitionName")]);
    m_competition_name_isSet = !json[QString("CompetitionName")].isNull() && m_competition_name_isValid;

    m_current_season_isValid = ::OpenAPI::fromJsonValue(m_current_season, json[QString("CurrentSeason")]);
    m_current_season_isSet = !json[QString("CurrentSeason")].isNull() && m_current_season_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("EndDate")]);
    m_end_date_isSet = !json[QString("EndDate")].isNull() && m_end_date_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_rounds_isValid = ::OpenAPI::fromJsonValue(m_rounds, json[QString("Rounds")]);
    m_rounds_isSet = !json[QString("Rounds")].isNull() && m_rounds_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_id_isValid = ::OpenAPI::fromJsonValue(m_season_id, json[QString("SeasonId")]);
    m_season_id_isSet = !json[QString("SeasonId")].isNull() && m_season_id_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("StartDate")]);
    m_start_date_isSet = !json[QString("StartDate")].isNull() && m_start_date_isValid;
}

QString OAISeason::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISeason::asJsonObject() const {
    QJsonObject obj;
    if (m_competition_id_isSet) {
        obj.insert(QString("CompetitionId"), ::OpenAPI::toJsonValue(m_competition_id));
    }
    if (m_competition_name_isSet) {
        obj.insert(QString("CompetitionName"), ::OpenAPI::toJsonValue(m_competition_name));
    }
    if (m_current_season_isSet) {
        obj.insert(QString("CurrentSeason"), ::OpenAPI::toJsonValue(m_current_season));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("EndDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_rounds.size() > 0) {
        obj.insert(QString("Rounds"), ::OpenAPI::toJsonValue(m_rounds));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_id_isSet) {
        obj.insert(QString("SeasonId"), ::OpenAPI::toJsonValue(m_season_id));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("StartDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    return obj;
}

qint32 OAISeason::getCompetitionId() const {
    return m_competition_id;
}
void OAISeason::setCompetitionId(const qint32 &competition_id) {
    m_competition_id = competition_id;
    m_competition_id_isSet = true;
}

bool OAISeason::is_competition_id_Set() const{
    return m_competition_id_isSet;
}

bool OAISeason::is_competition_id_Valid() const{
    return m_competition_id_isValid;
}

QString OAISeason::getCompetitionName() const {
    return m_competition_name;
}
void OAISeason::setCompetitionName(const QString &competition_name) {
    m_competition_name = competition_name;
    m_competition_name_isSet = true;
}

bool OAISeason::is_competition_name_Set() const{
    return m_competition_name_isSet;
}

bool OAISeason::is_competition_name_Valid() const{
    return m_competition_name_isValid;
}

bool OAISeason::isCurrentSeason() const {
    return m_current_season;
}
void OAISeason::setCurrentSeason(const bool &current_season) {
    m_current_season = current_season;
    m_current_season_isSet = true;
}

bool OAISeason::is_current_season_Set() const{
    return m_current_season_isSet;
}

bool OAISeason::is_current_season_Valid() const{
    return m_current_season_isValid;
}

QString OAISeason::getEndDate() const {
    return m_end_date;
}
void OAISeason::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAISeason::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAISeason::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAISeason::getName() const {
    return m_name;
}
void OAISeason::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISeason::is_name_Set() const{
    return m_name_isSet;
}

bool OAISeason::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIRound> OAISeason::getRounds() const {
    return m_rounds;
}
void OAISeason::setRounds(const QList<OAIRound> &rounds) {
    m_rounds = rounds;
    m_rounds_isSet = true;
}

bool OAISeason::is_rounds_Set() const{
    return m_rounds_isSet;
}

bool OAISeason::is_rounds_Valid() const{
    return m_rounds_isValid;
}

qint32 OAISeason::getSeason() const {
    return m_season;
}
void OAISeason::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAISeason::is_season_Set() const{
    return m_season_isSet;
}

bool OAISeason::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAISeason::getSeasonId() const {
    return m_season_id;
}
void OAISeason::setSeasonId(const qint32 &season_id) {
    m_season_id = season_id;
    m_season_id_isSet = true;
}

bool OAISeason::is_season_id_Set() const{
    return m_season_id_isSet;
}

bool OAISeason::is_season_id_Valid() const{
    return m_season_id_isValid;
}

QString OAISeason::getStartDate() const {
    return m_start_date;
}
void OAISeason::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAISeason::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAISeason::is_start_date_Valid() const{
    return m_start_date_isValid;
}

bool OAISeason::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_competition_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_competition_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rounds.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISeason::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
