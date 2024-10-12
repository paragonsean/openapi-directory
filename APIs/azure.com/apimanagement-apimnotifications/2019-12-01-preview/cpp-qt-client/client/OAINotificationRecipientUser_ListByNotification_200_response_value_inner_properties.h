/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties.h
 *
 * Recipient User Contract Properties.
 */

#ifndef OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties_H
#define OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties : public OAIObject {
public:
    OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties();
    OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties(QString json);
    ~OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUserId() const;
    void setUserId(const QString &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties)

#endif // OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties_H
