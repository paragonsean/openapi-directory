/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories.h
 *
 * Settings for blocked URL categories
 */

#ifndef OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories_H
#define OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories : public OAIObject {
public:
    OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories();
    OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories(QString json);
    ~OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getCategories() const;
    void setCategories(const QList<QString> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    QString getSettings() const;
    void setSettings(const QString &settings);
    bool is_settings_Set() const;
    bool is_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    QString m_settings;
    bool m_settings_isSet;
    bool m_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories)

#endif // OAICreateNetworkGroupPolicy_request_contentFiltering_blockedUrlCategories_H
