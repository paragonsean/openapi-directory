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

#include "OAISeasonTeam.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISeasonTeam::OAISeasonTeam(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISeasonTeam::OAISeasonTeam() {
    this->initializeModel();
}

OAISeasonTeam::~OAISeasonTeam() {}

void OAISeasonTeam::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_season_id_isSet = false;
    m_season_id_isValid = false;

    m_season_team_id_isSet = false;
    m_season_team_id_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_team_name_isSet = false;
    m_team_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAISeasonTeam::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISeasonTeam::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("Active")]);
    m_active_isSet = !json[QString("Active")].isNull() && m_active_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("Gender")]);
    m_gender_isSet = !json[QString("Gender")].isNull() && m_gender_isValid;

    m_season_id_isValid = ::OpenAPI::fromJsonValue(m_season_id, json[QString("SeasonId")]);
    m_season_id_isSet = !json[QString("SeasonId")].isNull() && m_season_id_isValid;

    m_season_team_id_isValid = ::OpenAPI::fromJsonValue(m_season_team_id, json[QString("SeasonTeamId")]);
    m_season_team_id_isSet = !json[QString("SeasonTeamId")].isNull() && m_season_team_id_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamId")]);
    m_team_id_isSet = !json[QString("TeamId")].isNull() && m_team_id_isValid;

    m_team_name_isValid = ::OpenAPI::fromJsonValue(m_team_name, json[QString("TeamName")]);
    m_team_name_isSet = !json[QString("TeamName")].isNull() && m_team_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;
}

QString OAISeasonTeam::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISeasonTeam::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("Active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_gender_isSet) {
        obj.insert(QString("Gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_season_id_isSet) {
        obj.insert(QString("SeasonId"), ::OpenAPI::toJsonValue(m_season_id));
    }
    if (m_season_team_id_isSet) {
        obj.insert(QString("SeasonTeamId"), ::OpenAPI::toJsonValue(m_season_team_id));
    }
    if (m_team.isSet()) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamId"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_team_name_isSet) {
        obj.insert(QString("TeamName"), ::OpenAPI::toJsonValue(m_team_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

bool OAISeasonTeam::isActive() const {
    return m_active;
}
void OAISeasonTeam::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAISeasonTeam::is_active_Set() const{
    return m_active_isSet;
}

bool OAISeasonTeam::is_active_Valid() const{
    return m_active_isValid;
}

QString OAISeasonTeam::getGender() const {
    return m_gender;
}
void OAISeasonTeam::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAISeasonTeam::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAISeasonTeam::is_gender_Valid() const{
    return m_gender_isValid;
}

qint32 OAISeasonTeam::getSeasonId() const {
    return m_season_id;
}
void OAISeasonTeam::setSeasonId(const qint32 &season_id) {
    m_season_id = season_id;
    m_season_id_isSet = true;
}

bool OAISeasonTeam::is_season_id_Set() const{
    return m_season_id_isSet;
}

bool OAISeasonTeam::is_season_id_Valid() const{
    return m_season_id_isValid;
}

qint32 OAISeasonTeam::getSeasonTeamId() const {
    return m_season_team_id;
}
void OAISeasonTeam::setSeasonTeamId(const qint32 &season_team_id) {
    m_season_team_id = season_team_id;
    m_season_team_id_isSet = true;
}

bool OAISeasonTeam::is_season_team_id_Set() const{
    return m_season_team_id_isSet;
}

bool OAISeasonTeam::is_season_team_id_Valid() const{
    return m_season_team_id_isValid;
}

OAITeam OAISeasonTeam::getTeam() const {
    return m_team;
}
void OAISeasonTeam::setTeam(const OAITeam &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAISeasonTeam::is_team_Set() const{
    return m_team_isSet;
}

bool OAISeasonTeam::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAISeasonTeam::getTeamId() const {
    return m_team_id;
}
void OAISeasonTeam::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAISeasonTeam::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAISeasonTeam::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QString OAISeasonTeam::getTeamName() const {
    return m_team_name;
}
void OAISeasonTeam::setTeamName(const QString &team_name) {
    m_team_name = team_name;
    m_team_name_isSet = true;
}

bool OAISeasonTeam::is_team_name_Set() const{
    return m_team_name_isSet;
}

bool OAISeasonTeam::is_team_name_Valid() const{
    return m_team_name_isValid;
}

QString OAISeasonTeam::getType() const {
    return m_type;
}
void OAISeasonTeam::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAISeasonTeam::is_type_Set() const{
    return m_type_isSet;
}

bool OAISeasonTeam::is_type_Valid() const{
    return m_type_isValid;
}

bool OAISeasonTeam::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_name_isSet) {
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

bool OAISeasonTeam::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
