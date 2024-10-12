/**
 * Security Center
 * API spec for Microsoft.Security (Azure Security Center) resource provider
 *
 * The version of the OpenAPI document: 2017-08-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWorkspaceSettings_List_default_response.h
 *
 * Error response structure.
 */

#ifndef OAIWorkspaceSettings_List_default_response_H
#define OAIWorkspaceSettings_List_default_response_H

#include <QJsonObject>

#include "OAIWorkspaceSettings_List_default_response_error.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWorkspaceSettings_List_default_response_error;

class OAIWorkspaceSettings_List_default_response : public OAIObject {
public:
    OAIWorkspaceSettings_List_default_response();
    OAIWorkspaceSettings_List_default_response(QString json);
    ~OAIWorkspaceSettings_List_default_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWorkspaceSettings_List_default_response_error getError() const;
    void setError(const OAIWorkspaceSettings_List_default_response_error &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWorkspaceSettings_List_default_response_error m_error;
    bool m_error_isSet;
    bool m_error_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWorkspaceSettings_List_default_response)

#endif // OAIWorkspaceSettings_List_default_response_H
