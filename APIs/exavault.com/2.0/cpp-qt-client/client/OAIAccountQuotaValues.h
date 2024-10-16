/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAccountQuotaValues.h
 *
 * 
 */

#ifndef OAIAccountQuotaValues_H
#define OAIAccountQuotaValues_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccountQuotaValues : public OAIObject {
public:
    OAIAccountQuotaValues();
    OAIAccountQuotaValues(QString json);
    ~OAIAccountQuotaValues() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isNoticeEnabled() const;
    void setNoticeEnabled(const bool &notice_enabled);
    bool is_notice_enabled_Set() const;
    bool is_notice_enabled_Valid() const;

    qint32 getNoticeThreshold() const;
    void setNoticeThreshold(const qint32 &notice_threshold);
    bool is_notice_threshold_Set() const;
    bool is_notice_threshold_Valid() const;

    bool isTransactionsNoticeEnabled() const;
    void setTransactionsNoticeEnabled(const bool &transactions_notice_enabled);
    bool is_transactions_notice_enabled_Set() const;
    bool is_transactions_notice_enabled_Valid() const;

    qint32 getTransactionsNoticeThreshold() const;
    void setTransactionsNoticeThreshold(const qint32 &transactions_notice_threshold);
    bool is_transactions_notice_threshold_Set() const;
    bool is_transactions_notice_threshold_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_notice_enabled;
    bool m_notice_enabled_isSet;
    bool m_notice_enabled_isValid;

    qint32 m_notice_threshold;
    bool m_notice_threshold_isSet;
    bool m_notice_threshold_isValid;

    bool m_transactions_notice_enabled;
    bool m_transactions_notice_enabled_isSet;
    bool m_transactions_notice_enabled_isValid;

    qint32 m_transactions_notice_threshold;
    bool m_transactions_notice_threshold_isSet;
    bool m_transactions_notice_threshold_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccountQuotaValues)

#endif // OAIAccountQuotaValues_H
