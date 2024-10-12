/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties.h
 *
 * Recipient Email Contract Properties.
 */

#ifndef OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties_H
#define OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties : public OAIObject {
public:
    OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties();
    OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties(QString json);
    ~OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties)

#endif // OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties_H
