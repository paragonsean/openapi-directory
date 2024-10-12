/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectCreate.h
 *
 * 
 */

#ifndef OAIProjectCreate_H
#define OAIProjectCreate_H

#include <QJsonObject>

#include "OAICustomArticleFieldAdd.h"
#include "OAIFundingCreate.h"
#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomArticleFieldAdd;
class OAIFundingCreate;

class OAIProjectCreate : public OAIObject {
public:
    OAIProjectCreate();
    OAIProjectCreate(QString json);
    ~OAIProjectCreate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QList<OAICustomArticleFieldAdd> getCustomFieldsList() const;
    void setCustomFieldsList(const QList<OAICustomArticleFieldAdd> &custom_fields_list);
    bool is_custom_fields_list_Set() const;
    bool is_custom_fields_list_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getFunding() const;
    void setFunding(const QString &funding);
    bool is_funding_Set() const;
    bool is_funding_Valid() const;

    QList<OAIFundingCreate> getFundingList() const;
    void setFundingList(const QList<OAIFundingCreate> &funding_list);
    bool is_funding_list_Set() const;
    bool is_funding_list_Valid() const;

    qint64 getGroupId() const;
    void setGroupId(const qint64 &group_id);
    bool is_group_id_Set() const;
    bool is_group_id_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QList<OAICustomArticleFieldAdd> m_custom_fields_list;
    bool m_custom_fields_list_isSet;
    bool m_custom_fields_list_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_funding;
    bool m_funding_isSet;
    bool m_funding_isValid;

    QList<OAIFundingCreate> m_funding_list;
    bool m_funding_list_isSet;
    bool m_funding_list_isValid;

    qint64 m_group_id;
    bool m_group_id_isSet;
    bool m_group_id_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectCreate)

#endif // OAIProjectCreate_H
