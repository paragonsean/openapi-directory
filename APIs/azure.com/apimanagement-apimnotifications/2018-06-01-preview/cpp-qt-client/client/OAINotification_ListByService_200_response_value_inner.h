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
 * OAINotification_ListByService_200_response_value_inner.h
 *
 * Notification details.
 */

#ifndef OAINotification_ListByService_200_response_value_inner_H
#define OAINotification_ListByService_200_response_value_inner_H

#include <QJsonObject>

#include "OAINotification_ListByService_200_response_value_inner_properties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINotification_ListByService_200_response_value_inner_properties;

class OAINotification_ListByService_200_response_value_inner : public OAIObject {
public:
    OAINotification_ListByService_200_response_value_inner();
    OAINotification_ListByService_200_response_value_inner(QString json);
    ~OAINotification_ListByService_200_response_value_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAINotification_ListByService_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAINotification_ListByService_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAINotification_ListByService_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotification_ListByService_200_response_value_inner)

#endif // OAINotification_ListByService_200_response_value_inner_H
