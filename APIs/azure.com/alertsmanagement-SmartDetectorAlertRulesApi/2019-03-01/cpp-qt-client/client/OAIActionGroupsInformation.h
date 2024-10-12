/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIActionGroupsInformation.h
 *
 * The Action Groups information, used by the alert rule.
 */

#ifndef OAIActionGroupsInformation_H
#define OAIActionGroupsInformation_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIActionGroupsInformation : public OAIObject {
public:
    OAIActionGroupsInformation();
    OAIActionGroupsInformation(QString json);
    ~OAIActionGroupsInformation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCustomEmailSubject() const;
    void setCustomEmailSubject(const QString &custom_email_subject);
    bool is_custom_email_subject_Set() const;
    bool is_custom_email_subject_Valid() const;

    QString getCustomWebhookPayload() const;
    void setCustomWebhookPayload(const QString &custom_webhook_payload);
    bool is_custom_webhook_payload_Set() const;
    bool is_custom_webhook_payload_Valid() const;

    QList<QString> getGroupIds() const;
    void setGroupIds(const QList<QString> &group_ids);
    bool is_group_ids_Set() const;
    bool is_group_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_custom_email_subject;
    bool m_custom_email_subject_isSet;
    bool m_custom_email_subject_isValid;

    QString m_custom_webhook_payload;
    bool m_custom_webhook_payload_isSet;
    bool m_custom_webhook_payload_isValid;

    QList<QString> m_group_ids;
    bool m_group_ids_isSet;
    bool m_group_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIActionGroupsInformation)

#endif // OAIActionGroupsInformation_H
