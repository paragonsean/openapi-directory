/**
 * Golf v2
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlayer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayer::OAIPlayer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayer::OAIPlayer() {
    this->initializeModel();
}

OAIPlayer::~OAIPlayer() {}

void OAIPlayer::initializeModel() {

    m_birth_city_isSet = false;
    m_birth_city_isValid = false;

    m_birth_date_isSet = false;
    m_birth_date_isValid = false;

    m_birth_state_isSet = false;
    m_birth_state_isValid = false;

    m_college_isSet = false;
    m_college_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_draft_kings_name_isSet = false;
    m_draft_kings_name_isValid = false;

    m_draft_kings_player_id_isSet = false;
    m_draft_kings_player_id_isValid = false;

    m_fan_duel_name_isSet = false;
    m_fan_duel_name_isValid = false;

    m_fan_duel_player_id_isSet = false;
    m_fan_duel_player_id_isValid = false;

    m_fantasy_alarm_player_id_isSet = false;
    m_fantasy_alarm_player_id_isValid = false;

    m_fantasy_draft_name_isSet = false;
    m_fantasy_draft_name_isValid = false;

    m_fantasy_draft_player_id_isSet = false;
    m_fantasy_draft_player_id_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_pga_debut_isSet = false;
    m_pga_debut_isValid = false;

    m_pga_tour_player_id_isSet = false;
    m_pga_tour_player_id_isValid = false;

    m_photo_url_isSet = false;
    m_photo_url_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_roto_wire_player_id_isSet = false;
    m_roto_wire_player_id_isValid = false;

    m_rotoworld_player_id_isSet = false;
    m_rotoworld_player_id_isValid = false;

    m_sport_radar_player_id_isSet = false;
    m_sport_radar_player_id_isValid = false;

    m_swings_isSet = false;
    m_swings_isValid = false;

    m_weight_isSet = false;
    m_weight_isValid = false;

    m_yahoo_player_id_isSet = false;
    m_yahoo_player_id_isValid = false;
}

void OAIPlayer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayer::fromJsonObject(QJsonObject json) {

    m_birth_city_isValid = ::OpenAPI::fromJsonValue(m_birth_city, json[QString("BirthCity")]);
    m_birth_city_isSet = !json[QString("BirthCity")].isNull() && m_birth_city_isValid;

    m_birth_date_isValid = ::OpenAPI::fromJsonValue(m_birth_date, json[QString("BirthDate")]);
    m_birth_date_isSet = !json[QString("BirthDate")].isNull() && m_birth_date_isValid;

    m_birth_state_isValid = ::OpenAPI::fromJsonValue(m_birth_state, json[QString("BirthState")]);
    m_birth_state_isSet = !json[QString("BirthState")].isNull() && m_birth_state_isValid;

    m_college_isValid = ::OpenAPI::fromJsonValue(m_college, json[QString("College")]);
    m_college_isSet = !json[QString("College")].isNull() && m_college_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("Country")]);
    m_country_isSet = !json[QString("Country")].isNull() && m_country_isValid;

    m_draft_kings_name_isValid = ::OpenAPI::fromJsonValue(m_draft_kings_name, json[QString("DraftKingsName")]);
    m_draft_kings_name_isSet = !json[QString("DraftKingsName")].isNull() && m_draft_kings_name_isValid;

    m_draft_kings_player_id_isValid = ::OpenAPI::fromJsonValue(m_draft_kings_player_id, json[QString("DraftKingsPlayerID")]);
    m_draft_kings_player_id_isSet = !json[QString("DraftKingsPlayerID")].isNull() && m_draft_kings_player_id_isValid;

    m_fan_duel_name_isValid = ::OpenAPI::fromJsonValue(m_fan_duel_name, json[QString("FanDuelName")]);
    m_fan_duel_name_isSet = !json[QString("FanDuelName")].isNull() && m_fan_duel_name_isValid;

    m_fan_duel_player_id_isValid = ::OpenAPI::fromJsonValue(m_fan_duel_player_id, json[QString("FanDuelPlayerID")]);
    m_fan_duel_player_id_isSet = !json[QString("FanDuelPlayerID")].isNull() && m_fan_duel_player_id_isValid;

    m_fantasy_alarm_player_id_isValid = ::OpenAPI::fromJsonValue(m_fantasy_alarm_player_id, json[QString("FantasyAlarmPlayerID")]);
    m_fantasy_alarm_player_id_isSet = !json[QString("FantasyAlarmPlayerID")].isNull() && m_fantasy_alarm_player_id_isValid;

    m_fantasy_draft_name_isValid = ::OpenAPI::fromJsonValue(m_fantasy_draft_name, json[QString("FantasyDraftName")]);
    m_fantasy_draft_name_isSet = !json[QString("FantasyDraftName")].isNull() && m_fantasy_draft_name_isValid;

    m_fantasy_draft_player_id_isValid = ::OpenAPI::fromJsonValue(m_fantasy_draft_player_id, json[QString("FantasyDraftPlayerID")]);
    m_fantasy_draft_player_id_isSet = !json[QString("FantasyDraftPlayerID")].isNull() && m_fantasy_draft_player_id_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("FirstName")]);
    m_first_name_isSet = !json[QString("FirstName")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("LastName")]);
    m_last_name_isSet = !json[QString("LastName")].isNull() && m_last_name_isValid;

    m_pga_debut_isValid = ::OpenAPI::fromJsonValue(m_pga_debut, json[QString("PgaDebut")]);
    m_pga_debut_isSet = !json[QString("PgaDebut")].isNull() && m_pga_debut_isValid;

    m_pga_tour_player_id_isValid = ::OpenAPI::fromJsonValue(m_pga_tour_player_id, json[QString("PgaTourPlayerID")]);
    m_pga_tour_player_id_isSet = !json[QString("PgaTourPlayerID")].isNull() && m_pga_tour_player_id_isValid;

    m_photo_url_isValid = ::OpenAPI::fromJsonValue(m_photo_url, json[QString("PhotoUrl")]);
    m_photo_url_isSet = !json[QString("PhotoUrl")].isNull() && m_photo_url_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_roto_wire_player_id_isValid = ::OpenAPI::fromJsonValue(m_roto_wire_player_id, json[QString("RotoWirePlayerID")]);
    m_roto_wire_player_id_isSet = !json[QString("RotoWirePlayerID")].isNull() && m_roto_wire_player_id_isValid;

    m_rotoworld_player_id_isValid = ::OpenAPI::fromJsonValue(m_rotoworld_player_id, json[QString("RotoworldPlayerID")]);
    m_rotoworld_player_id_isSet = !json[QString("RotoworldPlayerID")].isNull() && m_rotoworld_player_id_isValid;

    m_sport_radar_player_id_isValid = ::OpenAPI::fromJsonValue(m_sport_radar_player_id, json[QString("SportRadarPlayerID")]);
    m_sport_radar_player_id_isSet = !json[QString("SportRadarPlayerID")].isNull() && m_sport_radar_player_id_isValid;

    m_swings_isValid = ::OpenAPI::fromJsonValue(m_swings, json[QString("Swings")]);
    m_swings_isSet = !json[QString("Swings")].isNull() && m_swings_isValid;

    m_weight_isValid = ::OpenAPI::fromJsonValue(m_weight, json[QString("Weight")]);
    m_weight_isSet = !json[QString("Weight")].isNull() && m_weight_isValid;

    m_yahoo_player_id_isValid = ::OpenAPI::fromJsonValue(m_yahoo_player_id, json[QString("YahooPlayerID")]);
    m_yahoo_player_id_isSet = !json[QString("YahooPlayerID")].isNull() && m_yahoo_player_id_isValid;
}

QString OAIPlayer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayer::asJsonObject() const {
    QJsonObject obj;
    if (m_birth_city_isSet) {
        obj.insert(QString("BirthCity"), ::OpenAPI::toJsonValue(m_birth_city));
    }
    if (m_birth_date_isSet) {
        obj.insert(QString("BirthDate"), ::OpenAPI::toJsonValue(m_birth_date));
    }
    if (m_birth_state_isSet) {
        obj.insert(QString("BirthState"), ::OpenAPI::toJsonValue(m_birth_state));
    }
    if (m_college_isSet) {
        obj.insert(QString("College"), ::OpenAPI::toJsonValue(m_college));
    }
    if (m_country_isSet) {
        obj.insert(QString("Country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_draft_kings_name_isSet) {
        obj.insert(QString("DraftKingsName"), ::OpenAPI::toJsonValue(m_draft_kings_name));
    }
    if (m_draft_kings_player_id_isSet) {
        obj.insert(QString("DraftKingsPlayerID"), ::OpenAPI::toJsonValue(m_draft_kings_player_id));
    }
    if (m_fan_duel_name_isSet) {
        obj.insert(QString("FanDuelName"), ::OpenAPI::toJsonValue(m_fan_duel_name));
    }
    if (m_fan_duel_player_id_isSet) {
        obj.insert(QString("FanDuelPlayerID"), ::OpenAPI::toJsonValue(m_fan_duel_player_id));
    }
    if (m_fantasy_alarm_player_id_isSet) {
        obj.insert(QString("FantasyAlarmPlayerID"), ::OpenAPI::toJsonValue(m_fantasy_alarm_player_id));
    }
    if (m_fantasy_draft_name_isSet) {
        obj.insert(QString("FantasyDraftName"), ::OpenAPI::toJsonValue(m_fantasy_draft_name));
    }
    if (m_fantasy_draft_player_id_isSet) {
        obj.insert(QString("FantasyDraftPlayerID"), ::OpenAPI::toJsonValue(m_fantasy_draft_player_id));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("FirstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("LastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_pga_debut_isSet) {
        obj.insert(QString("PgaDebut"), ::OpenAPI::toJsonValue(m_pga_debut));
    }
    if (m_pga_tour_player_id_isSet) {
        obj.insert(QString("PgaTourPlayerID"), ::OpenAPI::toJsonValue(m_pga_tour_player_id));
    }
    if (m_photo_url_isSet) {
        obj.insert(QString("PhotoUrl"), ::OpenAPI::toJsonValue(m_photo_url));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_roto_wire_player_id_isSet) {
        obj.insert(QString("RotoWirePlayerID"), ::OpenAPI::toJsonValue(m_roto_wire_player_id));
    }
    if (m_rotoworld_player_id_isSet) {
        obj.insert(QString("RotoworldPlayerID"), ::OpenAPI::toJsonValue(m_rotoworld_player_id));
    }
    if (m_sport_radar_player_id_isSet) {
        obj.insert(QString("SportRadarPlayerID"), ::OpenAPI::toJsonValue(m_sport_radar_player_id));
    }
    if (m_swings_isSet) {
        obj.insert(QString("Swings"), ::OpenAPI::toJsonValue(m_swings));
    }
    if (m_weight_isSet) {
        obj.insert(QString("Weight"), ::OpenAPI::toJsonValue(m_weight));
    }
    if (m_yahoo_player_id_isSet) {
        obj.insert(QString("YahooPlayerID"), ::OpenAPI::toJsonValue(m_yahoo_player_id));
    }
    return obj;
}

QString OAIPlayer::getBirthCity() const {
    return m_birth_city;
}
void OAIPlayer::setBirthCity(const QString &birth_city) {
    m_birth_city = birth_city;
    m_birth_city_isSet = true;
}

bool OAIPlayer::is_birth_city_Set() const{
    return m_birth_city_isSet;
}

bool OAIPlayer::is_birth_city_Valid() const{
    return m_birth_city_isValid;
}

QString OAIPlayer::getBirthDate() const {
    return m_birth_date;
}
void OAIPlayer::setBirthDate(const QString &birth_date) {
    m_birth_date = birth_date;
    m_birth_date_isSet = true;
}

bool OAIPlayer::is_birth_date_Set() const{
    return m_birth_date_isSet;
}

bool OAIPlayer::is_birth_date_Valid() const{
    return m_birth_date_isValid;
}

QString OAIPlayer::getBirthState() const {
    return m_birth_state;
}
void OAIPlayer::setBirthState(const QString &birth_state) {
    m_birth_state = birth_state;
    m_birth_state_isSet = true;
}

bool OAIPlayer::is_birth_state_Set() const{
    return m_birth_state_isSet;
}

bool OAIPlayer::is_birth_state_Valid() const{
    return m_birth_state_isValid;
}

QString OAIPlayer::getCollege() const {
    return m_college;
}
void OAIPlayer::setCollege(const QString &college) {
    m_college = college;
    m_college_isSet = true;
}

bool OAIPlayer::is_college_Set() const{
    return m_college_isSet;
}

bool OAIPlayer::is_college_Valid() const{
    return m_college_isValid;
}

QString OAIPlayer::getCountry() const {
    return m_country;
}
void OAIPlayer::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIPlayer::is_country_Set() const{
    return m_country_isSet;
}

bool OAIPlayer::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIPlayer::getDraftKingsName() const {
    return m_draft_kings_name;
}
void OAIPlayer::setDraftKingsName(const QString &draft_kings_name) {
    m_draft_kings_name = draft_kings_name;
    m_draft_kings_name_isSet = true;
}

bool OAIPlayer::is_draft_kings_name_Set() const{
    return m_draft_kings_name_isSet;
}

bool OAIPlayer::is_draft_kings_name_Valid() const{
    return m_draft_kings_name_isValid;
}

qint32 OAIPlayer::getDraftKingsPlayerId() const {
    return m_draft_kings_player_id;
}
void OAIPlayer::setDraftKingsPlayerId(const qint32 &draft_kings_player_id) {
    m_draft_kings_player_id = draft_kings_player_id;
    m_draft_kings_player_id_isSet = true;
}

bool OAIPlayer::is_draft_kings_player_id_Set() const{
    return m_draft_kings_player_id_isSet;
}

bool OAIPlayer::is_draft_kings_player_id_Valid() const{
    return m_draft_kings_player_id_isValid;
}

QString OAIPlayer::getFanDuelName() const {
    return m_fan_duel_name;
}
void OAIPlayer::setFanDuelName(const QString &fan_duel_name) {
    m_fan_duel_name = fan_duel_name;
    m_fan_duel_name_isSet = true;
}

bool OAIPlayer::is_fan_duel_name_Set() const{
    return m_fan_duel_name_isSet;
}

bool OAIPlayer::is_fan_duel_name_Valid() const{
    return m_fan_duel_name_isValid;
}

qint32 OAIPlayer::getFanDuelPlayerId() const {
    return m_fan_duel_player_id;
}
void OAIPlayer::setFanDuelPlayerId(const qint32 &fan_duel_player_id) {
    m_fan_duel_player_id = fan_duel_player_id;
    m_fan_duel_player_id_isSet = true;
}

bool OAIPlayer::is_fan_duel_player_id_Set() const{
    return m_fan_duel_player_id_isSet;
}

bool OAIPlayer::is_fan_duel_player_id_Valid() const{
    return m_fan_duel_player_id_isValid;
}

qint32 OAIPlayer::getFantasyAlarmPlayerId() const {
    return m_fantasy_alarm_player_id;
}
void OAIPlayer::setFantasyAlarmPlayerId(const qint32 &fantasy_alarm_player_id) {
    m_fantasy_alarm_player_id = fantasy_alarm_player_id;
    m_fantasy_alarm_player_id_isSet = true;
}

bool OAIPlayer::is_fantasy_alarm_player_id_Set() const{
    return m_fantasy_alarm_player_id_isSet;
}

bool OAIPlayer::is_fantasy_alarm_player_id_Valid() const{
    return m_fantasy_alarm_player_id_isValid;
}

QString OAIPlayer::getFantasyDraftName() const {
    return m_fantasy_draft_name;
}
void OAIPlayer::setFantasyDraftName(const QString &fantasy_draft_name) {
    m_fantasy_draft_name = fantasy_draft_name;
    m_fantasy_draft_name_isSet = true;
}

bool OAIPlayer::is_fantasy_draft_name_Set() const{
    return m_fantasy_draft_name_isSet;
}

bool OAIPlayer::is_fantasy_draft_name_Valid() const{
    return m_fantasy_draft_name_isValid;
}

qint32 OAIPlayer::getFantasyDraftPlayerId() const {
    return m_fantasy_draft_player_id;
}
void OAIPlayer::setFantasyDraftPlayerId(const qint32 &fantasy_draft_player_id) {
    m_fantasy_draft_player_id = fantasy_draft_player_id;
    m_fantasy_draft_player_id_isSet = true;
}

bool OAIPlayer::is_fantasy_draft_player_id_Set() const{
    return m_fantasy_draft_player_id_isSet;
}

bool OAIPlayer::is_fantasy_draft_player_id_Valid() const{
    return m_fantasy_draft_player_id_isValid;
}

QString OAIPlayer::getFirstName() const {
    return m_first_name;
}
void OAIPlayer::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIPlayer::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIPlayer::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIPlayer::getLastName() const {
    return m_last_name;
}
void OAIPlayer::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIPlayer::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIPlayer::is_last_name_Valid() const{
    return m_last_name_isValid;
}

qint32 OAIPlayer::getPgaDebut() const {
    return m_pga_debut;
}
void OAIPlayer::setPgaDebut(const qint32 &pga_debut) {
    m_pga_debut = pga_debut;
    m_pga_debut_isSet = true;
}

bool OAIPlayer::is_pga_debut_Set() const{
    return m_pga_debut_isSet;
}

bool OAIPlayer::is_pga_debut_Valid() const{
    return m_pga_debut_isValid;
}

qint32 OAIPlayer::getPgaTourPlayerId() const {
    return m_pga_tour_player_id;
}
void OAIPlayer::setPgaTourPlayerId(const qint32 &pga_tour_player_id) {
    m_pga_tour_player_id = pga_tour_player_id;
    m_pga_tour_player_id_isSet = true;
}

bool OAIPlayer::is_pga_tour_player_id_Set() const{
    return m_pga_tour_player_id_isSet;
}

bool OAIPlayer::is_pga_tour_player_id_Valid() const{
    return m_pga_tour_player_id_isValid;
}

QString OAIPlayer::getPhotoUrl() const {
    return m_photo_url;
}
void OAIPlayer::setPhotoUrl(const QString &photo_url) {
    m_photo_url = photo_url;
    m_photo_url_isSet = true;
}

bool OAIPlayer::is_photo_url_Set() const{
    return m_photo_url_isSet;
}

bool OAIPlayer::is_photo_url_Valid() const{
    return m_photo_url_isValid;
}

qint32 OAIPlayer::getPlayerId() const {
    return m_player_id;
}
void OAIPlayer::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIPlayer::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIPlayer::is_player_id_Valid() const{
    return m_player_id_isValid;
}

qint32 OAIPlayer::getRotoWirePlayerId() const {
    return m_roto_wire_player_id;
}
void OAIPlayer::setRotoWirePlayerId(const qint32 &roto_wire_player_id) {
    m_roto_wire_player_id = roto_wire_player_id;
    m_roto_wire_player_id_isSet = true;
}

bool OAIPlayer::is_roto_wire_player_id_Set() const{
    return m_roto_wire_player_id_isSet;
}

bool OAIPlayer::is_roto_wire_player_id_Valid() const{
    return m_roto_wire_player_id_isValid;
}

qint32 OAIPlayer::getRotoworldPlayerId() const {
    return m_rotoworld_player_id;
}
void OAIPlayer::setRotoworldPlayerId(const qint32 &rotoworld_player_id) {
    m_rotoworld_player_id = rotoworld_player_id;
    m_rotoworld_player_id_isSet = true;
}

bool OAIPlayer::is_rotoworld_player_id_Set() const{
    return m_rotoworld_player_id_isSet;
}

bool OAIPlayer::is_rotoworld_player_id_Valid() const{
    return m_rotoworld_player_id_isValid;
}

QString OAIPlayer::getSportRadarPlayerId() const {
    return m_sport_radar_player_id;
}
void OAIPlayer::setSportRadarPlayerId(const QString &sport_radar_player_id) {
    m_sport_radar_player_id = sport_radar_player_id;
    m_sport_radar_player_id_isSet = true;
}

bool OAIPlayer::is_sport_radar_player_id_Set() const{
    return m_sport_radar_player_id_isSet;
}

bool OAIPlayer::is_sport_radar_player_id_Valid() const{
    return m_sport_radar_player_id_isValid;
}

QString OAIPlayer::getSwings() const {
    return m_swings;
}
void OAIPlayer::setSwings(const QString &swings) {
    m_swings = swings;
    m_swings_isSet = true;
}

bool OAIPlayer::is_swings_Set() const{
    return m_swings_isSet;
}

bool OAIPlayer::is_swings_Valid() const{
    return m_swings_isValid;
}

qint32 OAIPlayer::getWeight() const {
    return m_weight;
}
void OAIPlayer::setWeight(const qint32 &weight) {
    m_weight = weight;
    m_weight_isSet = true;
}

bool OAIPlayer::is_weight_Set() const{
    return m_weight_isSet;
}

bool OAIPlayer::is_weight_Valid() const{
    return m_weight_isValid;
}

qint32 OAIPlayer::getYahooPlayerId() const {
    return m_yahoo_player_id;
}
void OAIPlayer::setYahooPlayerId(const qint32 &yahoo_player_id) {
    m_yahoo_player_id = yahoo_player_id;
    m_yahoo_player_id_isSet = true;
}

bool OAIPlayer::is_yahoo_player_id_Set() const{
    return m_yahoo_player_id_isSet;
}

bool OAIPlayer::is_yahoo_player_id_Valid() const{
    return m_yahoo_player_id_isValid;
}

bool OAIPlayer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_birth_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_college_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_draft_kings_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_draft_kings_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fan_duel_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fan_duel_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fantasy_alarm_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fantasy_draft_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fantasy_draft_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pga_debut_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pga_tour_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_photo_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_roto_wire_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotoworld_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sport_radar_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_swings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_yahoo_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlayer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
