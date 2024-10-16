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
 * OAIGitHubMarketplacePurchase_account.h
 *
 * GitHub account information
 */

#ifndef OAIGitHubMarketplacePurchase_account_H
#define OAIGitHubMarketplacePurchase_account_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGitHubMarketplacePurchase_account : public OAIObject {
public:
    OAIGitHubMarketplacePurchase_account();
    OAIGitHubMarketplacePurchase_account(QString json);
    ~OAIGitHubMarketplacePurchase_account() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountType() const;
    void setAccountType(const QString &account_type);
    bool is_account_type_Set() const;
    bool is_account_type_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_type;
    bool m_account_type_isSet;
    bool m_account_type_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGitHubMarketplacePurchase_account)

#endif // OAIGitHubMarketplacePurchase_account_H
