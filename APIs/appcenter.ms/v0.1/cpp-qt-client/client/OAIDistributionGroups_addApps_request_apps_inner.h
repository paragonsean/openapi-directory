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
 * OAIDistributionGroups_addApps_request_apps_inner.h
 *
 * 
 */

#ifndef OAIDistributionGroups_addApps_request_apps_inner_H
#define OAIDistributionGroups_addApps_request_apps_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDistributionGroups_addApps_request_apps_inner : public OAIObject {
public:
    OAIDistributionGroups_addApps_request_apps_inner();
    OAIDistributionGroups_addApps_request_apps_inner(QString json);
    ~OAIDistributionGroups_addApps_request_apps_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDistributionGroups_addApps_request_apps_inner)

#endif // OAIDistributionGroups_addApps_request_apps_inner_H
