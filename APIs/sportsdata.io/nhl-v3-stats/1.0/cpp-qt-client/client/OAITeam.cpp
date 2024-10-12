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

#include "OAITeam.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITeam::OAITeam(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITeam::OAITeam() {
    this->initializeModel();
}

OAITeam::~OAITeam() {}

void OAITeam::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_conference_isSet = false;
    m_conference_isValid = false;

    m_division_isSet = false;
    m_division_isValid = false;

    m_global_team_id_isSet = false;
    m_global_team_id_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_primary_color_isSet = false;
    m_primary_color_isValid = false;

    m_quaternary_color_isSet = false;
    m_quaternary_color_isValid = false;

    m_secondary_color_isSet = false;
    m_secondary_color_isValid = false;

    m_stadium_id_isSet = false;
    m_stadium_id_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_tertiary_color_isSet = false;
    m_tertiary_color_isValid = false;

    m_wikipedia_logo_url_isSet = false;
    m_wikipedia_logo_url_isValid = false;

    m_wikipedia_word_mark_url_isSet = false;
    m_wikipedia_word_mark_url_isValid = false;
}

void OAITeam::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITeam::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("Active")]);
    m_active_isSet = !json[QString("Active")].isNull() && m_active_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("City")]);
    m_city_isSet = !json[QString("City")].isNull() && m_city_isValid;

    m_conference_isValid = ::OpenAPI::fromJsonValue(m_conference, json[QString("Conference")]);
    m_conference_isSet = !json[QString("Conference")].isNull() && m_conference_isValid;

    m_division_isValid = ::OpenAPI::fromJsonValue(m_division, json[QString("Division")]);
    m_division_isSet = !json[QString("Division")].isNull() && m_division_isValid;

    m_global_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_team_id, json[QString("GlobalTeamID")]);
    m_global_team_id_isSet = !json[QString("GlobalTeamID")].isNull() && m_global_team_id_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("Key")]);
    m_key_isSet = !json[QString("Key")].isNull() && m_key_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_primary_color_isValid = ::OpenAPI::fromJsonValue(m_primary_color, json[QString("PrimaryColor")]);
    m_primary_color_isSet = !json[QString("PrimaryColor")].isNull() && m_primary_color_isValid;

    m_quaternary_color_isValid = ::OpenAPI::fromJsonValue(m_quaternary_color, json[QString("QuaternaryColor")]);
    m_quaternary_color_isSet = !json[QString("QuaternaryColor")].isNull() && m_quaternary_color_isValid;

    m_secondary_color_isValid = ::OpenAPI::fromJsonValue(m_secondary_color, json[QString("SecondaryColor")]);
    m_secondary_color_isSet = !json[QString("SecondaryColor")].isNull() && m_secondary_color_isValid;

    m_stadium_id_isValid = ::OpenAPI::fromJsonValue(m_stadium_id, json[QString("StadiumID")]);
    m_stadium_id_isSet = !json[QString("StadiumID")].isNull() && m_stadium_id_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;

    m_tertiary_color_isValid = ::OpenAPI::fromJsonValue(m_tertiary_color, json[QString("TertiaryColor")]);
    m_tertiary_color_isSet = !json[QString("TertiaryColor")].isNull() && m_tertiary_color_isValid;

    m_wikipedia_logo_url_isValid = ::OpenAPI::fromJsonValue(m_wikipedia_logo_url, json[QString("WikipediaLogoUrl")]);
    m_wikipedia_logo_url_isSet = !json[QString("WikipediaLogoUrl")].isNull() && m_wikipedia_logo_url_isValid;

    m_wikipedia_word_mark_url_isValid = ::OpenAPI::fromJsonValue(m_wikipedia_word_mark_url, json[QString("WikipediaWordMarkUrl")]);
    m_wikipedia_word_mark_url_isSet = !json[QString("WikipediaWordMarkUrl")].isNull() && m_wikipedia_word_mark_url_isValid;
}

