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
 * OAIUserPermissions.h
 *
 * 
 */

#ifndef OAIUserPermissions_H
#define OAIUserPermissions_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUserPermissions : public OAIObject {
public:
    OAIUserPermissions();
    OAIUserPermissions(QString json);
    ~OAIUserPermissions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isChangePassword() const;
    void setChangePassword(const bool &change_password);
    bool is_change_password_Set() const;
    bool is_change_password_Valid() const;

    bool isRDelete() const;
    void setRDelete(const bool &r_delete);
    bool is_r_delete_Set() const;
    bool is_r_delete_Valid() const;

    bool isDeleteFormData() const;
    void setDeleteFormData(const bool &delete_form_data);
    bool is_delete_form_data_Set() const;
    bool is_delete_form_data_Valid() const;

    bool isDownload() const;
    void setDownload(const bool &download);
    bool is_download_Set() const;
    bool is_download_Valid() const;

    bool isList() const;
    void setList(const bool &list);
    bool is_list_Set() const;
    bool is_list_Valid() const;

    bool isModify() const;
    void setModify(const bool &modify);
    bool is_modify_Set() const;
    bool is_modify_Valid() const;

    bool isNotification() const;
    void setNotification(const bool &notification);
    bool is_notification_Set() const;
    bool is_notification_Valid() const;

    bool isShare() const;
    void setShare(const bool &share);
    bool is_share_Set() const;
    bool is_share_Valid() const;

    bool isUpload() const;
    void setUpload(const bool &upload);
    bool is_upload_Set() const;
    bool is_upload_Valid() const;

    bool isViewFormData() const;
    void setViewFormData(const bool &view_form_data);
    bool is_view_form_data_Set() const;
    bool is_view_form_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_change_password;
    bool m_change_password_isSet;
    bool m_change_password_isValid;

    bool m_r_delete;
    bool m_r_delete_isSet;
    bool m_r_delete_isValid;

    bool m_delete_form_data;
    bool m_delete_form_data_isSet;
    bool m_delete_form_data_isValid;

    bool m_download;
    bool m_download_isSet;
    bool m_download_isValid;

    bool m_list;
    bool m_list_isSet;
    bool m_list_isValid;

    bool m_modify;
    bool m_modify_isSet;
    bool m_modify_isValid;

    bool m_notification;
    bool m_notification_isSet;
    bool m_notification_isValid;

    bool m_share;
    bool m_share_isSet;
    bool m_share_isValid;

    bool m_upload;
    bool m_upload_isSet;
    bool m_upload_isValid;

    bool m_view_form_data;
    bool m_view_form_data_isSet;
    bool m_view_form_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserPermissions)

#endif // OAIUserPermissions_H
