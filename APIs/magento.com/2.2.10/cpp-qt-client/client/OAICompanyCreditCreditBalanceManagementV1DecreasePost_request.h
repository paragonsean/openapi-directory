/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICompanyCreditCreditBalanceManagementV1DecreasePost_request.h
 *
 * 
 */

#ifndef OAICompanyCreditCreditBalanceManagementV1DecreasePost_request_H
#define OAICompanyCreditCreditBalanceManagementV1DecreasePost_request_H

#include <QJsonObject>

#include "OAICompany_credit_data_credit_balance_options_interface.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICompany_credit_data_credit_balance_options_interface;

class OAICompanyCreditCreditBalanceManagementV1DecreasePost_request : public OAIObject {
public:
    OAICompanyCreditCreditBalanceManagementV1DecreasePost_request();
    OAICompanyCreditCreditBalanceManagementV1DecreasePost_request(QString json);
    ~OAICompanyCreditCreditBalanceManagementV1DecreasePost_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getComment() const;
    void setComment(const QString &comment);
    bool is_comment_Set() const;
    bool is_comment_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    qint32 getOperationType() const;
    void setOperationType(const qint32 &operation_type);
    bool is_operation_type_Set() const;
    bool is_operation_type_Valid() const;

    OAICompany_credit_data_credit_balance_options_interface getOptions() const;
    void setOptions(const OAICompany_credit_data_credit_balance_options_interface &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    double getValue() const;
    void setValue(const double &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_comment;
    bool m_comment_isSet;
    bool m_comment_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    qint32 m_operation_type;
    bool m_operation_type_isSet;
    bool m_operation_type_isValid;

    OAICompany_credit_data_credit_balance_options_interface m_options;
    bool m_options_isSet;
    bool m_options_isValid;

    double m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICompanyCreditCreditBalanceManagementV1DecreasePost_request)

#endif // OAICompanyCreditCreditBalanceManagementV1DecreasePost_request_H
