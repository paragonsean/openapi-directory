/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICompanyGeneralDetaisViewModel.h
 *
 * 
 */

#ifndef OAICompanyGeneralDetaisViewModel_H
#define OAICompanyGeneralDetaisViewModel_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICompanyGeneralDetaisViewModel : public OAIObject {
public:
    OAICompanyGeneralDetaisViewModel();
    OAICompanyGeneralDetaisViewModel(QString json);
    ~OAICompanyGeneralDetaisViewModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getCompanyAddresses() const;
    void setCompanyAddresses(const QList<QString> &company_addresses);
    bool is_company_addresses_Set() const;
    bool is_company_addresses_Valid() const;

    QString getCompanyName() const;
    void setCompanyName(const QString &company_name);
    bool is_company_name_Set() const;
    bool is_company_name_Valid() const;

    QString getCurrencyCode() const;
    void setCurrencyCode(const QString &currency_code);
    bool is_currency_code_Set() const;
    bool is_currency_code_Valid() const;

    QString getCurrencyDescription() const;
    void setCurrencyDescription(const QString &currency_description);
    bool is_currency_description_Set() const;
    bool is_currency_description_Valid() const;

    qint64 getCurrencyId() const;
    void setCurrencyId(const qint64 &currency_id);
    bool is_currency_id_Set() const;
    bool is_currency_id_Valid() const;

    QString getCurrentcySymbol() const;
    void setCurrentcySymbol(const QString &currentcy_symbol);
    bool is_currentcy_symbol_Set() const;
    bool is_currentcy_symbol_Valid() const;

    QList<QString> getEmails() const;
    void setEmails(const QList<QString> &emails);
    bool is_emails_Set() const;
    bool is_emails_Valid() const;

    QList<QString> getFaxes() const;
    void setFaxes(const QList<QString> &faxes);
    bool is_faxes_Set() const;
    bool is_faxes_Valid() const;

    QList<QString> getPhones() const;
    void setPhones(const QList<QString> &phones);
    bool is_phones_Set() const;
    bool is_phones_Valid() const;

    QString getRegionDescription() const;
    void setRegionDescription(const QString &region_description);
    bool is_region_description_Set() const;
    bool is_region_description_Valid() const;

    qint64 getRegionId() const;
    void setRegionId(const qint64 &region_id);
    bool is_region_id_Set() const;
    bool is_region_id_Valid() const;

    QString getVatReg() const;
    void setVatReg(const QString &vat_reg);
    bool is_vat_reg_Set() const;
    bool is_vat_reg_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_company_addresses;
    bool m_company_addresses_isSet;
    bool m_company_addresses_isValid;

    QString m_company_name;
    bool m_company_name_isSet;
    bool m_company_name_isValid;

    QString m_currency_code;
    bool m_currency_code_isSet;
    bool m_currency_code_isValid;

    QString m_currency_description;
    bool m_currency_description_isSet;
    bool m_currency_description_isValid;

    qint64 m_currency_id;
    bool m_currency_id_isSet;
    bool m_currency_id_isValid;

    QString m_currentcy_symbol;
    bool m_currentcy_symbol_isSet;
    bool m_currentcy_symbol_isValid;

    QList<QString> m_emails;
    bool m_emails_isSet;
    bool m_emails_isValid;

    QList<QString> m_faxes;
    bool m_faxes_isSet;
    bool m_faxes_isValid;

    QList<QString> m_phones;
    bool m_phones_isSet;
    bool m_phones_isValid;

    QString m_region_description;
    bool m_region_description_isSet;
    bool m_region_description_isValid;

    qint64 m_region_id;
    bool m_region_id_isSet;
    bool m_region_id_isValid;

    QString m_vat_reg;
    bool m_vat_reg_isSet;
    bool m_vat_reg_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICompanyGeneralDetaisViewModel)

#endif // OAICompanyGeneralDetaisViewModel_H
