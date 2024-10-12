/**
 * Soccer v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITeamDetail.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITeamDetail::OAITeamDetail(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITeamDetail::OAITeamDetail() {
    this->initializeModel();
}

OAITeamDetail::~OAITeamDetail() {}

void OAITeamDetail::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_address_isSet = false;
    m_address_isValid = false;

    m_area_id_isSet = false;
    m_area_id_isValid = false;

    m_area_name_isSet = false;
    m_area_name_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_club_color1_isSet = false;
    m_club_color1_isValid = false;

    m_club_color2_isSet = false;
    m_club_color2_isValid = false;

    m_club_color3_isSet = false;
    m_club_color3_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_fax_isSet = false;
    m_fax_isValid = false;

    m_founded_isSet = false;
    m_founded_isValid = false;

    m_full_name_isSet = false;
    m_full_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_global_team_id_isSet = false;
    m_global_team_id_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_nickname1_isSet = false;
    m_nickname1_isValid = false;

    m_nickname2_isSet = false;
    m_nickname2_isValid = false;

    m_nickname3_isSet = false;
    m_nickname3_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_players_isSet = false;
    m_players_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_venue_id_isSet = false;
    m_venue_id_isValid = false;

    m_venue_name_isSet = false;
    m_venue_name_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;

    m_wikipedia_logo_url_isSet = false;
    m_wikipedia_logo_url_isValid = false;

    m_wikipedia_word_mark_url_isSet = false;
    m_wikipedia_word_mark_url_isValid = false;

    m_zip_isSet = false;
    m_zip_isValid = false;
}

void OAITeamDetail::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITeamDetail::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("Active")]);
    m_active_isSet = !json[QString("Active")].isNull() && m_active_isValid;

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("Address")]);
    m_address_isSet = !json[QString("Address")].isNull() && m_address_isValid;

    m_area_id_isValid = ::OpenAPI::fromJsonValue(m_area_id, json[QString("AreaId")]);
    m_area_id_isSet = !json[QString("AreaId")].isNull() && m_area_id_isValid;

    m_area_name_isValid = ::OpenAPI::fromJsonValue(m_area_name, json[QString("AreaName")]);
    m_area_name_isSet = !json[QString("AreaName")].isNull() && m_area_name_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("City")]);
    m_city_isSet = !json[QString("City")].isNull() && m_city_isValid;

    m_club_color1_isValid = ::OpenAPI::fromJsonValue(m_club_color1, json[QString("ClubColor1")]);
    m_club_color1_isSet = !json[QString("ClubColor1")].isNull() && m_club_color1_isValid;

    m_club_color2_isValid = ::OpenAPI::fromJsonValue(m_club_color2, json[QString("ClubColor2")]);
    m_club_color2_isSet = !json[QString("ClubColor2")].isNull() && m_club_color2_isValid;

    m_club_color3_isValid = ::OpenAPI::fromJsonValue(m_club_color3, json[QString("ClubColor3")]);
    m_club_color3_isSet = !json[QString("ClubColor3")].isNull() && m_club_color3_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("Email")]);
    m_email_isSet = !json[QString("Email")].isNull() && m_email_isValid;

    m_fax_isValid = ::OpenAPI::fromJsonValue(m_fax, json[QString("Fax")]);
    m_fax_isSet = !json[QString("Fax")].isNull() && m_fax_isValid;

    m_founded_isValid = ::OpenAPI::fromJsonValue(m_founded, json[QString("Founded")]);
    m_founded_isSet = !json[QString("Founded")].isNull() && m_founded_isValid;

    m_full_name_isValid = ::OpenAPI::fromJsonValue(m_full_name, json[QString("FullName")]);
    m_full_name_isSet = !json[QString("FullName")].isNull() && m_full_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("Gender")]);
    m_gender_isSet = !json[QString("Gender")].isNull() && m_gender_isValid;

    m_global_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_team_id, json[QString("GlobalTeamId")]);
    m_global_team_id_isSet = !json[QString("GlobalTeamId")].isNull() && m_global_team_id_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("Key")]);
    m_key_isSet = !json[QString("Key")].isNull() && m_key_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_nickname1_isValid = ::OpenAPI::fromJsonValue(m_nickname1, json[QString("Nickname1")]);
    m_nickname1_isSet = !json[QString("Nickname1")].isNull() && m_nickname1_isValid;

    m_nickname2_isValid = ::OpenAPI::fromJsonValue(m_nickname2, json[QString("Nickname2")]);
    m_nickname2_isSet = !json[QString("Nickname2")].isNull() && m_nickname2_isValid;

    m_nickname3_isValid = ::OpenAPI::fromJsonValue(m_nickname3, json[QString("Nickname3")]);
    m_nickname3_isSet = !json[QString("Nickname3")].isNull() && m_nickname3_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("Phone")]);
    m_phone_isSet = !json[QString("Phone")].isNull() && m_phone_isValid;

    m_players_isValid = ::OpenAPI::fromJsonValue(m_players, json[QString("Players")]);
    m_players_isSet = !json[QString("Players")].isNull() && m_players_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamId")]);
    m_team_id_isSet = !json[QString("TeamId")].isNull() && m_team_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;

    m_venue_id_isValid = ::OpenAPI::fromJsonValue(m_venue_id, json[QString("VenueId")]);
    m_venue_id_isSet = !json[QString("VenueId")].isNull() && m_venue_id_isValid;

    m_venue_name_isValid = ::OpenAPI::fromJsonValue(m_venue_name, json[QString("VenueName")]);
    m_venue_name_isSet = !json[QString("VenueName")].isNull() && m_venue_name_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("Website")]);
    m_website_isSet = !json[QString("Website")].isNull() && m_website_isValid;

    m_wikipedia_logo_url_isValid = ::OpenAPI::fromJsonValue(m_wikipedia_logo_url, json[QString("WikipediaLogoUrl")]);
    m_wikipedia_logo_url_isSet = !json[QString("WikipediaLogoUrl")].isNull() && m_wikipedia_logo_url_isValid;

    m_wikipedia_word_mark_url_isValid = ::OpenAPI::fromJsonValue(m_wikipedia_word_mark_url, json[QString("WikipediaWordMarkUrl")]);
    m_wikipedia_word_mark_url_isSet = !json[QString("WikipediaWordMarkUrl")].isNull() && m_wikipedia_word_mark_url_isValid;

    m_zip_isValid = ::OpenAPI::fromJsonValue(m_zip, json[QString("Zip")]);
    m_zip_isSet = !json[QString("Zip")].isNull() && m_zip_isValid;
}

QString OAITeamDetail::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITeamDetail::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("Active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_address_isSet) {
        obj.insert(QString("Address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_area_id_isSet) {
        obj.insert(QString("AreaId"), ::OpenAPI::toJsonValue(m_area_id));
    }
    if (m_area_name_isSet) {
        obj.insert(QString("AreaName"), ::OpenAPI::toJsonValue(m_area_name));
    }
    if (m_city_isSet) {
        obj.insert(QString("City"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_club_color1_isSet) {
        obj.insert(QString("ClubColor1"), ::OpenAPI::toJsonValue(m_club_color1));
    }
    if (m_club_color2_isSet) {
        obj.insert(QString("ClubColor2"), ::OpenAPI::toJsonValue(m_club_color2));
    }
    if (m_club_color3_isSet) {
        obj.insert(QString("ClubColor3"), ::OpenAPI::toJsonValue(m_club_color3));
    }
    if (m_email_isSet) {
        obj.insert(QString("Email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_fax_isSet) {
        obj.insert(QString("Fax"), ::OpenAPI::toJsonValue(m_fax));
    }
    if (m_founded_isSet) {
        obj.insert(QString("Founded"), ::OpenAPI::toJsonValue(m_founded));
    }
    if (m_full_name_isSet) {
        obj.insert(QString("FullName"), ::OpenAPI::toJsonValue(m_full_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("Gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_global_team_id_isSet) {
        obj.insert(QString("GlobalTeamId"), ::OpenAPI::toJsonValue(m_global_team_id));
    }
    if (m_key_isSet) {
        obj.insert(QString("Key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_nickname1_isSet) {
        obj.insert(QString("Nickname1"), ::OpenAPI::toJsonValue(m_nickname1));
    }
    if (m_nickname2_isSet) {
        obj.insert(QString("Nickname2"), ::OpenAPI::toJsonValue(m_nickname2));
    }
    if (m_nickname3_isSet) {
        obj.insert(QString("Nickname3"), ::OpenAPI::toJsonValue(m_nickname3));
    }
    if (m_phone_isSet) {
        obj.insert(QString("Phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_players.size() > 0) {
        obj.insert(QString("Players"), ::OpenAPI::toJsonValue(m_players));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamId"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_venue_id_isSet) {
        obj.insert(QString("VenueId"), ::OpenAPI::toJsonValue(m_venue_id));
    }
    if (m_venue_name_isSet) {
        obj.insert(QString("VenueName"), ::OpenAPI::toJsonValue(m_venue_name));
    }
    if (m_website_isSet) {
        obj.insert(QString("Website"), ::OpenAPI::toJsonValue(m_website));
    }
    if (m_wikipedia_logo_url_isSet) {
        obj.insert(QString("WikipediaLogoUrl"), ::OpenAPI::toJsonValue(m_wikipedia_logo_url));
    }
    if (m_wikipedia_word_mark_url_isSet) {
        obj.insert(QString("WikipediaWordMarkUrl"), ::OpenAPI::toJsonValue(m_wikipedia_word_mark_url));
    }
    if (m_zip_isSet) {
        obj.insert(QString("Zip"), ::OpenAPI::toJsonValue(m_zip));
    }
    return obj;
}

bool OAITeamDetail::isActive() const {
    return m_active;
}
void OAITeamDetail::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAITeamDetail::is_active_Set() const{
    return m_active_isSet;
}

bool OAITeamDetail::is_active_Valid() const{
    return m_active_isValid;
}

QString OAITeamDetail::getAddress() const {
    return m_address;
}
void OAITeamDetail::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAITeamDetail::is_address_Set() const{
    return m_address_isSet;
}

bool OAITeamDetail::is_address_Valid() const{
    return m_address_isValid;
}

qint32 OAITeamDetail::getAreaId() const {
    return m_area_id;
}
void OAITeamDetail::setAreaId(const qint32 &area_id) {
    m_area_id = area_id;
    m_area_id_isSet = true;
}

bool OAITeamDetail::is_area_id_Set() const{
    return m_area_id_isSet;
}

bool OAITeamDetail::is_area_id_Valid() const{
    return m_area_id_isValid;
}

QString OAITeamDetail::getAreaName() const {
    return m_area_name;
}
void OAITeamDetail::setAreaName(const QString &area_name) {
    m_area_name = area_name;
    m_area_name_isSet = true;
}

bool OAITeamDetail::is_area_name_Set() const{
    return m_area_name_isSet;
}

bool OAITeamDetail::is_area_name_Valid() const{
    return m_area_name_isValid;
}

QString OAITeamDetail::getCity() const {
    return m_city;
}
void OAITeamDetail::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAITeamDetail::is_city_Set() const{
    return m_city_isSet;
}

bool OAITeamDetail::is_city_Valid() const{
    return m_city_isValid;
}

QString OAITeamDetail::getClubColor1() const {
    return m_club_color1;
}
void OAITeamDetail::setClubColor1(const QString &club_color1) {
    m_club_color1 = club_color1;
    m_club_color1_isSet = true;
}

bool OAITeamDetail::is_club_color1_Set() const{
    return m_club_color1_isSet;
}

bool OAITeamDetail::is_club_color1_Valid() const{
    return m_club_color1_isValid;
}

QString OAITeamDetail::getClubColor2() const {
    return m_club_color2;
}
void OAITeamDetail::setClubColor2(const QString &club_color2) {
    m_club_color2 = club_color2;
    m_club_color2_isSet = true;
}

bool OAITeamDetail::is_club_color2_Set() const{
    return m_club_color2_isSet;
}

bool OAITeamDetail::is_club_color2_Valid() const{
    return m_club_color2_isValid;
}

QString OAITeamDetail::getClubColor3() const {
    return m_club_color3;
}
void OAITeamDetail::setClubColor3(const QString &club_color3) {
    m_club_color3 = club_color3;
    m_club_color3_isSet = true;
}

bool OAITeamDetail::is_club_color3_Set() const{
    return m_club_color3_isSet;
}

bool OAITeamDetail::is_club_color3_Valid() const{
    return m_club_color3_isValid;
}

QString OAITeamDetail::getEmail() const {
    return m_email;
}
void OAITeamDetail::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAITeamDetail::is_email_Set() const{
    return m_email_isSet;
}

bool OAITeamDetail::is_email_Valid() const{
    return m_email_isValid;
}

QString OAITeamDetail::getFax() const {
    return m_fax;
}
void OAITeamDetail::setFax(const QString &fax) {
    m_fax = fax;
    m_fax_isSet = true;
}

bool OAITeamDetail::is_fax_Set() const{
    return m_fax_isSet;
}

bool OAITeamDetail::is_fax_Valid() const{
    return m_fax_isValid;
}

qint32 OAITeamDetail::getFounded() const {
    return m_founded;
}
void OAITeamDetail::setFounded(const qint32 &founded) {
    m_founded = founded;
    m_founded_isSet = true;
}

bool OAITeamDetail::is_founded_Set() const{
    return m_founded_isSet;
}

bool OAITeamDetail::is_founded_Valid() const{
    return m_founded_isValid;
}

QString OAITeamDetail::getFullName() const {
    return m_full_name;
}
void OAITeamDetail::setFullName(const QString &full_name) {
    m_full_name = full_name;
    m_full_name_isSet = true;
}

bool OAITeamDetail::is_full_name_Set() const{
    return m_full_name_isSet;
}

bool OAITeamDetail::is_full_name_Valid() const{
    return m_full_name_isValid;
}

QString OAITeamDetail::getGender() const {
    return m_gender;
}
void OAITeamDetail::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAITeamDetail::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAITeamDetail::is_gender_Valid() const{
    return m_gender_isValid;
}

qint32 OAITeamDetail::getGlobalTeamId() const {
    return m_global_team_id;
}
void OAITeamDetail::setGlobalTeamId(const qint32 &global_team_id) {
    m_global_team_id = global_team_id;
    m_global_team_id_isSet = true;
}

bool OAITeamDetail::is_global_team_id_Set() const{
    return m_global_team_id_isSet;
}

bool OAITeamDetail::is_global_team_id_Valid() const{
    return m_global_team_id_isValid;
}

QString OAITeamDetail::getKey() const {
    return m_key;
}
void OAITeamDetail::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAITeamDetail::is_key_Set() const{
    return m_key_isSet;
}

bool OAITeamDetail::is_key_Valid() const{
    return m_key_isValid;
}

QString OAITeamDetail::getName() const {
    return m_name;
}
void OAITeamDetail::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITeamDetail::is_name_Set() const{
    return m_name_isSet;
}

bool OAITeamDetail::is_name_Valid() const{
    return m_name_isValid;
}

QString OAITeamDetail::getNickname1() const {
    return m_nickname1;
}
void OAITeamDetail::setNickname1(const QString &nickname1) {
    m_nickname1 = nickname1;
    m_nickname1_isSet = true;
}

bool OAITeamDetail::is_nickname1_Set() const{
    return m_nickname1_isSet;
}

bool OAITeamDetail::is_nickname1_Valid() const{
    return m_nickname1_isValid;
}

QString OAITeamDetail::getNickname2() const {
    return m_nickname2;
}
void OAITeamDetail::setNickname2(const QString &nickname2) {
    m_nickname2 = nickname2;
    m_nickname2_isSet = true;
}

bool OAITeamDetail::is_nickname2_Set() const{
    return m_nickname2_isSet;
}

bool OAITeamDetail::is_nickname2_Valid() const{
    return m_nickname2_isValid;
}

QString OAITeamDetail::getNickname3() const {
    return m_nickname3;
}
void OAITeamDetail::setNickname3(const QString &nickname3) {
    m_nickname3 = nickname3;
    m_nickname3_isSet = true;
}

bool OAITeamDetail::is_nickname3_Set() const{
    return m_nickname3_isSet;
}

bool OAITeamDetail::is_nickname3_Valid() const{
    return m_nickname3_isValid;
}

QString OAITeamDetail::getPhone() const {
    return m_phone;
}
void OAITeamDetail::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAITeamDetail::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAITeamDetail::is_phone_Valid() const{
    return m_phone_isValid;
}

QList<OAIPlayer> OAITeamDetail::getPlayers() const {
    return m_players;
}
void OAITeamDetail::setPlayers(const QList<OAIPlayer> &players) {
    m_players = players;
    m_players_isSet = true;
}

bool OAITeamDetail::is_players_Set() const{
    return m_players_isSet;
}

bool OAITeamDetail::is_players_Valid() const{
    return m_players_isValid;
}

qint32 OAITeamDetail::getTeamId() const {
    return m_team_id;
}
void OAITeamDetail::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAITeamDetail::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAITeamDetail::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QString OAITeamDetail::getType() const {
    return m_type;
}
void OAITeamDetail::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITeamDetail::is_type_Set() const{
    return m_type_isSet;
}

bool OAITeamDetail::is_type_Valid() const{
    return m_type_isValid;
}

qint32 OAITeamDetail::getVenueId() const {
    return m_venue_id;
}
void OAITeamDetail::setVenueId(const qint32 &venue_id) {
    m_venue_id = venue_id;
    m_venue_id_isSet = true;
}

bool OAITeamDetail::is_venue_id_Set() const{
    return m_venue_id_isSet;
}

bool OAITeamDetail::is_venue_id_Valid() const{
    return m_venue_id_isValid;
}

QString OAITeamDetail::getVenueName() const {
    return m_venue_name;
}
void OAITeamDetail::setVenueName(const QString &venue_name) {
    m_venue_name = venue_name;
    m_venue_name_isSet = true;
}

bool OAITeamDetail::is_venue_name_Set() const{
    return m_venue_name_isSet;
}

bool OAITeamDetail::is_venue_name_Valid() const{
    return m_venue_name_isValid;
}

QString OAITeamDetail::getWebsite() const {
    return m_website;
}
void OAITeamDetail::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAITeamDetail::is_website_Set() const{
    return m_website_isSet;
}

bool OAITeamDetail::is_website_Valid() const{
    return m_website_isValid;
}

QString OAITeamDetail::getWikipediaLogoUrl() const {
    return m_wikipedia_logo_url;
}
void OAITeamDetail::setWikipediaLogoUrl(const QString &wikipedia_logo_url) {
    m_wikipedia_logo_url = wikipedia_logo_url;
    m_wikipedia_logo_url_isSet = true;
}

bool OAITeamDetail::is_wikipedia_logo_url_Set() const{
    return m_wikipedia_logo_url_isSet;
}

bool OAITeamDetail::is_wikipedia_logo_url_Valid() const{
    return m_wikipedia_logo_url_isValid;
}

QString OAITeamDetail::getWikipediaWordMarkUrl() const {
    return m_wikipedia_word_mark_url;
}
void OAITeamDetail::setWikipediaWordMarkUrl(const QString &wikipedia_word_mark_url) {
    m_wikipedia_word_mark_url = wikipedia_word_mark_url;
    m_wikipedia_word_mark_url_isSet = true;
}

bool OAITeamDetail::is_wikipedia_word_mark_url_Set() const{
    return m_wikipedia_word_mark_url_isSet;
}

bool OAITeamDetail::is_wikipedia_word_mark_url_Valid() const{
    return m_wikipedia_word_mark_url_isValid;
}

QString OAITeamDetail::getZip() const {
    return m_zip;
}
void OAITeamDetail::setZip(const QString &zip) {
    m_zip = zip;
    m_zip_isSet = true;
}

bool OAITeamDetail::is_zip_Set() const{
    return m_zip_isSet;
}

bool OAITeamDetail::is_zip_Valid() const{
    return m_zip_isValid;
}

bool OAITeamDetail::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_area_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_area_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_club_color1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_club_color2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_club_color3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_founded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_full_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
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

        if (m_nickname1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nickname2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nickname3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_players.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_venue_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_venue_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
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

        if (m_zip_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITeamDetail::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
