/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBatchItemDetails.h
 *
 * Details of the batch run if this transaction was part of a batch.
 */

#ifndef OAIBatchItemDetails_H
#define OAIBatchItemDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBatchItemDetails : public OAIObject {
public:
    OAIBatchItemDetails();
    OAIBatchItemDetails(QString json);
    ~OAIBatchItemDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBatchItemPublicUuid() const;
    void setBatchItemPublicUuid(const QString &batch_item_public_uuid);
    bool is_batch_item_public_uuid_Set() const;
    bool is_batch_item_public_uuid_Valid() const;

    QString getBatchName() const;
    void setBatchName(const QString &batch_name);
    bool is_batch_name_Set() const;
    bool is_batch_name_Valid() const;

    QString getBatchPublicUuid() const;
    void setBatchPublicUuid(const QString &batch_public_uuid);
    bool is_batch_public_uuid_Set() const;
    bool is_batch_public_uuid_Valid() const;

    QString getJobNumber() const;
    void setJobNumber(const QString &job_number);
    bool is_job_number_Set() const;
    bool is_job_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_batch_item_public_uuid;
    bool m_batch_item_public_uuid_isSet;
    bool m_batch_item_public_uuid_isValid;

    QString m_batch_name;
    bool m_batch_name_isSet;
    bool m_batch_name_isValid;

    QString m_batch_public_uuid;
    bool m_batch_public_uuid_isSet;
    bool m_batch_public_uuid_isValid;

    QString m_job_number;
    bool m_job_number_isSet;
    bool m_job_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBatchItemDetails)

#endif // OAIBatchItemDetails_H
