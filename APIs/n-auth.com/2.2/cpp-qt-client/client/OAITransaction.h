/**
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITransaction.h
 *
 * 
 */

#ifndef OAITransaction_H
#define OAITransaction_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITransaction : public OAIObject {
public:
    OAITransaction();
    OAITransaction(QString json);
    ~OAITransaction() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAmount() const;
    void setAmount(const QString &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    QString getBenificiary() const;
    void setBenificiary(const QString &benificiary);
    bool is_benificiary_Set() const;
    bool is_benificiary_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    QString m_benificiary;
    bool m_benificiary_isSet;
    bool m_benificiary_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITransaction)

#endif // OAITransaction_H
