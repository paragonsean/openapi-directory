/**
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuarter.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuarter::OAIQuarter(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuarter::OAIQuarter() {
    this->initializeModel();
}

OAIQuarter::~OAIQuarter() {}

void OAIQuarter::initializeModel() {

    m_away_team_score_isSet = false;
    m_away_team_score_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_home_team_score_isSet = false;
    m_home_team_score_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_quarter_id_isSet = false;
    m_quarter_id_isValid = false;

    m_score_id_isSet = false;
    m_score_id_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAIQuarter::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuarter::fromJsonObject(QJsonObject json) {

    m_away_team_score_isValid = ::OpenAPI::fromJsonValue(m_away_team_score, json[QString("AwayTeamScore")]);
    m_away_team_score_isSet = !json[QString("AwayTeamScore")].isNull() && m_away_team_score_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("Created")]);
    m_created_isSet = !json[QString("Created")].isNull() && m_created_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_home_team_score_isValid = ::OpenAPI::fromJsonValue(m_home_team_score, json[QString("HomeTeamScore")]);
    m_home_team_score_isSet = !json[QString("HomeTeamScore")].isNull() && m_home_team_score_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("Number")]);
    m_number_isSet = !json[QString("Number")].isNull() && m_number_isValid;

    m_quarter_id_isValid = ::OpenAPI::fromJsonValue(m_quarter_id, json[QString("QuarterID")]);
    m_quarter_id_isSet = !json[QString("QuarterID")].isNull() && m_quarter_id_isValid;

    m_score_id_isValid = ::OpenAPI::fromJsonValue(m_score_id, json[QString("ScoreID")]);
    m_score_id_isSet = !json[QString("ScoreID")].isNull() && m_score_id_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;
}

QString OAIQuarter::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuarter::asJsonObject() const {
    QJsonObject obj;
    if (m_away_team_score_isSet) {
        obj.insert(QString("AwayTeamScore"), ::OpenAPI::toJsonValue(m_away_team_score));
    }
    if (m_created_isSet) {
        obj.insert(QString("Created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_home_team_score_isSet) {
        obj.insert(QString("HomeTeamScore"), ::OpenAPI::toJsonValue(m_home_team_score));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_isSet) {
        obj.insert(QString("Number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_quarter_id_isSet) {
        obj.insert(QString("QuarterID"), ::OpenAPI::toJsonValue(m_quarter_id));
    }
    if (m_score_id_isSet) {
        obj.insert(QString("ScoreID"), ::OpenAPI::toJsonValue(m_score_id));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

qint32 OAIQuarter::getAwayTeamScore() const {
    return m_away_team_score;
}
void OAIQuarter::setAwayTeamScore(const qint32 &away_team_score) {
    m_away_team_score = away_team_score;
    m_away_team_score_isSet = true;
}

bool OAIQuarter::is_away_team_score_Set() const{
    return m_away_team_score_isSet;
}

bool OAIQuarter::is_away_team_score_Valid() const{
    return m_away_team_score_isValid;
}

QString OAIQuarter::getCreated() const {
    return m_created;
}
void OAIQuarter::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIQuarter::is_created_Set() const{
    return m_created_isSet;
}

bool OAIQuarter::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIQuarter::getDescription() const {
    return m_description;
}
void OAIQuarter::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIQuarter::is_description_Set() const{
    return m_description_isSet;
}

bool OAIQuarter::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIQuarter::getHomeTeamScore() const {
    return m_home_team_score;
}
void OAIQuarter::setHomeTeamScore(const qint32 &home_team_score) {
    m_home_team_score = home_team_score;
    m_home_team_score_isSet = true;
}

bool OAIQuarter::is_home_team_score_Set() const{
    return m_home_team_score_isSet;
}

bool OAIQuarter::is_home_team_score_Valid() const{
    return m_home_team_score_isValid;
}

QString OAIQuarter::getName() const {
    return m_name;
}
void OAIQuarter::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIQuarter::is_name_Set() const{
    return m_name_isSet;
}

bool OAIQuarter::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIQuarter::getNumber() const {
    return m_number;
}
void OAIQuarter::setNumber(const qint32 &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIQuarter::is_number_Set() const{
    return m_number_isSet;
}

bool OAIQuarter::is_number_Valid() const{
    return m_number_isValid;
}

qint32 OAIQuarter::getQuarterId() const {
    return m_quarter_id;
}
void OAIQuarter::setQuarterId(const qint32 &quarter_id) {
    m_quarter_id = quarter_id;
    m_quarter_id_isSet = true;
}

bool OAIQuarter::is_quarter_id_Set() const{
    return m_quarter_id_isSet;
}

bool OAIQuarter::is_quarter_id_Valid() const{
    return m_quarter_id_isValid;
}

qint32 OAIQuarter::getScoreId() const {
    return m_score_id;
}
void OAIQuarter::setScoreId(const qint32 &score_id) {
    m_score_id = score_id;
    m_score_id_isSet = true;
}

bool OAIQuarter::is_score_id_Set() const{
    return m_score_id_isSet;
}

bool OAIQuarter::is_score_id_Valid() const{
    return m_score_id_isValid;
}

QString OAIQuarter::getUpdated() const {
    return m_updated;
}
void OAIQuarter::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIQuarter::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIQuarter::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIQuarter::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_away_team_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quarter_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuarter::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
