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
 * OAINotification_ListByService_default_response.h
 *
 * Error Response.
 */

#ifndef OAINotification_ListByService_default_response_H
#define OAINotification_ListByService_default_response_H

#include <QJsonObject>

#include "OAINotification_ListByService_default_response_error.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINotification_ListByService_default_response_error;

class OAINotification_ListByService_default_response : public OAIObject {
public:
    OAINotification_ListByService_default_response();
    OAINotification_ListByService_default_response(QString json);
    ~OAINotification_ListByService_default_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAINotification_ListByService_default_response_error getError() const;
    void setError(const OAINotification_ListByService_default_response_error &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAINotification_ListByService_default_response_error m_error;
    bool m_error_isSet;
    bool m_error_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotification_ListByService_default_response)

#endif // OAINotification_ListByService_default_response_H
