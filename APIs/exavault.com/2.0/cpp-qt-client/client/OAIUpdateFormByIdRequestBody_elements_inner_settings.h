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
 * OAIUpdateFormByIdRequestBody_elements_inner_settings.h
 *
 * 
 */

#ifndef OAIUpdateFormByIdRequestBody_elements_inner_settings_H
#define OAIUpdateFormByIdRequestBody_elements_inner_settings_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateFormByIdRequestBody_elements_inner_settings : public OAIObject {
public:
    OAIUpdateFormByIdRequestBody_elements_inner_settings();
    OAIUpdateFormByIdRequestBody_elements_inner_settings(QString json);
    ~OAIUpdateFormByIdRequestBody_elements_inner_settings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsRequired() const;
    void setIsRequired(const bool &is_required);
    bool is_is_required_Set() const;
    bool is_is_required_Valid() const;

    bool isSenderEmail() const;
    void setSenderEmail(const bool &sender_email);
    bool is_sender_email_Set() const;
    bool is_sender_email_Valid() const;

    bool isUseAsFolderName() const;
    void setUseAsFolderName(const bool &use_as_folder_name);
    bool is_use_as_folder_name_Set() const;
    bool is_use_as_folder_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_required;
    bool m_is_required_isSet;
    bool m_is_required_isValid;

    bool m_sender_email;
    bool m_sender_email_isSet;
    bool m_sender_email_isValid;

    bool m_use_as_folder_name;
    bool m_use_as_folder_name_isSet;
    bool m_use_as_folder_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateFormByIdRequestBody_elements_inner_settings)

#endif // OAIUpdateFormByIdRequestBody_elements_inner_settings_H
