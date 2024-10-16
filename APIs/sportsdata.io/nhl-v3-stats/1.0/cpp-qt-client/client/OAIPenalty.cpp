/**
 * NHL v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPenalty.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPenalty::OAIPenalty(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPenalty::OAIPenalty() {
    this->initializeModel();
}

OAIPenalty::~OAIPenalty() {}

void OAIPenalty::initializeModel() {

    m_bench_penalty_served_by_player_id_isSet = false;
    m_bench_penalty_served_by_player_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_drawn_by_player_id_isSet = false;
    m_drawn_by_player_id_isValid = false;

    m_drawn_by_team_id_isSet = false;
    m_drawn_by_team_id_isValid = false;

    m_is_bench_penalty_isSet = false;
    m_is_bench_penalty_isValid = false;

    m_penalized_player_id_isSet = false;
    m_penalized_player_id_isValid = false;

    m_penalized_team_id_isSet = false;
    m_penalized_team_id_isValid = false;

    m_penalty_id_isSet = false;
    m_penalty_id_isValid = false;

    m_penalty_minutes_isSet = false;
    m_penalty_minutes_isValid = false;

    m_period_id_isSet = false;
    m_period_id_isValid = false;

    m_sequence_isSet = false;
    m_sequence_isValid = false;

    m_time_remaining_minutes_isSet = false;
    m_time_remaining_minutes_isValid = false;

    m_time_remaining_seconds_isSet = false;
    m_time_remaining_seconds_isValid = false;
}

void OAIPenalty::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPenalty::fromJsonObject(QJsonObject json) {

    m_bench_penalty_served_by_player_id_isValid = ::OpenAPI::fromJsonValue(m_bench_penalty_served_by_player_id, json[QString("BenchPenaltyServedByPlayerID")]);
    m_bench_penalty_served_by_player_id_isSet = !json[QString("BenchPenaltyServedByPlayerID")].isNull() && m_bench_penalty_served_by_player_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_drawn_by_player_id_isValid = ::OpenAPI::fromJsonValue(m_drawn_by_player_id, json[QString("DrawnByPlayerID")]);
    m_drawn_by_player_id_isSet = !json[QString("DrawnByPlayerID")].isNull() && m_drawn_by_player_id_isValid;

    m_drawn_by_team_id_isValid = ::OpenAPI::fromJsonValue(m_drawn_by_team_id, json[QString("DrawnByTeamID")]);
    m_drawn_by_team_id_isSet = !json[QString("DrawnByTeamID")].isNull() && m_drawn_by_team_id_isValid;

    m_is_bench_penalty_isValid = ::OpenAPI::fromJsonValue(m_is_bench_penalty, json[QString("IsBenchPenalty")]);
    m_is_bench_penalty_isSet = !json[QString("IsBenchPenalty")].isNull() && m_is_bench_penalty_isValid;

    m_penalized_player_id_isValid = ::OpenAPI::fromJsonValue(m_penalized_player_id, json[QString("PenalizedPlayerID")]);
    m_penalized_player_id_isSet = !json[QString("PenalizedPlayerID")].isNull() && m_penalized_player_id_isValid;

    m_penalized_team_id_isValid = ::OpenAPI::fromJsonValue(m_penalized_team_id, json[QString("PenalizedTeamID")]);
    m_penalized_team_id_isSet = !json[QString("PenalizedTeamID")].isNull() && m_penalized_team_id_isValid;

    m_penalty_id_isValid = ::OpenAPI::fromJsonValue(m_penalty_id, json[QString("PenaltyID")]);
    m_penalty_id_isSet = !json[QString("PenaltyID")].isNull() && m_penalty_id_isValid;

    m_penalty_minutes_isValid = ::OpenAPI::fromJsonValue(m_penalty_minutes, json[QString("PenaltyMinutes")]);
    m_penalty_minutes_isSet = !json[QString("PenaltyMinutes")].isNull() && m_penalty_minutes_isValid;

    m_period_id_isValid = ::OpenAPI::fromJsonValue(m_period_id, json[QString("PeriodID")]);
    m_period_id_isSet = !json[QString("PeriodID")].isNull() && m_period_id_isValid;

    m_sequence_isValid = ::OpenAPI::fromJsonValue(m_sequence, json[QString("Sequence")]);
    m_sequence_isSet = !json[QString("Sequence")].isNull() && m_sequence_isValid;

    m_time_remaining_minutes_isValid = ::OpenAPI::fromJsonValue(m_time_remaining_minutes, json[QString("TimeRemainingMinutes")]);
    m_time_remaining_minutes_isSet = !json[QString("TimeRemainingMinutes")].isNull() && m_time_remaining_minutes_isValid;

    m_time_remaining_seconds_isValid = ::OpenAPI::fromJsonValue(m_time_remaining_seconds, json[QString("TimeRemainingSeconds")]);
    m_time_remaining_seconds_isSet = !json[QString("TimeRemainingSeconds")].isNull() && m_time_remaining_seconds_isValid;
}

QString OAIPenalty::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPenalty::asJsonObject() const {
    QJsonObject obj;
    if (m_bench_penalty_served_by_player_id_isSet) {
        obj.insert(QString("BenchPenaltyServedByPlayerID"), ::OpenAPI::toJsonValue(m_bench_penalty_served_by_player_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_drawn_by_player_id_isSet) {
        obj.insert(QString("DrawnByPlayerID"), ::OpenAPI::toJsonValue(m_drawn_by_player_id));
    }
    if (m_drawn_by_team_id_isSet) {
        obj.insert(QString("DrawnByTeamID"), ::OpenAPI::toJsonValue(m_drawn_by_team_id));
    }
    if (m_is_bench_penalty_isSet) {
        obj.insert(QString("IsBenchPenalty"), ::OpenAPI::toJsonValue(m_is_bench_penalty));
    }
    if (m_penalized_player_id_isSet) {
        obj.insert(QString("PenalizedPlayerID"), ::OpenAPI::toJsonValue(m_penalized_player_id));
    }
    if (m_penalized_team_id_isSet) {
        obj.insert(QString("PenalizedTeamID"), ::OpenAPI::toJsonValue(m_penalized_team_id));
    }
    if (m_penalty_id_isSet) {
        obj.insert(QString("PenaltyID"), ::OpenAPI::toJsonValue(m_penalty_id));
    }
    if (m_penalty_minutes_isSet) {
        obj.insert(QString("PenaltyMinutes"), ::OpenAPI::toJsonValue(m_penalty_minutes));
    }
    if (m_period_id_isSet) {
        obj.insert(QString("PeriodID"), ::OpenAPI::toJsonValue(m_period_id));
    }
    if (m_sequence_isSet) {
        obj.insert(QString("Sequence"), ::OpenAPI::toJsonValue(m_sequence));
    }
    if (m_time_remaining_minutes_isSet) {
        obj.insert(QString("TimeRemainingMinutes"), ::OpenAPI::toJsonValue(m_time_remaining_minutes));
    }
    if (m_time_remaining_seconds_isSet) {
        obj.insert(QString("TimeRemainingSeconds"), ::OpenAPI::toJsonValue(m_time_remaining_seconds));
    }
    return obj;
}

qint32 OAIPenalty::getBenchPenaltyServedByPlayerId() const {
    return m_bench_penalty_served_by_player_id;
}
void OAIPenalty::setBenchPenaltyServedByPlayerId(const qint32 &bench_penalty_served_by_player_id) {
    m_bench_penalty_served_by_player_id = bench_penalty_served_by_player_id;
    m_bench_penalty_served_by_player_id_isSet = true;
}

bool OAIPenalty::is_bench_penalty_served_by_player_id_Set() const{
    return m_bench_penalty_served_by_player_id_isSet;
}

bool OAIPenalty::is_bench_penalty_served_by_player_id_Valid() const{
    return m_bench_penalty_served_by_player_id_isValid;
}

QString OAIPenalty::getDescription() const {
    return m_description;
}
void OAIPenalty::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPenalty::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPenalty::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIPenalty::getDrawnByPlayerId() const {
    return m_drawn_by_player_id;
}
void OAIPenalty::setDrawnByPlayerId(const qint32 &drawn_by_player_id) {
    m_drawn_by_player_id = drawn_by_player_id;
    m_drawn_by_player_id_isSet = true;
}

bool OAIPenalty::is_drawn_by_player_id_Set() const{
    return m_drawn_by_player_id_isSet;
}

bool OAIPenalty::is_drawn_by_player_id_Valid() const{
    return m_drawn_by_player_id_isValid;
}

qint32 OAIPenalty::getDrawnByTeamId() const {
    return m_drawn_by_team_id;
}
void OAIPenalty::setDrawnByTeamId(const qint32 &drawn_by_team_id) {
    m_drawn_by_team_id = drawn_by_team_id;
    m_drawn_by_team_id_isSet = true;
}

bool OAIPenalty::is_drawn_by_team_id_Set() const{
    return m_drawn_by_team_id_isSet;
}

bool OAIPenalty::is_drawn_by_team_id_Valid() const{
    return m_drawn_by_team_id_isValid;
}

bool OAIPenalty::isIsBenchPenalty() const {
    return m_is_bench_penalty;
}
void OAIPenalty::setIsBenchPenalty(const bool &is_bench_penalty) {
    m_is_bench_penalty = is_bench_penalty;
    m_is_bench_penalty_isSet = true;
}

bool OAIPenalty::is_is_bench_penalty_Set() const{
    return m_is_bench_penalty_isSet;
}

bool OAIPenalty::is_is_bench_penalty_Valid() const{
    return m_is_bench_penalty_isValid;
}

qint32 OAIPenalty::getPenalizedPlayerId() const {
    return m_penalized_player_id;
}
void OAIPenalty::setPenalizedPlayerId(const qint32 &penalized_player_id) {
    m_penalized_player_id = penalized_player_id;
    m_penalized_player_id_isSet = true;
}

bool OAIPenalty::is_penalized_player_id_Set() const{
    return m_penalized_player_id_isSet;
}

bool OAIPenalty::is_penalized_player_id_Valid() const{
    return m_penalized_player_id_isValid;
}

qint32 OAIPenalty::getPenalizedTeamId() const {
    return m_penalized_team_id;
}
void OAIPenalty::setPenalizedTeamId(const qint32 &penalized_team_id) {
    m_penalized_team_id = penalized_team_id;
    m_penalized_team_id_isSet = true;
}

bool OAIPenalty::is_penalized_team_id_Set() const{
    return m_penalized_team_id_isSet;
}

bool OAIPenalty::is_penalized_team_id_Valid() const{
    return m_penalized_team_id_isValid;
}

qint32 OAIPenalty::getPenaltyId() const {
    return m_penalty_id;
}
void OAIPenalty::setPenaltyId(const qint32 &penalty_id) {
    m_penalty_id = penalty_id;
    m_penalty_id_isSet = true;
}

bool OAIPenalty::is_penalty_id_Set() const{
    return m_penalty_id_isSet;
}

bool OAIPenalty::is_penalty_id_Valid() const{
    return m_penalty_id_isValid;
}

qint32 OAIPenalty::getPenaltyMinutes() const {
    return m_penalty_minutes;
}
void OAIPenalty::setPenaltyMinutes(const qint32 &penalty_minutes) {
    m_penalty_minutes = penalty_minutes;
    m_penalty_minutes_isSet = true;
}

bool OAIPenalty::is_penalty_minutes_Set() const{
    return m_penalty_minutes_isSet;
}

bool OAIPenalty::is_penalty_minutes_Valid() const{
    return m_penalty_minutes_isValid;
}

qint32 OAIPenalty::getPeriodId() const {
    return m_period_id;
}
void OAIPenalty::setPeriodId(const qint32 &period_id) {
    m_period_id = period_id;
    m_period_id_isSet = true;
}

bool OAIPenalty::is_period_id_Set() const{
    return m_period_id_isSet;
}

bool OAIPenalty::is_period_id_Valid() const{
    return m_period_id_isValid;
}

qint32 OAIPenalty::getSequence() const {
    return m_sequence;
}
void OAIPenalty::setSequence(const qint32 &sequence) {
    m_sequence = sequence;
    m_sequence_isSet = true;
}

bool OAIPenalty::is_sequence_Set() const{
    return m_sequence_isSet;
}

bool OAIPenalty::is_sequence_Valid() const{
    return m_sequence_isValid;
}

qint32 OAIPenalty::getTimeRemainingMinutes() const {
    return m_time_remaining_minutes;
}
void OAIPenalty::setTimeRemainingMinutes(const qint32 &time_remaining_minutes) {
    m_time_remaining_minutes = time_remaining_minutes;
    m_time_remaining_minutes_isSet = true;
}

bool OAIPenalty::is_time_remaining_minutes_Set() const{
    return m_time_remaining_minutes_isSet;
}

bool OAIPenalty::is_time_remaining_minutes_Valid() const{
    return m_time_remaining_minutes_isValid;
}

qint32 OAIPenalty::getTimeRemainingSeconds() const {
    return m_time_remaining_seconds;
}
void OAIPenalty::setTimeRemainingSeconds(const qint32 &time_remaining_seconds) {
    m_time_remaining_seconds = time_remaining_seconds;
    m_time_remaining_seconds_isSet = true;
}

bool OAIPenalty::is_time_remaining_seconds_Set() const{
    return m_time_remaining_seconds_isSet;
}

bool OAIPenalty::is_time_remaining_seconds_Valid() const{
    return m_time_remaining_seconds_isValid;
}

bool OAIPenalty::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bench_penalty_served_by_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_drawn_by_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_drawn_by_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_bench_penalty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_penalized_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_penalized_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_penalty_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_penalty_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_period_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sequence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_remaining_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_remaining_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPenalty::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
