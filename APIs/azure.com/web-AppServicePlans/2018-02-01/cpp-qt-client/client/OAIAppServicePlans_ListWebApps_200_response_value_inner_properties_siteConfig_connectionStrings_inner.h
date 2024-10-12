/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner.h
 *
 * Database connection string information.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getConnectionString() const;
    void setConnectionString(const QString &connection_string);
    bool is_connection_string_Set() const;
    bool is_connection_string_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_connection_string;
    bool m_connection_string_isSet;
    bool m_connection_string_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner_H
