/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWebhookTriggers_shares.h
 *
 * 
 */

#ifndef OAIWebhookTriggers_shares_H
#define OAIWebhookTriggers_shares_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWebhookTriggers_shares : public OAIObject {
public:
    OAIWebhookTriggers_shares();
    OAIWebhookTriggers_shares(QString json);
    ~OAIWebhookTriggers_shares() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isFormSubmit() const;
    void setFormSubmit(const bool &form_submit);
    bool is_form_submit_Set() const;
    bool is_form_submit_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_form_submit;
    bool m_form_submit_isSet;
    bool m_form_submit_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhookTriggers_shares)

#endif // OAIWebhookTriggers_shares_H
