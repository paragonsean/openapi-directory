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

/*
 * OAIAgentState.h
 *
 * 
 */

#ifndef OAIAgentState_H
#define OAIAgentState_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAgentState : public OAIObject {
public:
    OAIAgentState();
    OAIAgentState(QString json);
    ~OAIAgentState() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAgentNum() const;
    void setAgentNum(const qint32 &agent_num);
    bool is_agent_num_Set() const;
    bool is_agent_num_Valid() const;

    qint32 getState() const;
    void setState(const qint32 &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_agent_num;
    bool m_agent_num_isSet;
    bool m_agent_num_isValid;

    qint32 m_state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAgentState)

#endif // OAIAgentState_H
