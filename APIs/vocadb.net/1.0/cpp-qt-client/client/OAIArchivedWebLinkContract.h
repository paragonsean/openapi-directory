/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArchivedWebLinkContract.h
 *
 * 
 */

#ifndef OAIArchivedWebLinkContract_H
#define OAIArchivedWebLinkContract_H

#include <QJsonObject>

#include "OAIWebLinkCategory.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArchivedWebLinkContract : public OAIObject {
public:
    OAIArchivedWebLinkContract();
    OAIArchivedWebLinkContract(QString json);
    ~OAIArchivedWebLinkContract() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWebLinkCategory getCategory() const;
    void setCategory(const OAIWebLinkCategory &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isDisabled() const;
    void setDisabled(const bool &disabled);
    bool is_disabled_Set() const;
    bool is_disabled_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWebLinkCategory m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_disabled;
    bool m_disabled_isSet;
    bool m_disabled_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArchivedWebLinkContract)

#endif // OAIArchivedWebLinkContract_H
