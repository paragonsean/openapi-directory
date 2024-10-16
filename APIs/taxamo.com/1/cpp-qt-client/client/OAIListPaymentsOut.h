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
 * OAIListPaymentsOut.h
 *
 * 
 */

#ifndef OAIListPaymentsOut_H
#define OAIListPaymentsOut_H

#include <QJsonObject>

#include "OAIPayments.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPayments;

class OAIListPaymentsOut : public OAIObject {
public:
    OAIListPaymentsOut();
    OAIListPaymentsOut(QString json);
    ~OAIListPaymentsOut() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIPayments> getPayments() const;
    void setPayments(const QList<OAIPayments> &payments);
    bool is_payments_Set() const;
    bool is_payments_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIPayments> m_payments;
    bool m_payments_isSet;
    bool m_payments_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIListPaymentsOut)

#endif // OAIListPaymentsOut_H
