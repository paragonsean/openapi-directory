/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomerAccountManagementV1InitiatePasswordResetPut_request.h
 *
 * 
 */

#ifndef OAICustomerAccountManagementV1InitiatePasswordResetPut_request_H
#define OAICustomerAccountManagementV1InitiatePasswordResetPut_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICustomerAccountManagementV1InitiatePasswordResetPut_request : public OAIObject {
public:
    OAICustomerAccountManagementV1InitiatePasswordResetPut_request();
    OAICustomerAccountManagementV1InitiatePasswordResetPut_request(QString json);
    ~OAICustomerAccountManagementV1InitiatePasswordResetPut_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getRTemplate() const;
    void setRTemplate(const QString &r_template);
    bool is_r_template_Set() const;
    bool is_r_template_Valid() const;

    qint32 getWebsiteId() const;
    void setWebsiteId(const qint32 &website_id);
    bool is_website_id_Set() const;
    bool is_website_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_r_template;
    bool m_r_template_isSet;
    bool m_r_template_isValid;

    qint32 m_website_id;
    bool m_website_id_isSet;
    bool m_website_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomerAccountManagementV1InitiatePasswordResetPut_request)

#endif // OAICustomerAccountManagementV1InitiatePasswordResetPut_request_H
