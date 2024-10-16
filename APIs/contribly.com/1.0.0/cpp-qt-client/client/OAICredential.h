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
 * OAICredential.h
 *
 * 
 */

#ifndef OAICredential_H
#define OAICredential_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICredential : public OAIObject {
public:
    OAICredential();
    OAICredential(QString json);
    ~OAICredential() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getScopes() const;
    void setScopes(const QList<QString> &scopes);
    bool is_scopes_Set() const;
    bool is_scopes_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUser() const;
    void setUser(const QString &user);
    bool is_user_Set() const;
    bool is_user_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_scopes;
    bool m_scopes_isSet;
    bool m_scopes_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_user;
    bool m_user_isSet;
    bool m_user_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICredential)

#endif // OAICredential_H
