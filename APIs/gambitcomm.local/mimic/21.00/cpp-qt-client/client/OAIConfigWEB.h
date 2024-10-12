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
 * OAIConfigWEB.h
 *
 * 
 */

#ifndef OAIConfigWEB_H
#define OAIConfigWEB_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIConfigWEB : public OAIObject {
public:
    OAIConfigWEB();
    OAIConfigWEB(QString json);
    ~OAIConfigWEB() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getIsPersistentConnections() const;
    void setIsPersistentConnections(const qint32 &is_persistent_connections);
    bool is_is_persistent_connections_Set() const;
    bool is_is_persistent_connections_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    qint32 getPort() const;
    void setPort(const qint32 &port);
    bool is_port_Set() const;
    bool is_port_Valid() const;

    QString getRule() const;
    void setRule(const QString &rule);
    bool is_rule_Set() const;
    bool is_rule_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    QString getWsdl() const;
    void setWsdl(const QString &wsdl);
    bool is_wsdl_Set() const;
    bool is_wsdl_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_is_persistent_connections;
    bool m_is_persistent_connections_isSet;
    bool m_is_persistent_connections_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    qint32 m_port;
    bool m_port_isSet;
    bool m_port_isValid;

    QString m_rule;
    bool m_rule_isSet;
    bool m_rule_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;

    QString m_wsdl;
    bool m_wsdl_isSet;
    bool m_wsdl_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfigWEB)

#endif // OAIConfigWEB_H
