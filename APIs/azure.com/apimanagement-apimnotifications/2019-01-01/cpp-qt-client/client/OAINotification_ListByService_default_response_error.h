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
 * OAINotification_ListByService_default_response_error.h
 *
 * Error Body contract.
 */

#ifndef OAINotification_ListByService_default_response_error_H
#define OAINotification_ListByService_default_response_error_H

#include <QJsonObject>

#include "OAINotification_ListByService_default_response_error_details_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINotification_ListByService_default_response_error_details_inner;

class OAINotification_ListByService_default_response_error : public OAIObject {
public:
    OAINotification_ListByService_default_response_error();
    OAINotification_ListByService_default_response_error(QString json);
    ~OAINotification_ListByService_default_response_error() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QList<OAINotification_ListByService_default_response_error_details_inner> getDetails() const;
    void setDetails(const QList<OAINotification_ListByService_default_response_error_details_inner> &details);
    bool is_details_Set() const;
    bool is_details_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QList<OAINotification_ListByService_default_response_error_details_inner> m_details;
    bool m_details_isSet;
    bool m_details_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotification_ListByService_default_response_error)

#endif // OAINotification_ListByService_default_response_error_H
