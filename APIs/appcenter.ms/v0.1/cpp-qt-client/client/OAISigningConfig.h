/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISigningConfig.h
 *
 * 
 */

#ifndef OAISigningConfig_H
#define OAISigningConfig_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISigningConfig : public OAIObject {
public:
    OAISigningConfig();
    OAISigningConfig(QString json);
    ~OAISigningConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isHasStoreFile() const;
    void setHasStoreFile(const bool &has_store_file);
    bool is_has_store_file_Set() const;
    bool is_has_store_file_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_has_store_file;
    bool m_has_store_file_isSet;
    bool m_has_store_file_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISigningConfig)

#endif // OAISigningConfig_H
