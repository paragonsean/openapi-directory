/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIOutstandingShareholderLoans.h
 *
 * 
 */

#ifndef OAIIOutstandingShareholderLoans_H
#define OAIIOutstandingShareholderLoans_H

#include <QJsonObject>

#include "OAICurrency.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICurrency;

class OAIIOutstandingShareholderLoans : public OAIObject {
public:
    OAIIOutstandingShareholderLoans();
    OAIIOutstandingShareholderLoans(QString json);
    ~OAIIOutstandingShareholderLoans() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICurrency getClientAmount() const;
    void setClientAmount(const OAICurrency &client_amount);
    bool is_client_amount_Set() const;
    bool is_client_amount_Valid() const;

    OAICurrency getCoClientAmount() const;
    void setCoClientAmount(const OAICurrency &co_client_amount);
    bool is_co_client_amount_Set() const;
    bool is_co_client_amount_Valid() const;

    OAICurrency getOtherAmount() const;
    void setOtherAmount(const OAICurrency &other_amount);
    bool is_other_amount_Set() const;
    bool is_other_amount_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICurrency m_client_amount;
    bool m_client_amount_isSet;
    bool m_client_amount_isValid;

    OAICurrency m_co_client_amount;
    bool m_co_client_amount_isSet;
    bool m_co_client_amount_isValid;

    OAICurrency m_other_amount;
    bool m_other_amount_isSet;
    bool m_other_amount_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIOutstandingShareholderLoans)

#endif // OAIIOutstandingShareholderLoans_H
