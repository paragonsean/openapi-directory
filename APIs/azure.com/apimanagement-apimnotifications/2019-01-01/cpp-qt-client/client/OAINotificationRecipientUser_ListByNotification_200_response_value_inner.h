/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINotificationRecipientUser_ListByNotification_200_response_value_inner.h
 *
 * Recipient User details.
 */

#ifndef OAINotificationRecipientUser_ListByNotification_200_response_value_inner_H
#define OAINotificationRecipientUser_ListByNotification_200_response_value_inner_H

#include <QJsonObject>

#include "OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties;

class OAINotificationRecipientUser_ListByNotification_200_response_value_inner : public OAIObject {
public:
    OAINotificationRecipientUser_ListByNotification_200_response_value_inner();
    OAINotificationRecipientUser_ListByNotification_200_response_value_inner(QString json);
    ~OAINotificationRecipientUser_ListByNotification_200_response_value_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotificationRecipientUser_ListByNotification_200_response_value_inner)

#endif // OAINotificationRecipientUser_ListByNotification_200_response_value_inner_H
