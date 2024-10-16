/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAuthority.h
 *
 * 
 */

#ifndef OAIAuthority_H
#define OAIAuthority_H

#include <QJsonObject>

#include "OAIClient.h"
#include "OAIUser.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIClient;
class OAIUser;

class OAIAuthority : public OAIObject {
public:
    OAIAuthority();
    OAIAuthority(QString json);
    ~OAIAuthority() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIClient getClient() const;
    void setClient(const OAIClient &client);
    bool is_client_Set() const;
    bool is_client_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIUser getUser() const;
    void setUser(const OAIUser &user);
    bool is_user_Set() const;
    bool is_user_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIClient m_client;
    bool m_client_isSet;
    bool m_client_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIUser m_user;
    bool m_user_isSet;
    bool m_user_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAuthority)

#endif // OAIAuthority_H
