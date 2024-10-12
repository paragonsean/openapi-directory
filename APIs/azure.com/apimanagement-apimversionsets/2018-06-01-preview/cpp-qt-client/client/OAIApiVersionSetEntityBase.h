/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApiVersionSetEntityBase.h
 *
 * Api Version set base parameters
 */

#ifndef OAIApiVersionSetEntityBase_H
#define OAIApiVersionSetEntityBase_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApiVersionSetEntityBase : public OAIObject {
public:
    OAIApiVersionSetEntityBase();
    OAIApiVersionSetEntityBase(QString json);
    ~OAIApiVersionSetEntityBase() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getVersionHeaderName() const;
    void setVersionHeaderName(const QString &version_header_name);
    bool is_version_header_name_Set() const;
    bool is_version_header_name_Valid() const;

    QString getVersionQueryName() const;
    void setVersionQueryName(const QString &version_query_name);
    bool is_version_query_name_Set() const;
    bool is_version_query_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_version_header_name;
    bool m_version_header_name_isSet;
    bool m_version_header_name_isValid;

    QString m_version_query_name;
    bool m_version_query_name_isSet;
    bool m_version_query_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApiVersionSetEntityBase)

#endif // OAIApiVersionSetEntityBase_H
