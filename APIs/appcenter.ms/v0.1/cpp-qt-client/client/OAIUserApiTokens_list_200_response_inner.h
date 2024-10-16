/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUserApiTokens_list_200_response_inner.h
 *
 * 
 */

#ifndef OAIUserApiTokens_list_200_response_inner_H
#define OAIUserApiTokens_list_200_response_inner_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUserApiTokens_list_200_response_inner : public OAIObject {
public:
    OAIUserApiTokens_list_200_response_inner();
    OAIUserApiTokens_list_200_response_inner(QString json);
    ~OAIUserApiTokens_list_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<QString> getScope() const;
    void setScope(const QList<QString> &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<QString> m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserApiTokens_list_200_response_inner)

#endif // OAIUserApiTokens_list_200_response_inner_H
