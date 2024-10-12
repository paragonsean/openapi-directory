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
 * OAINotification_ListByService_200_response_value_inner_properties.h
 *
 * Notification Contract properties.
 */

#ifndef OAINotification_ListByService_200_response_value_inner_properties_H
#define OAINotification_ListByService_200_response_value_inner_properties_H

#include <QJsonObject>

#include "OAINotification_ListByService_200_response_value_inner_properties_recipients.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINotification_ListByService_200_response_value_inner_properties_recipients;

class OAINotification_ListByService_200_response_value_inner_properties : public OAIObject {
public:
    OAINotification_ListByService_200_response_value_inner_properties();
    OAINotification_ListByService_200_response_value_inner_properties(QString json);
    ~OAINotification_ListByService_200_response_value_inner_properties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAINotification_ListByService_200_response_value_inner_properties_recipients getRecipients() const;
    void setRecipients(const OAINotification_ListByService_200_response_value_inner_properties_recipients &recipients);
    bool is_recipients_Set() const;
    bool is_recipients_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAINotification_ListByService_200_response_value_inner_properties_recipients m_recipients;
    bool m_recipients_isSet;
    bool m_recipients_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotification_ListByService_200_response_value_inner_properties)

#endif // OAINotification_ListByService_200_response_value_inner_properties_H
