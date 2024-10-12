/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateEncryptionConfig.h
 *
 * The encryption configuration used to update a user managed Key Vault key.
 */

#ifndef OAIUpdateEncryptionConfig_H
#define OAIUpdateEncryptionConfig_H

#include <QJsonObject>

#include "OAIUpdateKeyVaultMetaInfo.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateKeyVaultMetaInfo;

class OAIUpdateEncryptionConfig : public OAIObject {
public:
    OAIUpdateEncryptionConfig();
    OAIUpdateEncryptionConfig(QString json);
    ~OAIUpdateEncryptionConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIUpdateKeyVaultMetaInfo getKeyVaultMetaInfo() const;
    void setKeyVaultMetaInfo(const OAIUpdateKeyVaultMetaInfo &key_vault_meta_info);
    bool is_key_vault_meta_info_Set() const;
    bool is_key_vault_meta_info_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIUpdateKeyVaultMetaInfo m_key_vault_meta_info;
    bool m_key_vault_meta_info_isSet;
    bool m_key_vault_meta_info_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateEncryptionConfig)

#endif // OAIUpdateEncryptionConfig_H
