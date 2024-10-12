/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApiVersionSet_ListByService_default_response_error_details_inner.h
 *
 * Error Field contract.
 */

#ifndef OAIApiVersionSet_ListByService_default_response_error_details_inner_H
#define OAIApiVersionSet_ListByService_default_response_error_details_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApiVersionSet_ListByService_default_response_error_details_inner : public OAIObject {
public:
    OAIApiVersionSet_ListByService_default_response_error_details_inner();
    OAIApiVersionSet_ListByService_default_response_error_details_inner(QString json);
    ~OAIApiVersionSet_ListByService_default_response_error_details_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getTarget() const;
    void setTarget(const QString &target);
    bool is_target_Set() const;
    bool is_target_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_target;
    bool m_target_isSet;
    bool m_target_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApiVersionSet_ListByService_default_response_error_details_inner)

#endif // OAIApiVersionSet_ListByService_default_response_error_details_inner_H
