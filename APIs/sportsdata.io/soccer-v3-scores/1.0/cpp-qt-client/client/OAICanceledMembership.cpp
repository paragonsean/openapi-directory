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

#include "OAICanceledMembership.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICanceledMembership::OAICanceledMembership(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICanceledMembership::OAICanceledMembership() {
    this->initializeModel();
}

OAICanceledMembership::~OAICanceledMembership() {}

void OAICanceledMembership::initializeModel() {

    m_canceled_membership_id_isSet = false;
    m_canceled_membership_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_membership_id_isSet = false;
    m_membership_id_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;
}

void OAICanceledMembership::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICanceledMembership::fromJsonObject(QJsonObject json) {

    m_canceled_membership_id_isValid = ::OpenAPI::fromJsonValue(m_canceled_membership_id, json[QString("CanceledMembershipId")]);
    m_canceled_membership_id_isSet = !json[QString("CanceledMembershipId")].isNull() && m_canceled_membership_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("Created")]);
    m_created_isSet = !json[QString("Created")].isNull() && m_created_isValid;

    m_membership_id_isValid = ::OpenAPI::fromJsonValue(m_membership_id, json[QString("MembershipId")]);
    m_membership_id_isSet = !json[QString("MembershipId")].isNull() && m_membership_id_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamId")]);
    m_team_id_isSet = !json[QString("TeamId")].isNull() && m_team_id_isValid;
}

QString OAICanceledMembership::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICanceledMembership::asJsonObject() const {
    QJsonObject obj;
    if (m_canceled_membership_id_isSet) {
        obj.insert(QString("CanceledMembershipId"), ::OpenAPI::toJsonValue(m_canceled_membership_id));
    }
    if (m_created_isSet) {
        obj.insert(QString("Created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_membership_id_isSet) {
        obj.insert(QString("MembershipId"), ::OpenAPI::toJsonValue(m_membership_id));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamId"), ::OpenAPI::toJsonValue(m_team_id));
    }
    return obj;
}

qint32 OAICanceledMembership::getCanceledMembershipId() const {
    return m_canceled_membership_id;
}
void OAICanceledMembership::setCanceledMembershipId(const qint32 &canceled_membership_id) {
    m_canceled_membership_id = canceled_membership_id;
    m_canceled_membership_id_isSet = true;
}

bool OAICanceledMembership::is_canceled_membership_id_Set() const{
    return m_canceled_membership_id_isSet;
}

bool OAICanceledMembership::is_canceled_membership_id_Valid() const{
    return m_canceled_membership_id_isValid;
}

QString OAICanceledMembership::getCreated() const {
    return m_created;
}
void OAICanceledMembership::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAICanceledMembership::is_created_Set() const{
    return m_created_isSet;
}

bool OAICanceledMembership::is_created_Valid() const{
    return m_created_isValid;
}

qint32 OAICanceledMembership::getMembershipId() const {
    return m_membership_id;
}
void OAICanceledMembership::setMembershipId(const qint32 &membership_id) {
    m_membership_id = membership_id;
    m_membership_id_isSet = true;
}

bool OAICanceledMembership::is_membership_id_Set() const{
    return m_membership_id_isSet;
}

bool OAICanceledMembership::is_membership_id_Valid() const{
    return m_membership_id_isValid;
}

qint32 OAICanceledMembership::getPlayerId() const {
    return m_player_id;
}
void OAICanceledMembership::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAICanceledMembership::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAICanceledMembership::is_player_id_Valid() const{
    return m_player_id_isValid;
}

qint32 OAICanceledMembership::getTeamId() const {
    return m_team_id;
}
void OAICanceledMembership::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAICanceledMembership::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAICanceledMembership::is_team_id_Valid() const{
    return m_team_id_isValid;
}

bool OAICanceledMembership::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_canceled_membership_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_membership_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICanceledMembership::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
