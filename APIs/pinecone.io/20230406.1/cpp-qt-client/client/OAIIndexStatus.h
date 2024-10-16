/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIndexStatus.h
 *
 * 
 */

#ifndef OAIIndexStatus_H
#define OAIIndexStatus_H

#include <QJsonObject>

#include "OAIIndexState.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIndexStatus : public OAIObject {
public:
    OAIIndexStatus();
    OAIIndexStatus(QString json);
    ~OAIIndexStatus() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHost() const;
    void setHost(const QString &host);
    bool is_host_Set() const;
    bool is_host_Valid() const;

    qint32 getPort() const;
    void setPort(const qint32 &port);
    bool is_port_Set() const;
    bool is_port_Valid() const;

    bool isReady() const;
    void setReady(const bool &ready);
    bool is_ready_Set() const;
    bool is_ready_Valid() const;

    OAIIndexState getState() const;
    void setState(const OAIIndexState &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_host;
    bool m_host_isSet;
    bool m_host_isValid;

    qint32 m_port;
    bool m_port_isSet;
    bool m_port_isValid;

    bool m_ready;
    bool m_ready_isSet;
    bool m_ready_isValid;

    OAIIndexState m_state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIndexStatus)

#endif // OAIIndexStatus_H
