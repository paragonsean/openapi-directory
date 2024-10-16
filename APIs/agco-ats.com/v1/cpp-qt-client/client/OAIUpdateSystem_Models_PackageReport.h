/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateSystem_Models_PackageReport.h
 *
 * 
 */

#ifndef OAIUpdateSystem_Models_PackageReport_H
#define OAIUpdateSystem_Models_PackageReport_H

#include <QJsonObject>

#include "OAIUpdateSystem_Models_Category.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateSystem_Models_Category;

class OAIUpdateSystem_Models_PackageReport : public OAIObject {
public:
    OAIUpdateSystem_Models_PackageReport();
    OAIUpdateSystem_Models_PackageReport(QString json);
    ~OAIUpdateSystem_Models_PackageReport() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIUpdateSystem_Models_Category> getCategories() const;
    void setCategories(const QList<OAIUpdateSystem_Models_Category> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    QString getPackageDescription() const;
    void setPackageDescription(const QString &package_description);
    bool is_package_description_Set() const;
    bool is_package_description_Valid() const;

    QString getPackageId() const;
    void setPackageId(const QString &package_id);
    bool is_package_id_Set() const;
    bool is_package_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIUpdateSystem_Models_Category> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    QString m_package_description;
    bool m_package_description_isSet;
    bool m_package_description_isValid;

    QString m_package_id;
    bool m_package_id_isSet;
    bool m_package_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateSystem_Models_PackageReport)

#endif // OAIUpdateSystem_Models_PackageReport_H
