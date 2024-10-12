/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICategory.h
 *
 * Zalando API Category Schema
 */

#ifndef OAICategory_H
#define OAICategory_H

#include <QJsonObject>

#include <QList>
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

    QList<QString> getChildKeys() const;
    void setChildKeys(const QList<QString> &child_keys);
    bool is_child_keys_Set() const;
    bool is_child_keys_Valid() const;

    qint32 getCid() const;
    void setCid(const qint32 &cid);
    bool is_cid_Set() const;
    bool is_cid_Valid() const;

    bool isHidden() const;
    void setHidden(const bool &hidden);
    bool is_hidden_Set() const;
    bool is_hidden_Valid() const;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isOutlet() const;
    void setOutlet(const bool &outlet);
    bool is_outlet_Set() const;
    bool is_outlet_Valid() const;

    QString getParentKey() const;
    void setParentKey(const QString &parent_key);
    bool is_parent_key_Set() const;
    bool is_parent_key_Valid() const;

    QList<QString> getSuggestedFilters() const;
    void setSuggestedFilters(const QList<QString> &suggested_filters);
    bool is_suggested_filters_Set() const;
    bool is_suggested_filters_Valid() const;

    QString getTargetGroup() const;
    void setTargetGroup(const QString &target_group);
    bool is_target_group_Set() const;
    bool is_target_group_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_child_keys;
    bool m_child_keys_isSet;
    bool m_child_keys_isValid;

    qint32 m_cid;
    bool m_cid_isSet;
    bool m_cid_isValid;

    bool m_hidden;
    bool m_hidden_isSet;
    bool m_hidden_isValid;

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_outlet;
    bool m_outlet_isSet;
    bool m_outlet_isValid;

    QString m_parent_key;
    bool m_parent_key_isSet;
    bool m_parent_key_isValid;

    QList<QString> m_suggested_filters;
    bool m_suggested_filters_isSet;
    bool m_suggested_filters_isValid;

    QString m_target_group;
    bool m_target_group_isSet;
    bool m_target_group_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICategory)

#endif // OAICategory_H
