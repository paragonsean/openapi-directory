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

#include "OAIInjury.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInjury::OAIInjury(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInjury::OAIInjury() {
    this->initializeModel();
}

OAIInjury::~OAIInjury() {}

void OAIInjury::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_body_part_isSet = false;
    m_body_part_isValid = false;

    m_expected_return_isSet = false;
    m_expected_return_isValid = false;

    m_injury_id_isSet = false;
    m_injury_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIInjury::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInjury::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("Active")]);
    m_active_isSet = !json[QString("Active")].isNull() && m_active_isValid;

    m_body_part_isValid = ::OpenAPI::fromJsonValue(m_body_part, json[QString("BodyPart")]);
    m_body_part_isSet = !json[QString("BodyPart")].isNull() && m_body_part_isValid;

    m_expected_return_isValid = ::OpenAPI::fromJsonValue(m_expected_return, json[QString("ExpectedReturn")]);
    m_expected_return_isSet = !json[QString("ExpectedReturn")].isNull() && m_expected_return_isValid;

    m_injury_id_isValid = ::OpenAPI::fromJsonValue(m_injury_id, json[QString("InjuryID")]);
    m_injury_id_isSet = !json[QString("InjuryID")].isNull() && m_injury_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("StartDate")]);
    m_start_date_isSet = !json[QString("StartDate")].isNull() && m_start_date_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;
}

QString OAIInjury::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInjury::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("Active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_body_part_isSet) {
        obj.insert(QString("BodyPart"), ::OpenAPI::toJsonValue(m_body_part));
    }
    if (m_expected_return_isSet) {
        obj.insert(QString("ExpectedReturn"), ::OpenAPI::toJsonValue(m_expected_return));
    }
    if (m_injury_id_isSet) {
        obj.insert(QString("InjuryID"), ::OpenAPI::toJsonValue(m_injury_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("StartDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

bool OAIInjury::isActive() const {
    return m_active;
}
void OAIInjury::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIInjury::is_active_Set() const{
    return m_active_isSet;
}

bool OAIInjury::is_active_Valid() const{
    return m_active_isValid;
}

QString OAIInjury::getBodyPart() const {
    return m_body_part;
}
void OAIInjury::setBodyPart(const QString &body_part) {
    m_body_part = body_part;
    m_body_part_isSet = true;
}

bool OAIInjury::is_body_part_Set() const{
    return m_body_part_isSet;
}

bool OAIInjury::is_body_part_Valid() const{
    return m_body_part_isValid;
}

QString OAIInjury::getExpectedReturn() const {
    return m_expected_return;
}
void OAIInjury::setExpectedReturn(const QString &expected_return) {
    m_expected_return = expected_return;
    m_expected_return_isSet = true;
}

bool OAIInjury::is_expected_return_Set() const{
    return m_expected_return_isSet;
}

bool OAIInjury::is_expected_return_Valid() const{
    return m_expected_return_isValid;
}

qint32 OAIInjury::getInjuryId() const {
    return m_injury_id;
}
void OAIInjury::setInjuryId(const qint32 &injury_id) {
    m_injury_id = injury_id;
    m_injury_id_isSet = true;
}

bool OAIInjury::is_injury_id_Set() const{
    return m_injury_id_isSet;
}

bool OAIInjury::is_injury_id_Valid() const{
    return m_injury_id_isValid;
}

QString OAIInjury::getName() const {
    return m_name;
}
void OAIInjury::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIInjury::is_name_Set() const{
    return m_name_isSet;
}

bool OAIInjury::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIInjury::getPlayerId() const {
    return m_player_id;
}
void OAIInjury::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIInjury::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIInjury::is_player_id_Valid() const{
    return m_player_id_isValid;
}

QString OAIInjury::getStartDate() const {
    return m_start_date;
}
void OAIInjury::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIInjury::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIInjury::is_start_date_Valid() const{
    return m_start_date_isValid;
}

QString OAIInjury::getStatus() const {
    return m_status;
}
void OAIInjury::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIInjury::is_status_Set() const{
    return m_status_isSet;
}

bool OAIInjury::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIInjury::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_body_part_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expected_return_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_injury_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInjury::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
