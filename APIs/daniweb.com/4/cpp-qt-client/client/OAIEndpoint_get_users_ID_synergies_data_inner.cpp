/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEndpoint_get_users_ID_synergies_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_get_users_ID_synergies_data_inner::OAIEndpoint_get_users_ID_synergies_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_get_users_ID_synergies_data_inner::OAIEndpoint_get_users_ID_synergies_data_inner() {
    this->initializeModel();
}

OAIEndpoint_get_users_ID_synergies_data_inner::~OAIEndpoint_get_users_ID_synergies_data_inner() {}

void OAIEndpoint_get_users_ID_synergies_data_inner::initializeModel() {

    m_additional_isSet = false;
    m_additional_isValid = false;

    m_conversation_isSet = false;
    m_conversation_isValid = false;

    m_match_isSet = false;
    m_match_isValid = false;

    m_meet_isSet = false;
    m_meet_isValid = false;

    m_relationship_isSet = false;
    m_relationship_isValid = false;
}

void OAIEndpoint_get_users_ID_synergies_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_get_users_ID_synergies_data_inner::fromJsonObject(QJsonObject json) {

    m_additional_isValid = ::OpenAPI::fromJsonValue(m_additional, json[QString("additional")]);
    m_additional_isSet = !json[QString("additional")].isNull() && m_additional_isValid;

    m_conversation_isValid = ::OpenAPI::fromJsonValue(m_conversation, json[QString("conversation")]);
    m_conversation_isSet = !json[QString("conversation")].isNull() && m_conversation_isValid;

    m_match_isValid = ::OpenAPI::fromJsonValue(m_match, json[QString("match")]);
    m_match_isSet = !json[QString("match")].isNull() && m_match_isValid;

    m_meet_isValid = ::OpenAPI::fromJsonValue(m_meet, json[QString("meet")]);
    m_meet_isSet = !json[QString("meet")].isNull() && m_meet_isValid;

    m_relationship_isValid = ::OpenAPI::fromJsonValue(m_relationship, json[QString("relationship")]);
    m_relationship_isSet = !json[QString("relationship")].isNull() && m_relationship_isValid;
}

QString OAIEndpoint_get_users_ID_synergies_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_get_users_ID_synergies_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_additional.isSet()) {
        obj.insert(QString("additional"), ::OpenAPI::toJsonValue(m_additional));
    }
    if (m_conversation.isSet()) {
        obj.insert(QString("conversation"), ::OpenAPI::toJsonValue(m_conversation));
    }
    if (m_match.isSet()) {
        obj.insert(QString("match"), ::OpenAPI::toJsonValue(m_match));
    }
    if (m_meet.isSet()) {
        obj.insert(QString("meet"), ::OpenAPI::toJsonValue(m_meet));
    }
    if (m_relationship.isSet()) {
        obj.insert(QString("relationship"), ::OpenAPI::toJsonValue(m_relationship));
    }
    return obj;
}

OAIEndpoint_get_users_ID_synergies_data_inner_additional OAIEndpoint_get_users_ID_synergies_data_inner::getAdditional() const {
    return m_additional;
}
void OAIEndpoint_get_users_ID_synergies_data_inner::setAdditional(const OAIEndpoint_get_users_ID_synergies_data_inner_additional &additional) {
    m_additional = additional;
    m_additional_isSet = true;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_additional_Set() const{
    return m_additional_isSet;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_additional_Valid() const{
    return m_additional_isValid;
}

OAIConversation OAIEndpoint_get_users_ID_synergies_data_inner::getConversation() const {
    return m_conversation;
}
void OAIEndpoint_get_users_ID_synergies_data_inner::setConversation(const OAIConversation &conversation) {
    m_conversation = conversation;
    m_conversation_isSet = true;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_conversation_Set() const{
    return m_conversation_isSet;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_conversation_Valid() const{
    return m_conversation_isValid;
}

OAIEndpoint_get_users_ID_synergies_data_inner_match OAIEndpoint_get_users_ID_synergies_data_inner::getMatch() const {
    return m_match;
}
void OAIEndpoint_get_users_ID_synergies_data_inner::setMatch(const OAIEndpoint_get_users_ID_synergies_data_inner_match &match) {
    m_match = match;
    m_match_isSet = true;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_match_Set() const{
    return m_match_isSet;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_match_Valid() const{
    return m_match_isValid;
}

OAIEndpoint_get_users_ID_synergies_data_inner_meet OAIEndpoint_get_users_ID_synergies_data_inner::getMeet() const {
    return m_meet;
}
void OAIEndpoint_get_users_ID_synergies_data_inner::setMeet(const OAIEndpoint_get_users_ID_synergies_data_inner_meet &meet) {
    m_meet = meet;
    m_meet_isSet = true;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_meet_Set() const{
    return m_meet_isSet;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_meet_Valid() const{
    return m_meet_isValid;
}

OAIEndpoint_get_users_ID_synergies_data_inner_relationship OAIEndpoint_get_users_ID_synergies_data_inner::getRelationship() const {
    return m_relationship;
}
void OAIEndpoint_get_users_ID_synergies_data_inner::setRelationship(const OAIEndpoint_get_users_ID_synergies_data_inner_relationship &relationship) {
    m_relationship = relationship;
    m_relationship_isSet = true;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_relationship_Set() const{
    return m_relationship_isSet;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::is_relationship_Valid() const{
    return m_relationship_isValid;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversation.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_match.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_meet.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_relationship.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_get_users_ID_synergies_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
