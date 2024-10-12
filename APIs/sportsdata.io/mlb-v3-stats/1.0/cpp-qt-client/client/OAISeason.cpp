/**
 * MLB v3 Stats
 * MLB scores, stats, and news API.
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

    m_api_season_isSet = false;
    m_api_season_isValid = false;

    m_post_season_start_date_isSet = false;
    m_post_season_start_date_isValid = false;

    m_regular_season_start_date_isSet = false;
    m_regular_season_start_date_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;
}

void OAISeason::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISeason::fromJsonObject(QJsonObject json) {

    m_api_season_isValid = ::OpenAPI::fromJsonValue(m_api_season, json[QString("ApiSeason")]);
    m_api_season_isSet = !json[QString("ApiSeason")].isNull() && m_api_season_isValid;

    m_post_season_start_date_isValid = ::OpenAPI::fromJsonValue(m_post_season_start_date, json[QString("PostSeasonStartDate")]);
    m_post_season_start_date_isSet = !json[QString("PostSeasonStartDate")].isNull() && m_post_season_start_date_isValid;

    m_regular_season_start_date_isValid = ::OpenAPI::fromJsonValue(m_regular_season_start_date, json[QString("RegularSeasonStartDate")]);
    m_regular_season_start_date_isSet = !json[QString("RegularSeasonStartDate")].isNull() && m_regular_season_start_date_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;
}

QString OAISeason::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISeason::asJsonObject() const {
    QJsonObject obj;
    if (m_api_season_isSet) {
        obj.insert(QString("ApiSeason"), ::OpenAPI::toJsonValue(m_api_season));
    }
    if (m_post_season_start_date_isSet) {
        obj.insert(QString("PostSeasonStartDate"), ::OpenAPI::toJsonValue(m_post_season_start_date));
    }
    if (m_regular_season_start_date_isSet) {
        obj.insert(QString("RegularSeasonStartDate"), ::OpenAPI::toJsonValue(m_regular_season_start_date));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    return obj;
}

QString OAISeason::getApiSeason() const {
    return m_api_season;
}
void OAISeason::setApiSeason(const QString &api_season) {
    m_api_season = api_season;
    m_api_season_isSet = true;
}

bool OAISeason::is_api_season_Set() const{
    return m_api_season_isSet;
}

bool OAISeason::is_api_season_Valid() const{
    return m_api_season_isValid;
}

QString OAISeason::getPostSeasonStartDate() const {
    return m_post_season_start_date;
}
void OAISeason::setPostSeasonStartDate(const QString &post_season_start_date) {
    m_post_season_start_date = post_season_start_date;
    m_post_season_start_date_isSet = true;
}

bool OAISeason::is_post_season_start_date_Set() const{
    return m_post_season_start_date_isSet;
}

bool OAISeason::is_post_season_start_date_Valid() const{
    return m_post_season_start_date_isValid;
}

QString OAISeason::getRegularSeasonStartDate() const {
    return m_regular_season_start_date;
}
void OAISeason::setRegularSeasonStartDate(const QString &regular_season_start_date) {
    m_regular_season_start_date = regular_season_start_date;
    m_regular_season_start_date_isSet = true;
}

bool OAISeason::is_regular_season_start_date_Set() const{
    return m_regular_season_start_date_isSet;
}

bool OAISeason::is_regular_season_start_date_Valid() const{
    return m_regular_season_start_date_isValid;
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

QString OAISeason::getSeasonType() const {
    return m_season_type;
}
void OAISeason::setSeasonType(const QString &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAISeason::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAISeason::is_season_type_Valid() const{
    return m_season_type_isValid;
}

bool OAISeason::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_post_season_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_regular_season_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_type_isSet) {
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
