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

    m_birth_country_isSet = false;
    m_birth_country_isValid = false;

    m_birth_date_isSet = false;
    m_birth_date_isValid = false;

    m_common_name_isSet = false;
    m_common_name_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_match_name_isSet = false;
    m_match_name_isValid = false;

    m_nationality_isSet = false;
    m_nationality_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
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

    m_birth_country_isValid = ::OpenAPI::fromJsonValue(m_birth_country, json[QString("BirthCountry")]);
    m_birth_country_isSet = !json[QString("BirthCountry")].isNull() && m_birth_country_isValid;

    m_birth_date_isValid = ::OpenAPI::fromJsonValue(m_birth_date, json[QString("BirthDate")]);
    m_birth_date_isSet = !json[QString("BirthDate")].isNull() && m_birth_date_isValid;

    m_common_name_isValid = ::OpenAPI::fromJsonValue(m_common_name, json[QString("CommonName")]);
    m_common_name_isSet = !json[QString("CommonName")].isNull() && m_common_name_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("FirstName")]);
    m_first_name_isSet = !json[QString("FirstName")].isNull() && m_first_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("Gender")]);
    m_gender_isSet = !json[QString("Gender")].isNull() && m_gender_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("LastName")]);
    m_last_name_isSet = !json[QString("LastName")].isNull() && m_last_name_isValid;

    m_match_name_isValid = ::OpenAPI::fromJsonValue(m_match_name, json[QString("MatchName")]);
    m_match_name_isSet = !json[QString("MatchName")].isNull() && m_match_name_isValid;

    m_nationality_isValid = ::OpenAPI::fromJsonValue(m_nationality, json[QString("Nationality")]);
    m_nationality_isSet = !json[QString("Nationality")].isNull() && m_nationality_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerId")]);
    m_player_id_isSet = !json[QString("PlayerId")].isNull() && m_player_id_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;
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
    if (m_birth_country_isSet) {
        obj.insert(QString("BirthCountry"), ::OpenAPI::toJsonValue(m_birth_country));
    }
    if (m_birth_date_isSet) {
        obj.insert(QString("BirthDate"), ::OpenAPI::toJsonValue(m_birth_date));
    }
    if (m_common_name_isSet) {
        obj.insert(QString("CommonName"), ::OpenAPI::toJsonValue(m_common_name));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("FirstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("Gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("LastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_match_name_isSet) {
        obj.insert(QString("MatchName"), ::OpenAPI::toJsonValue(m_match_name));
    }
    if (m_nationality_isSet) {
        obj.insert(QString("Nationality"), ::OpenAPI::toJsonValue(m_nationality));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerId"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_position_isSet) {
        obj.insert(QString("Position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
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

QString OAIPlayer::getBirthCountry() const {
    return m_birth_country;
}
void OAIPlayer::setBirthCountry(const QString &birth_country) {
    m_birth_country = birth_country;
    m_birth_country_isSet = true;
}

bool OAIPlayer::is_birth_country_Set() const{
    return m_birth_country_isSet;
}

bool OAIPlayer::is_birth_country_Valid() const{
    return m_birth_country_isValid;
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

QString OAIPlayer::getCommonName() const {
    return m_common_name;
}
void OAIPlayer::setCommonName(const QString &common_name) {
    m_common_name = common_name;
    m_common_name_isSet = true;
}

bool OAIPlayer::is_common_name_Set() const{
    return m_common_name_isSet;
}

bool OAIPlayer::is_common_name_Valid() const{
    return m_common_name_isValid;
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

QString OAIPlayer::getGender() const {
    return m_gender;
}
void OAIPlayer::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIPlayer::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIPlayer::is_gender_Valid() const{
    return m_gender_isValid;
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

QString OAIPlayer::getMatchName() const {
    return m_match_name;
}
void OAIPlayer::setMatchName(const QString &match_name) {
    m_match_name = match_name;
    m_match_name_isSet = true;
}

bool OAIPlayer::is_match_name_Set() const{
    return m_match_name_isSet;
}

bool OAIPlayer::is_match_name_Valid() const{
    return m_match_name_isValid;
}

QString OAIPlayer::getNationality() const {
    return m_nationality;
}
void OAIPlayer::setNationality(const QString &nationality) {
    m_nationality = nationality;
    m_nationality_isSet = true;
}

bool OAIPlayer::is_nationality_Set() const{
    return m_nationality_isSet;
}

bool OAIPlayer::is_nationality_Valid() const{
    return m_nationality_isValid;
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

QString OAIPlayer::getPosition() const {
    return m_position;
}
void OAIPlayer::setPosition(const QString &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIPlayer::is_position_Set() const{
    return m_position_isSet;
}

bool OAIPlayer::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIPlayer::getUpdated() const {
    return m_updated;
}
void OAIPlayer::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIPlayer::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIPlayer::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIPlayer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_birth_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_common_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_match_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nationality_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
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

bool OAIPlayer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
