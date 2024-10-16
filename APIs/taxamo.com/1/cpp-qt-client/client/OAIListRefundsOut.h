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
 * OAIListRefundsOut.h
 *
 * 
 */

#ifndef OAIListRefundsOut_H
#define OAIListRefundsOut_H

#include <QJsonObject>

#include "OAIRefunds.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRefunds;

class OAIListRefundsOut : public OAIObject {
public:
    OAIListRefundsOut();
    OAIListRefundsOut(QString json);
    ~OAIListRefundsOut() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIRefunds> getRefunds() const;
    void setRefunds(const QList<OAIRefunds> &refunds);
    bool is_refunds_Set() const;
    bool is_refunds_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIRefunds> m_refunds;
    bool m_refunds_isSet;
    bool m_refunds_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIListRefundsOut)

#endif // OAIListRefundsOut_H
