/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAgentState.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAgentState::OAIAgentState(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAgentState::OAIAgentState() {
    this->initializeModel();
}

OAIAgentState::~OAIAgentState() {}

void OAIAgentState::initializeModel() {

    m_agent_num_isSet = false;
    m_agent_num_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIAgentState::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAgentState::fromJsonObject(QJsonObject json) {

    m_agent_num_isValid = ::OpenAPI::fromJsonValue(m_agent_num, json[QString("agentNum")]);
    m_agent_num_isSet = !json[QString("agentNum")].isNull() && m_agent_num_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIAgentState::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAgentState::asJsonObject() const {
    QJsonObject obj;
    if (m_agent_num_isSet) {
        obj.insert(QString("agentNum"), ::OpenAPI::toJsonValue(m_agent_num));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

qint32 OAIAgentState::getAgentNum() const {
    return m_agent_num;
}
void OAIAgentState::setAgentNum(const qint32 &agent_num) {
    m_agent_num = agent_num;
    m_agent_num_isSet = true;
}

bool OAIAgentState::is_agent_num_Set() const{
    return m_agent_num_isSet;
}

bool OAIAgentState::is_agent_num_Valid() const{
    return m_agent_num_isValid;
}

qint32 OAIAgentState::getState() const {
    return m_state;
}
void OAIAgentState::setState(const qint32 &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIAgentState::is_state_Set() const{
    return m_state_isSet;
}

bool OAIAgentState::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIAgentState::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agent_num_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAgentState::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
