/**
 * Transportation Laws and Incentives
 * Query our database of federal and state laws and incentives for alternative fuels and vehicles, air quality, fuel efficiency, and other transportation-related topics. This dataset powers the <a href=\"https://afdc.energy.gov/laws\">Federal and State Laws and Incentives</a> on the Alternative Fuels Data Center.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICategory.h
 *
 * A category that the law applies to
 */

#ifndef OAICategory_H
#define OAICategory_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICategory : public OAIObject {
public:
    OAICategory();
    OAICategory(QString json);
    ~OAICategory() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCategoryType() const;
    void setCategoryType(const QString &category_type);
    bool is_category_type_Set() const;
    bool is_category_type_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_category_type;
    bool m_category_type_isSet;
    bool m_category_type_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICategory)

#endif // OAICategory_H
