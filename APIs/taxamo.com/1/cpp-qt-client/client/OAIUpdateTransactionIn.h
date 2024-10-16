/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateTransactionIn.h
 *
 * 
 */

#ifndef OAIUpdateTransactionIn_H
#define OAIUpdateTransactionIn_H

#include <QJsonObject>

#include "OAITransaction.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITransaction;

class OAIUpdateTransactionIn : public OAIObject {
public:
    OAIUpdateTransactionIn();
    OAIUpdateTransactionIn(QString json);
    ~OAIUpdateTransactionIn() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAITransaction getTransaction() const;
    void setTransaction(const OAITransaction &transaction);
    bool is_transaction_Set() const;
    bool is_transaction_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAITransaction m_transaction;
    bool m_transaction_isSet;
    bool m_transaction_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateTransactionIn)

#endif // OAIUpdateTransactionIn_H
