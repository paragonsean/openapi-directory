/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHybridConnectionCollection.h
 *
 * Collection of hostname bindings.
 */

#ifndef OAIHybridConnectionCollection_H
#define OAIHybridConnectionCollection_H

#include <QJsonObject>

#include "OAIHybridConnectionCollection_value_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIHybridConnectionCollection_value_inner;

class OAIHybridConnectionCollection : public OAIObject {
public:
    OAIHybridConnectionCollection();
    OAIHybridConnectionCollection(QString json);
    ~OAIHybridConnectionCollection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIHybridConnectionCollection_value_inner> getValue() const;
    void setValue(const QList<OAIHybridConnectionCollection_value_inner> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIHybridConnectionCollection_value_inner> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHybridConnectionCollection)

#endif // OAIHybridConnectionCollection_H
