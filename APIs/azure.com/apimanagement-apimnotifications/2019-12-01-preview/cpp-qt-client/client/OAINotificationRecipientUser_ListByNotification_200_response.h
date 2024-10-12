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
 * OAINotificationRecipientUser_ListByNotification_200_response.h
 *
 * Paged Recipient User list representation.
 */

#ifndef OAINotificationRecipientUser_ListByNotification_200_response_H
#define OAINotificationRecipientUser_ListByNotification_200_response_H

#include <QJsonObject>

#include "OAINotificationRecipientUser_ListByNotification_200_response_value_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINotificationRecipientUser_ListByNotification_200_response_value_inner;

class OAINotificationRecipientUser_ListByNotification_200_response : public OAIObject {
public:
    OAINotificationRecipientUser_ListByNotification_200_response();
    OAINotificationRecipientUser_ListByNotification_200_response(QString json);
    ~OAINotificationRecipientUser_ListByNotification_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAINotificationRecipientUser_ListByNotification_200_response_value_inner> getValue() const;
    void setValue(const QList<OAINotificationRecipientUser_ListByNotification_200_response_value_inner> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAINotificationRecipientUser_ListByNotification_200_response_value_inner> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotificationRecipientUser_ListByNotification_200_response)

#endif // OAINotificationRecipientUser_ListByNotification_200_response_H
