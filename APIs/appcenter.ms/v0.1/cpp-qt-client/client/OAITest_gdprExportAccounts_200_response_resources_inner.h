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
 * OAITest_gdprExportAccounts_200_response_resources_inner.h
 *
 * 
 */

#ifndef OAITest_gdprExportAccounts_200_response_resources_inner_H
#define OAITest_gdprExportAccounts_200_response_resources_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_gdprExportAccounts_200_response_resources_inner : public OAIObject {
public:
    OAITest_gdprExportAccounts_200_response_resources_inner();
    OAITest_gdprExportAccounts_200_response_resources_inner(QString json);
    ~OAITest_gdprExportAccounts_200_response_resources_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    QString getRel() const;
    void setRel(const QString &rel);
    bool is_rel_Set() const;
    bool is_rel_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    QString m_rel;
    bool m_rel_isSet;
    bool m_rel_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_gdprExportAccounts_200_response_resources_inner)

#endif // OAITest_gdprExportAccounts_200_response_resources_inner_H
