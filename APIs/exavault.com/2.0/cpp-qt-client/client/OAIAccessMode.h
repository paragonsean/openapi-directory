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
 * OAIAccessMode.h
 *
 * An object defining what a not-logged-in visitor can do with the share contents
 */

#ifndef OAIAccessMode_H
#define OAIAccessMode_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccessMode : public OAIObject {
public:
    OAIAccessMode();
    OAIAccessMode(QString json);
    ~OAIAccessMode() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isRDelete() const;
    void setRDelete(const bool &r_delete);
    bool is_r_delete_Set() const;
    bool is_r_delete_Valid() const;

    bool isDownload() const;
    void setDownload(const bool &download);
    bool is_download_Set() const;
    bool is_download_Valid() const;

    bool isModify() const;
    void setModify(const bool &modify);
    bool is_modify_Set() const;
    bool is_modify_Valid() const;

    bool isUpload() const;
    void setUpload(const bool &upload);
    bool is_upload_Set() const;
    bool is_upload_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_r_delete;
    bool m_r_delete_isSet;
    bool m_r_delete_isValid;

    bool m_download;
    bool m_download_isSet;
    bool m_download_isValid;

    bool m_modify;
    bool m_modify_isSet;
    bool m_modify_isValid;

    bool m_upload;
    bool m_upload_isSet;
    bool m_upload_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccessMode)

#endif // OAIAccessMode_H
