/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICompetition.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompetition::OAICompetition(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompetition::OAICompetition() {
    this->initializeModel();
}

OAICompetition::~OAICompetition() {}

void OAICompetition::initializeModel() {

    m_area_id_isSet = false;
    m_area_id_isValid = false;

    m_area_name_isSet = false;
    m_area_name_isValid = false;

    m_competition_id_isSet = false;
    m_competition_id_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_player_stats_coverage_isSet = false;
    m_player_stats_coverage_isValid = false;

    m_seasons_isSet = false;
    m_seasons_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAICompetition::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompetition::fromJsonObject(QJsonObject json) {

    m_area_id_isValid = ::OpenAPI::fromJsonValue(m_area_id, json[QString("AreaId")]);
    m_area_id_isSet = !json[QString("AreaId")].isNull() && m_area_id_isValid;

    m_area_name_isValid = ::OpenAPI::fromJsonValue(m_area_name, json[QString("AreaName")]);
    m_area_name_isSet = !json[QString("AreaName")].isNull() && m_area_name_isValid;

    m_competition_id_isValid = ::OpenAPI::fromJsonValue(m_competition_id, json[QString("CompetitionId")]);
    m_competition_id_isSet = !json[QString("CompetitionId")].isNull() && m_competition_id_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("Format")]);
    m_format_isSet = !json[QString("Format")].isNull() && m_format_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("Gender")]);
    m_gender_isSet = !json[QString("Gender")].isNull() && m_gender_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_player_stats_coverage_isValid = ::OpenAPI::fromJsonValue(m_player_stats_coverage, json[QString("PlayerStatsCoverage")]);
    m_player_stats_coverage_isSet = !json[QString("PlayerStatsCoverage")].isNull() && m_player_stats_coverage_isValid;

    m_seasons_isValid = ::OpenAPI::fromJsonValue(m_seasons, json[QString("Seasons")]);
    m_seasons_isSet = !json[QString("Seasons")].isNull() && m_seasons_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;
}

QString OAICompetition::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompetition::asJsonObject() const {
    QJsonObject obj;
    if (m_area_id_isSet) {
        obj.insert(QString("AreaId"), ::OpenAPI::toJsonValue(m_area_id));
    }
    if (m_area_name_isSet) {
        obj.insert(QString("AreaName"), ::OpenAPI::toJsonValue(m_area_name));
    }
    if (m_competition_id_isSet) {
        obj.insert(QString("CompetitionId"), ::OpenAPI::toJsonValue(m_competition_id));
    }
    if (m_format_isSet) {
        obj.insert(QString("Format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_gender_isSet) {
        obj.insert(QString("Gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_player_stats_coverage_isSet) {
        obj.insert(QString("PlayerStatsCoverage"), ::OpenAPI::toJsonValue(m_player_stats_coverage));
    }
    if (m_seasons.size() > 0) {
        obj.insert(QString("Seasons"), ::OpenAPI::toJsonValue(m_seasons));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAICompetition::getAreaId() const {
    return m_area_id;
}
void OAICompetition::setAreaId(const qint32 &area_id) {
    m_area_id = area_id;
    m_area_id_isSet = true;
}

bool OAICompetition::is_area_id_Set() const{
    return m_area_id_isSet;
}

bool OAICompetition::is_area_id_Valid() const{
    return m_area_id_isValid;
}

QString OAICompetition::getAreaName() const {
    return m_area_name;
}
void OAICompetition::setAreaName(const QString &area_name) {
    m_area_name = area_name;
    m_area_name_isSet = true;
}

bool OAICompetition::is_area_name_Set() const{
    return m_area_name_isSet;
}

bool OAICompetition::is_area_name_Valid() const{
    return m_area_name_isValid;
}

qint32 OAICompetition::getCompetitionId() const {
    return m_competition_id;
}
void OAICompetition::setCompetitionId(const qint32 &competition_id) {
    m_competition_id = competition_id;
    m_competition_id_isSet = true;
}

bool OAICompetition::is_competition_id_Set() const{
    return m_competition_id_isSet;
}

bool OAICompetition::is_competition_id_Valid() const{
    return m_competition_id_isValid;
}

QString OAICompetition::getFormat() const {
    return m_format;
}
void OAICompetition::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAICompetition::is_format_Set() const{
    return m_format_isSet;
}

bool OAICompetition::is_format_Valid() const{
    return m_format_isValid;
}

QString OAICompetition::getGender() const {
    return m_gender;
}
void OAICompetition::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAICompetition::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAICompetition::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAICompetition::getName() const {
    return m_name;
}
void OAICompetition::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICompetition::is_name_Set() const{
    return m_name_isSet;
}

bool OAICompetition::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICompetition::isPlayerStatsCoverage() const {
    return m_player_stats_coverage;
}
void OAICompetition::setPlayerStatsCoverage(const bool &player_stats_coverage) {
    m_player_stats_coverage = player_stats_coverage;
    m_player_stats_coverage_isSet = true;
}

bool OAICompetition::is_player_stats_coverage_Set() const{
    return m_player_stats_coverage_isSet;
}

bool OAICompetition::is_player_stats_coverage_Valid() const{
    return m_player_stats_coverage_isValid;
}

QList<OAISeason> OAICompetition::getSeasons() const {
    return m_seasons;
}
void OAICompetition::setSeasons(const QList<OAISeason> &seasons) {
    m_seasons = seasons;
    m_seasons_isSet = true;
}

bool OAICompetition::is_seasons_Set() const{
    return m_seasons_isSet;
}

bool OAICompetition::is_seasons_Valid() const{
    return m_seasons_isValid;
}

QString OAICompetition::getType() const {
    return m_type;
}
void OAICompetition::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICompetition::is_type_Set() const{
    return m_type_isSet;
}

bool OAICompetition::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICompetition::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_area_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_area_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_competition_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_stats_coverage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seasons.size() > 0) {
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

bool OAICompetition::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
