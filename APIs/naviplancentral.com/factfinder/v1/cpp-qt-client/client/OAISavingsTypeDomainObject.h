/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISavingsTypeDomainObject.h
 *
 * 
 */

#ifndef OAISavingsTypeDomainObject_H
#define OAISavingsTypeDomainObject_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISavingsTypeDomainObject : public OAIObject {
public:
    OAISavingsTypeDomainObject();
    OAISavingsTypeDomainObject(QString json);
    ~OAISavingsTypeDomainObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getTypeName() const;
    void setTypeName(const QString &type_name);
    bool is_type_name_Set() const;
    bool is_type_name_Valid() const;

    QList<QString> getValidAmountTypes() const;
    void setValidAmountTypes(const QList<QString> &valid_amount_types);
    bool is_valid_amount_types_Set() const;
    bool is_valid_amount_types_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_type_name;
    bool m_type_name_isSet;
    bool m_type_name_isValid;

    QList<QString> m_valid_amount_types;
    bool m_valid_amount_types_isSet;
    bool m_valid_amount_types_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISavingsTypeDomainObject)

#endif // OAISavingsTypeDomainObject_H
