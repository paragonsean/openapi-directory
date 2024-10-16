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
 * OAIWebhookTriggers_resources.h
 *
 * 
 */

#ifndef OAIWebhookTriggers_resources_H
#define OAIWebhookTriggers_resources_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWebhookTriggers_resources : public OAIObject {
public:
    OAIWebhookTriggers_resources();
    OAIWebhookTriggers_resources(QString json);
    ~OAIWebhookTriggers_resources() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCompress() const;
    void setCompress(const bool &compress);
    bool is_compress_Set() const;
    bool is_compress_Valid() const;

    bool isCopy() const;
    void setCopy(const bool &copy);
    bool is_copy_Set() const;
    bool is_copy_Valid() const;

    bool isCreateFolder() const;
    void setCreateFolder(const bool &create_folder);
    bool is_create_folder_Set() const;
    bool is_create_folder_Valid() const;

    bool isRDelete() const;
    void setRDelete(const bool &r_delete);
    bool is_r_delete_Set() const;
    bool is_r_delete_Valid() const;

    bool isDownload() const;
    void setDownload(const bool &download);
    bool is_download_Set() const;
    bool is_download_Valid() const;

    bool isExtract() const;
    void setExtract(const bool &extract);
    bool is_extract_Set() const;
    bool is_extract_Valid() const;

    bool isMove() const;
    void setMove(const bool &move);
    bool is_move_Set() const;
    bool is_move_Valid() const;

    bool isRename() const;
    void setRename(const bool &rename);
    bool is_rename_Set() const;
    bool is_rename_Valid() const;

    bool isUpload() const;
    void setUpload(const bool &upload);
    bool is_upload_Set() const;
    bool is_upload_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_compress;
    bool m_compress_isSet;
    bool m_compress_isValid;

    bool m_copy;
    bool m_copy_isSet;
    bool m_copy_isValid;

    bool m_create_folder;
    bool m_create_folder_isSet;
    bool m_create_folder_isValid;

    bool m_r_delete;
    bool m_r_delete_isSet;
    bool m_r_delete_isValid;

    bool m_download;
    bool m_download_isSet;
    bool m_download_isValid;

    bool m_extract;
    bool m_extract_isSet;
    bool m_extract_isValid;

    bool m_move;
    bool m_move_isSet;
    bool m_move_isValid;

    bool m_rename;
    bool m_rename_isSet;
    bool m_rename_isValid;

    bool m_upload;
    bool m_upload_isSet;
    bool m_upload_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhookTriggers_resources)

#endif // OAIWebhookTriggers_resources_H
