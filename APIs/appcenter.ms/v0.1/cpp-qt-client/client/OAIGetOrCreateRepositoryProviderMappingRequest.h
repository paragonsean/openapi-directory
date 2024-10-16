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
 * OAIGetOrCreateRepositoryProviderMappingRequest.h
 *
 * 
 */

#ifndef OAIGetOrCreateRepositoryProviderMappingRequest_H
#define OAIGetOrCreateRepositoryProviderMappingRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetOrCreateRepositoryProviderMappingRequest : public OAIObject {
public:
    OAIGetOrCreateRepositoryProviderMappingRequest();
    OAIGetOrCreateRepositoryProviderMappingRequest(QString json);
    ~OAIGetOrCreateRepositoryProviderMappingRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getExternalAccountName() const;
    void setExternalAccountName(const QString &external_account_name);
    bool is_external_account_name_Set() const;
    bool is_external_account_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_external_account_name;
    bool m_external_account_name_isSet;
    bool m_external_account_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrCreateRepositoryProviderMappingRequest)

#endif // OAIGetOrCreateRepositoryProviderMappingRequest_H