QString OAITeam::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITeam::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("Active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_city_isSet) {
        obj.insert(QString("City"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_conference_isSet) {
        obj.insert(QString("Conference"), ::OpenAPI::toJsonValue(m_conference));
    }
    if (m_division_isSet) {
        obj.insert(QString("Division"), ::OpenAPI::toJsonValue(m_division));
    }
    if (m_global_team_id_isSet) {
        obj.insert(QString("GlobalTeamID"), ::OpenAPI::toJsonValue(m_global_team_id));
    }
    if (m_key_isSet) {
        obj.insert(QString("Key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_primary_color_isSet) {
        obj.insert(QString("PrimaryColor"), ::OpenAPI::toJsonValue(m_primary_color));
    }
    if (m_quaternary_color_isSet) {
        obj.insert(QString("QuaternaryColor"), ::OpenAPI::toJsonValue(m_quaternary_color));
    }
    if (m_secondary_color_isSet) {
        obj.insert(QString("SecondaryColor"), ::OpenAPI::toJsonValue(m_secondary_color));
    }
    if (m_stadium_id_isSet) {
        obj.insert(QString("StadiumID"), ::OpenAPI::toJsonValue(m_stadium_id));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_tertiary_color_isSet) {
        obj.insert(QString("TertiaryColor"), ::OpenAPI::toJsonValue(m_tertiary_color));
    }
    if (m_wikipedia_logo_url_isSet) {
        obj.insert(QString("WikipediaLogoUrl"), ::OpenAPI::toJsonValue(m_wikipedia_logo_url));
    }
    if (m_wikipedia_word_mark_url_isSet) {
        obj.insert(QString("WikipediaWordMarkUrl"), ::OpenAPI::toJsonValue(m_wikipedia_word_mark_url));
    }
    return obj;
}

bool OAITeam::isActive() const {
    return m_active;
}
void OAITeam::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAITeam::is_active_Set() const{
    return m_active_isSet;
}

bool OAITeam::is_active_Valid() const{
    return m_active_isValid;
}

QString OAITeam::getCity() const {
    return m_city;
}
void OAITeam::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAITeam::is_city_Set() const{
    return m_city_isSet;
}

bool OAITeam::is_city_Valid() const{
    return m_city_isValid;
}

QString OAITeam::getConference() const {
    return m_conference;
}
void OAITeam::setConference(const QString &conference) {
    m_conference = conference;
    m_conference_isSet = true;
}

bool OAITeam::is_conference_Set() const{
    return m_conference_isSet;
}

bool OAITeam::is_conference_Valid() const{
    return m_conference_isValid;
}

QString OAITeam::getDivision() const {
    return m_division;
}
void OAITeam::setDivision(const QString &division) {
    m_division = division;
    m_division_isSet = true;
}

bool OAITeam::is_division_Set() const{
    return m_division_isSet;
}

bool OAITeam::is_division_Valid() const{
    return m_division_isValid;
}

qint32 OAITeam::getGlobalTeamId() const {
    return m_global_team_id;
}
void OAITeam::setGlobalTeamId(const qint32 &global_team_id) {
    m_global_team_id = global_team_id;
    m_global_team_id_isSet = true;
}

bool OAITeam::is_global_team_id_Set() const{
    return m_global_team_id_isSet;
}

bool OAITeam::is_global_team_id_Valid() const{
    return m_global_team_id_isValid;
}

QString OAITeam::getKey() const {
    return m_key;
}
void OAITeam::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAITeam::is_key_Set() const{
    return m_key_isSet;
}

bool OAITeam::is_key_Valid() const{
    return m_key_isValid;
}

QString OAITeam::getName() const {
    return m_name;
}
void OAITeam::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITeam::is_name_Set() const{
    return m_name_isSet;
}

bool OAITeam::is_name_Valid() const{
    return m_name_isValid;
}

QString OAITeam::getPrimaryColor() const {
    return m_primary_color;
}
void OAITeam::setPrimaryColor(const QString &primary_color) {
    m_primary_color = primary_color;
    m_primary_color_isSet = true;
}

bool OAITeam::is_primary_color_Set() const{
    return m_primary_color_isSet;
}

bool OAITeam::is_primary_color_Valid() const{
    return m_primary_color_isValid;
}

QString OAITeam::getQuaternaryColor() const {
    return m_quaternary_color;
}
void OAITeam::setQuaternaryColor(const QString &quaternary_color) {
    m_quaternary_color = quaternary_color;
    m_quaternary_color_isSet = true;
}

bool OAITeam::is_quaternary_color_Set() const{
    return m_quaternary_color_isSet;
}

bool OAITeam::is_quaternary_color_Valid() const{
    return m_quaternary_color_isValid;
}

QString OAITeam::getSecondaryColor() const {
    return m_secondary_color;
}
void OAITeam::setSecondaryColor(const QString &secondary_color) {
    m_secondary_color = secondary_color;
    m_secondary_color_isSet = true;
}

bool OAITeam::is_secondary_color_Set() const{
    return m_secondary_color_isSet;
}

bool OAITeam::is_secondary_color_Valid() const{
    return m_secondary_color_isValid;
}

qint32 OAITeam::getStadiumId() const {
    return m_stadium_id;
}
void OAITeam::setStadiumId(const qint32 &stadium_id) {
    m_stadium_id = stadium_id;
    m_stadium_id_isSet = true;
}

bool OAITeam::is_stadium_id_Set() const{
    return m_stadium_id_isSet;
}

bool OAITeam::is_stadium_id_Valid() const{
    return m_stadium_id_isValid;
}

qint32 OAITeam::getTeamId() const {
    return m_team_id;
}
void OAITeam::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAITeam::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAITeam::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QString OAITeam::getTertiaryColor() const {
    return m_tertiary_color;
}
void OAITeam::setTertiaryColor(const QString &tertiary_color) {
    m_tertiary_color = tertiary_color;
    m_tertiary_color_isSet = true;
}

bool OAITeam::is_tertiary_color_Set() const{
    return m_tertiary_color_isSet;
}

bool OAITeam::is_tertiary_color_Valid() const{
    return m_tertiary_color_isValid;
}

QString OAITeam::getWikipediaLogoUrl() const {
    return m_wikipedia_logo_url;
}
void OAITeam::setWikipediaLogoUrl(const QString &wikipedia_logo_url) {
    m_wikipedia_logo_url = wikipedia_logo_url;
    m_wikipedia_logo_url_isSet = true;
}

bool OAITeam::is_wikipedia_logo_url_Set() const{
    return m_wikipedia_logo_url_isSet;
}

bool OAITeam::is_wikipedia_logo_url_Valid() const{
    return m_wikipedia_logo_url_isValid;
}

QString OAITeam::getWikipediaWordMarkUrl() const {
    return m_wikipedia_word_mark_url;
}
void OAITeam::setWikipediaWordMarkUrl(const QString &wikipedia_word_mark_url) {
    m_wikipedia_word_mark_url = wikipedia_word_mark_url;
    m_wikipedia_word_mark_url_isSet = true;
}

bool OAITeam::is_wikipedia_word_mark_url_Set() const{
    return m_wikipedia_word_mark_url_isSet;
}

bool OAITeam::is_wikipedia_word_mark_url_Valid() const{
    return m_wikipedia_word_mark_url_isValid;
}

bool OAITeam::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quaternary_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stadium_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tertiary_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wikipedia_logo_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wikipedia_word_mark_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITeam::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
