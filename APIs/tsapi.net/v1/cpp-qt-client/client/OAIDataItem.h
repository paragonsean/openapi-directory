/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDataItem.h
 *
 * 
 */

#ifndef OAIDataItem_H
#define OAIDataItem_H

#include <QJsonObject>

#include "OAIParentRef.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIParentRef;

class OAIDataItem : public OAIObject {
public:
    OAIDataItem();
    OAIDataItem(QString json);
    ~OAIDataItem() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIdent() const;
    void setIdent(const QString &ident);
    bool is_ident_Set() const;
    bool is_ident_Valid() const;

    OAIParentRef getParentIdent() const;
    void setParentIdent(const OAIParentRef &parent_ident);
    bool is_parent_ident_Set() const;
    bool is_parent_ident_Valid() const;

    QList<QString> getValues() const;
    void setValues(const QList<QString> &values);
    bool is_values_Set() const;
    bool is_values_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ident;
    bool m_ident_isSet;
    bool m_ident_isValid;

    OAIParentRef m_parent_ident;
    bool m_parent_ident_isSet;
    bool m_parent_ident_isValid;

    QList<QString> m_values;
    bool m_values_isSet;
    bool m_values_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDataItem)

#endif // OAIDataItem_H
